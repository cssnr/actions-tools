import json
import os
import random
import re
import string
from contextlib import contextmanager
from typing import Any, List, Optional
from urllib.parse import quote
from urllib.request import Request, urlopen

from yaml import Loader, YAMLError, load


try:
    # noinspection PyUnresolvedReferences
    from github import Auth, Github
except ImportError:  # pragma: no cover
    _has_github = False
else:
    _has_github = True


# from . import context as ctx

# https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands


_true = ["y", "yes", "true", "on"]
_false = ["n", "no", "false", "off"]

_indent = 0
_end_token = ""


# context = ctx


# Core


def debug(message: str, **kwargs):
    """
    Send a Debug message
    https://docs.github.com/en/actions/how-tos/monitor-workflows/enable-debug-logging
    :param message: Message
    :param kwargs: Extra print kwargs
    """
    print(f"::debug::{message}", **kwargs)


def info(message: str, **kwargs):
    """
    Send an Info message
    :param message: Message
    :param kwargs: Extra print kwargs
    """
    print(" " * _indent + message, **kwargs)


def notice(message: str, **kwargs):
    """
    Send a Notice message
    https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#setting-a-notice-message
    :param message: Message
    :param kwargs: Notice options and print kwargs
    """
    cmd_args = _cmd_args(kwargs)
    print(f"::notice{cmd_args}::{message}", **kwargs)


def warn(message: str, **kwargs):
    """
    Send a Warning message
    https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#setting-a-warning-message
    :param message: Message
    :param kwargs: Warning options and print kwargs
    """
    cmd_args = _cmd_args(kwargs)
    print(f"::warning{cmd_args}::{message}", **kwargs)


def error(message: str, **kwargs):
    """
    Send an Error message
    https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#setting-an-error-message
    :param message: Message
    :param kwargs: Error options and print kwargs
    """
    cmd_args = _cmd_args(kwargs)
    print(f"::error{cmd_args}::{message}")


def _cmd_args(kwargs) -> str:
    keys = ["title", "file", "col", "endColumn", "line", "endLine"]
    results = []
    items = kwargs.copy()
    for key, value in items.items():
        if key not in keys:
            continue
        value = str(value).replace(":", "%3A").replace(",", "%2C")
        results.append(f"{key}={value}")
        del kwargs[key]
    result = ",".join(results)
    return f" {result}" if result else ""


def is_debug() -> bool:
    return bool(os.getenv("RUNNER_DEBUG"))


def set_failed(message: str):
    error(message)
    raise SystemExit


def mask(message: str):
    """
    Mask a secret
    https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#masking-a-value-in-a-log
    :param message: Secret to mask
    """
    print(f"::add-mask::{message}")


def start_group(title: str):
    print(f"::group::{title}")


def end_group():
    print("::endgroup::")


@contextmanager
def group(title: str):
    print(f"::group::{title}")
    try:
        yield info
    finally:
        print("::endgroup::")


def stop_commands(end_token: str = ""):
    global _end_token
    if not end_token:
        r = random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16)
        end_token = "".join(r)
    _end_token = end_token
    print(f"::stop-commands::{_end_token}")


def start_commands(end_token: str = ""):
    if not end_token:
        end_token = _end_token
    print(f"::{end_token}::")


def set_output(output: str, value: Any):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        print(f"{output}={value}", file=f)  # type: ignore


def set_env(name: str, value: str):
    with open(os.environ["GITHUB_ENV"], "a") as f:
        print(f"{name}={value}", file=f)  # type: ignore


def add_path(path: str):
    with open(os.environ["GITHUB_PATH"], "a") as f:
        print(path, file=f)  # type: ignore


def set_state(name: str, value: Any) -> str:
    if name.startswith("STATE_"):
        name = name[6:]
    with open(os.environ["GITHUB_STATE"], "a") as f:
        print(f"{name}={value}", file=f)  # type: ignore
    return f"STATE_{name}"


def get_state(name: str) -> str:
    if name.startswith("STATE_"):
        name = name[6:]
    return os.getenv(f"STATE_{name}", "")


def summary(text: str, nlc: int = 1):
    """
    Write to the Job Summary file
    https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#adding-a-job-summary
    :param text:str: Raw Text
    :param nlc:int: New Line Count
    :return:
    """
    new_lines = os.linesep * nlc
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
        print(f"{text}{new_lines}", file=f)  # type: ignore


# Inputs


def get_input(name: str, req: bool = False, strip: bool = True) -> str:
    """
    Get String Input
    :param name: str: Input Name
    :param req: bool: If Required
    :param strip: bool: To Strip
    :return:
    """
    value: str = _get_input_str(name, strip)
    if req and not value:
        raise ValueError(f"Error Parsing Required Input: {name} -> {value}")
    return value


def get_bool(name: str, req: bool = False) -> bool:
    """
    Get Boolean Input
    :param name: str: Input Name
    :param req: bool: If Required
    :return:
    """
    value = _get_input_str(name, True).lower()
    if req and value not in _true + _false:
        raise ValueError(f"Error Parsing Required Input: {name} -> {value}")
    if value in _true:
        return True
    return False


def get_list(name: str, req: bool = False, strip: bool = True, split: str = "[,|\n]") -> List[str]:
    """
    Get List Input
    :param name: str: Input Name
    :param req: bool: If Required
    :param strip: bool: To Strip
    :param split: str: Split Regex
    :return:
    """
    value = _get_input_str(name, True)
    if req and not value:
        raise ValueError(f"Error Parsing Required Input: {name} -> {value}")
    results: List[str] = []
    for x in re.split(split, value):
        if strip:
            x = x.strip()
        if x:
            results.append(x)
    return results


def get_dict(name: str, req=False) -> dict:
    """
    Get Dict Input - from JSON or YAML String
    TODO: This function can return Any
    :param name: str: Input Name
    :param req: bool: If Required
    :return:
    """
    value = _get_input_str(name, True)
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        pass
    try:
        res = load(value, Loader=Loader)
        if res:
            return res
    except YAMLError:
        pass
    if req:
        raise ValueError(f"Error Parsing Required Input: {name} -> {repr(value)}")
    return {}


def _get_input_str(name: str, strip: bool = True) -> str:
    value = os.getenv(f"INPUT_{name.upper()}", "")
    if strip:
        value = value.strip()
    return value


# OIDC
# https://docs.github.com/en/actions/reference/security/oidc#methods-for-requesting-the-oidc-token


def get_id_token(audience: Optional[str] = None) -> str:
    """
    Get and mask OIDC Token
    :param audience:
    :return:
    """
    tip = "Check permissions: id-token"
    request_url = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
    if not request_url:
        raise ValueError(f"No ACTIONS_ID_TOKEN_REQUEST_URL - {tip}")
    request_token = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
    if not request_token:
        raise ValueError(f"No ACTIONS_ID_TOKEN_REQUEST_TOKEN - {tip}")
    if audience:
        # request_url += f"&audience={quote(audience)}"
        sep = "&" if "?" in request_url else "?"
        request_url += f"{sep}audience={quote(audience)}"

    request = Request(request_url)
    request.add_header("Authorization", f"bearer {request_token}")
    response = urlopen(request)
    # code = response.getcode()
    # if not 199 < code < 300:
    #     raise ValueError(f"Invalid response code: {code} - {tip}")
    content = response.read().decode()
    # print(f"content: {content}")
    data = json.loads(content)
    value = data.get("value")
    if not value:
        raise ValueError(f"No ID Token in response - {tip}")
    mask(value)
    return value


# PyGithub


def get_github(token: str, **kwargs) -> Github:
    """
    Get Github from PyGithub
    :param token: GitHub Token
    :param kwargs: PyGithub kwargs
    :return:
    """
    if not _has_github:  # pragma: no cover
        raise ImportError("Install actions-tools[github] or PyGithub")
    return Github(auth=Auth.Token(token), **kwargs)


# Additional


def get_event(path: Optional[str] = None) -> dict:
    with open(path or os.environ["GITHUB_EVENT_PATH"]) as f:
        return json.load(f)


def get_version(fallback: str = "Source") -> str:
    workflow_ref: str = os.environ.get("GITHUB_WORKFLOW_REF", "")
    if workflow_ref:
        return workflow_ref.rsplit("/", 1)[-1]
    return fallback


def get_random(length: int = 16) -> str:
    r = random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length)
    return "".join(r)


def command(name: str, value: str = "", **kwargs):
    cmd_args = _cmd_args(kwargs)
    print(f"::{name}{cmd_args}::{value}", **kwargs)


def start_indent(spaces: int = 2):
    global _indent
    _indent = spaces


def end_indent():
    global _indent
    _indent = 0

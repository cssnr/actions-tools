import json
import os
import random
import re
import string
from contextlib import contextmanager
from typing import List, Optional

from yaml import Loader, load


# from . import context as ctx


# https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands


_true = ["y", "yes", "true", "on"]
_false = ["n", "no", "false", "off"]

_indent = 0
_endtoken = ""


# context = ctx


# Core


def debug(message: str, *args, **kwargs):
    print(f"::debug::{message}", *args, **kwargs)


def info(message: str, *args, **kwargs):
    print(" " * _indent + message, *args, **kwargs)


def notice(message: str, *args, **kwargs):
    print(f"::notice::{message}", *args, **kwargs)


def warn(message: str, *args, **kwargs):
    print(f"::warning::{message}", *args, **kwargs)


def error(message: str, *args, **kwargs):
    print(f"::error::{message}", *args, **kwargs)


def is_debug() -> bool:
    return bool(os.getenv("RUNNER_DEBUG"))


def set_failed(message: str):
    error(message)
    raise SystemExit


def mask(message: str):
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


def stop_commands(endtoken: str = ""):
    global _endtoken
    if not endtoken:
        r = random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16)
        endtoken = "".join(r)
    _endtoken = endtoken
    print(f"::stop-commands::{_endtoken}")


def start_commands(endtoken: str = ""):
    if not endtoken:
        endtoken = _endtoken
    print(f"::{endtoken}::")


def set_output(output: str, value: str):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        print(f"{output}={value}", file=f)  # type: ignore


def set_env(name: str, value: str):
    with open(os.environ["GITHUB_ENV"], "a") as f:
        print(f"{name}={value}", file=f)  # type: ignore


def add_path(path: str):
    with open(os.environ["GITHUB_PATH"], "a") as f:
        print(path, file=f)  # type: ignore


def set_state(name: str, value: str) -> str:
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
    NOTE: Make this its own module
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
    Get Input by Name
    :param name: str: Input Name
    :param req: bool: If Required
    :param strip: bool: To Strip
    :return: str
    """
    value = os.getenv(f"INPUT_{name.upper()}", "")
    value = _get_str_value(value, strip)
    if req and not value:
        raise ValueError(f"Error Parsing Required Input: {name} -> {value}")
    return value


def get_list(name: str, req: bool = False, strip: bool = True, split: str = "[,|\n]") -> List[str]:
    """
    Get Input by Name
    :param name: str: Input Name
    :param req: bool: If Required
    :param strip: bool: To Strip
    :param split: str: Split Regex
    :return: list
    """
    value = os.getenv(f"INPUT_{name.upper()}", "")
    value = _get_str_value(value, strip)
    if req and not value.strip():
        raise ValueError(f"Error Parsing Required Input: {name} -> {value}")
    results = []
    for x in re.split(split, value):
        results.append(_get_str_value(x, strip))
    return results


def get_bool(name: str, req: bool = False) -> bool:
    """
    Get Boolean Input by Name
    :param name: str: Input Name
    :param req: bool: If Required
    :return: bool
    """
    value = os.getenv(f"INPUT_{name.upper()}", "").strip().lower()
    if req and value not in _true + _false:
        raise ValueError(f"Error Parsing Required Input: {name} -> {value}")
    if value in _true:
        return True
    return False


def _get_str_value(value, strip: bool = True) -> str:
    if strip:
        value = value.strip()
    return value


# Additional


def get_data(name: str, req=False) -> dict:
    """
    Get JSON/YAML Data by Name
    :param name: str: Input Name
    :param req: bool: If Required
    :return: dict
    """
    value = os.getenv(f"INPUT_{name.upper()}", "")
    value = _get_str_value(value)
    try:
        return json.loads(value)
    except Exception as e:
        print(f"::debug::{e}")
    try:
        res = load(value, Loader=Loader)
        if res:
            return res
    except Exception as e:
        print(f"::debug::{e}")
    if req:
        raise ValueError(f"Error Parsing Required Input: {name} -> {repr(value)}")
    return {}


def get_event(path: Optional[str] = None) -> dict:
    with open(path or os.environ["GITHUB_EVENT_PATH"]) as f:
        return json.load(f)


def get_random(length: int = 16) -> str:
    r = random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length)
    return "".join(r)


def get_version(fallback: str = "Source") -> str:
    workflow_ref: str = os.environ.get("GITHUB_WORKFLOW_REF", "")
    print(f"GITHUB_WORKFLOW_REF: {workflow_ref}")
    if workflow_ref:
        return workflow_ref.rsplit("/", 1)[-1]
    return fallback


def command(name: str, value: str = ""):
    print(f"::{name}::{value}")


def start_indent(spaces: int = 2):
    global _indent
    _indent = spaces


def end_indent():
    global _indent
    _indent = 0

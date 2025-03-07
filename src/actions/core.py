import os
import random
import re
import string
from contextlib import contextmanager
from typing import List, Optional


# https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions


_true = ["y", "yes", "true", "on"]
_false = ["n", "no", "false", "off"]

_indent = 0
_endtoken = ""


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
def with_group(title: str):
    print(f"::group::{title}")
    try:
        yield info
    finally:
        print("::endgroup::")


def stop_commands(endtoken: str = ""):
    global _endtoken
    if not endtoken:
        r = random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16)  # NOSONAR
        endtoken = "".join(r)
    _endtoken = endtoken
    print(f"::stop-commands::{_endtoken}")


def start_commands(endtoken: str = ""):
    global _endtoken
    if not endtoken:
        endtoken = _endtoken
    print(f"::{endtoken}::")


def set_output(output: str, value: str):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        # noinspection PyTypeChecker
        print(f"{output}={value}", file=f)


def set_env(name: str, value: str):
    with open(os.environ["GITHUB_ENV"], "a") as f:
        # noinspection PyTypeChecker
        print(f"{name}={value}", file=f)


def add_path(path: str):
    with open(os.environ["GITHUB_PATH"], "a") as f:
        # noinspection PyTypeChecker
        print(path, file=f)


def set_state(name: str, value: str) -> str:
    if name.startswith("STATE_"):
        name = name[6:]
    with open(os.environ["GITHUB_STATE"], "a") as f:
        # noinspection PyTypeChecker
        print(f"{name}={value}", file=f)
    return f"STATE_{name}"


def get_state(name: str) -> str:
    if name.startswith("STATE_"):
        name = name[6:]
    return os.getenv(f"STATE_{name}", "")


def summary(text: str, nlc=1):
    """
    TODO: Make this its own module
    :param text:str: Raw Text
    :param nlc:int: New Line Count
    :return:
    """
    new_lines = os.linesep * nlc
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
        # noinspection PyTypeChecker
        print(f"{text}{new_lines}", file=f)


# Inputs


def get_input(name: str, req=False, low=False, strip=True) -> str:
    """
    Get Input by Name
    :param name: str: Input Name
    :param req: bool: If Required
    :param low: bool: To Lower
    :param strip: bool: To Strip
    :return: str
    """
    value = os.getenv(f"INPUT_{name.upper()}", "")
    value = _get_str_value(value, strip, low)
    if req and not value:
        raise ValueError(f"Error Parsing Required Input: {name} -> {value}")
    return value


def get_list(name: str, split: str = "[,|\n]", req=False, low=False, strip=True) -> List[str]:
    """
    Get Input by Name
    :param name: str: Input Name
    :param split: str: Split Regex
    :param req: bool: If Required
    :param strip: bool: To Strip
    :param low: bool: To Lowercase
    :return: list
    """
    value = os.getenv(f"INPUT_{name.upper()}", "")
    value = _get_str_value(value, strip, low)
    if req and not value.strip():
        raise ValueError(f"Error Parsing Required Input: {name} -> {value}")
    results = []
    for x in re.split(split, value):
        results.append(_get_str_value(x, strip, low))
    return results


def get_bool(name: str, req=False) -> bool:
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


def _get_str_value(value, strip=True, low=False) -> str:
    if strip:
        value = value.strip()
    if low:
        value = value.lower()
    return value


# Additional


def command(name: str, value: Optional[str] = ""):
    print(f"::{name}::{value}")


def get_random(length: int = 16) -> str:
    r = random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length)  # NOSONAR
    return "".join(r)


def start_indent(spaces: int = 2):
    global _indent
    _indent = spaces


def end_indent():
    global _indent
    _indent = 0

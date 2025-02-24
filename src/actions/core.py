import os
import re
from typing import Union


true = ["y", "yes", "true", "on"]
false = ["n", "no", "false", "off"]

_indent = 0


def debug(message: str):
    print(f"::debug::{message}")


def info(message: str, **kwargs):
    print(" " * _indent + message, **kwargs)


def notice(message: str):
    print(f"::notice::{message}")


def warn(message: str):
    print(f"::warning::{message}")


def error(message: str):
    """
    TODO: Add error options
    https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#setting-an-error-message
    """
    print(f"::error::{message}")


def set_failed(message: str):
    error(message)
    raise SystemExit


def mask(message: str):
    print(f"::add-mask::{message}")


def start_group(title: str):
    print(f"::group::{title}")


def end_group():
    print("::endgroup::")


def start_indent(spaces: int):
    global _indent
    _indent = spaces


def end_indent():
    global _indent
    _indent = 0


def set_output(output: str, value: str):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        print(f"{output}={value}", file=f)


def set_env(var: str, value: str):
    with open(os.environ["GITHUB_ENV"], "a") as f:
        print(f"{var}={value}", file=f)


def summary(text: str, nlc=1):
    """
    TODO: Make this its own module
    :param text:str: Raw Text
    :param nlc:int: New Line Count
    :return:
    """
    new_lines = "\n" * nlc
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
        print(f"{text}{new_lines}", file=f)


def debug(message: str):
    print(f"::debug::{message}")


def info(message: str):
    print(f"::notice::{message}")


def warn(message: str):
    print(f"::warning::{message}")


def error(message: str):
    """
    TODO: Add error options
    https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#setting-an-error-message
    """
    print(f"::error::{message}")


def set_failed(message: str):
    error(message)
    raise SystemExit


def mask(message: str):
    print(f"::add-mask::{message}")


def start_group(title: str):
    print(f"::group::{title}")


def end_group():
    print("::endgroup::")


def set_output(output: str, value: str):
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        print(f"{output}={value}", file=f)


def set_env(var: str, value: str):
    with open(os.environ["GITHUB_ENV"], "a") as f:
        print(f"{var}={value}", file=f)


def summary(text: str, nlc=1):
    """
    TODO: Make this its own module
    :param text:str: Raw Text
    :param nlc:int: New Line Count
    :return:
    """
    new_lines = "\n" * nlc
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
        print(f"{text}{new_lines}", file=f)


def get_input(name: str, req=False, low=False, strip=True, boolean=False, split="") -> Union[str, bool, list]:
    """
    Get Input by Name
    :param name: str: Input Name
    :param req: bool: If Required
    :param low: bool: To Lower
    :param strip: bool: To Strip
    :param boolean: bool: If Boolean
    :param split: str: To Split
    :return: Union[str, bool, list]
    """
    value = os.environ.get(f"INPUT_{name.upper()}", "")
    if boolean:
        value = value.strip().lower()
        if req and value not in true + false:
            raise ValueError(f"Error Validating a Required Boolean Input: {name}")
        if value in ["y", "yes", "true", "on"]:
            return True
        return False

    if split:
        result = []
        for x in re.split(split, value):
            result.append(_get_str_value(x, low, strip))
        return result

    value = _get_str_value(value, low, strip)
    if req and not value:
        raise ValueError(f"Error Parsing a Required Input: {name}")
    return value


def _get_str_value(value, low=False, strip=True):
    if strip:
        value = value.strip()
    if low:
        value = value.lower()
    return value

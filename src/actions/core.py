import os
import re
from typing import Union


true = ["y", "yes", "true", "on"]
false = ["n", "no", "false", "off"]


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
        l = []
        for x in re.split(split, value):
            l.append(_get_str_value(x, low, strip))
        return l

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

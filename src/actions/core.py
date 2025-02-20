import os
from typing import Union
from . import __version__


true = ["y", "yes", "true", "on"]
false = ["n", "no", "false", "off"]


def get_input(name: str, strip=True, low=False, boolean=False) -> Union[str, bool]:
    value = os.environ.get(f"INPUT_{name.upper()}", "")
    if boolean:
        value = value.strip().lower()
        if value not in true + false:
            raise ValueError(f"Unable to Validate a Boolean Input: {name}")
        if value in ["y", "yes", "true", "on"]:
            return True
        return False
    if trim:
        value = value.strip()
    if low:
        value = value.lower()
    return value

import os

import pytest

from actions import core


os.environ["INPUT_TEST"] = " TRUE "


def test_print():
    core.debug("debug")
    core.info("info")
    core.notice("notice")
    core.warn("warn")
    with pytest.raises(SystemExit):
        core.set_failed("test")
    core.mask("test")
    core.start_group("test")
    core.end_group()
    core.start_indent(5)
    core.info("indent")
    core.end_indent()
    core.info("dedent")


def test_outputs():
    if not os.environ.get("GITHUB_OUTPUT"):
        os.environ["GITHUB_OUTPUT"] = "output.txt"
    core.set_output("test", "value")
    if not os.environ.get("GITHUB_ENV"):
        os.environ["GITHUB_ENV"] = "output.txt"
    core.set_env("test", "value")
    if not os.environ.get("GITHUB_STEP_SUMMARY"):
        os.environ["GITHUB_STEP_SUMMARY"] = "output.txt"
    core.summary("test")


def test_inputs():
    assert core.get_input("test") == os.environ["INPUT_TEST"].strip()
    assert core.get_input("test", low=True) == os.environ["INPUT_TEST"].strip().lower()
    assert core.get_input("test", strip=False) == os.environ["INPUT_TEST"]
    assert core.get_input("test", boolean=True)
    assert isinstance(core.get_input("test", split="\n"), list)
    assert len(core.get_input("test", split="\n")) == 1

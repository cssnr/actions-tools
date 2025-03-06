import os

import pytest

from actions import core


os.environ["INPUT_TEST"] = " TRUE "
os.environ["GITHUB_OUTPUT"] = os.environ.get("GITHUB_OUTPUT") or "output.txt"
os.environ["GITHUB_ENV"] = os.environ.get("GITHUB_ENV") or "output.txt"
os.environ["GITHUB_PATH"] = os.environ.get("GITHUB_PATH") or "output.txt"
os.environ["GITHUB_STEP_SUMMARY"] = os.environ.get("GITHUB_STEP_SUMMARY") or "output.txt"


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
    core.start_indent()
    core.info("indent")
    core.end_indent()
    core.info("dedent")
    core.stop_commands()
    core.info("::warning::Just kidding")
    core.start_commands()
    with core.with_group("With Group") as p:
        print("with group")
        p("core.info")
    print("no group")


def test_outputs():
    core.set_output("test", "value")
    core.set_env("test", "value")
    core.summary("test")
    core.add_path("/dev/null")


def test_inputs():
    assert core.get_input("test") == os.environ["INPUT_TEST"].strip()
    assert core.get_input("test", low=True) == os.environ["INPUT_TEST"].strip().lower()
    assert core.get_input("test", strip=False) == os.environ["INPUT_TEST"]
    assert core.get_input("test", boolean=True)
    with pytest.raises(ValueError):
        core.get_input("asdf", boolean=True, req=True)
    assert isinstance(core.get_input("test", split="\n"), list)
    assert len(core.get_input("test", split="\n")) == 1


def test_getters():
    assert len(core.get_random(20)) == 20

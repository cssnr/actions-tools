import os

from actions import core


os.environ["INPUT_TEST"] = " TRUE "


def test_inputs():
    assert core.get_input("test") == os.environ["INPUT_TEST"].strip()
    assert core.get_input("test", low=True) == os.environ["INPUT_TEST"].strip().lower()
    assert core.get_input("test", strip=False) == os.environ["INPUT_TEST"]
    assert core.get_input("test", boolean=True)
    assert isinstance(core.get_input("test", split="\n"), list)
    assert len(core.get_input("test", split="\n")) == 1


def test_outputs():
    if not os.environ.get("GITHUB_OUTPUT"):
        os.environ["GITHUB_OUTPUT"] = "output.txt"
        if os.path.exists(os.environ["GITHUB_OUTPUT"]):
            os.remove(os.environ["GITHUB_OUTPUT"])
    core.set_output("test", "winning")

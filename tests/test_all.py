import os
from actions import core

os.environ["INPUT_TEST"] = " TRUE "


def test_inputs():
    assert core.get_input("test") == os.environ["INPUT_TEST"].strip()
    assert core.get_input("test", low=True) == os.environ["INPUT_TEST"].strip().lower()
    assert core.get_input("test", strip=False) == os.environ["INPUT_TEST"]
    assert core.get_input("test", boolean=True) == True
    assert isinstance(core.get_input("test", split="\n"), list)
    assert len(core.get_input("test", split="\n")) == 1

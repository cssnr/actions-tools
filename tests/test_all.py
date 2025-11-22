import os
from pathlib import Path

import pytest

from actions import context, core


cwd = Path(__file__).resolve().parent

os.environ["INPUT_TEST"] = " TRUE "
os.environ["INPUT_FALSE"] = " untrue "
os.environ["INPUT_NUMBER"] = " 1 "
os.environ["INPUT_DICT1"] = "status: broken\nby: ralf"
os.environ["INPUT_DICT2"] = '{"status": "broken", "by": "ralf"}'
os.environ["INPUT_DICT3"] = "{asdf"
os.environ["GITHUB_WORKFLOW_REF"] = "cssnr/actions-tools/.github/workflows/test.yaml@refs/heads/v1.0.0"
os.environ["GITHUB_OUTPUT"] = os.environ.get("GITHUB_OUTPUT") or os.path.join(cwd, "output.txt")
os.environ["GITHUB_ENV"] = os.environ.get("GITHUB_ENV") or os.path.join(cwd, "output.txt")
os.environ["GITHUB_PATH"] = os.environ.get("GITHUB_PATH") or os.path.join(cwd, "output.txt")
os.environ["GITHUB_STATE"] = os.environ.get("GITHUB_STATE") or os.path.join(cwd, "output.txt")
os.environ["GITHUB_STEP_SUMMARY"] = os.environ.get("GITHUB_STEP_SUMMARY") or os.path.join(cwd, "output-summary.txt")
os.environ["GITHUB_EVENT_PATH"] = os.environ.get("GITHUB_EVENT_PATH") or os.path.join(cwd, "event.json")


def test_print():
    core.debug("debug")
    core.info("info")
    core.notice("notice")
    core.warn("warn")
    with pytest.raises(SystemExit):
        core.set_failed("failed")
    core.mask("secret")
    core.start_group("group")
    core.end_group()
    core.start_indent()
    core.info("indent")
    core.end_indent()
    core.info("dedent")
    core.stop_commands()
    core.info("::warning::Just kidding")
    core.start_commands()
    with core.group("Title") as p:
        core.info("with group")
        p("core.info")
    core.info("no group")
    core.command("debug", "command")
    args = {
        "title": "Test Title",
        "file": "test-file.txt",
        "col": 1,
        "endColumn": 2,
        "line": 3,
        "endLine": 4,
        "end": "\n",
    }
    core.notice("notice with args", **args)


def test_outputs():
    core.set_output("test", "value")
    core.set_env("test", "value")
    core.add_path("/dev/null")
    core.set_state("STATE_test", "value")
    os.environ["STATE_test"] = "value"  # for testing core.get_state
    core.set_output("multi", "line1\nline2\nline3")


def test_inputs():
    assert core.get_input("test") == os.environ["INPUT_TEST"].strip()
    assert core.get_input("test", strip=False) == os.environ["INPUT_TEST"]
    with pytest.raises(ValueError):
        core.get_input("asdf", True)

    assert core.get_bool("test")
    assert not core.get_bool("false")
    with pytest.raises(ValueError):
        core.get_bool("asdf", True)

    assert isinstance(core.get_list("test", split="\n"), list)
    assert len(core.get_list("test", split="\n")) == 1
    with pytest.raises(ValueError):
        core.get_list("asdf", True)

    assert core.get_dict("dict1") == {"status": "broken", "by": "ralf"}
    assert core.get_dict("dict2") == {"status": "broken", "by": "ralf"}

    assert core.get_dict("dict3") == {}
    with pytest.raises(ValueError):
        core.get_dict("dict3", True)

    assert core.get_data("test") is True
    assert core.get_dict("test") == {}
    with pytest.raises(ValueError):
        core.get_data("test", True)
        core.get_dict("test", True)

    assert core.get_data("number") == 1
    assert core.get_dict("number") == {}
    with pytest.raises(ValueError):
        core.get_data("number", True)
        core.get_dict("number", True)

    assert not core.get_data("asdf")
    assert core.get_dict("asdf") == {}
    with pytest.raises(ValueError):
        core.get_data("asdf", True)
        core.get_dict("asdf", True)


def test_getters():
    assert core.get_state("STATE_test") == "value"
    assert len(core.get_random(20)) == 20
    assert not core.is_debug()
    assert core.get_event()
    assert core.get_version() == "v1.0.0"
    del os.environ["GITHUB_WORKFLOW_REF"]
    assert core.get_version() == "Source"
    assert core.get_version("asdf") == "asdf"
    assert context.repository_name is not None


def test_oidc_token():
    with pytest.raises(ValueError):
        core.get_id_token()
    # 3029-d29f-4014-9fb4 {"foo": "bar"}
    os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"] = "https://dummyjson.com/c/3029-d29f-4014-9fb4"
    with pytest.raises(ValueError):
        core.get_id_token()
    os.environ["ACTIONS_ID_TOKEN_REQUEST_TOKEN"] = "xxx"
    with pytest.raises(ValueError):
        core.get_id_token("audience")
    # 46d5-1506-40d5-b4f7 {"value": "bar"}
    os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"] = "https://dummyjson.com/c/46d5-1506-40d5-b4f7"
    assert core.get_id_token() == "bar"


def test_github(monkeypatch):
    # monkeypatch.delitem(sys.modules, "Github", raising=False)
    # importlib.reload(core)
    g = core.get_github("xxx")
    assert g


def test_summary():
    core.summary.clear()
    assert core.summary.stringify() == ""
    core.summary.add_eol()
    core.summary("ralf broke", False)
    assert_summary("\nralf broke")

    core.summary.add_raw("ralf broke")
    assert_summary("ralf broke\n")

    core.summary.add_heading("ralf broke")
    assert_summary("\n<h1>ralf broke</h1>\n\n")

    core.summary.add_hr()
    core.summary.add_br()
    assert_summary("\n<hr>\n\n\n<br>\n\n")

    core.summary.add_image("ralf", "broke")
    assert_summary('\n<img src="ralf" alt="broke" width="100" height="auto">\n\n')

    core.summary.add_link("ralf", "broke")
    assert_summary('\n<a href="broke">ralf</a>\n\n')

    core.summary.add_quote("i broke this")
    assert_summary("\n<blockquote>i broke this</blockquote>\n\n")
    core.summary.add_quote("i broke this", "ralf")
    assert_summary('\n<blockquote cite="ralf">i broke this</blockquote>\n\n')

    core.summary.clear()
    core.summary.add_code("broke", "ralf")
    assert_summary('\n<pre lang="ralf"><code>broke</code></pre>\n\n')

    core.summary.clear()
    core.summary.add_details("ralf", "broke")
    assert_summary("\n<details><summary>ralf</summary>broke</details>\n\n")

    core.summary.clear()
    core.summary.add_list(["ralf", "broke"])
    assert_summary("\n<ul><li>ralf</li>\n<li>broke</li></ul>\n\n")

    core.summary.clear()
    core.summary.add_table([["Who", "Did What"], ["ralf", "broke it"]])
    assert_summary(
        "\n<table><thead><tr><th>Who</th><th>Did What</th></tr></thead><tbody><tr><td>ralf</td><td>broke it</td></tr></tbody></table>\n\n"
    )

    core.summary.clear()
    with core.summary.code() as p:
        p("line 1")
        p("line 2")
    assert_summary('\n<pre lang="text"><code>line 1\nline 2</code></pre>\n\n')

    core.summary.clear()
    with core.summary.details("Summary") as p:
        p("line 1")
        p("line 2")
    assert_summary("\n<details><summary>Summary</summary>\n\nline 1\nline 2\n\n</details>\n\n")

    core.summary.clear()
    with core.summary.list() as p:
        p("line 1")
        p("line 2")
    assert_summary("\n<ul>\n<li>line 1</li>\n<li>line 2</li>\n</ul>\n\n")


def assert_summary(result: str, clear: bool = True):
    with open(os.environ["GITHUB_STEP_SUMMARY"], "r") as f:
        text = f.read()
        # print(f"repr: {repr(text)}")
        assert text == result
    if clear:
        core.summary.clear()

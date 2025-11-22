---
icon: lucide/notebook-pen
---

# :lucide-notebook-pen: Usage

After [installing](index.md) import the module and start using the methods...

## From actions/core

Full `core` reference: [/src/actions/core.py](https://github.com/cssnr/actions-tools/blob/master/src/actions/core.py)

### Inputs

```python
from actions import core

my_str = core.get_input("string")  # -> str
my_req = core.get_input("string", True)  # (1)!
my_bool = core.get_bool("boolean")  # -> bool
my_list = core.get_list("list")  # -> list
my_dict = core.get_dict("dict")  # -> dict - from json or yaml
my_data = core.get_data("data")  # -> Any - from json or yaml
```

1.  All the `get_input` methods accept these args/kwargs:

    ```python
    def get_input(name: str, req: bool = False, strip: bool = True) -> str:
        """
        Get String Input
        :param name: str: Input Name
        :param req: bool: If Required
        :param strip: bool: To Strip
        :return:
        """
    ```

    Additional kwargs are passed directly to `print`.

### Context

This is a custom `object`: [/src/actions/context.py](https://github.com/cssnr/actions-tools/blob/master/src/actions/context.py)

```python
from actions import core, context

core.info(f"event_name: {context.event_name}")
core.info(f"ref_name: {context.ref_name}")
core.info(f"runner_temp: {context.runner_temp}")
```

Reference: https://docs.github.com/en/actions/reference/workflows-and-actions/variables

### Event

The event payload depends on the event that triggered the workflow.

```python
from actions import core

event = core.get_event()  # -> dict
core.info(str(event))
repository = event.get("repository")
core.info(str(repository))
```

Reference: https://docs.github.com/en/webhooks/webhook-events-and-payloads

### Logging

```python
from actions import core

core.info("info")  # alias for print
core.debug("debug")

# Annotations
core.notice("notice")
core.warn("warn")
core.error("error", title="Title", file="File", col=1, endColumn=2, line=3, endLine=4)

# Blocks
core.start_group("Title")
core.info("This is folded.")
core.end_group()

with core.group("Title") as p:
    p("This is folded.")  # (1)!
    core.info("Also folded.")
```

1.  Any output in this context will be folded.

Reference: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands

### Env/Path

```python
from actions import core

# Environment
core.set_env("NAME", "value")

# System Path
core.add_path("/dev/null")
```

### State

```python
from actions import core

# Set State
name = core.set_state("name", "value")

# Get State
value = core.get_state("name")
```

### Secret/Outputs

```python
from actions import core

# Mask Secret
core.mask("super-secret-string")

# Set Output
core.set_output("name", "cssnr")
```

### Summary

```python
from actions import core

core.summary.add_raw("text")  # (1)!
# text\n
core.summary.add_eol()
# \n
core.summary.add_code("python", "from actions import core")
# \n<pre lang="python"><code>from actions import core</code></pre>\n\n
core.summary.add_list(["item 1", "item 2"])
# \n<ul><li>ralf</li>\n<li>broke</li></ul>\n\n
core.summary.add_details("Summary", "Details...")
# \n<details><summary>Summary</summary>Details...</details>\n\n
core.summary.add_image("src", "alt", 100)
# \n<img src="src" alt="alt" width="100" height="auto">\n\n
core.summary.add_heading("Heading", 1)
# \n<h1>Heading</h1>\n\n
core.summary.add_hr()
# \n<hr>\n\n
core.summary.add_br()
# \n<br>\n\n
core.summary.add_quote("I broke it.", "ralf")
# \n<blockquote cite="ralf">I broke it.</blockquote>\n\n
core.summary.add_link("text", "href")
# \n<a href="href">text</a>\n\n
```

1.  This can be any [GitHub flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

Summary context handlers.

```python
from actions import core

with core.summary.code() as add:
    add("line 1")
    add("line 2")
# \n<pre lang="text"><code>line 1\nline 2</code></pre>\n\n

with core.summary.list() as add:
    add("line 1")
    add("line 2")
# \n<ul>\n<li>line 1</li>\n<li>line 2</li>\n</ul>\n\n

with core.summary.details("Summary") as add:
    add("line 1")
    add("line 2")
# \n<details><summary>Summary</summary>\n\nline 1\nline 2\n\n</details>\n\n
```

### Commands

```python
from actions import core

# Stop Commands
core.stop_commands()
core.info("::error::log output with commands")
core.start_commands()

# Custom Commands
core.command("warning", "Warned!")  # core.warn()
```

### Debug/Set Failed

```python
from actions import core

# Runner Debug
debug_on = core.is_debug()  # -> bool
core.info(f"debug_on: {debug_on}")

# Exit with Failure
core.set_failed("Mayday!")  # (1)!
```

1.  This is shorthand for:
    ```python
    core.error("Mayday!")
    raise SystemExit
    ```

### PyGithub (Octokit)

```python
from actions import core, context

token = core.get_input("token", True)

g = core.get_github(token)  # (1)!

repo = g.get_repo(f"{context.repository}")
core.info(f"repo.name: {repo.name}")
```

1.  To use `get_github` install with the github extra:
    ```shell
    python -m pip install actions-tools[github]
    ```

Reference: https://pygithub.readthedocs.io/en/stable/

### OIDC Token

```python
from actions import core

id_token = core.get_id_token()
id_token_aud = core.get_id_token("audience")
```

Reference: https://docs.github.com/en/actions/reference/security/oidc

## New In actions-tools

```python
from actions import core, context

# Context
core.info(f"repository_name: {context.repository_name}")

# Action Version
version = core.get_version()  # from GITHUB_WORKFLOW_REF

# Random
rand = core.get_random(32)

# Indent
core.start_indent(4)
core.info("Indented")  # only works with core.info
core.end_indent()
```

## Example Actions

- Create Files Action: [cssnr/create-files-action/src/main.py](https://github.com/cssnr/create-files-action/blob/master/src/main.py)
- Python Action Template: [smashedr/test-action-py/src/main.py](https://github.com/smashedr/test-action-py/blob/master/src/main.py)
- Python UV Action Template: [smashedr/test-action-uv/src/main.py](https://github.com/smashedr/test-action-uv/blob/master/src/main.py)

&nbsp;

!!! question

    If you need help or run into issues, [support](support.md) is available!

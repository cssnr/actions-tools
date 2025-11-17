---
icon: lucide/notebook-pen
---

# Usage

After [installing](index.md) import the module and start using the methods...

## From @actions/toolkit

```python
from actions import core, context

# Input
# (1)!
my_str = core.get_input("string")  # -> str
my_req = core.get_input("string", True)  # required
my_bool = core.get_bool("boolean")  # -> bool
my_list = core.get_list("list")  # -> list
my_dict = core.get_dict("dict")  # -> dict - from json or yaml
my_data = core.get_dict("data")  # -> Any - from json or yaml

# Context
# (2)!
core.info(f"event_name: {context.event_name}")
core.info(f"ref_name: {context.ref_name}")
core.info(f"runner_temp: {context.runner_temp}")

# Event
# (3)!
event = core.get_event()  # -> dict
core.info(str(event))
repository = event.get("repository")

# Logging
core.info("info")  # alias for print
core.debug("debug")

# Annotations
# (4)!
core.notice("notice")
core.warn("warn")
core.error("error", title="Title", file="File", col=1, endColumn=2, line=3, endLine=4)

# Blocks
core.start_group("Title")
core.info("This is folded.")
core.end_group()

with core.group("Title") as p:
    p("This is folded.")
    core.info("Also folded.")

# Environment
core.set_env("NAME", "value")

# State
name = core.set_state("name", "value")
value = core.get_state("name")

# System Path
core.add_path("/dev/null")

# Set Secret
core.mask("super-secret-string")

# Outputs
core.set_output("name", "cssnr")

# Commands
core.stop_commands()
core.info("::error::log output with commands")
core.start_commands()

# Summary
core.summary("## Test Action")

# Abort
core.set_failed("Mayday!")

# Runner Debug
core.is_debug()

# PyGithub (Octokit)
# (5)!
token = core.get_input("token", True)
g = core.get_github(token)
repo = g.get_repo(f"{context.repository}")
core.info(f"repo.name: {repo.name}")

# OIDC Token
# https://docs.github.com/en/actions/reference/security/oidc
id_token = core.get_id_token()
id_token_aud = core.get_id_token("audience")
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

2.  Full `context` reference: [../src/actions/context.py](https://github.com/cssnr/actions-tools/blob/master/src/actions/context.py)

    Reference: https://docs.github.com/en/actions/reference/workflows-and-actions/variables

3.  The event payload depends on the event that triggered the workflow.

    Reference: https://docs.github.com/en/webhooks/webhook-events-and-payloads

4.  All annotation methods accept all kwargs shown below.

    Reference: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#setting-a-notice-message

5.  This requires PyGithub. Make sure to install with:

    ```shell
    python -m pip install actions-tools[github]
    ```

    Reference: https://pygithub.readthedocs.io/en/stable/

Full `core` reference: [../src/actions/core.py](https://github.com/cssnr/actions-tools/blob/master/src/actions/core.py)  
Full `context` reference: [../src/actions/context.py](https://github.com/cssnr/actions-tools/blob/master/src/actions/context.py)

## New In actions-tools

```python
from actions import core, context

# Context
core.info(f"repository_name: {context.repository_name}")

# Commands
core.command("warning", "Warned!")  # core.warn()

# Action Version
version = core.get_version()  # from GITHUB_WORKFLOW_REF

# Random
rand = core.get_random(32)

# Indent
core.start_indent(4)
core.info("Indented")  # only works with core.info
core.end_indent()
```

Example Actions:

- Create Files Action: [cssnr/create-files-action/src/main.py](https://github.com/cssnr/create-files-action/blob/master/src/main.py)
- Python Action Template: [smashedr/test-action-py/src/main.py](https://github.com/smashedr/test-action-py/blob/master/src/main.py)
- Python UV Action Template: [smashedr/test-action-uv/src/main.py](https://github.com/smashedr/test-action-uv/blob/master/src/main.py)

&nbsp;

!!! question

    If you need help or run into issues, [support](support.md) is available!

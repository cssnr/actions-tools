---
icon: lucide/cog
---

# Usage

Once [installed](index.md) import the module and start using methods.

## From @actions/toolkit

```python
from actions import core, context

# Input
my_str = core.get_input("string")  # -> str
my_req = core.get_input("string", True)  # required
my_bool = core.get_bool("boolean")  # -> bool
my_list = core.get_list("list")  # -> list
my_data = core.get_dict("dict")  # -> dict - from json or yaml

# Context
# https://docs.github.com/en/actions/reference/workflows-and-actions/variables
core.info(f"event_name: {context.event_name}")
core.info(f"ref_name: {context.ref_name}")
core.info(f"runner_temp: {context.runner_temp}")

# Event
# https://docs.github.com/en/webhooks/webhook-events-and-payloads
event = core.get_event()  # -> dict
core.info(str(event))
repository = event.get("repository")

# Logging
core.info("info")  # alias for print
core.debug("debug")

# Annotations
# https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#setting-a-notice-message
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

# OIDC Token
# https://docs.github.com/en/actions/reference/security/oidc
id_token = core.get_id_token()
```

View Example Action: [smashedr/test-action-py](https://github.com/smashedr/test-action-py/blob/master/src/main.py)

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

## GitHub API PyGithub

To access the GitHub API install [PyGithub](https://github.com/PyGithub/PyGithub).

```shell
python -m pip install PyGithub
```

Then import and initialize with the `token`.

```python
from actions import core, context
from github import Auth, Github

token: str = core.get_input("token")
g = Github(auth=Auth.Token(token))
repo = g.get_repo(f"{context.repository}")
core.info(f"repo.name: {repo.name}")
```

Reference: https://pygithub.readthedocs.io/en/stable/

&nbsp;

!!! note

    This project is in active development.
    Please [let us know](https://github.com/cssnr/actions-tools/discussions/categories/feature-requests)
    what features you want to see.

!!! example "Work in Progress"

    This documentation site is a work in progress.
    See the [README.md](https://github.com/cssnr/actions-tools?tab=readme-ov-file#readme) for more details.

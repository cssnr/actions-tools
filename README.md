[![Release](https://img.shields.io/github/actions/workflow/status/cssnr/actions-tools/release.yaml?logo=github&logoColor=white&label=release)](https://github.com/cssnr/actions-tools/actions/workflows/release.yaml)
[![Test](https://img.shields.io/github/actions/workflow/status/cssnr/actions-tools/test.yaml?logo=github&logoColor=white&label=test)](https://github.com/cssnr/actions-tools/actions/workflows/test.yaml)
[![Lint](https://img.shields.io/github/actions/workflow/status/cssnr/actions-tools/lint.yaml?logo=github&logoColor=white&label=lint)](https://github.com/cssnr/actions-tools/actions/workflows/lint.yaml)
[![Codecov](https://codecov.io/gh/cssnr/actions-tools/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/actions-tools)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cssnr_actions-tools&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cssnr_actions-tools)
[![PyPI](https://img.shields.io/pypi/v/actions-tools?logo=python&logoColor=white&label=PyPI)](https://pypi.org/project/actions-tools/)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/actions-tools?logo=github)](https://github.com/cssnr/actions-tools/releases/latest)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/actions-tools?logo=htmx&logoColor=white)](https://github.com/cssnr/actions-tools)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Factions-tools%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=version)](https://github.com/cssnr/actions-tools)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/actions-tools?logo=github&logoColor=white&label=updated)](https://github.com/cssnr/actions-tools/graphs/commit-activity)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/actions-tools?style=flat&logo=github&logoColor=white)](https://github.com/cssnr/actions-tools/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&logoColor=white&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)

# Actions Tools

- [Install](#Install)
- [Usage](#Usage)
- [Support](#Support)
- [Contributing](#Contributing)

> [!WARNING]  
> This project is in development and is NOT stable!

GitHub Actions Tools for Python.

## Install

From PyPI: https://pypi.org/p/actions-tools

```shell
python -m pip install actions-tools
```

From source:

```shell
git clone https://github.com/cssnr/actions-tools
python -m pip install -e actions-tools
```

Uninstall:

```shell
python -m pip uninstall actions-tools
```

## Usage

Functionality from @actions/toolkit

```python
from actions import core

# Input
myStr = core.get_input('myStr')
myLowerString = core.get_input('myLowerStr', low=1)
myRequiredStr = core.get_input('myRequiredStr', req=1)
myBoolean = core.get_input('myBoolean', boolean=1)
myList = core.get_input('myList', split="[,|\n]")

# Logging
core.info("info")  # alias for print
core.debug("debug")

# Annotations
core.notice("notice")
core.warn("warn")
core.error("error")

# Blocks
core.start_group("Test")
core.info('This is folded.')
core.end_group()

with core.with_group("Test") as info:
    info('This is folded.')
    core.info('Also folded.')

# Summary
core.summary('## Test Action')

# Environment
core.set_env('NAME', 'value')

# State
stateName = core.set_state('NAME', 'value')
stateValue = core.get_state('NAME')

# System Path
core.add_path('/dev/null')

# Outputs
core.set_output('name', 'cssnr')

# Abort
core.set_failed("Mayday!")
```

Functionality new in actions-tools

```python
from actions import core

# Commands
core.command('warning', 'Warned!')

# Random
myRandom = core.get_random(32)

# Indent
core.start_indent(4)
core.info('Indented')  # only works with core.info
core.end_indent()
```

# Support

For general help or to request a feature, see:

- Q&A Discussion: https://github.com/cssnr/actions-tools/discussions/categories/q-a
- Request a Feature: https://github.com/cssnr/actions-tools/discussions/categories/feature-requests
- Chat with us on Discord: https://discord.gg/wXy6m2X8wY

If you are experiencing an issue/bug or getting unexpected results, you can:

- Report an Issue: https://github.com/cssnr/actions-tools/issues
- Provide General Feedback: [https://cssnr.github.io/feedback/](https://cssnr.github.io/feedback/?app=actions-tools)
- Chat with us on Discord: https://discord.gg/wXy6m2X8wY

# Contributing

> [!TIP]
> See the [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on testing and building.

Currently, the best way to contribute to this project is to star this project on GitHub, open a
[feature request](https://github.com/cssnr/actions-tools/discussions/categories/feature-requests)
or report any [issues](https://github.com/cssnr/actions-tools/issues) you find.

Additionally, you can support other GitHub Actions I have published:

- [Stack Deploy Action](https://github.com/cssnr/stack-deploy-action?tab=readme-ov-file#readme)
- [Portainer Stack Deploy](https://github.com/cssnr/portainer-stack-deploy-action?tab=readme-ov-file#readme)
- [VirusTotal Action](https://github.com/cssnr/virustotal-action?tab=readme-ov-file#readme)
- [Mirror Repository Action](https://github.com/cssnr/mirror-repository-action?tab=readme-ov-file#readme)
- [Update Version Tags Action](https://github.com/cssnr/update-version-tags-action?tab=readme-ov-file#readme)
- [Update JSON Value Action](https://github.com/cssnr/update-json-value-action?tab=readme-ov-file#readme)
- [Parse Issue Form Action](https://github.com/cssnr/parse-issue-form-action?tab=readme-ov-file#readme)
- [Cloudflare Purge Cache Action](https://github.com/cssnr/cloudflare-purge-cache-action?tab=readme-ov-file#readme)
- [Mozilla Addon Update Action](https://github.com/cssnr/mozilla-addon-update-action?tab=readme-ov-file#readme)
- [Docker Tags Action](https://github.com/cssnr/docker-tags-action?tab=readme-ov-file#readme)

For a full list of current projects to support visit: [https://cssnr.github.io/](https://cssnr.github.io/)

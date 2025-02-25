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
- [Development](#Development)
- [Contributing](#Contributing)

GitHub Actions Tools for Python.

> [!WARNING]  
> This project is in development and is NOT stable!

## Install

```shell
python -m pip install actions-tools
```

## Usage

Functionality from @actions/toolkit

```python
from actions import core

# Input
name = core.get_input('name')

# Logging
core.debug("debug")
core.info("info") # print
core.warn("warn")
core.error("error")

# Blocks
core.start_group("Test")
core.info('This folded.')
core.end_group()

# Summary
core.summary('## Test Action')

# Output
core.set_env('VAR', 'value')
core.set_output('name', 'god')

# Abort
core.set_failed("Mayday!")
```

Functionality new in actions-tools

```python
from actions import core

# Indent
core.start_indent(4)
core.info('Indented') # only works with core.info
core.end_indent()
```

# Development

### Install

Install the package from source:

```shell
python -m pip install -U pip
python -m pip install -Ur requirements.txt
python -m pip install -e .
```

Prettier is used to format yaml, json and md.

```shell
npm install -g prettier
```

To Uninstall:

```shell
python -m pip uninstall actions-tools
```

### Test

First [Install](#Install), then run:

```shell
coverage run -m pytest
coverage report -m
```

### Building

Build the project locally:

```shell
python -m pip install -U pip
python -m pip install -Ur requirements.txt
python -m pip build
```

Install the built package:

```shell
python -m pip install dist/actions_tools-0.0.1-py3-none-any.whl
```

# Contributing

Currently, the best way to contribute to this project is to star this project on GitHub.

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

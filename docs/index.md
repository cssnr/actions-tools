---
icon: lucide/rocket
---

[![PyPI Version](https://img.shields.io/pypi/v/actions-tools?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/actions-tools/)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/actions-tools?logo=github)](https://github.com/cssnr/actions-tools/releases)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Factions-tools%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/actions-tools?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/actions-tools?logo=pypi&logoColor=white)](https://pepy.tech/projects/actions-tools)
[![Codecov](https://codecov.io/gh/cssnr/actions-tools/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/actions-tools)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cssnr_actions-tools&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cssnr_actions-tools)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/actions-tools?logo=htmx&logoColor=white)](https://github.com/cssnr/actions-tools?tab=readme-ov-file#readme)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/actions-tools?logo=github&logoColor=white&label=updated)](https://github.com/cssnr/actions-tools/graphs/commit-activity)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/actions-tools?logo=github)](https://github.com/cssnr/actions-tools/graphs/contributors)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/cssnr/actions-tools?logo=bookstack&logoColor=white&label=repo%20size)](https://github.com/cssnr/actions-tools)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/actions-tools?style=flat&logo=github)](https://github.com/cssnr/actions-tools/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/actions-tools?style=flat&logo=github&logoColor=white)](https://github.com/cssnr/actions-tools/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

[![Image title](https://raw.githubusercontent.com/smashedr/repo-images/refs/heads/master/actions-tools/logo128.png){ align=right }](https://github.com/cssnr/actions-tools?tab=readme-ov-file#readme)

# Get Started

A Typed Python GitHub Actions Tookit similar to [actions/toolkit](https://github.com/actions/toolkit).

**To get started [install](#install) the tools and view the [usage](usage.md).**

If you run into any issues, [support](support.md) is available.

## Install

From PyPI: https://pypi.org/p/actions-tools

```shell
python -m pip install actions-tools
```

With [PyGithub](https://github.com/PyGithub/PyGithub) (for GitHub API access).

```shell
python -m pip install actions-tools[github]
```

Add to requirements.

=== "requirements.txt"

    ``` text
    actions-tools
    ```

=== "with PyGithub"

    ``` text
    actions-tools[github]
    ```

Install from source.

```shell
git clone https://github.com/cssnr/actions-tools
python -m pip install actions-tools
```

Uninstall.

```shell
python -m pip uninstall actions-tools
```

&nbsp;

<!-- TODO: Mirror README.md usage here and update Usage for the docs site -->

[:lucide-notebook-pen: View the Usage](usage.md){ .md-button .md-button--primary }

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

**Make sure to view the full [Usage](usage.md) guide.**

&nbsp;

!!! question

    If you need help or run into issues, [support](support.md) is available!

!!! info

    This project is in active development.
    Please [let us know](https://github.com/cssnr/actions-tools/discussions/categories/feature-requests)
    what features you want to see.

!!! example "Documentation"

    This documentation site is a work in progress.
    See the [README.md](https://github.com/cssnr/actions-tools?tab=readme-ov-file#readme) for more details.

[![PyPI Version](https://img.shields.io/pypi/v/actions-tools?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/actions-tools/)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/actions-tools?logo=github)](https://github.com/cssnr/actions-tools/releases)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Factions-tools%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/actions-tools?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/actions-tools?logo=pypi&logoColor=white)](https://pepy.tech/projects/actions-tools)
[![Codecov](https://codecov.io/gh/cssnr/actions-tools/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/actions-tools)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cssnr_actions-tools&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cssnr_actions-tools)
[![Release Workflow](https://img.shields.io/github/actions/workflow/status/cssnr/actions-tools/release.yaml?logo=github&logoColor=white&label=release)](https://github.com/cssnr/actions-tools/actions/workflows/release.yaml)
[![Lint Workflow](https://img.shields.io/github/actions/workflow/status/cssnr/actions-tools/lint.yaml?logo=github&logoColor=white&label=lint)](https://github.com/cssnr/actions-tools/actions/workflows/lint.yaml)
[![Test Workflow](https://img.shields.io/github/actions/workflow/status/cssnr/actions-tools/test.yaml?logo=github&logoColor=white&label=test)](https://github.com/cssnr/actions-tools/actions/workflows/test.yaml)
[![GitHub Deployments](https://img.shields.io/github/deployments/cssnr/actions-tools/pypi?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/actions-tools/)
[![GitHub Deployments](https://img.shields.io/github/deployments/cssnr/actions-tools/docs?logo=materialformkdocs&logoColor=white&label=docs)](https://actions-tools.cssnr.com/)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/actions-tools?logo=htmx&logoColor=white)](https://github.com/cssnr/actions-tools?tab=readme-ov-file#readme)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/actions-tools?logo=github&logoColor=white&label=updated)](https://github.com/cssnr/actions-tools/graphs/commit-activity)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/actions-tools?logo=github)](https://github.com/cssnr/actions-tools/graphs/contributors)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/cssnr/actions-tools?logo=bookstack&logoColor=white&label=repo%20size)](https://github.com/cssnr/actions-tools)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/actions-tools?style=flat&logo=github)](https://github.com/cssnr/actions-tools/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/actions-tools?style=flat&logo=github&logoColor=white)](https://github.com/cssnr/actions-tools/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

# Actions Tools

- [Install](#Install)
- [Usage](#Usage)
- [Support](#Support)
- [Contributing](#Contributing)

<p align="center"><a title="Actions Tools Docs" href="https://actions-tools.cssnr.com/" target="_blank">
<img alt="Actions Tools Docs" width="256" height="auto" src="https://raw.githubusercontent.com/smashedr/repo-images/refs/heads/master/actions-tools/logo256.png" />
</a></p>

A Typed Python GitHub Actions Tookit similar to [actions/toolkit](https://github.com/actions/toolkit).

> [!NOTE]  
> This project is in active development.  
> Please [let us know](https://github.com/cssnr/actions-tools/discussions/categories/feature-requests)
> what features you want to see.  
> The [Documentation Site](https://actions-tools.cssnr.com/) is also a work in progress...

## Install

From PyPI: https://pypi.org/p/actions-tools

```shell
python -m pip install actions-tools
```

With [PyGithub](https://github.com/PyGithub/PyGithub) (for GitHub API access).

```shell
python -m pip install actions-tools[github]
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

## Usage

A usage guide is also available on the [documentation site](https://actions-tools.cssnr.com/usage/).

Functionality from @actions/toolkit

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

# PyGithub (Octokit)
# https://pygithub.readthedocs.io/en/stable/
token = core.get_input("token", True)
g = core.get_github(token)
repo = g.get_repo(f"{context.repository}")
core.info(f"repo.name: {repo.name}")

# OIDC Token
# https://docs.github.com/en/actions/reference/security/oidc
id_token = core.get_id_token()
```

- Full `core` reference: [../src/actions/core.py](https://github.com/cssnr/actions-tools/blob/master/src/actions/core.py)
- Full `context` reference: [../src/actions/context.py](https://github.com/cssnr/actions-tools/blob/master/src/actions/context.py)

Functionality new in actions-tools

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

View example action: [smashedr/test-action-py](https://github.com/smashedr/test-action-py/blob/master/src/main.py)

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

If you would like to submit a PR, please review the [CONTRIBUTING.md](#contributing-ov-file).

Please consider making a donation to support the development of this project
and [additional](https://cssnr.com/) open source projects.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cssnr)

Additionally, you can support other [GitHub Actions](https://actions.cssnr.com/) I have published:

- [Stack Deploy Action](https://github.com/cssnr/stack-deploy-action?tab=readme-ov-file#readme)
- [Portainer Stack Deploy Action](https://github.com/cssnr/portainer-stack-deploy-action?tab=readme-ov-file#readme)
- [Docker Context Action](https://github.com/cssnr/docker-context-action?tab=readme-ov-file#readme)
- [Actions Up Action](https://github.com/cssnr/actions-up-action?tab=readme-ov-file#readme)
- [VirusTotal Action](https://github.com/cssnr/virustotal-action?tab=readme-ov-file#readme)
- [Mirror Repository Action](https://github.com/cssnr/mirror-repository-action?tab=readme-ov-file#readme)
- [Update Version Tags Action](https://github.com/cssnr/update-version-tags-action?tab=readme-ov-file#readme)
- [Docker Tags Action](https://github.com/cssnr/docker-tags-action?tab=readme-ov-file#readme)
- [Update JSON Value Action](https://github.com/cssnr/update-json-value-action?tab=readme-ov-file#readme)
- [JSON Key Value Check Action](https://github.com/cssnr/json-key-value-check-action?tab=readme-ov-file#readme)
- [Parse Issue Form Action](https://github.com/cssnr/parse-issue-form-action?tab=readme-ov-file#readme)
- [Cloudflare Purge Cache Action](https://github.com/cssnr/cloudflare-purge-cache-action?tab=readme-ov-file#readme)
- [Mozilla Addon Update Action](https://github.com/cssnr/mozilla-addon-update-action?tab=readme-ov-file#readme)
- [Package Changelog Action](https://github.com/cssnr/package-changelog-action?tab=readme-ov-file#readme)
- [NPM Outdated Check Action](https://github.com/cssnr/npm-outdated-action?tab=readme-ov-file#readme)
- [Label Creator Action](https://github.com/cssnr/label-creator-action?tab=readme-ov-file#readme)
- [Algolia Crawler Action](https://github.com/cssnr/algolia-crawler-action?tab=readme-ov-file#readme)
- [Upload Release Action](https://github.com/cssnr/upload-release-action?tab=readme-ov-file#readme)
- [Check Build Action](https://github.com/cssnr/check-build-action?tab=readme-ov-file#readme)
- [Web Request Action](https://github.com/cssnr/web-request-action?tab=readme-ov-file#readme)
- [Get Commit Action](https://github.com/cssnr/get-commit-action?tab=readme-ov-file#readme)

<details><summary>❔ Unpublished Actions</summary>

These actions are not published on the Marketplace, but may be useful.

- [cssnr/create-files-action](https://github.com/cssnr/create-files-action?tab=readme-ov-file#readme) - Create various files from templates.
- [cssnr/draft-release-action](https://github.com/cssnr/draft-release-action?tab=readme-ov-file#readme) - Keep a draft release ready to publish.
- [cssnr/env-json-action](https://github.com/cssnr/env-json-action?tab=readme-ov-file#readme) - Convert env file to json or vice versa.
- [cssnr/push-artifacts-action](https://github.com/cssnr/push-artifacts-action?tab=readme-ov-file#readme) - Sync files to a remote host with rsync.
- [smashedr/update-release-notes-action](https://github.com/smashedr/update-release-notes-action?tab=readme-ov-file#readme) - Update release notes.
- [smashedr/combine-release-notes-action](https://github.com/smashedr/combine-release-notes-action?tab=readme-ov-file#readme) - Combine release notes.

---

</details>

<details><summary>📝 Template Actions</summary>

These are basic action templates that I use for creating new actions.

- [js-test-action](https://github.com/smashedr/js-test-action?tab=readme-ov-file#readme) - JavaScript
- [ts-test-action](https://github.com/smashedr/ts-test-action?tab=readme-ov-file#readme) - TypeScript
- [py-test-action](https://github.com/smashedr/py-test-action?tab=readme-ov-file#readme) - Python (Dockerfile)
- [docker-test-action](https://github.com/smashedr/docker-test-action?tab=readme-ov-file#readme) - Docker (Image)

Note: The `docker-test-action` builds, runs and pushes images to [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

---

</details>

For a full list of current projects visit: [https://cssnr.github.io/](https://cssnr.github.io/)

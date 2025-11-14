# Contributing

- [Workflow](#Workflow)
- [Setup](#Setup)
- [Formatting](#Formatting)
- [Testing](#Testing)
- [Building](#Building)
- [Documentation](#Documentation)

This is a basic contributing guide and is a work in progress.

## Workflow

[![Fork](https://badges.cssnr.com/static/fork?lucide=git-fork&style=for-the-badge&color=3674a7)](https://github.com/cssnr/actions-tools/fork)

1. Fork the repository.
2. Create a branch in your fork!
3. Make your changes, see [Setup](#Setup).
4. Test your changes, see [Testing](#Testing).
5. Commit and push your changes.
6. Create a PR to this repository.
7. Verify all the tests pass, fix the issues.
8. Make sure to keep your branch up-to-date.

If you need help with anything, [let us know](#readme-ov-file)...

## Setup

Clone the repository, change into the directory and run.

```shell
python -m pip install -U pip
python -m pip install -Ur requirements.txt
```

Install the project as an editable.

```shell
python -m pip install -e .
```

# Formatting

Black is used to format python code.

Prettier is used to format yaml, json and md.

```shell
npm install -g prettier
npx prettier --check .
npx prettier --write .
```

For details on linters see the [pyproject.toml](pyproject.toml) and [.github/workflows/lint.yaml](.github/workflows/lint.yaml).

## Testing

First [Setup](#Setup) the project, then run.

```shell
pytest -s
pytest -s -k test_print
```

To see coverage, run the test with.

```shell
coverage run -m pytest
coverage report -m
```

Run a test by name.

```shell
pytest -s -k test_print
```

## Building

Build the project locally.

```shell
python -m pip install -U pip
python -m pip install -Ur requirements.txt
python -m build
```

Install the built package.

```shell
python -m pip install dist/actions_tools-0.0.1-py3-none-any.whl
```

The default version is `0.0.1` unless you set the environment variable `GITHUB_REF_NAME`.

See [src/actions/\_\_init\_\_.py](src/actions/__init__.py) for more details.

## Documentation

The docs are built with Zensical.

```shell
python -m pip install -U zensical
zensical serve
```

Then visit: http://localhost:8000/

You can also build the docs locally.

```shell
zensical build
```

This builds the docs to the `sites` folder. It should run on any static site.

```shell
docker run --rm -p 8000:80 --name docker-static -v "./site:/static" ghcr.io/cssnr/docker-nginx-static:latest
```

Then visit: http://localhost:8000/

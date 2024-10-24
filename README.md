![Static Badge](https://img.shields.io/badge/Python-3.9_%7C_3.10_%7C_3.11_%7C_3.12-blue?logo=python&logoColor=white)
[![PyPI - Version](https://img.shields.io/pypi/v/cron-mon-py)](https://pypi.org/project/cron-mon-py/)
[![Read the Docs](https://img.shields.io/readthedocs/cron-mon-py)](https://cron-mon-py.readthedocs.io)

[![CI](https://github.com/cron-mon-io/cron-mon-py/actions/workflows/ci.yml/badge.svg)](https://github.com/cron-mon-io/cron-mon-py/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/cron-mon-io/cron-mon-py/graph/badge.svg?token=EBVN9A4223)](https://codecov.io/gh/cron-mon-io/cron-mon-py)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

# `cron-mon-py`

A simple Python package to make using [CronMon](https://github.com/cron-mon-io) in your cron jobs and scheduled tasks quick and easy.


## Installation

`cron-mon-py` can be installed via `pip` - or your Python package manager of choice - like any other Python package you might install

```console
pip install cron-mon-py
```

## Example

Simply import the `monitor` decorator and use it on any function that serves as the entry point to your cron job/ scheduled task that you wish to monitor:

> You'll need to have setup a _Monitor_ and an API key within CronMon itself, and have exposed the API key in an environment variable called `CRON_MON_API_KEY`.

```python
from cron_mon import monitor

# Replace <your-monitor-id> with your actual Monitor ID
@monitor("<your-monitor-id>")
def cron_job():
    """Your cron job code here"""
    ...
```

## Development

### Setting up a development environment

`cron-mon-py` uses [`uv`](https://docs.astral.sh/uv/) to manage dependencies, so you'll need `uv` installed to get setup to work on `cron-mon-py`. You can either install `uv` on your machine, or you can use the dev container provided in the repository if your IDE supports dev containers (hint: it's very well supported on Visual Studio Code).

Once you have `uv` setup, you can use the `Makefile` provided to install all dependencies and run the tests. The available commands are as follows:

* `install`: Install all of the required dependencies to work on `cron-mon-py`
* `static-tests`: Run static tests via `ruff` and `mypy`
* `unit-tests`: Run unit tests via `pytest`
* `test`: Run all of the available tests for `cron-mon-py` (`static-tests` and `unit-tests`)
* `build`: Build the package
* `docs`: Build the package's docs
* `serve-docs`: Serve the package's documentation with hot-reload
* `format`: Autoformat the code with `ruff`*

> *You can avoid having to use `make format` if you setup your IDE to autoformat on save. The provided dev container has this already setup for you.

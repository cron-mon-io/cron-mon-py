"""Tests that ensure the `monitor` decorator takes its config from env."""

import os

import pytest


@pytest.mark.parametrize(
    ["env_vars", "error_message"],
    [
        ({}, "CRON_MON_SERVER_URL"),
        ({"CRON_MON_SERVER_URL": "http://localhost:8000"}, "CRON_MON_API_KEY"),
        ({"CRON_MON_API_KEY": "test"}, "CRON_MON_SERVER_URL"),
    ],
)
def test_monitor_env(env_vars: dict[str, str], error_message: str) -> None:
    """Test that the `monitor` decorator takes its config from env."""
    # Is there a way to test this without modifying the environment?
    os.environ.clear()
    os.environ.update(env_vars)

    with pytest.raises(KeyError, match=error_message):
        from cron_mon.monitor import monitor  # noqa: F401

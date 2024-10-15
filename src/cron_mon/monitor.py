"""Decorator for monitoring function execution time via CronMon."""

import os
from functools import wraps
from typing import Any, Callable

from requests import Session


class monitor:
    """A decorator class for monitoring function execution time via CronMon."""

    __SERVER_URL = os.environ["CRON_MON_SERVER_URL"]
    __API_KEY = os.environ["CRON_MON_API_KEY"]
    # TODO: Logger?

    def __init__(self, monitor_id: str) -> None:
        """Initialize the decorator with the monitor ID to use for monitoring.

        Args:
            monitor_id: The monitor ID to use for monitoring the function.
        """
        self.monitor_id = monitor_id
        self.monitor_url = (
            f"{self.__SERVER_URL}/api/v1/monitors/{self.monitor_id}"
        )

    def __call__(self, func: Callable[..., Any]) -> Callable[[Any], Any]:
        """Wrap the function with monitoring logic.

        Args:
            func: The function to wrap with monitoring logic.
        """

        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            with Session() as session:
                # Record the start of the job.
                # TODO: Handle exceptions from the server.
                job_id = session.post(
                    url=f"{self.monitor_url}/jobs/start",
                    headers={"X-API-Key": self.__API_KEY},
                ).json()["data"]["job_id"]

                # Execute the decorated function and record the output and any
                # exceptions that occur.
                exc = None
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    exc = e

                # Finish the job by sending the output and whether the job
                # succeeded or not.
                # TODO: Handle exceptions from the server.
                output = exc or result
                session.post(
                    url=f"{self.monitor_url}/jobs/{job_id}/finish",
                    headers={"X-API-Key": self.__API_KEY},
                    json={
                        "succeeded": exc is None,
                        "output": str(output) if output else None,
                    },
                )

                # Raise an exception if one occurred, since we don't want to
                # swallow exceptions, just record them. The underlying
                # application can decide if/ how to handle them.
                if exc:
                    raise exc

                return result

        return wrapper

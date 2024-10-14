"""Decorator for monitoring function execution time via CronMon."""

from functools import wraps
from typing import Any, Callable

from requests import Session


def monitor(monitor_id: str) -> Callable[[Any], Any]:
    """Decorator for monitoring function execution time via CronMon.

    Args:
        monitor_id: The monitor ID to use for monitoring the function.
    """
    BASE_URL = "http://127.0.0.1:8000/api/v1"

    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            session = Session()
            job_id = session.post(
                f"{BASE_URL}/monitors/{monitor_id}/jobs/start"
            ).json()["data"]["job_id"]

            exc = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                exc = e

            output = exc or result
            session.post(
                f"{BASE_URL}/monitors/{monitor_id}/jobs/{job_id}/finish",
                json={
                    "succeeded": exc is None,
                    "output": str(output) if output else None,
                },
            )
            if exc:
                raise exc

            return result

        return wrapper

    return decorator

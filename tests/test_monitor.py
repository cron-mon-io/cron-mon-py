"""Basic tests for the `monitor` decorator on the 'happy path'."""

import responses
from responses import matchers

from cron_mon import monitor


@responses.activate
def test_monitoring() -> None:
    """Test that the `monitor` decorator works as expected."""
    monitor_id = "a04376e2-0fb5-4949-9744-7c5d0a50b411"
    start_api_url = (
        f"http://mock.cron-mon.io/api/v1/monitors/{monitor_id}/jobs/start"
    )
    finish_api_url = f"http://mock.cron-mon.io/api/v1/monitors/{monitor_id}/jobs/12345/finish"
    responses.post(
        start_api_url,
        json={"data": {"job_id": "12345"}},
        match=[matchers.header_matcher({"X-API-Key": "mock-api-key"})],
    )
    responses.post(
        finish_api_url,
        json={"data": {}},
        match=[matchers.header_matcher({"X-API-Key": "mock-api-key"})],
    )

    @monitor(monitor_id)
    def cron_job() -> str:
        """A sample cron job."""
        return "Hello, world!"

    cron_job()

    assert [c.request.url for c in responses.calls] == [
        "http://mock.cron-mon.io/api/v1/monitors/a04376e2-0fb5-4949-9744-7c5d0a50b411/jobs/start",
        "http://mock.cron-mon.io/api/v1/monitors/a04376e2-0fb5-4949-9744-7c5d0a50b411/jobs/12345/finish",
    ]

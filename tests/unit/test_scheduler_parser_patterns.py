"""Pattern-matching path of ScheduleParser (no LLM involved)."""

import pytest

from muxi.runtime.services.scheduler.parser import ScheduleParser


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "text, expected",
    [
        ("every day at 3:30pm", "30 15 * * *"),
        ("daily at 9:15am", "15 9 * * *"),
        ("every monday at 10:45am", "45 10 * * 1"),
        ("every tuesday and thursday at 3:30pm", "30 15 * * 2,4"),
        ("every day at 12:05am", "5 0 * * *"),
        ("every day at 3pm", "0 15 * * *"),
        ("every day at 14:30", "30 14 * * *"),
    ],
)
async def test_twelve_hour_time_with_minutes(text, expected):
    assert await ScheduleParser()._try_pattern_matching(text) == expected

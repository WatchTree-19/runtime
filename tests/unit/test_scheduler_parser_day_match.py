"""Day-name extraction in ScheduleParser's pattern-matching path (no LLM)."""

import pytest

from muxi.runtime.services.scheduler.parser import ScheduleParser


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "text, expected",
    [
        ("monthly at 9am", "0 9 1 * *"),
        ("every 6 hours this month", "0 */6 * * *"),
        ("every 2 hours on mondays", "0 */2 * * 1"),
        ("every 2 hours on weekdays", "0 */2 * * 1-5"),
        ("every 30 minutes on sat", "*/30 * * * 6"),
        ("every 2 hours on thurs", "0 */2 * * 4"),
        ("every 2 hours on tues", "0 */2 * * 2"),
    ],
)
async def test_day_names_do_not_match_inside_other_words(text, expected):
    assert await ScheduleParser()._try_pattern_matching(text) == expected

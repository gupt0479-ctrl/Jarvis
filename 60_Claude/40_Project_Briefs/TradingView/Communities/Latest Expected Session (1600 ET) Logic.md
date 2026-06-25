---
type: community
cohesion: 0.14
members: 14
---

# Latest Expected Session (16:00 ET) Logic

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[.test_after_close_on_trading_day_returns_today()]] - code - tests/test_calendar.py
- [[.test_before_close_on_trading_day_returns_previous()]] - code - tests/test_calendar.py
- [[.test_defaults_to_nyse()]] - code - tests/test_calendar.py
- [[.test_exactly_at_close_returns_today()]] - code - tests/test_calendar.py
- [[.test_on_holiday_returns_previous_trading_day()]] - code - tests/test_calendar.py
- [[.test_on_weekend_returns_previous_friday()]] - code - tests/test_calendar.py
- [[After 1600 ET on a trading day, latest expected session is today.]] - rationale - tests/test_calendar.py
- [[At exactly 1600 ET on a trading day, today is the latest expected session.]] - rationale - tests/test_calendar.py
- [[Before 1600 ET on a trading day, latest expected session is previous trading da]] - rationale - tests/test_calendar.py
- [[On a holiday, latest expected session is the previous trading day.]] - rationale - tests/test_calendar.py
- [[On a weekend, latest expected session is the previous Friday.]] - rationale - tests/test_calendar.py
- [[Test get_latest_expected_session logic around 1600 ET.]] - rationale - tests/test_calendar.py
- [[TestLatestExpectedSession]] - code - tests/test_calendar.py
- [[When no exchange specified, should default to NYSE.]] - rationale - tests/test_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Latest_Expected_Session_1600_ET_Logic
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Market Calendar Unit Test Setup]]
- 1 edge to [[_COMMUNITY_MarketCalendar & CalendarError]]
- 1 edge to [[_COMMUNITY_Market Calendar Core]]

## Top bridge nodes
- [[TestLatestExpectedSession]] - degree 10, connects to 3 communities
---
type: community
cohesion: 0.14
members: 14
---

# Calendar Holiday Exclusion Tests

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[.test_christmas_excluded()]] - code - tests/test_calendar.py
- [[.test_holiday_week_has_fewer_sessions()]] - code - tests/test_calendar.py
- [[.test_independence_day_excluded()]] - code - tests/test_calendar.py
- [[.test_mlk_day_excluded()]] - code - tests/test_calendar.py
- [[.test_new_years_day_excluded()]] - code - tests/test_calendar.py
- [[.test_thanksgiving_excluded()]] - code - tests/test_calendar.py
- [[A week with a holiday should have fewer than 5 sessions.]] - rationale - tests/test_calendar.py
- [[Christmas Day (2024-12-25) should not be a trading session.]] - rationale - tests/test_calendar.py
- [[Independence Day (2024-07-04) should not be a trading session.]] - rationale - tests/test_calendar.py
- [[MLK Day (2024-01-15) should not be a trading session.]] - rationale - tests/test_calendar.py
- [[New Year's Day (2024-01-01) should not be a trading session.]] - rationale - tests/test_calendar.py
- [[Test that get_trading_sessions excludes known exchange holidays.]] - rationale - tests/test_calendar.py
- [[TestTradingSessionsExcludesHolidays]] - code - tests/test_calendar.py
- [[Thanksgiving (2024-11-28) should not be a trading session.]] - rationale - tests/test_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Calendar_Holiday_Exclusion_Tests
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Market Calendar Unit Test Setup]]
- 1 edge to [[_COMMUNITY_MarketCalendar & CalendarError]]
- 1 edge to [[_COMMUNITY_Market Calendar Core]]

## Top bridge nodes
- [[TestTradingSessionsExcludesHolidays]] - degree 10, connects to 3 communities
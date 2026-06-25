---
type: community
cohesion: 0.17
members: 12
---

# Trading Session Weekend Exclusion Tests

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[.test_single_saturday_returns_empty()]] - code - tests/test_calendar.py
- [[.test_single_sunday_returns_empty()]] - code - tests/test_calendar.py
- [[.test_two_weeks_no_holidays()]] - code - tests/test_calendar.py
- [[.test_week_with_no_holidays()]] - code - tests/test_calendar.py
- [[.test_weekend_only_range_returns_empty()]] - code - tests/test_calendar.py
- [[A normal week (Mon-Fri) should return 5 sessions, no weekends.]] - rationale - tests/test_calendar.py
- [[A range covering only Saturday and Sunday should return no sessions.]] - rationale - tests/test_calendar.py
- [[A single Saturday should return no sessions.]] - rationale - tests/test_calendar.py
- [[A single Sunday should return no sessions.]] - rationale - tests/test_calendar.py
- [[Test that get_trading_sessions never returns Saturday or Sunday.]] - rationale - tests/test_calendar.py
- [[TestTradingSessionsExcludesWeekends]] - code - tests/test_calendar.py
- [[Two full weeks should return 10 sessions.]] - rationale - tests/test_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Trading_Session_Weekend_Exclusion_Tests
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Market Calendar Unit Test Setup]]
- 1 edge to [[_COMMUNITY_MarketCalendar & CalendarError]]
- 1 edge to [[_COMMUNITY_Market Calendar Core]]

## Top bridge nodes
- [[TestTradingSessionsExcludesWeekends]] - degree 9, connects to 3 communities
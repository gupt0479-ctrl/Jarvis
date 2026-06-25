---
type: community
cohesion: 0.14
members: 14
---

# Missing Sessions Detection Tests

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[.test_all_missing_returns_all_expected()]] - code - tests/test_calendar.py
- [[.test_extra_dates_in_actual_ignored()]] - code - tests/test_calendar.py
- [[.test_missing_sessions_excludes_holidays()]] - code - tests/test_calendar.py
- [[.test_no_gaps_returns_empty()]] - code - tests/test_calendar.py
- [[.test_partial_gap_identified()]] - code - tests/test_calendar.py
- [[.test_supports_five_years_history()]] - code - tests/test_calendar.py
- [[Calendar should support at least 5 years of historical sessions.]] - rationale - tests/test_calendar.py
- [[Extra dates in actual_dates that aren't expected sessions are ignored.]] - rationale - tests/test_calendar.py
- [[Holidays should not appear in missing sessions.]] - rationale - tests/test_calendar.py
- [[Test that get_missing_sessions correctly identifies gaps in data.]] - rationale - tests/test_calendar.py
- [[TestGetMissingSessions]] - code - tests/test_calendar.py
- [[When all expected sessions are present, missing should be empty.]] - rationale - tests/test_calendar.py
- [[When no actual dates provided, all expected sessions are missing.]] - rationale - tests/test_calendar.py
- [[When some sessions are missing, they should be identified.]] - rationale - tests/test_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Missing_Sessions_Detection_Tests
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Market Calendar Unit Test Setup]]
- 1 edge to [[_COMMUNITY_MarketCalendar & CalendarError]]
- 1 edge to [[_COMMUNITY_Market Calendar Core]]

## Top bridge nodes
- [[TestGetMissingSessions]] - degree 10, connects to 3 communities
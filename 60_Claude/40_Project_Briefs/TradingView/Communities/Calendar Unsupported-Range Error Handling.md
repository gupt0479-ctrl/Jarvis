---
type: community
cohesion: 0.17
members: 12
---

# Calendar Unsupported-Range Error Handling

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[.test_far_future_date_raises_error()]] - code - tests/test_calendar.py
- [[.test_is_trading_day_unsupported_range()]] - code - tests/test_calendar.py
- [[.test_start_after_end_returns_empty()]] - code - tests/test_calendar.py
- [[.test_unsupported_exchange_raises_error()]] - code - tests/test_calendar.py
- [[.test_very_old_date_raises_error()]] - code - tests/test_calendar.py
- [[A date before the calendar's supported range should raise CalendarError.]] - rationale - tests/test_calendar.py
- [[A date far in the future beyond calendar range should raise CalendarError.]] - rationale - tests/test_calendar.py
- [[An unsupported exchange should raise CalendarError.]] - rationale - tests/test_calendar.py
- [[Test that CalendarError is raised for unsupported date ranges.]] - rationale - tests/test_calendar.py
- [[TestCalendarErrorUnsupportedRange]] - code - tests/test_calendar.py
- [[When start  end, should return empty list (not an error).]] - rationale - tests/test_calendar.py
- [[is_trading_day should raise CalendarError for dates outside supported range.]] - rationale - tests/test_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Calendar_Unsupported-Range_Error_Handling
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Market Calendar Unit Test Setup]]
- 1 edge to [[_COMMUNITY_MarketCalendar & CalendarError]]
- 1 edge to [[_COMMUNITY_Market Calendar Core]]

## Top bridge nodes
- [[TestCalendarErrorUnsupportedRange]] - degree 9, connects to 3 communities
---
type: community
cohesion: 0.14
members: 14
---

# Is-Trading-Day Tests

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[.test_friday_is_trading_day()]] - code - tests/test_calendar.py
- [[.test_holiday_is_not_trading_day()]] - code - tests/test_calendar.py
- [[.test_monday_is_trading_day()]] - code - tests/test_calendar.py
- [[.test_nasdaq_weekends_not_trading()]] - code - tests/test_calendar.py
- [[.test_saturday_is_not_trading_day()]] - code - tests/test_calendar.py
- [[.test_sunday_is_not_trading_day()]] - code - tests/test_calendar.py
- [[A known holiday should not be a trading day.]] - rationale - tests/test_calendar.py
- [[A regular Friday should be a trading day.]] - rationale - tests/test_calendar.py
- [[A regular Monday should be a trading day.]] - rationale - tests/test_calendar.py
- [[NASDAQ also doesn't trade on weekends.]] - rationale - tests/test_calendar.py
- [[Saturday should not be a trading day.]] - rationale - tests/test_calendar.py
- [[Sunday should not be a trading day.]] - rationale - tests/test_calendar.py
- [[Test is_trading_day correctly identifies non-trading days.]] - rationale - tests/test_calendar.py
- [[TestIsTradingDay]] - code - tests/test_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Is-Trading-Day_Tests
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Market Calendar Unit Test Setup]]
- 1 edge to [[_COMMUNITY_MarketCalendar & CalendarError]]
- 1 edge to [[_COMMUNITY_Market Calendar Core]]

## Top bridge nodes
- [[TestIsTradingDay]] - degree 10, connects to 3 communities
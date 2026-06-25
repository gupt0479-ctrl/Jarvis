---
type: community
cohesion: 0.13
members: 21
---

# Market Calendar Core

**Cohesion:** 0.13 - loosely connected
**Members:** 21 nodes

## Members
- [[.__init__()_3]] - code - src/research_data/calendar.py
- [[._validate_date_range()]] - code - src/research_data/calendar.py
- [[.get_missing_sessions()]] - code - src/research_data/calendar.py
- [[.get_trading_sessions()]] - code - src/research_data/calendar.py
- [[Determines expected trading sessions for US equity exchanges.      Supports NY]] - rationale - src/research_data/calendar.py
- [[Generate valid (start, end) date pairs within 2020-2025.]] - rationale - tests/test_property_market_calendar.py
- [[Initialize calendar instances for supported exchanges.]] - rationale - src/research_data/calendar.py
- [[MarketCalendar]] - code - src/research_data/calendar.py
- [[Property 6 Market Calendar Excludes Non-Trading Days.      Validates Requi]] - rationale - tests/test_property_market_calendar.py
- [[Property-based tests for Market Calendar (Property 6).  Property 6 Market Cal]] - rationale - tests/test_property_market_calendar.py
- [[Return expected trading sessions in the given date range.          Args]] - rationale - src/research_data/calendar.py
- [[Return trading sessions in the range that are not in actual_dates.          Ar]] - rationale - src/research_data/calendar.py
- [[TestProperty6MarketCalendarExcludesNonTradingDays]] - code - tests/test_property_market_calendar.py
- [[Validate that the requested date range is within the calendar's bounds.]] - rationale - src/research_data/calendar.py
- [[date_ranges()]] - code - tests/test_property_market_calendar.py
- [[test_all_sessions_within_requested_range()]] - code - tests/test_property_market_calendar.py
- [[test_known_holidays_excluded()]] - code - tests/test_property_market_calendar.py
- [[test_nasdaq_no_weekends()]] - code - tests/test_property_market_calendar.py
- [[test_no_weekends_in_trading_sessions()]] - code - tests/test_property_market_calendar.py
- [[test_property_market_calendar.py]] - code - tests/test_property_market_calendar.py
- [[test_sessions_are_sorted()]] - code - tests/test_property_market_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Market_Calendar_Core
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_MarketCalendar & CalendarError]]
- 2 edges to [[_COMMUNITY_Data Quality Auditor]]
- 1 edge to [[_COMMUNITY_Market Calendar Unit Test Setup]]
- 1 edge to [[_COMMUNITY_Trading Session Weekend Exclusion Tests]]
- 1 edge to [[_COMMUNITY_Calendar Holiday Exclusion Tests]]
- 1 edge to [[_COMMUNITY_Latest Expected Session (1600 ET) Logic]]
- 1 edge to [[_COMMUNITY_Is-Trading-Day Tests]]
- 1 edge to [[_COMMUNITY_Calendar Unsupported-Range Error Handling]]
- 1 edge to [[_COMMUNITY_Missing Sessions Detection Tests]]

## Top bridge nodes
- [[MarketCalendar]] - degree 24, connects to 9 communities
- [[.get_trading_sessions()]] - degree 5, connects to 1 community
- [[._validate_date_range()]] - degree 4, connects to 1 community
- [[TestProperty6MarketCalendarExcludesNonTradingDays]] - degree 4, connects to 1 community
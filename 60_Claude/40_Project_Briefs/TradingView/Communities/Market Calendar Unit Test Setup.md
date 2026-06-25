---
type: community
cohesion: 0.50
members: 4
---

# Market Calendar Unit Test Setup

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[Create a MarketCalendar instance for tests.]] - rationale - tests/test_calendar.py
- [[Unit tests for the market calendar module (Task 6.5).  Covers - get_trading_]] - rationale - tests/test_calendar.py
- [[calendar()]] - code - tests/test_calendar.py
- [[test_calendar.py]] - code - tests/test_calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Market_Calendar_Unit_Test_Setup
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Trading Session Weekend Exclusion Tests]]
- 1 edge to [[_COMMUNITY_Calendar Holiday Exclusion Tests]]
- 1 edge to [[_COMMUNITY_Latest Expected Session (1600 ET) Logic]]
- 1 edge to [[_COMMUNITY_Is-Trading-Day Tests]]
- 1 edge to [[_COMMUNITY_Calendar Unsupported-Range Error Handling]]
- 1 edge to [[_COMMUNITY_Missing Sessions Detection Tests]]
- 1 edge to [[_COMMUNITY_Market Calendar Core]]

## Top bridge nodes
- [[test_calendar.py]] - degree 8, connects to 6 communities
- [[calendar()]] - degree 3, connects to 1 community
---
type: community
cohesion: 0.20
members: 11
---

# MarketCalendar & CalendarError

**Cohesion:** 0.20 - loosely connected
**Members:** 11 nodes

## Members
- [[._get_calendar()]] - code - src/research_data/calendar.py
- [[.get_latest_expected_session()]] - code - src/research_data/calendar.py
- [[.is_trading_day()]] - code - src/research_data/calendar.py
- [[CalendarError]] - code - src/research_data/calendar.py
- [[Check if a given date is a trading day for the exchange.          Args]] - rationale - src/research_data/calendar.py
- [[Exception]] - code
- [[Get or create a calendar instance for the given exchange.          Args]] - rationale - src/research_data/calendar.py
- [[Market calendar for determining expected trading sessions.  Uses the exchange_]] - rationale - src/research_data/calendar.py
- [[Raised when a calendar operation fails due to unsupported date range or invalid]] - rationale - src/research_data/calendar.py
- [[Return the latest expected trading session as of now.          Logic]] - rationale - src/research_data/calendar.py
- [[calendar.py]] - code - src/research_data/calendar.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MarketCalendar__CalendarError
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Market Calendar Core]]
- 1 edge to [[_COMMUNITY_Trading Session Weekend Exclusion Tests]]
- 1 edge to [[_COMMUNITY_Calendar Holiday Exclusion Tests]]
- 1 edge to [[_COMMUNITY_Latest Expected Session (1600 ET) Logic]]
- 1 edge to [[_COMMUNITY_Is-Trading-Day Tests]]
- 1 edge to [[_COMMUNITY_Calendar Unsupported-Range Error Handling]]
- 1 edge to [[_COMMUNITY_Missing Sessions Detection Tests]]
- 1 edge to [[_COMMUNITY_InsufficientDataError]]
- 1 edge to [[_COMMUNITY_App Config Loading]]

## Top bridge nodes
- [[CalendarError]] - degree 13, connects to 7 communities
- [[Exception]] - degree 3, connects to 2 communities
- [[._get_calendar()]] - degree 6, connects to 1 community
- [[.is_trading_day()]] - degree 4, connects to 1 community
- [[.get_latest_expected_session()]] - degree 3, connects to 1 community
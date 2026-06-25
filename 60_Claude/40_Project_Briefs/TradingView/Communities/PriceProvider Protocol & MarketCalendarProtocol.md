---
type: community
cohesion: 0.22
members: 9
---

# PriceProvider Protocol & MarketCalendarProtocol

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[.fetch_daily_ohlcv()]] - code - src/research_data/providers/base.py
- [[.to_trading_date()]] - code - src/research_data/normalization.py
- [[Convert a datedatetime to the trading date in the exchange timezone.]] - rationale - src/research_data/normalization.py
- [[Fetch daily OHLCV data for a symbol within a date range.          Args]] - rationale - src/research_data/providers/base.py
- [[MarketCalendarProtocol]] - code - src/research_data/normalization.py
- [[PriceProvider]] - code - src/research_data/providers/base.py
- [[Protocol]] - code
- [[Protocol for market calendar implementations.      Used to derive trading_date]] - rationale - src/research_data/normalization.py
- [[Protocol that all data providers must implement.      Each provider exposes it]] - rationale - src/research_data/providers/base.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PriceProvider_Protocol__MarketCalendarProtocol
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Provider API-Key Validation]]
- 2 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 2 edges to [[_COMMUNITY_App Config Loading]]
- 1 edge to [[_COMMUNITY_Normalization Pipeline]]
- 1 edge to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 1 edge to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 1 edge to [[_COMMUNITY_ProviderCapabilities Model]]
- 1 edge to [[_COMMUNITY_Provider Registry Internals]]
- 1 edge to [[_COMMUNITY_CSV Fixture Provider]]

## Top bridge nodes
- [[PriceProvider]] - degree 10, connects to 6 communities
- [[MarketCalendarProtocol]] - degree 8, connects to 5 communities
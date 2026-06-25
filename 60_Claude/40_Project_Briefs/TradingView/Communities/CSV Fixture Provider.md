---
type: community
cohesion: 0.20
members: 12
---

# CSV Fixture Provider

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Members
- [[.__init__()_5]] - code - src/research_data/providers/csv_fixture.py
- [[._parse_row()]] - code - src/research_data/providers/csv_fixture.py
- [[.fetch_daily_ohlcv()_1]] - code - src/research_data/providers/csv_fixture.py
- [[CSV fixture provider for deterministic testing without network access.  Loads]] - rationale - src/research_data/providers/csv_fixture.py
- [[CSVFixtureProvider]] - code - src/research_data/providers/csv_fixture.py
- [[Fetch daily OHLCV data for a symbol from local CSV fixtures.          Args]] - rationale - src/research_data/providers/csv_fixture.py
- [[Initialize the CSV fixture provider.          Args             config Provi]] - rationale - src/research_data/providers/csv_fixture.py
- [[Map a provider config adjustment_policy string to PriceAdjustment enum.]] - rationale - src/research_data/providers/csv_fixture.py
- [[Parse a single CSV row into an OHLCVRecord.          This method intentionally]] - rationale - src/research_data/providers/csv_fixture.py
- [[Provider that loads deterministic sample data from local CSV fixtures.      Co]] - rationale - src/research_data/providers/csv_fixture.py
- [[_parse_adjustment_policy()]] - code - src/research_data/providers/csv_fixture.py
- [[csv_fixture.py]] - code - src/research_data/providers/csv_fixture.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CSV_Fixture_Provider
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 2 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 1 edge to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 1 edge to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 1 edge to [[_COMMUNITY_ProviderCapabilities Model]]
- 1 edge to [[_COMMUNITY_Provider API-Key Validation]]
- 1 edge to [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol]]
- 1 edge to [[_COMMUNITY_Provider Registry]]
- 1 edge to [[_COMMUNITY_Provider Registry Internals]]

## Top bridge nodes
- [[CSVFixtureProvider]] - degree 14, connects to 9 communities
- [[.fetch_daily_ohlcv()_1]] - degree 4, connects to 1 community
- [[._parse_row()]] - degree 4, connects to 1 community
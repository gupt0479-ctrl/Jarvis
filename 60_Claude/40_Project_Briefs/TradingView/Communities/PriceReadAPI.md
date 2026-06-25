---
type: community
cohesion: 0.25
members: 9
---

# PriceReadAPI

**Cohesion:** 0.25 - loosely connected
**Members:** 9 nodes

## Members
- [[.__init__()_2]] - code - src/research_data/read_api.py
- [[._row_to_record()]] - code - src/research_data/read_api.py
- [[.get_price_frame()]] - code - src/research_data/read_api.py
- [[Convert a DuckDB row tuple to an OHLCVRecord instance.]] - rationale - src/research_data/read_api.py
- [[Downstream-facing interface for reading time-ordered price frames.      Return]] - rationale - src/research_data/read_api.py
- [[PriceReadAPI]] - code - src/research_data/read_api.py
- [[Read API for downstream module consumption.  Provides typed access to time-ord]] - rationale - src/research_data/read_api.py
- [[Return time-ordered OHLCV rows with provenance and quality metadata.]] - rationale - src/research_data/read_api.py
- [[read_api.py]] - code - src/research_data/read_api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PriceReadAPI
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 2 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 2 edges to [[_COMMUNITY_InsufficientDataError]]
- 2 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]

## Top bridge nodes
- [[PriceReadAPI]] - degree 9, connects to 4 communities
- [[._row_to_record()]] - degree 6, connects to 3 communities
- [[.get_price_frame()]] - degree 4, connects to 1 community
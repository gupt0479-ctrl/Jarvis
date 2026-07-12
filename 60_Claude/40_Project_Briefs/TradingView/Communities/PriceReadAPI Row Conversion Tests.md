---
type: community
members: 11
---

# PriceReadAPI Row Conversion Tests

**Members:** 11 nodes

## Members
- [[._row_to_record()]] - code - src/research_data/read_api.py
- [[.get_price_frame()]] - code - src/research_data/read_api.py
- [[.test_price_adjustment_from_string()]] - code - tests/test_models.py
- [[.test_price_adjustment_invalid_value_raises()]] - code - tests/test_models.py
- [[Convert a DuckDB row tuple to an OHLCVRecord instance.]] - rationale - src/research_data/read_api.py
- [[OHLCVRecord_4]] - code
- [[PriceAdjustment]] - code - src/research_data/models.py
- [[PriceAdjustment_1]] - code
- [[Return time-ordered OHLCV rows with provenance and quality metadata.]] - rationale - src/research_data/read_api.py
- [[Type of price adjustment applied to OHLCV data.]] - rationale - src/research_data/models.py
- [[date_15]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PriceReadAPI_Row_Conversion_Tests
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Brain Model Enums & Ids]]
- 2 edges to [[_COMMUNITY_OHLCVRecord Model Validation Tests]]
- 2 edges to [[_COMMUNITY_FactorEngine & PriceReadAPI Core]]
- 2 edges to [[_COMMUNITY_Enum Serialization Tests]]
- 1 edge to [[_COMMUNITY_Core Models & Quality Auditor Modules]]
- 1 edge to [[_COMMUNITY_Quality Status Label Mapping]]
- 1 edge to [[_COMMUNITY_Adjustment Policy Mapping Tests]]
- 1 edge to [[_COMMUNITY_Provider-to-Canonical Normalizer]]
- 1 edge to [[_COMMUNITY_Provider Protocol & Capabilities]]
- 1 edge to [[_COMMUNITY_Benchmark Reporter Metrics]]
- 1 edge to [[_COMMUNITY_Duplicate PK Property Test]]
- 1 edge to [[_COMMUNITY_Quality Status Classification Property Test]]
- 1 edge to [[_COMMUNITY_Data Quality Auditor Unit Tests]]
- 1 edge to [[_COMMUNITY_DuckDB Batch Upsert Tests]]
- 1 edge to [[_COMMUNITY_Insufficient-Data Error Tests]]

## Top bridge nodes
- [[PriceAdjustment]] - degree 16, connects to 10 communities
- [[.get_price_frame()]] - degree 9, connects to 3 communities
- [[._row_to_record()]] - degree 8, connects to 3 communities
- [[.test_price_adjustment_from_string()]] - degree 2, connects to 1 community
- [[.test_price_adjustment_invalid_value_raises()]] - degree 2, connects to 1 community
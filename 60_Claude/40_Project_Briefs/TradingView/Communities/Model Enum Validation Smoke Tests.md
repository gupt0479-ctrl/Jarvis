---
type: community
cohesion: 0.33
members: 6
---

# Model Enum Validation Smoke Tests

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[.test_enum_is_str()]] - code - tests/test_models_validation.py
- [[.test_price_adjustment_values()]] - code - tests/test_models_validation.py
- [[.test_quality_status_values()]] - code - tests/test_models_validation.py
- [[Quick validation tests for models.py to verify task 1.2 implementation.]] - rationale - tests/test_models_validation.py
- [[TestEnumerations]] - code - tests/test_models_validation.py
- [[test_models_validation.py]] - code - tests/test_models_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Model_Enum_Validation_Smoke_Tests
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 3 edges to [[_COMMUNITY_Evidence Packet Models]]
- 2 edges to [[_COMMUNITY_InsufficientDataError]]
- 2 edges to [[_COMMUNITY_ProviderCapabilities Model]]
- 2 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 2 edges to [[_COMMUNITY_DataQualityReport Model]]
- 1 edge to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 1 edge to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]

## Top bridge nodes
- [[TestEnumerations]] - degree 13, connects to 8 communities
- [[test_models_validation.py]] - degree 10, connects to 6 communities
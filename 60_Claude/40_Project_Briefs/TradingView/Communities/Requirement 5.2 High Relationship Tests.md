---
type: community
cohesion: 0.50
members: 4
---

# Requirement 5.2: High Relationship Tests

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[.test_high_less_than_close_rejected()]] - code - tests/test_models.py
- [[.test_high_less_than_open_rejected()]] - code - tests/test_models.py
- [[Requirement 5.2 high must be = open, close, low.]] - rationale - tests/test_models.py
- [[TestValidationHighRelationships]] - code - tests/test_models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Requirement_52_High_Relationship_Tests
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 2 edges to [[_COMMUNITY_Evidence Packet Models]]
- 1 edge to [[_COMMUNITY_DataQualityReport Model]]
- 1 edge to [[_COMMUNITY_InsufficientDataError]]
- 1 edge to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 1 edge to [[_COMMUNITY_ProviderCapabilities Model]]
- 1 edge to [[_COMMUNITY_ProviderFetchResult Model]]
- 1 edge to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]

## Top bridge nodes
- [[TestValidationHighRelationships]] - degree 13, connects to 8 communities
- [[.test_high_less_than_close_rejected()]] - degree 3, connects to 1 community
- [[.test_high_less_than_open_rejected()]] - degree 3, connects to 1 community
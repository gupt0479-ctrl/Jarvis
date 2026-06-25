---
type: community
cohesion: 0.31
members: 10
---

# DataEvidencePacket Construction Tests

**Cohesion:** 0.31 - loosely connected
**Members:** 10 nodes

## Members
- [[._make_packet()]] - code - tests/test_models.py
- [[.test_confidence_cap_bounds()_1]] - code - tests/test_models.py
- [[.test_full_construction()_2]] - code - tests/test_models.py
- [[.test_json_round_trip()]] - code - tests/test_models.py
- [[.test_json_round_trip_with_empty_refs()]] - code - tests/test_models.py
- [[.test_stale_quality_status()]] - code - tests/test_models.py
- [[Serialize to JSON and deserialize back, verify equivalence.]] - rationale - tests/test_models.py
- [[Test DataEvidencePacket construction and JSON serialization.]] - rationale - tests/test_models.py
- [[TestDataEvidencePacket]] - code - tests/test_models.py
- [[confidence_cap must be between 0.0 and 1.0._1]] - rationale - tests/test_models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DataEvidencePacket_Construction_Tests
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Evidence Packet Models]]
- 2 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 1 edge to [[_COMMUNITY_DataQualityReport Model]]
- 1 edge to [[_COMMUNITY_InsufficientDataError]]
- 1 edge to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 1 edge to [[_COMMUNITY_ProviderCapabilities Model]]
- 1 edge to [[_COMMUNITY_ProviderFetchResult Model]]
- 1 edge to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]

## Top bridge nodes
- [[TestDataEvidencePacket]] - degree 17, connects to 8 communities
- [[._make_packet()]] - degree 8, connects to 1 community
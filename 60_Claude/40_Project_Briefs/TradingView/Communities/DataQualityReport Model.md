---
type: community
cohesion: 0.29
members: 10
---

# DataQualityReport Model

**Cohesion:** 0.29 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_confidence_cap_bounds()]] - code - tests/test_models.py
- [[.test_construction()_3]] - code - tests/test_models_validation.py
- [[.test_full_construction()_1]] - code - tests/test_models.py
- [[.test_missing_status_zero_confidence()]] - code - tests/test_models.py
- [[DataQualityReport]] - code - src/research_data/models.py
- [[Per-symbol quality report generated after an ingestion run.]] - rationale - src/research_data/models.py
- [[Test DataQualityReport model construction.]] - rationale - tests/test_models.py
- [[TestDataQualityReport_1]] - code - tests/test_models.py
- [[TestDataQualityReport]] - code - tests/test_models_validation.py
- [[confidence_cap must be between 0.0 and 1.0.]] - rationale - tests/test_models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DataQualityReport_Model
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 8 edges to [[_COMMUNITY_Evidence Packet Models]]
- 4 edges to [[_COMMUNITY_InsufficientDataError]]
- 4 edges to [[_COMMUNITY_ProviderCapabilities Model]]
- 4 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 3 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 3 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 2 edges to [[_COMMUNITY_Model Enum Validation Smoke Tests]]
- 2 edges to [[_COMMUNITY_Data Quality Auditor]]
- 1 edge to [[_COMMUNITY_Requirement 5.2 High Relationship Tests]]
- 1 edge to [[_COMMUNITY_Raw Payload Hash Validation Tests]]
- 1 edge to [[_COMMUNITY_DataEvidencePacket Construction Tests]]

## Top bridge nodes
- [[DataQualityReport]] - degree 32, connects to 12 communities
- [[TestDataQualityReport]] - degree 11, connects to 8 communities
- [[TestDataQualityReport_1]] - degree 14, connects to 7 communities
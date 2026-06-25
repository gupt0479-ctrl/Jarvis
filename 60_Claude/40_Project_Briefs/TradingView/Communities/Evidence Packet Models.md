---
type: community
cohesion: 0.17
members: 17
---

# Evidence Packet Models

**Cohesion:** 0.17 - loosely connected
**Members:** 17 nodes

## Members
- [[.test_evidence_packet_construction()]] - code - tests/test_models_validation.py
- [[.test_evidence_packet_json_serialization()]] - code - tests/test_models_validation.py
- [[.test_evidence_ref_construction()]] - code - tests/test_models_validation.py
- [[.test_large_negative_volume_rejected()]] - code - tests/test_models.py
- [[.test_low_greater_than_close_rejected()]] - code - tests/test_models.py
- [[.test_low_greater_than_open_rejected()]] - code - tests/test_models.py
- [[.test_negative_volume_rejected()]] - code - tests/test_models.py
- [[BaseModel]] - code
- [[DataEvidencePacket]] - code - src/research_data/models.py
- [[EvidenceRef]] - code - src/research_data/models.py
- [[Reference to a specific row in a data table for provenance tracking.]] - rationale - src/research_data/models.py
- [[Requirement 5.3 low must be = open, close.]] - rationale - tests/test_models.py
- [[Requirement 5.4 volume must be = 0.]] - rationale - tests/test_models.py
- [[Structured evidence packet with full provenance for downstream AI consumption.]] - rationale - src/research_data/models.py
- [[TestEvidenceModels]] - code - tests/test_models_validation.py
- [[TestValidationLowRelationships]] - code - tests/test_models.py
- [[TestValidationVolume]] - code - tests/test_models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Evidence_Packet_Models
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 8 edges to [[_COMMUNITY_ProviderCapabilities Model]]
- 8 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 8 edges to [[_COMMUNITY_DataQualityReport Model]]
- 7 edges to [[_COMMUNITY_InsufficientDataError]]
- 5 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 5 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 4 edges to [[_COMMUNITY_DataEvidencePacket Construction Tests]]
- 3 edges to [[_COMMUNITY_Model Enum Validation Smoke Tests]]
- 2 edges to [[_COMMUNITY_Requirement 5.2 High Relationship Tests]]
- 2 edges to [[_COMMUNITY_Raw Payload Hash Validation Tests]]

## Top bridge nodes
- [[DataEvidencePacket]] - degree 29, connects to 11 communities
- [[EvidenceRef]] - degree 29, connects to 11 communities
- [[TestEvidenceModels]] - degree 13, connects to 8 communities
- [[TestValidationLowRelationships]] - degree 13, connects to 7 communities
- [[TestValidationVolume]] - degree 13, connects to 7 communities
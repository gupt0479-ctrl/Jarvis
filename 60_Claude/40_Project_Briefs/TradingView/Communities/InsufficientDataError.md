---
type: community
cohesion: 0.23
members: 12
---

# InsufficientDataError

**Cohesion:** 0.23 - loosely connected
**Members:** 12 nodes

## Members
- [[.__init__()]] - code - src/research_data/models.py
- [[.test_can_be_raised_and_caught()]] - code - tests/test_models.py
- [[.test_construction()]] - code - tests/test_models_validation.py
- [[.test_construction_and_attributes()]] - code - tests/test_models.py
- [[.test_is_exception()]] - code - tests/test_models_validation.py
- [[.test_is_exception_subclass()]] - code - tests/test_models.py
- [[.test_message_contains_details()]] - code - tests/test_models.py
- [[InsufficientDataError]] - code - src/research_data/models.py
- [[Raised when a symbol has fewer rows than required for the requested operation.]] - rationale - src/research_data/models.py
- [[Test InsufficientDataError exception class.]] - rationale - tests/test_models.py
- [[TestInsufficientDataError_1]] - code - tests/test_models.py
- [[TestInsufficientDataError]] - code - tests/test_models_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/InsufficientDataError
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 7 edges to [[_COMMUNITY_Evidence Packet Models]]
- 4 edges to [[_COMMUNITY_ProviderCapabilities Model]]
- 4 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 4 edges to [[_COMMUNITY_DataQualityReport Model]]
- 3 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 3 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 2 edges to [[_COMMUNITY_Model Enum Validation Smoke Tests]]
- 2 edges to [[_COMMUNITY_Data Quality Auditor]]
- 2 edges to [[_COMMUNITY_PriceReadAPI]]
- 1 edge to [[_COMMUNITY_Requirement 5.2 High Relationship Tests]]
- 1 edge to [[_COMMUNITY_Raw Payload Hash Validation Tests]]
- 1 edge to [[_COMMUNITY_DataEvidencePacket Construction Tests]]
- 1 edge to [[_COMMUNITY_MarketCalendar & CalendarError]]

## Top bridge nodes
- [[InsufficientDataError]] - degree 33, connects to 13 communities
- [[TestInsufficientDataError]] - degree 12, connects to 8 communities
- [[TestInsufficientDataError_1]] - degree 15, connects to 7 communities
- [[.test_message_contains_details()]] - degree 3, connects to 1 community
- [[.test_construction()]] - degree 3, connects to 1 community
---
type: community
cohesion: 0.33
members: 9
---

# ProviderCapabilities Model

**Cohesion:** 0.33 - loosely connected
**Members:** 9 nodes

## Members
- [[.test_construction()_1]] - code - tests/test_models_validation.py
- [[.test_experimental_flag()]] - code - tests/test_models.py
- [[.test_full_construction()]] - code - tests/test_models.py
- [[.test_optional_fields_default_none()]] - code - tests/test_models.py
- [[Describes the capabilities and constraints of a data provider.]] - rationale - src/research_data/models.py
- [[ProviderCapabilities]] - code - src/research_data/models.py
- [[Test ProviderCapabilities model construction and defaults.]] - rationale - tests/test_models.py
- [[TestProviderCapabilities_1]] - code - tests/test_models.py
- [[TestProviderCapabilities]] - code - tests/test_models_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProviderCapabilities_Model
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 8 edges to [[_COMMUNITY_Evidence Packet Models]]
- 4 edges to [[_COMMUNITY_InsufficientDataError]]
- 4 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 4 edges to [[_COMMUNITY_DataQualityReport Model]]
- 3 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 3 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 2 edges to [[_COMMUNITY_Model Enum Validation Smoke Tests]]
- 1 edge to [[_COMMUNITY_Requirement 5.2 High Relationship Tests]]
- 1 edge to [[_COMMUNITY_Raw Payload Hash Validation Tests]]
- 1 edge to [[_COMMUNITY_DataEvidencePacket Construction Tests]]
- 1 edge to [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol]]
- 1 edge to [[_COMMUNITY_Provider Registry]]
- 1 edge to [[_COMMUNITY_CSV Fixture Provider]]
- 1 edge to [[_COMMUNITY_Provider Registry Internals]]

## Top bridge nodes
- [[ProviderCapabilities]] - degree 34, connects to 15 communities
- [[TestProviderCapabilities]] - degree 11, connects to 8 communities
- [[TestProviderCapabilities_1]] - degree 14, connects to 7 communities
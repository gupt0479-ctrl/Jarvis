---
type: community
cohesion: 0.27
members: 10
---

# ProviderFetchResult Model

**Cohesion:** 0.27 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_construction()_2]] - code - tests/test_models_validation.py
- [[.test_empty_result_defaults()]] - code - tests/test_models.py
- [[.test_full_construction_with_records()]] - code - tests/test_models.py
- [[Property 11 No Data Fabrication on Empty Provider Response.      For any prov]] - rationale - tests/test_property_no_fabrication.py
- [[ProviderFetchResult]] - code - src/research_data/models.py
- [[Result of a provider fetch operation including raw payload and parsed records.]] - rationale - src/research_data/models.py
- [[Test ProviderFetchResult model construction and defaults.]] - rationale - tests/test_models.py
- [[TestProperty11NoDataFabrication]] - code - tests/test_property_no_fabrication.py
- [[TestProviderFetchResult_1]] - code - tests/test_models.py
- [[TestProviderFetchResult]] - code - tests/test_models_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProviderFetchResult_Model
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 10 edges to [[_COMMUNITY_Normalization Pipeline]]
- 8 edges to [[_COMMUNITY_Evidence Packet Models]]
- 4 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 4 edges to [[_COMMUNITY_Data Quality Auditor]]
- 4 edges to [[_COMMUNITY_InsufficientDataError]]
- 4 edges to [[_COMMUNITY_ProviderCapabilities Model]]
- 4 edges to [[_COMMUNITY_DataQualityReport Model]]
- 4 edges to [[_COMMUNITY_AssetUniverse Config & DuckDB Storage]]
- 3 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 3 edges to [[_COMMUNITY_DuckDB Schema Init & Duplicate-PK Handling]]
- 2 edges to [[_COMMUNITY_Adjustment Policy Mapping Tests]]
- 2 edges to [[_COMMUNITY_Model Enum Validation Smoke Tests]]
- 2 edges to [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol]]
- 2 edges to [[_COMMUNITY_CSV Fixture Provider]]
- 1 edge to [[_COMMUNITY_Provider API-Key Validation]]
- 1 edge to [[_COMMUNITY_Requirement 5.2 High Relationship Tests]]
- 1 edge to [[_COMMUNITY_Raw Payload Hash Validation Tests]]
- 1 edge to [[_COMMUNITY_DataEvidencePacket Construction Tests]]
- 1 edge to [[_COMMUNITY_Secret Redaction]]
- 1 edge to [[_COMMUNITY_Provider Registry]]

## Top bridge nodes
- [[ProviderFetchResult]] - degree 58, connects to 20 communities
- [[TestProviderFetchResult]] - degree 11, connects to 8 communities
- [[TestProviderFetchResult_1]] - degree 13, connects to 7 communities
- [[TestProperty11NoDataFabrication]] - degree 5, connects to 3 communities
- [[.test_full_construction_with_records()]] - degree 4, connects to 1 community
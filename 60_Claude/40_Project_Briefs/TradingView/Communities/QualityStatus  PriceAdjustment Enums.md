---
type: community
cohesion: 0.13
members: 17
---

# QualityStatus / PriceAdjustment Enums

**Cohesion:** 0.13 - loosely connected
**Members:** 17 nodes

## Members
- [[.test_enum_in_model_json_serialization()]] - code - tests/test_models.py
- [[.test_price_adjustment_from_string()]] - code - tests/test_models.py
- [[.test_price_adjustment_invalid_value_raises()]] - code - tests/test_models.py
- [[.test_price_adjustment_is_str_subclass()]] - code - tests/test_models.py
- [[.test_price_adjustment_to_string()]] - code - tests/test_models.py
- [[.test_quality_status_from_string()]] - code - tests/test_models.py
- [[.test_quality_status_invalid_value_raises()]] - code - tests/test_models.py
- [[.test_quality_status_is_str_subclass()]] - code - tests/test_models.py
- [[.test_quality_status_to_string()]] - code - tests/test_models.py
- [[Classification of data quality for a symbol or record.]] - rationale - src/research_data/models.py
- [[Enum .value gives the serialized string form.]] - rationale - tests/test_models.py
- [[Enum .value gives the serialized string form._1]] - rationale - tests/test_models.py
- [[PriceAdjustment inherits from str, so it can be compared to its value.]] - rationale - tests/test_models.py
- [[QualityStatus]] - code - src/research_data/models.py
- [[QualityStatus inherits from str, so it can be compared to its value.]] - rationale - tests/test_models.py
- [[Test enum serialization (to string) and deserialization (from string).]] - rationale - tests/test_models.py
- [[TestEnumSerialization]] - code - tests/test_models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/QualityStatus_/_PriceAdjustment_Enums
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 5 edges to [[_COMMUNITY_Normalization Pipeline]]
- 5 edges to [[_COMMUNITY_Evidence Packet Models]]
- 5 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 4 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 4 edges to [[_COMMUNITY_AssetUniverse Config & DuckDB Storage]]
- 3 edges to [[_COMMUNITY_DuckDB Schema Init & Duplicate-PK Handling]]
- 3 edges to [[_COMMUNITY_InsufficientDataError]]
- 3 edges to [[_COMMUNITY_ProviderCapabilities Model]]
- 3 edges to [[_COMMUNITY_DataQualityReport Model]]
- 3 edges to [[_COMMUNITY_Data Quality Auditor]]
- 2 edges to [[_COMMUNITY_Adjustment Policy Mapping Tests]]
- 2 edges to [[_COMMUNITY_PriceReadAPI]]
- 1 edge to [[_COMMUNITY_Model Enum Validation Smoke Tests]]
- 1 edge to [[_COMMUNITY_Requirement 5.2 High Relationship Tests]]
- 1 edge to [[_COMMUNITY_Raw Payload Hash Validation Tests]]
- 1 edge to [[_COMMUNITY_DataEvidencePacket Construction Tests]]
- 1 edge to [[_COMMUNITY_Secret Redaction]]
- 1 edge to [[_COMMUNITY_CSV Fixture Provider]]

## Top bridge nodes
- [[QualityStatus]] - degree 51, connects to 19 communities
- [[TestEnumSerialization]] - degree 21, connects to 7 communities
- [[.test_enum_in_model_json_serialization()]] - degree 3, connects to 1 community
- [[.test_price_adjustment_from_string()]] - degree 2, connects to 1 community
- [[.test_price_adjustment_invalid_value_raises()]] - degree 2, connects to 1 community
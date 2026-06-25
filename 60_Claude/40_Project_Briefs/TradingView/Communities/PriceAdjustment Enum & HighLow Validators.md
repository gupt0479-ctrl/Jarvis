---
type: community
cohesion: 0.18
members: 12
---

# PriceAdjustment Enum & High/Low Validators

**Cohesion:** 0.18 - loosely connected
**Members:** 12 nodes

## Members
- [[Enum]] - code
- [[PriceAdjustment]] - code - src/research_data/models.py
- [[Pydantic models, enumerations, and validation rules for the research data system]] - rationale - src/research_data/models.py
- [[Type of price adjustment applied to OHLCV data.]] - rationale - src/research_data/models.py
- [[models.py]] - code - src/research_data/models.py
- [[validate_adjusted_close()]] - code - src/research_data/models.py
- [[validate_high_low_relationships()]] - code - src/research_data/models.py
- [[validate_no_future_dates()]] - code - src/research_data/models.py
- [[validate_non_negative_volume()]] - code - src/research_data/models.py
- [[validate_positive_prices()]] - code - src/research_data/models.py
- [[validate_raw_payload_hash()]] - code - src/research_data/models.py
- [[validate_symbol()]] - code - src/research_data/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PriceAdjustment_Enum__High/Low_Validators
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 7 edges to [[_COMMUNITY_Normalization Pipeline]]
- 5 edges to [[_COMMUNITY_Evidence Packet Models]]
- 5 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 4 edges to [[_COMMUNITY_AssetUniverse Config & DuckDB Storage]]
- 3 edges to [[_COMMUNITY_Adjustment Policy Mapping Tests]]
- 3 edges to [[_COMMUNITY_DuckDB Schema Init & Duplicate-PK Handling]]
- 3 edges to [[_COMMUNITY_InsufficientDataError]]
- 3 edges to [[_COMMUNITY_ProviderCapabilities Model]]
- 3 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 3 edges to [[_COMMUNITY_DataQualityReport Model]]
- 3 edges to [[_COMMUNITY_Data Quality Auditor]]
- 2 edges to [[_COMMUNITY_PriceReadAPI]]
- 1 edge to [[_COMMUNITY_Model Enum Validation Smoke Tests]]
- 1 edge to [[_COMMUNITY_Requirement 5.2 High Relationship Tests]]
- 1 edge to [[_COMMUNITY_Raw Payload Hash Validation Tests]]
- 1 edge to [[_COMMUNITY_DataEvidencePacket Construction Tests]]
- 1 edge to [[_COMMUNITY_Secret Redaction]]
- 1 edge to [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol]]
- 1 edge to [[_COMMUNITY_CSV Fixture Provider]]

## Top bridge nodes
- [[PriceAdjustment]] - degree 54, connects to 20 communities
- [[models.py]] - degree 18, connects to 7 communities
- [[Enum]] - degree 3, connects to 1 community
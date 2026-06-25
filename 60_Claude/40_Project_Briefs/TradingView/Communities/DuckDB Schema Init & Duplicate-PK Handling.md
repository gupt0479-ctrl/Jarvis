---
type: community
cohesion: 0.06
members: 37
---

# DuckDB Schema Init & Duplicate-PK Handling

**Cohesion:** 0.06 - loosely connected
**Members:** 37 nodes

## Members
- [[.test_creates_all_tables()]] - code - tests/test_storage.py
- [[.test_creates_exactly_six_tables()]] - code - tests/test_storage.py
- [[.test_daily_ohlcv_has_primary_key()]] - code - tests/test_storage.py
- [[.test_idempotent_preserves_data()]] - code - tests/test_storage.py
- [[Calling init_db twice should not destroy existing data.]] - rationale - tests/test_storage.py
- [[Create all required tables and indexes using CREATE TABLE IF NOT EXISTS.]] - rationale - src/research_data/storage.py
- [[Create an in-memory DuckDB connection with schema initialized.]] - rationale - tests/test_storage.py
- [[Generate a dict with at least one secret field and at least one non-secret field]] - rationale - tests/test_property_no_secrets.py
- [[Generate a valid OHLCVRecord with consistent OHLC relationships.      Ensures]] - rationale - tests/test_property_roundtrip.py
- [[Generate a valid OHLCVRecord with optional fixed PK fields.]] - rationale - tests/test_property_duplicate_pk.py
- [[Generate valid OHLC prices satisfying high = openclose = low.]] - rationale - tests/test_property_duplicate_pk.py
- [[Property 12 Duplicate Primary Key Rejection.      When two records share the]] - rationale - tests/test_property_duplicate_pk.py
- [[Property 13 No Secrets in Stored Metadata.      For any request metadata with]] - rationale - tests/test_property_no_secrets.py
- [[Property 2 OHLCV Round-Trip Integrity.      For any valid OHLCVRecord that pa]] - rationale - tests/test_property_roundtrip.py
- [[Property-based tests for OHLCV round-trip integrity (Property 2).  Property 2]] - rationale - tests/test_property_roundtrip.py
- [[Property-based tests for duplicate primary key handling (Property 12).  Proper]] - rationale - tests/test_property_duplicate_pk.py
- [[Property-based tests for no secrets in stored metadata (Property 13).  Propert]] - rationale - tests/test_property_no_secrets.py
- [[Test that init_db creates all required tables. Requirement 8.1.]] - rationale - tests/test_storage.py
- [[TestInitDb]] - code - tests/test_storage.py
- [[TestProperty12DuplicatePrimaryKeyHandling]] - code - tests/test_property_duplicate_pk.py
- [[TestProperty13NoSecretsInStoredMetadata]] - code - tests/test_property_no_secrets.py
- [[TestProperty2OHLCVRoundTripIntegrity]] - code - tests/test_property_roundtrip.py
- [[daily_ohlcv should have composite primary key (symbol, trading_date, source, pri]] - rationale - tests/test_storage.py
- [[db()]] - code - tests/test_storage.py
- [[init_db should create all 6 required tables.]] - rationale - tests/test_storage.py
- [[init_db should create exactly 6 tables.]] - rationale - tests/test_storage.py
- [[init_db()]] - code - src/research_data/storage.py
- [[ohlcv_prices()]] - code - tests/test_property_duplicate_pk.py
- [[request_params_with_secrets()]] - code - tests/test_property_no_secrets.py
- [[test_property_duplicate_pk.py]] - code - tests/test_property_duplicate_pk.py
- [[test_property_no_secrets.py]] - code - tests/test_property_no_secrets.py
- [[test_property_roundtrip.py]] - code - tests/test_property_roundtrip.py
- [[test_roundtrip_preserves_all_fields()]] - code - tests/test_property_roundtrip.py
- [[test_secrets_redacted_in_stored_metadata()]] - code - tests/test_property_no_secrets.py
- [[test_upsert_overwrites_duplicate_pk()]] - code - tests/test_property_duplicate_pk.py
- [[valid_ohlcv_record()]] - code - tests/test_property_duplicate_pk.py
- [[valid_ohlcv_records()]] - code - tests/test_property_roundtrip.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DuckDB_Schema_Init__Duplicate-PK_Handling
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_AssetUniverse Config & DuckDB Storage]]
- 6 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 3 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 3 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 3 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 2 edges to [[_COMMUNITY_Data Quality Auditor]]
- 1 edge to [[_COMMUNITY_App Config Loading]]
- 1 edge to [[_COMMUNITY_Provider API-Key Validation]]

## Top bridge nodes
- [[TestInitDb]] - degree 14, connects to 7 communities
- [[TestProperty12DuplicatePrimaryKeyHandling]] - degree 5, connects to 3 communities
- [[TestProperty2OHLCVRoundTripIntegrity]] - degree 5, connects to 3 communities
- [[init_db()]] - degree 11, connects to 2 communities
- [[test_upsert_overwrites_duplicate_pk()]] - degree 4, connects to 2 communities
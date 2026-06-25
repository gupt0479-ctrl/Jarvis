---
type: community
cohesion: 0.05
members: 65
---

# Data Quality Auditor

**Cohesion:** 0.05 - loosely connected
**Members:** 65 nodes

## Members
- [[.__init__()_1]] - code - src/research_data/quality.py
- [[._check_contradictory_ohlc()]] - code - src/research_data/quality.py
- [[._check_duplicate_dates()]] - code - src/research_data/quality.py
- [[._check_non_monotonic_dates()]] - code - src/research_data/quality.py
- [[._check_stale()]] - code - src/research_data/quality.py
- [[._check_unknown_adjustment()]] - code - src/research_data/quality.py
- [[.audit_symbol()]] - code - src/research_data/quality.py
- [[.detect_cross_provider_disagreement()]] - code - src/research_data/quality.py
- [[.test_computes_correct_sha256_hash()]] - code - tests/test_storage.py
- [[.test_csv_format_detection()]] - code - tests/test_storage.py
- [[.test_file_content_matches_payload()]] - code - tests/test_storage.py
- [[.test_json_array_format_detection()]] - code - tests/test_storage.py
- [[.test_never_overwrites_existing_file()]] - code - tests/test_storage.py
- [[.test_raises_on_file_write_failure()]] - code - tests/test_storage.py
- [[.test_records_in_raw_market_payloads_table()]] - code - tests/test_storage.py
- [[.test_redacts_secrets_in_stored_params()]] - code - tests/test_storage.py
- [[.test_returns_content_hash()]] - code - tests/test_storage.py
- [[.test_skips_duplicate_hash_for_same_symbol_source()]] - code - tests/test_storage.py
- [[.test_writes_file_to_correct_path()]] - code - tests/test_storage.py
- [[CSV content should be detected and stored with .csv extension.]] - rationale - tests/test_storage.py
- [[Check if the latest bar is older than the latest expected session.          Ar]] - rationale - src/research_data/quality.py
- [[Compare OHLCV fields between two providers for the same symboldate.]] - rationale - src/research_data/quality.py
- [[Create a ProviderFetchResult for testing.]] - rationale - tests/test_storage.py
- [[Data Quality Auditor for the research data system.  Evaluates symbol-level and]] - rationale - src/research_data/quality.py
- [[DataQualityAuditor]] - code - src/research_data/quality.py
- [[Detect duplicate trading_dates in the records.          Returns]] - rationale - src/research_data/quality.py
- [[Detect non-monotonic (out-of-order) trading_dates.          Checks that dates]] - rationale - src/research_data/quality.py
- [[Detect records where price_adjustment is UNKNOWN.          Returns]] - rationale - src/research_data/quality.py
- [[Detect records with impossible OHLC relationships.          Checks for]] - rationale - src/research_data/quality.py
- [[Evaluates symbol-level data quality and generates quality reports.      Uses M]] - rationale - src/research_data/quality.py
- [[Existing raw payload files should never be overwritten.]] - rationale - tests/test_storage.py
- [[Generate a ProviderFetchResult with a random raw payload.]] - rationale - tests/test_property_raw_payload_hash.py
- [[Generate a provider config dict with a random non-empty subset of required field]] - rationale - tests/test_property_provider_registry.py
- [[Generate a quality report for a symbol after ingestion.          Takes normali]] - rationale - src/research_data/quality.py
- [[If file write fails, an IOError should be raised.]] - rationale - tests/test_storage.py
- [[If hash already exists for same symbolsource, skip insert and return hash.]] - rationale - tests/test_storage.py
- [[Initialize the auditor with an optional MarketCalendar instance.          Args]] - rationale - src/research_data/quality.py
- [[JSON array content should be detected as json format.]] - rationale - tests/test_storage.py
- [[Payload metadata should be recorded in raw_market_payloads table.]] - rationale - tests/test_storage.py
- [[Property 10 Provider Registry Rejects Invalid Configuration.      For any pro]] - rationale - tests/test_property_provider_registry.py
- [[Property 3 Raw Payload Hash Consistency.      For any raw payload written to]] - rationale - tests/test_property_raw_payload_hash.py
- [[Property-based tests for provider registry validation (Property 10).  Property]] - rationale - tests/test_property_provider_registry.py
- [[Property-based tests for raw payload hash consistency (Property 3).  Property]] - rationale - tests/test_property_raw_payload_hash.py
- [[Raw payload should be written to the correct directory structure.]] - rationale - tests/test_storage.py
- [[Returned hash should be the SHA-256 of the raw payload.]] - rationale - tests/test_storage.py
- [[Secret fields in request_params should be redacted in stored metadata.]] - rationale - tests/test_storage.py
- [[Test raw payload writer. Requirements 3.1-3.7, 14.2.]] - rationale - tests/test_storage.py
- [[TestProperty10ProviderRegistryRejectsInvalidConfig]] - code - tests/test_property_provider_registry.py
- [[TestProperty3RawPayloadHashConsistency]] - code - tests/test_property_raw_payload_hash.py
- [[TestWriteRawPayload]] - code - tests/test_storage.py
- [[Write a providers.toml file with a single provider entry.]] - rationale - tests/test_property_provider_registry.py
- [[Write a raw provider payload to disk and record it in the database.      Persi]] - rationale - src/research_data/storage.py
- [[Written file content should match the raw payload.]] - rationale - tests/test_storage.py
- [[_make_fetch_result()_1]] - code - tests/test_storage.py
- [[_write_providers_toml()]] - code - tests/test_property_provider_registry.py
- [[fetch_results_with_payload()]] - code - tests/test_property_raw_payload_hash.py
- [[provider_config_with_missing_fields()]] - code - tests/test_property_provider_registry.py
- [[quality.py]] - code - src/research_data/quality.py
- [[str]] - code
- [[test_missing_required_fields_raises_config_error()]] - code - tests/test_property_provider_registry.py
- [[test_property_provider_registry.py]] - code - tests/test_property_provider_registry.py
- [[test_property_raw_payload_hash.py]] - code - tests/test_property_raw_payload_hash.py
- [[test_stored_hash_matches_recomputed_hash_from_file()]] - code - tests/test_property_raw_payload_hash.py
- [[write_raw_payload should return the content hash string.]] - rationale - tests/test_storage.py
- [[write_raw_payload()]] - code - src/research_data/storage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Data_Quality_Auditor
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_AssetUniverse Config & DuckDB Storage]]
- 7 edges to [[_COMMUNITY_Provider Config Loading & Validation]]
- 5 edges to [[_COMMUNITY_Provider API-Key Validation]]
- 4 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 4 edges to [[_COMMUNITY_Provider Registry]]
- 3 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 3 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 2 edges to [[_COMMUNITY_DuckDB Schema Init & Duplicate-PK Handling]]
- 2 edges to [[_COMMUNITY_InsufficientDataError]]
- 2 edges to [[_COMMUNITY_App Config Loading]]
- 2 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 2 edges to [[_COMMUNITY_DataQualityReport Model]]
- 2 edges to [[_COMMUNITY_Market Calendar Core]]
- 1 edge to [[_COMMUNITY_Provider Registry Missing-Config Tests]]
- 1 edge to [[_COMMUNITY_Secret Redaction]]

## Top bridge nodes
- [[str]] - degree 42, connects to 8 communities
- [[TestWriteRawPayload]] - degree 21, connects to 7 communities
- [[DataQualityAuditor]] - degree 15, connects to 5 communities
- [[write_raw_payload()]] - degree 18, connects to 3 communities
- [[_make_fetch_result()_1]] - degree 14, connects to 2 communities
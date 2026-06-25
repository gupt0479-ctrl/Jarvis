---
type: community
cohesion: 0.05
members: 70
---

# Asset/Universe Config & DuckDB Storage

**Cohesion:** 0.05 - loosely connected
**Members:** 70 nodes

## Members
- [[.test_batch_size_respected()]] - code - tests/test_storage.py
- [[.test_custom_run_id_used_when_provided()]] - code - tests/test_storage.py
- [[.test_failed_batch_does_not_corrupt_previous_data()]] - code - tests/test_storage.py
- [[.test_failed_run_with_error_message()]] - code - tests/test_storage.py
- [[.test_insert_empty_list_returns_zero()]] - code - tests/test_storage.py
- [[.test_insert_multiple_records()]] - code - tests/test_storage.py
- [[.test_insert_records_different_symbols()]] - code - tests/test_storage.py
- [[.test_insert_single_record()]] - code - tests/test_storage.py
- [[.test_large_batch_insert()]] - code - tests/test_storage.py
- [[.test_multi_batch_failure_preserves_committed_batches()]] - code - tests/test_storage.py
- [[.test_multiple_runs_stored_independently()]] - code - tests/test_storage.py
- [[.test_partial_batch_failure_rolls_back_entire_batch()]] - code - tests/test_storage.py
- [[.test_records_all_fields()]] - code - tests/test_storage.py
- [[.test_returns_run_id()]] - code - tests/test_storage.py
- [[.test_seed_is_idempotent()]] - code - tests/test_storage.py
- [[.test_seed_updates_existing_provider()]] - code - tests/test_storage.py
- [[.test_seeds_assets()]] - code - tests/test_storage.py
- [[.test_seeds_providers()]] - code - tests/test_storage.py
- [[.test_upsert_overwrites_existing_record()]] - code - tests/test_storage.py
- [[A failed run should store the error_message field.]] - rationale - tests/test_storage.py
- [[A failure mid-batch should roll back all records in that batch.]] - rationale - tests/test_storage.py
- [[AssetConfig]] - code - src/research_data/config.py
- [[Calling seed_metadata twice should not duplicate rows.]] - rationale - tests/test_storage.py
- [[Configuration for a single asset in the universe.]] - rationale - src/research_data/config.py
- [[Configuration for the asset universe.]] - rationale - src/research_data/config.py
- [[Create a minimal AppConfig for testing seed_metadata.]] - rationale - tests/test_storage.py
- [[Create a valid OHLCVRecord with sensible defaults.]] - rationale - tests/test_storage.py
- [[Create an in-memory DuckDB connection without schema (for testing init_db).]] - rationale - tests/test_storage.py
- [[Detect whether a raw payload is JSON or CSV.      Uses a simple heuristic if]] - rationale - src/research_data/storage.py
- [[DuckDB storage layer for the research data system.  Provides schema initializa]] - rationale - src/research_data/storage.py
- [[If a batch fails, previously committed data should remain intact.]] - rationale - tests/test_storage.py
- [[If run_data includes run_id, it should be used instead of generating one.]] - rationale - tests/test_storage.py
- [[If the second batch fails, the first committed batch should remain.]] - rationale - tests/test_storage.py
- [[Insert OHLCV records in batches with upsert semantics.      Inserts up to batc]] - rationale - src/research_data/storage.py
- [[Insert or replace a single OHLCV record.      Uses INSERT OR REPLACE to handle]] - rationale - src/research_data/storage.py
- [[Inserting a record with the same primary key should overwrite.]] - rationale - tests/test_storage.py
- [[Inserting a single record should return 1.]] - rationale - tests/test_storage.py
- [[Inserting an empty list should return 0.]] - rationale - tests/test_storage.py
- [[Inserting more than default batch_size records works correctly with smaller batc]] - rationale - tests/test_storage.py
- [[Inserting multiple records with different dates should return correct count.]] - rationale - tests/test_storage.py
- [[Multiple ingestion runs should be stored as separate records.]] - rationale - tests/test_storage.py
- [[Record an ingestion run with all metadata.      Args         conn DuckDB co]] - rationale - src/research_data/storage.py
- [[Records should be inserted in batches of the specified size.]] - rationale - tests/test_storage.py
- [[Records with different symbols should all be inserted.]] - rationale - tests/test_storage.py
- [[Seed providers and assets tables from application configuration.      Uses INS]] - rationale - src/research_data/storage.py
- [[Test batch insert writes correct number of records. Requirement 8.4.]] - rationale - tests/test_storage.py
- [[Test ingestion run recording with all fields. Requirement 8.6.]] - rationale - tests/test_storage.py
- [[Test that seed_metadata populates providers and assets from config.]] - rationale - tests/test_storage.py
- [[Test that transaction abort on failure leaves previous state intact. Requirement]] - rationale - tests/test_storage.py
- [[TestBatchInsertOhlcv]] - code - tests/test_storage.py
- [[TestRecordIngestionRun]] - code - tests/test_storage.py
- [[TestSeedMetadata]] - code - tests/test_storage.py
- [[TestTransactionAbort]] - code - tests/test_storage.py
- [[Unit tests for the storage layer (Tasks 2.4, 5.3).  Covers - init_db creates]] - rationale - tests/test_storage.py
- [[UniverseConfig]] - code - src/research_data/config.py
- [[_detect_payload_format()]] - code - src/research_data/storage.py
- [[_make_app_config()]] - code - tests/test_storage.py
- [[_make_record()_1]] - code - tests/test_storage.py
- [[_upsert_single_record()]] - code - src/research_data/storage.py
- [[batch_insert_ohlcv()]] - code - src/research_data/storage.py
- [[raw_db()]] - code - tests/test_storage.py
- [[record_ingestion_run should return a valid UUID string.]] - rationale - tests/test_storage.py
- [[record_ingestion_run should store all provided fields.]] - rationale - tests/test_storage.py
- [[record_ingestion_run()]] - code - src/research_data/storage.py
- [[seed_metadata should populate the assets table from config.]] - rationale - tests/test_storage.py
- [[seed_metadata should populate the providers table from config.]] - rationale - tests/test_storage.py
- [[seed_metadata should update existing provider entries (upsert).]] - rationale - tests/test_storage.py
- [[seed_metadata()]] - code - src/research_data/storage.py
- [[storage.py]] - code - src/research_data/storage.py
- [[test_storage.py]] - code - tests/test_storage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Asset/Universe_Config__DuckDB_Storage
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Data Quality Auditor]]
- 9 edges to [[_COMMUNITY_App Config Loading]]
- 7 edges to [[_COMMUNITY_DuckDB Schema Init & Duplicate-PK Handling]]
- 5 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 5 edges to [[_COMMUNITY_Provider API-Key Validation]]
- 4 edges to [[_COMMUNITY_Secret Redaction]]
- 4 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 4 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 4 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]

## Top bridge nodes
- [[TestBatchInsertOhlcv]] - degree 17, connects to 6 communities
- [[TestRecordIngestionRun]] - degree 15, connects to 6 communities
- [[TestSeedMetadata]] - degree 14, connects to 6 communities
- [[TestTransactionAbort]] - degree 13, connects to 6 communities
- [[AssetConfig]] - degree 11, connects to 4 communities
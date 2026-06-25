---
source_file: "src/research_data/storage.py"
type: "code"
community: "Asset/Universe Config & DuckDB Storage"
location: "L176"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Asset/Universe_Config__DuckDB_Storage
---

# batch_insert_ohlcv()

## Connections
- [[.test_batch_size_respected()]] - `calls` [INFERRED]
- [[.test_failed_batch_does_not_corrupt_previous_data()]] - `calls` [INFERRED]
- [[.test_insert_empty_list_returns_zero()]] - `calls` [INFERRED]
- [[.test_insert_multiple_records()]] - `calls` [INFERRED]
- [[.test_insert_records_different_symbols()]] - `calls` [INFERRED]
- [[.test_insert_single_record()]] - `calls` [INFERRED]
- [[.test_large_batch_insert()]] - `calls` [INFERRED]
- [[.test_multi_batch_failure_preserves_committed_batches()]] - `calls` [INFERRED]
- [[.test_partial_batch_failure_rolls_back_entire_batch()]] - `calls` [INFERRED]
- [[.test_upsert_overwrites_existing_record()]] - `calls` [INFERRED]
- [[Insert OHLCV records in batches with upsert semantics.      Inserts up to batc]] - `rationale_for` [EXTRACTED]
- [[_upsert_single_record()]] - `calls` [EXTRACTED]
- [[storage.py]] - `contains` [EXTRACTED]
- [[test_roundtrip_preserves_all_fields()]] - `calls` [INFERRED]
- [[test_upsert_overwrites_duplicate_pk()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Asset/Universe_Config__DuckDB_Storage
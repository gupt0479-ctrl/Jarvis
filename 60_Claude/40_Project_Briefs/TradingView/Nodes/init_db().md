---
source_file: "src/research_data/storage.py"
type: "code"
community: "DuckDB Schema Init & Duplicate-PK Handling"
location: "L153"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/DuckDB_Schema_Init__Duplicate-PK_Handling
---

# init_db()

## Connections
- [[.test_creates_all_tables()]] - `calls` [INFERRED]
- [[.test_creates_exactly_six_tables()]] - `calls` [INFERRED]
- [[.test_daily_ohlcv_has_primary_key()]] - `calls` [INFERRED]
- [[.test_idempotent_preserves_data()]] - `calls` [INFERRED]
- [[Create all required tables and indexes using CREATE TABLE IF NOT EXISTS.]] - `rationale_for` [EXTRACTED]
- [[db()]] - `calls` [INFERRED]
- [[storage.py]] - `contains` [EXTRACTED]
- [[test_roundtrip_preserves_all_fields()]] - `calls` [INFERRED]
- [[test_secrets_redacted_in_stored_metadata()]] - `calls` [INFERRED]
- [[test_stored_hash_matches_recomputed_hash_from_file()]] - `calls` [INFERRED]
- [[test_upsert_overwrites_duplicate_pk()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/DuckDB_Schema_Init__Duplicate-PK_Handling
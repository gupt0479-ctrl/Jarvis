---
source_file: "tests/test_storage.py"
type: "rationale"
community: "DuckDB Schema Init & Duplicate-PK Handling"
location: "L197"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/DuckDB_Schema_Init__Duplicate-PK_Handling
---

# Calling init_db twice should not destroy existing data.

## Connections
- [[.test_idempotent_preserves_data()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/DuckDB_Schema_Init__Duplicate-PK_Handling
---
source_file: "tests/test_storage.py"
type: "code"
community: "DuckDB Schema Init & Duplicate-PK Handling"
location: "L161"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/DuckDB_Schema_Init__Duplicate-PK_Handling
---

# TestInitDb

## Connections
- [[.test_creates_all_tables()]] - `method` [EXTRACTED]
- [[.test_creates_exactly_six_tables()]] - `method` [EXTRACTED]
- [[.test_daily_ohlcv_has_primary_key()]] - `method` [EXTRACTED]
- [[.test_idempotent_preserves_data()]] - `method` [EXTRACTED]
- [[AppConfig]] - `uses` [INFERRED]
- [[AssetConfig]] - `uses` [INFERRED]
- [[OHLCVRecord]] - `uses` [INFERRED]
- [[PriceAdjustment]] - `uses` [INFERRED]
- [[ProviderConfig]] - `uses` [INFERRED]
- [[ProviderFetchResult]] - `uses` [INFERRED]
- [[QualityStatus]] - `uses` [INFERRED]
- [[Test that init_db creates all required tables. Requirement 8.1.]] - `rationale_for` [EXTRACTED]
- [[UniverseConfig]] - `uses` [INFERRED]
- [[test_storage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/DuckDB_Schema_Init__Duplicate-PK_Handling
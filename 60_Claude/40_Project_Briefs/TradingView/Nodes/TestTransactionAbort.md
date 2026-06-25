---
source_file: "tests/test_storage.py"
type: "code"
community: "Asset/Universe Config & DuckDB Storage"
location: "L356"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Asset/Universe_Config__DuckDB_Storage
---

# TestTransactionAbort

## Connections
- [[.test_failed_batch_does_not_corrupt_previous_data()]] - `method` [EXTRACTED]
- [[.test_multi_batch_failure_preserves_committed_batches()]] - `method` [EXTRACTED]
- [[.test_partial_batch_failure_rolls_back_entire_batch()]] - `method` [EXTRACTED]
- [[AppConfig]] - `uses` [INFERRED]
- [[AssetConfig]] - `uses` [INFERRED]
- [[OHLCVRecord]] - `uses` [INFERRED]
- [[PriceAdjustment]] - `uses` [INFERRED]
- [[ProviderConfig]] - `uses` [INFERRED]
- [[ProviderFetchResult]] - `uses` [INFERRED]
- [[QualityStatus]] - `uses` [INFERRED]
- [[Test that transaction abort on failure leaves previous state intact. Requirement]] - `rationale_for` [EXTRACTED]
- [[UniverseConfig]] - `uses` [INFERRED]
- [[test_storage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Asset/Universe_Config__DuckDB_Storage
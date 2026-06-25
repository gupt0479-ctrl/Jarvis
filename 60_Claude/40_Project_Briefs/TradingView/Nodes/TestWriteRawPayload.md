---
source_file: "tests/test_storage.py"
type: "code"
community: "Data Quality Auditor"
location: "L776"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Data_Quality_Auditor
---

# TestWriteRawPayload

## Connections
- [[.test_computes_correct_sha256_hash()]] - `method` [EXTRACTED]
- [[.test_csv_format_detection()]] - `method` [EXTRACTED]
- [[.test_file_content_matches_payload()]] - `method` [EXTRACTED]
- [[.test_json_array_format_detection()]] - `method` [EXTRACTED]
- [[.test_never_overwrites_existing_file()]] - `method` [EXTRACTED]
- [[.test_raises_on_file_write_failure()]] - `method` [EXTRACTED]
- [[.test_records_in_raw_market_payloads_table()]] - `method` [EXTRACTED]
- [[.test_redacts_secrets_in_stored_params()]] - `method` [EXTRACTED]
- [[.test_returns_content_hash()]] - `method` [EXTRACTED]
- [[.test_skips_duplicate_hash_for_same_symbol_source()]] - `method` [EXTRACTED]
- [[.test_writes_file_to_correct_path()]] - `method` [EXTRACTED]
- [[AppConfig]] - `uses` [INFERRED]
- [[AssetConfig]] - `uses` [INFERRED]
- [[OHLCVRecord]] - `uses` [INFERRED]
- [[PriceAdjustment]] - `uses` [INFERRED]
- [[ProviderConfig]] - `uses` [INFERRED]
- [[ProviderFetchResult]] - `uses` [INFERRED]
- [[QualityStatus]] - `uses` [INFERRED]
- [[Test raw payload writer. Requirements 3.1-3.7, 14.2.]] - `rationale_for` [EXTRACTED]
- [[UniverseConfig]] - `uses` [INFERRED]
- [[test_storage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Data_Quality_Auditor
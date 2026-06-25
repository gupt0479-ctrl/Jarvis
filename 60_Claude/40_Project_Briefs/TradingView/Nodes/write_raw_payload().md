---
source_file: "src/research_data/storage.py"
type: "code"
community: "Data Quality Auditor"
location: "L434"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Data_Quality_Auditor
---

# write_raw_payload()

## Connections
- [[.test_computes_correct_sha256_hash()]] - `calls` [INFERRED]
- [[.test_csv_format_detection()]] - `calls` [INFERRED]
- [[.test_file_content_matches_payload()]] - `calls` [INFERRED]
- [[.test_json_array_format_detection()]] - `calls` [INFERRED]
- [[.test_never_overwrites_existing_file()]] - `calls` [INFERRED]
- [[.test_raises_on_file_write_failure()]] - `calls` [INFERRED]
- [[.test_records_in_raw_market_payloads_table()]] - `calls` [INFERRED]
- [[.test_redacts_secrets_in_stored_params()]] - `calls` [INFERRED]
- [[.test_returns_content_hash()]] - `calls` [INFERRED]
- [[.test_skips_duplicate_hash_for_same_symbol_source()]] - `calls` [INFERRED]
- [[.test_writes_file_to_correct_path()]] - `calls` [INFERRED]
- [[Write a raw provider payload to disk and record it in the database.      Persi]] - `rationale_for` [EXTRACTED]
- [[_detect_payload_format()]] - `calls` [EXTRACTED]
- [[redact_secrets()]] - `calls` [EXTRACTED]
- [[storage.py]] - `contains` [EXTRACTED]
- [[str]] - `calls` [INFERRED]
- [[test_secrets_redacted_in_stored_metadata()]] - `calls` [INFERRED]
- [[test_stored_hash_matches_recomputed_hash_from_file()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Data_Quality_Auditor
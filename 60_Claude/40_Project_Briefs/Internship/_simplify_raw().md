---
source_file: "tests/test_run_pipeline.py"
type: "code"
community: "test_writer.py"
location: "L23"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_writerpy
---

# _simplify_raw()

## Connections
- [[_fake_http_get()]] - `calls` [EXTRACTED]
- [[_listing_with_date()]] - `calls` [EXTRACTED]
- [[_strip_case_keys()]] - `calls` [EXTRACTED]
- [[test_build_matched_reason_per_source()]] - `calls` [EXTRACTED]
- [[test_dedup_new_dedupes_within_the_same_run()]] - `calls` [EXTRACTED]
- [[test_dedup_new_skips_excluded_uid()]] - `calls` [INFERRED]
- [[test_eligible_posting_gets_content_section()]] - `calls` [EXTRACTED]
- [[test_fetch_and_filter_counts_and_matches()]] - `calls` [EXTRACTED]
- [[test_fetch_and_filter_skips_excluded_uid()]] - `calls` [INFERRED]
- [[test_fetch_failure_fails_open_to_thin_dossier()]] - `calls` [EXTRACTED]
- [[test_opt_cache_short_circuits_before_fetch()]] - `calls` [EXTRACTED]
- [[test_opt_exclusion_rejects_and_caches()]] - `calls` [EXTRACTED]
- [[test_run_once_never_fetches_an_already_excluded_uid()]] - `calls` [INFERRED]
- [[test_run_pipeline.py]] - `contains` [EXTRACTED]
- [[test_validate_and_write_happy_path()]] - `calls` [EXTRACTED]
- [[test_validate_and_write_rejects_cross_source_duplicate()]] - `calls` [EXTRACTED]
- [[test_validate_and_write_rejects_dead_url()]] - `calls` [EXTRACTED]
- [[test_validate_and_write_seeds_dedup_keys_from_existing_vault_files()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_writerpy
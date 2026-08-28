---
source_file: "tests/test_run_pipeline.py"
type: "code"
community: "test_writer.py"
location: "L369"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_writerpy
---

# _run_once_kwargs()

## Connections
- [[_fake_http_get()]] - `indirect_call` [INFERRED]
- [[_fake_http_head_all_live()]] - `indirect_call` [INFERRED]
- [[test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run()]] - `calls` [EXTRACTED]
- [[test_run_once_does_not_alert_below_threshold()]] - `calls` [INFERRED]
- [[test_run_once_does_not_mark_seen_when_push_fails()]] - `calls` [EXTRACTED]
- [[test_run_once_excludes_and_never_refetches_real_dead_link_after_threshold()]] - `calls` [INFERRED]
- [[test_run_once_files_issue_and_persists_state_on_zero_match_streak()]] - `calls` [INFERRED]
- [[test_run_once_files_issue_on_exclusion_spike()]] - `calls` [INFERRED]
- [[test_run_once_files_issue_on_systemic_rejection_not_routine_one()]] - `calls` [EXTRACTED]
- [[test_run_once_files_issue_once_per_bucket_crossing_capacity()]] - `calls` [EXTRACTED]
- [[test_run_once_global_total_thresholds()]] - `calls` [EXTRACTED]
- [[test_run_once_halts_and_files_issue_on_fetch_network_failure()]] - `calls` [EXTRACTED]
- [[test_run_once_halts_on_schema_drift_and_writes_nothing()]] - `calls` [EXTRACTED]
- [[test_run_once_happy_path_marks_seen_and_writes_dossiers()]] - `calls` [EXTRACTED]
- [[test_run_once_never_fetches_an_already_excluded_uid()]] - `calls` [INFERRED]
- [[test_run_once_reports_bucket_at_capacity_without_refusing_writes()]] - `calls` [EXTRACTED]
- [[test_run_once_second_run_does_not_rewrite_already_seen_items()]] - `calls` [EXTRACTED]
- [[test_run_once_writes_interndock_listings_when_wired()]] - `calls` [EXTRACTED]
- [[test_run_pipeline.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_writerpy
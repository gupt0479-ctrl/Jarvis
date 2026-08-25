---
source_file: "tests/test_run_pipeline.py"
type: "code"
community: "test_writer.py"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_writerpy
---

# test_run_pipeline.py

## Connections
- [[GitPushError]] - `imports` [EXTRACTED]
- [[SchemaDriftError]] - `imports` [EXTRACTED]
- [[_applyguy_raw()]] - `contains` [EXTRACTED]
- [[_fake_http_get()]] - `contains` [EXTRACTED]
- [[_fake_http_get_only_interndock()]] - `contains` [EXTRACTED]
- [[_fake_http_head_all_live()]] - `contains` [EXTRACTED]
- [[_fake_interndock_sitemap_get()]] - `contains` [EXTRACTED]
- [[_josegael_raw()]] - `contains` [EXTRACTED]
- [[_listing_with_date()]] - `contains` [EXTRACTED]
- [[_page_with()]] - `contains` [EXTRACTED]
- [[_run_once_kwargs()]] - `contains` [EXTRACTED]
- [[_seed_bucket()]] - `contains` [EXTRACTED]
- [[_simplify_raw()]] - `contains` [EXTRACTED]
- [[_strip_case_keys()]] - `contains` [EXTRACTED]
- [[_vanshb03_raw()]] - `contains` [EXTRACTED]
- [[_zshah101_raw()]] - `contains` [EXTRACTED]
- [[compute_uid()]] - `imports` [EXTRACTED]
- [[cross_source_key()]] - `imports` [EXTRACTED]
- [[filter.py]] - `imports_from` [EXTRACTED]
- [[git_ops.py]] - `imports_from` [EXTRACTED]
- [[identity.py]] - `imports_from` [EXTRACTED]
- [[load_profile()]] - `imports` [EXTRACTED]
- [[normalize.py]] - `imports_from` [EXTRACTED]
- [[normalize_josegael()]] - `imports` [EXTRACTED]
- [[normalize_simplify()]] - `imports` [EXTRACTED]
- [[run_pipeline.py]] - `imports` [EXTRACTED]
- [[schema_drift.py]] - `imports_from` [EXTRACTED]
- [[test_build_matched_reason_per_source()]] - `contains` [EXTRACTED]
- [[test_count_dossiers_by_bucket_counts_real_files()]] - `contains` [EXTRACTED]
- [[test_cross_source_key_punctuation_insensitive_marmon_case()]] - `contains` [EXTRACTED]
- [[test_debate_losses.py]] - `imports_from` [EXTRACTED]
- [[test_dedup_new_dedupes_within_the_same_run()]] - `contains` [EXTRACTED]
- [[test_dedup_new_splits_new_vs_already_seen()]] - `contains` [EXTRACTED]
- [[test_discover_interndock_fails_open_on_sitemap_error()]] - `contains` [EXTRACTED]
- [[test_discover_interndock_fetches_only_new_candidates_and_persists_state()]] - `contains` [EXTRACTED]
- [[test_discover_interndock_returns_empty_when_fetch_fn_is_none()]] - `contains` [EXTRACTED]
- [[test_eligible_posting_gets_content_section()]] - `contains` [EXTRACTED]
- [[test_fetch_and_filter_counts_and_matches()]] - `contains` [EXTRACTED]
- [[test_fetch_failure_fails_open_to_thin_dossier()]] - `contains` [EXTRACTED]
- [[test_file_github_issue_calls_gh_with_expected_args()]] - `contains` [EXTRACTED]
- [[test_load_save_seen_ids_round_trips()]] - `contains` [EXTRACTED]
- [[test_load_seen_ids_missing_file_returns_empty_set()]] - `contains` [EXTRACTED]
- [[test_opt_cache_short_circuits_before_fetch()]] - `contains` [EXTRACTED]
- [[test_opt_exclusion_rejects_and_caches()]] - `contains` [EXTRACTED]
- [[test_prioritize_and_cap_grants_reserved_slot_to_preferred_company_losing_the_debate()]] - `contains` [EXTRACTED]
- [[test_prioritize_and_cap_keeps_most_recent_first()]] - `contains` [EXTRACTED]
- [[test_prioritize_and_cap_missing_date_posted_sorts_last()]] - `contains` [EXTRACTED]
- [[test_prioritize_and_cap_orders_preferred_company_first_within_bucket()]] - `contains` [EXTRACTED]
- [[test_prioritize_and_cap_reserved_slot_is_a_noop_with_no_preferred_candidates()]] - `contains` [EXTRACTED]
- [[test_prioritize_and_cap_reserved_slot_recency_tiebreak_among_preferred()]] - `contains` [EXTRACTED]
- [[test_prioritize_and_cap_scopes_budget_per_bucket()]] - `contains` [EXTRACTED]
- [[test_prioritize_and_cap_without_preferred_companies_keeps_recency_only_order()]] - `contains` [EXTRACTED]
- [[test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run()]] - `contains` [EXTRACTED]
- [[test_run_once_does_not_mark_seen_when_push_fails()]] - `contains` [EXTRACTED]
- [[test_run_once_files_issue_on_systemic_rejection_not_routine_one()]] - `contains` [EXTRACTED]
- [[test_run_once_files_issue_once_per_bucket_crossing_capacity()]] - `contains` [EXTRACTED]
- [[test_run_once_global_total_thresholds()]] - `contains` [EXTRACTED]
- [[test_run_once_halts_and_files_issue_on_fetch_network_failure()]] - `contains` [EXTRACTED]
- [[test_run_once_halts_on_schema_drift_and_writes_nothing()]] - `contains` [EXTRACTED]
- [[test_run_once_happy_path_marks_seen_and_writes_dossiers()]] - `contains` [EXTRACTED]
- [[test_run_once_reports_bucket_at_capacity_without_refusing_writes()]] - `contains` [EXTRACTED]
- [[test_run_once_second_run_does_not_rewrite_already_seen_items()]] - `contains` [EXTRACTED]
- [[test_run_once_writes_interndock_listings_when_wired()]] - `contains` [EXTRACTED]
- [[test_validate_and_write_happy_path()]] - `contains` [EXTRACTED]
- [[test_validate_and_write_rejects_cross_source_duplicate()]] - `contains` [EXTRACTED]
- [[test_validate_and_write_rejects_dead_url()]] - `contains` [EXTRACTED]
- [[test_validate_and_write_seeds_dedup_keys_from_existing_vault_files()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_writerpy
---
type: community
members: 74
---

# test_writer.py

**Members:** 74 nodes

## Members
- [[150170 stay informational-only (logged via dossier_total, no issue);     19020]] - rationale - tests/test_run_pipeline.py
- [[A bucket with 0 eligible candidates this run must not let another     bucket's i]] - rationale - tests/test_run_pipeline.py
- [[A source going offline (DNS failure, deleted repo, 5xx) must produce a     logge]] - rationale - tests/test_run_pipeline.py
- [[A uid that wins without ever having lost before (the common case)     must not e]] - rationale - tests/test_debate_losses.py
- [[GitPushError]] - code - core/git_ops.py
- [[If the exact same uid were somehow matched twice in one run, it should     only]] - rationale - tests/test_run_pipeline.py
- [[Integration-level confirmation that run_once actually wires     should_alert_on_]] - rationale - tests/test_debate_losses.py
- [[Keys come from the dossier files actually in the checkout — a listing     whose]] - rationale - tests/test_run_pipeline.py
- [[Loses twice (deferred), then wins (written) on the third attempt —     its loss]] - rationale - tests/test_debate_losses.py
- [[Pre-seed stateexcluded_uids.json with a real candidate's uid already     at the]] - rationale - tests/test_debate_losses.py
- [[Real fixture set writes exactly 1 'Other'-bucket item per run under the     defa]] - rationale - tests/test_run_pipeline.py
- [[Real incident, 2026-08-21 287 of 304 total excluded-log entries     (94%) were]] - rationale - tests/test_debate_losses.py
- [[Same program via two sources (two distinct uids, one company+title) —     the se]] - rationale - tests/test_run_pipeline.py
- [[Task L integration two 'Other'-bucket candidates, non-preferred one     posted]] - rationale - tests/test_run_pipeline.py
- [[Task N (Prompt 5) — consecutive-loss tracking and the excluded-uid list.  update]] - rationale - tests/test_debate_losses.py
- [[The core guarantee a deferred item is not marked seen, so it's neither     lost]] - rationale - tests/test_run_pipeline.py
- [[The critical ordering guarantee a validated, written dossier whose     push fai]] - rationale - tests/test_run_pipeline.py
- [[_candidate()_1]] - code - tests/test_debate_losses.py
- [[_fake_http_get()]] - code - tests/test_run_pipeline.py
- [[_fake_http_head_all_live()]] - code - tests/test_run_pipeline.py
- [[_josegael_raw()]] - code - tests/test_run_pipeline.py
- [[_listing_with_date()]] - code - tests/test_run_pipeline.py
- [[_page_with()]] - code - tests/test_run_pipeline.py
- [[_run_once_kwargs()]] - code - tests/test_run_pipeline.py
- [[_seed_bucket()]] - code - tests/test_run_pipeline.py
- [[_simplify_raw()]] - code - tests/test_run_pipeline.py
- [[_strip_case_keys()]] - code - tests/test_run_pipeline.py
- [[_vanshb03_raw()]] - code - tests/test_run_pipeline.py
- [[_zshah101_raw()]] - code - tests/test_run_pipeline.py
- [[compute_uid()]] - code - core/identity.py
- [[normalize_simplify()]] - code - ingestion/normalize.py
- [[preferred_companies=None (the default) must reproduce the exact     pre-Task-L r]] - rationale - tests/test_run_pipeline.py
- [[test_build_matched_reason_per_source()]] - code - tests/test_run_pipeline.py
- [[test_count_dossiers_by_bucket_counts_real_files()]] - code - tests/test_run_pipeline.py
- [[test_debate_losses.py]] - code - tests/test_debate_losses.py
- [[test_dedup_new_dedupes_within_the_same_run()]] - code - tests/test_run_pipeline.py
- [[test_dedup_new_skips_excluded_uid()]] - code - tests/test_debate_losses.py
- [[test_dedup_new_splits_new_vs_already_seen()]] - code - tests/test_run_pipeline.py
- [[test_deferred_4_times_still_in_pool_not_excluded()]] - code - tests/test_debate_losses.py
- [[test_deferred_5th_time_excludes_and_removes_from_losses()]] - code - tests/test_debate_losses.py
- [[test_eligible_posting_gets_content_section()]] - code - tests/test_run_pipeline.py
- [[test_fetch_and_filter_counts_and_matches()]] - code - tests/test_run_pipeline.py
- [[test_fetch_and_filter_skips_excluded_uid()]] - code - tests/test_debate_losses.py
- [[test_fetch_failure_fails_open_to_thin_dossier()]] - code - tests/test_run_pipeline.py
- [[test_file_github_issue_calls_gh_with_expected_args()]] - code - tests/test_run_pipeline.py
- [[test_load_save_seen_ids_round_trips()]] - code - tests/test_run_pipeline.py
- [[test_load_seen_ids_missing_file_returns_empty_set()]] - code - tests/test_run_pipeline.py
- [[test_opt_cache_short_circuits_before_fetch()]] - code - tests/test_run_pipeline.py
- [[test_opt_exclusion_rejects_and_caches()]] - code - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_keeps_most_recent_first()]] - code - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_missing_date_posted_sorts_last()]] - code - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_orders_preferred_company_first_within_bucket()]] - code - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_scopes_budget_per_bucket()]] - code - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_without_preferred_companies_keeps_recency_only_order()]] - code - tests/test_run_pipeline.py
- [[test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run()]] - code - tests/test_run_pipeline.py
- [[test_run_once_does_not_mark_seen_when_push_fails()]] - code - tests/test_run_pipeline.py
- [[test_run_once_files_issue_on_exclusion_spike()]] - code - tests/test_debate_losses.py
- [[test_run_once_files_issue_on_systemic_rejection_not_routine_one()]] - code - tests/test_run_pipeline.py
- [[test_run_once_files_issue_once_per_bucket_crossing_capacity()]] - code - tests/test_run_pipeline.py
- [[test_run_once_global_total_thresholds()]] - code - tests/test_run_pipeline.py
- [[test_run_once_halts_and_files_issue_on_fetch_network_failure()]] - code - tests/test_run_pipeline.py
- [[test_run_once_halts_on_schema_drift_and_writes_nothing()]] - code - tests/test_run_pipeline.py
- [[test_run_once_happy_path_marks_seen_and_writes_dossiers()]] - code - tests/test_run_pipeline.py
- [[test_run_once_never_fetches_an_already_excluded_uid()]] - code - tests/test_debate_losses.py
- [[test_run_once_reports_bucket_at_capacity_without_refusing_writes()]] - code - tests/test_run_pipeline.py
- [[test_run_once_second_run_does_not_rewrite_already_seen_items()]] - code - tests/test_run_pipeline.py
- [[test_run_pipeline.py]] - code - tests/test_run_pipeline.py
- [[test_should_alert_on_exclusion_spike_threshold()]] - code - tests/test_debate_losses.py
- [[test_validate_and_write_happy_path()]] - code - tests/test_run_pipeline.py
- [[test_validate_and_write_rejects_cross_source_duplicate()]] - code - tests/test_run_pipeline.py
- [[test_validate_and_write_rejects_dead_url()]] - code - tests/test_run_pipeline.py
- [[test_validate_and_write_seeds_dedup_keys_from_existing_vault_files()]] - code - tests/test_run_pipeline.py
- [[test_wins_on_attempt_3_never_excluded()]] - code - tests/test_debate_losses.py
- [[test_written_uid_not_in_losses_is_a_no_op_pop()]] - code - tests/test_debate_losses.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_writerpy
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_write_dossier]]
- 15 edges to [[_COMMUNITY_recheck.py]]
- 15 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 4 edges to [[_COMMUNITY_vault_root]]
- 2 edges to [[_COMMUNITY_render_dossier]]
- 2 edges to [[_COMMUNITY_build_frontmatter]]
- 1 edge to [[_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix]]
- 1 edge to [[_COMMUNITY_commit_and_push_with_retry]]

## Top bridge nodes
- [[normalize_simplify()]] - degree 36, connects to 7 communities
- [[test_run_pipeline.py]] - degree 57, connects to 4 communities
- [[test_debate_losses.py]] - degree 18, connects to 3 communities
- [[compute_uid()]] - degree 25, connects to 2 communities
- [[GitPushError]] - degree 8, connects to 2 communities
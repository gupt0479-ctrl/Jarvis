---
type: community
members: 30
---

# test_writer.py

**Members:** 30 nodes

## Members
- [[150170 stay informational-only (logged via dossier_total, no issue);     19020]] - rationale - tests/test_run_pipeline.py
- [[A source going offline (DNS failure, deleted repo, 5xx) must produce a     logge]] - rationale - tests/test_run_pipeline.py
- [[Real fixture set writes exactly 1 'Other'-bucket item per run under the     defa]] - rationale - tests/test_run_pipeline.py
- [[The core guarantee a deferred item is not marked seen, so it's neither     lost]] - rationale - tests/test_run_pipeline.py
- [[The critical ordering guarantee a validated, written dossier whose     push fai]] - rationale - tests/test_run_pipeline.py
- [[_fake_http_get()]] - code - tests/test_run_pipeline.py
- [[_josegael_raw()]] - code - tests/test_run_pipeline.py
- [[_run_once_kwargs()]] - code - tests/test_run_pipeline.py
- [[_seed_bucket()]] - code - tests/test_run_pipeline.py
- [[_strip_case_keys()]] - code - tests/test_run_pipeline.py
- [[_vanshb03_raw()]] - code - tests/test_run_pipeline.py
- [[_zshah101_raw()]] - code - tests/test_run_pipeline.py
- [[test_build_matched_reason_per_source()]] - code - tests/test_run_pipeline.py
- [[test_count_dossiers_by_bucket_counts_real_files()]] - code - tests/test_run_pipeline.py
- [[test_dedup_new_splits_new_vs_already_seen()]] - code - tests/test_run_pipeline.py
- [[test_fetch_and_filter_counts_and_matches()]] - code - tests/test_run_pipeline.py
- [[test_file_github_issue_calls_gh_with_expected_args()]] - code - tests/test_run_pipeline.py
- [[test_load_save_seen_ids_round_trips()]] - code - tests/test_run_pipeline.py
- [[test_load_seen_ids_missing_file_returns_empty_set()]] - code - tests/test_run_pipeline.py
- [[test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run()]] - code - tests/test_run_pipeline.py
- [[test_run_once_does_not_mark_seen_when_push_fails()]] - code - tests/test_run_pipeline.py
- [[test_run_once_files_issue_on_systemic_rejection_not_routine_one()]] - code - tests/test_run_pipeline.py
- [[test_run_once_files_issue_once_per_bucket_crossing_capacity()]] - code - tests/test_run_pipeline.py
- [[test_run_once_global_total_thresholds()]] - code - tests/test_run_pipeline.py
- [[test_run_once_halts_and_files_issue_on_fetch_network_failure()]] - code - tests/test_run_pipeline.py
- [[test_run_once_halts_on_schema_drift_and_writes_nothing()]] - code - tests/test_run_pipeline.py
- [[test_run_once_happy_path_marks_seen_and_writes_dossiers()]] - code - tests/test_run_pipeline.py
- [[test_run_once_reports_bucket_at_capacity_without_refusing_writes()]] - code - tests/test_run_pipeline.py
- [[test_run_once_second_run_does_not_rewrite_already_seen_items()]] - code - tests/test_run_pipeline.py
- [[test_run_pipeline.py]] - code - tests/test_run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_writerpy
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_normalize_simplify]]
- 6 edges to [[_COMMUNITY__listing_with_date]]
- 3 edges to [[_COMMUNITY_write_dossier]]
- 3 edges to [[_COMMUNITY_recheck.py]]
- 3 edges to [[_COMMUNITY_commit_and_push_with_retry]]
- 3 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 3 edges to [[_COMMUNITY_vault_root]]
- 1 edge to [[_COMMUNITY_test_freehire.py]]
- 1 edge to [[_COMMUNITY_test_debate_losses.py]]

## Top bridge nodes
- [[test_run_pipeline.py]] - degree 57, connects to 9 communities
- [[test_build_matched_reason_per_source()]] - degree 5, connects to 2 communities
- [[_run_once_kwargs()]] - degree 14, connects to 1 community
- [[_fake_http_get()]] - degree 9, connects to 1 community
- [[_seed_bucket()]] - degree 6, connects to 1 community
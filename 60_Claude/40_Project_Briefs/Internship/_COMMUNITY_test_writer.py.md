---
type: community
members: 23
---

# test_writer.py

**Members:** 23 nodes

## Members
- [[150170 stay informational-only (logged via dossier_total, no issue);     19020]] - rationale - tests/test_run_pipeline.py
- [[A source going offline (DNS failure, deleted repo, 5xx) must produce a     logge]] - rationale - tests/test_run_pipeline.py
- [[Real fixture set writes exactly 1 'Other'-bucket item per run under the     defa]] - rationale - tests/test_run_pipeline.py
- [[The core guarantee a deferred item is not marked seen, so it's neither     lost]] - rationale - tests/test_run_pipeline.py
- [[The critical ordering guarantee a validated, written dossier whose     push fai]] - rationale - tests/test_run_pipeline.py
- [[_run_once_kwargs()]] - code - tests/test_run_pipeline.py
- [[_seed_bucket()]] - code - tests/test_run_pipeline.py
- [[test_count_dossiers_by_bucket_counts_real_files()]] - code - tests/test_run_pipeline.py
- [[test_discover_interndock_fails_open_on_sitemap_error()]] - code - tests/test_run_pipeline.py
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
- 16 edges to [[_COMMUNITY_normalize_simplify]]
- 11 edges to [[_COMMUNITY__fake_http_get]]
- 9 edges to [[_COMMUNITY__listing_with_date]]
- 6 edges to [[_COMMUNITY__fake_http_get_only_interndock]]
- 3 edges to [[_COMMUNITY_write_dossier]]
- 3 edges to [[_COMMUNITY_recheck.py]]
- 3 edges to [[_COMMUNITY_commit_and_push_with_retry]]
- 3 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 3 edges to [[_COMMUNITY_vault_root]]
- 2 edges to [[_COMMUNITY_test_debate_losses.py]]

## Top bridge nodes
- [[test_run_pipeline.py]] - degree 67, connects to 10 communities
- [[_run_once_kwargs()]] - degree 16, connects to 4 communities
- [[_seed_bucket()]] - degree 6, connects to 1 community
- [[test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run()]] - degree 4, connects to 1 community
- [[test_run_once_does_not_mark_seen_when_push_fails()]] - degree 4, connects to 1 community
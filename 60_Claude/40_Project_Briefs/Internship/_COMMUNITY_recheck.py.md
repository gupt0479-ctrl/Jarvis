---
type: community
members: 58
---

# recheck.py

**Members:** 58 nodes

## Members
- [[Fetch raw listings from each source. Used both by the scheduled pipeline and (wi]] - rationale - ingestion/sources.py
- [[Not a Dossier (doesn't go through validate.validate()'s dossier-specific     fro]] - rationale - tests/test_run_log.py
- [[Path]] - code
- [[Phase 3 orchestration schema-drift check - fetch - filter - dedup - validat]] - rationale - run_pipeline.py
- [[Real per-bucket file counts in the vault checkout — Viewed isn't one     of BUC]] - rationale - run_pipeline.py
- [[Returns ((uid, listing), ... for genuinely new items, already_seen_count).]] - rationale - run_pipeline.py
- [[Returns (updated_losses, newly_excluded (uid, listing), ...).     Increments]] - rationale - run_pipeline.py
- [[Returns {source_name {fetch_count int, matched Listing, ...}}.     excl]] - rationale - run_pipeline.py
- [[Task N (Prompt 5) — one line per uid the first time it's excluded,     same appe]] - rationale - core/run_log.py
- [[Two-tier run log per the plan raw per-run JSONL in this repo, a weekly markdown]] - rationale - core/run_log.py
- [[_append_markdown_line()]] - code - core/run_log.py
- [[_commit_log()]] - code - recheck.py
- [[_ts()]] - code - tests/test_run_log.py
- [[append_excluded_log()]] - code - core/run_log.py
- [[append_run_log()]] - code - core/run_log.py
- [[append_weekly_rollup()]] - code - core/run_log.py
- [[count_dossiers_by_bucket()]] - code - run_pipeline.py
- [[datetime]] - code
- [[datetime_1]] - code
- [[datetime_2]] - code
- [[dedup_new()]] - code - run_pipeline.py
- [[fetch_ai_jobs()]] - code - ingestion/sources.py
- [[fetch_and_filter()]] - code - run_pipeline.py
- [[fetch_ashby()]] - code - ingestion/sources.py
- [[fetch_greenhouse()]] - code - ingestion/sources.py
- [[fetch_josegael()]] - code - ingestion/sources.py
- [[fetch_simplify()]] - code - ingestion/sources.py
- [[fetch_vanshb03()]] - code - ingestion/sources.py
- [[fetch_zshah101()]] - code - ingestion/sources.py
- [[format_weekly_rollup()]] - code - core/run_log.py
- [[load_capacity_notified()]] - code - run_pipeline.py
- [[load_debate_losses()]] - code - run_pipeline.py
- [[load_excluded_uids()]] - code - run_pipeline.py
- [[load_profile()]] - code - core/filter.py
- [[load_recent_runs()]] - code - core/run_log.py
- [[load_seen_ids()]] - code - run_pipeline.py
- [[recheck.py]] - code - recheck.py
- [[run_log.py]] - code - core/run_log.py
- [[run_once()]] - code - run_pipeline.py
- [[run_pipeline.py]] - code - run_pipeline.py
- [[save_capacity_notified()]] - code - run_pipeline.py
- [[save_debate_losses()]] - code - run_pipeline.py
- [[save_excluded_uids()]] - code - run_pipeline.py
- [[save_seen_ids()]] - code - run_pipeline.py
- [[should_alert_on_exclusion_spike()]] - code - run_pipeline.py
- [[should_run_weekly_rollup()]] - code - core/run_log.py
- [[sources.py]] - code - ingestion/sources.py
- [[test_append_run_log_writes_one_json_line_per_call()]] - code - tests/test_run_log.py
- [[test_append_weekly_rollup_appends_without_rewriting()]] - code - tests/test_run_log.py
- [[test_append_weekly_rollup_creates_file_with_header()]] - code - tests/test_run_log.py
- [[test_appended_run_log_note_has_no_blank_lines_or_stray_dashes()]] - code - tests/test_run_log.py
- [[test_format_weekly_rollup_aggregates_written_and_rejections()]] - code - tests/test_run_log.py
- [[test_format_weekly_rollup_handles_zero_activity()]] - code - tests/test_run_log.py
- [[test_load_recent_runs_filters_by_timestamp()]] - code - tests/test_run_log.py
- [[test_load_recent_runs_on_missing_file_returns_empty()]] - code - tests/test_run_log.py
- [[test_run_log.py]] - code - tests/test_run_log.py
- [[test_should_run_weekly_rollup_only_fires_sunday_2300_utc()]] - code - tests/test_run_log.py
- [[update_debate_losses()]] - code - run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/recheckpy
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_write_dossier]]
- 10 edges to [[_COMMUNITY_revalidate.py]]
- 9 edges to [[_COMMUNITY_test_write_dossier_creates_missing_dossiers_dir]]
- 9 edges to [[_COMMUNITY_test_writer.py]]
- 9 edges to [[_COMMUNITY_build_frontmatter]]
- 8 edges to [[_COMMUNITY_commit_and_push_with_retry]]
- 8 edges to [[_COMMUNITY_render_dossier]]
- 5 edges to [[_COMMUNITY_vault_root]]
- 5 edges to [[_COMMUNITY_writer.py]]
- 4 edges to [[_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix]]
- 4 edges to [[_COMMUNITY_plan_removals]]
- 3 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]

## Top bridge nodes
- [[run_pipeline.py]] - degree 75, connects to 11 communities
- [[Path]] - degree 26, connects to 5 communities
- [[recheck.py]] - degree 24, connects to 4 communities
- [[load_profile()]] - degree 9, connects to 4 communities
- [[run_once()]] - degree 26, connects to 3 communities
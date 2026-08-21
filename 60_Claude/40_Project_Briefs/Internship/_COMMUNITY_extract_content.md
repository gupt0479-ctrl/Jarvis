---
type: community
members: 60
---

# extract_content

**Members:** 60 nodes

## Members
- [[A dossier written before dossier_uids.json existed (or hand-edited into     the]] - rationale - tests/test_recheck.py
- [[A source missing from feeds_by_source means its fetch failed — its     dossiers]] - rationale - tests/test_recheck.py
- [[Frontmatter dicts of every dossier file actually present in the vault     checko]] - rationale - vault_writer/writer.py
- [[Most-recently-posted first; missing date_posted sorts last, never first     (an]] - rationale - run_pipeline.py
- [[Not a Dossier (doesn't go through validate.validate()'s dossier-specific     fro]] - rationale - tests/test_run_log.py
- [[Path]] - code
- [[Phase 3 orchestration schema-drift check - fetch - filter - dedup - validat]] - rationale - run_pipeline.py
- [[Renders + validates each new listing; writes the ones that pass into     the Jar]] - rationale - run_pipeline.py
- [[Returns ((uid, listing), ... for genuinely new items, already_seen_count).]] - rationale - run_pipeline.py
- [[Returns {source_name {fetch_count int, matched Listing, ...}}.]] - rationale - run_pipeline.py
- [[Two-tier run log per the plan raw per-run JSONL in this repo, a weekly markdown]] - rationale - core/run_log.py
- [[{uid, path, reason} for dossiers whose posting closed. A source that     faile]] - rationale - recheck.py
- [[_commit_log()]] - code - recheck.py
- [[_fm()]] - code - tests/test_recheck.py
- [[_prioritize_and_cap()]] - code - run_pipeline.py
- [[_ts()]] - code - tests/test_run_log.py
- [[append_run_log()]] - code - core/run_log.py
- [[append_weekly_rollup()]] - code - core/run_log.py
- [[build_matched_reason()]] - code - run_pipeline.py
- [[datetime]] - code
- [[datetime_1]] - code
- [[datetime_2]] - code
- [[dedup_new()]] - code - run_pipeline.py
- [[fetch_and_filter()]] - code - run_pipeline.py
- [[fetch_josegael()]] - code - ingestion/sources.py
- [[fetch_simplify()]] - code - ingestion/sources.py
- [[fetch_vanshb03()]] - code - ingestion/sources.py
- [[fetch_zshah101()]] - code - ingestion/sources.py
- [[file_github_issue()]] - code - run_pipeline.py
- [[format_weekly_rollup()]] - code - core/run_log.py
- [[load_profile()]] - code - core/filter.py
- [[load_recent_runs()]] - code - core/run_log.py
- [[load_seen_ids()]] - code - run_pipeline.py
- [[main()_2]] - code - recheck.py
- [[plan_removals is the recheck's whole decision surface — pure, tested offline.]] - rationale - tests/test_recheck.py
- [[plan_removals()]] - code - recheck.py
- [[recheck.py]] - code - recheck.py
- [[run_log.py]] - code - core/run_log.py
- [[run_once()]] - code - run_pipeline.py
- [[run_pipeline.py]] - code - run_pipeline.py
- [[save_seen_ids()]] - code - run_pipeline.py
- [[scan_dossiers()]] - code - vault_writer/writer.py
- [[should_run_weekly_rollup()]] - code - core/run_log.py
- [[test_absent_from_feed_is_removed()]] - code - tests/test_recheck.py
- [[test_active_false_upstream_is_removed()]] - code - tests/test_recheck.py
- [[test_all_active_removes_nothing()]] - code - tests/test_recheck.py
- [[test_append_run_log_writes_one_json_line_per_call()]] - code - tests/test_run_log.py
- [[test_append_weekly_rollup_appends_without_rewriting()]] - code - tests/test_run_log.py
- [[test_append_weekly_rollup_creates_file_with_header()]] - code - tests/test_run_log.py
- [[test_appended_run_log_note_has_no_blank_lines_or_stray_dashes()]] - code - tests/test_run_log.py
- [[test_dossier_with_no_manifest_entry_is_skipped_not_removed()]] - code - tests/test_recheck.py
- [[test_failed_fetch_skips_that_sources_dossiers_entirely()]] - code - tests/test_recheck.py
- [[test_format_weekly_rollup_aggregates_written_and_rejections()]] - code - tests/test_run_log.py
- [[test_format_weekly_rollup_handles_zero_activity()]] - code - tests/test_run_log.py
- [[test_load_recent_runs_filters_by_timestamp()]] - code - tests/test_run_log.py
- [[test_load_recent_runs_on_missing_file_returns_empty()]] - code - tests/test_run_log.py
- [[test_recheck.py]] - code - tests/test_recheck.py
- [[test_run_log.py]] - code - tests/test_run_log.py
- [[test_should_run_weekly_rollup_only_fires_sunday_2300_utc()]] - code - tests/test_run_log.py
- [[validate_and_write()]] - code - run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/extract_content
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY__content_fetch_url]]
- 17 edges to [[_COMMUNITY_posting_page.py]]
- 9 edges to [[_COMMUNITY_test_extract_content_with_no_internal_structure_stays_one_block]]
- 8 edges to [[_COMMUNITY_phd_only_exclusion]]
- 6 edges to [[_COMMUNITY_test_posting_page.py]]
- 5 edges to [[_COMMUNITY_test_extract_content_from_real_ashby_page]]
- 5 edges to [[_COMMUNITY_test_extract_content_dedupes_repeated_paragraph_real_conagra_case]]
- 4 edges to [[_COMMUNITY_test_extract_content_skips_google_careers_listing_shell]]
- 3 edges to [[_COMMUNITY_test_extract_content_strips_read_more_and_follow_us_chrome_real_manhattan_case]]

## Top bridge nodes
- [[run_pipeline.py]] - degree 58, connects to 9 communities
- [[validate_and_write()]] - degree 15, connects to 5 communities
- [[recheck.py]] - degree 23, connects to 3 communities
- [[load_profile()]] - degree 7, connects to 3 communities
- [[Path]] - degree 16, connects to 2 communities
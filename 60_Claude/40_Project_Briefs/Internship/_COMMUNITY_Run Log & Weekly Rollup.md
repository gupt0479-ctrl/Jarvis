---
type: community
members: 80
---

# Run Log & Weekly Rollup

**Members:** 80 nodes

## Members
- [[A bare 'remote' repo plus two independent clones (ourstheirs),     simulating o]] - rationale - tests/test_git_ops.py
- [[Both sides edit the same line of the same file — pull --rebase can     never cle]] - rationale - tests/test_git_ops.py
- [[Commit-and-push with a retry-once-on-rejected-push loop.  The Jarvis vault has i]] - rationale - core/git_ops.py
- [[Exercises commit_and_push_with_retry against real local git repos (a bare 'remot]] - rationale - tests/test_git_ops.py
- [[Fetch raw listings from each source. Used both by the scheduled pipeline and (wi]] - rationale - ingestion/sources.py
- [[Frontmatter dicts of every dossier file actually present in the vault     checko]] - rationale - vault_writer/writer.py
- [[GitPushError]] - code - core/git_ops.py
- [[Not a Dossier (doesn't go through validate.validate()'s dossier-specific     fro]] - rationale - tests/test_run_log.py
- [[Path]] - code
- [[Phase 3 orchestration schema-drift check - fetch - filter - dedup - validat]] - rationale - run_pipeline.py
- [[Real per-bucket file counts in the vault checkout — Viewed isn't one     of BUC]] - rationale - run_pipeline.py
- [[Returns ((uid, listing), ... for genuinely new items, already_seen_count).]] - rationale - run_pipeline.py
- [[Returns (updated_losses, newly_excluded (uid, listing), ...).     Increments]] - rationale - run_pipeline.py
- [[Returns {source_name {fetch_count int, matched Listing, ...}}.     excl]] - rationale - run_pipeline.py
- [[Stages everything under repo_dir, commits, and pushes. On a rejected     push (s]] - rationale - core/git_ops.py
- [[Task N (Prompt 5) — one line per uid the first time it's excluded,     same appe]] - rationale - core/run_log.py
- [[The actual scenario this module exists for 'theirs' (the vault's own     auto-c]] - rationale - tests/test_git_ops.py
- [[Two-tier run log per the plan raw per-run JSONL in this repo, a weekly markdown]] - rationale - core/run_log.py
- [[_append_markdown_line()]] - code - core/run_log.py
- [[_commit_log()]] - code - recheck.py
- [[_configure_identity()]] - code - tests/test_git_ops.py
- [[_git()]] - code - core/git_ops.py
- [[_log_messages()]] - code - tests/test_git_ops.py
- [[_run()]] - code - tests/test_git_ops.py
- [[_ts()]] - code - tests/test_run_log.py
- [[append_excluded_log()]] - code - core/run_log.py
- [[append_run_log()]] - code - core/run_log.py
- [[append_weekly_rollup()]] - code - core/run_log.py
- [[commit_and_push_with_retry()]] - code - core/git_ops.py
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
- [[file_github_issue()]] - code - run_pipeline.py
- [[format_weekly_rollup()]] - code - core/run_log.py
- [[git_ops.py]] - code - core/git_ops.py
- [[load_capacity_notified()]] - code - run_pipeline.py
- [[load_debate_losses()]] - code - run_pipeline.py
- [[load_excluded_uids()]] - code - run_pipeline.py
- [[load_profile()]] - code - core/filter.py
- [[load_recent_runs()]] - code - core/run_log.py
- [[load_seen_ids()]] - code - run_pipeline.py
- [[main()_2]] - code - recheck.py
- [[recheck.py]] - code - recheck.py
- [[remote_and_clones()]] - code - tests/test_git_ops.py
- [[run_log.py]] - code - core/run_log.py
- [[run_once()]] - code - run_pipeline.py
- [[run_pipeline.py]] - code - run_pipeline.py
- [[save_capacity_notified()]] - code - run_pipeline.py
- [[save_debate_losses()]] - code - run_pipeline.py
- [[save_excluded_uids()]] - code - run_pipeline.py
- [[save_seen_ids()]] - code - run_pipeline.py
- [[scan_dossiers()]] - code - vault_writer/writer.py
- [[should_run_weekly_rollup()]] - code - core/run_log.py
- [[sources.py]] - code - ingestion/sources.py
- [[test_append_run_log_writes_one_json_line_per_call()]] - code - tests/test_run_log.py
- [[test_append_weekly_rollup_appends_without_rewriting()]] - code - tests/test_run_log.py
- [[test_append_weekly_rollup_creates_file_with_header()]] - code - tests/test_run_log.py
- [[test_appended_run_log_note_has_no_blank_lines_or_stray_dashes()]] - code - tests/test_run_log.py
- [[test_format_weekly_rollup_aggregates_written_and_rejections()]] - code - tests/test_run_log.py
- [[test_format_weekly_rollup_handles_zero_activity()]] - code - tests/test_run_log.py
- [[test_git_ops.py]] - code - tests/test_git_ops.py
- [[test_load_recent_runs_filters_by_timestamp()]] - code - tests/test_run_log.py
- [[test_load_recent_runs_on_missing_file_returns_empty()]] - code - tests/test_run_log.py
- [[test_nothing_to_commit_returns_false()]] - code - tests/test_git_ops.py
- [[test_raises_after_exhausting_retries_on_persistent_conflict()]] - code - tests/test_git_ops.py
- [[test_retries_once_on_rejected_push_and_succeeds()]] - code - tests/test_git_ops.py
- [[test_run_log.py]] - code - tests/test_run_log.py
- [[test_should_run_weekly_rollup_only_fires_sunday_2300_utc()]] - code - tests/test_run_log.py
- [[test_simple_push_succeeds_without_race()]] - code - tests/test_git_ops.py
- [[update_debate_losses()]] - code - run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Run_Log__Weekly_Rollup
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Layer 1 Eligibility Filter]]
- 12 edges to [[_COMMUNITY_Dossier Writer (Vault Output)]]
- 9 edges to [[_COMMUNITY_Priority-Bucket Classification]]
- 9 edges to [[_COMMUNITY_Write-Gate Validation Tests]]
- 6 edges to [[_COMMUNITY_Fetch, Dedup & Identity]]
- 6 edges to [[_COMMUNITY_Feed Schema-Drift Checks]]
- 5 edges to [[_COMMUNITY_normalize_simplify]]
- 5 edges to [[_COMMUNITY_Posting Page Fetch & OPTPhD Screen]]
- 5 edges to [[_COMMUNITY_Recheck Closure Detection]]
- 4 edges to [[_COMMUNITY_CSSoftware Relevance Gate]]
- 3 edges to [[_COMMUNITY_Freehire Ingestion Source]]
- 2 edges to [[_COMMUNITY_Cross-Source Identity Keys]]
- 1 edge to [[_COMMUNITY_test_debate_losses.py]]

## Top bridge nodes
- [[run_pipeline.py]] - degree 72, connects to 12 communities
- [[load_profile()]] - degree 9, connects to 5 communities
- [[run_once()]] - degree 25, connects to 3 communities
- [[Path]] - degree 24, connects to 3 communities
- [[sources.py]] - degree 19, connects to 3 communities
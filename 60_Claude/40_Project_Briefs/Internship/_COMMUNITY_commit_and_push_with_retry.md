---
type: community
members: 44
---

# commit_and_push_with_retry

**Members:** 44 nodes

## Members
- [[A bare 'remote' repo plus two independent clones (ourstheirs),     simulating o]] - rationale - tests/test_git_ops.py
- [[A dossier written before dossier_uids.json existed (or hand-edited into     the]] - rationale - tests/test_recheck.py
- [[A source missing from feeds_by_source means its fetch failed — its     dossiers]] - rationale - tests/test_recheck.py
- [[Both sides edit the same line of the same file — pull --rebase can     never cle]] - rationale - tests/test_git_ops.py
- [[Commit-and-push with a retry-once-on-rejected-push loop.  The Jarvis vault has i]] - rationale - core/git_ops.py
- [[Exception]] - code
- [[Exercises commit_and_push_with_retry against real local git repos (a bare 'remot]] - rationale - tests/test_git_ops.py
- [[Frontmatter dicts of every dossier file actually present in the vault     checko]] - rationale - vault_writer/writer.py
- [[GitPushError]] - code - core/git_ops.py
- [[Real, reproducible bug found 2026-08-23 scan_dossiers() globs Viewed     along]] - rationale - tests/test_recheck.py
- [[Stages everything under repo_dir, commits, and pushes. On a rejected     push (s]] - rationale - core/git_ops.py
- [[The actual scenario this module exists for 'theirs' (the vault's own     auto-c]] - rationale - tests/test_git_ops.py
- [[{uid, path, reason} for dossiers whose posting closed. A source that     faile]] - rationale - recheck.py
- [[_commit_log()]] - code - recheck.py
- [[_configure_identity()]] - code - tests/test_git_ops.py
- [[_fm()]] - code - tests/test_recheck.py
- [[_git()]] - code - core/git_ops.py
- [[_log_messages()]] - code - tests/test_git_ops.py
- [[_run()]] - code - tests/test_git_ops.py
- [[commit_and_push_with_retry()]] - code - core/git_ops.py
- [[datetime_1]] - code
- [[fetch_josegael()]] - code - ingestion/sources.py
- [[fetch_simplify()]] - code - ingestion/sources.py
- [[fetch_vanshb03()]] - code - ingestion/sources.py
- [[fetch_zshah101()]] - code - ingestion/sources.py
- [[git_ops.py]] - code - core/git_ops.py
- [[main()_2]] - code - recheck.py
- [[plan_removals is the recheck's whole decision surface — pure, tested offline.]] - rationale - tests/test_recheck.py
- [[plan_removals()]] - code - recheck.py
- [[recheck.py]] - code - recheck.py
- [[remote_and_clones()]] - code - tests/test_git_ops.py
- [[scan_dossiers()]] - code - vault_writer/writer.py
- [[test_absent_from_feed_is_removed()]] - code - tests/test_recheck.py
- [[test_active_false_upstream_is_removed()]] - code - tests/test_recheck.py
- [[test_all_active_removes_nothing()]] - code - tests/test_recheck.py
- [[test_already_removed_dossier_is_not_re_swept()]] - code - tests/test_recheck.py
- [[test_dossier_with_no_manifest_entry_is_skipped_not_removed()]] - code - tests/test_recheck.py
- [[test_failed_fetch_skips_that_sources_dossiers_entirely()]] - code - tests/test_recheck.py
- [[test_git_ops.py]] - code - tests/test_git_ops.py
- [[test_nothing_to_commit_returns_false()]] - code - tests/test_git_ops.py
- [[test_raises_after_exhausting_retries_on_persistent_conflict()]] - code - tests/test_git_ops.py
- [[test_recheck.py]] - code - tests/test_recheck.py
- [[test_retries_once_on_rejected_push_and_succeeds()]] - code - tests/test_git_ops.py
- [[test_simple_push_succeeds_without_race()]] - code - tests/test_git_ops.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/commit_and_push_with_retry
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_recheck.py]]
- 12 edges to [[_COMMUNITY_test_filter.py]]
- 6 edges to [[_COMMUNITY_build_frontmatter]]
- 4 edges to [[_COMMUNITY_revalidate.py]]
- 3 edges to [[_COMMUNITY_plan_removals]]
- 1 edge to [[_COMMUNITY_vault_root]]
- 1 edge to [[_COMMUNITY_test_writer.py]]
- 1 edge to [[_COMMUNITY_writer.py]]

## Top bridge nodes
- [[recheck.py]] - degree 25, connects to 4 communities
- [[scan_dossiers()]] - degree 9, connects to 4 communities
- [[fetch_simplify()]] - degree 4, connects to 3 communities
- [[git_ops.py]] - degree 8, connects to 2 communities
- [[GitPushError]] - degree 8, connects to 2 communities
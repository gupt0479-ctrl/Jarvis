---
type: community
members: 19
---

# commit_and_push_with_retry

**Members:** 19 nodes

## Members
- [[A bare 'remote' repo plus two independent clones (ourstheirs),     simulating o]] - rationale - tests/test_git_ops.py
- [[Both sides edit the same line of the same file — pull --rebase can     never cle]] - rationale - tests/test_git_ops.py
- [[Commit-and-push with a retry-once-on-rejected-push loop.  The Jarvis vault has i]] - rationale - core/git_ops.py
- [[Exercises commit_and_push_with_retry against real local git repos (a bare 'remot]] - rationale - tests/test_git_ops.py
- [[GitPushError]] - code - core/git_ops.py
- [[Stages everything under repo_dir, commits, and pushes. On a rejected     push (s]] - rationale - core/git_ops.py
- [[The actual scenario this module exists for 'theirs' (the vault's own     auto-c]] - rationale - tests/test_git_ops.py
- [[_configure_identity()]] - code - tests/test_git_ops.py
- [[_git()]] - code - core/git_ops.py
- [[_log_messages()]] - code - tests/test_git_ops.py
- [[_run()]] - code - tests/test_git_ops.py
- [[commit_and_push_with_retry()]] - code - core/git_ops.py
- [[git_ops.py]] - code - core/git_ops.py
- [[remote_and_clones()]] - code - tests/test_git_ops.py
- [[test_git_ops.py]] - code - tests/test_git_ops.py
- [[test_nothing_to_commit_returns_false()]] - code - tests/test_git_ops.py
- [[test_raises_after_exhausting_retries_on_persistent_conflict()]] - code - tests/test_git_ops.py
- [[test_retries_once_on_rejected_push_and_succeeds()]] - code - tests/test_git_ops.py
- [[test_simple_push_succeeds_without_race()]] - code - tests/test_git_ops.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/commit_and_push_with_retry
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_recheck.py]]
- 3 edges to [[_COMMUNITY_write_dossier]]
- 3 edges to [[_COMMUNITY_test_writer.py]]
- 2 edges to [[_COMMUNITY_commit_and_push_with_retry_1]]
- 1 edge to [[_COMMUNITY_schema_drift.py]]

## Top bridge nodes
- [[GitPushError]] - degree 8, connects to 4 communities
- [[commit_and_push_with_retry()]] - degree 14, connects to 3 communities
- [[git_ops.py]] - degree 8, connects to 3 communities
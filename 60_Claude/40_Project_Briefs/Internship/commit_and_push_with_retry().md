---
source_file: "core/git_ops.py"
type: "code"
community: "recheck.py"
location: "L23"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/recheckpy
---

# commit_and_push_with_retry()

## Connections
- [[GitPushError]] - `calls` [EXTRACTED]
- [[Path]] - `calls` [INFERRED]
- [[Stages everything under repo_dir, commits, and pushes. On a rejected     push (s]] - `rationale_for` [EXTRACTED]
- [[_commit_log()]] - `calls` [EXTRACTED]
- [[_git()]] - `calls` [EXTRACTED]
- [[git_ops.py]] - `contains` [EXTRACTED]
- [[main()_2]] - `calls` [EXTRACTED]
- [[recheck.py]] - `imports` [EXTRACTED]
- [[run_pipeline.py]] - `imports` [EXTRACTED]
- [[test_git_ops.py]] - `imports` [EXTRACTED]
- [[test_nothing_to_commit_returns_false()]] - `calls` [EXTRACTED]
- [[test_raises_after_exhausting_retries_on_persistent_conflict()]] - `calls` [EXTRACTED]
- [[test_retries_once_on_rejected_push_and_succeeds()]] - `calls` [EXTRACTED]
- [[test_simple_push_succeeds_without_race()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/recheckpy
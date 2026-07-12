---
type: community
members: 14
---

# Paper-Test Contract Tests

**Members:** 14 nodes

## Members
- [[Paper-test contract tests thesis gate, timed entry, replay journal.]] - rationale - tests/test_paper.py
- [[make_thesis()]] - code - tests/test_paper.py
- [[test_action_vocabulary_is_closed()]] - code - tests/test_paper.py
- [[test_no_entry_before_window_opens()]] - code - tests/test_paper.py
- [[test_non_accumulate_theses_never_auto_enter()]] - code - tests/test_paper.py
- [[test_open_fill_requires_approval_and_window()]] - code - tests/test_paper.py
- [[test_paper.py]] - code - tests/test_paper.py
- [[test_paper_records_contain_no_execution_language()]] - code - tests/test_paper.py
- [[test_pending_reviews_jump_ahead_hook()]] - code - tests/test_paper.py
- [[test_replay_writes_journal_as_if_time_passed()]] - code - tests/test_paper.py
- [[test_thesis_approval_human_gate()]] - code - tests/test_paper.py
- [[test_thesis_requires_text_and_valid_window()]] - code - tests/test_paper.py
- [[test_timed_entry_fills_first_session_in_window()]] - code - tests/test_paper.py
- [[test_window_without_data_expires_honestly()]] - code - tests/test_paper.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Paper-Test_Contract_Tests
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Read API & Synthetic Fixtures]]
- 2 edges to [[_COMMUNITY_Paper Replay Run Model]]
- 1 edge to [[_COMMUNITY_Paper Trading Thesis Store]]
- 1 edge to [[_COMMUNITY_Paper Fill Model]]
- 1 edge to [[_COMMUNITY_DuckDB Storage Layer & Timestamp Fix]]
- 1 edge to [[_COMMUNITY_DB Schema Init Tests]]
- 1 edge to [[_COMMUNITY_Journal Entry Model]]

## Top bridge nodes
- [[test_paper.py]] - degree 20, connects to 4 communities
- [[make_thesis()]] - degree 12, connects to 1 community
- [[test_open_fill_requires_approval_and_window()]] - degree 3, connects to 1 community
- [[test_replay_writes_journal_as_if_time_passed()]] - degree 3, connects to 1 community
- [[test_paper_records_contain_no_execution_language()]] - degree 3, connects to 1 community
---
type: community
members: 16
---

# build_frontmatter

**Members:** 16 nodes

## Members
- [[A single fetch hiccup (fetch_count == 0, e.g. a swallowed     RequestException)]] - rationale - tests/test_zero_match_alert.py
- [[A source that has never once produced a match isn't drifting, it's     just stru]] - rationale - tests/test_zero_match_alert.py
- [[Integration-level confirmation that run_once actually calls issue_fn     once th]] - rationale - tests/test_zero_match_alert.py
- [[Pins the real, concrete incident this task was built from (Prompt 19     Task 1)]] - rationale - tests/test_zero_match_alert.py
- [[Task 3 (Prompt 19, 2026-08-28) — per-source zero-match-rate alert.  Same pure f]] - rationale - tests/test_zero_match_alert.py
- [[test_load_save_zero_match_streaks_round_trips()]] - code - tests/test_zero_match_alert.py
- [[test_load_zero_match_streaks_missing_file_returns_empty_dict()]] - code - tests/test_zero_match_alert.py
- [[test_run_once_does_not_alert_below_threshold()]] - code - tests/test_zero_match_alert.py
- [[test_run_once_files_issue_and_persists_state_on_zero_match_streak()]] - code - tests/test_zero_match_alert.py
- [[test_zero_match_alert.py]] - code - tests/test_zero_match_alert.py
- [[test_zero_match_streak_fires_exactly_once_at_threshold()]] - code - tests/test_zero_match_alert.py
- [[test_zero_match_streak_increments_while_fetching_but_not_matching()]] - code - tests/test_zero_match_alert.py
- [[test_zero_match_streak_never_alerts_if_source_never_matched()]] - code - tests/test_zero_match_alert.py
- [[test_zero_match_streak_real_ashby_incident_shape()]] - code - tests/test_zero_match_alert.py
- [[test_zero_match_streak_resets_on_a_real_match_and_marks_ever_matched()]] - code - tests/test_zero_match_alert.py
- [[test_zero_match_streak_unaffected_by_a_zero_fetch_run()]] - code - tests/test_zero_match_alert.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/build_frontmatter
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_writer.py]]
- 1 edge to [[_COMMUNITY_recheck.py]]

## Top bridge nodes
- [[test_zero_match_alert.py]] - degree 13, connects to 2 communities
- [[test_run_once_files_issue_and_persists_state_on_zero_match_streak()]] - degree 3, connects to 1 community
- [[test_run_once_does_not_alert_below_threshold()]] - degree 2, connects to 1 community
---
type: community
members: 3
---

# validate_and_write

**Members:** 3 nodes

## Members
- [[Renders + validates each new listing; writes the ones that pass into     the Jar]] - rationale - run_pipeline.py
- [[build_matched_reason()]] - code - run_pipeline.py
- [[validate_and_write()]] - code - run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/validate_and_write
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_run_pipeline.py]]
- 3 edges to [[_COMMUNITY_test_debate_losses.py]]
- 2 edges to [[_COMMUNITY_debate_compare]]
- 2 edges to [[_COMMUNITY_dedup_new]]
- 1 edge to [[_COMMUNITY_test_cross_source_key_punctuation_insensitive_marmon_case]]
- 1 edge to [[_COMMUNITY_run_log.py]]
- 1 edge to [[_COMMUNITY_validate.py]]
- 1 edge to [[_COMMUNITY_update_debate_losses]]

## Top bridge nodes
- [[validate_and_write()]] - degree 16, connects to 8 communities
- [[build_matched_reason()]] - degree 2, connects to 1 community
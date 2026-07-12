---
type: community
members: 10
---

# Paper Replay Run Model

**Members:** 10 nodes

## Members
- [[.get_replay_run()]] - code - src/research_data/paper/store.py
- [[.validate_range()]] - code - src/research_data/paper/models.py
- [[One accelerated historical replay over a date range.]] - rationale - src/research_data/paper/models.py
- [[One accelerated historical replay over a date range._1]] - rationale - src/research_data/paper/models.py
- [[ReplayRun]] - code - src/research_data/paper/models.py
- [[Typed paper-trading records. No execution language, full provenance.]] - rationale - src/research_data/paper/models.py
- [[_new_id()_1]] - code - src/research_data/paper/models.py
- [[_utcnow()_1]] - code - src/research_data/paper/models.py
- [[datetime_8]] - code
- [[models.py_3]] - code - src/research_data/paper/models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Paper_Replay_Run_Model
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Paper Trading Thesis Store]]
- 3 edges to [[_COMMUNITY_Brain Model Enums & Ids]]
- 2 edges to [[_COMMUNITY_Journal Entry Model]]
- 2 edges to [[_COMMUNITY_Brain Closed-Loop Rules]]
- 2 edges to [[_COMMUNITY_Paper-Test Contract Tests]]
- 1 edge to [[_COMMUNITY_Paper Replay Lesson Citation Wiring]]
- 1 edge to [[_COMMUNITY_Gate Harness Return Metrics]]
- 1 edge to [[_COMMUNITY_Paper Engine Replay Execution]]
- 1 edge to [[_COMMUNITY_Paper Fill Model]]
- 1 edge to [[_COMMUNITY_OHLCVRecord Model Field Validators]]

## Top bridge nodes
- [[ReplayRun]] - degree 13, connects to 6 communities
- [[models.py_3]] - degree 13, connects to 4 communities
- [[.get_replay_run()]] - degree 4, connects to 1 community
- [[.validate_range()]] - degree 2, connects to 1 community
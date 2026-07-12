---
type: community
members: 35
---

# Paper Trading Thesis Store

**Members:** 35 nodes

## Members
- [[.__init__()_10]] - code - src/research_data/paper/store.py
- [[.add_journal_entry()]] - code - src/research_data/paper/store.py
- [[.approve_thesis()]] - code - src/research_data/paper/store.py
- [[.complete_replay_run()]] - code - src/research_data/paper/store.py
- [[.create_replay_run()]] - code - src/research_data/paper/store.py
- [[.get_journal_entry()]] - code - src/research_data/paper/store.py
- [[.get_thesis()]] - code - src/research_data/paper/store.py
- [[.init_schema()_2]] - code - src/research_data/paper/store.py
- [[.list_theses()]] - code - src/research_data/paper/store.py
- [[.propose_thesis()]] - code - src/research_data/paper/store.py
- [[.record_fill()]] - code - src/research_data/paper/store.py
- [[.set_thesis_status()]] - code - src/research_data/paper/store.py
- [[.validate_thesis_text()]] - code - src/research_data/paper/models.py
- [[.validate_window()]] - code - src/research_data/paper/models.py
- [[A pre-approval contract why, what, when, and how much.      Timed auto-entry is]] - rationale - src/research_data/paper/models.py
- [[DuckDB persistence for theses, fills, journal entries, and replay runs.]] - rationale - src/research_data/paper/store.py
- [[DuckDBPyConnection_3]] - code
- [[Human gate PROPOSED → APPROVED. Auto-entry is illegal before this.]] - rationale - src/research_data/paper/store.py
- [[Human gate PROPOSED → APPROVED. Auto-entry is illegal before this._1]] - rationale - src/research_data/paper/store.py
- [[Naive-UTC normalization (DuckDB TIMESTAMP converts aware → local)._1]] - rationale - src/research_data/paper/store.py
- [[PaperStore]] - code - src/research_data/paper/store.py
- [[PaperStoreError]] - code - src/research_data/paper/store.py
- [[Persist a fill. OPEN fills demand an approved thesis and a fill         date ins]] - rationale - src/research_data/paper/store.py
- [[Persist a fill. OPEN fills demand an approved thesis and a fill         date ins_1]] - rationale - src/research_data/paper/store.py
- [[Raised on illegal paper-store operations.]] - rationale - src/research_data/paper/store.py
- [[Thesis]] - code - src/research_data/paper/models.py
- [[ThesisStatus]] - code - src/research_data/paper/models.py
- [[Typed persistence API for the paper book.]] - rationale - src/research_data/paper/store.py
- [[Typed persistence API for the paper book._1]] - rationale - src/research_data/paper/store.py
- [[_as_utc()_1]] - code - src/research_data/paper/store.py
- [[_loads()_1]] - code - src/research_data/paper/store.py
- [[_row_to_thesis()]] - code - src/research_data/paper/store.py
- [[_to_db_ts()_2]] - code - src/research_data/paper/store.py
- [[datetime_9]] - code
- [[store.py_2]] - code - src/research_data/paper/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Paper_Trading_Thesis_Store
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Journal Entry Model]]
- 6 edges to [[_COMMUNITY_Paper Replay Run Model]]
- 4 edges to [[_COMMUNITY_Brain Closed-Loop Rules]]
- 4 edges to [[_COMMUNITY_Paper Fill Model]]
- 3 edges to [[_COMMUNITY_Paper Replay Lesson Citation Wiring]]
- 3 edges to [[_COMMUNITY_Brain Model Enums & Ids]]
- 2 edges to [[_COMMUNITY_Fundamentals Backfill & Study Scripts]]
- 2 edges to [[_COMMUNITY_OHLCVRecord Model Field Validators]]
- 1 edge to [[_COMMUNITY_Assemble & Gate Projection Modules]]
- 1 edge to [[_COMMUNITY_StrategySpec Lifecycle & Human Gate]]
- 1 edge to [[_COMMUNITY_Gate Harness Return Metrics]]
- 1 edge to [[_COMMUNITY_Paper Engine Replay Execution]]
- 1 edge to [[_COMMUNITY_Paper-Test Contract Tests]]
- 1 edge to [[_COMMUNITY_DB Schema Init Tests]]

## Top bridge nodes
- [[PaperStore]] - degree 27, connects to 8 communities
- [[Thesis]] - degree 14, connects to 5 communities
- [[_as_utc()_1]] - degree 6, connects to 3 communities
- [[store.py_2]] - degree 10, connects to 2 communities
- [[PaperStoreError]] - degree 9, connects to 2 communities
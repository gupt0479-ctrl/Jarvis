# C29 — Refutation Loop Logic

**Community 29** — 5 nodes, cohesion 0.33

Shared refutation loop termination rules used by both the coordinator and legacy graph.

## Key Nodes

`refutation_next_step()`, `_run_causal_loop()`, `Refutation loop termination rules shared by coordinator and legacy graph.`, `Stop when refuters pass or when estimation is explicitly withheld.`

## What This Code Does

`refutation_next_step(state)` checks two termination conditions:
1. `causal_refutation_passed` is True → `"end"`
2. `method == "withheld:data_quality_gates"` → `"end"` (no point retrying when data is insufficient)
3. Otherwise → `"causal_synthesis"` (retry)

`_run_causal_loop()` is the while-loop wrapper in `coordinator/runner.py` that calls causal_synthesis_node + dowhy_engine_node and checks `refutation_next_step` each iteration.

## Source Files

`src/coordinator/refutation.py`, `src/coordinator/runner.py`

## Related Notes

- [[causal-engine/03-estimation|Estimation]] — produces causal_refutation_passed
- [[pipeline/01-langgraph-topology|LangGraph Topology]] — conditional_refutation_check uses this

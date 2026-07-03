---
type: project
status: sprout
created: 2026-07-01
tags:
  - brief
  - causalops
---
﻿---
tags: [causalops, langgraph, pipeline, graph]
---

# LangGraph Pipeline

> **Note:** `src/graph.py` is **deprecated for execution** in Phase 2b+. The [[Coordinator Execution Model]] replaced `graph.ainvoke()` with a phase-by-phase coordinator. `graph.py` remains for reference and refutation routing tests.

## Original Topology

```
START
  ↓
orchestrator              ← grand_orchestrator_node (LLM)
  ↓ route_to_parents (conditional: Send per AgentConfig)
parent_agent              ← parent_agent_node (LLM, parallel)
  ↓ (all merge at)
gather_children           ← gather_children_node (barrier)
  ↓ route_to_children (conditional: Send per ChildConfig)
child_agent               ← child_agent_node (LLM, parallel)
  ↓ (all merge at)
evaluate_memos            ← evaluate_memos_node (LLM)
  ↓
causal_synthesis          ← causal_synthesis_node (LLM)
  ↓
dowhy_engine              ← dowhy_engine_node (deterministic)
  ↓ conditional_refutation_check
  ├── "end" → END
  └── "causal_synthesis" → causal_synthesis (retry loop)
```

## Node Functions

| Node | Function | Location | LLM? |
|------|----------|----------|------|
| `orchestrator` | `grand_orchestrator_node` | `agents.py` | Yes |
| `parent_agent` | `parent_agent_node` | `agents.py` | Yes |
| `gather_children` | `gather_children_node` | `graph.py` | No |
| `child_agent` | `child_agent_node` | `agents.py` | Yes |
| `evaluate_memos` | `evaluate_memos_node` | `evaluator.py` | Yes |
| `causal_synthesis` | `causal_synthesis_node` | `causal.py` | Yes |
| `dowhy_engine` | `dowhy_engine_node` | `causal.py` | No |

## Parallel Fan-Out Mechanism

LangGraph uses `Send` objects for parallel dispatch. Each `Send` targets a node name and provides a sub-state dict. The results are merged back via the reducer annotations on `GraphState`.

```python
# route_to_parents: one Send per AgentConfig
return [
    Send("parent_agent", {
        "task_description": state["task_description"],
        "run_id": state["run_id"],
        "correlation_id": state["correlation_id"],
        "persona": config.persona,
        "focus_objective": config.focus_objective,
        "policy": config.policy.model_dump() if config.policy else None,
    })
    for config in state.get("parent_configs", [])
]
```

The `child_configs` field uses `operator.add` as its reducer — so when multiple parent agents return `{"child_configs": [...]}`, LangGraph accumulates all of them.

## Refutation Loop

After `dowhy_engine`, `conditional_refutation_check` decides whether to retry:
- If refuters passed **or** ATE was withheld → `"end"` (stop)
- Otherwise → `"causal_synthesis"` (retry with the same evidence, potentially refining the DAG)

The check is delegated to `coordinator.refutation.refutation_next_step(state)`.

## Phase 2b Replacement

The coordinator (`coordinator/runner.py`) executes the same logical phases but:
- Uses async barriers instead of LangGraph's graph edges
- Persists phase-by-phase state to `RunRecord` in SQLite
- Dispatches parent/child tasks via Kafka `hivemind.spawn` topic
- Worker process (`src/worker/`) consumes spawn tasks and executes agents
- Enables recovery after restarts (SQLite state survives container restarts)

## Related Notes

- [[Coordinator Execution Model]] — What actually runs in Phase 2b
- [[GraphState Contract]] — The shared state TypedDict
- [[agents]] — Node implementations
- [[causal]] — Causal synthesis + DoWhy engine nodes

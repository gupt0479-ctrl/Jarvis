# LangGraph Topology

`src/graph.py` defines the original LangGraph workflow. Deprecated for execution in Phase 2b+: the [[pipeline/02-coordinator|coordinator]] replaced `graph.ainvoke()`. This file still ships for reference and refutation routing tests.

## Node-to-Function Table

| Node | Function | Source file | LLM? |
|------|----------|------------|------|
| `orchestrator` | `grand_orchestrator_node` | `agents.py` | Yes |
| `parent_agent` | `parent_agent_node` | `agents.py` | Yes |
| `gather_children` | `gather_children_node` | `graph.py` | No (barrier) |
| `child_agent` | `child_agent_node` | `agents.py` | Yes |
| `evaluate_memos` | `evaluate_memos_node` | `evaluator.py` | Yes |
| `causal_synthesis` | `causal_synthesis_node` | `causal.py` | Yes |
| `dowhy_engine` | `dowhy_engine_node` | `causal.py` | No |

## Graph Topology (diagram)

```
START
  ↓
orchestrator
  ↓ route_to_parents (conditional edges → Send per AgentConfig)
parent_agent  ← parallel fan-out
  ↓ (all converge at)
gather_children  ← barrier
  ↓ route_to_children (conditional edges → Send per ChildConfig)
child_agent  ← parallel fan-out
  ↓ (all converge at)
evaluate_memos
  ↓
causal_synthesis
  ↓
dowhy_engine
  ↓ conditional_refutation_check
  ├── "end" → END
  └── "causal_synthesis" → (retry loop)
```

## Parallel Fan-Out: Send Mechanics

LangGraph dispatches parallel agents using `Send` objects. Each `Send` targets a node name and provides a sub-state dict. Results merge via `operator.add` reducer annotations on the fields.

```python
def route_to_parents(state: GraphState) -> list[Send]:
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

`child_configs` uses `operator.add` as its reducer — multiple parent agents all return `{"child_configs": [...]}` and LangGraph accumulates all children.

## Gather Children Node

A pure barrier — no computation, just a convergence point so all parent `child_configs` are collected before child dispatch begins:

```python
def gather_children_node(state: GraphState) -> dict:
    child_count = len(state.get("child_configs", []))
    return {}   # returns nothing; reducer accumulation already happened
```

## Refutation Loop

`conditional_refutation_check` delegates to `coordinator.refutation.refutation_next_step(state)`:
- If `causal_refutation_passed` is True → `"end"`
- If `method == "withheld:data_quality_gates"` → `"end"` (no point retrying if data is insufficient)
- Otherwise → `"causal_synthesis"` (retry DAG design)

## Why the Coordinator Replaced This

| Problem with `graph.ainvoke` | Coordinator solution |
|------------------------------|---------------------|
| State is ephemeral (crash loses everything) | SQLite `RunRecord` persists each phase |
| Can't run Kafka producer + consumer in same loop | api container publishes, worker container consumes |
| No recovery after container restart | SQLite state survives restarts |
| Fan-out blocking = backpressure on event loop | Kafka barriers decouple producer from consumer |

`graph.py` nodes (the functions) still work unchanged — the coordinator calls them directly via `asyncio.to_thread`.

## Related Notes

- [[pipeline/02-coordinator|Coordinator]] — what actually executes in Phase 2b
- [[pipeline/03-graphstate|GraphState]] — the shared state TypedDict all nodes read/write
- [[agents/00-agent-hierarchy|Agent Hierarchy]] — what each node tier decides

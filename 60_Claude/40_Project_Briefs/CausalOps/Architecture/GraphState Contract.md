---
type: project
status: sprout
created: 2026-07-01
tags: [causalops, schema, langgraph, state]
---

# GraphState Contract

`GraphState` is the master LangGraph `TypedDict` defined in `src/schema.py`. Every node in the workflow reads from it and returns only the fields it changes (LangGraph merges partial updates).

## Full TypedDict Definition

```python
class GraphState(TypedDict):
    # Core identity
    task_description: str         # The incident/scenario prompt
    run_id: str                   # Unique run identifier (e.g. "run-20260601-143022-a1b2c3d4")
    correlation_id: str           # Matches run_id; used for Kafka envelope correlation

    # Agent configs (orchestrator → parent evolution → parent dispatch)
    parent_configs: list[AgentConfig]
    child_configs: Annotated[list[ChildConfig], operator.add]  # reducer: accumulate across parents

    # Agent outputs (child agents → evaluator)
    memos: Annotated[list[DecisionMemo], operator.add]         # reducer: accumulate across children
    ranked_strategies: list[dict[str, Any]]
    final_recommendation: str | None
    evaluator_error: str | None

    # Causal outputs (causal synthesis → DoWhy → reasoning)
    causal_payload: dict[str, Any] | None         # CausalPayload.model_dump()
    causal_refutation_passed: bool
    causal_refutation_attempts: int
    dowhy_results: dict[str, Any] | None          # legacy format
    evidence_records: list[dict[str, Any]]        # EvidenceRecord dicts from caller
    causal_dataset_profile: dict[str, Any] | None # CausalDatasetProfile.model_dump()
    causal_estimate_report: dict[str, Any] | None # CausalEstimateReport.model_dump()
    causal_discovery_report: dict[str, Any] | None
    reasoning_report: dict[str, Any] | None

    # Learning outputs (evolution → policy learning)
    agent_evolution_report: dict[str, Any] | None
    policy_optimization_report: dict[str, Any] | None
```

## Reducer Semantics

Two fields use `Annotated[list, operator.add]` which means LangGraph **appends** rather than replaces:
- `child_configs` — each parent agent returns `{"child_configs": [ChildConfig, ...]}` and LangGraph accumulates all children from all parents
- `memos` — each child agent returns `{"memos": [DecisionMemo]}` and LangGraph accumulates all memos from all children

All other fields are **replaced** on each node update (last writer wins).

## Parallel Sub-State TypedDicts

Parent and child agents run as parallel LangGraph `Send` dispatches. They receive their own sub-state objects:

### ParentState
```python
class ParentState(TypedDict):
    task_description: str
    run_id: str
    correlation_id: str
    persona: str           # from AgentConfig.persona
    focus_objective: str   # from AgentConfig.focus_objective
    policy: NotRequired[dict[str, Any] | None]  # evolved AgentPolicy.model_dump()
```

### ChildState
```python
class ChildState(TypedDict):
    task_description: str
    run_id: str
    correlation_id: str
    parent_persona: str    # which parent spawned this child
    persona: str           # from ChildConfig.persona
    focus_objective: str   # from ChildConfig.focus_objective
    policy: NotRequired[dict[str, Any] | None]  # evolved AgentPolicy.model_dump()
```

## Key Pydantic Models

### AgentConfig
```python
class AgentConfig(BaseModel):
    persona: str              # e.g. "Network Forensics Analyst"
    focus_objective: str      # e.g. "Trace lateral movement from initial compromise"
    policy: AgentPolicy | None  # attached by island evolution
```

### ChildConfig
```python
class ChildConfig(BaseModel):
    parent_persona: str       # set by coordinator after parent runs
    persona: str
    focus_objective: str
    policy: AgentPolicy | None
```

### AgentPolicy (compact EA genome → prompt prior)
```python
class AgentPolicy(BaseModel):
    policy_id: str            # e.g. "parent.network_forensics_analyst.a1b2c3d4e5"
    island_id: str            # e.g. "parent-island-2"
    generation: int
    traits: dict[str, float]  # 8 traits: evidence_weight, causal_focus, etc.
    mutation_rate: float
    fitness: float
    lineage: list[str]        # last 5 ancestry labels
    objective_hint: str | None  # top 3 trait names rendered as text
```

### DecisionMemo
```python
class DecisionMemo(BaseModel):
    perspective: str          # child persona
    strategy: str             # recommended action
    risks: list[str]
    assumptions: list[str]
    second_order_effects: list[str]
    evidence_needs: list[str] # concrete telemetry/logs/CVEs needed
    confidence: str | None    # "High" | "Medium" | "Low" | "N/A"
```

## How Coordinator Uses This

In Phase 2b, the `RunRecord` in `coordinator/store.py` mirrors `GraphState` as a dataclass. `record.to_graph_state()` converts it into a dict compatible with this TypedDict for passing to node functions. `record.apply_node_update(update)` applies partial node updates back.

## Related Notes

- [[schema]] — Full source code reference
- [[agents]] — Nodes that produce parent/child configs and memos
- [[Coordinator Execution Model]] — How RunRecord bridges coordinator ↔ graph nodes
- [[System Overview]] — Pipeline context

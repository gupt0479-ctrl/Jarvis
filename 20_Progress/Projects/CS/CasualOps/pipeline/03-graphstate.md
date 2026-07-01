# GraphState Contract

`GraphState` in `src/schema.py` is the master `TypedDict` shared across all LangGraph nodes and coordinator phases. Every node reads from it and returns only the fields it changes — LangGraph (or the coordinator bridge) merges partial updates.

## Full Field Listing

```python
class GraphState(TypedDict):
    # Core identity
    task_description: str         # the incident/scenario prompt
    run_id: str                   # e.g. "run-20260601-143022-a1b2c3d4"
    correlation_id: str           # matches run_id; used for Kafka envelope correlation

    # Agent configs (orchestrator → evolution → dispatch)
    parent_configs: list[AgentConfig]
    child_configs: Annotated[list[ChildConfig], operator.add]  # accumulate across parents

    # Agent outputs (children → evaluator)
    memos: Annotated[list[DecisionMemo], operator.add]  # accumulate across children
    ranked_strategies: list[dict[str, Any]]
    final_recommendation: str | None
    evaluator_error: str | None

    # Causal pipeline outputs
    causal_payload: dict[str, Any] | None         # CausalPayload.model_dump()
    causal_refutation_passed: bool
    causal_refutation_attempts: int
    dowhy_results: dict[str, Any] | None          # legacy format
    evidence_records: list[dict[str, Any]]        # EvidenceRecord dicts from caller
    causal_dataset_profile: dict[str, Any] | None
    causal_estimate_report: dict[str, Any] | None
    causal_discovery_report: dict[str, Any] | None
    reasoning_report: dict[str, Any] | None

    # Learning outputs
    agent_evolution_report: dict[str, Any] | None
    policy_optimization_report: dict[str, Any] | None

    # Memory layer (planned — added by memory implementation)
    run_id: str                                    # already present; used to key memory writes
    memory_context: list[dict[str, Any]] | None   # retrieved past context — list of dicts, NOT str
```

## Three State Layers

The fields cluster into three distinct authorship zones:

**Layer 1 — Agent hypotheses.** `parent_configs`, `child_configs`, `memos`, `ranked_strategies`, `final_recommendation`. LLM-authored. Never fed into the estimator.

**Layer 2 — Evidence and estimation.** `evidence_records`, `causal_payload`, `causal_dataset_profile`, `causal_estimate_report`, `causal_discovery_report`. Deterministic code produces this from external records.

**Layer 3 — Learning.** `agent_evolution_report`, `policy_optimization_report`, `reasoning_report`. Deterministic code using Layer 1 + 2 as input signal.

## Reducer Semantics

Two fields use `Annotated[list, operator.add]` — LangGraph **appends** rather than replaces:

- `child_configs` — each parent returns `{"child_configs": [ChildConfig, ...]}` and LangGraph accumulates all across all parents
- `memos` — each child returns `{"memos": [DecisionMemo]}` and all accumulate

All other fields: last writer wins (replacement semantics).

## Parallel Sub-States

Parent and child agents receive isolated sub-state TypedDicts, not the full GraphState:

```python
class ParentState(TypedDict):
    task_description: str
    run_id: str
    correlation_id: str
    persona: str
    focus_objective: str
    policy: NotRequired[dict[str, Any] | None]  # evolved AgentPolicy.model_dump()

class ChildState(TypedDict):
    task_description: str
    run_id: str
    correlation_id: str
    parent_persona: str    # which parent spawned this child
    persona: str
    focus_objective: str
    policy: NotRequired[dict[str, Any] | None]
```

These are passed via `Send` objects in `graph.py` or via Kafka spawn events in the coordinator.

## Key Pydantic Models Behind the Fields

**AgentPolicy** (the EA genome → prompt prior):
```python
class AgentPolicy(BaseModel):
    policy_id: str            # e.g. "parent.network_forensics_analyst.a1b2c3d4e5"
    island_id: str
    generation: int
    traits: dict[str, float]  # 8 traits, all float in [0,1]
    mutation_rate: float
    fitness: float
    lineage: list[str]        # last 5 ancestry labels
    objective_hint: str | None
```

**DecisionMemo** (child agent output):
```python
class DecisionMemo(BaseModel):
    perspective: str
    strategy: str
    risks: list[str]
    assumptions: list[str]
    second_order_effects: list[str]
    evidence_needs: list[str]  # must be concrete: logs, CVEs, telemetry
    confidence: str | None     # "High" | "Medium" | "Low" | "N/A"
```

## RunRecord Bridge

In Phase 2b, `coordinator/store.py`'s `RunRecord` mirrors `GraphState` as a dataclass. `record.to_graph_state()` converts it to a GraphState-compatible dict. `record.apply_node_update(update)` applies partial node updates back, with `operator.add` semantics for list fields.

## Related Notes

- [[agents/00-agent-hierarchy|Agent Hierarchy]] — who writes which fields
- [[pipeline/02-coordinator|Coordinator]] — how RunRecord bridges to GraphState
- [[causal-engine/02-evidence|Evidence]] — what evidence_records contains
- [[memory-layer/00-design|Memory Layer Design]] — memory_context field (planned)

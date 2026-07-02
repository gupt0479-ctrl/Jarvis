---
type: project
status: active
created: 2026-07-02
updated: 2026-07-02
related_progress:
  - "[[CausalOps — Index]]"
tags:
  - causalops
  - agents
  - langgraph
next: "[[causal-engine]]"
---

# Agents

CausalOps uses three tiers of LLM agents. Each tier narrows scope: the orchestrator decomposes the incident, parents decompose into sub-problems, children solve one sub-problem each and produce the DecisionMemos that feed the causal pipeline.

## Three Tiers

```
Grand Orchestrator  (1)
  -> produces 2-3 AgentConfigs
Parent Agents  (2-3, parallel)
  -> each produces 2 ChildConfigs
Child Agents  (4-6, parallel)
  -> each produces 1 DecisionMemo
```

| Tier | LLM temp | Output | Count per run |
|------|----------|--------|---------------|
| Grand Orchestrator | 0.4 | `list[AgentConfig]` | 1 |
| Parent Agent | 0.4 | `list[ChildConfig]` | 2-3 |
| Child Agent | 0.0 | `DecisionMemo` | 4-6 |

Child agents use `temperature=0.0` (deterministic). Their memos are the raw input to the evaluator.

## Grand Orchestrator (grand_orchestrator_node)

Decomposes the incident into 2-3 distinct investigatory vectors (geopolitical context, network forensics, identity risk, supply-chain exposure, insider threat). It does not investigate -- it assigns investigation scope.

```python
def grand_orchestrator_node(state: GraphState) -> dict:
    # Returns: {"parent_configs": list[AgentConfig]}
```

Structured output via `llm.with_structured_output(ParentConfigsOutput)`. LLM is Gemini via `src/llm.py`.

**Memory context injection:** `memory_context` is `list[dict[str, Any]] | None` in GraphState -- a structured list, not a string. The orchestrator formats it using `_format_memory_context()`:

```python
ctx = state.get("memory_context") or []
if ctx:
    prompt = ORCHESTRATOR_PROMPT + "\n\n## Relevant Past Incidents\n" + _format_memory_context(ctx)
```

Do NOT do `state.get("memory_context") or ""` -- it's a list, not a string. Past context goes into the orchestrator prompt only. Never as `EvidenceRecord` objects.

## Parent Agents (parent_agent_node)

Receive one investigatory vector and think metacognitively: what are the blind spots? What sub-problems need specialized attention? Each parent spawns exactly 2 child agents with specific personas and objectives.

Parallel fan-out via `Send` objects in LangGraph, or via `hivemind.spawn` Kafka topic in the coordinator.

## Child Agents (child_agent_node)

Receive one sub-problem and perform granular investigation. Output a `DecisionMemo`:

```python
class DecisionMemo(BaseModel):
    perspective: str
    strategy: str
    risks: list[str]
    assumptions: list[str]
    second_order_effects: list[str]
    evidence_needs: list[str]  # must name concrete telemetry, logs, CVEs -- not vague descriptions
    confidence: str | None     # "High" | "Medium" | "Low" | "N/A"
```

`evidence_needs` is the critical field. It must name concrete telemetry, logs, CVE feeds, or incident-report facts -- not vague descriptions.

**Failure handling:** If any child agent fails (content filter, timeout, exception), `_fallback_memo()` returns a memo with `strategy: "[UNAVAILABLE - reason]"` and `confidence: "Low"`. A single child failure cannot crash the pipeline.

## Island Evolution (evolution.py)

Before agents run, `evolution.py` runs a steady-state island EA over their configurations. Each agent gets an `AgentPolicy` with 8 trait values that steer its prompt:

```
policy_id=parent.network_forensics.a1b2;
prioritize causal focus, evidence weight;
top_traits=causal_focus=0.86, evidence_weight=0.84
```

The 8 traits: `evidence_weight`, `causal_focus`, `temporal_awareness`, and 5 others. Evolution steers agents toward more evidence-focused investigation without changing what they investigate.

**AgentPolicy:**
```python
class AgentPolicy(BaseModel):
    policy_id: str
    island_id: str
    generation: int
    traits: dict[str, float]   # 8 traits, all float in [0,1]
    mutation_rate: float
    fitness: float
    lineage: list[str]         # last 5 ancestry labels
    objective_hint: str | None
```

Fitness function: weighted combination of evaluator scores, causal estimate quality, anomaly counts, and evidence completeness from memos.

`evolve_parent_configs(state, configs)` runs before parent dispatch. `evolve_child_configs(state, configs)` runs before child dispatch. Both are deterministic.

## Evaluator (evaluator.py)

`evaluate_memos_node` ranks all DecisionMemos from all children. Uses LLM with structured output (`EvaluationScore`). Produces `ranked_strategies` and `final_recommendation`.

```python
class EvaluationScore(BaseModel):
    memo_id: str
    score: float          # 0.0-1.0
    reasoning: str
    key_strengths: list[str]
    key_weaknesses: list[str]
```

The evaluator's ranked output feeds into causal synthesis -- the causal architect uses the top recommendations as context when designing the DAG.

## Telemetry

Every agent node publishes `EXECUTION_PHASE` events to Kafka `hivemind.telemetry` at start and end. The frontend subscribes via `GET /run/{run_id}/events` SSE for live progress.

## Related Notes

- [[CausalOps — Index]] -- project index
- [[pipeline-coordinator]] -- how coordinator phases call these nodes
- [[causal-engine]] -- what agent output feeds into
- [[memory-layer]] -- memory_retrieve and memory_write nodes

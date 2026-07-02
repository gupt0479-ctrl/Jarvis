# Agent Hierarchy

CausalOps uses three tiers of LLM agents. Each tier narrows scope: the orchestrator decomposes the incident, parents decompose into sub-problems, children solve one sub-problem each and produce the DecisionMemos that feed the causal pipeline.

## Three Tiers

```
Grand Orchestrator  (1)
  ↓ produces 2-3 AgentConfigs
Parent Agents  (2-3, parallel)
  ↓ each produces 2 ChildConfigs
Child Agents  (4-6, parallel)
  ↓ each produces 1 DecisionMemo
```

| Tier | LLM temp | Output | Count per run |
|------|----------|--------|---------------|
| Grand Orchestrator | 0.4 | `list[AgentConfig]` | 1 |
| Parent Agent | 0.4 | `list[ChildConfig]` | 2-3 |
| Child Agent | 0.0 | `DecisionMemo` | 4-6 |

Child agents use `temperature=0.0` (deterministic) — their memos are the raw evidence input to the evaluator, and variation here adds noise without value.

## What Each Level Decides

**Grand Orchestrator** decomposes the incident into 2-3 distinct investigatory vectors — geopolitical context, network forensics, identity risk, supply-chain exposure, or insider threat. It does not investigate; it assigns investigation scope.

**Parent Agents** receive one vector and think metacognitively: what are the blind spots? What sub-problems need specialized attention? Each parent spawns exactly 2 child agents with specific personas and objectives.

**Child Agents** receive one sub-problem and perform granular investigation. They output a `DecisionMemo` with: `strategy`, `risks`, `assumptions`, `second_order_effects`, `evidence_needs`, and a `confidence` label. The `evidence_needs` field is the critical one — it must name concrete telemetry, logs, CVE feeds, or incident-report facts, not vague descriptions.

## Policy Priors

Before agents run, `evolution.py` runs a steady-state island EA over their configurations. Each agent gets an `AgentPolicy` with 8 trait values (evidence_weight, causal_focus, temporal_awareness, etc.) that are rendered into its prompt as a compact context string:

```
policy_id=parent.network_forensics.a1b2;
prioritize causal focus, evidence weight;
top_traits=causal_focus=0.86, evidence_weight=0.84
```

This steers the agent toward more evidence-focused, causal-chain-oriented investigation without changing what it investigates.

## Failure Handling

If any child agent fails (content filter, timeout, exception), `_fallback_memo()` returns a memo with `strategy: "[UNAVAILABLE - reason]"` and `confidence: "Low"`. A single child failure cannot crash the pipeline.

## How This Changes with Memory Layer

The orchestrator will receive a `memory_context` field in `GraphState` — a text string from `memory_retrieve_node` summarizing the 3 most similar past runs. The orchestrator prompt is extended to use this context before decomposing the incident.

Memory context is prompt text only. It is never passed as `EvidenceRecord` objects. Past runs inform reasoning, not data.

## Related Notes

- [[agents/01-orchestrator|Orchestrator]] — grand_orchestrator_node prompt and output
- [[agents/02-evolution|Evolution]] — how policy priors are computed
- [[agents/03-evaluator|Evaluator]] — what ranks the DecisionMemos
- [[pipeline/03-graphstate|GraphState]] — where all agent outputs accumulate

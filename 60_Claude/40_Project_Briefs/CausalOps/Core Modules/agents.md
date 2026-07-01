---
tags: [causalops, agents, langgraph, llm, orchestrator]
aliases: [agents.py]
---

# agents.py — Hierarchical Agent Nodes

`src/agents.py` implements the three LangGraph nodes that use the LLM: the grand orchestrator, parent agents, and child agents. **This is the only place where LLM calls produce structured agent artifacts.** The module does not touch evidence records or estimator outputs.

## LLM Configuration

```python
llm = get_llm(temperature=0.4)        # orchestrator + parent agents
low_temp_llm = get_llm(temperature=0.0)  # child agents (deterministic memos)
```

LLM is Gemini via `src/llm.py`. Uses `with_structured_output()` for typed extraction.

## Grand Orchestrator

**Produces:** `list[AgentConfig]` — 2-3 parent investigation tracks

**Prompt role:** "You are the Grand Orchestrator for HiveMind SOC operations. Decompose the incident into 2-3 distinct investigatory vectors such as geopolitical context, network forensics, identity risk, supply-chain exposure, or insider threat."

**Output model:**
```python
class ParentConfigsOutput(BaseModel):
    parent_configs: list[AgentConfig]
```

**Returns to GraphState:** `{"parent_configs": result.parent_configs}`

**Side effects:** Publishes one `AGENT_CONFIG` spawn event per parent config to Kafka.

## Parent Agent

**Produces:** `list[ChildConfig]` — 2 specialized child tasks per parent

**Prompt role:** "You are a {persona} Parent Agent investigating a major SOC incident. Your objective is: {focus_objective}. Analyze the incident metacognitively, name blind spots, and spawn 2 specialized Child Agents."

**Policy context injection:** The evolved `AgentPolicy` is rendered into a compact prompt string showing top traits and objective hint:
```python
"policy_id=parent.network_forensics.a1b2; prioritize causal focus, evidence weight; top_traits=causal_focus=0.86, evidence_weight=0.84"
```

**Returns to GraphState:** `{"child_configs": result.child_configs}` — accumulated via `operator.add` reducer.

**Side effects:** Publishes one `CHILD_CONFIG` spawn event per child config.

## Child Agent

**Produces:** One `DecisionMemo` per child

**Prompt role:** "You are a {persona} Child Agent responding to a {parent_persona}. Your objective: {focus_objective}. Perform a granular incident investigation and output a structured DecisionMemo. Include explicit assumptions, risks, second_order_effects, evidence_needs, and a confidence label."

**Key constraint on `evidence_needs`:** Must name concrete telemetry, logs, CVE feeds, incident-report facts, or analyst observations that would confirm or falsify the strategy — not vague descriptions.

**Failure handling:** `_fallback_memo()` is returned when:
- Azure content filter blocks the request (`ContentFilterFinishReasonError`)
- Any unexpected exception occurs

Fallback memos have `strategy: "[UNAVAILABLE - reason]"` and `confidence: "Low"`. This prevents a single child failure from crashing the entire pipeline.

**Returns to GraphState:** `{"memos": [memo]}` — accumulated via `operator.add` reducer.

**Side effects:** Publishes `DECISION_MEMO` artifact to Kafka.

## Policy Context Rendering

```python
def _policy_context(policy: Any) -> str:
    # Renders top 4 traits by value into a compact string
    # Falls back to "No evolved policy prior; use the stated objective."
    top_traits = sorted(traits.items(), key=lambda item: item[1], reverse=True)[:4]
    top_text = ", ".join(f"{name}={value:.2f}" for name, value in top_traits)
    return f"policy_id={policy_id}; prioritize {priority}; top_traits={top_text}."
```

## Bus Publishing

Every node publishes telemetry at start and end:
```python
publish_telemetry(agent_id="orchestrator", tier="orchestrator", phase="ORCHESTRATOR", message="...", status="running")
```

And publishes artifacts (configs, memos) to Kafka for SSE streaming to the frontend.

## Related Notes

- [[schema]] — AgentConfig, ChildConfig, DecisionMemo definitions
- [[evolution]] — How AgentPolicy is attached to configs before agents run
- [[GraphState Contract]] — The TypedDicts agents read from and write to
- [[evaluator]] — Consumes the memos produced here
- [[Kafka Bus Overview]] — What gets published and on which topics

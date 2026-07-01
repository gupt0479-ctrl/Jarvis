# C09 — Agent Nodes (Parent, Child, Orchestrator)

**Community 9** — 23 nodes, cohesion 0.14

The LLM-facing agent node functions: parent agent, child agent, and output models. The grand orchestrator is in Community 19 (graph.py topology).

## Key Nodes

`child_agent_node()`, `ChildConfigsOutput`, `_fallback_memo()`, `memo_to_text()`, `parent_agent_node()`, `ParentConfigsOutput`, `_policy_context()`

## What This Code Does

**`parent_agent_node`**: Takes a `ParentState` (persona + objective + policy), calls LLM with `temperature=0.4`, returns `{"child_configs": list[ChildConfig]}`. Publishes `CHILD_CONFIG` spawn events.

**`child_agent_node`**: Takes a `ChildState`, calls LLM with `temperature=0.0`, returns `{"memos": [DecisionMemo]}`. Publishes `DECISION_MEMO` artifact. Falls back to `_fallback_memo()` on any exception.

**`_policy_context`**: Renders an `AgentPolicy` into a compact prompt string showing the top 4 traits by value.

**`memo_to_text`**: Serializes a `DecisionMemo` to a compact string for prompt injection (used by evaluator).

## Source File

`src/agents.py`

## Related Notes

- [[agents/00-agent-hierarchy|Agent Hierarchy]] — how these nodes fit the tier structure
- [[agents/01-orchestrator|Orchestrator]] — grand_orchestrator_node (Community 19)

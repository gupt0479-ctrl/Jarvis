# Evaluator

`src/evaluator.py` ranks all `DecisionMemo` objects from child agents and synthesizes a final recommendation. It is the last LLM call before the causal pipeline begins.

## Role in Pipeline

Evaluator sits between child agent output and causal synthesis:
```
Child Agents → [all memos accumulated] → Evaluator → Causal Architect
```

The causal architect uses the top-ranked strategy to guide which DAG variables and edges to prioritize.

## What It Does

1. Receives all accumulated `memos` from `GraphState`
2. Analyzes the task description to infer implicit priorities (incident containment? root-cause? compliance?)
3. Scores each memo on 4 dimensions
4. Ranks perspectives best to worst
5. Synthesizes a final recommendation
6. Writes `ranked_strategies` and `final_recommendation` to GraphState

## Scoring: EvaluationScore

```python
class EvaluationScore(BaseModel):
    relevance: float               # 0.0–1.0 relevance to the task
    reasoning: float               # 0.0–1.0 quality of the reasoning chain
    constraint_satisfaction: float # 0.0–1.0 satisfaction of scenario constraints
    overall_score: float           # 0.0–1.0 composed score
```

## Output Models

```python
class MemoEvaluation(BaseModel):
    perspective: str
    score: EvaluationScore
    feedback: str                  # brief per-memo feedback

class RankedStrategies(BaseModel):
    evaluations: list[MemoEvaluation]
    ranked_perspectives: list[str]       # best to worst
    final_recommendation: str            # synthesized top-level recommendation
```

## Dynamic Prompt Design

The evaluator does not use a fixed scoring rubric. It first analyzes the task to determine implicit priorities, then scores memos against those inferred priorities. This means the same memo might rank differently across different incident types.

## LLM Config

Uses `temperature=0.4` (same as orchestrator/parents). Structured output via `llm.with_structured_output(RankedStrategies)`.

## GraphState Writes

```python
return {
    "ranked_strategies": [...],    # list[MemoEvaluation] dicts
    "final_recommendation": "...",
    "evaluator_error": None,       # or error string if evaluation failed
}
```

## Bus Publishing

Publishes `RANKED_STRATEGIES` artifact to `hivemind.artifacts` for SSE streaming and frontend display.

## Related Notes

- [[agents/00-agent-hierarchy|Agent Hierarchy]] — the memos that feed this node
- [[causal-engine/00-overview|Causal Engine]] — the ranked output feeds causal_synthesis_node
- [[pipeline/03-graphstate|GraphState]] — `ranked_strategies` and `final_recommendation` fields

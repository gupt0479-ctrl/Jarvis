---
type: project
status: sprout
created: 2026-07-01
tags: [causalops, evaluator, ranking, llm]
aliases: [evaluator.py]
---

# evaluator.py — Adaptive Memo Evaluator

`src/evaluator.py` ranks the `DecisionMemo` objects produced by child agents and synthesizes a final recommendation. It uses an LLM with `temperature=0.4` and structured output.

## What It Does

1. Receives all accumulated `memos` from `GraphState`
2. Analyzes the task to infer implicit priorities
3. Scores each memo on 4 dimensions
4. Ranks perspectives from best to worst
5. Synthesizes a final recommendation
6. Writes results to `ranked_strategies` and `final_recommendation`

## Scoring Dimensions (EvaluationScore)

```python
class EvaluationScore(BaseModel):
    relevance: float               # 0.0–1.0 relevance to the task
    reasoning: float               # 0.0–1.0 reasoning quality
    constraint_satisfaction: float # 0.0–1.0 satisfaction of scenario constraints
    overall_score: float           # 0.0–1.0 composed score
```

## Output Models

```python
class MemoEvaluation(BaseModel):
    perspective: str
    score: EvaluationScore
    feedback: str  # brief feedback on the memo

class RankedStrategies(BaseModel):
    evaluations: list[MemoEvaluation]
    ranked_perspectives: list[str]      # best to worst
    final_recommendation: str           # synthesized top-level recommendation
```

## Prompt Design (DYNAMIC_EVALUATOR_PROMPT)

The evaluator prompt is task-adaptive:
1. Analyzes the original task to determine implicit priorities
2. Scores each memo against those inferred priorities (not a fixed rubric)
3. Produces a final recommendation grounded in the highest-scoring strategies

This means the scoring criteria adapt to whether the task is about incident containment, root-cause analysis, compliance reporting, etc.

## What Gets Written to GraphState

```python
return {
    "ranked_strategies": [...],      # list of MemoEvaluation dicts
    "final_recommendation": "...",   # synthesized recommendation text
    "evaluator_error": None,         # or error string if evaluation failed
}
```

## Role in the Pipeline

The evaluator output becomes input to the causal architect in `causal.py`:
```python
# causal_synthesis_node uses:
evaluator_text = str(ranked[-1] if ranked else {})  # highest-ranked strategy
```

The causal architect uses the final recommendation to guide which variables and edges to prioritize in the DAG.

## Bus Publishing

Publishes `RANKED_STRATEGIES` artifact to Kafka for SSE streaming and frontend display.

## Related Notes

- [[agents]] — Produces the memos that evaluator ranks
- [[causal]] — Consumes evaluator output for DAG generation
- [[schema]] — DecisionMemo model that feeds into evaluator
- [[benchmarking]] — Separately scores this tier's output quality

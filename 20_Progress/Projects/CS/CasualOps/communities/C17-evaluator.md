# C17 — Memo Evaluator

**Community 17** — 17 nodes, cohesion 0.12

The adaptive memo evaluator: task-inferred scoring criteria, 4-dimension scoring, final recommendation synthesis.

## Key Nodes

`evaluate_memos_node()`, `EvaluationScore`, `_memo_value()`, `MemoEvaluation`, `RankedStrategies`

## What This Code Does

`evaluate_memos_node()` calls LLM with `temperature=0.4` and structured output. First analyzes the task to infer implicit priorities, then scores each memo on relevance, reasoning, constraint_satisfaction, overall_score. Returns `ranked_strategies` and `final_recommendation` to GraphState.

`_memo_value()` serializes a memo's content into a string for prompt injection.

## Source File

`src/evaluator.py`

## Related Notes

- [[agents/03-evaluator|Evaluator]] — full description

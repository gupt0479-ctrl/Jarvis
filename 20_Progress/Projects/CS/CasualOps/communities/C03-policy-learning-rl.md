# C03 — Policy Learning / RL

**Community 3** — 32 nodes, cohesion 0.18

KG-grounded model-based RL and bidirectional meta-learning. Runs at the end of every completed run.

## Key Nodes

`_actions()`, `_bidirectional_meta_learning()`, `build_policy_optimization_report()`, `_causal_reward()`, `_clamp()`, `_confidence_score()`, `_evaluation_scores()`

## What This Code Does

Computes global rewards from evaluator scores, causal estimate quality, and reasoning anomalies. Runs Bellman value iteration (12 steps, discount 0.82) over the 5D KG topology to produce Q-values per policy state. Outputs greedy policy, Stackelberg response (leader/follower game), and bidirectional meta-learning update (top-down push + bottom-up aggregate).

## Source File

`src/policy_learning.py`

## Related Notes

- [[agents/02-evolution|Evolution]] — island EA that produces the policy priors updated by RL
- [[pipeline/02-coordinator|Coordinator]] — `_run_policy_learning` phase

---
tags: [causalops, rl, policy, meta-learning, q-values, stackelberg]
aliases: [policy_learning.py]
---

# policy_learning.py — KG-Grounded RL & Meta-Learning

`src/policy_learning.py` runs at the end of every completed run. It builds a model-based RL report from the run's outputs and the 5D KG snapshot, then publishes the report as a Kafka artifact and stores it in the run artifact.

## Inputs

- `state: dict[str, Any]` — the full GraphState at run completion
- `kg_snapshot: dict[str, Any]` — the 5D KG nodes/edges for this run

## Core Function: build_policy_optimization_report()

Produces a report containing:

### Global Rewards
Computed from evaluator scores, causal estimate quality, reasoning anomalies:
- Evaluator score average over child memos
- Estimate strength (normalized ATE * refutation signal)
- Anomaly penalty (subtract for unexplained anomalies)

### KG Transition Weights
Edge confidence values from the 5D KG become transition weights in the MDP model.

### Value Iteration Q-Values
```python
DISCOUNT = 0.82
VALUE_ITERATIONS = 12
```
Runs Bellman value iteration over the KG topology for `VALUE_ITERATIONS` steps to produce Q-values per policy state.

### Greedy Policy
The policy with the highest Q-value per state.

### Stackelberg Response
A leader/follower game-theoretic response between the greedy policy (leader) and a simulated adversary (follower). Models adversarial adaptation.

### Bidirectional Meta-Learning
Two-direction update:
1. **Top-down push:** Shared meta-prior from best policies is pushed down into child policy shards
2. **Bottom-up aggregate:** Local delta updates from each child shard are aggregated back into an updated meta-prior

This enables future runs to start island populations from learned priors (currently within-run only; cross-run persistence is roadmap).

## Output

```json
{
  "global_rewards": {...},
  "value_iteration": {
    "q_values": {...},
    "iterations": 12,
    "discount": 0.82
  },
  "greedy_policy": {...},
  "stackelberg_response": {...},
  "meta_learning": {
    "meta_prior": {...},
    "child_shards": [...],      // N updated per-child policies
    "aggregation_delta": {...}
  }
}
```

Published as `POLICY_OPTIMIZATION_REPORT` on `hivemind.artifacts`.

## Trait Names

```python
from evolution import TRAIT_NAMES  # same 8 traits as island EA
```

The RL loop updates the same trait dimensions that the island EA evolves, creating a consistent policy vocabulary across the run lifecycle.

## Current Limitation

Policy priors are **within-run only**. Cross-run persistence (seeding future island populations from learned priors) is listed in the roadmap as "Persistent cross-run policy memory."

## Related Notes

- [[evolution]] — Island EA that produces initial policy priors (same trait space)
- [[reasoning]] — Provides anomaly data for global reward computation
- [[estimators]] — Provides estimate quality for reward signal
- [[graph_5d]] — Provides KG snapshot for transition weights
- [[Coordinator Execution Model]] — `_run_policy_learning` phase

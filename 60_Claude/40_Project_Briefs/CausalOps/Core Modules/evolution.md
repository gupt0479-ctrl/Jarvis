---
type: project
status: sprout
created: 2026-07-01
tags: [causalops, evolution, genetic-algorithm, policy, ea]
aliases: [evolution.py]
---

# evolution.py — Steady-State Island Evolution

`src/evolution.py` runs a deterministic evolutionary algorithm over agent *policy traits* before each agent tier is dispatched. It does not modify incident descriptions, evidence records, or strategies — it evolves compact behavioral priors that are injected into agent prompts.

## 8 Policy Traits (TRAIT_NAMES)

```python
TRAIT_NAMES = (
    "evidence_weight",      # how strongly to weight telemetry/logs
    "causal_focus",         # emphasis on causal chain and DAG design
    "temporal_awareness",   # sensitivity to event ordering and time
    "exploration",          # willingness to investigate novel angles
    "exploitation",         # focus on well-known patterns
    "risk_aversion",        # conservatism in containment recommendations
    "coordination",         # coordination with other agents
    "resource_budget",      # efficiency vs thoroughness trade-off
)
```

Each trait is a float in [0, 1].

## Algorithm: Steady-State Island EA

```
Initialization:
  - island_count: 3 (default, bounded 1-6)
  - population_per_config: 3 per agent config per island
  - generations: 8 (default, bounded 2-40)
  - migration_interval: 3 (every N generations, migrate best individual to next island)

Per generation:
  - tournament selection (size 3) → pick 2 parents
  - crossover: per-trait, each trait from parent A (35%), parent B (35%), or average (30%)
  - bounded mutation: each trait has 72% chance of being perturbed by ±mutation_rate
  - steady-state replacement: worst individual for that config_index is replaced

Migration:
  - Best genome per island migrates to the next island (ring topology)
  - Replaces worst genome of that config_index in destination
  - Only if migrant has higher fitness than the worst
```

## Fitness Function

```python
fitness = (
    0.28 * overlap            # Jaccard overlap of agent tokens vs task tokens
  + 0.22 * specificity        # how many distinct tokens in persona+objective
  + 0.14 * evidence_alignment # overlap with evidence-domain terms (siem, edr, cve, logs...)
  + 0.28 * trait_balance      # 1 - mean absolute deviation from ideal trait vector
  + 0.08 * coordination_bonus # (coordination + causal_focus) / 2
)
```

## Task-Adaptive Ideal Traits

The ideal trait vector is derived from the task description:
```python
ideal = {
    "evidence_weight": 0.72,  # always high (default)
    "causal_focus": 0.72,     # always high (default)
    ...
}
# Adjusted if task mentions:
# "kafka", "stream", "real-time" → temporal_awareness=0.84, coordination=0.76
# "causal", "graph", "dag" → causal_focus=0.86
# "uncertain", "novel" → exploration=0.72
# "contain", "incident", "breach" → risk_aversion=0.74
```

## Seed Traits

Initial traits are seeded deterministically from `sha256(seed_key)` — same task + same agent persona always produces the same initial genome. This makes runs reproducible.

## Outputs

### `evolve_parent_configs(state, configs)` → `(list[AgentConfig], report_dict)`
Attaches an `AgentPolicy` to each `AgentConfig`. The policy carries `policy_id`, `traits`, `fitness`, and `lineage`.

### `evolve_child_configs(state, configs)` → `(list[ChildConfig], report_dict)`
Same but for child configs.

### Evolution Report
```json
{
  "algorithm": "steady_state_island_evolution",
  "tier": "parent",
  "island_count": 3,
  "generations": 8,
  "best_fitness": 0.742,
  "selected_policies": [...],
  "islands": [
    {"island_id": "parent-island-1", "best_fitness": 0.71, "mean_fitness": 0.63},
    ...
  ]
}
```

Published to Kafka as `AGENT_EVOLUTION_REPORT` and merged into `agent_evolution_report` in `GraphState`.

## What Evolution Does NOT Do

- Does not modify the task description
- Does not generate evidence
- Does not rewrite objectives
- Does not affect the causal DAG or estimator

Evolution is a prior-tuning mechanism, not a content generator.

## Related Notes

- [[agents]] — Where evolved policies are consumed as prompt context
- [[policy_learning]] — Post-run RL that could seed future island populations
- [[schema]] — AgentPolicy model definition
- [[Coordinator Execution Model]] — Where evolution fits in the execution sequence

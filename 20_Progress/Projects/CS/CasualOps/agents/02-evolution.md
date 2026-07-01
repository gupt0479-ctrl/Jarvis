# Island Evolution

`src/evolution.py` runs a steady-state island evolutionary algorithm over agent *policy traits* before each agent tier is dispatched. It does not modify incident descriptions, evidence, or strategies — it evolves compact behavioral priors injected into agent prompts.

## 8 Policy Traits

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

All traits are floats in `[0, 1]`.

## Algorithm: Steady-State Island EA

```
Configuration:
  island_count: 3 (default, bounded 1-6)
  population_per_config: 3 per agent config per island
  generations: 8 (default, bounded 2-40)
  migration_interval: 3 (migrate best individual every N generations)

Per generation:
  1. Tournament selection (size 3) → pick 2 parents
  2. Crossover: each trait from parent A (35%), parent B (35%), or average (30%)
  3. Bounded mutation: each trait has 72% chance of ±mutation_rate perturbation
  4. Steady-state replacement: worst individual for that config_index is replaced

Migration (ring topology):
  Best genome per island → next island
  Replaces worst genome of that config_index in destination
  Only if migrant fitness > worst's fitness
```

## Fitness Function

```python
fitness = (
    0.28 * overlap            # Jaccard overlap of agent tokens vs task tokens
  + 0.22 * specificity        # distinct tokens in persona + objective
  + 0.14 * evidence_alignment # overlap with evidence-domain terms (siem, edr, cve, logs...)
  + 0.28 * trait_balance      # 1 - mean absolute deviation from ideal trait vector
  + 0.08 * coordination_bonus # (coordination + causal_focus) / 2
)
```

## Task-Adaptive Ideal Traits

The ideal trait vector shifts based on task description keywords:

| Keyword trigger | Trait boosted |
|-----------------|---------------|
| "kafka", "stream", "real-time" | temporal_awareness=0.84, coordination=0.76 |
| "causal", "graph", "dag" | causal_focus=0.86 |
| "uncertain", "novel" | exploration=0.72 |
| "contain", "incident", "breach" | risk_aversion=0.74 |

## Seed Traits (Reproducibility)

Initial traits seeded from `sha256(seed_key)` where seed_key includes the task description and agent persona. Same task + same persona always produces the same initial genome.

## Outputs

```python
evolve_parent_configs(state, configs) → (list[AgentConfig], report_dict)
evolve_child_configs(state, configs)  → (list[ChildConfig], report_dict)
```

Each returned `AgentConfig` has an `AgentPolicy` attached with `policy_id`, `traits`, `fitness`, and `lineage` (last 5 ancestors).

Evolution report published as `AGENT_EVOLUTION_REPORT` to `hivemind.artifacts` and stored in `GraphState.agent_evolution_report`.

## What Evolution Does NOT Do

- Does not modify task description, evidence records, or causal DAG
- Does not generate content — only steers existing prompts
- Does not affect estimator or discovery

## Related Notes

- [[agents/01-orchestrator|Orchestrator]] — consumes evolved AgentPolicy via prompt injection
- [[agents/00-agent-hierarchy|Agent Hierarchy]] — where evolution fits in the pipeline
- [[pipeline/02-coordinator|Coordinator]] — `_run_parent_evolution` and `_run_child_evolution` phases

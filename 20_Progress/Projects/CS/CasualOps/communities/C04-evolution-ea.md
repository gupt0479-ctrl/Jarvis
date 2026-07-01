# C04 — Island Evolutionary Algorithm

**Community 4** — 30 nodes, cohesion 0.16

Steady-state island EA over agent policy traits. Runs before parent and child dispatch.

## Key Nodes

`ConfigT`, `_agent_ref()`, `_bounded_int()`, `_clamp()`, `_empty_report()`, `evolve_child_configs()`, `_evolve_configs()`, `evolve_parent_configs()`

## What This Code Does

`_evolve_configs()` is the core loop: tournament selection, crossover (35%/35%/30% per trait), bounded mutation (72% per-trait probability), steady-state replacement. Runs 3 islands × 8 generations. `_bounded_int()` constrains hyperparameters to valid ranges.

## Source File

`src/evolution.py`

## Related Notes

- [[agents/02-evolution|Evolution]] — full algorithm with fitness formula

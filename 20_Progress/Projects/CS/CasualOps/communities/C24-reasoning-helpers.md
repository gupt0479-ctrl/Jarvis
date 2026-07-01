# C24 — Reasoning + bind_from_state

**Community 24** — 11 nodes, cohesion 0.24

Deterministic reasoning layer functions and the `bind_from_state` helper used throughout the codebase.

## Key Nodes

`bind_from_state()`, `_asset_table()`, `build_reasoning_report()`, `Coordinator node: reason over the run's validated causal model.`

## What This Code Does

`bind_from_state()` is a cross-community bridge: every agent node calls it to bind run_id/correlation_id for Kafka telemetry. It appears in Community 24 because of its co-occurrence with reasoning functions.

`build_reasoning_report()` takes the validated causal graph, estimate report, and evidence records and produces: anomalies per asset, zone summary, ranked recommendations.

`_asset_table()` formats the asset anomaly data for the reasoning report output.

## Source Files

`src/reasoning.py`, `src/bus/helpers.py`

## Related Notes

- [[causal-engine/04-reasoning|Reasoning]] — full description
- [[event-bus/00-topics|Kafka Topics]] — bind_from_state connects agents to bus context

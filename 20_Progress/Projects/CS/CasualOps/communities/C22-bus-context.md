# C22 — Bus Publish Context

**Community 22** — 9 nodes, cohesion 0.16

Per-run Kafka publish context: sequence counters, run_id/correlation_id binding, and artifact count tracking.

## Key Nodes

`get_run_summary()`, `RunPublishContext`, `Counts semantic artifacts published during one run.`, `Increment counters for a published artifact type.`

## Source File

`src/bus/context.py`

## Related Notes

- [[event-bus/00-topics|Kafka Topics]] — how context is used for telemetry correlation

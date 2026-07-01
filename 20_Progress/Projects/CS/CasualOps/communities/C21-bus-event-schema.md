# C21 — Bus Event Schema

**Community 21** — 10 nodes, cohesion 0.21

The canonical Kafka message schema: `ArtifactType` enum, topic routing, and telemetry consumer type annotation.

## Key Nodes

`ArtifactType`, `Event envelope schema and artifact type registry.`, `Semantic artifact kinds published on the HiveMind bus.`, `topic_for_artifact()`, `Kafka topic names and artifact routing.`, `Telemetry consumer for SSE streaming.`

## Source File

`src/bus/events.py`, `src/bus/topics.py`

## Related Notes

- [[event-bus/00-topics|Kafka Topics]] — full topic structure and ArtifactType enum listing

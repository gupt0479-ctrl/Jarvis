# C00 — Kafka/SSE Telemetry Consumers

**Community 0** — 67 nodes, cohesion 0.05

Kafka consumer infrastructure, SSE telemetry streaming, and bus context binding. The largest community in the graph — it captures the async plumbing that connects the coordinator to the frontend.

## Key Nodes

`AIOKafkaConsumer`, `stream_telemetry()`, `bind_run_context()`, `publish_dlq()`, `AbstractEventLoop`, `Event`

## What This Code Does

Streams `EXECUTION_PHASE` envelopes from `hivemind.telemetry` to connected SSE clients. Each `GET /run/{run_id}/events` request creates a unique consumer group with a filtered view of the telemetry topic for that specific run_id. The stream closes when it sees a COMPLETE or ERROR phase event.

Also handles the DLQ publisher (`publish_dlq`) used when spawn tasks exceed `HIVEMIND_SPAWN_MAX_RETRIES`.

## Source Files

`src/bus/` (producer.py, consumer.py, context.py), relevant pieces in `src/api.py` (stream_telemetry endpoint)

## Related Notes

- [[event-bus/00-topics|Kafka Topics]] — full topic structure and EventEnvelope schema
- [[infrastructure/01-api|API]] — GET /run/{run_id}/events endpoint

---
type: evergreen
status: seed
created: 2026-04-25
updated: 2026-04-25
tags:
  - evergreen
  - synthesis
concepts:
  - "[[Kafka Redis and Workers]]"
  - "[[40_Resources/CS/AI/MCPs]]"
tracks:
  - systems
  - ai
---

# Kafka Pipelines vs Agent Tool Orchestration

Both are about routing work through a sequence of specialized processors. The architecture patterns rhyme, even though the domains look different.

## The Structural Parallel

**Kafka pipeline** (BOOM):
- External stream (Kafka) → internal queue (Redis) → typed workers (alert, enrichment, filter) → output stream
- Each worker has a defined contract: what it reads, what it produces, what errors it can throw
- The scheduler orchestrates worker lifecycle: startup, heartbeat, shutdown

**Agent tool orchestration** (MCP):
- User request → planner (model decides which tools to call) → tool execution (MCP servers) → result aggregation → response
- Each tool has a defined contract: input schema, output format, error types
- The host orchestrates tool lifecycle: discovery, invocation, permission checking

## Where They Converge

- Both use typed contracts at boundaries (Rust traits in BOOM, JSON-RPC schemas in MCP)
- Both need error handling that doesn't cascade (a failed enrichment worker shouldn't crash the scheduler; a failed tool call shouldn't crash the agent)
- Both benefit from observability at handoff points (worker spans in BOOM, tool call logging in MCP)
- Both separate the "what to do" decision from the "how to do it" execution

## Where They Diverge

- Kafka pipelines are deterministic: the same input produces the same output (assuming fixed filter versions). Agent orchestration is non-deterministic: the model may choose different tools for the same request.
- Kafka workers process batches. MCP tools process single requests.
- Kafka pipelines are designed for throughput. Agent orchestration is designed for flexibility.

## Why This Matters

If you understand Kafka pipeline architecture, you already have the mental model for agent orchestration. The vocabulary changes (workers → tools, queues → tool calls, scheduler → planner), but the engineering concerns are the same: typed contracts, error isolation, observability at boundaries, and lifecycle management.

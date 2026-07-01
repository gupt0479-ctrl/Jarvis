---
tags: [causalops, roadmap, status, future]
---

# Roadmap & Status

## What's Implemented (as of 2026-07)

| Feature | Status | Notes |
|---------|--------|-------|
| Hierarchical LangGraph agents (orchestrator → parent → child) | ✅ Done | `agents.py` |
| Steady-state island evolution for policy priors | ✅ Done | `evolution.py` |
| Adaptive memo evaluator | ✅ Done | `evaluator.py` |
| Causal Hypothesis Architect (DAG + measurement plan) | ✅ Done | `causal.py` |
| PC-algorithm causal discovery + edge validation | ✅ Done | `causal_discovery.py` |
| Evidence compiler with statistical gates | ✅ Done | `dataset_compiler.py` |
| DoWhy + statsmodels estimation | ✅ Done | `estimators.py` |
| Evidence normalizers (Sentinel, CVE, incidents) | ✅ Done | `evidence_adapters.py` |
| Reasoning layer (anomaly detection + recommendations) | ✅ Done | `reasoning.py` |
| Model-based RL + Stackelberg + meta-learning | ✅ Done | `policy_learning.py` |
| 5D Spatiotemporal Knowledge Graph (SQLite) | ✅ Done | `graph_5d.py` |
| Phase 2b Coordinator (replacing graph.ainvoke) | ✅ Done | `coordinator/` |
| Kafka/Redpanda event bus with worker dispatch | ✅ Done | `bus/` + `worker/` |
| FastAPI with async SSE streaming | ✅ Done | `api.py` |
| React/TanStack frontend | ✅ Done | `app/` |
| Docker Compose full stack (api + worker + redpanda + frontend) | ✅ Done | `docker-compose.yml` |
| Deterministic smoke test (`/demo/estimate`) | ✅ Done | `demo_fixtures.py` |

## Immediate Priority: Memory Layer

| Component | Status | Blocker |
|-----------|--------|---------|
| `memory/embedder.py` | ❌ Waiting | Azure embedding deployment needed |
| `memory/extractor.py` | ❌ Waiting | Credentials needed |
| `memory/store.py` | ❌ Waiting | `SUPABASE_SERVICE_ROLE_KEY` needed |
| `memory/nodes.py` | ❌ Waiting | Above |
| `memory/mcp_server.py` | ❌ Waiting | Above |
| Supabase schema migration | ❌ Waiting | Tables: `memory_runs`, `memory_entities`, `memory_entity_edges` |
| LangGraph topology update | ❌ Waiting | After implementation |

→ See [[Memory Layer]] for full design doc.

## Near-Term Roadmap (from README)

- **Authenticated Microsoft Sentinel connector** — live tenant credentials, not just exports
- **Splunk HEC/search export connector**
- **NVD API puller** — scheduled CVE refresh
- **Larger benchmark suite** — golden incident prompts
- **Streaming execution telemetry** from LangGraph to React UI (SSE partially done)
- **Backtesting** against historical incident retrospectives
- **Persistent cross-run policy memory** — seed future island populations from past priors

## Future Enhancements (Architecture Vision)

### Production-Grade MCP Intelligence Fabric
Distributed MCP client layer for dynamic discovery, authentication, and routing across cyber-oriented MCP servers (threat intelligence, tool orchestration, policy enforcement, reasoning augmentation). Zero-trust, latency-aware intelligence plane.

### Deep Hierarchical Agent Expansion
Additional recursive child-agent layers with adaptive spawning policies driven by task complexity, uncertainty, and resource availability. Speculative parallel reasoning.

### Full Distributed Execution
- Horizontally scaled worker services (compose/k8s)
- Shared run state in Redis or Postgres (SQLite for local dev)
- Idempotency keys, retry policy, dead-letter topics
- Avro + Schema Registry for versioned envelopes
- S3/MinIO for large artifact storage
- In-flight run recovery after restarts
- Observability: consumer lag dashboards, DLQ alerting

### Online RL With Live Kafka Feedback
Extend run-level policy learning into a continuously running controller that updates Q-values as new KG events arrive.

### Federated Multi-Swarm Coordination
Independent agent clusters that exchange semantic state and negotiate objectives while preserving localized autonomy.

### Adaptive Trust & Reputation Layer
Reputation-driven trust framework for agents, tools, and MCP servers using latency, correctness, and semantic reliability metrics. Dynamic routing and circuit-breaking.

### Real-Time Causal Reasoning Infrastructure
Streaming causal inference engine capable of constructing and updating probabilistic causal models from live swarm telemetry.

## Related Notes

- [[_Index]] — Master index
- [[Memory Layer]] — Immediate priority implementation design
- [[System Overview]] — Current architecture

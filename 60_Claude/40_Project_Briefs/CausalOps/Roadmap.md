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

## Memory Layer — Complete (pending SQL migration + integration tests)

| Component | Status | Notes |
|-----------|--------|-------|
| `memory/embedder.py` | ✅ Done | Azure text-embedding-3-small, sync, 3-attempt backoff |
| `memory/extractor.py` | ✅ Done | Deterministic entity extraction, no LLM |
| `memory/store.py` | ✅ Done | SupabaseMemoryStore, 4 methods |
| `memory/nodes.py` | ✅ Done | memory_retrieve_node + memory_write_node (async) |
| `memory/mcp_server.py` | ✅ Done | Standalone FastMCP, port 8001, 4 tools |
| Coordinator phases wired | ✅ Done | memory_retrieve before orchestrator, memory_write after policy_learning |
| RunRecord serialization | ✅ Done | memory_context field added to schema + store |
| agents.py memory injection | ✅ Done | _format_memory_context() in orchestrator prompt |
| 10 unit tests (no creds) | ✅ Done | test_extractor.py + test_mcp_tools.py |
| Supabase project provisioned | ✅ Done | glbmdbwqmuttykhicasq |
| SQL migration | ⏳ Pending | Run on project glbmdbwqmuttykhicasq (SQL in [[Memory Layer Implementation Plan]]) |
| Integration tests | ⏳ Pending | Requires SUPABASE_SERVICE_ROLE_KEY + Azure embedding in .env |

→ See [[Memory Layer]] for current design and status.

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

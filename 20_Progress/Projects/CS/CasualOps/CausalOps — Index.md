---
type: project
status: active
created: 2026-07-02
updated: 2026-07-02
related_progress: []
tags:
  - causalops
  - index
next: "[[memory-layer]]"
---

# CausalOps — Index

CausalOps is an evidence-backed causal reasoning engine for cyber SOC operations. It converts an incident prompt into a structured investigation, proposes a causal DAG, compiles real SIEM/CVE/incident evidence, and only estimates intervention impact when statistical quality gates pass. If evidence is too weak, the ATE is withheld.

**The core design:** LLM proposes hypotheses. Deterministic code falsifies them. An LLM cannot inject data rows or steer which edges survive statistical tests.

## Current Phase

**Memory layer implementation — complete, pending SQL migration + integration tests.**

All `src/memory/` files written. Coordinator phases wired (memory_retrieve before orchestrator, memory_write after policy_learning). RunRecord serialization updated. 10 unit tests passing. Supabase project provisioned (glbmdbwqmuttykhicasq).

Remaining steps:
1. Run SQL migration on Supabase project glbmdbwqmuttykhicasq
2. Run `pytest tests/memory/ -m integration -v` with credentials in `.env`

## Subsystem Notes

- [[pipeline-coordinator]] — execution model, phase sequence, coordinator runner, LangGraph topology, GraphState contract
- [[agents]] — orchestrator, parent/child agents, island evolution, evaluator, memory context injection
- [[causal-engine]] — causal discovery (PC algorithm), evidence compiler, DoWhy estimation, reasoning layer
- [[event-bus]] — Kafka topics, EventEnvelope, spawn worker, SSE telemetry
- [[memory-layer]] — vector store, knowledge graph, temporal decay, MCP server, current status
- [[infrastructure]] -- Docker setup, API endpoints, environment variables

## Key Invariants

1. LLMs never generate estimator rows. `source_type: "synthetic"` records are skipped by the compiler.
2. ATE is withheld when data gates fail. `method = "withheld:data_quality_gates"` is correct behavior.
3. Memory context goes into the orchestrator prompt only -- never as `EvidenceRecord` objects.
4. `dataset_compiler.py` and `estimators.py` are statistical safeguards -- do not modify.
5. Never use Supabase anon key in Python backend. RLS silently blocks writes.
6. Never call `embed_text()` directly in async context -- wrap with `asyncio.to_thread`.

## Real Execution Path

`src/graph.py` is deprecated for execution (Phase 2b+). The real path is `src/coordinator/runner.py::execute_run()` -- an async state machine that persists phase state to SQLite between each phase.

Phase sequence:
```
memory_retrieve -> orchestrator -> parent_evolution -> parents (Kafka barrier)
  -> gather_children -> child_evolution -> children (Kafka barrier) -> evaluator
  -> causal_loop (synthesis + dowhy, retries) -> reasoner -> policy_learning
  -> memory_write -> completed
```

## Repo Path

`/home/anant_gupta/projects/hub/CausalOps/`

---
tags: [causalops, index, soc, causal-reasoning]
aliases: [CausalOps, CausalOps Index]
---

# CausalOps — Master Index

> **Core promise:** The LLM proposes hypotheses. Evidence decides whether an ATE is allowed to exist.

CausalOps is an evidence-backed causal reasoning engine for cyber SOC operations. It turns a messy incident prompt into a structured investigation, proposes a causal DAG, compiles real SIEM/CVE/incident evidence, and only estimates intervention impact when statistical quality gates pass. If evidence is too weak, the ATE is withheld — by design.

**Tech stack:** Python 3.12, FastAPI, LangGraph, Pydantic v2, DoWhy, statsmodels, Redpanda (Kafka), SQLite, React/TanStack/Vite.

**LLM:** Gemini 2.5 Flash (default) / Gemini 2.5 Pro (high-reasoning). Configured via `GEMINI_API_KEY`.

---

## Architecture

- [[System Overview]] — What CausalOps is, how the layers fit together
- [[LangGraph Pipeline]] — Original LangGraph graph topology (reference)
- [[Coordinator Execution Model]] — Phase 2b coordinator replacing `graph.ainvoke`
- [[GraphState Contract]] — The master TypedDict shared across all nodes
- [[Design Philosophy]] — Why LLM proposes and deterministic code falsifies

---

## Core Modules

| Module | Role |
|--------|------|
| [[schema]] | All Pydantic models + GraphState TypedDict |
| [[agents]] | Orchestrator, parent, child agent nodes |
| [[evaluator]] | Adaptive memo ranking |
| [[evolution]] | Steady-state island EA for policy priors |
| [[causal]] | Causal synthesis + DoWhy engine nodes |
| [[causal_discovery]] | PC-style DAG validation from evidence data |
| [[dataset_compiler]] | Evidence → DataFrame (DO NOT TOUCH) |
| [[estimators]] | DoWhy + statsmodels (DO NOT TOUCH) |
| [[evidence_adapters]] | Sentinel/CVE/incident normalizers |
| [[benchmarking]] | Deterministic tier scoring |
| [[engine]] | `run_causalops()` + artifact persistence |
| [[api]] | FastAPI routes |
| [[reasoning]] | Anomaly detection + zone pressure + recommendations |
| [[policy_learning]] | KG-grounded RL, Q-values, meta-learning |
| [[graph_5d]] | 5D Spatiotemporal Knowledge Graph (SQLite) |
| [[demo_fixtures]] | Deterministic smoke-test evidence |

---

## Event Bus & Coordinator

- [[Kafka Bus Overview]] — Redpanda topics, envelopes, telemetry flow
- [[Event Schema]] — `EventEnvelope`, `ArtifactType`, tier routing
- [[Coordinator Runner]] — Phase-by-phase async execution loop
- [[Run Store]] — SQLite-backed durable run state

---

## Infrastructure

- [[Docker Setup]] — Services: api, worker, redpanda, frontend
- [[API Reference]] — All endpoints with curl examples
- [[Environment Variables]] — Every env var, defaults, secrets

---

## Memory Layer (Complete — pending SQL migration + integration tests)

- [[Memory Layer]] — Current status and component overview
- [[Memory Layer Implementation Plan]] — Full schema SQL, implementation history, ADRs

---

## Roadmap

- [[Roadmap]] — What's implemented, what's blocked, future enhancements

---

## Claude Code Prompts

- [[Memory Layer Implementation Prompt]] — Ready-to-paste implementation prompt for Sonnet 4.6
- [[Token Efficiency Notes]] — How to run Claude Code sessions efficiently on this project

---

## Graphify

- [[What Graphify Does]] — What the tool is, the pipeline it runs, commands to use it
- [[How Notes Were Actually Written]] — Honest account: graphify was not used; notes were hand-written

---

## Key Invariants (Never Break These)

1. **LLMs never generate estimator rows.** `source_type: "synthetic"` records are skipped by the compiler.
2. **ATE is withheld when data gates fail.** `method = "withheld:data_quality_gates"` is correct behavior, not a bug.
3. **Never use Supabase anon key in Python backend.** RLS silently blocks writes.
4. **`dataset_compiler.py` and `estimators.py` are statistical safeguards — do not modify.**
5. **Memory context goes into the orchestrator prompt only — never as `EvidenceRecord` objects.**
6. **Never call `embed_text()` directly in async context** — wrap with `await asyncio.to_thread(embed_text, text)`.

# HiveMind Agent Guide

This file is the first stop for Codex, Cursor, Kiro, and other AI agents working
in this repository.

## Project Snapshot

HiveMind is an evidence-backed causal reasoning engine for cyber operations. It
takes an incident prompt, uses hierarchical LangGraph agents to produce decision
memos, synthesizes a measurable causal DAG, compiles real evidence records into
an estimator-ready dataset, and only returns a treatment effect when statistical
quality gates pass.

Core guardrail: LLMs may propose hypotheses, memos, causal graphs, and
measurement plans. LLMs must not invent estimator rows or treat generated
narrative as empirical evidence.

## Current Architecture

- Backend: Python, FastAPI, LangGraph, Pydantic, DoWhy, statsmodels.
- Frontend: React/TanStack/Vite app under `app/`.
- API boundary: `src/api.py`.
- LangGraph assembly: `src/graph.py`.
- Agent nodes: `src/agents.py`.
- Shared contracts: `src/schema.py`.
- Evidence compiler: `src/dataset_compiler.py`.
- Estimator: `src/estimators.py`.
- Evidence normalizers: `src/evidence_adapters.py`.
- Run orchestration and artifact persistence: `src/engine.py`.

## Source Of Truth

- `README.md` explains the product, architecture, and demo workflow.
- `Docs/` contains reviewed project workflow and context documents.
- `.kiro/` is reserved for Kiro's planning document set.
- `.cursor/` contains Cursor rules, skills, hooks, and project agent workflow.
  Global MCP servers (Obsidian, GitHub) live in `~/.cursor/mcp.json`.

When Kiro produces plan docs, Codex should read them carefully before changing
implementation. Codex is responsible for code correctness, architecture review,
and turning approved plans into clean changes.

## First Focus Area

Persistent Semantic Memory and Retrieval Layer:

- Hybrid long-term memory combining vector retrieval, graph traversal, and
  temporal indexing.
- Persistent contextual awareness across tasks.
- Longitudinal reasoning and adaptive learning.
- Future MCP bridge may expose memory, graph, threat intelligence, and tool
  orchestration to the agent swarm.

This feature is roadmap-level in the current repo. Treat it as architecture work
that must be designed against existing schemas, evidence provenance, graph state,
and artifact persistence.

## Working Rules

- Keep changes small, reviewed, and tied to the existing architecture.
- Preserve the evidence boundary between hypotheses and empirical records.
- Prefer typed Pydantic contracts and explicit state fields over loose dicts.
- Do not add hidden live integrations, credentials, background services, or
  automatic hooks without review.
- Do not write generated data, secrets, or run artifacts into Git.
- Do not change `.kiro/` unless the user asks for Kiro plan updates.
- Use `Docs/` for reviewed project documentation.

## Verification Commands

Backend and full stack:

```bash
docker-compose up --build
curl http://localhost:8000/health
curl http://localhost:8000/demo/estimate
docker-compose down
```

Frontend:

```bash
cd app && npm run lint
cd app && npm run build
cd app && npm run dev
cd app && npm run preview
```

## Git Workflow

Use the fork-first workflow documented in `Docs/GITHUB_WORKFLOW.md`.
Normal work goes to a branch on `origin`, then opens a PR into
`darshgarg7/HiveMind:main`.

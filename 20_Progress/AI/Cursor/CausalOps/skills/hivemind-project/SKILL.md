---
name: hivemind-project
description: Use when working in the HiveMind repo, reviewing its architecture, editing backend or frontend code, interpreting Kiro plans, or making changes that must preserve the evidence-backed causal reasoning guardrails.
---

# HiveMind Project Skill

## Start Here

1. Read `AGENTS.md`.
2. Read `Docs/PROJECT_CONTEXT.md`.
3. Read relevant Kiro docs in `.kiro/` if they exist for the task.
4. Inspect the code path before editing.

## Architecture Anchors

- `src/schema.py`: Pydantic contracts and LangGraph state.
- `src/graph.py`: LangGraph node wiring.
- `src/agents.py`: orchestrator, parent-agent, and child-agent nodes.
- `src/evaluator.py`: memo ranking.
- `src/causal.py`: causal DAG and estimator node bridge.
- `src/dataset_compiler.py`: evidence-to-dataframe compiler and data gates.
- `src/estimators.py`: DoWhy, statsmodels, and refuters.
- `src/api.py`: FastAPI surface.
- `app/src/lib/hivemind-api.ts`: frontend API client.

## Guardrails

- Do not let LLM-generated text become estimator data.
- Keep provenance visible for evidence, memory, and retrieved context.
- Prefer explicit schemas over loosely shaped dictionaries.
- Keep `data/`, `.env`, generated artifacts, and credentials out of Git.
- Do not add external services, MCP servers, or live hooks without review.

## Verification

Use the smallest relevant check:

```bash
docker-compose up --build
curl http://localhost:8000/health
curl http://localhost:8000/demo/estimate
cd app && npm run lint
cd app && npm run build
```

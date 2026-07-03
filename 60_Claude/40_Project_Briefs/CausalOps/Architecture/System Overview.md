---
type: project
status: sprout
created: 2026-07-01
tags:
  - brief
  - causalops
---
﻿---
tags: [causalops, architecture, overview]
---

# System Overview

## What It Is

CausalOps is a cyber SOC decision system that turns an incident prompt into a structured investigation and a **guarded causal estimate**. The key differentiator is not "the agent is confident" — it is that the agent can explain what evidence would be needed, compile that evidence, and **withhold statistical claims when data is too weak**.

## Pipeline Layers

| Layer | Component | Guardrail |
|-------|-----------|-----------|
| Decomposition | Grand Orchestrator | Standardized tier scoring |
| Policy evolution | Island EA | Steady-state replacement, bounded mutation |
| Investigation | Parent Agents → Child Agents | Explicit objectives per branch |
| Ranking | Evaluator | Structured scores and final recommendation |
| Hypothesis | Causal Architect | No dataset-row generation allowed |
| Validation | Causal Discovery (PC algorithm) | Independence tests on compiled data |
| Compilation | Evidence Compiler | Provenance, missingness, balance gates |
| Estimation | DoWhy + statsmodels | ATE withheld when data is weak |
| Reasoning | Reasoning Layer | Deterministic anomaly detection |
| Learning | RL + Meta-learning | KG-grounded value iteration |
| Streaming | 5D KG + Kafka | Temporal spatiotemporal event log |

## Data Flow (High Level)

```
Incident Prompt
  → Grand Orchestrator                   (LLM: decompose into 2-3 tracks)
    → Island Evolution (parent tier)     (deterministic EA: evolve policy priors)
      → Parent Agents (parallel)         (LLM: spawn child configs)
        → Island Evolution (child tier)  (deterministic EA: evolve child priors)
          → Child Agents (parallel)      (LLM: produce DecisionMemos)
            → Evaluator                  (LLM: rank memos)
              → Causal Architect         (LLM: design DAG + measurement plan)
                → Causal Discovery       (deterministic: validate DAG vs data)
                  → Evidence Compiler    (deterministic: normalize → dataframe)
                    → DoWhy Estimator    (deterministic: estimate ATE or withhold)
                      → Reasoning Layer  (deterministic: anomalies + recommendations)
                        → Policy RL      (deterministic: value iteration + meta-learning)
                          → Run Artifact (persisted JSON + 5D KG)
```

## Three Hard Boundaries

### 1. LLM → Evidence Boundary
Agent output is hypothesis context. Evidence enters only through normalized `EvidenceRecord` objects from real SIEM/CVE/incident exports. The compiler skips any record with `source_type: "synthetic"`.

### 2. Evidence → Estimator Boundary
The estimator receives only the compiled dataframe and the quality profile from `dataset_compiler.py`. It never receives raw text or agent narratives.

### 3. ATE Gate
Below 50 complete rows with valid treatment/control variation, ATE is withheld:
```json
{ "method": "withheld:data_quality_gates", "ate": null, "p_value": null }
```

## Services (Docker Compose)

| Service | Port | Role |
|---------|------|------|
| `api` | 8000 | FastAPI: coordinator + SSE, no spawn consumer |
| `worker` | — | Spawn consumer + graph stream consumer |
| `redpanda` | 19092 | Kafka-compatible event bus |
| `frontend` | 8080 | React/TanStack UI |

Shared state: `./data/` volume (runs.db + graph_5d.db + JSON artifacts).

## Related Notes

- [[Design Philosophy]] — Why this architecture exists
- [[Coordinator Execution Model]] — How the phases actually execute in Phase 2b
- [[LangGraph Pipeline]] — Original LangGraph topology (reference only)
- [[GraphState Contract]] — The shared state object

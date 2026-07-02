# Pipeline Overview

CausalOps converts an incident prompt into a guarded causal estimate through 10 sequential stages. The key claim: LLM proposes causal hypotheses, deterministic code decides whether a statistical effect is allowed to exist.

## The Three Hard Boundaries

These constraints define what CausalOps is. Violating any of them removes the epistemic value.

**Boundary 1 — LLM → Evidence.** Agent output is hypothesis context. Evidence enters only through `EvidenceRecord` objects from real SIEM/CVE/incident exports. The compiler skips any record with `source_type: "synthetic"`. An LLM cannot inject rows.

**Boundary 2 — Evidence → Estimator.** `dataset_compiler.py` receives only normalized evidence records and the graph structure. It never receives agent narratives, memos, or raw text as data. The estimator receives only the compiled dataframe and quality profile.

**Boundary 3 — ATE Gate.** Below 50 complete rows with valid treatment/control variation, ATE is withheld:
```json
{ "method": "withheld:data_quality_gates", "ate": null, "p_value": null }
```
This is correct behavior, not a failure.

## End-to-End Data Flow

```
Incident Prompt
  → [memory_retrieve]              planned: inject past context before orchestrator
  → Grand Orchestrator             LLM: decompose into 2-3 investigation tracks
    → Island Evolution (parents)   deterministic EA: evolve policy priors per track
      → Parent Agents (parallel)   LLM: spawn 2 child configs each
        → Island Evolution (children)  deterministic EA: evolve child priors
          → Child Agents (parallel)    LLM: produce DecisionMemos
            → Evaluator              LLM: rank memos, synthesize recommendation
              → Causal Architect     LLM: design DAG + measurement plan (no data rows)
                → Causal Discovery   deterministic: PC tests on compiled data
                  → Evidence Compiler  deterministic: normalize → dataframe
                    → DoWhy Estimator  deterministic: estimate ATE or withhold
                      → Reasoning Layer  deterministic: anomalies + recommendations
                        → Policy RL      deterministic: value iteration + meta-learning
                          → [memory_write]   planned: embed + store run in Supabase
                            → Run Artifact   persisted JSON + 5D KG
```

## Pipeline Layers Table

| Layer | Component | Source | Guardrail |
|-------|-----------|--------|-----------|
| Decomposition | Grand Orchestrator | `agents.py` | Tier scoring |
| Policy evolution | Island EA | `evolution.py` | Bounded mutation, steady-state |
| Investigation | Parent → Child Agents | `agents.py` | Explicit objectives per branch |
| Ranking | Evaluator | `evaluator.py` | Structured scores |
| Hypothesis | Causal Architect | `causal.py` | No dataset-row generation |
| Validation | Causal Discovery | `causal_discovery.py` | Independence tests |
| Compilation | Evidence Compiler | `dataset_compiler.py` | Provenance, missingness, balance |
| Estimation | DoWhy + statsmodels | `estimators.py` | ATE withheld when data is weak |
| Reasoning | Reasoning Layer | `reasoning.py` | Deterministic anomaly detection |
| Learning | RL + meta-learning | `policy_learning.py` | KG-grounded value iteration |

## Services (Docker Compose)

| Service | Port | Role |
|---------|------|------|
| `api` | 8000 | FastAPI: coordinator + SSE, no spawn consumer |
| `worker` | — | Spawn consumer + graph stream consumer |
| `redpanda` | 19092 | Kafka-compatible event bus |
| `frontend` | 8080 | React/TanStack UI |
| `mcp` | 8001 | Memory MCP server (planned) |

Shared state: `./data/` volume (runs.db + graph_5d.db + JSON artifacts).

## Related Notes

- [[pipeline/01-langgraph-topology|LangGraph Topology]] — original graph.py structure
- [[pipeline/02-coordinator|Coordinator]] — Phase 2b execution model
- [[pipeline/03-graphstate|GraphState]] — the shared state TypedDict
- [[causal-engine/00-overview|Causal Engine Overview]] — epistemic design in depth

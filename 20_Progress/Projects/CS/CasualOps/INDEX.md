# CausalOps — HiveMind Knowledge Base

Master index for the HiveMind causal reasoning engine. Repo: `/home/anant_gupta/projects/hub/CausalOps/`. Working directory for all Python source: `src/`.

## Graph Stats (graphify — 2026-07-01, commit `1ca0d2a7`)

- **687 nodes · 1700 edges · 33 communities**
- Extraction: 97% EXTRACTED · 3% INFERRED
- God nodes (most connected): `RunRecord` (48), `RunStore` (45), `ArtifactType` (32), `EventEnvelope` (28), `publish_telemetry()` (27), `run_hivemind()` (26), `GraphState` (24)
- Import cycle: `worker/__main__.py → worker/__main__.py` (self-loop, benign)
- Graph built from Python source only (`src/`). Doc files excluded (no LLM key).
- Refresh: `graphify update /home/anant_gupta/projects/hub/CausalOps/src` (no API cost)

See [[GRAPH_REPORT]] for full community breakdown and surprising connections.

## Thematic Notes

Reading order matches how the pipeline executes — start at `pipeline/` then drill into any subsystem.

### Pipeline
- [[pipeline/00-overview|00 — Overview]] — what HiveMind is, 3 hard boundaries, end-to-end data flow
- [[pipeline/01-langgraph-topology|01 — LangGraph Topology]] — graph.py node table, Send mechanics, refutation loop
- [[pipeline/02-coordinator|02 — Coordinator]] — Phase 2b executor, all phases, SQLite state, api/worker split
- [[pipeline/03-graphstate|03 — GraphState]] — TypedDict fields, reducer semantics, sub-state TypedDicts

### Agents
- [[agents/00-agent-hierarchy|00 — Agent Hierarchy]] — orchestrator→parent→child decision tree
- [[agents/01-orchestrator|01 — Orchestrator]] — grand_orchestrator_node, memory_context injection (planned)
- [[agents/02-evolution|02 — Evolution]] — island EA, 8 traits, fitness formula, task-adaptive ideal
- [[agents/03-evaluator|03 — Evaluator]] — memo ranking, EvaluationScore, final recommendation

### Causal Engine
- [[causal-engine/00-overview|00 — Overview]] — epistemic design: LLM proposes, deterministic code falsifies
- [[causal-engine/01-discovery|01 — Discovery]] — PC algorithm, EdgeVerdict statuses, MIN_ROWS_FOR_DISCOVERY
- [[causal-engine/02-evidence|02 — Evidence]] — EvidenceRecord, compiler gates, synthetic guard, compile flow
- [[causal-engine/03-estimation|03 — Estimation]] — DoWhy backdoor, statsmodels OLS, refuters, ATE withholding
- [[causal-engine/04-reasoning|04 — Reasoning]] — anomaly detection, zone pressure, recommendations

### Event Bus
- [[event-bus/00-topics|00 — Topics]] — 6 Redpanda topics, EventEnvelope, artifact→topic routing, DLQ
- [[event-bus/01-worker|01 — Worker]] — spawn consumer, retry backoff, barrier pattern, api/worker split

### Memory Layer
- [[memory-layer/00-design|00 — Design]] — 5 components, vector store + KG + MCP, why standalone
- [[memory-layer/01-status|01 — Status]] — what's blocked (credentials), what can be coded, test plan

### Infrastructure
- [[infrastructure/00-docker|00 — Docker]] — 4 services (+mcp planned), ports, volumes, SQLite journal mode
- [[infrastructure/01-api|01 — API]] — every endpoint grouped by purpose, request/response shapes
- [[infrastructure/02-env-vars|02 — Environment Variables]] — all env vars, secrets, never-commit list

## Graph Communities (auto-detected by graphify)

32 communities written (1 thin community with <3 nodes omitted). Labels assigned manually from node content. See [[GRAPH_REPORT]] for node lists and surprising cross-community connections.

| Community | Theme | Key nodes |
|-----------|-------|-----------|
| [[communities/C00-kafka-bus\|C00]] | Kafka/SSE telemetry consumers | `stream_telemetry`, `bind_run_context`, `publish_dlq` |
| [[communities/C01-5d-graph-ingestion\|C01]] | 5D KG ingestion | `ingest_causal`, `ingest_child`, `get_5d_graph` |
| [[communities/C02-evidence-normalizers\|C02]] | Evidence normalizers | `normalize_sentinel_export`, `normalize_cve_export` |
| [[communities/C03-policy-learning-rl\|C03]] | Policy learning / RL | `build_policy_optimization_report`, `_bidirectional_meta_learning` |
| [[communities/C04-evolution-ea\|C04]] | Island EA | `evolve_parent_configs`, `evolve_child_configs`, `_evolve_configs` |
| [[communities/C05-benchmarking\|C05]] | Tier scoring | `score_agent_tiers` |
| [[communities/C06-runstore-sqlite\|C06]] | RunStore SQLite methods | `Increment completed parent count`, `set_phase` |
| [[communities/C07-causal-discovery\|C07]] | PC algorithm discovery | `discover_and_validate`, `EdgeVerdict`, `apply_discovery` |
| [[communities/C08-spawn-commands\|C08]] | Spawn command builders | `build_parent_command`, `build_child_command` |
| [[communities/C09-agent-nodes\|C09]] | Agent nodes | `parent_agent_node`, `child_agent_node`, `_fallback_memo` |
| [[communities/C10-api-endpoints\|C10]] | API endpoints | `lifespan`, `get_run_5d_graph`, `health_check` |
| [[communities/C11-bus-publish\|C11]] | Bus publish functions | `publish_telemetry`, `publish_artifact`, `publish_spawn` |
| [[communities/C12-coordinator-barriers\|C12]] | Coordinator barrier waiting | `wait_for_barrier`, `enqueue_parent_tasks` |
| [[communities/C13-coordinator-phases\|C13]] | Coordinator phases | `execute_run`, `_backfill_5d_graph`, `_gather_children` |
| [[communities/C14-dataset-compiler\|C14]] | Dataset compiler | `compile_evidence_dataset`, `passes_estimation_gates`, `clean_variable` |
| [[communities/C15-engine-impact\|C15]] | Engine / impact | `_impact_confidence`, `_strategy_card`, `clear_run_context` |
| [[communities/C16-dowhy-estimator\|C16]] | DoWhy + statsmodels | `estimate_causal_effect`, `_build_gml`, `_linear_regression_stats` |
| [[communities/C17-evaluator\|C17]] | Memo evaluator | `evaluate_memos_node`, `EvaluationScore`, `RankedStrategies` |
| [[communities/C18-causal-nodes\|C18]] | Causal LangGraph nodes | `causal_synthesis_node`, `dowhy_engine_node` |
| [[communities/C19-langgraph-topology\|C19]] | LangGraph topology (deprecated) | `build_graph`, `grand_orchestrator_node`, `route_to_parents` |
| [[communities/C20-streamlit-demo\|C20]] | Streamlit demo (legacy) | `main`, `_default_incident` |
| [[communities/C21-bus-event-schema\|C21]] | Bus event schema | `ArtifactType`, `topic_for_artifact` |
| [[communities/C22-bus-context\|C22]] | Bus publish context | `RunPublishContext`, `get_run_summary` |
| [[communities/C23-demo-fixtures\|C23]] | Demo fixtures | `demo_causal_payload`, `patch_lateral_movement_evidence` |
| [[communities/C24-reasoning-helpers\|C24]] | Reasoning + bind_from_state | `build_reasoning_report`, `bind_from_state` |
| [[communities/C25-coordinator-state-machine\|C25]] | Coordinator state machine | RunStore singleton, `_record_from_json` |
| [[communities/C26-run-enqueue\|C26]] | Run enqueue | `enqueue_run`, `_execute_run_background`, `run_engine_sync` |
| [[communities/C27-runrecord-json\|C27]] | RunRecord JSON | `_record_to_json`, `apply_node_update` |
| [[communities/C28-graph-db\|C28]] | 5D graph DB connection | `connect_graph_db`, `graph_db_path` |
| [[communities/C29-refutation-logic\|C29]] | Refutation loop | `refutation_next_step`, `_run_causal_loop` |
| [[communities/C30-estimate-endpoint\|C30]] | Estimate endpoint | `estimate_from_evidence`, `EstimateRequest` |
| [[communities/C31-run-status\|C31]] | Run status + artifact | `get_run_status`, `load_run_artifact` |

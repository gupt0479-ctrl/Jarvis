# Graph Report - /home/anant_gupta/projects/hub/CausalOps/src  (2026-07-01)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 687 nodes · 1700 edges · 33 communities (32 shown, 1 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 47 edges (avg confidence: 0.51)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1ca0d2a7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]

## God Nodes (most connected - your core abstractions)
1. `RunRecord` - 48 edges
2. `RunStore` - 45 edges
3. `ArtifactType` - 32 edges
4. `EventEnvelope` - 28 edges
5. `publish_telemetry()` - 27 edges
6. `run_hivemind()` - 26 edges
7. `bind_from_state()` - 25 edges
8. `GraphState` - 24 edges
9. `publish_artifact()` - 22 edges
10. `execute_run()` - 21 edges

## Surprising Connections (you probably didn't know these)
- `ParentConfigsOutput` --uses--> `ArtifactType`  [INFERRED]
  agents.py → bus/events.py
- `ParentConfigsOutput` --uses--> `AgentConfig`  [INFERRED]
  agents.py → schema.py
- `ParentConfigsOutput` --uses--> `ChildConfig`  [INFERRED]
  agents.py → schema.py
- `ParentConfigsOutput` --uses--> `GraphState`  [INFERRED]
  agents.py → schema.py
- `ChildConfigsOutput` --uses--> `ArtifactType`  [INFERRED]
  agents.py → bus/events.py

## Import Cycles
- 1-file cycle: `worker/__main__.py -> worker/__main__.py`

## Communities (33 total, 1 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (67): AbstractEventLoop, AIOKafkaConsumer, Event, Yield telemetry envelopes for a single run_id.      Uses a unique consumer group, stream_telemetry(), bind_run_context(), Bind publish context for the current async task / thread., publish_dlq() (+59 more)

### Community 1 - "Community 1"
Cohesion: 0.11
Nodes (49): _derive_location(), _field(), get_5d_graph(), ingest_causal(), ingest_child(), ingest_evidence_record(), ingest_evolution_report(), ingest_findings() (+41 more)

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (32): normalize_cve_export(), normalize_incident_export(), normalize_sentinel_export(), NormalizeRequest, Request body for export-to-evidence normalization endpoints., Normalize Microsoft Sentinel or SIEM-like export rows., Normalize NVD/CVE feed rows into evidence records., Normalize incident-report export rows into evidence records. (+24 more)

### Community 3 - "Community 3"
Cohesion: 0.18
Nodes (32): _actions(), _bidirectional_meta_learning(), build_policy_optimization_report(), _causal_reward(), _clamp(), _confidence_score(), _evaluation_scores(), _field() (+24 more)

### Community 4 - "Community 4"
Cohesion: 0.16
Nodes (30): ConfigT, _agent_ref(), _bounded_int(), _clamp(), _empty_report(), evolve_child_configs(), _evolve_configs(), evolve_parent_configs() (+22 more)

### Community 5 - "Community 5"
Cohesion: 0.13
Nodes (28): _field(), _has_path(), _is_acyclic(), Any, Deterministic quality metrics for each HiveMind agent tier.  These metrics are n, Score whether parent agents produced complete child tasks., Score child memo output using bus count and a single memo sample., Score child-agent memo completeness. (+20 more)

### Community 6 - "Community 6"
Cohesion: 0.11
Nodes (14): Connection, Path, Persist coordinator run state in SQLite., Update run lifecycle status., Update run phase and persist., Increment completed parent count; return new total., Increment completed child count; return new total., Append child configs from a parent agent. (+6 more)

### Community 7 - "Community 7"
Cohesion: 0.14
Nodes (23): apply_discovery(), _binarize(), _conditional_test(), discover_and_validate(), DiscoveryReport, EdgeVerdict, estimation_edges(), _g_statistic() (+15 more)

### Community 8 - "Community 8"
Cohesion: 0.12
Nodes (23): BaseModel, build_child_command(), build_parent_command(), _child_idempotency_key(), _parent_idempotency_key(), Publish executable spawn work commands for Phase 2b workers., Build a RUN_PARENT spawn envelope., Build a RUN_CHILD spawn envelope. (+15 more)

### Community 9 - "Community 9"
Cohesion: 0.14
Nodes (23): child_agent_node(), ChildConfigsOutput, _fallback_memo(), memo_to_text(), parent_agent_node(), ParentConfigsOutput, _policy_context(), Any (+15 more)

### Community 10 - "Community 10"
Cohesion: 0.10
Nodes (22): _allowed_origins(), get_run_5d_graph(), get_run_reasoning(), health_check(), Ingest5DRequest, ingest_run_5d_graph(), lifespan(), HTTP interface for HiveMind's causal evidence compiler.  The API exposes two pat (+14 more)

### Community 11 - "Community 11"
Cohesion: 0.17
Nodes (21): get_run_context(), Return the active run context, if any., Kafka event bus for HiveMind semantic artifacts and telemetry., _emit(), publish_artifact(), publish_run_event(), publish_spawn(), publish_telemetry() (+13 more)

### Community 12 - "Community 12"
Cohesion: 0.11
Nodes (17): Barrier waits for coordinator phase advancement., Poll run store until predicate is true or timeout., wait_for_barrier(), _dispatch_children(), _dispatch_parents(), enqueue_child_tasks(), enqueue_parent_tasks(), Publish RUN_PARENT commands for each orchestrator parent config. (+9 more)

### Community 13 - "Community 13"
Cohesion: 0.16
Nodes (20): _backfill_5d_graph(), execute_run(), _gather_children(), _ingest_policy_optimization(), _load_kg_snapshot(), Any, Coordinator state machine — replaces LangGraph graph.ainvoke in Phase 2a., Barrier telemetry after all parents complete. (+12 more)

### Community 14 - "Community 14"
Cohesion: 0.15
Nodes (21): clean_variable(), _coerce_float(), compile_evidence_dataset(), DatasetCompilation, _normalize_records(), passes_estimation_gates(), _profile_warnings(), Any (+13 more)

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (21): clear_run_context(), Clear run context after a workflow finishes., _impact_ate(), _impact_confidence(), _memo_text(), Any, Convert a raw decision memo into a compact UI strategy card., Return ATE for the UI, or None when estimation was withheld. (+13 more)

### Community 16 - "Community 16"
Cohesion: 0.17
Nodes (19): _build_gml(), estimate_causal_effect(), _linear_regression_stats(), Any, DataFrame, Estimate causal effects from compiled evidence datasets.  DoWhy is used for caus, Build a GML DAG string compatible with NetworkX and DoWhy., Compute OLS diagnostics for the treatment coefficient. (+11 more)

### Community 17 - "Community 17"
Cohesion: 0.12
Nodes (17): AzureChatOpenAI, ChatOpenAI, evaluate_memos_node(), EvaluationScore, _memo_value(), MemoEvaluation, Any, RankedStrategies (+9 more)

### Community 18 - "Community 18"
Cohesion: 0.17
Nodes (18): causal_synthesis_node(), dowhy_engine_node(), _ensure_nodes(), _format_memo(), _memo_value(), Any, LangGraph nodes for causal hypothesis generation and estimation.  The LLM-facing, Compile evidence records and estimate causal effects when gates pass. (+10 more)

### Community 19 - "Community 19"
Cohesion: 0.19
Nodes (16): grand_orchestrator_node(), Decompose the incident into parent-agent investigation tracks., build_graph(), conditional_refutation_check(), gather_children_node(), LangGraph assembly for HiveMind's investigation and causal workflow.  Deprecated, Route execution to parent agents selected by the orchestrator., Barrier node that lets dynamically produced child configs converge. (+8 more)

### Community 20 - "Community 20"
Cohesion: 0.18
Nodes (14): _default_incident(), main(), Legacy Streamlit entry point for the HiveMind backend.  The Docker Compose demo, Render estimator output without pretending withheld effects are valid., Return the default incident prompt for local demos., Render the Streamlit demo and execute HiveMind on demand., Execute a run and render graph, impact, and raw artifact panels., Render an interactive causal DAG when graph data exists. (+6 more)

### Community 21 - "Community 21"
Cohesion: 0.21
Nodes (10): Telemetry consumer for SSE streaming., ArtifactType, Event envelope schema and artifact type registry., Semantic artifact kinds published on the HiveMind bus., Per-run Kafka publish counters for Phase 1b metrics., Kafka topic names and artifact routing., Return the Kafka topic for an artifact type., topic_for_artifact() (+2 more)

### Community 22 - "Community 22"
Cohesion: 0.16
Nodes (9): get_run_summary(), Per-run publish context (run id, correlation id, sequence counters)., Tracks sequencing for one HiveMind run., Return bus artifact counters for the active run, or empty defaults., RunPublishContext, Shared helpers for binding publish context inside graph nodes., Counts semantic artifacts published during one run., Increment counters for a published artifact type. (+1 more)

### Community 23 - "Community 23"
Cohesion: 0.23
Nodes (12): demo_estimate(), Run a deterministic SIEM-style evidence-backed causal estimate., demo_causal_payload(), patch_lateral_movement_evidence(), patch_lateral_movement_graph(), Any, Deterministic evidence fixtures for demos and smoke tests.  The fixture in this, Return deterministic SIEM-style evidence records for demo estimation. (+4 more)

### Community 24 - "Community 24"
Cohesion: 0.24
Nodes (11): bind_from_state(), Any, Bind Kafka publish context from LangGraph state (sync or fan-out nodes)., _asset_table(), build_reasoning_report(), Any, Deterministic reasoning layer over the 5D spatiotemporal graph.  Consumes what t, Coordinator node: reason over the run's validated causal model. (+3 more)

### Community 25 - "Community 25"
Cohesion: 0.18
Nodes (7): Run coordinator — bus-native scheduler replacing LangGraph in Phase 2., SQLite-backed durable run state for the Phase 2 coordinator., Load a run record by id., Override the process-default run store (tests)., _record_from_json(), set_run_store(), Filesystem path helpers for runtime state.

### Community 26 - "Community 26"
Cohesion: 0.18
Nodes (11): enqueue_run(), _execute_run_background(), Any, Request body for the full agentic workflow., Run HiveMind in the background for async POST /run., Enqueue the full agent graph and return immediately., Blocking run endpoint retained for scripts and integration tests., run_engine_sync() (+3 more)

### Community 27 - "Community 27"
Cohesion: 0.25
Nodes (5): Any, Insert a new run record., Create a queued run awaiting background execution., Merge a node return dict into this record., _record_to_json()

### Community 28 - "Community 28"
Cohesion: 0.33
Nodes (6): Fetch the compiled 5D spatiotemporal graph nodes and edges.          Reads from, connect_graph_db(), graph_db_path(), Path, Resolve the 5D graph database path (overridable via env for tests)., Open (and lazily initialise) a connection to the dedicated graph DB.

### Community 29 - "Community 29"
Cohesion: 0.33
Nodes (5): Any, Refutation loop termination rules shared by coordinator and legacy graph., Stop when refuters pass or when estimation is explicitly withheld., refutation_next_step(), _run_causal_loop()

### Community 30 - "Community 30"
Cohesion: 0.50
Nodes (4): estimate_from_evidence(), EstimateRequest, Request body for deterministic evidence-backed estimation., Compile caller evidence and return a causal estimate report.

### Community 31 - "Community 31"
Cohesion: 0.50
Nodes (4): get_run_status(), Return run lifecycle status and artifact when complete., load_run_artifact(), Load a persisted run artifact from disk.

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `RunRecord` connect `Community 12` to `Community 6`, `Community 8`, `Community 9`, `Community 13`, `Community 19`, `Community 25`, `Community 27`, `Community 29`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Why does `RunStore` connect `Community 6` to `Community 0`, `Community 8`, `Community 9`, `Community 12`, `Community 13`, `Community 19`, `Community 25`, `Community 27`, `Community 28`, `Community 29`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Why does `ArtifactType` connect `Community 21` to `Community 0`, `Community 1`, `Community 3`, `Community 4`, `Community 8`, `Community 9`, `Community 11`, `Community 17`, `Community 18`, `Community 22`, `Community 24`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `RunRecord` (e.g. with `AgentConfig` and `ChildConfig`) actually correct?**
  _`RunRecord` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `RunStore` (e.g. with `AgentConfig` and `ChildConfig`) actually correct?**
  _`RunStore` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `ArtifactType` (e.g. with `ChildConfigsOutput` and `ParentConfigsOutput`) actually correct?**
  _`ArtifactType` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `LangGraph agent nodes for hierarchical cyber investigation.  The agent layer is`, `Structured output from the grand orchestrator.`, `Decompose the incident into parent-agent investigation tracks.` to the rest of the system?**
  _273 weakly-connected nodes found - possible documentation gaps or missing edges._
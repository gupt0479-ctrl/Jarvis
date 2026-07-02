---
type: project
status: active
created: 2026-07-02
updated: 2026-07-02
related_progress:
  - "[[CausalOps — Index]]"
tags:
  - causalops
  - coordinator
  - pipeline
next: "[[agents]]"
---

# Pipeline and Coordinator

## What the Pipeline Does

CausalOps converts an incident prompt into a guarded causal estimate through 10 sequential stages. The key claim: LLM proposes causal hypotheses, deterministic code decides whether a statistical effect can exist.

## Three Hard Boundaries

**Boundary 1 — LLM -> Evidence.** Agent output is hypothesis context. Evidence enters only through `EvidenceRecord` objects from real SIEM/CVE/incident exports. The compiler skips any record with `source_type: "synthetic"`.

**Boundary 2 -- Evidence -> Estimator.** `dataset_compiler.py` receives only normalized evidence records and the graph structure. Never raw text, never agent narratives.

**Boundary 3 -- ATE Gate.** Below 50 complete rows with valid treatment/control variation, ATE is withheld:
```json
{ "method": "withheld:data_quality_gates", "ate": null, "p_value": null }
```
This is correct behavior, not a failure.

## End-to-End Data Flow

```
Incident Prompt
  -> memory_retrieve_node       fetches 3 similar past runs -> GraphState.memory_context
  -> Grand Orchestrator         LLM: decompose into 2-3 investigation tracks
    -> Island Evolution (parents)   deterministic EA: evolve policy priors
      -> Parent Agents (parallel)   LLM: each spawns 2 ChildConfigs
        -> Island Evolution (children)   deterministic EA: evolve child priors
          -> Child Agents (parallel)     LLM: each produces 1 DecisionMemo
            -> Evaluator              LLM: rank memos, synthesize recommendation
              -> Causal Architect     LLM: design DAG + measurement plan (no data rows)
                -> Causal Discovery   deterministic: PC tests validate each edge
                  -> Evidence Compiler  deterministic: normalize -> dataframe
                    -> DoWhy Estimator  deterministic: estimate ATE or withhold
                      -> Reasoning Layer  deterministic: anomalies + recommendations
                        -> Policy RL      deterministic: value iteration + meta-learning
                          -> memory_write_node    embed + store run in Supabase
                            -> Run Artifact   persisted JSON + 5D KG
```

## Real Execution Path (Phase 2b)

`src/graph.py` is NOT the execution path. Its docstring says "Deprecated for execution in Phase 2b+." The real path is `src/coordinator/runner.py::execute_run()`.

```python
async def execute_run(task_description, evidence_records, run_id, correlation_id):
    record = run_store.create_run(...)          # SQLite row created

    await _run_memory_retrieve(record, store)   # async, try/except swallows
    await _run_orchestrator(record, store)       # asyncio.to_thread
    await _run_parent_evolution(record, store)   # asyncio.to_thread
    await _dispatch_parents(record, store)       # Kafka publish + barrier wait
    await _gather_children(record, store)        # telemetry log
    await _run_child_evolution(record, store)    # asyncio.to_thread
    await _dispatch_children(record, store)      # Kafka publish + barrier wait
    await _run_evaluator(record, store)          # asyncio.to_thread
    await _run_causal_loop(record, store)        # while loop: synthesis + dowhy
    await _run_reasoner(record, store)           # asyncio.to_thread
    if not kafka_enabled():
        _backfill_5d_graph(record)              # no-Kafka path only
    await _run_policy_learning(record, store)    # asyncio.to_thread
    await _run_memory_write(record, store)       # async, try/except swallows

    record.status = "completed"
    run_store.save(record)
    return record.to_graph_state()
```

**Memory phase rules:** Both memory phases are awaited directly (no `asyncio.to_thread`). Both wrapped in `try/except` that logs and swallows -- Supabase outage must never fail a run.

## Why Phase 2b Replaced graph.ainvoke

| Problem with `graph.ainvoke` | Coordinator solution |
|------------------------------|---------------------|
| Ephemeral state (crash loses everything) | SQLite RunRecord persists each phase |
| Kafka producer + consumer in same loop | api publishes, worker consumes |
| No recovery after restart | SQLite state survives restarts |
| Fan-out blocking event loop | Kafka barriers decouple dispatch from execution |

## RunRecord <-> GraphState Bridge

`RunRecord` in `coordinator/store.py` mirrors `GraphState` as a dataclass. `record.to_graph_state()` converts it to a GraphState-compatible dict for node functions. `record.apply_node_update(update)` applies partial node updates back, with list-append semantics for `child_configs` and `memos`.

## Kafka Barriers (Parent and Child Dispatch)

```python
await enqueue_parent_tasks(record)     # publish RUN_PARENT to hivemind.spawn per parent
refreshed = await wait_for_barrier(
    store, record.run_id,
    lambda run: run.parents_barrier_met()   # True when all parents complete
)
```

`wait_for_barrier` polls SQLite every 0.5s. Workers consume `hivemind.spawn`, run the agent node, increment `completed_parent_count`. Barrier lifts when count reaches `expected_parent_count`.

## Causal Loop

```python
while True:
    causal_synthesis_node(state)    # LLM: design DAG
    dowhy_engine_node(state)        # deterministic: compile + estimate
    if refutation_next_step(state) == "end":
        break
```

Breaks when refuters passed, or `method == "withheld:data_quality_gates"`.

## Two-Container Architecture

| Container | `CAUSALOPS_ENABLE_SPAWN_WORKER` | Behavior |
|-----------|--------------------------------|---------|
| `api` | `"0"` | Publishes spawn tasks, does NOT consume them |
| `worker` | `"1"` | Consumes spawn tasks, runs agents, writes results to SQLite |

## SQLite Persistence

```python
DEFAULT_DB_PATH = data_dir() / "runs.db"
# PRAGMA journal_mode=DELETE  (not WAL -- WAL breaks on Docker bind mounts)
# PRAGMA busy_timeout=30000
```

Both api and worker write to the same `./data/runs.db` via Docker bind mount.

## LangGraph Topology (Reference Only)

`src/graph.py` defines the original LangGraph workflow. Still ships for reference and refutation routing tests. Memory layer nodes are also wired here cosmetically.

```
START -> memory_retrieve -> orchestrator
  -> parent_agent (parallel fan-out via Send)
  -> gather_children (barrier)
  -> child_agent (parallel fan-out via Send)
  -> evaluate_memos
  -> causal_synthesis
  -> dowhy_engine
  -> conditional_refutation_check
  -> (retry: causal_synthesis | end: memory_write) -> END
```

## GraphState Contract

`GraphState` in `src/schema.py` is the master TypedDict:

```python
class GraphState(TypedDict):
    task_description: str
    run_id: str
    correlation_id: str
    parent_configs: list[AgentConfig]
    child_configs: Annotated[list[ChildConfig], operator.add]  # accumulate across parents
    memos: Annotated[list[DecisionMemo], operator.add]         # accumulate across children
    ranked_strategies: list[dict[str, Any]]
    final_recommendation: str | None
    evaluator_error: str | None
    causal_payload: dict[str, Any] | None
    causal_refutation_passed: bool
    causal_refutation_attempts: int
    evidence_records: list[dict[str, Any]]
    causal_dataset_profile: dict[str, Any] | None
    causal_estimate_report: dict[str, Any] | None
    causal_discovery_report: dict[str, Any] | None
    reasoning_report: dict[str, Any] | None
    agent_evolution_report: dict[str, Any] | None
    policy_optimization_report: dict[str, Any] | None
    memory_context: list[dict[str, Any]] | None  # retrieved past context (list, NOT str)
```

Two fields use `Annotated[list, operator.add]`: LangGraph appends rather than replaces for `child_configs` and `memos`.

## Docker Services

| Service | Port | Role |
|---------|------|------|
| `api` | 8000 | FastAPI: coordinator + SSE, no spawn consumer |
| `worker` | -- | Spawn consumer + graph stream consumer |
| `redpanda` | 19092 | Kafka-compatible event bus |
| `frontend` | 8080 | React/TanStack UI |
| `mcp` | 8001 | Memory MCP server |

## Related Notes

- [[CausalOps — Index]] -- project index
- [[agents]] -- orchestrator, parent/child agents, evolution
- [[causal-engine]] -- evidence, estimation, reasoning
- [[event-bus]] -- Kafka topics and worker
- [[memory-layer]] -- memory implementation status

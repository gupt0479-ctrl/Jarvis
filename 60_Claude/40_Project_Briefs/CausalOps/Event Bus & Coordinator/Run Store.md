---
type: project
status: sprout
created: 2026-07-01
tags: [causalops, coordinator, sqlite, run-store, persistence]
aliases: [coordinator/store.py]
---

# Run Store — SQLite-Backed Durable Run State

`src/coordinator/store.py` provides `RunRecord` (in-memory view) and `RunStore` (SQLite persistence) for durable run state. This is what allows the coordinator to survive container restarts and enables the api/worker split.

## RunRecord Dataclass

```python
@dataclass
class RunRecord:
    run_id: str
    correlation_id: str
    task_description: str
    phase: str = "created"
    status: str = "running"           # created | queued | running | completed | failed
    error_detail: str | None = None
    evidence_records: list[dict]
    parent_configs: list[AgentConfig]
    child_configs: list[ChildConfig]
    memos: list[DecisionMemo]
    ranked_strategies: list[dict]
    final_recommendation: str | None
    evaluator_error: str | None
    causal_payload: dict | None
    causal_refutation_passed: bool
    causal_refutation_attempts: int
    dowhy_results: dict | None
    causal_dataset_profile: dict | None
    causal_estimate_report: dict | None
    reasoning_report: dict | None
    agent_evolution_report: dict | None
    policy_optimization_report: dict | None
    # Coordinator barriers
    expected_parent_count: int
    completed_parent_count: int
    expected_child_count: int
    completed_child_count: int
```

## RunStore Methods

```python
class RunStore:
    def create_run(run_id, correlation_id, task_description, evidence_records, status) → RunRecord
    def get_run(run_id) → RunRecord          # raises KeyError if not found
    def save(record: RunRecord) → None       # JSON-serialize and upsert to SQLite
    def set_phase(record, phase) → None      # update phase + save
    def set_status(record, status, error_detail=None) → None
    def enqueue_run(...) → RunRecord         # create with status="queued"
    def get_5d_graph(run_id) → dict          # load KG from graph_5d.db
```

## SQLite Configuration

```python
DEFAULT_DB_PATH = data_dir() / "runs.db"
# PRAGMA journal_mode=DELETE  (NOT WAL — WAL shared-memory unreliable on Docker bind mounts)
# PRAGMA busy_timeout=30000
# PRAGMA synchronous=NORMAL
```

Both api and worker containers write to the same `./data/runs.db` via a Docker bind mount. The `DELETE` journal mode (rollback journal) ensures single-writer safety without shared memory.

## RunRecord.to_graph_state()

Converts RunRecord to a dict compatible with `GraphState` TypedDict:
```python
state = record.to_graph_state()
# → passes to node functions that expect a GraphState dict
```

## RunRecord.apply_node_update(update)

Merges a node's partial update dict into the RunRecord:
```python
record.apply_node_update({"parent_configs": [...]})
# → updates record.parent_configs and saves
```

For list fields with reducers (memos, child_configs), applies `operator.add` semantics to accumulate.

## Barrier Predicates

```python
def parents_barrier_met(self) → bool:
    return self.completed_parent_count >= self.expected_parent_count

def children_barrier_met(self) → bool:
    return self.completed_child_count >= self.expected_child_count
```

Workers increment these counters as they complete tasks.

## Global Singleton

```python
_DEFAULT_STORE: RunStore | None = None

def get_run_store() → RunStore:
    ...  # lazily created singleton per process

def set_run_store(store) → None:
    ...  # used in tests to inject a test store
```

## Related Notes

- [[Coordinator Runner]] — Uses RunStore for all phase state persistence
- [[Coordinator Execution Model]] — Why SQLite persistence matters (recovery, api/worker split)
- [[Kafka Bus Overview]] — Workers write results to RunStore after consuming spawn tasks

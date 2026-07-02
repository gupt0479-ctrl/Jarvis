---
type: project
status: active
created: 2026-07-02
updated: 2026-07-02
related_progress:
  - "[[CausalOps — Index]]"
tags:
  - causalops
  - causal-inference
  - dowhy
next: "[[event-bus]]"
---

# Causal Engine

The causal engine is four deterministic stages: discovery, evidence compilation, estimation, and reasoning. LLMs have no visibility into any of these stages after synthesis. If statistical guards fail, the ATE is withheld rather than estimated unreliably.

## Stage 1: Causal Discovery (causal_discovery.py)

**Input:** DAG skeleton from causal synthesis (LLM-proposed edges).

**Process:** PC algorithm over evidence data. For each proposed edge, runs conditional independence tests. Each edge is either:
- **validated** — kept in the graph
- **refuted** — removed
- **undecided** — insufficient data to decide

**Key constants:**
```python
ALPHA = float(os.getenv("CAUSALOPS_DISCOVERY_ALPHA", "0.1"))      # independence test threshold
MIN_ROWS = int(os.getenv("CAUSALOPS_DISCOVERY_MIN_ROWS", "30"))   # min rows to run discovery
```

Below `MIN_ROWS`, all edges are marked "compatible" (not validated, not refuted).

**Output:** `causal_discovery_report` with per-edge status and test statistics.

## Stage 2: Evidence Compiler (dataset_compiler.py)

**Input:** `evidence_records` (list of `EvidenceRecord` dicts) + validated DAG.

**Safeguard — source_type guard:**
```python
if record.get("source_type") == "synthetic":
    continue   # skip silently
```
Records must originate from real exports (SIEM, CVE databases, incident logs). No agent-generated data rows pass this gate.

**Process:**
1. Normalize evidence records to a flat dataframe
2. Identify treatment column (binary indicator from DAG) and outcome column
3. Build control and treatment groups

**Output:** DataFrame + `causal_dataset_profile` with row counts, missing data rates, and treatment split.

## Stage 3: DoWhy Estimation (estimators.py)

**Input:** DataFrame from compiler + dataset profile.

**ATE gate (hard rules):**
```python
MIN_COMPLETE_ROWS = 50
# Must have: >= MIN_COMPLETE_ROWS rows, treatment variation, outcome variation
```

If any gate fails:
```json
{
  "method": "withheld:data_quality_gates",
  "ate": null,
  "p_value": null,
  "effect_size": null
}
```

This is **correct behavior**, not a bug. The `ate: null` result with `method: "withheld:..."` indicates evidence was insufficient -- the pipeline continues with this in the report, and the evaluator uses it to contextualize recommendations.

**When gates pass:** Runs DoWhy with linear regression estimator. Computes ATE + p-value + confidence interval. Runs refuter tests (placebo treatment, random common cause, data subset). If refuters fail, `causal_refutation_passed = False` and the causal loop retries synthesis.

**Output:** `causal_estimate_report` with ATE, confidence, refutation results.

## Stage 4: Reasoning Layer (reasoning.py)

**Input:** `evidence_records`, `causal_payload` (validated graph), `causal_estimate_report`.

**What it produces:**

1. **Anomaly detection** — Assets whose adverse outcome probability deviates from treatment group average by more than `CAUSALOPS_ANOMALY_THRESHOLD` (default 0.15). Each anomaly is explained by walking the validated DAG for active non-refuted edges. Anomalies with no explaining cause → **unexplained** → highest severity signal.

2. **Zone pressure summary** — Anomaly and outcome concentration per network zone.

3. **Ranked recommendations:**
   1. Investigate unexplained anomalies (model cannot account for them)
   2. Apply treatment to highest-risk assets (only if ATE statistically significant)
   3. Mitigate confirmed secondary causes from validated DAG

**Key constants:**
```python
ANOMALY_THRESHOLD = float(os.getenv("CAUSALOPS_ANOMALY_THRESHOLD", "0.15"))
MAX_LISTED_TARGETS = int(os.getenv("CAUSALOPS_REASONING_MAX_TARGETS", "10"))
```

**Output:** `reasoning_report` with anomaly list, zone summary, and ranked recommendations.

## LangGraph Node Interface

All four stages expose LangGraph-compatible node functions:

```python
def causal_discovery_node(state: GraphState) -> dict:
    # Reads: evidence_records, causal_payload
    # Writes: {"causal_discovery_report": report, "causal_payload": updated_graph}

def causal_synthesis_node(state: GraphState) -> dict:
    # LLM node — reads: task_description, ranked_strategies, final_recommendation, evidence_records
    # Writes: {"causal_payload": dag_design}

def dowhy_engine_node(state: GraphState) -> dict:
    # Reads: evidence_records, causal_payload
    # Writes: {"causal_estimate_report": report, "causal_dataset_profile": profile,
    #          "causal_refutation_passed": bool, "causal_refutation_attempts": n}

def reasoning_node(state: GraphState) -> dict:
    # Reads: evidence_records, causal_payload, causal_estimate_report
    # Writes: {"reasoning_report": report}
```

## 5D Knowledge Graph Integration

Validated edges from discovery + anomaly nodes from reasoning are written to the SQLite graph DB (`graph_5d.db`) after each run:
- Each causal edge → KG edge with relationship type
- Each anomaly → KG node with asset details + anomaly flag
- All tagged with `run_id` for cross-run traceability

The KG is built either via Kafka stream (when `KAFKA_ENABLED`) or via `_backfill_5d_graph()` in the coordinator (no-Kafka path).

## Related Notes

- [[CausalOps — Index]] -- project index
- [[pipeline-coordinator]] -- causal loop phase in execute_run
- [[agents]] -- evaluator output feeds causal synthesis context
- [[memory-layer]] -- anomaly nodes written to KG then embedded for future retrieval

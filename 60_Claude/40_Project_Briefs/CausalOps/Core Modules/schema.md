---
type: project
status: sprout
created: 2026-07-01
tags: [causalops, schema, pydantic, models]
aliases: [schema.py]
---

# schema.py — Shared Contracts

`src/schema.py` is the single source of truth for all Pydantic models and the `GraphState` TypedDict. Every other module imports from here. **This is the contract layer** — changing it affects the entire pipeline.

## Three Separated Layers

```python
"""
* agent outputs — LLM-authored hypotheses and memos
* evidence records — normalized observations from logs/feeds/reports
* causal estimate reports — produced by deterministic compiler + estimator
"""
```

This separation prevents the estimator from silently falling back to LLM-generated rows.

## Causal Graph Models

### CausalNode
```python
class CausalNode(BaseModel):
    id: str              # unique variable name, no spaces
    label: str           # human readable
    description: str     # what this node represents in the scenario
```

### CausalEdge
```python
class CausalEdge(BaseModel):
    source: str
    target: str
    relationship: str           # causal mechanism description
    required_evidence: list[str]   # observable records that support this edge
    falsification_tests: list[str] # observations that would weaken this edge
```

### CausalGraphDef
```python
class CausalGraphDef(BaseModel):
    nodes: list[CausalNode]
    edges: list[CausalEdge]
    treatment_variable: str      # the intervention node ID
    outcome_variable: str        # the outcome node ID
    candidate_confounders: list[str]  # covariates to adjust for
```

### VariableMeasurementPlan
```python
class VariableMeasurementPlan(BaseModel):
    variable: str
    description: str
    evidence_fields: list[str]   # expected fields from telemetry/feeds/reports
    aggregation: str             # how to aggregate raw evidence into a row
    expected_type: Literal["binary", "continuous", "count"]
```

### CausalPayload
The LLM-authored causal hypothesis (no data rows):
```python
class CausalPayload(BaseModel):
    graph: CausalGraphDef
    measurement_plan: list[VariableMeasurementPlan]
    edge_evidence_requirements: list[EdgeEvidenceRequirement]
```

## Evidence Models

### EvidenceRecord
The normalized evidence contract — all external data enters through this:
```python
class EvidenceRecord(BaseModel):
    source_type: Literal[
        "siem", "edr", "cve", "incident_report",
        "asset_inventory", "manual", "synthetic"
    ]
    source_name: str           # e.g. "sentinel-kql-export"
    observed_at: str | None    # ISO timestamp
    asset_id: str | None       # host, workload, identity
    user_id: str | None
    event_type: str | None     # normalized event/detection type
    technique_id: str | None   # MITRE ATT&CK ID
    cve_id: str | None
    severity: float | None
    raw_text: str | None       # raw log line or report excerpt
    raw_ref: str | None        # pointer back to original record
    extracted_fields: dict[str, Any]  # already-normalized values
    confidence: float = 1.0
```

**Key invariant:** `source_type: "synthetic"` records are skipped by `dataset_compiler.py`.

### CausalDatasetProfile
Quality profile from the compiler:
```python
class CausalDatasetProfile(BaseModel):
    data_mode: Literal["empirical", "insufficient_data", "synthetic_simulation"]
    n_rows: int
    columns: list[str]
    treatment: str
    outcome: str
    adjustment_set: list[str]
    treated_count: int
    control_count: int
    missingness: dict[str, float]
    warnings: list[str]
```

### CausalEstimateReport
Full statistical report:
```python
class CausalEstimateReport(BaseModel):
    data_mode: Literal["empirical", "insufficient_data", "synthetic_simulation"]
    method: str          # e.g. "backdoor.linear_regression" or "withheld:data_quality_gates"
    treatment: str
    outcome: str
    adjustment_set: list[str]
    n_rows: int = 0
    ate: float | None = None
    standard_error: float | None = None
    p_value: float | None = None
    ci_low: float | None = None
    ci_high: float | None = None
    refutation_passed: bool = False
    refuters: list[RefuterReport]
    warnings: list[str]
    dataset_profile: CausalDatasetProfile | None
```

## Agent Models

See [[GraphState Contract]] for `AgentConfig`, `ChildConfig`, `AgentPolicy`, `DecisionMemo`.

## Related Notes

- [[GraphState Contract]] — TypedDict + agent schemas in detail
- [[dataset_compiler]] — Uses EvidenceRecord and CausalDatasetProfile
- [[estimators]] — Returns CausalEstimateReport
- [[agents]] — Produces AgentConfig, ChildConfig, DecisionMemo
- [[causal]] — Uses CausalPayload and CausalGraphDef

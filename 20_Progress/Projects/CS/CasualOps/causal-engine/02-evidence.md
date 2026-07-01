# Evidence Compiler

`src/dataset_compiler.py` is the statistical boundary between LLM hypotheses and estimation. **DO NOT MODIFY** — it is the primary safeguard preventing LLM-generated rows from reaching DoWhy.

## What It Accepts and Rejects

Input: a `CausalGraphDef` dict (the treatment/outcome/confounders) and a list of `EvidenceRecord` dicts from the caller.

**Critical guard**: any record with `source_type: "synthetic"` is skipped before any processing. This is the line that prevents LLM-generated synthetic data from contaminating estimates.

## Statistical Gates

```python
MIN_COMPLETE_ROWS = 50           # minimum observation rows for estimation
RECOMMENDED_COMPLETE_ROWS = 200  # recommended for stable estimates
MIN_TREATMENT_GROUP_ROWS = 10    # minimum rows in both treated and control groups
```

`passes_estimation_gates()` returns `(False, warnings)` if any gate fails → estimator withholds ATE.

## EvidenceRecord (from schema.py)

The normalized evidence contract — all external data enters through this:

```python
class EvidenceRecord(BaseModel):
    source_type: Literal[
        "siem", "edr", "cve", "incident_report",
        "asset_inventory", "manual", "synthetic"
    ]
    source_name: str          # e.g. "sentinel-kql-export"
    observed_at: str | None   # ISO timestamp
    asset_id: str | None
    user_id: str | None
    event_type: str | None
    technique_id: str | None  # MITRE ATT&CK ID
    cve_id: str | None
    severity: float | None
    raw_text: str | None
    raw_ref: str | None       # pointer back to original record
    extracted_fields: dict[str, Any]  # already-normalized field values
    confidence: float = 1.0
```

## Compile Flow

1. Extract treatment/outcome/confounders from graph_def
2. Filter out `source_type: "synthetic"` records
3. For each record: look up numeric values for each variable via `_variable_lookup()`
4. Build a row if at least treatment OR outcome has a value
5. Coerce all values to float via `_coerce_float()`
6. Build pandas DataFrame (one row per evidence record with data)
7. Drop rows missing treatment or outcome
8. Build `CausalDatasetProfile` with counts, missingness, warnings
9. Return `DatasetCompilation`

## Variable Lookup Priority

For each variable, searches `extracted_fields` dict using:
1. Exact match on variable name
2. Case-insensitive match
3. Normalized match (spaces → underscores, lowercase)
4. `raw_text` float parsing as fallback

## Type Coercion (_coerce_float)

```
"true"/"yes"/"present"/"detected"/"treated" → 1.0
"false"/"no"/"absent"/"clean"/"control"     → 0.0
numeric strings → float(value)
None or ""     → None (missing)
```

## DatasetCompilation Output

```python
@dataclass
class DatasetCompilation:
    dataframe: pd.DataFrame          # numeric rows, one per evidence observation
    profile: CausalDatasetProfile    # quality metrics and metadata
    provenance: list[dict[str, Any]] # row-level source traceability
```

Each provenance row records: asset_id, observed_at, source_type, source_name, raw_ref, and which variables were found vs missing.

## Evidence Normalizers (evidence_adapters.py)

External evidence enters via three normalizers before compilation:

- `normalize_sentinel_records()` → `source_type: "siem"` — extracts Computer, AlertName, TimeGenerated, MITRE technique, plus all remaining fields as `extracted_fields`
- `normalize_cve_records()` → `source_type: "cve"` — extracts cve_id, baseScore, English description
- `normalize_incident_reports()` → `source_type: "incident_report"` — extracts asset_id, severity, technique from summary text

All three pass arbitrary extra fields through as `extracted_fields`, so custom SIEM columns like `Patch_Applied` or `Lateral_Movement` survive to the compiler.

## Related Notes

- [[causal-engine/01-discovery|Discovery]] — also receives the compiled dataframe for independence tests
- [[causal-engine/03-estimation|Estimation]] — consumes DatasetCompilation.dataframe and profile
- [[causal-engine/00-overview|Overview]] — why the synthetic guard is the primary safeguard
- [[infrastructure/01-api|API]] — `/normalize/*` and `/estimate` endpoints

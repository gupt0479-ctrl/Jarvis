# Causal Engine Overview

The causal pipeline enforces a strict authorship separation: LLMs design the hypothesis, deterministic code decides whether a statistical effect can exist. This is the core differentiator from agent demos that generate plausible-sounding effects.

## The Epistemic Problem Being Solved

When an LLM both proposes the causal story *and* provides the supporting data, you cannot distinguish real causal effects from confident hallucination. HiveMind solves this by separating authorship by law, not by convention.

| Who authors it | What it can produce | What it cannot produce |
|----------------|---------------------|------------------------|
| LLM | Causal DAG, measurement plan, memos | Estimator data rows |
| Deterministic code | Evidence dataset, ATE, p-value, CIs | Narrative or strategy |

## The Three Hard Boundaries (repeated from [[pipeline/00-overview|Overview]])

**LLM → Evidence**: `EvidenceRecord` with `source_type: "synthetic"` are skipped by the compiler.

**Evidence → Estimator**: The estimator receives only the compiled dataframe and quality profile. Never raw text, never agent output.

**ATE Gate**: Below 50 complete rows with valid variation, ATE is withheld. `ate=null` is the honest answer when data is insufficient.

## Causal Pipeline Stages

```
causal_synthesis_node        LLM: design DAG + measurement plan
       ↓
causal_discovery             deterministic: PC tests validate each edge
       ↓
compile_evidence_dataset     deterministic: normalize records → dataframe
       ↓
estimate_causal_effect       deterministic: DoWhy + statsmodels
       ↓ conditional_refutation_check
       ├── end (refuters passed or ATE withheld)
       └── causal_synthesis (retry loop)
```

## What causal_synthesis_node Can and Cannot Do

It can produce: a `CausalGraphDef` (nodes, edges, treatment, outcome, confounders), a `VariableMeasurementPlan` (how to compile evidence into each variable), and `EdgeEvidenceRequirement` (confirming/falsifying evidence per edge).

It cannot produce: numeric data rows, EvidenceRecord objects, or ATE values. The `CausalPayload` Pydantic model has no field for dataset rows — there is nowhere to put them.

## Demo Evidence Detection

```python
if is_demo_evidence(evidence_records):
    # use bundled fixture, skip LLM call for causal_synthesis
    payload_dict = demo_causal_payload()
```

A run uses demo evidence when: no evidence records provided, or all records have `source_type: "synthetic"`. This enables smoke testing without real credentials.

## Causal Discovery as an Additional Safeguard

The LLM proposes a DAG. `causal_discovery.py` runs PC-style independence tests on the *actual compiled evidence* to validate every edge. Refuted edges are dropped before DoWhy runs. The LLM cannot steer these verdicts.

## ATE Withholding Logic

```python
if not gates_passed:
    return CausalEstimateReport(
        method="withheld:data_quality_gates",
        ate=None, p_value=None, ...
    )
```

Gates checked: min 50 complete rows, min 10 treated + 10 control rows, variation in treatment and outcome, acceptable missingness per column.

## Related Notes

- [[causal-engine/01-discovery|Discovery]] — PC algorithm details
- [[causal-engine/02-evidence|Evidence]] — EvidenceRecord, compiler, gates
- [[causal-engine/03-estimation|Estimation]] — DoWhy and statsmodels
- [[causal-engine/04-reasoning|Reasoning]] — anomalies and recommendations
- [[pipeline/00-overview|Pipeline Overview]] — where this fits end-to-end

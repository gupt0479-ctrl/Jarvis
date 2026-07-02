---
tags: [causalops, philosophy, design, epistemics]
---

# Design Philosophy

## The Core Claim

> "The LLM proposes hypotheses. Evidence decides whether an ATE is allowed to exist."

Most agent demos stop at a confident narrative. CausalOps is built to survive the engineering objection: **"Where did the data come from?"**

## The Epistemic Crisis It Solves

LLM agents have a failure mode: they generate plausible narratives that are internally consistent but empirically unfounded. When an LLM both proposes the causal story *and* provides the supporting data, you cannot distinguish real causal effects from confident hallucination.

CausalOps solves this by enforcing strict authorship separation:

| Who authors it | What it can produce | What it cannot produce |
|---------------|---------------------|------------------------|
| LLM | Causal DAG hypothesis, measurement plan, memos | Estimator data rows |
| Deterministic code | Evidence dataset, ATE, p-value, confidence intervals | Narrative or strategy |

## Why ATE Withholding Is the Point

When `ate = null` and `method = "withheld:data_quality_gates"`, the system is working correctly. This is not a failure — it is the honest answer when evidence is insufficient. A system that always returns a number is less trustworthy than one that refuses when data is weak.

Gates checked before estimation:
- Minimum 50 complete observation rows
- Minimum 10 treated rows and 10 control rows
- Observed variation in both treatment and outcome
- Acceptable covariate missingness (< threshold per column)

## Causal Discovery as an Additional Safeguard

The LLM proposes a DAG. `causal_discovery.py` then runs a PC-algorithm-style independence test on the *actual compiled data* to validate every edge:

- **confirmed** — dependence and orientation match the hypothesis
- **compatible** — dependence supported but data cannot orient the edge; hypothesis direction adopted
- **reversed** — data orients the edge in the opposite direction
- **refuted** — variables are statistically independent; edge is removed before estimation
- **discovered** — data shows a dependency the LLM did not hypothesize

Refuted edges are dropped before DoWhy runs. The LLM cannot steer these verdicts because they are computed from evidence records, not from LLM output.

## Agent Evolution Philosophy

`evolution.py` runs a steady-state island evolutionary algorithm over agent *policy traits* — not over the incident description or evidence. The traits (evidence_weight, causal_focus, temporal_awareness, etc.) are priors that steer agent prompts, not content generators. Evolution cannot fake data; it can only make agents more evidence-focused.

## Reinforcement Learning Philosophy

`policy_learning.py` runs after each completed run. It builds a model-based RL report from:
- Evaluator scores (did agents produce good memos?)
- Causal estimate strength (did the evidence support the hypothesis?)
- Reasoning anomalies (what did the data flag as surprising?)
- KG topology (how are entities connected?)

The RL loop learns *policy priors* for future runs — not ground-truth facts about the world. It is meta-learning, not knowledge injection.

## Related Notes

- [[System Overview]] — Full pipeline and data flow
- [[dataset_compiler]] — Where the statistical boundary lives
- [[estimators]] — What happens when gates pass or fail
- [[causal_discovery]] — How the DAG is validated against data
- [[evolution]] — Island EA mechanics
- [[policy_learning]] — KG-grounded RL mechanics

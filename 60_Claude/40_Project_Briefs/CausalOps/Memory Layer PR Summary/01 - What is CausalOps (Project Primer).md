---
type: project
status: reference
created: 2026-07-09
tags: [causalops, project-primer, onboarding]
---

# What is CausalOps? (Read This If You Know Nothing About the Project)

> [!note] This note assumes zero prior context. If you already know what CausalOps is, skip to [[00 - Executive Summary (Meeting Prep)]].

## The Problem CausalOps Solves

Large language models are very good at producing *convincing* explanations. They are equally good at producing convincing explanations that are **completely unsupported by evidence** — a phenomenon usually called "hallucination," though in this context it's really an epistemology problem, not just a factual-accuracy problem.

Most "AI agent" systems let an LLM do all three of these steps itself:
1. Generate a hypothesis ("this incident was caused by X")
2. Generate the supporting evidence
3. Explain why the evidence proves the hypothesis

The result reads well — it has confident language, a plausible narrative, maybe even numbers in it — but it has no actual statistical foundation. The LLM is grading its own homework, and homework graded by the student who wrote it always passes.

This isn't a hypothetical concern for a cybersecurity tool. If an analyst trusts a fabricated causal claim ("patching this vulnerability reduced attacks by 40%") that was never actually tested against real data, they make real remediation decisions on a number that means nothing.

## The Core Design Principle

> *"The LLM proposes hypotheses. Deterministic code falsifies them."*

This is CausalOps's one-sentence design philosophy, and it is enforced as a hard architectural boundary, not a guideline. Concretely, this boundary shows up as five separate rules, each backed by actual code:

1. **The LLM never generates evidence rows.** `dataset_compiler.py` has an explicit guard: any evidence record tagged `source_type == "synthetic"` is silently dropped before it ever reaches the statistical estimator. There is no code path by which an LLM's output becomes a row in the dataset DoWhy estimates against.
2. **A separate, deterministic evidence compiler** (`dataset_compiler.py`) ingests real SIEM logs, CVE records, and incident reports, and *only* that real data is used to test any hypothesis.
3. **Statistical libraries compute the answer, not the LLM.** `DoWhy` (for the causal estimate) and `statsmodels` (for the p-value, computed independently via OLS regression) do the actual math. The LLM's role stops at proposing *which* variables might be causally related — it never gets to say what the effect size is.
4. **A separate causal-discovery pass validates the LLM's proposed graph.** The LLM might hypothesize "patching reduces lateral movement" — but a PC-algorithm-based conditional-independence test (`causal_discovery.py`) checks that hypothesis against the *actual* evidence and **prunes any edge that isn't statistically supported**, regardless of how confident the LLM's proposal sounded.
5. **If the evidence is too weak, the system refuses to produce a number.** Concretely: fewer than 50 complete treatment/outcome observations, fewer than 10 treated rows, fewer than 10 control rows, or no observed variation in treatment or outcome — any one of these triggers a refusal. The API returns exactly this instead of a fabricated result:

```json
{
  "method": "withheld:data_quality_gates",
  "ate": null,
  "confidence_interval": null,
  "p_value": null
}
```

*This refusal-when-uncertain behavior is treated as a **feature**, not a bug — stated explicitly in the project's own documentation.* A system that always gives you an answer is less trustworthy than one that sometimes says "the evidence doesn't support a conclusion yet," because the former has no way to distinguish a confident correct answer from a confident guess.

## What "CausalOps" Actually Does, End to End — A Worked Example

Imagine a SOC analyst submits: *"Suspected lateral movement via RDP in the finance segment — host FIN-042 shows unusual authentication patterns following a recent patch deployment."*

Here is what happens, step by step, mapped to the ten pipeline stages CausalOps's own documentation names:

| # | Stage | What happens with this specific example |
|---|---|---|
| 1 | **Decompose** | The orchestrator agent reads the incident and decides how many independent investigation "tracks" to spin up — e.g., one track for "was this actually lateral movement," another for "was the patch actually a factor." |
| 2 | **Investigate** | Parent agents each spawn child agents with narrow, specific mandates — e.g. a child agent tasked purely with "identify the fastest containment strategy" writes a decision memo; another, tasked with "name the telemetry needed to test causality," writes a different one. |
| 3 | **Evaluate** | An evaluator agent (or, in the newer "standard" fast execution mode, a deterministic local scoring function) ranks the memos by relevance, reasoning quality, and constraint satisfaction. |
| 4 | **Hypothesize** | A "Causal Architect" agent proposes a directed acyclic graph (DAG) — e.g., `Patch_Applied → Lateral_Movement`, with `Asset_Criticality` as a candidate confounder. |
| 5 | **Compile Evidence** | The deterministic compiler pulls real evidence records — actual SIEM rows, actual CVE records — tagged with real `source_type` values, and normalizes them into a clean statistical dataset. Anything the LLM might have generated itself is rejected here, by rule 1 above. |
| 6 | **Estimate** | If (and only if) the data quality gates pass, DoWhy computes an Average Treatment Effect (ATE) — e.g., "applying the patch is associated with a −0.31 change in lateral-movement likelihood" — with a genuine p-value from `statsmodels`, not a number the LLM invented. |
| 7 | **Validate the Graph** | The PC-algorithm causal-discovery pass independently checks whether `Asset_Criticality` really behaves like a confounder in the actual data, or whether that edge should be pruned. |
| 8 | **Reason** | A deterministic reasoning layer looks for anomalies in the whole picture and drafts recommended next actions — not another LLM call, by design (this is one of the project's own stated "hard questions and answers": *"why isn't the reasoning layer another LLM?"* — because a second LLM checking a first LLM's work is not independent verification, it's the same failure mode twice). |
| 9 | **Learn** | A reinforcement-learning loop updates policy priors — e.g., if "Evidence & Causal Measurement Analyst" personas have historically produced higher-quality memos for RDP-related incidents, that gets reflected in future agent configuration for similar incidents. |
| 10 | **Remember** | The completed investigation becomes part of a persistent 5-dimensional knowledge graph *(a separate, pre-existing system — see the callout below)*. |

**This PR's contribution sits conceptually alongside steps 1 and 10**: the new memory layer retrieves relevant *past* investigations (like this exact FIN-042 example, if a similar one existed) *before* step 1 even begins, and persists the finished investigation for future retrieval *after* step 9 completes — regardless of whether the fast or full pipeline was used. See [[02 - The Persistent Memory Layer, Component by Component]] for the precise mechanics.

> [!warning] Two different "memory" systems exist in this codebase — don't confuse them.
> - The **5D Spatiotemporal Knowledge Graph** (`graph_5d.py`) already existed before this PR. It's a `(subject, predicate, object, time, location)` graph that powers reinforcement learning, historical replay, and visualization *within* the artifacts of investigations that have run through this system, primarily for the RL/policy-learning loop.
> - The **Persistent Semantic Memory Layer** (this PR's subject) is new, and lives in Supabase rather than the local SQLite/graph database. It works *across* runs in a way the 5D graph alone was never designed for — it's what lets the system recognize "this looks like the incident from three weeks ago" using semantic (meaning-based) similarity search, not just structural graph traversal.
> See [[02 - The Persistent Memory Layer, Component by Component]] for full detail on the new system, and how the two systems relate.

## Why "Agent Swarm," Not "One Agent" — And Why It Evolves

CausalOps deliberately uses a *hierarchy* of specialized agents rather than one large LLM call answering everything at once:

```
Orchestrator (decomposes the incident)
   ├── Parent Agent 1 (e.g. "Rapid SOC Triage Lead")
   │      ├── Child Agent 1a (e.g. "Containment & Blast Radius Analyst")
   │      └── Child Agent 1b (e.g. "Evidence & Causal Measurement Analyst")
   └── Parent Agent 2 (if the orchestrator decided a second track was warranted)
          └── Child Agent 2a
```

Each child agent writes exactly one decision memo, from one narrow perspective. The evaluator then ranks these memos rather than trusting any single agent's confidence in its own answer — a form of the same "don't let something grade its own homework" principle that governs evidence, applied to agent output itself.

**Agents also evolve, and this is not an LLM-driven process either.** A deterministic **steady-state island evolutionary algorithm** (tournament selection, crossover, bounded mutation, periodic migration between "islands" of agent configurations) tunes each agent's policy — traits like `evidence_weight`, `causal_focus`, `temporal_awareness`, `risk_aversion`, `coordination` — across runs. Reinforcement learning (a model-based value-iteration approach, computing a Stackelberg-style leader/follower response between parent and child policy tiers) further refines these policies based on how well past investigations' strategies actually performed, feeding a shared "meta-prior" back down into future agent configurations. None of this tuning is done by asking an LLM "how should agents behave differently" — it's computed.

## The Execution Path That Actually Runs in Production — A Detail Worth Getting Right

There are two versions of the coordination logic in this codebase, and confusing them is a common and costly mistake for anyone new to the project:

- **`src/graph.py`** — a LangGraph state-graph implementation. **This is reference-only.** Its own module docstring explicitly says it is deprecated for execution. It's useful for understanding the conceptual topology of the pipeline, but nothing in production actually runs through it.
- **`src/coordinator/runner.py::execute_run()`** — the **real** execution path: an async state machine that persists progress to SQLite (`data/runs.db`) between every single phase, so a run's state survives a process restart mid-investigation.

This distinction mattered directly for the memory-layer work: the new `memory_retrieve`/`memory_write` phases were added to `coordinator/runner.py`, not `graph.py` — adding them only to the reference implementation would have produced code that looked correct in review but did nothing in the actual running system.

## The Technology Stack, With the "Why" Behind Each Choice

| Layer | Technology | Why this, specifically |
|---|---|---|
| Chat LLM | NVIDIA Nemotron (primary) → Gemini (fallback) → Azure OpenAI (final fallback) | A three-tier fallback chain, checked in `src/llm.py`'s `get_llm()` function in priority order — if the primary provider's key isn't set, it silently falls through, so the system degrades gracefully rather than hard-failing on a single provider outage |
| Causal inference | DoWhy + statsmodels | DoWhy gives a principled causal-inference framework (identification, estimation, refutation); statsmodels is used *independently* to compute the p-value via OLS, so the p-value isn't just DoWhy's own internal number — it's a second, separately-computed statistic |
| Causal discovery | PC algorithm (conditional independence testing) | A well-established, non-LLM algorithm for inferring which edges in a proposed causal graph are actually statistically defensible given the data |
| Event bus | Kafka (via Redpanda) | Decouples the coordinator from worker processes, allowing horizontal scaling of the "spawn" workload (dispatching parent/child agent tasks) independently of the API |
| Run persistence | SQLite (`data/runs.db`) | Chosen deliberately for local/single-node deployments; the codebase's own `RunStore`/`WorkerExecutor` interfaces are designed to allow a future swap to Redis/Postgres without changing calling code |
| **Memory layer (this PR)** | **Supabase (Postgres + pgvector) + Gemini embeddings + standalone MCP server** | See [[02 - The Persistent Memory Layer, Component by Component]] for the full rationale — briefly, Postgres+pgvector avoids introducing an entirely separate vector-database technology when a well-understood relational database extension does the job |
| Frontend | React 19 + TanStack Start | A modern, server-side-rendering-capable React framework |
| Backend | FastAPI | Async-native Python web framework, matching the async-throughout design of the coordinator |

## A Short Glossary (For Anyone New to This Domain)

- **ATE (Average Treatment Effect)** — the statistical estimate of how much a "treatment" (e.g., applying a patch) causally affects an "outcome" (e.g., likelihood of lateral movement), as opposed to a mere correlation.
- **DAG (Directed Acyclic Graph)** — a graph with directional edges and no cycles, used here to represent a hypothesized causal structure (X causes Y, Y causes Z, etc., with no loops).
- **Confounder** — a variable that influences both the treatment and the outcome, and which — if not accounted for — can make an estimate misleadingly attribute an effect to the treatment that's actually caused by the confounder.
- **Refutation test** — a check DoWhy runs to see whether its own estimate holds up under perturbation (e.g., adding a random common cause, or subsetting the data) — a sanity check on the estimate itself, not just on whether one was produced.
- **DoWhy** — the open-source causal-inference Python library CausalOps uses for identification, estimation, and refutation.
- **MITRE ATT&CK technique ID** — a standardized identifier (like `T1021.001`, "Remote Desktop Protocol") for a specific adversary tactic, from the MITRE ATT&CK knowledge base — the industry-standard taxonomy this project uses to tag techniques.

## Where to Go Next

Now that you know what CausalOps *is* and how a single incident flows through it end to end, [[02 - The Persistent Memory Layer, Component by Component]] explains exactly what this PR added to it — with code.

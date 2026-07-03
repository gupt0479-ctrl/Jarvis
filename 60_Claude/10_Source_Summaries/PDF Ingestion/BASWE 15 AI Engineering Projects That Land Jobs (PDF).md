---
type: input
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - summary
notes:
  - "[[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]]"
  - "[[Tracker]]"
source_url: 60_Claude/05_Clippings/PDFs/BASWE__15_AI_Engineering_Projects_Guide.docx.pdf
source_note: "[[BASWE__15_AI_Engineering_Projects_Guide.docx.pdf]]"
input_kind: pdf
track: career
---
# 15 AI Engineering Projects That Actually Land Jobs — Summary
**Source:** `60_Claude/05_Clippings/PDFs/BASWE__15_AI_Engineering_Projects_Guide.docx.pdf`
**Ingested:** 2026-07-03
**Pages:** 55
## Source
A build-guide from **BASWE / AiEngineerAccelerator™**: fifteen portfolio-project blueprints for mid-level software engineers moving into AI engineering. Each is an **architectural blueprint** (not a tutorial), scoped to **12–14 days at 2–3 h/day**, meant to be built independently so the implementation decisions become interview material. Full per-phase build steps and code live in the PDF; this note captures every project's what/why/stack and phase structure so the catalog is usable without reopening it.
## Key Claims
- **Build 2–3 deeply, not all 15** — "two deep, polished projects beat five shallow ones every time"
- Every project solves a **real production operational problem**, deliberately **not** "I called an LLM API and deployed a chatbot"
- The design leverages **existing SWE skills** (Docker, CI/CD, APIs, databases) as a **structural advantage** for a career switcher
- The 15 span the actual dimensions AI teams hire for: **evaluation, cost optimization, observability, CI/CD integration, retrieval, fine-tuning, multi-agent orchestration**
- The recurring winning pattern across projects: **hand-built golden dataset → multi-dimensional scoring → diff/regression detection → feedback loop that grows the dataset from failures** — "evaluation quality is bounded by data quality"
- Two portfolio proofs matter more than the code: a **3-minute Loom walkthrough** and a **case study that leads with a number** ("reduced cost by X%", "Y% faithfulness")
- LLM-as-judge, structured output (Pydantic/instructor), and Docker-compose appear in nearly every stack — these are the assumed baseline
## Full Content
### Project 1 — Model Regression Detection System
==A CI/CD pipeline that tests any LLM feature against a golden dataset on every prompt/model change, detects quality regressions, and Slack-alerts before bad output ships.==
*Why it lands:* every team ships prompt changes blind; this proves you think about what happens after deployment. *Stack:* Python, OpenAI, RAGAS/DeepEval, SQLite, Slack webhooks, GitHub Actions, Streamlit, Docker. *Phases:* define the LLM feature (versioned YAML prompts) → hand-build a 50–100 case golden dataset with deliberate edge cases → multi-dimensional eval engine with run-to-run diffing + significance thresholds (warn >3%, critical >8%) → HTML diff report + Slack alerts + slow-drift detection (7-run moving average) → wire into GitHub Actions on `/prompts` changes, block merge on critical regressions → Loom + blog post.
> [!TIP] Interview lead: talk about how you built the golden dataset (hand-labeled, expanded from failures) — signals you understand eval quality is bounded by data quality.
### Project 2 — LLM Cost Autopilot
==A routing layer that classifies each request's complexity and sends it to the cheapest model that can handle it, with an async quality-verification loop that auto-escalates failures.==
*Why it lands:* signals you understand AI engineering as a business problem — the junior/senior gap. *Stack:* Python, OpenAI+Anthropic+Ollama, FastAPI, scikit-learn classifier, LLM-as-judge, SQLite, Streamlit/Grafana, Docker. *Phases:* unified model interface (ModelConfig registry with real pricing) → complexity classifier (3 tiers, 200+ hand-labeled prompts, ≥80% accuracy is fine for V1) → async quality verifier that re-checks cheap-model output against the top-tier model, auto-escalates, and feeds failures back to retrain the classifier weekly → logging + cost dashboard with the "you saved $X / X% reduction" money-shot metric → FastAPI `/v1/completions` where the router picks the model → load test 500–1,000 prompts, write the case study.
### Project 3 — Failure Forensics Tool for AI Pipelines
==An observability layer for multi-step pipelines that traces every step and answers "where did this go wrong?" via backward root-cause analysis — a mini LangSmith/Braintrust.==
*Why it lands:* articulating why observability matters for AI is a senior signal. *Stack:* Python, LangChain/custom chain, OpenTelemetry spans, SQLite+JSON traces, React/Streamlit, Docker. *Phases:* 4-step pipeline (intake→extraction→classification→summarization) with injected failure modes → tracing layer (Trace/Span objects, per-step confidence scores, decorator instrumentation) → backward trace analyzer with a failure taxonomy (extraction hallucination, misclassification, propagation error, prompt failure, context loss) and an evidence chain → visual trace explorer (color-coded nodes, diff view, flagging button) → feedback-to-eval loop (flags auto-become test cases) + failure analytics → demo 50 docs with 8–10 planted failures.
### Project 4 — Self-Healing Technical Documentation
==A GitHub Action that detects when code changes make docs stale, and either auto-PRs corrected docs or flags them for review.==
*Why it lands:* lives inside CI/CD not a Streamlit demo; solves a universal pain; demonstrates the full stack (embeddings→retrieval→generation→deployment) as an installable tool. *Stack:* Python/TS, OpenAI text-embedding-3-small, ChromaDB, GPT-4o/Claude, PyGithub, GitHub Actions, Docker. *Phases:* code-to-docs mapping (parse code + docs into chunks, link graph via heuristics + embedding similarity) → change detection on git diff (filter to meaningful changes, LLM confirms staleness) → doc repair engine (targeted rewrites preserving style, confidence-gated auto-fix vs TODO draft) → package as a GitHub Action with PR workflow + summary comment → test on a forked real project (FastAPI/Pydantic), measure TP/FP/FN → publish to the Actions marketplace.
### Project 5 — LLM Output Arbitration System
==A multi-agent pipeline where three specialized critic models (accuracy, logic, completeness) independently evaluate an output and an adjudicator resolves their disagreements into one confidence-scored verdict.==
*Why it lands:* builds a system that catches bad answers instead of generating answers — the evaluation mindset teams rarely see. *Stack:* Python, LangGraph, OpenAI+Anthropic+Ollama, Pydantic+instructor, SQLite, FastAPI, React/Streamlit. *Phases:* critic architecture (3 roles, structured critique format, **deliberately different model per critic** so they don't share blind spots) → LangGraph orchestration (parallel fan-out/fan-in, disagreement detector, graceful degradation on critic failure) → adjudicator agent (evidence-based conflict resolution, final 1–10 verdict with dismissed-flag reasoning) → verdict explorer UI (inline annotations, critic comparison panel, batch mode) → FastAPI + critic-behavior analytics → planted test cases across error types.
### Project 6 — RAG Pipeline with Hybrid Search Over Internal Docs
==Production RAG with dense + sparse (BM25) retrieval fused via RRF, a reranker, grounded generation with inline citations, and citation verification.==
*Why it lands:* RAG is the single most-requested AI-eng skill, but most candidates ship a toy single-PDF demo; hybrid retrieval + chunking decisions + citation verification is the production differentiator. *Stack:* Python, text-embedding-3-small, ChromaDB/Qdrant, rank_bm25, GPT-4o/Claude, LangChain splitters, FastAPI, Docker. *Phases:* ingestion + **3 switchable chunking strategies** (fixed+overlap, header-recursive, semantic) + dedup → hybrid retrieval (dense top-k + BM25 + RRF fusion + cross-encoder reranker) → grounded generation with bracketed citations + per-citation LLM-as-judge verification + confidence scorer + graceful "I don't know" → eval framework (50+ golden Q&A incl. multi-hop and no-answer cases, faithfulness/citation-accuracy metrics, chunking-strategy comparison) → API + dashboard with hybrid-vs-dense toggle.
### Project 7 — Semantic Caching Layer for LLM APIs
==Middleware that detects semantically similar prior requests and serves cached responses, cutting latency to near-zero and cost 30–60%.==
*Why it lands:* infrastructure efficiency with obvious ROI. *Stack:* Python, text-embedding-3-small, Redis+RedisVL/Qdrant, FastAPI, Prometheus+Grafana, Docker. *Phases:* cache index + similarity engine (embed prompts, cosine-threshold 0.95 = hit, key includes system-prompt hash + temperature + model to prevent cross-contamination) → **drop-in OpenAI-compatible proxy** (change base URL, zero code changes; streaming buffered-and-cached) → cache policies (TTL tiers by content, invalidation on prompt/model change, similarity-threshold tuner, adaptive per-task thresholds) → Prometheus/Grafana with near-miss analyzer → 2,000-request load test.
### Project 8 — Text-to-SQL with Guardrails and Hallucination Detection
==NL→SQL against a real DB, with guardrails blocking destructive ops, back-translation verification, and confidence scoring.==
*Why it lands:* high-value, notoriously hard; guardrails + hallucination detection proves you can ship AI a compliance team approves. *Stack:* Python, GPT-4o/Claude, PostgreSQL/DuckDB (not SQLite toy), SQLAlchemy introspection, custom guardrail middleware, FastAPI, Docker. *Phases:* schema-aware prompt engine (auto-introspect, filter tables by embedding relevance, explicit ambiguity clarification) → generation + safety layer (block DDL/DML, enforce LIMIT, subquery-depth cap, EXPLAIN row-scan block, read-only sandboxed rollback transaction, SELECT-only DB user) → hallucination detection (SQL→question back-translation, result sanity checks, **independent multi-query agreement** as correctness signal) → interface + feedback loop → eval suite → "zero unsafe queries executed" headline. Lead with safety, not accuracy.
### Project 9 — Prompt Versioning and A/B Testing Platform
==Treats prompts as versioned artifacts, splits traffic across variants, measures custom metrics, and declares statistically significant winners — feature-flag rigor for prompts.==
*Why it lands:* shows prompt engineering at scale is an experimentation problem, not guessing. *Stack:* Python, OpenAI/Anthropic, PostgreSQL, scipy.stats, FastAPI, React/Streamlit, Docker. *Phases:* prompt registry ("git for prompts": versions, diffs, rollback by activating a version, template variables) → experiment engine (traffic splitter with consistent hashing, auto-stop guardrails on error/quality) → metrics + analysis (pluggable collectors, two-sample t-test / Mann-Whitney, significance + minimum detectable effect, auto winner declaration with 24h hold) → management UI + audit log ("who changed the prompt that broke it Tuesday?").
### Project 10 — Fine-Tuning Pipeline with LoRA
==End-to-end LoRA fine-tuning of an open base model on a domain dataset, benchmarked head-to-head against the base, with full experiment tracking and reproducibility.==
*Why it lands:* where AI-eng meets ML-eng; a reproducible pipeline with eval beats a one-off notebook. *Stack:* Python, Llama-3-8B/Mistral-7B, HuggingFace PEFT+TRL, Unsloth/QLoRA, lm-eval-harness, W&B/MLflow, vLLM/Ollama. *Phases:* training dataset (narrow measurable task, 500–2,000 instruction-format examples, sacred 80/10/10 split, 30–50 handcrafted eval examples) → training pipeline (LoRA on q_proj/v_proj, rank 16 / alpha 2×rank / dropout 0.05, QLoRA on consumer GPU, W&B logging, early stopping, hyperparameter sweep over rank/LR/epochs) → evaluate base-vs-fine-tuned on the same benchmark + LLM-as-judge + **catastrophic forgetting check** → inference (export the tiny <100MB adapter, serve on vLLM/Ollama, A/B endpoint) → experiment report + "X%→Y% while keeping Z% general capability" headline.
> [!NOTE] The when-to-fine-tune framing (vs few-shot or RAG) is itself an interview point — the report must justify why fine-tuning was the right tool.
### Project 11 — LLM Gateway with Rate Limiting, Fallback Routing, Observability
==A production gateway in front of all org LLM calls: per-team rate limits and budgets, automatic provider fallback on outage/rate-limit, unified observability.==
*Why it lands:* pure infrastructure engineering applied to AI — leads with SWE strengths. *Stack:* Python/Go, FastAPI, Redis token-bucket, YAML hot-reload config, OpenTelemetry+Prometheus, Grafana, Docker. *Phases:* unified proxy (provider abstraction, team-key auth/routing, streaming passthrough, request enrichment for central policy) → rate limiting + budget caps (atomic distributed token buckets, 429 + Retry-After, dollar budgets with 80% warning, tiered priority) → fallback routing (health checks, automatic failover to alternate provider, circuit breaker) → OpenTelemetry tracing + Grafana across every call → containerize + load test.
### Project 12 — AI Feature Flag System with Gradual Rollout and Quality Monitoring
==Feature flags built for AI features (where "working" is a quality gradient, not binary): percentage rollouts, live quality monitoring, automatic rollback below a threshold.==
*Why it lands:* proves AI features need different operational patterns than traditional code. *Stack:* Python, PostgreSQL+Redis, custom+LLM-as-judge quality eval, Python client SDK, React/Streamlit, Slack webhooks, Docker. Core idea: tie the flag's rollout percentage to a live quality score and auto-roll-back on degradation, with a drop-in SDK for apps.
### Project 13 — Automated Eval Dataset Generator from Production Logs
==Mines production LLM logs, clusters interactions to find edge/failure cases, and auto-converts them into labeled eval test cases — solving the eval *data supply* problem.==
*Why it lands:* the hardest part of eval is the dataset, not the harness; turning traffic into eval data is a force multiplier. *Stack:* Python, PostgreSQL/ClickHouse, scikit-learn+HDBSCAN clustering, GPT-4o/Claude labeling, custom eval runner, Streamlit, Cron/Celery, Docker.
### Project 14 — Multi-Modal Document Processor with OCR, LLM Extraction, Validation
==Any-format doc → OCR → LLM structured extraction → business-rule validation, with a human-in-the-loop review UI for low-confidence results.==
*Why it lands:* document processing is one of the largest enterprise AI categories; touches vision + NLU + production engineering. *Stack:* Python, Tesseract+EasyOCR, GPT-4o-vision/Claude, GPT-4o+instructor, Pydantic validation, Celery+Redis queue, React/Streamlit, Docker.
### Project 15 — Agent Orchestration System with Tool Use, Memory, Human-in-the-Loop
==A supervisor agent decomposes tasks, delegates to specialized tool-using agents, keeps persistent memory, and escalates to a human when confidence is low — with full decision observability.==
*Why it lands:* agents are the frontier and most candidate projects are single-agent toys; multi-agent + real tool use + persistent memory + HITL escalation proves you can architect autonomous systems. *Stack:* Python, LangGraph, OpenAI+Anthropic, custom+MCP tools, PostgreSQL+ChromaDB (short-term + semantic long-term memory), Redis+Celery, React/Streamlit, Docker.
## Why It Matters
This is the concrete project menu for the exact bar the [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] guide sets ("3 deployed projects = mid-level interviews"), and several map straight onto vault work already in flight: Project 5 (multi-agent critics) and Project 15 (agent orchestration + MCP) are literally what CausalOps and the Jarvis agent layer are; Project 6 (hybrid RAG + citations) is the jarvis-memory semantic-search roadmap; Project 10 (LoRA + eval) is the CSCI-2033/ML track applied. For the Bangalore flagship loop, the right move is picking **one** (Project 6 or 15 leverage the most existing work) and building it to the "deployed + evaluated + tested + Loom + case-study-with-a-number" standard, not sampling several. The catalog's real lesson is the repeated pattern — golden dataset → scoring → regression diff → failure-fed feedback loop — which is the same discipline the vault's own eval-less skills lack.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/BASWE__15_AI_Engineering_Projects_Guide.docx.pdf`
- [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] — the market context; this is the project menu for that roadmap's Step 5
- [[Tracker]] — internship pipeline these portfolio pieces feed
- [[Claude OS]] — CausalOps (≈Project 5/15) and jarvis-memory (≈Project 6) already exist here
- [[DeepThinksFinance AI Portfolio Optimizer (PDF)]] — a comparable full-stack "deployed + tested" build in the trading domain
## Open Questions
- [ ] Which single project best reuses existing work — Project 6 (RAG, feeds jarvis-memory) or Project 15 (agents, feeds CausalOps)?
- [ ] The guide targets 3–5-year SWEs; which projects are realistically shippable by a student in one Bangalore week vs which need the full 12–14 days?
- [ ] Can Project 1 (regression detection) be turned inward as the missing eval layer for the Jarvis writing skills?
## Flashcards
#cards/career
What's the core advice on how many of the 15 projects to build?::Build **2–3 exceptionally well**, not all 15 — "two deep, polished projects beat five shallow ones every time."
What single pattern recurs across the strongest projects in this guide?::**Hand-built golden dataset → multi-dimensional scoring → run-to-run regression diff → feedback loop that grows the dataset from failures** — because eval quality is bounded by data quality.
Why does the arbitration project (5) assign a different LLM to each critic?::So the critics **don't share blind spots** — disagreement between different models is the most valuable signal; same-model critics would agree on the same mistakes.
In the text-to-SQL project, what should the case study lead with, and why?::**Safety** ("blocks 100% of destructive operations"), not accuracy — companies care more about not breaking things than about accuracy percentages.
What are the two portfolio proofs the guide says matter more than the code?::A **3-minute Loom walkthrough** and a **case study that leads with a number** (cost reduction %, faithfulness %, accuracy delta).
What makes the semantic cache (7) and cost autopilot (2) "drop-in"?::They mirror the **OpenAI API contract**, so an app switches to them by **changing only the base URL** — zero code changes.

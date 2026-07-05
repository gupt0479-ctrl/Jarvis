---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "I am currently updating my linkedin profile completely."
started_at: 2026-06-30T17:06:00
ended_at: 2026-06-30T17:09:33
project: Cowork
status: raw
session_id: 40d5e7fa-b985-4cd2-82f7-a330b77a44be
tags:
  - input
  - ai-conversation
  - claude-code
---

# I am currently updating my linkedin profile completely.

## You

I am currently updating my linkedin profile completely. I want you to analyze all the projects I have worked on - displayed on my portfolio(https://anantgupta.dev) and written in this vault. Provide me with descriptions, skills for each project that I will be listing here. The maximum charachters is 2000 so keep it tight just like the portfolio. Focus on what skills to be displayed upon reading through the sanity skills section of the portfolio. Provide me with professional and clean descriptions.

## Claude

Now let me resolve the skill references to get their names:

I have everything I need. Let me now compile the LinkedIn entries.

Here are all 9 projects with LinkedIn-ready descriptions and skills. I pulled the taglines, summaries, and tech stacks directly from your Sanity CMS and wrote descriptions around what makes each project technically interesting.

---

## 1. Orby — Portfolio Agent
**Skills:** Next.js · TypeScript · Redis · LLM APIs · Prompt Engineering · Agent Systems · API Security

> Built an adversarially-hardened AI agent that powers my portfolio. Orby is a single-route agent runtime that answers visitor questions exclusively from real portfolio content — it cannot be jailbroken, misled, or used off-topic.
>
> The system is secured with origin-locking, HMAC-signed cookies, and per-IP rate limiting via Redis to defend against prompt-flooding. Strict system prompt boundaries and output filtering keep the agent on-topic at inference time. A promptfoo eval suite gates every deployment — the agent has to pass adversarial prompt tests before it ships.
>
> Built on Next.js with TypeScript throughout. The architecture demonstrates how to ship LLM-powered features in production without sacrificing safety or predictability.

*(~570 chars)*

---

## 2. Jarvis — Personal Knowledge OS
**Skills:** Python · Linux · Git · Prompt Engineering · Agent Systems · MCP (Model Context Protocol) · Knowledge Management

> A personal knowledge operating system built on Obsidian where structured notes are the source of truth for AI-driven software development. The vault doesn't just document projects — it builds them.
>
> Built custom MCP servers connecting Claude to Obsidian, the filesystem, GitHub, and external tools. Designed agent workflows for daily planning, session continuity, note distillation, and vault maintenance. A semantic retrieval layer maintains persistent context across AI sessions so no work is repeated.
>
> The same system drove the development of BOOM, Arc, and CasualOps — design notes fed into agents, which executed multi-step engineering tasks. An experiment in building intelligence infrastructure that compounds over time.

*(~680 chars)*

---

## 3. BOOM — Burst & Outburst Observations Monitor
**Skills:** Rust · Python · MongoDB · Redis · Docker · REST API Design · Linux · Data Pipelines

> Production Rust infrastructure for the BOOM astronomical alert broker at the University of Minnesota (Prof. Coughlin). The system ingests, enriches, and filters real-time alert streams from the Zwicky Transient Facility (ZTF), which surveys the night sky nightly for transient events — supernovae, variable stars, near-Earth objects.
>
> Built a modular pipeline with ingestion workers, enrichment classifiers, and filter workers managed by a central scheduler. Redis handles high-speed inter-service messaging. MongoDB stores structured alert records for cross-session retrieval. The full stack runs in Docker on Linux research infrastructure.
>
> Also built observability tooling to monitor pipeline health and alert processing rates. Processes large-scale nightly survey volumes in a live astrophysics research environment.

*(~715 chars)*

---

## 4. CasualOps
**Skills:** Python · LangGraph · LLM APIs · Multi-Agent Systems · RAG · PostgreSQL · pgvector · Cybersecurity · Evaluation Frameworks

> A multi-agent SOC intelligence system built with LangGraph. An orchestrator decomposes incoming cyber incidents into structured investigation tasks, dispatching parallel parent/child agent chains to analyze different attack surfaces simultaneously.
>
> The system's core feature is a persistent semantic memory layer backed by PostgreSQL + pgvector, retrieved using exponential temporal decay — recent incidents are weighted higher, but historical patterns still surface when relevant. Specialized sub-agents handle threat classification, causal modeling, and remediation planning. A RAG pipeline grounds every agent decision in real incident data.
>
> An eval suite validates agent correctness across adversarial and ambiguous scenarios. The system improves with each incident — decomposing attacks into causal models faster and more accurately over time.

*(~735 chars)*

---

## 5. Arc — Learning Hub
**Skills:** Next.js · TypeScript · Tailwind CSS · PostgreSQL · pgvector · Drizzle ORM · RAG · LLM APIs · Three.js

> A self-directed learning platform that turns unstructured courses into structured study plans with an AI tutor layer. Most learning tools track time — Arc tracks understanding.
>
> A course ingestion pipeline scrapes and structures any course into a topic graph. Study sessions are logged with streak tracking. The RAG-based AI tutor is backed by pgvector — lessons are chunked, embedded, and retrieved by semantic similarity to surface the right context for each question. 3D visual knowledge graph components built with Three.js give spatial thinkers a different way to navigate material.
>
> Built on Next.js and TypeScript with Drizzle ORM for type-safe, schema-first data management. The retrieval quality improves as users log sessions — the more you study, the better the tutor gets at predicting what you need next.

*(~735 chars)*

---

## 6. TradingView — Personal Market Analyzer
**Skills:** Next.js · TypeScript · Python · PostgreSQL · LLM APIs · Prompt Engineering · Data Pipelines

> A personal investing research tool that enforces a hard boundary between AI-generated analysis and deterministic financial data. Most AI investing tools blur this line — this one doesn't.
>
> The system includes a portfolio tracker, watchlist, and strategy lab for backtesting investment theses. An AI evidence card feed generates structured research cards tagged with one of four verdicts — ACCUMULATE, HOLD, WATCH, or AVOID — each backed by cited evidence from the underlying data. The AI is strictly advisory and cannot touch portfolio records.
>
> A Python pipeline handles market data ingestion, normalization, and PostgreSQL storage. The deliberate AI boundary makes every recommendation auditable — you can always trace it back to the data that produced it.

*(~670 chars)*

---

## 7. Resq
**Skills:** Next.js · React · TypeScript · PostgreSQL · Drizzle ORM · Zod · LLM APIs · Audit Systems

> A cash flow forecasting tool for early-stage founders that keeps AI strictly out of the math. Resq generates deterministic 13-week cash runway projections — zero LLM involvement in any financial calculation.
>
> A typed service layer with Zod validation enforces schema contracts at every data boundary. A SHA-256 hash-chained audit log makes every forecast version tamper-evident. Operational live/degraded modes via a TinyFish state machine ensure the system honestly reports its own reliability — degraded mode flags when data freshness drops below threshold.
>
> The LLM layer handles only natural language summaries and Q&A on top of already-computed data. Drizzle ORM + PostgreSQL manage schema with full migration support. A CFO workspace a non-technical founder can trust: the math is deterministic, the audit trail is cryptographic, and the AI is clearly labeled advisory.

*(~775 chars)*

---

## 8. OpsPilot *(Hackathon)*
**Skills:** Next.js · React · TypeScript · PostgreSQL · Zod · LLM APIs · Webhook Design · System Design

> Hackathon project: a restaurant operations dashboard connecting the full ops workflow while keeping AI advisory and money flows deterministic.
>
> Built the end-to-end pipeline: reservation → invoice → payment → finance ledger → review analysis → recovery recommendation. Shipped idempotent mark-paid flows to prevent double-processing under network failures, and webhook ingestion with event deduplication so payment events are processed exactly once. A full migration and seed stack ensures the system starts from a verified, testable state.
>
> The AI layer analyzes customer reviews and surfaces operational recovery actions — it advises but never touches financial records. Zod validation enforces type contracts across every service boundary. The core design principle: AI advises, deterministic services own the money.

*(~680 chars)*

---

## 9. SafeReach *(Hackathon)*
**Skills:** React · Next.js · TypeScript · Python · LLM APIs · Web Accessibility (WCAG) · Prompt Engineering

> Hackathon project: an emergency alert and disaster-preparedness tool designed for people with disabilities. Most emergency systems assume full physical and cognitive mobility — SafeReach doesn't.
>
> Real-time disaster alerts are filtered by the user's registered disability profile. A visit-prep flow generates AI accessibility assessments and risk ratings before users access a location. An AI translation layer converts generic emergency protocols (evacuate, shelter-in-place) into plain-language, disability-specific instructions.
>
> The UI is accessibility-first: screen reader compatible, high-contrast, large-text defaults, minimal interaction required under stress. A Python backend ingests public emergency data feeds and handles profile matching. Scoped to one defensible, complete flow — from alert receipt to actionable instruction — shipped within hackathon constraints.

*(~720 chars)*

---

All descriptions are well under 2000 characters, tight, and focused on the technical decisions that make each project defensible. A few notes:

- **Resq and OpsPilot** lead with the AI boundary principle since that's your strongest differentiator across projects — you're clearly thinking about where AI belongs in a system.
- **BOOM** is your most production-credible entry — lean into the "live research environment" framing on LinkedIn.
- For the hackathon projects (SafeReach, OpsPilot), the *(Hackathon)* tag signals context without downplaying the engineering.

*Tools used: ToolSearch, mcp__workspace__web_fetch, TaskCreate, mcp__1e8f8959-e665-4a1c-8e14-8b3b3020e53f__list_projects, mcp__jarvis__search_simple, mcp__1e8f8959-e665-4a1c-8e14-8b3b3020e53f__query_documents, mcp__1e8f8959-e665-4a1c-8e14-8b3b3020e53f__get_schema, TaskUpdate*



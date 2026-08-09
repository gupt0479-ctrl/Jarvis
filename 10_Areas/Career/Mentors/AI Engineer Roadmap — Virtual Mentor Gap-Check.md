---
type: evergreen
status: sprout
created: 2026-07-29
updated: 2026-07-29
tags:
  - evergreen
  - career
notes:
  - "[[AI Engineer Roadmap — roadmap.sh (web)]]"
  - "[[Engineer Edge Roadmap]]"
next:
---
# AI Engineer Roadmap — Virtual Mentor Gap-Check
## Why This Lives Here, Distinct From Mentorship and Networking
[[60_Claude/20_Distilled_Notes/Mentorship and Networking]] covers the CSE Mentor Program — a real human relationship (mentor Ahnaf), built through demonstrated execution over 6+ months, producing warm introductions. This note covers something genuinely different: **roadmap.sh's AI Engineer roadmap used as a self-directed gap-check, not a course to complete or a person to talk to.** Checked before writing anything: no overlap in content between the two — one is relationship-building, this is a checklist. Per [[00_Execution]], this is why the two stay as separate notes rather than being folded together.
## How To Use It
==Not a curriculum to work through linearly — a checklist to run before starting a new project phase, to see which prerequisite skills are actually missing.== Per [[AI Engineer Roadmap — roadmap.sh (web)]], the roadmap's spine is: LLM fundamentals → prompt/context engineering → embeddings + vector DBs → RAG → AI agents (+ MCP) → multimodal → **evaluation & observability**.
**The gap-check move:** before committing real hours to a new AI/ML project phase, walk the spine and ask "does my current work already evidence this section, or is this a real gap?" The source summary already ran this check once: the vault already touches most of the spine (LLMs via Claude, MCP servers, agents in CausalOps/Jarvis, RAG in jarvis-memory) — the clearest surfaced gap is **evaluation & observability** (LangSmith/Langfuse/RAGAS/DeepEval, deterministic vs. model-based evals), which lines up exactly with the same eval gap already being closed via [[Code Review & Eval Gap|Semgrep + promptfoo]] and [[20_Progress/Projects/CS/Portfolio/nextgen-chatbot/10 - Orby Golden Eval Dataset (Grounding Cases)|Orby's golden dataset]].
## When To Actually Consult It
- Before starting a new BASWE-style portfolio project — check which roadmap section it maps to, and whether that section is a strength or a genuine gap first.
- Before scoping a hackathon idea (per [[10_Areas/Career/Hackathon/Hackathons]]) that leans AI/LLM — confirm the idea doesn't require a roadmap section with zero vault evidence yet.
- Not before every coding session — this is a phase-boundary check, not a daily reference.
## Evidence
- [[AI Engineer Roadmap — roadmap.sh (web)]] — the full roadmap spine and the gap-check already run once
- [[60_Claude/20_Distilled_Notes/Mentorship and Networking]] — the distinct, human-relationship note this doesn't duplicate
- [[Engineer Edge Roadmap]] — where the evaluation/observability gap this roadmap surfaces is already being closed
- [[00_Execution]] — the resolved verdict this note executes

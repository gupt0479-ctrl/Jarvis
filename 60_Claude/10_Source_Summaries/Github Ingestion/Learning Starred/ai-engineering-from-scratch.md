---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - learning
source_url: https://github.com/rohitg00/ai-engineering-from-scratch
notes:
  - "[[40_Resources/CS/Repos]]"
---
# AI Engineering From Scratch

**GitHub:** [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | **Stars:** 36.6k | **Updated:** June 2026

## What it is
A 20-phase, 280+ lesson structured curriculum (~290 hours) from "what is an LLM" through production deployment, with a ROADMAP.md as the single source of truth for phase structure. Each lesson follows a six-beat pattern (problem → concept → build → use → ship). Has a glossary, a web catalog, and Claude Code skill files (`.claude/skills/`) baked into the repo. Updated very actively (1,636 commits as of June 2026).

## How Anant uses it
Use ROADMAP.md as a gap-check tool, not as a course to complete linearly. The 20-phase structure maps the full journey from foundations to production: when you finish LLM Zoomcamp and need to identify what to learn next, open ROADMAP.md and mark off what you know — the remaining phases show gaps.

Specific phases relevant to current projects:
- Phases covering RAG and agent loops: cross-reference with LLM Zoomcamp work to find what the Zoomcamp skips.
- Phases covering fine-tuning and reasoning models: relevant when Kronos needs a specialized model.
- Production phases: check before deploying any model endpoint for TradingAgents.

The `.claude/skills/` folder is an interesting reference for how to structure Claude Code skills in the Jarvis vault.

## How to install / run it (Windows)
Browse ROADMAP.md on GitHub to get the phase map. Clone the repo to access the lesson files and skill files. No cohort — entirely self-paced. The web catalog at the repo's GitHub Pages site provides searchable access to all lessons.

## Caveats / current state
Active development (daily commits). This is a community-maintained curriculum, not an official course. The 20-phase, 290-hour estimate makes it a substantial commitment if taken end-to-end. Use it selectively (ROADMAP.md as a map, specific lessons when you need depth on a topic) rather than trying to complete all phases before building. Not a replacement for LLM Zoomcamp or ML Zoomcamp — those are more structured and have community support.

## Connects to
[[40_Resources/CS/Repos]]

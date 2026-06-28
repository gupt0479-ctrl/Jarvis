---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - projects
  - learning
source_url: https://github.com/kju4q/ai-weekend-builds
notes:
  - "[[40_Resources/CS/Repos]]"
---
# AI Weekend Builds

**GitHub:** [kju4q/ai-weekend-builds](https://github.com/kju4q/ai-weekend-builds) | **Stars:** 179 | **Updated:** May 4, 2026

## What it is
10 AI project templates (Vol 1 + Vol 2) each with a full README, starter Python/Node code, and exact prompts. Difficulty-sorted: Easy (1–3h) → Medium (5–9h) → Advanced (full day).

**Vol 1 projects:** Excalidraw MCP diagram agent, one-command web researcher, personal RAG assistant, multi-agent research crew, autonomous coding agent (reads GitHub issues, writes fixes).

**Vol 2:** 5 more (build guides, no boilerplate).

## How Anant uses it
Reference when starting a new weekend project rather than starting from blank. The multi-agent research crew (04) and autonomous coding agent (05) are the most useful templates — directly applicable to the trading project (multi-agent analyst/researcher pattern) and Jarvis (issue-driven agent). The personal RAG assistant (03) is a useful template for a local Jarvis search experiment.

Not a curriculum — pick one project, run the starter, extend it. The prompts folder per project is often more useful than the code itself.

## How to install / run it (Windows)
Requires Python and an Anthropic API key. Per project: `pip install -r requirements.txt` then follow the project's README. No Windows-specific issues noted.

## Caveats / current state
Small repo (179 stars, 1 contributor). Vol 2 has 5 more projects but no starter code — build guides only. Last updated May 2026, not actively maintained. The excalidraw MCP agent (01) requires the Excalidraw MCP server which adds setup friction.

**Verdict: yes** — scan the README table when starting a weekend project. Projects 03–05 have real reuse value.

## Connects to
- [[40_Resources/CS/Repos]]

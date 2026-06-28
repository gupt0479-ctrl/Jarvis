---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - learning
source_url: https://github.com/patchy631/ai-engineering-hub
notes:
  - "[[40_Resources/CS/Repos]]"
---
# AI Engineering Hub

**GitHub:** [patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub) | **Stars:** 36.1k | **Updated:** June 2026

## What it is
A growing collection of self-contained Jupyter notebooks (530+ commits, 200+ folders) covering individual LLM and agent engineering patterns. Each folder is one notebook covering one technique: examples include Multi-Agent deep researcher with MCP, agent with MCP memory, DeepSeek fine-tuning, RAG with various backends (Colivara, website scraping via Firecrawl), LaTeX OCR with Llama, and reasoning model construction. Not a structured curriculum — each notebook is independent.

## How Anant uses it
Do not read linearly. Use as an implementation reference when you need a working notebook for a specific technique:
- When building the TradingAgents multi-agent system: search folders named `Multi-Agent-*` and `agent-with-mcp-*` for patterns on how to wire agents to MCP servers.
- When building a reasoning layer in Kronos: look at `Build-reasoning-model` for the construction pattern.
- When adding memory to Jarvis agents: check `agent-with-mcp-memory`.
- When scraping data sources for trading signals: check `Website-to-API-with-FireCrawl`.
The repo is updated frequently (new notebooks weekly), so search by topic rather than browsing sequentially.

## How to install / run it (Windows)
Browse GitHub directly or clone to run locally. Each notebook has its own requirements. No cohort structure — just notebooks on demand.

## Caveats / current state
Quality varies across notebooks. Some are highly polished, others are rough implementation sketches. This is a reference collection, not a verified course. The MCP-related notebooks were added in late 2025 and are among the most current. Not a substitute for the structured Zoomcamp courses — use this when you need "show me the code" for a specific pattern.

## Connects to
[[40_Resources/CS/Repos]]

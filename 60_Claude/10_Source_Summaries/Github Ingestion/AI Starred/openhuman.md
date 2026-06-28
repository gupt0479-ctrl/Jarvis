---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - ai-assistant
  - personal-ai
source_url: https://github.com/tinyhumansai/openhuman
notes:
  - "[[40_Resources/CS/Repos]]"
---
# OpenHuman

**GitHub:** [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | **Stars:** ~29k | **Updated:** Active (Early Beta)

## What it is
Desktop app (Tauri/Rust, GPL license) that packages a personal AI assistant with local Obsidian-style Markdown memory vault, managed model routing, web search proxying, and agent tools. "Local + managed services" — stores memory and workspace on your machine, but the default experience uses OpenHuman-hosted backend for auth, model routing, OAuth, and web search.

## How Anant uses it
**Verdict: Jarvis competitor, not a complement. Stick with Jarvis.**

OpenHuman solves the same problem Jarvis solves (personal AI + knowledge vault) but as a packaged product rather than a custom system. The Obsidian-style memory tree that attracted your attention is architecturally similar to what you already have in Jarvis.

Comparison vs Jarvis:
- **OpenHuman:** polished GUI, zero-code setup, locked into their managed services by default, Early Beta ("rough edges"), GPL license
- **Jarvis:** fully customizable, you own every component, skills/agents you wrote, no external dependency, integrates directly with Claude Code's toolchain

The managed backend is a key caveat: OpenHuman's model routing, web search, and OAuth flows depend on tinyhumans.ai servers. Jarvis runs entirely on your machine via Claude API + Obsidian.

**Is this your personal assistant now?** No — Jarvis already fills this role with more control and a pipeline you understand. OpenHuman would mean starting over with less customization.

## How to install / run it (Windows)
Windows: download signed `.msi` from [GitHub Releases](https://github.com/tinyhumansai/openhuman/releases/latest) and run it. No terminal required.

## Caveats / current state
- Early Beta: explicitly "rough edges" per README
- GPL license: if you distribute anything built on it, GPL terms apply
- Default setup requires OpenHuman managed backend for auth + model routing — not fully offline out of the box (must configure custom API keys to go fully local)
- Rust binary: fast and native on Windows
- Active community (Discord, Reddit)
- **vs Jan:** Jan is purely offline local LLM chat, no managed services. OpenHuman is broader (memory, agents, calendar) but with managed backend dependency. Jan is more trustworthy for air-gapped local use.

## Connects to
[[40_Resources/CS/Repos]]

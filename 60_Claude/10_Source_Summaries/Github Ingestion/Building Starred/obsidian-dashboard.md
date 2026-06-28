---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - jarvis
  - obsidian
  - tooling
source_url: https://github.com/handrovermeulen/Obsidian-Dashboard
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Obsidian Dashboard (Agentic OS)

**GitHub:** [handrovermeulen/Obsidian-Dashboard](https://github.com/handrovermeulen/Obsidian-Dashboard) | **Stars:** 61 | **Updated:** May 26, 2026

## What it is
Step-by-step guide for building a custom Obsidian community plugin as a Claude Code command center. The end product: one Obsidian pane showing live project status, action queues, skill launcher tiles, calendar, news feeds, and meeting transcripts — all reading from JSON files written by headless Claude scripts.

Architecture: Obsidian plugin (Preact + TypeScript + Tailwind, bundled to `main.js`) reads `data/*.json` files. Separate headless `claude -p` scripts query MCP tools and write JSON on a schedule. The dashboard is a read-only window into vault data flows, not a live API consumer.

## How Anant uses it
The guide maps directly onto Jarvis. The skill launcher tiles are the exact mechanism for one-click `/startday`, `/closeday`, `/ingest-clipping` execution from inside Obsidian — no terminal needed. The action queue card (reads `data/action-queue.json`) could replace the manual step of running `/startday` and then reviewing recommendations.

Phases 1–5 are the actual build. Phase 3 (moodboard → Claude Design → design system) handles the visual style. Phase 7 builds cards one at a time. Phase 9 covers how `claude -p` fires skills from skill tiles.

Key detail from the guide: `claude -p` draws from a separate API credit pool, not the Max subscription. At 5–10 skill presses/day, this is negligible.

## How to install / run it (Windows)
The guide uses the Terminal community plugin inside Obsidian for the integrated CLI. Steps:
1. Obsidian → Settings → Community Plugins → search "Terminal" (Polymart) → install
2. Clone the repo for the `starter/` shell script templates
3. Follow Phase 2–5 of the README to scaffold the plugin, then Phase 7 for cards

## Caveats / current state
61 stars means it's niche but the guide is detailed and practical. The design moodboard → Claude Design flow adds effort upfront (Phase 3–4) but is optional — could skip straight to Phase 5 scaffolding with a minimal aesthetic. Calendar tab requires a separate `cc-refresh-calendar.sh` with its own dedicated MCP config (not the full server set, which causes schema conflicts).

Built by Handro Vermeulen at PRGRMMD (an AI agency). The repo is a guide, not installable code — you build the plugin from scratch following the phases. Stars are low because it was published May 2026.

**Verdict: yes** — the skill launcher tiles alone are worth implementing. Read Phases 5–9 before building anything to understand the full architecture.

## Connects to
- [[40_Resources/CS/Repos]]
- [[Jarvis OS — North Star]]

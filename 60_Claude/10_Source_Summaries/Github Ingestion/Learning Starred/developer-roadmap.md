---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - learning
source_url: https://github.com/nilbuild/developer-roadmap
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Developer Roadmap (roadmap.sh)

**GitHub:** [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | **Stars:** 358k | **Updated:** June 2026

## What it is
The source repo for roadmap.sh — an interactive site with clickable skill trees for 80+ technology tracks. Each node links to learning resources. Tracks are actively maintained with community contributions (1,500+ contributors, updated as recently as June 25 2026). The interactive web version at roadmap.sh is more useful than the GitHub README for actual navigation.

## How Anant uses it
Use roadmap.sh directly (not the GitHub repo) for gap analysis:
- **AI Engineer roadmap** (roadmap.sh/ai-engineer): check this before starting a new AI project phase to see whether there are prerequisite skills you haven't covered. Useful before starting the TradingAgents RAG layer or Kronos inference pipeline.
- **Backend roadmap** (roadmap.sh/backend): review before SWE internship interviews — it maps the CS fundamentals that backend interviewers test.
- **Data Structures and Algorithms** (roadmap.sh/datastructures-and-algorithms) + **LeetCode roadmap** (roadmap.sh/leetcode): use these to structure interview prep by topic rather than grinding randomly.
- **MLOps roadmap** (roadmap.sh/mlops): check when moving from "model works locally" to "model deployed reliably."

Do not try to complete any roadmap end-to-end. Use them as checklists: mark what you know, identify the 2–3 gaps that matter for the next concrete goal, address those.

## How to install / run it (Windows)
No install. Go to roadmap.sh, pick a track, and use the interactive progress tracker (requires free account). The GitHub repo is only useful if you want to contribute content or run the site locally.

## Caveats / current state
The roadmap.sh site has a "Claude Code Roadmap" and "AI Agents Roadmap" as of 2026 — both are new tracks added in the last year. The content quality varies by track; the Backend, Python, and Computer Science tracks are the most thoroughly vetted. Some AI-specific tracks are newer and may have shallower content.

## Connects to
[[40_Resources/CS/Repos]]

---
type: input
status: seed
created: 2026-05-28
tags:
  - github
  - claude
source_url: https://github.com/shanraisshan/claude-code-best-practice
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Claude Code Best Practice
> [!DECISION] Could be used to learn claude code workflows used in the below mentioned repos? Could these practices be copied from here? What exactly can I learn from here? Could be the first step before diving into multiple installations of repos and plugins? What does it teach me? need to be used for learning but how exactly.
> **Answer:** Yes — read this BEFORE installing anything. It's a menu, not a tutorial. Key things to extract: (1) CLAUDE.md structure patterns (how to write instructions Claude actually follows), (2) memory management patterns (what to put in memory vs. context vs. notes), (3) parallel agent spawning patterns (how to split work across background agents without collisions). Copy the agents/commands/skills sections selectively — use this repo to understand WHY the patterns in gstack/mattpocock/ECC work, then install those more targeted repos. Don't try to implement everything from here directly.

**What it is:** A GitHub Trending #1 HTML repo (55K+ stars) containing a structured collection of Claude Code best practices organized into best-practice guides, orchestration workflow documentation, and actual agents/commands/skills.

**Why it's here:** The readme signals it's more than a tutorial — it includes real Claude Code components (marked with A/C/S for agents, commands, skills) and covers the transition from "vibe coding" to agentic engineering patterns.

**Why it's not a priority:** The repo is primarily a learning and reference resource. The components it ships are best practices embedded in documentation rather than installable modules. The substantive workflow patterns (orchestration, agentic engineering) are covered more actionably by garrytan/gstack, mattpocock/skills, and addyosmani/agent-skills — which ship actual working skills rather than documented patterns. Read through once for vocabulary and framing, but don't treat it as infrastructure.

---
type: input
status: seed
created: 2026-05-28
tags:
  - github
  - claude
source_url: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
notes:
  - "[[40_Resources/CS/Repos]]"
---
# system-prompts-and-models-of-ai-tools
> [!DECISION] How exactly can each of these prompts be used?
> **Answer:** Three concrete uses: **(1) CLAUDE.md optimization** — the Claude Code system prompt shows what Claude already "knows" by default. Don't re-write instructions that duplicate it; saves tokens every session. **(2) Pattern extraction from competitors** — Cursor's system prompt has explicit error recovery rules; Devin has deployment checklists with verification steps. Extract these patterns into your own CLAUDE.md or skills. Cursor's "always read the error message fully before proposing a fix" type instructions are the most immediately usable. **(3) Guard rail understanding** — see exactly what safety constraints exist so you can write prompts that work within them rather than fighting them. Pairs with CL4R1T4S for understanding how to prompt restrained models effectively.

**What it is:** A public collection of extracted/leaked system prompts from commercial AI tools — Claude Code, Cursor, Devin, Manus, Replit, and others.

**Why it's here:** Useful for understanding how commercial coding agents are instructed, which informs writing better CLAUDE.md and skill prompts.

**Why it's not a priority:** Pure reference material — no code, no installable components. The Claude Code system prompt is available directly from Anthropic's docs. The value here is in seeing how *competitors* structure their prompts, but that's a one-time read, not something to return to repeatedly.

---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[Claude OS]]"
source_url: 60_Claude/05_Clippings/PDFs/Free Claude Cowork Skills.pdf
source_note: "[[60_Claude/05_Clippings/PDFs/Free Claude Cowork Skills.pdf]]"
input_kind: pdf
track: ai
---
# Free Claude Code Skill Libraries (380+) — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Free Claude Cowork Skills.pdf`
**Ingested:** 2026-07-04
**Pages:** 2
## Source
A pointer sheet to free, open-source GitHub libraries of Claude Code skills/commands/agents you can drop into `.claude/commands/`.
## Key Claims
- ==Skills are just `.md` files — copy them to `~/.claude/commands/` (global) or `your-project/.claude/commands/` (project), restart Claude Code, and they're available==
- **Always review a skill file before installing** — skills run inside Claude Code with full project access
- The big libraries: **Awesome Agent Skills** (380+ skills from Anthropic/Google/Vercel/Stripe/Cloudflare/Netlify + community), **Claude Command Suite** (148 slash commands + 54 agents: code review, feature creation, security audits, architecture), **Production-Ready Commands** (57 across Essentials/Full-Stack/Security/Data-ML/Infra)
- Curated lists: **Awesome Claude Code** (skills/hooks/commands/orchestrators, also a web directory at awesomeclaude.ai), **Awesome Claude Skills** (20+ incl. /brainstorm, /write-plan, /execute-plan), **Claude Code Settings** (starter kit)
## Why It Matters
A larger, community-sourced version of the everything-claude-code marketplace triage already in [[Claude OS]] — same lesson applies: **width is the disease, not the cure** (North Star Part 2). The vault already has 13 purpose-built skills; the value here is *targeted mining* against the confirmed gaps (/emerge, /challenge, /drift) and the missing eval/observability layer, not bulk-installing 380 skills. Notable overlaps with the vault's own thesis: `/write-plan` + `/execute-plan` mirror the plan-then-execute discipline, and the security-audit/code-review commands are the eval layer the Jarvis skills lack. Treat awesomeclaude.ai as a browse-before-adopt directory; install only what a named gap needs. Anti-drift note: skill shopping is weekly-slot work, not daily ops.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Free Claude Cowork Skills.pdf`
- [[Claude OS]] — the skill roster and the everything-claude-code triage this parallels
## Open Questions
- [ ] Mine Awesome Claude Skills for a real /challenge or /emerge implementation to adapt, rather than authoring from scratch?
- [ ] Is there a ready security-review/eval skill worth adopting to close the Jarvis eval gap?
## Flashcards
#cards/ai
How do you install a community Claude Code skill?::Copy the `.md` file to `~/.claude/commands/` (global) or `your-project/.claude/commands/` (project) and restart Claude Code — but **review the file first**, since skills run with full project access.
What's the right way to use a 380-skill library, given the vault's history?::**Targeted mining against named gaps** (/emerge, /challenge, eval/observability), not bulk-installing — width was the original disease per the North Star.

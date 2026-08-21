---
type: evergreen
status: sprout
created: 2026-08-20
updated: 2026-08-20
tags:
  - evergreen
  - claude-kit
  - global
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global]]"
  - "[[Daily Operations]]"
  - "[[Vault Curation]]"
next:
---
# How to Use Global
==Reach for global tooling only for something that should follow you across every project on that OS — vault upkeep, session-lifecycle habits, cross-cutting capture. If the task is specific to one project, the project's own `.claude/` (tracked in the other five Toolkit categories) is the right layer, not here.==
# WSL home
Real, live global tooling — usable from any WSL Claude Code session, this vault's own included.
## Agents
- **obsidian-architect** — invoke for a structural pass (folder logic, MOC coverage, frontmatter consistency, orphan/broken-link sweep) across the whole vault, not a single note. Opus-backed, so reserve it for a genuine audit, not a quick check.
- **obsidian-researcher** — invoke for open-ended "find everything about X across the vault" questions where the answer isn't in one obvious folder.
- **obsidian-session-archivist** — invoke to write session context/progress back into the vault from a WSL session that doesn't have this vault's own `research-distiller`/`vault-curator` pair loaded.
**Caution before reaching for any of these three:** read [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global|What Global]]'s stale-path finding first — all three still reference `10_UMN/`, `00_Inbox/Headway/`, and `50_Archive/copilot/`, none of which exist in this vault's current structure. Cross-check the folder a result lands in before trusting it; don't assume the path in the agent's own instructions is current.
## Commands
- `/obsidian-daily-review`, `/obsidian-session-review` — context-loading reviews; prefer this vault's own `/context` and `/closeday` skills when working in Jarvis specifically, since those are written against the current folder structure.
- `/second-brain-capture`, `/second-brain-compress`, `/second-brain-graduate`, `/second-brain-resume`, `/second-brain-review` — a five-stage capture→process→archive lifecycle, predating and independent of this vault's own `/ingest-clipping`, `/distill-note`, `/closeday`. Not currently the primary path for Jarvis work; useful as a fallback in a WSL project that has no vault-specific skills of its own.
## Hooks
Not invoked directly — they run automatically. `wsl-session-export.ps1` is the one that matters day to day: it's what actually populates `60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/`, wired to both `SessionEnd` and `Stop` so a crashed or force-closed session still gets captured. If a WSL session's conversation is missing from that folder, this hook (or its `-BackfillAll` recovery mode) is the first thing to check, not the sync mechanism.
## Skills
The Cloudflare/Workers cluster (`cloudflare`, `cloudflare-one`, `durable-objects`, `wrangler`, `web-perf`, etc.) is reference material for Workers-based projects — reach for it when building on Cloudflare, not for vault work. The `obsidian-*` skills cluster overlaps with the agents above; `graphify` auto-triggers on any input per the WSL home's own `CLAUDE.md`, so it doesn't need a manual invocation the way the others do.
# Windows home
Nothing to use yet, and that's a plain fact, not a gap to paper over. The only real global content is `export-ai-session` — invoke directly as `/export-ai-session`, works from either OS since Claude Code registers it per-session from whichever home directory is active, not shared between the two. If a task needs an agent, command, or hook while working from a plain Windows Claude Code session (not WSL), none exist globally yet — either build one and place it in the real Windows home directory first, or fall back to whatever the specific project's own `.claude/` provides.
# Particular Use
## Daily Operations
The WSL `second-brain-*` command lifecycle and `obsidian-daily-review`/`obsidian-session-review` are a real alternative path — see [[Daily Operations]] for why this vault's own `/startday`/`/closeday` are currently preferred over them.
## Vault Curation
`obsidian-architect` for structural audits, `obsidian-researcher` for open-ended search — see [[Vault Curation]] for how these compare to Jarvis's own `vault-curator` agent.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global]] for the underlying inventory this note gives usage guidance for.

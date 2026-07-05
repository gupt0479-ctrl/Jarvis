---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - claude-code
  - setup
  - trading-view
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: "none — reference dump from the gupta-builds/TradingView repo, not synced to this vault"
---
# Trading View — Claude Code Setup
A copy of the Claude Code config for the `gupta-builds/TradingView` repo — a data-ingestion project run through a Kiro design-first spec workflow (`.kiro/specs/data-ingestion-foundation/`: requirements.md, design.md, tasks.md). Previously an empty placeholder folder (as `TradingView/`, no space); re-exported with real content on 2026-07-05 under the folder name `Trading View` (with a space). Reference material only — not the same as the live TradingView build at `20_Progress/Projects/CS/TradingView/` per the Vault Architecture note.
## Files
### Agents
- [[20_Progress/AI/Claude Code/Trading View/agents/guardrail-auditor|guardrail-auditor]] — audits code/docs against the project's non-negotiable safety constraints (no execution language, no data fabrication, secrets redaction, confidence caps, scope boundaries)
- [[20_Progress/AI/Claude Code/Trading View/agents/spec-implementer|spec-implementer]] — implements the next open task from `tasks.md` strictly per `design.md`, reconciles checkbox state with actual code
### Skills
- [[20_Progress/AI/Claude Code/Trading View/skills/guardrail-check/SKILL|skills/guardrail-check/SKILL]] — mechanical grep sweep for guardrail violations, hands findings to `guardrail-auditor`
- [[20_Progress/AI/Claude Code/Trading View/skills/kiro-status/SKILL|skills/kiro-status/SKILL]] — reconciles `tasks.md` checkbox state against what's actually implemented
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Claude Code/Trading View"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `hooks/block-secrets.sh` — PreToolUse hook on Bash; blocks `git commit`/`git push` when the diff contains an `.env` file or secret-shaped value (this repo is public).
- `settings.json` — Claude Code project settings (Bash/git permission allowlist).
- `settings.local.json` — local permission overrides.
## Status & Gaps
This folder was empty (dead) as of the first pass on 2026-07-05 and has since been re-exported with the project's actual `.claude/` contents, under a renamed folder (`Trading View` instead of `TradingView`). No live equivalent exists in this vault to diff against, so every markdown file is marked `static`. This project treats `.claude/` as canonical and `.kiro/steering` as a thin mirror — same convention as Resq.
## Links
[[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

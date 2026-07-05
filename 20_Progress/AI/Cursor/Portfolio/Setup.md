---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - cursor
  - setup
  - portfolio
notes:
  - "[[20_Progress/AI/Cursor/MOC]]"
next: "none — external project dump; commands/portfolio-guide.md is corrupted and would need re-capture if this project is revisited"
---
# Portfolio — Cursor Setup
A copy of the Cursor config for a personal Next.js + Sanity CMS + Three.js portfolio site — the same project as [[20_Progress/AI/Claude Code/Portfolio/Setup|Portfolio's Claude Code dump]]. Reference material, not part of this vault's own tooling.
## Files
### Agents
- [[20_Progress/AI/Cursor/Portfolio/agents/portfolio-cms|agents/portfolio-cms]] — Sanity CMS/content specialist
- [[20_Progress/AI/Cursor/Portfolio/agents/portfolio-polish|agents/portfolio-polish]] — visual/UX polish and completion-gap specialist
- [[20_Progress/AI/Cursor/Portfolio/agents/portfolio-verify|agents/portfolio-verify]] — post-change lint/typecheck/build verification specialist
### Commands
- [[20_Progress/AI/Cursor/Portfolio/commands/portfolio-guide|commands/portfolio-guide]] — quick-reference command/workflow cheat sheet (corrupted, see Status & Gaps)
### Skills
- [[20_Progress/AI/Cursor/Portfolio/skills/portfolio-completion/SKILL|skills/portfolio-completion/SKILL]] — completion checklist and section-order wiring
- [[20_Progress/AI/Cursor/Portfolio/skills/portfolio-content-cms/SKILL|skills/portfolio-content-cms/SKILL]] — Sanity schema/query/type consistency guide
- [[20_Progress/AI/Cursor/Portfolio/skills/portfolio-ui-polish/SKILL|skills/portfolio-ui-polish/SKILL]] — layout, 3D background, and accessibility guide
### Docs
- [[20_Progress/AI/Cursor/Portfolio/plans/sanity_render_alignment_9e8bf844|plans/sanity_render_alignment_9e8bf844]] — in-progress plan auditing Sanity fields against GROQ queries and UI, fixing schema drift
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Cursor/Portfolio"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `rules/Portfolio-Main-Rules.mdc` — always-on Cursor rule: senior front-end persona, code standards, styling and accessibility rules for the portfolio repo.
- `settings.json` — Cursor project settings for this dump.
- `debug-3327cb.log` — a leftover debug log capture, not project config.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — marked `static` except where noted.
- **`commands/portfolio-guide.md` is corrupted and marked `draft`**: the file has no frontmatter, every line carries a stray 2-space indent, and it ends with leaked tool-call XML fragments (`</parameter>`, `</function>`, `</tool_call>`) that don't belong in a markdown doc — evidence the original capture accidentally scraped part of an AI tool's own function-call output. Content is otherwise readable (a command/workflow cheat sheet); re-capture cleanly if this project's Cursor layer is revisited.
- `plans/sanity_render_alignment_9e8bf844.plan.md` has 5 `pending` todos and 1 `in_progress` — this plan was mid-flight when the dump was taken, not stale relative to a live source (there is none), just unfinished in its own right.
- Cursor's plan file format uses native `name:`/`overview:`/`todos:` keys — left untouched; only `setup_status`/`updated`/`notes` were added.
## Links
[[20_Progress/AI/Cursor/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]

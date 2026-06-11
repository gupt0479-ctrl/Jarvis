---
type: evergreen
status: tree
created: 2026-05-31
updated: 2026-06-11
tags:
  - system
  - ai-agents
  - rules
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[Jarvis Writing and Formatting]]"
  - "[[Agent Operating Guide]]"
---
# Vault Rules — Operational Reference

This file holds the tool-selection table and the session-end protocol. The formatting spec (blank lines, markers, frontmatter, quality gate, safety rules, source ingestion) now lives in [[Jarvis Writing and Formatting]]. Placement rules live in [[40_Resources/Obsidian/Jarvis Vault Architecture]]. The cold-start read order and strategy live in [[Jarvis OS — North Star]].

**The single test:** open any two instruction files — if a sentence is true in both, one is wrong and must become a pointer.

## Tool Selection

### Reading Files

| Situation | Tool |
|---|---|
| Any text file or Markdown note | `Read` |
| PDF file | Python pypdf via `Bash` |
| Image file | `Read` (multimodal) |
| Live URL | `WebFetch` |
| Search file contents | `Grep` |
| Find files by pattern | `Glob` |
| Directory listing | `Bash` (ls) |

### Writing Files

| Situation | Tool |
|---|---|
| Patching an existing file by heading | `Edit` (patch only — do not rewrite) |
| Creating a new file | `Write` |
| Full rewrite of an existing file | `Read` first, then `Write` |

### MCP Filesystem Tools

Prefer `Read`, `Edit`, `Write`, `Grep`, `Glob` over `mcp__filesystem__*` equivalents. Use MCP filesystem tools only when the core tools cannot perform the operation. Never use MCP tools to read plugin `data.json` files unless explicitly asked.

### Subagents

- Use subagents for broad exploration requiring 3+ queries
- `subagent_type: Explore` for finding files without a known path
- `subagent_type: research-distiller` for long technical PDFs requiring section-by-section extraction
- Do not spawn subagents for tasks completable inline with 1–2 tool calls

## Session End Protocol

After any meaningful vault changes, append a concise entry to `60_Claude/07_AI_Information/Session Logs/log.md`.

Format:
```
## [YYYY-MM-DD] [operation] | [title or subject]
- What was created or changed
- Why it matters
- Open questions
- Next action if one exists
```

Update `updated:` in the frontmatter of any note that changed meaningfully. Do not update dashboards just to create activity.

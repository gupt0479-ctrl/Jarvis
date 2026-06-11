# mcp-hub

**Description:** Defines which files to send to each external AI tool as context, and how to keep those files current. The vault's external-agent contract.

**Usage:** `/mcp-hub` for menu. `/mcp-hub list-tools` to list configured tools. `/mcp-hub context-pack {tool}` to print or write a context pack for that tool. `/mcp-hub sync` to refresh stale wrapper files.

> Save to: `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\mcp-hub.md`
> Cowork blocked the direct write to `.claude/`; copy from this scratchpad into the vault path above.

---

## What This Skill Does

External agents (Claude Code, Cursor, Kiro, Codex, Cowork, ChatGPT, future agents) all need a small, focused context pack — not the whole vault. This skill is the single place that decides:

1. Which files each tool reads first.
2. Which wrapper file each tool consumes (`.claude/`, `.cursor/`, `.kiro/`, `AGENTS.md`).
3. How to verify those wrappers still point at the right vault paths.
4. How to print a one-shot context pack on demand for tools that don't load files automatically (web Claude, ChatGPT).

The skill is read-mostly. It writes only when explicitly told to (`/mcp-hub sync` or `/mcp-hub context-pack {tool} --write`).

---

## Reading Order (Required Before Acting)

1. `AGENTS.md`
2. `CLAUDE.md`
3. `HUMAN_WRITING.md`
4. `60_Claude/7_AI_Information/AI_CONTEXT.md`
5. `40_Resources/Obsidian/Claude Pro Workflow.md`
6. `40_Resources/Obsidian/MCP-Hub-Index.md` — the single-page external orientation note.
7. `00_Dashboard.md`
8. Tail of `60_Claude/07_AI_Information/Session Logs/log.md` — last 30 lines.

---

## Tool Registry

The canonical map of external tools and their required context files. When a tool is added or removed, edit this table — do not invent ad hoc rules elsewhere.

| Tool | Wrapper File | Spine Files Required | Live State Files | Project Context | Writes Back? |
|------|--------------|----------------------|------------------|-----------------|--------------|
| Claude Code CLI | `CLAUDE.md` (auto-loaded) | AGENTS.md, HUMAN_WRITING.md, AI_CONTEXT.md | 00_Dashboard.md, session log tail | task-specific notes only | Yes — vault edits, skills, agents |
| Cowork (this) | Project instructions + CLAUDE.md | Same as Claude Code | Same | task-specific | Yes — vault edits |
| Cursor | `.cursor/rules/workspace-context.mdc` | AGENTS.md, HUMAN_WRITING.md, AI_CONTEXT.md | 00_Dashboard.md | repo-level `AGENTS.md` if present | Yes — repo edits via Cursor |
| Kiro | `.kiro/steering/workspace-context.md` | AGENTS.md, HUMAN_WRITING.md, AI_CONTEXT.md | 00_Dashboard.md, session log tail | spec folder under `.kiro/specs/` | Yes — specs only |
| Codex | `AGENTS.md` (auto-loaded) | HUMAN_WRITING.md, AI_CONTEXT.md | 00_Dashboard.md | active project note | Yes — scripts, repo edits |
| Claude Desktop | Project knowledge upload | Same as Claude Code | Same | task-specific | Read-first (per Claude Pro Workflow) |
| Claude mobile | None — capture only | Quick reference to AGENTS rules | None | None | No — capture only |
| Claude web / ChatGPT | Project knowledge upload | Compressed spine + MCP-Hub-Index | 00_Dashboard summary | hand-picked notes | No — distillation happens in Cowork/Code |
| External agent (new) | `40_Resources/Obsidian/MCP-Hub-Index.md` | AGENTS.md, HUMAN_WRITING.md, AI_CONTEXT.md | 00_Dashboard, session log | depends | Depends on agent capability |

---

## Context Pack Format

Every context pack — regardless of tool — has the same five sections. The differences are which files fill each section and how much detail.

```markdown
# Jarvis Context Pack — {tool} — YYYY-MM-DD

## Read Order
1. {file 1}
2. {file 2}
... (the spine pack)

## Live State
- Active projects: {top 3 from 00_Dashboard active-projects table}
- Open `next:` actions: {top 5}
- Last 3 session log entries: {compressed one-liner each}

## Project Context
- Current project note: {path or "none"}
- Relevant concept notes: {top 5 by track}
- Open questions: {from the project note or recent log}

## Safety Rules
- Folder roles: {paste from CLAUDE.md folder roles table — compressed}
- Protected paths: {from CLAUDE.md + Vault Operating System}
- Writing standard: read HUMAN_WRITING.md before drafting prose

## Suggested Next Actions
- {tool-specific: for Code → run morning-start; for Cursor → load repo CONTEXT.md; for web → ask the question}
```

---

## Operations

### `/mcp-hub` (menu)

Print the tool registry table and the operation list. Suggest the most relevant operation based on the current session context.

### `/mcp-hub list-tools`

Print the tool registry table. For each tool, verify the wrapper file exists. Mark with [OK] / [MISSING]. If missing, suggest the fix.

### `/mcp-hub context-pack {tool}`

Build and print the context pack for the named tool. By default, print to chat. With `--write`, save to `60_Claude/45_Outputs/Context Packs/Context Pack — {tool} — YYYY-MM-DD.md`.

Tool-specific overrides:

- **claude-code:** include `.claude/skills/` index and `.claude/agents/` index.
- **cursor:** include the active repo's `CONTEXT.md` if it exists and any `.cursor/rules/` files.
- **kiro:** include the active spec folder's `requirements.md`, `design.md`, `tasks.md`.
- **codex:** include the active repo's `AGENTS.md` if present.
- **web (Claude/ChatGPT):** strict 2000-token cap. Compress aggressively: spine pack as headings only, live state as 5 bullets, project context as note titles only.
- **mobile:** smallest possible pack — three rules and a list of where to file captures.

### `/mcp-hub sync`

Verify every wrapper file's references against the actual vault. Checks performed:

1. Does each path in each wrapper resolve to an existing file?
2. Does `[[AI_CONTEXT]]` in the wrapper resolve to `60_Claude/7_AI_Information/AI_CONTEXT.md` (the only file by that name)?
3. Does each wrapper's "read these files" list match the current canonical spine in `AI_CONTEXT.md`?
4. Are there files in `AI_CONTEXT.md`'s canonical sources list that the wrappers don't include? Or vice versa?

For each drift detected, print a diff and propose a patch. Apply only on `--apply` flag.

### `/mcp-hub verify {tool}`

Single-tool version of `sync`. Useful when you've just added a new tool or changed a wrapper.

---

## Wrapper File Standards

Every wrapper file (anything that bridges an external tool to this vault) must:

1. Be under 50 lines. Wrappers should point at the canonical spine, not duplicate it.
2. List the spine files using full vault-root paths, not bare filenames (avoid the `AI_CONTEXT.md` ambiguity).
3. State explicitly: "This vault uses `[[wikilinks]]` for internal references. Paths in this file are vault-root-relative."
4. Include one line stating the tool's write scope (repo edits / vault edits / read-only).
5. Update its `updated:` timestamp or filesystem mtime when the spine changes.

---

## How to Add a New Tool

When a new AI tool needs to read this vault:

1. Decide its wrapper-file location (follow each tool's convention: `.cursor/rules/`, `.kiro/steering/`, repo-root `AGENTS.md`, etc.).
2. Add a row to the Tool Registry table in this file.
3. Build the wrapper using the Wrapper File Standards above.
4. Run `/mcp-hub verify {new-tool}` to confirm it resolves.
5. Run `/mcp-hub context-pack {new-tool}` to confirm the pack builds.
6. Log the addition in the session log.

---

## How to Keep the Hub Healthy

Run `/mcp-hub sync` weekly (or after any spine file changes). Specifically run it after:

- Renaming or moving any spine file.
- Adding or removing a skill, agent, or rule file under `.claude/`.
- Updating `AI_CONTEXT.md`'s canonical sources list.
- Adding a new external tool to the workflow.

The `/ops` skill should call `/mcp-hub sync` as part of `morning-start` once per week — see the integration note below.

---

## Integration With Existing Skills

- **`/ops morning-start`:** can include `/mcp-hub list-tools` as a quick verification step.
- **`/ops health-check`:** the wrapper-file drift check is a useful extra dimension. Add as a manual flag.
- **`/weekly-review`:** include "MCP hub wrapper drift" as a check item.
- **`learning-agent`:** generates the context pack for itself when it needs to drill across multiple tools.
- **`research-distiller`:** consumes the context pack when ingesting cross-tool conversations.

---

## Failure Modes

- **Wrapper drift.** Wrappers point at paths that no longer exist. Caught by `/mcp-hub sync`.
- **Spine drift.** A new canonical source is added to `AI_CONTEXT.md` but wrappers don't include it. Caught by `/mcp-hub sync`.
- **Over-stuffing.** A wrapper grows past 50 lines and starts duplicating spine content. The wrapper becomes its own source of truth, which defeats the hub's purpose. Prune in weekly review.
- **Tool-specific path bugs.** Each tool has its own conventions (Cursor uses `#[[file:...]]` syntax, Kiro uses `inclusion: always` frontmatter, etc.). Use each tool's syntax inside its wrapper, but always with full vault-root paths.

---

## Output Style

- Tables for the registry.
- Bullets for live state and suggestions.
- Code blocks for proposed patches.
- Follow `HUMAN_WRITING.md`: no filler, no audit narration, concrete and compressed.

---

## Session Log Entry

When the skill modifies wrapper files or writes a context pack, append:

```
## [YYYY-MM-DD] mcp-hub | [operation]
- Tools verified: {list}
- Wrappers patched: {list with old → new}
- Context packs written: {list of files}
- Drift items resolved: {count}
```

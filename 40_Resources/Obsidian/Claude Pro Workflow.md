---
type: evergreen
status: sprout
created: 2026-05-26
updated: 2026-05-26
tags:
  - evergreen
  - claude
  - workflow
  - ai
notes:
  - "[[AI_CONTEXT]]"
  - "[[CLAUDE.md]]"
  - "[[Vault Operating System]]"
  - "[[Jarvis]]"
source_status: mixed
---
# Claude Pro Workflow

This note is the operating contract for using Claude Pro with Jarvis without burning the plan on context churn.

## One-Line Rule

Claude Pro works best here when Claude Code is the workbench, Claude Desktop is the thinking room, mobile is capture, and Jarvis is the shared memory layer.

## What Is True

- Claude Code, Claude Desktop, claude.ai, and mobile share the same Claude usage pool.
- MCP does not create extra usage. It only helps when it replaces pasted context with small targeted reads.
- Tools and connectors can be token-expensive. A bad MCP workflow can hit limits faster than a plain chat.
- Jarvis should not be scanned as a whole vault by default.
- Local Obsidian MCP is a desktop/laptop workflow. Mobile should not be expected to read localhost tools.

## Surface Roles

| Surface | Use For | Do Not Use For |
|---|---|---|
| Claude Code | implementation, vault maintenance, project edits, repo exploration, verification | rambling brainstorms with no target |
| Claude Desktop | architecture, review, learning, note discussion, planning | uncontrolled vault edits |
| Claude mobile | quick capture, small questions, reviewing prepared context | local vault MCP, long implementation sessions |
| Jarvis | memory, source notes, decisions, context packs, session continuity | raw undistilled transcript dumping |

## Context-Pack Start

Claude should start with a small context pack:

1. `AGENTS.md`
2. `HUMAN_WRITING.md`
3. `60_Claude/7_AI_Information/AI_CONTEXT.md`
4. `00_Dashboard.md`
5. the tail of `60_Claude/10_Session_Logs/log.md`
6. task-specific notes only after the task is clear

Do not ask Claude to read the whole vault. If a broad search is needed, ask for a targeted search query first.

## Claude Code Prompt

```text
Use the Jarvis context pack. Read AGENTS.md, HUMAN_WRITING.md, 60_Claude/7_AI_Information/AI_CONTEXT.md, 00_Dashboard.md, and the recent tail of 60_Claude/10_Session_Logs/log.md. Then read only the project or course notes needed for this task. Do not scan the whole vault unless I explicitly ask.
```

## Desktop Prompt

```text
Read the Jarvis context pack: AI_CONTEXT, dashboard, recent session log tail, and the relevant project note. Do not scan the whole vault unless I ask. Treat Desktop as planning/review only; do not modify notes unless I explicitly ask for a vault edit.
```

## Mobile Prompt

```text
Capture this as a quick Jarvis note idea. Keep it short, extract decisions and next actions, and tell me what note or project it should be filed under later.
```

## Rate-Limit Discipline

- Use Sonnet for normal coding, notes, and implementation.
- Use Opus only for hard planning, cross-cutting architecture, or stuck debugging.
- Start a new session or run `/clear` between unrelated tasks.
- Use `/compact` when the current task still needs the conversation history.
- Prefer paths and note names over pasted files.
- In Claude Code, inspect `/context` when a session feels heavy.
- Disable unused Desktop tools/connectors for chats that do not need them.

## MCP Rules

- MCP should answer "where is the right context?" before it answers "what is everything?"
- Obsidian MCP reads should start with indexes, dashboards, and project boards.
- Claude Desktop should be read-first. Write access belongs in Claude Code until the workflow is stable.
- Do not put API keys in vault notes or shared config files.
- If a connector needs public internet access, treat it as a security project, not a quick setup step.
- Current Claude Code builds read project MCP servers from `.mcp.json` at the vault root. Jarvis also keeps `.claude/.mcp.json` as an older compatibility copy.

## Hook Policy

Use hooks for small deterministic reminders and local activity metadata. Do not log every edit or tool call.

Current intended hooks:

- `SessionStart`: remind Claude Code of the Jarvis context-pack policy when launched inside this vault.
- `SessionEnd`: write compact local activity metadata to the user's private Claude directory, not to the vault session log.

Human session summaries still belong in `60_Claude/10_Session_Logs/log.md` after meaningful vault work.

## Failure Modes

- Full-vault reads create fake confidence and waste limits.
- Auto-writing Desktop tools can create slop faster than the vault can absorb it.
- Long conversations make every next message more expensive.
- Local MCP is not mobile MCP. A remote Jarvis connector needs explicit security design.
- Storing secrets in `.claude/settings.json`, MCP JSON, or Obsidian notes turns workflow config into credential debt.

## Verification Checklist

- `claude --version` works.
- Claude Code `/status` shows Claude.ai subscription auth when using Claude Pro.
- Claude Code `/mcp` or `claude mcp list` lists the expected project MCP servers from `.mcp.json`.
- Project settings do not force `ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`, or model overrides.
- Desktop can read/search Jarvis but is not treated as the primary vault editor.
- The first working session ends with a human-readable session log entry.

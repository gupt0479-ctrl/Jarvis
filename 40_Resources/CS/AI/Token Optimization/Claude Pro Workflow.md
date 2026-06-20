---
type: evergreen
status: sprout
created: 2026-05-26
updated: 2026-06-20
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

## How the Limits Actually Work (2026)

The weekly limit is not a message count. Anthropic's interface talks in "messages," but the real unit is tokens of compute, weighted by model, conversation length, effort level, and which tools are loaded. The same question can cost several times more on Opus with a long history than on Sonnet in a fresh chat.

Two windows stack:

- A **5-hour rolling window** — starts on your first prompt, not on a clock hour. Rough community sizing: ~44k tokens on Pro, ~88k on Max 5x, ~220k on Max 20x.
- A **weekly cap** (added Aug 2025) that counts only the time Claude is actively processing or reasoning.

The cost driver most people miss: every new message re-sends the entire conversation as input. Message 201 costs as much input as messages 1–200 combined. The usual way to burn the week is one long session, not the number of questions — it is the accumulated context dragged along each turn.

Usage limit and context window are different things. The 200k context window ends a single conversation when full; usage limits stop you across all conversations. They interact: with code execution on, Claude auto-summarizes a long chat to keep going, and that summarization itself spends usage. If you are near a limit inside a long chat, starting a new one is cheaper than continuing.

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
3. `60_Claude/07_AI_Information/AI_CONTEXT.md`
4. `00_Dashboard.md`
5. the tail of `60_Claude/07_AI_Information/Session Logs/log.md`
6. task-specific notes only after the task is clear

Do not ask Claude to read the whole vault. If a broad search is needed, ask for a targeted search query first.

## Claude Code Prompt

```text
Use the Jarvis context pack. Read AGENTS.md, HUMAN_WRITING.md, 60_Claude/07_AI_Information/AI_CONTEXT.md, 00_Dashboard.md, and the recent tail of 60_Claude/07_AI_Information/Session Logs/log.md. Then read only the project or course notes needed for this task. Do not scan the whole vault unless I explicitly ask.
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

## Cowork Discipline

Cowork shares the same usage pool as Code and chat, but it front-loads cost: every session reads the connected folder, global instructions, and skills before you ask anything. The setup is the lever.

- Keep `CLAUDE.md` and project instructions lean — they load every session, so every extra paragraph is a recurring tax.
- Don't keep 50 files in the connected folder when 3 are relevant. Fetch-don't-dump still applies.
- Use plain chat (Haiku or Sonnet) for thinking; open Cowork only when you know what you want built.
- For recurring work — digests, reviews, briefings — use the `/schedule` plugin instead of one ever-growing session.
- This environment defers MCP tool definitions and loads them on demand via tool search, instead of loading every connector's schema upfront. Keep it that way: with this many connectors attached, upfront loading would spend roughly a third of the window before the first message.

## Token-Discipline Block (paste into project instructions)

Drop this into `CLAUDE.md` or a project's instructions to make frugal behavior the default:

```text
Token discipline:
- One task per conversation. Tell me to /clear or open a new chat when the task changes.
- Default to Sonnet; escalate to Opus only for hard planning or stuck debugging; use Haiku for quick lookups.
- Fetch, don't dump: read the context pack (AGENTS, AI_CONTEXT, dashboard, log tail) + only task-specific notes. Never scan the whole vault unless I explicitly ask.
- Prefer targeted grep/search over broad reads; prefer note names and paths over pasted file bodies.
- Keep extended thinking off and effort low for routine edits.
- Run /compact proactively around 250–300k tokens, not after the warning.
- Disable connectors not needed for the current task.
```

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

Human session summaries still belong in `60_Claude/07_AI_Information/Session Logs/log.md` after meaningful vault work.

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

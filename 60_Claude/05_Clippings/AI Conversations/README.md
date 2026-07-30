---
type: dashboard
status: tree
created: 2026-05-29
updated: 2026-07-30
tags:
  - clippings
  - ai-conversations
  - readme
notes:
  - "[[60_Claude/07_AI_Information/AI Conversation - Summaries/README]]"
  - "[[Jarvis Three-Month Research Engine Master Plan]]"
---
# AI Conversations — Raw Archive
This folder is the raw archive for exported LLM conversation transcripts (Claude Code, Claude web, Codex, Cursor, Kiro, ChatGPT, Ollama, future tools).
## Structure (added 2026-07-05)
Split by OS environment first, then by tool, since Claude Code/Kiro/Cursor each maintain separate config and session history on Windows vs WSL:
```
AI Conversations/
  Windows/
    Claude Code/   ← wired up: raw JSONL mirror + exported markdown notes (fully automatic via SessionEnd hook)
    Cowork/        ← wired up (2026-07-06): Cowork/Agent-Mode sessions, swept from %APPDATA%\Claude\local-agent-mode-sessions on every session end (no standing junction — credentials are scattered per-sandbox)
    Kiro/          ← scaffold only, not wired
    Cursor/        ← wired up (2026-07-30): per-project subfolders, JSONL+SQLite join, Task Scheduler sweep — see below
  WSL/
    Claude Code/   ← wired up (2026-07-30): per-project subfolders, raw JSONL mirror + richer exported markdown notes (tool calls captured, not just names), fully automatic via SessionEnd hook — see below
    Kiro/          ← scaffold only, not wired
    Cursor/        ← wired up (2026-07-30): same two-source join as Windows/Cursor, routed here for vscode-remote / file://wsl$ workspaces
  Claude App/      ← Desktop app, cloud-based — not part of the Windows/WSL split
  OpenCode/
```
`Windows/Claude Code/_raw_jsonl/` is an NTFS junction straight to `~/.claude/projects` — the complete, unredacted, zero-token safety-net archive. It's gitignored (`**/_raw_jsonl/`) and must stay that way. Exported per-session markdown notes (the immutable, redacted, readable layer described below) live alongside it in the same folder. Both this and the Cowork sweep below are now fully automatic, triggered by the global `SessionEnd` hook (`30_Order/System/claude-workflow/hooks/jarvis-session-continuity.ps1`) — no manual step. The global `/export-ai-session` skill's job is now just tier-2 distillation of notes that already exist.

`Windows/Cowork/` covers Claude Desktop's Cowork/Agent-Mode feature, which spins up a fully isolated `.claude` sandbox per task under `%APPDATA%\Claude\local-agent-mode-sessions` (42+ sandboxes observed, each with its own `.credentials.json`). Because credentials are scattered per-sandbox rather than centralized the way `~/.claude/projects` is, there is deliberately no raw-JSONL junction here — a blanket directory link would mirror those credentials into the vault. Instead the same `SessionEnd` hook sweeps for new Cowork transcripts (via long-path-safe `.NET` enumeration, since these paths run past Windows' 260-char `MAX_PATH`) every time a normal Claude Code session ends, since Cowork's sandboxes can't fire the hook themselves — "eventually consistent" rather than instant, but fully automatic.

`Windows/Cursor/` and `WSL/Cursor/` (rewired 2026-07-30) join **two** stores — the old SQLite-only / on-demand `_raw_composer/` story is retired:

1. **Per-session JSONL** under `~/.cursor/projects/**/agent-transcripts/<uuid>/<uuid>.jsonl` — lives on the OS where the workspace ran (WSL home or Windows profile). Shape is lean: `role` + `message.content[]` with `text` / `tool_use` blocks. No `timestamp`, `usage`, or `model` fields — those frontmatter keys are omitted for Cursor, never fabricated.
2. **Windows-only SQLite** `%APPDATA%\Cursor\User\globalStorage\state.vscdb`, table `composerHeaders` — `composerId` equals the JSONL filename. The `value` JSON supplies `name` (title), `subtitle`, `createdAt` / `lastUpdatedAt` (epoch-ms → local `YYYY-MM-DDTHH:MM:SS`, no offset, no fraction), `filesChangedCount`, `totalLinesAdded`, `totalLinesRemoved`, `isDraft`. No token or cost data anywhere in this store.

Routing uses `workspaceIdentifier.uri` (fallback: `workspaceStorage/<workspaceId>/workspace.json`): `vscode-remote://wsl+...` or `file://wsl$/...` → `WSL/Cursor/<project>/`; `file:///c:/...` / `file:///d:/...` → `Windows/Cursor/<project>/`. `<project>` is the resolved folder basename. The exporter always runs on **Windows** (that's where SQLite lives); WSL JSONL is read via `\\wsl.localhost\<distro>\home\...`.

Layout per project (mirrors WSL Claude Code):
```
{WSL|Windows}/Cursor/<project>/
  MM-DD {name}.md                 ← one per session
  _raw_jsonl/                     ← Windows: NTFS junction to that Cursor project's agent-transcripts/; WSL: one-way per-session .jsonl copy (DrvFs can't junction)
  _archive-pre-fix/               ← pre-2026-07-30 flat notes, archived not deleted
  00 - Session Index.md           ← Dataview over this folder
  00 - Tool Usage Rollup.md       ← DataviewJS tool/file aggregates (no tokens/cost — Cursor doesn't have them)
```

Skip (no note) if: no `composerHeaders` row, `isDraft`/`isArchived`/`isSubagent`, or the JSONL has no real assistant turn. Dedup: WSL flat `_raw_jsonl/<session_id>.jsonl` existence, or any note already carrying that `session_id`.

**Trigger:** Windows Task Scheduler task `Jarvis-Cursor-Session-Export` (every 15 min) running `30_Order/System/cursor-workflow/scripts/sweep-cursor-sessions.ps1`. A Cursor `sessionEnd` hook is **not** used for live export — confirmed 2026-07-30 in `cursor.hooks` logs for this vscode-remote+wsl workspace: `User config path: \home\anant_gupta\.cursor\hooks.json` (WSL), not the Windows `%USERPROFILE%\.cursor\hooks.json`. WSL-side hooks cannot reliably open the Windows SQLite store. Same eventually-consistent pattern as Cowork. Manual: `py export-cursor-sessions.py --backfill` / `--sweep`.

Backfill reconciled (2026-07-30): 48 WSL + 20 Windows JSONL = 68; `composerHeaders` 207 total / 127 non-archived non-subagent; jsonl∩header = 67; exported **63** (47 WSL + 16 Windows) after skipping 2 archived + 2 subagent + 1 jsonl-with-no-header. The 140 header-only rows are composers with no agent-transcripts JSONL (older bubble-store chats, aborted drafts, etc.).

`WSL/Claude Code/` (wired 2026-07-30, revised 2026-07-30) is intentionally a different shape from `Windows/Claude Code/`, fixing gaps that Windows's exporter still has (tracked separately, out of scope to fix there in this pass): it exports **every** WSL project's session unconditionally (no `cwd`-gated allowlist), splits output **per-project** rather than dumping everything into one flat `Jarvis`-labeled folder, captures full tool-call inputs/results (not just tool names), titles sessions from Claude Code's own auto-generated `ai-title` (not a slug guessed from the first message), and generates session-level rollup metadata including a real per-model `cost_usd`. Wiring: the global `SessionEnd` hook `~/.claude/hooks/wsl-session-export.ps1` (WSL-side, `~/.claude/settings.json`); the same script also supports a manual `-BackfillAll` mode that walks every transcript under `~/.claude/projects/**/*.jsonl` (idempotent — safe to re-run). Layout per project:
```
WSL/Claude Code/<project-basename-of-cwd>/
  MM-DD {ai-title}.md              ← one per session (folder path already says "Claude Code", so the filename doesn't repeat it)
  _raw_jsonl/                      ← one-way copy (not a junction — can't junction across the WSL/DrvFs boundary) of this project's session .jsonl files; gitignore-equivalent, unredacted safety net
  _archive-pre-fix/                ← pre-2026-07-30 output, archived (not deleted) when the exporter was rewritten
  00 - Session Index.md            ← live Dataview query over this folder's session notes (date, linked title, turns, duration, tokens, cost) — recomputed by Obsidian at render time, not hand-built
  00 - Tool Usage Rollup.md        ← live DataviewJS block aggregating tool-name counts, files-touched-by-session-count, and total tokens/cost across every session note in this folder
```
Dedup is keyed off the raw per-session copy (`_raw_jsonl/<session_id>.jsonl`) rather than a shared JSON index file, since that copy is already keyed on `session_id` and its mere existence is sufficient to know a session was processed — no extra index file, no write contention.

A session is skipped entirely (no markdown, no folder pollution — though the raw JSONL safety-net copy still lands) if it has zero real assistant turns, or if Claude Code never generated an `ai-title` for it (a reliable signal of a trivial session — bare `/clear`, `/exit`, empty session).

`WSL/Claude Code/` session notes carry these frontmatter keys beyond the "Required Frontmatter" minimum below: `source_os` (`wsl`), `duration_minutes` (first/last transcript timestamp), `exported_at` (when this export ran — distinct from `started_at`/`ended_at`, when the session actually happened), `tools_used` (a mapping of `ToolName: count`), `tokens` (`input`/`output`/`cache_creation`/`cache_read`/`total`, summed per assistant message's `usage` block), `cost_usd` (computed from Anthropic's published per-model pricing, summed across every distinct model that ran in the session — `null` if a model string has no findable price), `model` (list of every distinct model string that appeared), and `files_touched` (deduped list of file paths the session's Read/Write/Edit/MultiEdit calls touched — what the two rollup Dataview queries aggregate against). Each assistant turn's body also gets a **Tool Calls** subsection listing every `tool_use` with redacted meaningful inputs (and result, for `Bash`/`Edit`/`MultiEdit`/`Write`), and the note ends with an **Actions Taken** section (files created/modified/deleted, commands run, tool-call tally) — richer than Windows's tool-name-only capture, at the cost of meaningfully larger notes.
## Rules
- **Files dropped here are immutable.** Read-only, never rewritten in place.
- Distillation outputs go to `60_Claude/07_AI_Information/AI Conversation - Summaries/`.
- Promotion to durable knowledge (concept notes, project briefs, outputs) requires a manual decision after distillation — not automatic.
## File Naming
```
MM-DD {source-app} - {slugified title}.md
```
Examples:
- `05-29 Claude Code Vault - Audit session.md`
- `05-29 Chatgpt Rag Architecture - Discussion.md`
## Required Frontmatter (Minimum)
```yaml
---
type: input
input_kind: ai-conversation
source_app: claude-code | claude-web | codex | cursor | kiro | chatgpt | ollama | other
title: human-readable conversation title
started_at: YYYY-MM-DDTHH:MM:SS
ended_at: YYYY-MM-DDTHH:MM:SS
project: optional project name
status: raw
tags:
  - #input
  - #...
---
```
## Distillation Workflow
1. Drop raw transcript here with the frontmatter above.
2. Run `/ingest-clipping "60_Claude/05_Clippings/AI Conversations/your-file.md"` or invoke the `research-distiller` agent.
3. Distilled summary lands in `60_Claude/30_Source_Summaries/AI Conversations/` with provenance back here.
4. Promotion to durable knowledge is a separate manual step.
## Related
- [[Jarvis Three-Month Research Engine Master Plan]] — defines the conversation memory workstream.
- [[Jarvis Multi-Agent PKM Plan]] — earlier design for the conversation registry schema.
- [[60_Claude/40_Project_Briefs/Vault-Audit-2026-05-29]] — flags this folder's prior absence as the highest-impact Month 1 fix.

---
type: dashboard
status: tree
created: 2026-05-29
updated: 2026-05-29
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
    Cursor/        ← wired up (2026-07-05): exported markdown notes + optional _raw_composer/
  WSL/
    Claude Code/   ← scaffold only, not wired
    Kiro/          ← scaffold only, not wired
    Cursor/        ← wired up (2026-07-05): same pipeline as Windows/Cursor, routed here for vscode-remote workspaces
  Claude App/      ← Desktop app, cloud-based — not part of the Windows/WSL split
  OpenCode/
```
`Windows/Claude Code/_raw_jsonl/` is an NTFS junction straight to `~/.claude/projects` — the complete, unredacted, zero-token safety-net archive. It's gitignored (`**/_raw_jsonl/`) and must stay that way. Exported per-session markdown notes (the immutable, redacted, readable layer described below) live alongside it in the same folder. Both this and the Cowork sweep below are now fully automatic, triggered by the global `SessionEnd` hook (`30_Order/System/claude-workflow/hooks/jarvis-session-continuity.ps1`) — no manual step. The global `/export-ai-session` skill's job is now just tier-2 distillation of notes that already exist.

`Windows/Cowork/` covers Claude Desktop's Cowork/Agent-Mode feature, which spins up a fully isolated `.claude` sandbox per task under `%APPDATA%\Claude\local-agent-mode-sessions` (42+ sandboxes observed, each with its own `.credentials.json`). Because credentials are scattered per-sandbox rather than centralized the way `~/.claude/projects` is, there is deliberately no raw-JSONL junction here — a blanket directory link would mirror those credentials into the vault. Instead the same `SessionEnd` hook sweeps for new Cowork transcripts (via long-path-safe `.NET` enumeration, since these paths run past Windows' 260-char `MAX_PATH`) every time a normal Claude Code session ends, since Cowork's sandboxes can't fire the hook themselves — "eventually consistent" rather than instant, but fully automatic.

Cursor uses a different Tier 0 shape than Claude Code: conversation data lives in a single commingled Windows SQLite store (`%APPDATA%\Cursor\User\globalStorage\state.vscdb`), not a per-project JSONL tree, so there is no standing junction. Instead each of `Windows/Cursor/` and `WSL/Cursor/` may contain an on-demand `_raw_composer/` folder (gitignored via `**/_raw_composer/`), populated per-composer only when explicitly requested — see `30_Order/System/cursor-workflow/README.md`. Cursor conversations are routed to `Windows/Cursor/` or `WSL/Cursor/` by the originating workspace's URI scheme (`file` vs `vscode-remote`), not by which OS the export script runs on — the script itself always runs on Windows since that's where the SQLite store lives.
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

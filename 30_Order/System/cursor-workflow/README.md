---
type: reference
status: living
created: 2026-07-05
updated: 2026-07-30
tags:
  - cursor
  - ai-conversations
  - readme
---
# Cursor Workflow

Exports Cursor agent sessions into the Jarvis vault raw-archive format
described in `60_Claude/05_Clippings/AI Conversations/README.md`.

## Where the data actually lives (verified 2026-07-30)

Two stores, joined on `composerId` == JSONL filename UUID:

| Location | Holds | Role |
|---|---|---|
| `~/.cursor/projects/**/agent-transcripts/<uuid>/<uuid>.jsonl` | Lean `role` + `message.content[]` (`text` / `tool_use`). No timestamp/usage/model. Lives on the OS where the workspace ran (48 WSL + 20 Windows as of 2026-07-30). | Transcript body + tool calls |
| `%APPDATA%\Cursor\User\globalStorage\state.vscdb` → `composerHeaders` | `composerId`, `workspaceId`, timestamps, `isArchived`, `isSubagent`, `value` JSON (`name`, `subtitle`, `isDraft`, `filesChangedCount`, `totalLinesAdded`, `totalLinesRemoved`, …). No tokens/cost. | Title, times, actions seed, junk signals |
| `workspaceStorage/<workspaceId>/workspace.json` | `{ "folder": "vscode-remote://…" \| "file:///…" }` | Routing fallback when `value.workspaceIdentifier.uri` is missing |

The older bubble-store path (`cursorDiskKV` `composerData:` / `bubbleId:`) and
the on-demand `_raw_composer/` dump remain in this folder for reference but
are **not** the live export path anymore. Agent JSONL + `composerHeaders` is.

## Scripts

- **`scripts/export-cursor-sessions.py`** — the live exporter.
  - `--backfill` — every JSONL∩header session (idempotent)
  - `--sweep` — only rows with `lastUpdatedAt` newer than `cursor-export-state.json`
  - `--composer-id <uuid>` — one session
  - `--archive-old` — move flat pre-rewrite notes into `_archive-pre-fix/`
- **`scripts/sweep-cursor-sessions.ps1`** — Task Scheduler entrypoint (calls the Python exporter with `--sweep`, logs under `cursor-workflow/logs/`).
- **`scripts/sweep-cursor-sessions-silent.vbs`** — hidden launcher (WindowStyle 0) so the 15-min sweep never pops a console.
- **`scripts/register-cursor-export-task.ps1`** — registers `Jarvis-Cursor-Session-Export` (every 15 min, daily re-arm, hidden via the VBS launcher).
- Legacy (still present, not the live path): `export-cursor-composer.py`,
  `list-cursor-composers.py`, `dump-composer-raw.py`, `cursor-db-run.py`,
  `append-exported-composer.py`, `redact_secrets.py`.

## Trigger — Task Scheduler, not sessionEnd

For `vscode-remote+wsl` workspaces, Cursor loads user hooks from the **WSL**
path (`\home\anant_gupta\.cursor\hooks.json`), confirmed in
`cursor.hooks.workspaceId-*.log`. The Windows
`%USERPROFILE%\.cursor\hooks.json` (merget hooks etc.) is not what fires for
remote WSL sessions. A WSL-side `sessionEnd` cannot reliably open
`state.vscdb` on NTFS while Cursor holds it. So automation is the same
eventually-consistent sweep pattern as Cowork: Windows Task Scheduler →
`sweep-cursor-sessions.ps1`.

## Skip / dedup

Skip if: no `composerHeaders` row, `isDraft` / `isArchived` / `isSubagent`,
or no real assistant turn in the JSONL. Dedup via flat
`_raw_jsonl/<session_id>.jsonl` (WSL copies) or `session_id:` already present
in a project note (Windows junction case).

## Verification

```powershell
py "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\cursor-workflow\scripts\export-cursor-sessions.py" --backfill
py "...\export-cursor-sessions.py" --composer-id "c36b6eba-22c9-445e-bbcf-3e01ba02b2f1"
powershell -File "...\register-cursor-export-task.ps1"
```

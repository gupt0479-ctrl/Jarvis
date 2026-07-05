---
type: reference
status: living
created: 2026-07-05
tags:
  - cursor
  - ai-conversations
  - readme
---
# Cursor Workflow

Mirrors `30_Order/System/claude-workflow/` for Cursor. Exports composer
(chat/agent) conversations out of Cursor's Windows SQLite store into the
Jarvis vault raw-archive format described in
`60_Claude/05_Clippings/AI Conversations/README.md`.

## Where the data actually lives (verified 2026-07-05)

Cursor's real conversation store is Windows-side SQLite, **not**
`~/.cursor/projects/<id>/` (that folder holds agent runtime state — terminals,
MCP config, and a **partial** JSONL mirror covering only ~13% of composers on
this machine).

| Location | Holds | Role here |
|---|---|---|
| `%APPDATA%\Cursor\User\globalStorage\state.vscdb` | 3 tables: `ItemTable`, `cursorDiskKV`, `composerHeaders` (this last one is genuinely empty — verified, 0 rows) | **Primary source** |
| `cursorDiskKV` key `composerData:<uuid>` | Per-conversation metadata + `fullConversationHeadersOnly[]` (ordered list of `{bubbleId, type, grouping, ...}`) | Conversation body |
| `cursorDiskKV` key `bubbleId:<composerId>:<bubbleId>` | One turn. `type: 1` = user, `type: 2` = assistant. Natural-language prose in `.text`; empty `.text` on a type-2 bubble means thinking/tool-only (not a bug) | Turn content |
| `ItemTable` key `composer.composerHeaders` | `{allComposers: [...]}` — discovery index with name, timestamps, workspace URI | Discovery |
| `~/.cursor/projects/*/agent-transcripts/<id>/<id>.jsonl` | Newer Glass/Agent JSONL, Claude-shaped (`role`, `message.content[]` with `text`/`tool_use` blocks) | **Fallback only** — used when SQLite has no row for a composer ID |

Verified counts on this machine (2026-07-05): 183 composers in the
`composer.composerHeaders` index (122 `vscode-remote` / 32 `file` / 29 with
no workspace URI), but **224** `composerData:*` rows in `cursorDiskKV` — 41
composers exist in the raw KV store but fell out of the header index. The
scripts here read `cursorDiskKV` directly for export (so they can still find
those 41) and cross-reference the header index for workspace routing only.
One `composerData` row was observed with a `NULL` value (a tombstone) — the
scripts skip these, they are not errors.

## One pipeline, not two

All conversation data — including for WSL (Remote-WSL) projects — lives in
this same Windows SQLite file. Confirmed by direct WSL filesystem check: no
`~/.config/Cursor`, no `state.vscdb` anywhere under WSL. A WSL workspace just
shows up in the same `composer.composerHeaders` index with a
`vscode-remote://wsl+...` URI. **There is one export script, not a
WSL-side reader** — output is routed to `Windows/Cursor/` or `WSL/Cursor/`
by URI scheme (`file` → windows, `vscode-remote` → wsl), independent of
where the script itself runs (always Windows, since that's where the DB is).

## Scripts

- **`scripts/export-cursor-composer.py --composer-id <uuid> (--output <path> | --output-dir <dir>)`**
  Writes one composer to a raw archive note. Reads SQLite first, falls back
  to agent-transcripts JSONL if the composer has no SQLite row. Redacts
  secrets via `redact_secrets.py` (a line-for-line Python port of the
  `Redact-Secrets` PowerShell function in
  `claude-workflow/scripts/export-claude-session.ps1` — that function is
  inline in the PS script, not a shared file, so this is a deliberate
  duplication rather than a shared module across languages).
- **`scripts/list-cursor-composers.py [--jarvis-only] [--limit N] [--json]`**
  Discovery/preview helper. Cross-references `exported-cursor-composers.json`
  to skip already-exported composers.
- **`scripts/dump-composer-raw.py --composer-id <uuid> --output-dir <path>`**
  Tier 0 only. Writes the composer's full, unredacted `composerData` +
  bubbles as one JSON file. Run by hand — not part of the default export
  path. Destination must be a gitignored `_raw_composer/` folder.
- **`exported-cursor-composers.json`** — flat array of already-exported
  composer UUIDs, same shape as `claude-workflow/exported-claude-sessions.json`.
  Read with `utf-8-sig` (BOM-safe). **Always append via**
  `append-exported-composer.py` — never PowerShell `Set-Content`, which can
  write a BOM and break index parsing.
- **`scripts/append-exported-composer.py <composer-id>`** — append one ID to
  the index without BOM issues.
- **`scripts/cursor-db-run.py <script.py> [args...]`** — WSL helper: retries
  via Windows Python when `/mnt/c/.../state.vscdb` hits `disk I/O error` while
  Cursor is running.

## Known limitation: tool names

Unlike the Claude Code JSONL schema (which has a clean `tool_use.name`
block), no bubble sampled on this machine had a populated `toolResults`
array, and there's no other bubble-level field with a decodable tool name —
`grouping.capabilityType` is a numeric enum with no public mapping. Rather
than guess, `export-cursor-composer.py` emits a generic
`*Tool activity (details omitted)*` marker for type-2 bubbles that have
grouping/tool metadata but empty `.text`, instead of a specific tool name.
This means composers that are mostly tool-driven (long agent runs) will
produce noticeably shorter notes than their raw turn count — that's the
prose-only turns being kept, not a parsing failure. Verified example:
composer `4a4fde38…` has 271 raw header turns but only 32 turns survive into
the exported note, because most of the rest were empty-text
thinking/tool-only bubbles.

## Consent gates already resolved (2026-07-05)

- Tier 0: on-demand `_raw_composer/` dumps only, no standing junction to
  `state.vscdb` (it's commingled across every workspace and unredacted).
- Automation: manual skill invocation (`/export-cursor-session` in Cursor),
  same as Claude Code's `/export-ai-session`. No Cursor hook was added —
  nothing runs without you asking.

## Verification

```powershell
py "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\cursor-workflow\scripts\list-cursor-composers.py" --jarvis-only --limit 5

py "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\cursor-workflow\scripts\export-cursor-composer.py" `
  --composer-id "<uuid>" `
  --output-dir "D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\05_Clippings\AI Conversations\Windows\Cursor"

py "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\cursor-workflow\scripts\append-exported-composer.py" "<uuid>"
```

### WSL (Remote-WSL workspace)

```bash
DB='/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/globalStorage/state.vscdb'
SCRIPTS=/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/cursor-workflow/scripts

python3 "$SCRIPTS/cursor-db-run.py" "$SCRIPTS/list-cursor-composers.py" \
  --jarvis-only --limit 5 --json --db "$DB"
```

If `cursor-db-run.py` still fails, run the same command from Windows
PowerShell (the DB always lives on Windows). See the WSL skill at
`~/.cursor/skills/export-cursor-session/SKILL.md`.

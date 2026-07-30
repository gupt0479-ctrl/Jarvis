---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl
title: "Cursor session exporter design"
started_at: 2026-07-30T18:22:22
ended_at: 2026-07-30T18:23:14
exported_at: 2026-07-30T19:56:24
project: second-brain-claudekit
cwd: "/home/anant_gupta/projects/ai/claude/second-brain-claudekit"
session_id: 64c95dda-5e9d-4fc8-9961-1d1cc77744e9
status: raw
turn_count: 2
tools_used:
  GetMcpTools: 1
  Glob: 3
  Read: 1
  TodoWrite: 1
files_touched:
  - "/home/anant_gupta/.cursor/skills-cursor/create-hook/SKILL.md"
files_changed_count: 5
lines_added: 1054
lines_removed: 0
tags:
  - input
  - ai-conversation
  - cursor
  - wsl
---

# Cursor session exporter design

## You

<timestamp>Thursday, Jul 30, 2026, 6:23 PM (UTC+5:30)</timestamp>
<user_query>
```markdown
# Task: Build the Cursor session exporter for both WSL and Windows, in one pass

## Architecture — confirmed by direct investigation, not assumed

Cursor's session data is split across two stores that must be joined:

1. **Per-session JSONL transcripts** — physically live wherever the
   workspace actually runs: `~/.cursor/projects/**/agent-transcripts/
   <uuid>/<uuid>.jsonl` on WSL (**47 real files**, confirmed via
   `find ... -mindepth/-maxdepth` excluding nested `subagents/`) and the
   same structure natively on Windows at `C:\Users\Anant Gupta\.cursor\
   projects\**\agent-transcripts\**\*.jsonl` (**21 real files**). Shape:
   ```json
   {"role": "user"|"assistant", "message": {"content": [{"type": "text", "text": "..."}, {"type": "tool_use", "name": "Shell", "input": {"command": "...", "description": "..."}}]}}
   ```
   Confirmed: **no `timestamp`, no `usage`, no `model` field anywhere**
   in these files — much leaner than Claude Code's JSONL. Do not assume
   these fields exist; they don't.

2. **A single, still-actively-written SQLite store, Windows-only**:
   `C:\Users\Anant Gupta\AppData\Roaming\Cursor\User\globalStorage\
   state.vscdb` (576MB, modified within the last hour as of this
   writing). It has a `composerHeaders` table:
   ```
   columns: composerId, workspaceId, createdAt, lastUpdatedAt, isArchived, isSubagent, recency, checkpointAt, value
   ```
   `composerId` is the **same UUID as the JSONL filename** — this is the
   join key. `value` is a JSON blob. Confirmed on a real session
   (`[REDACTED]`, this very repo's most recent
   chat):
   ```json
   {"name": "Second brain claude kit", "subtitle": "Edited settings.json, Log.md, MOC.md, Sync - Unison.md", "createdAt": 1785342411186, "lastUpdatedAt": 1785415397875, "filesChangedCount": ..., "totalLinesAdded": ..., "totalLinesRemoved": ..., "isDraft": false, "isArchived": false, ...}
   ```
   `name` is the title-equivalent of Claude Code's `ai-title`. `subtitle`
   is a ready-made files-touched summary. `createdAt`/`lastUpdatedAt` are
   epoch-millisecond timestamps — convert to ISO, no offset, no
   fractional seconds (same normalized format used for the Claude Code
   fixes — don't introduce yet another inconsistent format).
   **Confirmed: no token count, no cost figure, anywhere in this store.**
   Do not fabricate `tokens`/`cost_usd` for Cursor notes — omit those
   frontmatter keys entirely rather than writing zeros or guesses.

   `126` non-archived, non-subagent rows exist in `composerHeaders`
   today; `62` of those have a real (non-draft) `name`. This does **not**
   cleanly match the 68 total JSONL files found (47+21) — reconcile this
   discrepancy for real (some composers may have no JSONL, e.g. very
   short/aborted sessions; some JSONL files may lack a `composerHeaders`
   row) and report the exact reconciled numbers, don't paper over the gap.

3. **Workspace routing** (WSL vs Windows folder): resolve `workspaceId`
   via `%APPDATA%\Cursor\User\workspaceStorage\<workspaceId>\
   workspace.json`, which contains a `folder` URI — `vscode-remote://
   wsl+ubuntu/...` routes to `WSL/Cursor/`, `file:///c:/...` or `file://
   /d:/...` routes to `Windows/Cursor/`. This exact mechanism is already
   anticipated (but not implemented) in `AI Conversations/README.md`'s
   existing Cursor section — read that section first, and update it once
   this is real rather than aspirational.

## Where this must run

The SQLite correlation only works from Windows (that's the only place
the store lives). Build and run this on **Windows** Claude Code, reading
WSL-side JSONL files via `\\wsl.localhost\<distro>\home\anant_gupta\
.cursor\projects\...` (check `wsl -l -v` for the exact distro name, don't
assume `Ubuntu`) and Windows-side ones directly.

## Per-project folder structure — same convention as everything else built so far

`Windows/Cursor/<project-name>/` and `WSL/Cursor/<project-name>/`
(routed per the workspace scheme above), `<project-name>` derived from
the resolved workspace folder path's basename. Each folder gets the same
shape already established: `<MM-DD> <name>.md` per session, `_raw_
jsonl/` (a real junction on the Windows side; a plain one-way copy for
WSL-hosted ones, matching the earlier WSL Claude Code precedent and the
same DrvFs reasoning), `00 - Session Index.md` and `00 - Tool Usage
Rollup.md` as Dataview queries — identical pattern to Claude Code, don't
reinvent it.

## Frontmatter — adapted for what Cursor actually has, nothing fabricated

```yaml
---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl | windows
title: <composerHeaders.value.name>
started_at: <createdAt, converted, normalized ISO format>
ended_at: <lastUpdatedAt, same format>
exported_at: <same format>
project: <resolved workspace folder basename>
cwd: <resolved workspace folder path>
session_id: <composerId>
status: raw
turn_count: <int>
tools_used:
  Shell: <count>
  ... (tally actual tool_use names seen — note these are Cursor's own
       tool names like "Shell", not Claude Code's, don't assume overlap)
files_touched:
  - <derived from tool_use inputs where a path is present, same approach as Claude Code>
files_changed_count: <composerHeaders.value.filesChangedCount, if present>
lines_added: <totalLinesAdded, if present>
lines_removed: <totalLinesRemoved, if present>
tags: [input, ai-conversation, cursor, wsl|windows]
---
```
No `tokens:` or `cost_usd:` keys at all — this data doesn't exist for
Cursor, full stop.

## Skip degenerate sessions

Skip (no note written) if: `isDraft: true`, `isArchived: true` in the
`composerHeaders` value, or the JSONL has no real assistant turn, or no
`composerHeaders` row exists at all. Same philosophy as the Claude Code
junk filter — use the platform's own signal, don't invent a heuristic.

## Actions Taken section

Cursor already hands you `subtitle` and `filesChangedCount`/
`totalLinesAdded`/`totalLinesRemoved` — use those directly as the seed
for the end-of-note `## Actions Taken` section instead of re-deriving
everything from tool calls the way the Claude Code version has to.
Still list the actual tool-call tally too (Shell commands run, etc.).

## Trigger mechanism — investigate before choosing, don't assume

Cursor supports a native `sessionEnd` hook (`~/.cursor/hooks.json` +
`~/.cursor/hooks/*`, confirmed via the `create-hook` skill's own
documentation). Before wiring it as the live trigger, verify **where a
user-level `sessionEnd` hook actually executes for a `vscode-remote+wsl`
workspace** — on the Windows host or inside the WSL remote extension
host — since the SQLite store is only reachable from Windows. If the
hook fires WSL-side for remote workspaces and can't reliably reach the
Windows SQLite file, fall back to a scheduled sweep instead (a Windows
Task Scheduler job that periodically scans `composerHeaders` for rows
newer than the last processed `lastUpdatedAt` and correlates to JSONL) —
the same fallback pattern already used for Cowork, which can't
self-trigger either. State clearly which mechanism you ended up using
and why.

## Existing notes — archive, don't delete

`WSL/Cursor/07-05 Cursor - MCP failure resolution plan.md` (1 file) and
the 3 existing `Windows/Cursor/` notes get archived into `_archive-
pre-fix/` in their respective folders before regenerating everything
fresh under the new per-project structure, per this vault's rule.

## Backfill

All reconciled real sessions across both WSL (47 JSONL) and Windows (21
JSONL), correlated against `composerHeaders`, minus whatever's correctly
skipped as draft/archived/no-header per the rule above.

## Update `AI Conversations/README.md`

Its Cursor section currently describes only the old on-demand `_raw_
composer/` SQLite-only story. Rewrite it to describe what's actually
being built: the two-source join, the per-project folder structure, and
the trigger mechanism you land on.

## Testing

1. Correlate and export at least 3 sessions per OS, including the known
   reference one (`[REDACTED]`, "Second brain
   claude kit") — confirm its title, subtitle-derived actions, and
   timestamps match what's shown above exactly.
2. Confirm the 126-vs-68 reconciliation numbers and explain the gap.
3. Re-run backfill a second time — zero duplicates.
4. Confirm at least one WSL-remote workspace session routes correctly to
   `WSL/Cursor/`, and one Windows-local one to `Windows/Cursor/`.

Report back with: the reconciled real session count per OS, which
trigger mechanism you landed on and why, sample output, and any
blockers — especially if the `sessionEnd` hook execution location
turns out to make the live-trigger approach unworkable.
```
</user_query>

## Cursor

I'll build the Cursor session exporter against the confirmed architecture. First I'm reading the existing Claude Code exporter pattern, the Cursor README section, and the create-hook skill so the design matches what's already in the vault.

**Tool calls:**

- `TodoWrite` — `{"todos":[{"id":"1","content":"Explore existing exporters, README, vault structure, hooks","status":"in_progress"},{"id":"2","content":"Investigate sessionEnd hook execution location (WSL vs Windows)","status":"pending"},{"id":"3","content":"Build Cursor exporter (Windows-side, join SQLite + JSONL)"…`
- `Read` — `/home/anant_gupta/.cursor/skills-cursor/create-hook/SKILL.md`
- `GetMcpTools` — `{"server":"user-jarvis"}`
- `Glob` — pattern `**/AI Conversations/**/*`, path `.`
- `Glob` — pattern `**/*export*cursor*`, path `.`
- `Glob` — pattern `**/*claude*export*`, path `.`

## Actions Taken
- Summary: Edited export-cursor-sessions.py, _run-backfill.ps1, _run-ref-test.ps1, register-cursor-export-task.ps1, sweep-cursor-sessions.ps1
- Files changed (Cursor): 5
- Lines: +1054 / -0
- Files touched (from tool calls): /home/anant_gupta/.cursor/skills-cursor/create-hook/SKILL.md
- Commands run: (none)
- Tool call tally: GetMcpTools (1), Glob (3), Read (1), TodoWrite (1)

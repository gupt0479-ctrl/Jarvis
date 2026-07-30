---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl
title: "Cursor AI conversation pipeline"
started_at: 2026-07-05T18:02:57
ended_at: 2026-07-05T18:16:37
exported_at: 2026-07-30T19:56:24
project: CausalOps
cwd: "/home/anant_gupta/projects/hub/CausalOps"
session_id: a00cc305-b6a8-4cc0-a2ae-0b860c267fb4
status: raw
turn_count: 2
tools_used:
  Glob: 6
  Read: 2
  Shell: 4
files_touched:
  - "/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/mcps/user-jarvis-fs"
  - "/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/mcps/user-jarvis-fs/tools/list_allowed_directories.json"
  - "/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/mcps/user-jarvis-fs/tools/read_text_file.json"
files_changed_count: 0
lines_added: 0
lines_removed: 0
tags:
  - input
  - ai-conversation
  - cursor
  - wsl
---

# Cursor AI conversation pipeline

## You

<timestamp>Sunday, Jul 5, 2026, 6:16 PM (UTC+5:30)</timestamp>
<user_query>
Task: build an AI-conversation archive pipeline for Cursor (Windows + WSL), matching a pipeline already built for Claude Code in this same vault.

## Context

This vault (`D:\Users\_Anant\10_Areas\Documents\Jarvis`) just got a working pipeline that captures Claude Code sessions into curated notes. You're building the Cursor equivalent — same philosophy, different mechanics, because Cursor stores its data completely differently than Claude Code does.

Read these first, in this order:
1. `60_Claude/05_Clippings/AI Conversations/README.md` — raw-archive frontmatter schema and naming convention you must match (just with `source_app: cursor` instead of `claude-code`)
2. `60_Claude/07_AI_Information/AI Conversation - Summaries/README.md` — the distilled-summary template you must match exactly
3. `30_Order/Workflows/Conversation Capture.md` — the three-layer philosophy (raw archive → distilled summary → manual promotion)
4. `30_Order/System/claude-workflow/scripts/export-claude-session.ps1` — the Claude Code reference implementation. Copy its *approach* (strip tool-call payloads, keep only natural-language text, redact secrets with regex, matching frontmatter schema) — do not copy its *parsing logic*, since Cursor's data format is not JSONL.
5. `C:\Users\<your-user>\.claude\skills\export-ai-session\SKILL.md` — the global-skill pattern this mirrors, if you can read outside-repo paths.

Destination folders already exist and are empty, waiting for you:
- `60_Claude/05_Clippings/AI Conversations/Windows/Cursor/`
- `60_Claude/05_Clippings/AI Conversatio
Distilled summaries always go to `60_Claude/07_AI_Information/AI Conversation - Summaries/`, alongside the
Claude Code ones already there.

## Step 1 — Find out where your own conv(do this before designing anything)

Do not assume a schema. I already checkedead end:`C:\Users\<user>\.cursor\projects\<id>\` (your CLI-agent directory, structurally similar to Claude Code's
`.claude\projects\`) only contains `termrollback) and empty `canvases\` folders — no actual chat/composer text. `ai-tracking\ai-code-tracking.db` also exists there but looks like it tracks
code diffs, not conversations.

The real chat/composer history is most lfork storage instead:
- `%APPDATA%\Cursor\User\workspaceStorage\<hash>\state.vscdb` (per-workspace, SQLite)
- `%APPDATA%\Cursor\User\globalStorage\s
                                                                                               Query these directly (sqlite3 or Python)ames holding conversation content in thecurrently installed Cursor version — they've changed across versions (historically things like `composer.composerData`, `aiService.prom...`) and I don't have current, verifiedknowledge of the exact schema. Report what you find before writing a parser against it.                    
There's also an existing raw mirror at `20_Progress/AI/Cursor/.cursor_windows/` and `.cursor_wsl/`         (gitignored, pasted from a past session)ul, but treat it as a stale snapshot, not a live source.                                                                                             
## Step 2 — Resolve the Windows/WSL question honestly                                                      
Claude Code has a genuinely separate `~/.claude` per OS (Windows and WSL each run their own CLI, own configown history) — that's why its vault folds/` and `WSL/`. Cursor may not work thesame way: it's an Electron GUI app whose main process runs on Windows even when editing a WSL-mounted foldeover Remote-WSL, so a WSL-opened project sit in the *same* Windows-side`workspaceStorage` database, distinguished only by a `vscode-remote://wsl+...` workspace URI — not in a    physically separate store inside the WSL
                                                                                                           Check for this directly: is there a `~/. inside the WSL filesystem holding itsown conversation data, or does everything trace back to the Windows-side SQLite regardless of which folder open? Report the actual answer before bu that might turn out to be reading thesame underlying data twice.                                                                                
## Step 3 — Build the pipeline, once the format is confirmed                                               
Same two-or-three-tier structure as the Claude Code build:                                                 - **Tier 0 (optional, zero-token):** a renuinely separatesper-project/per-workspace the way Claude Code's does. If Cursor's data is one commingled database across evproject on the machine, don't force a juuivalent (e.g., a filtered exportscript) instead of copying the whole database in.                                                          - **Tier 1 (mechanical, near-zero token)e conversation into one markdown file,keeping only natural-language turns (never raw tool commands/output), redacting secrets, matching the      raw-archive frontmatter/naming schema exfiled under `Windows/Cursor/` or`WSL/Cursor/` per what Step 2 found).                                                                      - **Tier 2 (costs tokens, curated):** anhat Was Decided / What Changed /Important Context / Source Claims / Inferred Claims / Open Questions / Follow-Up Actions / Related Notes / Should Be Promoted? — written to `AI Con for conversations worth keeping, noteverything.

Redaction, at minimum: known key prefixes (`sk-`, `sk-ant-`, `ghp_`, `xox[baprs]-`, `AKIA`, `Bearer <tokenand a fallback rule for any bare 24+ chareal pasted API key was found incleartext in a Claude Code transcript during the equivalent build — assume Cursor transcripts carry the sarisk, since it's the same user pasting tway.
                                                                                                          ## Hard rules, non-negotiable
                                                                                                          - **Never create a standing/global confin always-on rule, anything that runsautomatically on every future session) **or a filesystem junction/symlink into a directory holding credentor unredacted session data, without stopicitly first.** Don't infer consent forthese from "build the pipeline" — surface the specific decision and wait for a direct answer. This bit me twice during the Claude Code build (a glnction were both attempted on inferredconsent and correctly blocked; both went through fine once asked directly).                               - **Any raw mirror or junction you do crnore` in the same turn**, following theexisting pattern (`60_Claude/05_Clippings/AI Conversations/**/_raw_jsonl/` is already there for Claude Codnever leave one sitting unignored in thifly.
- **`60_Claude/05_Clippings/` is append-only** — new files only, never edit a previously-written raw captuin place.
- Before writing large amounts of content, propose your concrete findings (where the data actually lives, whether Windows/WSL are really separate)-check — the format is genuinelyuncertain going in, and guessing wrong here wastes real effort.

Scope: Cursor only, Windows and WSL both (pending what Step 2 actually finds — they may collapse into one pipeline). Kiro is a separate, later tas
</user_query>

## Cursor

Researching the Jarvis vault reference files and probing Cursor's conversation storage on this machine before drafting the pipeline plan.

[REDACTED]

Reference files aren't in the CausalOps repo — checking the Jarvis vault via MCP and probing Cursor storage locations.

[REDACTED]

[REDACTED]

**Tool calls:**

- `Glob` — pattern `**/60_Claude/05_Clippings/AI Conversations/README.md`, path `.`
- `Glob` — pattern `**/export-claude-session.ps1`, path `.`
- `Glob` — pattern `**/Conversation Capture.md`, path `.`
- `Glob` — pattern `**/.cursor_windows/**`, path `.`
- `Glob` — pattern `**/export-ai-session/SKILL.md`, path `.`
- `Glob` — pattern `**/*`, path `/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/mcps/user-jarvis-fs`
- `Shell` — `ls -la "/mnt/c/Users" 2>/dev/null | head -20; ls -la "/mnt/d/Users" 2>/dev/null | head -20; ls -la ~/.cursor/projects/ 2>/dev/null | head -15`
- `Shell` — `find ~/.cursor -maxdepth 4 -type f \( -name "*.vscdb" -o -name "*.db" -o -name "*.jsonl" \) 2>/dev/null | head -40`
- `Read` — `/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/mcps/user-jarvis-fs/tools/list_allowed_directories.json`
- `Read` — `/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/mcps/user-jarvis-fs/tools/read_text_file.json`
- `Shell` — `ls -la "/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/" 2>/dev/null; ls "/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/workspaceStorage/" 2>/dev/null | head -10; ls "/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/globalStorage/" 2>/dev/null | head -20`
- `Shell` — `find ~/.cursor -type f 2>/dev/null | head -50; ls -la ~/.cursor/ 2>/dev/null; ls -la ~/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/ 2>/dev/null`

## Actions Taken
- Summary: Read read_text_file.json, list_allowed_directories.json
- Files changed (Cursor): 0
- Lines: +0 / -0
- Files touched (from tool calls): /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/mcps/user-jarvis-fs, /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/mcps/user-jarvis-fs/tools/list_allowed_directories.json, /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/mcps/user-jarvis-fs/tools/read_text_file.json
- Commands run: ls -la "/mnt/c/Users" 2>/dev/null | head -20; ls -la "/mnt/d/Users" 2>/dev/null | head -20; ls -la ~/.cursor/projects/ 2>/dev/null | head -15, find ~/.cursor -maxdepth 4 -type f \( -name "*.vscdb" -o -name "*.db" -o -name "*.jsonl" \) 2>/dev/null | head -40, ls -la "/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/" 2>/dev/null; ls "/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/workspaceStorage/" 2>/dev/null | head -10; ls "/mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/globalStorage/" 2>/dev/null | head -20, find ~/.cursor -type f 2>/dev/null | head -50; ls -la ~/.cursor/ 2>/dev/null; ls -la ~/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/ 2>/dev/null
- Tool call tally: Glob (6), Read (2), Shell (4)

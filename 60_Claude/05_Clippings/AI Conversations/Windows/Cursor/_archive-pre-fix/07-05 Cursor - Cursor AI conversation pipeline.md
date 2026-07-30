---
type: input
input_kind: ai-conversation
source_app: cursor
title: "Cursor AI conversation pipeline"
started_at: 2026-07-05T13:47:17
ended_at: 2026-07-05T13:47:20
status: raw
composer_id: c160a19f-5865-481f-a6d3-01e91cdab3a1
workspace_uri: 'file:///d%3A/Users/_Anant/10_Areas/Documents/Jarvis'
workspace_env: windows
tags:
  - input
  - ai-conversation
  - cursor
---

# Cursor AI conversation pipeline

## You

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

Scope: Cursor only, Windows and WSL both (pending what Step 2 actually finds — they may collapse into one pipeline). Kiro is a separate, later task

## Cursor

Investigating Cursor's conversation storage and reviewing the Claude Code pipeline docs to draft an accurate plan.

## Cursor

Searching Cursor's SQLite stores and the vault's existing pipeline structure.

## Cursor

Confirming SQLite is the authoritative store; agent-transcripts JSONL is a partial parallel for newer Glass sessions. Creating the plan.

## You

<system_notification>
The following task has finished. If you were already aware, ignore this notification and do not restate prior responses.

<task>
kind: shell
status: success
task_id: 709153
title: Search WSL for Cursor SQLite databases
output_path: C:\Users\Anant Gupta\.cursor\projects\empty-window\terminals\709153.txt
</task>
</system_notification>
<user_query>Briefly inform the user about the task result and perform any follow-up actions (if needed). If there's no follow-ups needed, don't explicitly say that.</user_query>

## Cursor

## Investigation complete

**WSL search:** No separate conversation database in WSL. No `~/.config/Cursor`, no WSL-local `state.vscdb`. WSL `~/.cursor/` only has config (skills, hooks, project slugs). All chat history lives in the Windows Electron profile.

**Where Cursor actually stores conversations:**
- **Primary:** `%APPDATA%\Cursor\User\globalStorage\state.vscdb` (~430 MB) — `composerData:<uuid>` + `bubbleId:<composerId>:<bubbleId>` entries (type 1 = user, type 2 = assistant)
- **Index:** `composer.composerHeaders` → 183 composers (122 WSL, 32 local)
- **Partial fallback:** `~/.cursor/projects/*/agent-transcripts/*.jsonl` (~24 files, Claude-like format) — same sessions also exist in SQLite
- **Not sufficient alone:** `aiService.generations` in per-workspace DBs (user prompts only)

**Windows/WSL:** One pipeline, not two. WSL projects use `vscode-remote://wsl+...` URIs in the same Windows SQLite. Exports can route to `WSL/Cursor/` vs `Windows/Cursor/` by workspace scheme without reading data twice.

A full implementation plan is ready in the plan file. Before building, two items need your explicit sign-off (same gates as the Claude Code build):

1. **Tier 0 raw safety net** — recommended: on-demand per-composer JSON dumps to gitignored `_raw_composer/` (not a junction to the 430 MB DB)
2. **No automatic hooks** — export stays manual via `/export-cursor-session` unless you ask for a standing hook

Say the word when you want implementation to start, and confirm Tier 0 preference if you have one.

## You

I built a Cursor-to-Jarvis conversation archive pipeline in a Claude Code session and need you to finish the last mile and do the first real production run. Full context so you don't have to rediscover any of it:

What this is: Jarvis is a vault at D:\Users\_Anant\10_Areas\Documents\Jarvis. It already has a working Claude Code conversation-archive pipeline (30_Order/System/claude-workflow/, skill ~/.claude/skills/export-ai-session/). I've now built the equivalent for Cursor.

Verified facts about this machine (confirmed via direct SQLite queries, don't re-derive):
- Cursor's conversation data lives entirely in Windows %APPDATA%\Cursor\User\globalStorage\state.vscdb (SQLite) â true even for WSL/Remote-WSL workspaces. No ~/.config/Cursor, no local DB anywhere in WSL. One pipeline, not two.
- Schema: table cursorDiskKV, keys composerData:<uuid> (has fullConversationHeadersOnly[]) and bubbleId:<composerId>:<bubbleId> (type:1=user, type:2=assistant, prose in .text).
- Discovery index composer.composerHeaders (in ItemTable) had 183 composers (122 vscode-remote=WSL / 32 file=Windows / 29 no-URI) but there are 224 composerData:* rows in raw cursorDiskKV â 41 fell out of the index but still have data. Scripts read cursorDiskKV directly so nothing is missed.
- No bubble-level field reliably names which tool ran (unlike Claude Code's tool_use.name). Exports mark tool-only turns as generic *Tool activity (details omitted)*. Long agentic composers export noticeably shorter than their raw turn count (verified: a 271-turn composer kept onlyÂ 32) â expected, not a bug.
- Redaction is a standalone Python port (redact_secrets.py), not shared with the PowerShell Claude pipeline (which has it inline, not as a separate file).

Already built and tested â D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\cursor-workflow\: export-cursor-composer.py, list-cursor-composers.py, dump-composer-raw.py (Tier 0, on-demand only), redact_secrets.py, exported-cursor-composers.json ([]), README.md. Output routing: file workspaces â Windows/Cursor/, vscode-remote â WSL/Cursor/ (both folders exist). _raw_composer/ is gitignored, populated only on explicit request. Global skill at C:\Users\Anant Gupta\.cursor\skills\export-cursor-session\SKILL.md.

Consent decisions already locked in â don't re-litigate: Tier 0 is on-demand dumps only, no standing junction. Automation is manual-skill-only (/export-cursor-session), no hook â mirrors Claude Code's original pattern. (Claude Code itself was later upgraded elsewhere to a fully automatic SessionEnd hook; Cursor deliberately isn't yet â that's intentional, ask before changing it.)

What's actually left â your job:
1. Fix skill visibility for WSL workspaces. I only placed the skill on the Windows side. WSL has its own separate ~/.cursor/skills/ directory (distinct from ~/.cursor/skills-cursor/, which is Cursor's built-in managed-skills mirror, not user skills) â confirmed directly. A Cursor window opened against a WSL project currently can't see /export-cursor-session at all. Mirror the skill to /home/anant_gupta/.cursor/skills/export-cursor-session/SKILL.md, adjusted for WSL paths: scripts at /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/cursor-workflow/scripts/, DB at /mnt/c/Users/Anant Gupta/AppData/Roaming/Cursor/User/globalStorage/state.vscdb (pass via --db). The scripts are pure Python/pathlib with no Windows-only path assumptions, so python3 against those /mnt/... paths should work â verify it actually runs rather than assuming.
2. Do the first real production run. Everything so far was only tested against throwaway /tmp files â no composer has actually been exported into the vault yet. Run /export-cursor-session for real, pick a handful of meaningful composers, and actually write the raw notes + summaries + log entry + index update.
3. Skim the real output for redaction misses before calling it done.
4. Report back: what got exported (Windows vs WSL), whether the WSL mirror worked end-to-end, anything hand-redacted.

## Cursor

Finishing the last mile: reading the existing pipeline, mirroring the skill for WSL, then running the first production export.

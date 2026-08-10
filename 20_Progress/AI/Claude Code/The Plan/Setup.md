---
type: input
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - claude-code
  - sync
  - claude-kit
notes:
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: None — the last target onboarded this pass; genuinely new discovery, not a re-run of a known plan
---
# The Plan — Setup
This note is Jarvis-only. It is never read or written by the sync itself — `sync-all.sh` never touches it, it carries no `paths` entry in the manifest. It exists purely to tell a Jarvis reader what's actually in this folder and how it got that way.
## What this is — a correction to earlier research
Earlier passes (2026-07-30, and again in this session's own research phase) concluded "The Plan is likely a separate Obsidian vault, not a code project — no matching repo found under `~/projects`." That conclusion was **half right and half wrong**: it's correct that this isn't a WSL code project, but wrong that there's nothing to sync. "The Plan" is a real, separate Windows-side Obsidian vault at `D:\Users\_Anant\10_Areas\Documents\The Plan`, git remote `gupta-builds/Obsidian-SecondBrain`, with its own genuine live `.claude/` config — the earlier searches only looked under `~/projects` (WSL) and never checked the Windows-native sibling-vault path directly. Confirmed by direct inspection 2026-08-10, not assumed. Rebuilt clean the same session it was correctly identified — everything except this Setup.md was deleted from the old flat dump and the folder was fully repopulated by a fresh sync.
## Sync scope
Bidirectional, via `second-brain-claudekit/60_Claude/scripts/sync-all.sh`, manifest entry `The Plan`, `needs_fat: true` (same-drive Windows-native pairing, like `Jarvis` — both replicas are still DrvFs from the executing WSL process's point of view). Synced paths: `.claude/agents`, `.claude/skills`, `.claude/settings.json`, root `CLAUDE.md`, root `AGENTS.md`. Not synced: `.claude/settings.local.json` (machine-local).
## What's actually here
- `.claude/agents/` — 3 files: `career-operator.md`, `research-distiller.md`, `vault-curator.md` — the same agent *names* Jarvis itself uses, adapted for this vault rather than shared.
- `.claude/skills/` — 10 files: `closeday.md`, `connect-notes.md`, `context.md`, `distill-note.md`, `ingest-clipping.md`, `lint-claude-layer.md`, `organize-csci2033.md`, `today.md`, `trace-topic.md`, `weekly-review.md`.
- `.claude/settings.json` — scoped tightly to one MCP server (`obsidian`) with explicit per-tool permissions (read/get/search/write/patch/append/manage-frontmatter/manage-tags/replace) — narrower than Jarvis's own `settings.json`.
- `CLAUDE.md` — this vault's own operating contract: an older PARA-ish folder scheme (`60_Claude/05_Clippings`, `10_Session_Logs`, `20_Distilled_Notes`, `30_Source_Summaries`, `40_Project_Briefs`, `50_Reviews`, `60_Indexes`) — visibly an earlier stage of the same conventions Jarvis itself now uses, not identical to Jarvis's current structure.
- `AGENTS.md` — present alongside `CLAUDE.md`.
## Verification performed
Both directions and the conflict path tested for real with a throwaway file (`.claude/skills/_sync_test.md`), same battery as every project target this session:
1. Created on the Jarvis-mirror side, synced, confirmed it landed in the real vault at `D:\...\The Plan\.claude\skills\`.
2. Edited on The Plan's own side, synced, confirmed the edit landed back in the mirror.
3. Edited differently on both sides without syncing in between, synced: Unison reported the conflict and **both edits stayed intact**.
4. Deleted from both sides, synced once more, confirmed a clean no-op.
## Trigger
Live on the 15-minute Windows Scheduled Task `ClaudeKit-Sync-All` as of 2026-08-10.

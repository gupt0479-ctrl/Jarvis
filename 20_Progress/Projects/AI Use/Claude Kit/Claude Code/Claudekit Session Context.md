---
type: reference
status: active
created: 2026-08-11
updated: 2026-08-19
tags:
  - claude-kit
  - second-brain-claudekit
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Prompts]]"
next: null
---
# Claudekit Session Context
==Everything a session working inside `second-brain-claudekit` needs to know, split out from [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Prompts]] on 2026-08-19 so that note holds only pasteable prompts, per its own standing rule.==

## Facts verified true as of 2026-08-11 (re-verify before trusting — 8 days old already)
- The Jarvis mirror (`20_Progress/AI/Claude Code/second-brain-claudekit/`) is **view-only, by decision** — never edit it directly. Edit the real repo; `60_Claude/scripts/sync-all.sh` (every 15 min) carries it to Jarvis automatically. Mechanically enforced: `sync-manifest.json`'s `second-brain-claudekit` entry carries `"force_source": true` — on a genuine conflict, the repo's version wins automatically.
- The sync layer (all 10 manifest entries) was live and verified working as of 2026-08-11.
- `60_Claude/30_Reviews/AI/Tools/Tool log.md`, `30_Order/Standards/Review Standard.md`, and the two `AI Tools Weekly/Monthly Review Template.md` files exist and are real (built 2026-08-10/11) — see [[10_Areas/AI/Setup/Review System]] for the full write-up.
- **Conversation capture (Windows + WSL Claude Code, Cowork) is being rebuilt separately, in progress as of 2026-08-19 — do not touch it from a claudekit-repo session.** It is not this repo's concern; it lives in global/Jarvis-side hook config.

## What to check in Jarvis before reviewing or improving any tool in this repo
| Jarvis path | Answers |
|---|---|
| `60_Claude/30_Reviews/AI/Tools/Tool log.md` | Which skill/command/agent was used, when, on what, and whether it worked cleanly — the first stop, not the raw sessions |
| `60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/<project>/` and `Windows/Claude Code/<project>/` | The actual session transcript for a Tool log row that needs more depth |
| `20_Progress/AI/Claude Code/_All-Projects-Sync-Log.md` | Whether this repo's own sync (and every other project's) is actually running clean |
| `20_Progress/Projects/AI Use/Claude Kit/Log.md` | Structural changes to the sync/mirror layer itself, chronological — absorbed `Write Log.md`'s scope 2026-08-20 when that file was retired |
| `20_Progress/Projects/AI Use/Claude Kit/Tool Map.md` | Pipeline stage for every tool this repo has ever sandboxed — check before assuming something needs re-evaluating from scratch |
| `60_Claude/30_Reviews/AI/Scheduled/Weekly/` and `.../Monthly/` | Already-synthesized findings — check before re-deriving something a review already covered |

## The per-destination-project staging idea (2026-08-11, still the plan — repurposed 2026-08-19)
The repo-root staging folders (`agents/`, `commands/`, `hooks/`, plus a new `docs/` for pure-canon per-project documents) should eventually be subfoldered by **destination project**, e.g. `skills/CausalOps/research-mcp-loop.md`, `agents/CausalOps/...`. Create subfolders only as real content actually lands — no empty scaffolding for projects with nothing staged yet. `skills/` keeps its existing role (source-repo-provenance staging via `sandbox/` → `tested-tools/`) — this destination-project convention is for the *other* three folders, once their current zero/partial-provenance scaffold content (see the 2026-08-19 Claudekit prompt) has been cleared out to `tested-tools/`. **This staging content is drafted here, promoted from here — never auto-promoted.** A file sitting in `agents/CausalOps/` is not live in CausalOps until someone deliberately copies it into CausalOps's real `.claude/` after it clears `_docs/Promotion-Criteria.md`'s bar.

## Open, not fully decided
- **Resolved 2026-08-19**: whether a `tests/` directory belongs alongside `sandbox/`/`tested-tools/` — yes, scoped as this repo's strictest gate. See the 2026-08-19 Claudekit prompt and `_docs/Gaps.md`/`_docs/Repo-Map.md` in the repo.
- Exactly how content moves from a project's real, already-synced `.claude/` (e.g. `20_Progress/AI/Claude Code/CausalOps/.claude/agents/`) into this repo's per-destination-project staging folders. Direction is settled (project → Jarvis → claudekit, for review, never the reverse); mechanism isn't — likely a script, likely Jarvis-side since it only touches already-mirrored files. Not built yet. Don't build it without confirming the design first.

## Links
[[20_Progress/AI/Claude Code/Sync - Unison]] for sync mechanics. [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] for current pipeline state. [[30_Order/Standards/Review Standard]] for the review process. [[10_Areas/AI/Setup/Review System]] for the full review-system write-up (2026-08-19).

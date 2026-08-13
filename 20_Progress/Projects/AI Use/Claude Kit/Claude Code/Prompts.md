---
type: input
status: active
created: 2026-08-11
updated: 2026-08-11
tags:
  - claude-kit
  - prompts
  - second-brain-claudekit
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
next: Paste the prompt below into a fresh Sonnet 5 session with cwd = ~/projects/ai/claude/second-brain-claudekit
---
# Claude Kit — Build Prompts
==Prompts for a session working directly inside second-brain-claudekit (WSL), written from the Jarvis side per this repo's own convention (`_docs/Jarvis.md`) — not written or refined inside the repo itself.==
## Context this session needs, verified true as of 2026-08-11
- The Jarvis mirror (`20_Progress/AI/Claude Code/second-brain-claudekit/`) is **view-only from now on, by decision** — never edit it directly. Edit the real repo; the existing Unison leg (`60_Claude/scripts/sync-all.sh`, every 15 min) carries it to Jarvis automatically. This is now also mechanically enforced, not just a remembered rule: `sync-manifest.json`'s `second-brain-claudekit` entry carries `"force_source": true`, which `sync-all.sh` translates into Unison's `-force <repo_root>` — on a genuine conflict (same file changed on both sides), the repo's version wins automatically instead of the sync stalling on a skipped conflict.
- The sync layer (all 10 manifest entries — every tracked project plus both home directories) is live and verified working, not just registered — confirmed 2026-08-11 by a live test run, all 10 `OK`.
- Conversation capture (both Windows and WSL Claude Code, plus Cowork) is now fully live: `SessionEnd` **and** `Stop` both trigger export (Stop fires after every turn — far more reliable than SessionEnd alone, which depends on a clean process exit). A 30-minute scheduled `-BackfillAll` safety net exists on both platforms. Every session note carries real tool-call detail, tokens, and cost — this is the data source for tool-use review.
- `60_Claude/30_Reviews/AI/Tools/Tool log.md` now exists (structure defined, empty) — the per-skill-use log `/export-ai-session` writes to going forward.
- `30_Order/Standards/Review Standard.md` plus `AI Tools Weekly/Monthly Review Template.md` now exist — the gated review process (100% clarity required before any auto-fix, per this repo's own `_docs/Design.md` sequencing) is defined.
## What this session is for
Two things, in order. Don't skip to the second before the first is real.
### 1. Build the per-project staging structure inside this repo
Reorganize the repo-root staging folders (`agents/`, `commands/`, `hooks/`, `skills/` — confirmed by `_docs/Repo-Map.md` as the pre-`.claude/` drafting area, distributed elsewhere once ready) to be subfoldered by destination project, e.g.:
```
skills/CausalOps/research-mcp-loop.md
skills/CausalOps/research-mcp-loop/template.md   (if the skill needs a directory shape)
agents/CausalOps/...
commands/CausalOps/...
hooks/CausalOps/...
```
Add a fifth folder, `docs/`, for per-project markdown that isn't an executable artifact — the same shape Resq's and OpsPilot's real `.claude/` already use for pure canon documents (PRD, context, playbooks). Not every project needs every subfolder populated; create them as real content actually lands, not as empty scaffolding for projects with nothing staged yet.
**This staging content is drafted here, promoted from here — never auto-promoted.** Nothing in this reorganization changes `_docs/Promotion-Criteria.md`'s bar or the sandbox → tested-tools → promoted pipeline. A file sitting in `skills/CausalOps/` is not live in CausalOps until someone deliberately copies it into CausalOps's real `.claude/` after it clears the bar — exactly the existing manual ritual in `_docs/Jarvis.md`, unchanged.
### 2. Write the "what to look for in Jarvis" reference
This repo needs a standing reference — in `CLAUDE.md` or a new `_docs/` file, your call — naming exactly which Jarvis directories to check before improving a tool, and what each one answers. Not a file watcher, not new automation — this repo's own `_docs/Design.md` already committed to "the qualification pipeline runs solidly first, evidence accumulates, only then is automation decided" (2026-08-09), and inventing a trigger mechanism now would violate that sequencing. Write it as a checklist a session (manual, or run when explicitly asked to "review and improve") works through:
| Jarvis path | Answers |
|---|---|
| `60_Claude/30_Reviews/AI/Tools/Tool log.md` | Which skill/command/agent was used, when, on what, and whether it worked cleanly — the first stop, not the raw sessions |
| `60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/<project>/` and `Windows/Claude Code/<project>/` | The actual session transcript for a Tool log row that needs more depth — real tool calls, real arguments, real narration |
| `20_Progress/AI/Claude Code/_All-Projects-Sync-Log.md` | Whether this repo's own sync (and every other project's) is actually running clean |
| `20_Progress/AI/Claude Code/Write Log.md` | Structural changes to the sync/mirror layer itself, chronological |
| `20_Progress/Projects/AI Use/Claude Kit/Tool Map.md` | Pipeline stage for every tool this repo has ever sandboxed — check before assuming something needs re-evaluating from scratch |
| `60_Claude/30_Reviews/AI/Scheduled/Weekly/` and `.../Monthly/` | Already-synthesized findings — check here before re-deriving something a review already covered |
## Open, not decided — bring back to Jarvis rather than deciding alone
- Whether a `tests/` directory belongs alongside `sandbox/`/`tested-tools/` for a distinct purpose, or whether `tested-tools/`'s existing second-look stage already covers it — named as a maybe, not resolved.
- Exactly how content moves from a project's real, already-synced `.claude/` (already sitting in its own Jarvis mirror folder, e.g. `20_Progress/AI/Claude Code/CausalOps/.claude/agents/`) into this repo's new per-project staging folders. The direction is settled (project → Jarvis → claudekit, for review, never the reverse), but the mechanism isn't — likely a script, likely Jarvis-side since it only touches already-mirrored files sitting in Jarvis, but not built yet. Don't build it from this session without confirming the design first.
## Links
[[20_Progress/AI/Claude Code/Sync - Unison]] for the sync mechanics this depends on. [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] for current pipeline state. [[30_Order/Standards/Review Standard]] for the review process this repo's own tool improvements should eventually feed into.

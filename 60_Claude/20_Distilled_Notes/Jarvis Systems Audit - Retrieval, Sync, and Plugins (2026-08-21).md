---
type: evergreen
status: sprout
created: 2026-08-21
tags:
  - audit
  - meta
  - retrieval
  - plugins
notes:
  - "[[Jarvis OS — North Star]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[Jarvis Writing and Formatting]]"
  - "[[40_Resources/Obsidian/Plugins/Plugin Inventory and Configuration Map]]"
  - "[[40_Resources/Obsidian/Plugins/Plugin Gaps Recommendations and Verification]]"
  - "[[40_Resources/Obsidian/Plugins/Spaced Repetition and Learning Loops]]"
  - "[[Sync - Unison]]"
  - "[[Ingestion Pipeline Audit — Clippings, Summaries & Implementation (2026-07-27)]]"
next: "Verify Spaced Repetition's effective config layer in Settings, then scope the Cursor sync manifest to skills-cursor/ and plans/ only"
---
# Jarvis Systems Audit - Retrieval, Sync, and Plugins (2026-08-21)
A conversation-only session (no vault writing until the end, by explicit instruction) that started from one question - how to use Obsidian to cut the token cost of working with Jarvis toward zero - and turned into a full forensic pass across the retrieval layer, the cross-repo sync system, and the plugin stack. The session's own method was itself a finding: nearly every claim below started as an assumption and got overturned or sharpened by actually running a tool or reading a file, several times correcting something stated earlier in the same conversation.
## Session goal and decisions locked
Three decisions were made explicitly before any fix work, and they should govern anything built from this note:
1. **Resume [[Jarvis OS — North Star]]'s convergence plan rather than redesigning from scratch.** Its four-move sequence is still the right strategy; only the order of Move 4's sub-steps changes (below).
2. **Multi-repo rule enforcement (why other synced repos don't always follow Jarvis's own rules) is explicitly out of scope for this session.** It is a real, separate problem, not folded into this audit.
3. **"Cut token cost" means both interactive Claude Code sessions in Jarvis and the automated pipelines that write into it** (the GitHub Actions internship loop, the Unison sync, the capture backfill) - not just one or the other.
The North Star's own Part 5.4 growth path for `jarvis-memory` goes indexer boundary unfixed, straight to semantic search. This session reordered that, and the reorder is now the standing plan: **fix the indexer/scan boundary, then close the frontmatter type vocabulary, then populate the link graph from existing wikilinks, then consider semantic search.** Reasoning: semantic search ranks over whatever set of notes it's given; ranking a polluted set just produces better-ranked garbage. The cheaper, higher-leverage fixes come first.
## Finding 1 - the registry and every vault-wide tool index vendor noise, not just vault content
`jarvis-memory/registry.py` line 60 runs `root.rglob("*.md")` with no exclusion list at all. It walks every markdown file under the vault root, including files that were never meant to be vault knowledge. Verified counts:
- **1,425 markdown files** under `20_Progress/AI/Cursor/.cursor_windows/plugins/cache/` and its WSL twin - vendored plugin documentation bundled with Cursor extensions (Sanity, Vercel, etc.), identical on any machine with the same plugins.
- **638 markdown files** under some `node_modules/` folder somewhere in the vault tree (for example `30_Order/System/excalidraw-mcp/node_modules/cytoscape/`).
- `jarvis_status` reports 8,173 notes indexed with frontmatter `type:` values including `code`, `rationale`, `class`, `community`, `runbook`, `decision-log` - none of them in the vault's own type guide. These are vendor docs' own frontmatter, not vault content, leaking into a field every North Star Part 6 retrieval rule assumes is a closed vocabulary.
- `jarvis-cli health` scans a different set (5,997 files) and reports 448 duplicate filenames - 582 `README.md`, 214 `SKILL.md`, 128 `configuration.md`, 123 `api.md`, 122 `gotchas.md`, 122 `patterns.md`. That exact shape (gotchas.md, patterns.md, configuration.md, api.md) is the signature of Cursor's plugin-cache file layout, not vault duplication.
This happened live, in this very session: the first `Glob` search for `AGENTS.md` returned six vendor-cache hits before the real file. Every tool that touches this vault - `jarvis-memory`, `jarvis-cli`, Obsidian's Dataview dashboards, and a Claude Code session's own file search - pays a tax proportional to files it was never supposed to see.
## Finding 2 - the pollution has one root cause, and it is a sync-scoping gap, not a scanner bug
`20_Progress/AI/Claude Code/Sync - Unison.md` documents a working, careful system: a manifest-driven Unison sync that mirrors exactly `.claude/agents`, `.claude/commands`, `.claude/hooks`, `.claude/skills`, and root `CLAUDE.md`/`AGENTS.md` from eight real project repos into Jarvis every 15 minutes, explicitly excluding machine-local settings and runtime files. This is why "only `.claude/` and Claude conversations have been perfectly set up," in the user's own words.
Cursor's mirror (`20_Progress/AI/Cursor/.cursor_windows/`, `.cursor_wsl/`) has no equivalent manifest - it is a raw copy of Cursor's entire application-data directory. Checked directly:
- **Genuinely useful, worth keeping:** `skills-cursor/` (13 real skill folders - `create-skill`, `create-subagent`, `loop`, `sdk`, `shell`, `statusline`, and others - the direct analog to `.claude/skills/`) and `plans/` (7 saved task-plan files with real prose from past Cursor sessions).
- **Pure noise, zero knowledge value, ever:** `extensions/` (roughly 30 installed VS Code/Cursor extension binaries, not documentation), `plugins/cache/` (the 1,425 files above, regenerated automatically by Cursor), `ai-tracking/ai-code-tracking.db` (a SQLite runtime file), `projects/` (workspace-state folders keyed by random IDs), `ide_state.json`, `argv.json`.
**The fix is not a new invention - it is applying the exact pattern the Claude Code sync already proved: give Cursor a scoped manifest entry** (`skills-cursor/` and `plans/` only) instead of chasing the noise afterward with exclusion lists in three separate tools. Both should still happen - the manifest fix stops new pollution at the source, and exclusion lists in `registry.py`/`jarvis-cli` are the agreed backstop against any future stray sync doing the same thing again.
## Finding 3 - the "5,354 broken wikilinks" number is mostly a parser bug, not a linking-discipline problem
`jarvis-cli links` reports 5,354 broken wikilinks and 370 ambiguous ones. Reading the actual sample output shows most of these are not real breaks: entries like `10_Areas/AI/Claude Code\|AI` are the tool's link parser choking on the `[[path|alias]]` pipe-alias syntax, not a link pointing nowhere. The ambiguous-link list is mostly duplicate filenames caused by Finding 1's vendor pollution - "AGENTS.md, 18 matches" counts every vendored `AGENTS.md` copy, not 18 real ambiguities in vault content.
The genuinely broken links, filtered by eye from the sample, number closer to eight or ten: an unwritten `Claude Code Prompts` note, a couple of stub references, one PDF-attachment link. The user's own self-assessment ("fairly consistent" linking) was closer to the truth than the raw tool output, which currently cries wolf at roughly 500 times the real rate. This number cannot be trusted for prioritization until the pipe-alias parsing bug in `jarvis-cli` is fixed.
## Finding 4 - conversation capture works; the registry just does not know about it yet
`60_Claude/05_Clippings/AI Conversations/` holds 891 files and is actively growing - `00 - Capture Health.md` (auto-generated by `update-capture-health.ps1`) logs a clean Windows backfill run as recent as 2026-08-21T10:30 and a clean WSL run at 10:15 the same day. Capture is real and current, not broken.
Two things are true at once, and both matter:
- `jarvis_status` reports **zero conversations indexed.** `registry.py`'s conversation-ingestion step was never built past a stub - the 891 files exist on disk but the registry's `conversations` table has never been populated from them. This is a cheap, well-scoped fix: "fill a table, add one function, add one `@mcp.tool()`," per the server's own README.
- The hook script written to make capture automatic (`jarvis-session-continuity.ps1`, which injects a SessionStart context pack and exports transcripts on SessionEnd/Stop) is not wired in either the project's `.claude/settings.json` or the global `~/.claude/settings.json` - the global file has every hook event pointed at Merget's own recorder instead. Capture still works because a separate, independently-built scheduled task (`update-capture-health.ps1`, roughly every 15-30 minutes) polls Claude's own session storage and backfills anything new. Two mechanisms exist for the same job; only one is actually running. Not urgent, but it is the same "one fact, two homes" pattern the North Star already names as the disease.
## Finding 5 - most "disabled" plugins are lazy-loaded, not off (a correction made mid-session)
An earlier pass in this same session claimed roughly 15 plugins were disabled and that this explained the styling gaps. That claim was too strong, and `40_Resources/Obsidian/Plugins/Plugin Inventory and Configuration Map.md` (already written, 2026-05-15) is why: the `lazy-plugins` plugin deliberately defers Kanban, Excalidraw, Git, Hover Editor, Omnisearch, Periodic Notes, QuickAdd, Spaced Repetition, and Copilot by 5-15 seconds after startup so they do not slow boot. Missing from `community-plugins.json` does not mean inactive.
What is actually still open, checked directly against that note:
- **`excalibrain`** - the inventory note says (from May) "no matching plugin folder was found," but the folder exists on disk now, checked this session. The note is stale on this one point and needs a fresh check in the Obsidian UI to confirm it is actually loading.
- **`workspaces-plus`** - installed, no readable manifest, still unverified, exactly as the note already says.
- **The Spaced Repetition config-layer conflict is real and was already flagged by the vault's own docs, not discovered here first.** `Spaced Repetition and Learning Loops.md` carries a warning calling this "the single highest-impact unknown for this plugin": `data.json` holds two conflicting layers - the legacy top-level keys say tag `#cards` and bold-cloze on, the nested `settings` block says tag `#flashcards` and bold-cloze off. Every card written anywhere in this vault assumes the legacy layer is the one in effect. Nobody has checked Settings -> Spaced Repetition to confirm which layer the installed version (1.13.9) actually reads. Five-minute check, still undone.
Three plugin-topic docs were spot-checked for the "most docs are thin, not concrete" claim (`Plugin Gaps Recommendations and Verification.md`, `Plugin Inventory and Configuration Map.md`, `Spaced Repetition and Learning Loops.md`) and all three are strong - sourced with real external links, specific about current settings, honest about their own open questions, each with a named gold-standard example note. That claim does not hold uniformly across the folder; it needs to be pointed at specific plugin docs rather than applied to the whole `40_Resources/Obsidian/Plugins/` folder.
## Finding 6 - new items surfaced directly by the user, not yet documented anywhere
- **A Dataview rendering bug:** `==highlight==` combined with an inline code span (`` ` ``) breaks Dataview rendering. Reported firsthand by the user across multiple past occurrences. Not yet captured as a named gotcha anywhere in `Jarvis Writing and Formatting.md` or the plugin docs.
- **A global writing rule:** never use an em dash: use a plain hyphen instead, or restructure the sentence, in every project. `C:\Users\Anant Gupta\.claude\CLAUDE.md` did not exist before this session; it now exists and carries only this rule, written during the session at the user's explicit request (the one piece of writing done before the end-of-session batch, because it was small, global, and low-risk).
- **Dissatisfaction with Canvas for visual/spatial work:** described as "multiple cards fit together," not the "rigid and full screen" experience wanted. This is a real, separate design question - not a plugin-config fix - and needs its own scoping conversation before any note gets written about it.
## Priority queue
**Fix now (low effort, high clarity payoff):**
1. Verify Spaced Repetition's effective config layer in Settings -> Spaced Repetition (`#cards` vs `#flashcards`, bold-cloze on vs off) - the plugin's own doc already calls this the top unknown.
2. Verify whether `excalibrain` actually loads now that its folder exists; update the stale line in `Plugin Inventory and Configuration Map.md` once confirmed.
3. Name and document the Dataview `==` plus backtick rendering bug somewhere durable (destination to be decided - likely `Jarvis Writing and Formatting.md` or a new entry in the Plugins folder).
**Decide (needs the user, not a default):**
1. What "rigid and full screen" visual/spatial tooling should actually look like, since Canvas does not fit - a dedicated conversation, not a quick fix.
2. Which specific plugin docs in `40_Resources/Obsidian/Plugins/` feel thin or missing - the three spot-checked were strong, so this should not become a blanket rebuild.
**Build (the actual highest-leverage work - identified and queued, not yet executed):**
1. Scope Cursor's sync manifest to `skills-cursor/` and `plans/` only, matching the Claude Code manifest's pattern; drop `extensions/`, `plugins/cache/`, `ai-tracking/`, `projects/`.
2. Add exclusion lists to `registry.py`'s `rglob` walk and to `jarvis-cli`'s scan, as the agreed backstop against future sync pollution.
3. Close the frontmatter `type:` vocabulary - stop undefined values (`code`, `rationale`, `class`, `community`, and others) from vendor docs leaking into a field every retrieval rule treats as closed.
4. Populate `jarvis-memory`'s `links` table from the wikilinks that already exist in vault notes - this alone unlocks graph-traversal retrieval (`jarvis_neighborhood`) with no embedding infrastructure required.
5. Populate `jarvis-memory`'s `conversations` table from the 891 already-captured files - the capture pipeline works, the registry just never learned about it.
6. Fix `jarvis-cli`'s wikilink parser so it stops choking on `[[path|alias]]` syntax - the current broken-link count cannot be trusted for prioritization until this is fixed.
7. Reconcile the two conversation-capture mechanisms - the disconnected live-hook design (`jarvis-session-continuity.ps1`) versus the scheduled backfill that is actually doing the work. Pick one, remove or repair the other.
**Low priority - correctly sequenced last, not dropped:**
1. `jarvis_semantic_search` and the rest of the embedding-based retrieval layer - waits until the boundary and graph fixes above land, per the reordering decided at the top of this note.
## Next thread
This audit closed with two follow-on threads, deliberately kept separate from this note:
- A discussion of AI fundamentals - the concepts and terminology behind what this vault, and the user's broader "vibe coding" practice, already do without always naming - aimed at `40_Resources/CS/AI`, which currently holds only a few rough, unstructured notes.
- This session will **not** write into `40_Resources/CS/AI` directly. It will produce a second distilled note in this same folder describing what needs to be done there, written only after that discussion happens, following the same discuss-first pattern this entire session used.

---
type: input
status: active
created: 2026-08-11
updated: 2026-08-19
tags:
  - claude-kit
  - prompts
  - second-brain-claudekit
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]"
next: "Run # Claudekit first, in a fresh session with cwd = ~/projects/ai/claude/second-brain-claudekit. Run # Jarvis second, once the Claudekit run's final report exists to read."
---
# Claude Kit — Build Prompts
==Only prompts live in this note, each inside a fenced block, ready to paste into a fresh session. Everything else — context, background, open questions — lives in [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]. Rewritten 2026-08-19; this note's prior content (dated 2026-08-11) is preserved there, not lost.==

## Sequencing

**Run `# Claudekit` first.** It lays out the repo's own structural base — nothing in `# Jarvis` should be attempted until that base is real, because `# Jarvis`'s job is to document what the base actually became, not what it was planned to become. Read the Claudekit session's final report (or its `git log`/diff) before starting `# Jarvis`.

# Claudekit

Paste into a fresh Claude Code session, cwd = `~/projects/ai/claude/second-brain-claudekit`. Recommended: run at `high` or `xhigh` effort — this task is multi-step, spans the whole repo, and has zero tolerance for fabricated results.

```
You are laying out the structural base of this repo for the first time since its initial scaffold. This repo's job is a qualification pipeline for external Claude Code tooling: sandbox/<repo>/ (real clone, run for real) → tested-tools/<type>/<use-case>/<repo>/ (cleared the bar, second look) → promoted (this repo's .claude/, a specific project, or Jarvis's real .claude/) — or tested-tools/_future/<repo>/ (cleared the bar, no current project needs it yet). _docs/Architecture.md, _docs/Promotion-Criteria.md, _docs/Design.md, _docs/Repo-Map.md, and _docs/Gaps.md already exist and are current as of 2026-08-19 — read all five before doing anything else. They are the source of truth for every claim in this prompt; if anything here conflicts with what you read there, trust what you read.

Ground rule for the whole session: never fabricate. Not a source-repo name, not a passing test, not a populated folder to look complete. Every one of this repo's own docs treats "I read about it" and "I ran it" as different kinds of evidence — hold yourself to the same bar while documenting your own work. Where a real decision is ambiguous and only Anant can make it, use AskUserQuestion — don't guess and don't stall either; batch related questions together rather than asking one at a time.

Standard git safety applies throughout: check `git status` before anything that could discard work, never force-push or force-reset, stage specific files rather than `git add -A`. Do not commit at the end without being asked — stop after Phase 7 and report what changed, staged or not.

## Phase 1 — Resolve agents/, commands/, hooks/ (repo root)

These three folders currently hold leftover content from the repo's two original scaffold commits (d35f0b7 and 726f6de, both 2026-04-03) that was never run through this repo's own qualification pipeline. Two different provenance stories apply — verify both for real with `git log -p --follow -- <file>` or `git show <commit> -- <file>` before acting, don't take this prompt's word for it:

1. **commands/compress.md, commands/preserve.md, commands/resume.md** — added in commit 726f6de, whose own message calls them "CPR commands." This is the Compress-Preserve-Resume pattern. A real external repo named cpr-compress-preserve-resume is tracked in Jarvis's own Tier-1/Priority-1 install lists (decided Jarvis-only, not global, per _docs/Design.md) — but it was never actually cloned into sandbox/ or tested. Confirm this is still accurate, then: clone the real repo into sandbox/cpr-compress-preserve-resume/, run it for real per _docs/Promotion-Criteria.md's four questions, and compare its actual behavior against what's hand-authored here. Land the outcome in tested-tools/commands/cpr-compress-preserve-resume/ with a written, dated verdict — adopt the real repo's version, keep the hand-authored one with a documented reason it's equivalent or better, or some explicit blend. This is the first artifact in this repo to carry a real evidenced promotion reason for this specific pattern; treat it as the template for how every future promotion decision should be documented.

2. **Every other file** — agents/connector.md, agents/researcher.md, agents/reviewer.md, agents/writer.md, commands/brainstorm.md, commands/capture.md, commands/connect.md, commands/inbox-process.md, commands/journal.md, commands/research.md, commands/review.md, commands/summarize.md, hooks/auto-link.md, hooks/daily-summary.md, hooks/post-note-create.md — added in commit d35f0b7, the very first scaffold commit, with no reference to any specific external repo in that commit's message or the files' own content. Confirm each one has no real external-repo origin (check content against every repo currently in sandbox/ and tested-tools/, not just the commit message). Do not invent a source repo for any of them. Once confirmed zero-provenance, ask Anant (one batched AskUserQuestion) how to handle this whole set: relocate to a clearly-labeled tested-tools/<type>/native-scaffold/ bucket that honestly states "authored directly in this repo's initial scaffold, never tested against an external source"; archive/delete as dead scaffold weight now that the repo's real purpose is established; or keep as-is with a documented reason. Apply whatever is chosen to the full set — every file, not a sample.

3. After both are resolved, repurpose the now-cleared agents/, commands/, hooks/ folders (plus a new docs/ folder) as per-destination-project staging: agents/<ProjectName>/, commands/<ProjectName>/, hooks/<ProjectName>/, docs/<ProjectName>/ — per the plan already recorded in Jarvis's Claudekit Session Context note. Create subfolders only as real content lands; leave the folders otherwise empty, not pre-scaffolded with placeholders. skills/ keeps its current role (source-repo staging) untouched.

## Phase 2 — Lay out 60_Claude/ completely

- Add 60_Claude/vault-rules/pipeline-conventions.md covering everything _docs/Gaps.md's section 4 names as missing: sandbox/<repo-name>/ naming, the tested-tools/<type>/<use-case>/<repo>/ three-level convention plus tested-tools/_future/<repo>/FOR-WHAT.md, the per-destination-project staging convention from Phase 1.3, and the instructions/ and tests/ conventions from Phases 3-4 below.
- Add 60_Claude/Templates/for-what.md — the template every tested-tools/_future/<repo>/FOR-WHAT.md should follow.
- Fix 60_Claude/README.md's scripts/ row and _docs/Sync.md's framing: name sync-all.sh + sync-manifest.json + sync-all-silent.vbs + register-sync-task.ps1 as the live multi-project engine; sync-jarvis.sh + sync-jarvis-silent.vbs + register-jarvis-sync-task.ps1 as legacy, kept only for rollback.
- Confirm 60_Claude/scripts/check_dependency.py has a preset for every dependency claim already tested for real (bun for gbrain, the Chromium shared libs for gstack) — add any missing ones.

## Phase 3 — Establish tests/

Structure: tests/<type>/<repo-name>/, mirroring tested-tools/. Each entry holds either a runnable script reproducing the real install/init/test commands, or a dated markdown log of the real commands and their real output — the mechanical answer to Promotion-Criteria.md's question 1 ("did it actually run without a manual workaround"). Backfill for what's already sitting in tested-tools/ today: tested-tools/skills/mattpocock-engineering/ has 17 skills, none individually tested yet — write down exactly that state as the real test backlog. Do not write a test file that claims something passed if it hasn't actually been run.

## Phase 4 — Establish instructions/

Convention: instructions/<repo-name>/<file> holds instruction-shaped files (CLAUDE.md, AGENTS.md, PRD.md, or equivalent) copied from a sandbox/ candidate specifically because the pattern in it is worth reviewing or reusing — never this repo's own root CLAUDE.md. Run a real discovery pass across every repo in sandbox/ (e.g. find sandbox/ -maxdepth 2 -iname 'CLAUDE.md' -o -iname 'AGENTS.md' -o -iname 'PRD.md') and copy real hits in, one subfolder per source repo. If nothing is found, leave the folder empty and say so — don't manufacture an example.

## Phase 5 — tested-tools/_future/

Do not force-populate this folder. As of this repo's own research on 2026-08-19, nothing currently sitting in tested-tools/ or sandbox/ has genuinely cleared the qualification bar with no current project need (gbrain is pending an embedding-provider decision, mattpocock-skills is ungrouped, ECC is undecided) — re-verify this is still true, and if so, leave the folder empty. An empty _future/ folder with the convention documented (Phase 2) is the correct, non-gap state — do not invent a candidate just to have something here.

## Phase 6 — Write _docs/How to/

Only start this phase once Phases 1-5 are real and committed to the working tree (even if not git-committed). This is second-brain-claudekit's own version of Jarvis's Toolkit "How to Use X" pattern — how this repo's own pipeline actually works, for a future session (or Anant) to read cold. Base the content on _docs/Jarvis.md and _docs/Gaps.md, both already updated 2026-08-19 with verified research on Jarvis's review system and conversation-capture pipeline — do not re-research Jarvis from scratch, cite those two docs. Write:
- _docs/How to/README.md — an index
- _docs/How to/review-system.md — how Jarvis's review system actually works today (trigger, sources, the 100%-clarity gate), and what if anything this repo's own pipeline activity should feed into it
- _docs/How to/conversation-capture.md — re-verify the current capture status before writing (it was mid-fix as of 2026-08-19 in a separate, parallel effort — do not assume it is still broken or already fixed; check the actual current state)
- _docs/How to/using-staged-artifacts.md — how agents/commands/hooks/skills/instructions staging and promotion actually works now, post-Phase-1
- _docs/How to/tests-and-promotion.md — how tests/ gates a promotion decision, referencing Promotion-Criteria.md and the Qualification-Checklist

## Phase 7 — Close the loop

Update _docs/Repo-Map.md and _docs/Gaps.md: check off every item this session actually resolved, dated 2026-08-19 (or today's real date if different), and leave anything not actually resolved explicitly open with a reason — do not mark something done that was deferred to an AskUserQuestion answer you didn't get. Run git status, review the full diff for anything that looks like a secret or an accidental deletion, then stop and report: what changed, what's still open, and the exact AskUserQuestion answers you got in Phase 1. Do not commit unless explicitly asked to.

Apply every instruction above to every file it names — not a sample, not just the first one you check. If you find yourself about to skip a file "because the others were probably the same," verify that file specifically first.
```

# Jarvis

Paste into a fresh Claude Code session, cwd = the Jarvis vault root (Windows). Run this only after reading the Claudekit session's final report from Phase 7 above.

```
You are updating Jarvis's own AI-tooling notes to reflect (a) what's actually true about the review system and conversation-capture design already built here 2026-08-10/11, and (b) whatever second-brain-claudekit's own base-layout session (run separately, in that repo, per its own "# Claudekit" prompt) actually did. Read that session's Phase 7 report before starting — do not assume what it did, confirm it, either from the report or from 20_Progress/AI/Claude Code/second-brain-claudekit/ (view-only mirror, synced automatically — do not edit it directly, it exists only to let you check the repo's real current state from here).

Explicitly out of scope: conversation capture itself (the WSL/Windows Stop/SessionEnd hooks, wsl-session-export.ps1, export-claude-session.ps1, the scheduled backfill safety net) is being rebuilt in a separate, already-in-progress effort. Do not edit those hooks or their scheduled tasks. You may read their current state for reference.

Ground rule: every claim you write must be checked against a real file, not remembered or assumed — the notes you are fixing are stale specifically because past versions of them stopped doing this. Where you're not sure, say so in the note rather than guessing.

1. Rewrite 10_Areas/AI/Setup/Review System.md for real — it is currently completely empty. Source of truth, all real and already built 2026-08-10/11: 30_Order/Standards/Review Standard.md, 30_Order/Templates/Capability/AI Tools Weekly Review Template.md, 30_Order/Templates/Capability/AI Tools Monthly Review Template.md, 60_Claude/30_Reviews/AI/Tools/Tool log.md. Write the concrete answer to "how does the review system actually work": what triggers a review (nothing automatic — manual/human-triggered, by design, per Review Standard.md's own "Used By Workflow" section), what sources it must cite, what the Decided Fixes 100%-clarity gate means in practice, and what's still genuinely missing (the review-writing cadence itself has no cron; 60_Claude/30_Reviews/AI/Conversations/ is still unwired; Tool log.md has zero data rows because /export-ai-session has never been run against a real session).

2. Update 10_Areas/AI/Setup/Gaps.md: remove or check off whatever the new Review System.md now covers, keep the review-writing-cadence gap and the Conversations/ folder gap, and add the tested-skills/tested-tools terminology drift below plus whatever second-brain-claudekit's Phase 7 report says is still open on that side.

3. Reconcile terminology in 20_Progress/Projects/AI Use/Claude Kit/Tool Map.md: it currently calls the second pipeline stage tested-skills; the real repo folder (confirmed 2026-08-09) is tested-tools. Fix every occurrence in this note's pipeline-stage vocabulary to match the repo. Also add a parked (future) stage matching the repo's tested-tools/_future/ folder, only if the Claudekit session's report confirms that folder was actually scoped/built — check, don't assume.

4. If the Claudekit session's Phase 1 report says cpr-compress-preserve-resume was cloned into sandbox/ and tested for real, add or update its Tool Map.md row with the real verdict. If it wasn't reached, don't add a row that implies it was.

5. Fix the stale tool tables in 10_Areas/AI/Claude Code.md that Toolkit/What Agents.md, Toolkit/What Commands.md, and Toolkit/What MCPs.md already flagged as wrong (a command table dated 2026-07-03, missing several commands built since, still listing a removed organize-csci2033 command; an MCP list missing excalidraw). Those three notes already did the diff work — read them and apply it, don't re-derive it.

6. Resolve Toolkit/Cursor.md — currently a 0-byte stub sitting alongside populated peer notes. Either write real content following the same "What X" pattern as its siblings, or replace it with one explicit line stating it's intentionally deferred and why, so it stops reading as an accidental gap.

Definition of done: Review System.md is a complete, accurate, no-longer-vague source-of-truth note; Gaps.md reflects true current state, not stale-as-of-2026-08-09 state; Tool Map.md's terminology matches the real repo; the three flagged stale tables in Claude Code.md are fixed; Cursor.md is resolved one way or the other. Add one dated entry to 20_Progress/Projects/AI Use/Claude Kit/Log.md summarizing exactly what changed, using the existing ## [YYYY-MM-DD] tag | title convention — don't invent a new logging format.
```

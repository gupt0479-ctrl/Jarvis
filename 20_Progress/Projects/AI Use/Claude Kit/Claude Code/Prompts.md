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
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session
    Context]]"
next: Run the corrected Claudekit prompt first (fresh session, cwd =
  second-brain-claudekit). Then run Jarvis Step 1, then Step 2, each in a fresh
  Windows session, cwd = Jarvis vault root. Step 3 is not written yet.
---
# Claude Kit — Build Prompts
==Only prompts live in this note, each inside a fenced block, ready to paste into a fresh session. Everything else — context, background, open questions — lives in [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]. Rewritten 2026-08-19; this note's prior content (dated 2026-08-11) is preserved there, not lost.==

## Sequencing

**Run `# Claudekit` first.** It lays out the repo's own structural base — nothing in `# Jarvis` should be attempted until that base is real, because `# Jarvis`'s job is to document what the base actually became, not what it was planned to become. Read the Claudekit session's final report (or its `git log`/diff) before starting `# Jarvis`.

# Claudekit

**Superseded 2026-08-19.** The original 7-phase prompt got agents/commands/hooks resolution, tests/, and tested-tools/_future/ right (verified directly against the repo — see Phase 0 below). It got instructions/ built on a wrong premise entirely, left 60_Claude/vault-rules/ as generic PARA convention instead of a real operational write-contract, and never built the Standards/ + artifact-authoring-template layer 60_Claude/ actually needs. Replaced below with a corrected prompt scoped specifically to those three things, grounded in Jarvis's own real 30_Order/ and Write Contract patterns (read directly this session, not assumed).

Paste into a fresh Claude Code session, cwd = `~/projects/ai/claude/second-brain-claudekit`. Recommended: `high` or `xhigh` effort.

```
You are correcting and completing second-brain-claudekit's base-layout work. A prior session got several things right — verify this, don't just trust it: agents/, commands/, hooks/ provenance was resolved for real (the CPR pattern actually tested, verdict "blend" in tested-tools/commands/cpr-compress-preserve-resume/VERDICT.md; the other 15 zero-provenance files relocated to tested-tools/{agents,commands,hooks}/native-scaffold/); tests/ was backfilled for both; tested-tools/_future/ was correctly left empty. It got three things wrong or too thin, which is this session's actual job to fix:

1. instructions/ was built on a wrong premise and needs to be cleared and rebuilt correctly.
2. 60_Claude/vault-rules/ has no real operational write-safety rules for this repo — only generic PARA note-writing convention.
3. 60_Claude/ has no Standards/ folder and no templates for authoring a new agent, skill, command, or hook.

Read _docs/Repo-Map.md and _docs/Gaps.md first for full context on what's already real in this repo. Ground rule for the whole session: verify every claim against a real file before writing anything that depends on it — this repo's own docs have already drifted stale from trusted-but-unverified claims more than once (see _docs/Repo-Map.md's incident log); don't repeat that pattern here.

## Phase 0 — confirm what's already correct, don't redo it

Confirm each of these still exists as described: tested-tools/commands/cpr-compress-preserve-resume/ (with VERDICT.md), tested-tools/{agents,commands,hooks}/native-scaffold/ (15 files total), tests/commands/cpr-compress-preserve-resume/, tests/skills/mattpocock-engineering/, and tested-tools/_future/ (empty, correctly — nothing has cleared the bar with no project home yet). If any of these are missing or meaningfully different from this description, stop and report before touching anything else — that's a signal something changed that needs investigating, not a green light to silently rebuild it differently.

## Phase 1 — instructions/, corrected

Everything currently in instructions/ is wrong and must be cleared out: it holds one subfolder per sandbox/ candidate (adx, ecc, gbrain, and so on) with CLAUDE.md/AGENTS.md files copied from repos being evaluated for ingestion. That was a misreading of the original intent. Remove all of it. Before deleting, check whether any of it has standalone reference value; if so, note where it might belong instead (most likely nowhere new is needed — it was extracted from repos already sitting in sandbox/ with their own files intact) rather than defaulting to keeping a copy somewhere just in case.

instructions/ is for the real projects Anant actively works on — never for sandbox/ candidates. It holds exactly the instruction-shaped markdown files (CLAUDE.md, AGENTS.md, PRD.md, and similar) that already exist for each real project, one subfolder per project: instructions/CausalOps/CLAUDE.md, instructions/CausalOps/AGENTS.md, and so on — the same per-destination-project convention already established for agents/, commands/, hooks/, docs/.

The authoritative list of real projects and exactly which instruction files each one has is 60_Claude/scripts/sync-manifest.json — read it fresh; do not use any project list given to you secondhand, including any list in this prompt. For every entry with "kind": "project", filter its paths array down to the markdown instruction files specifically (CLAUDE.md, AGENTS.md, PRD.md, README.md-as-instructions, and similar — not .claude/agents, .claude/commands, .claude/hooks, .claude/skills, or other non-instruction subpaths), and copy the real, current content of each from that entry's source path (most are directly readable from this WSL session — check each one; fall back to the entry's mirror path in Jarvis only if source isn't reachable) into instructions/<ProjectName>/<file>.

This is meant to become a live-synced folder, the same way agents/, commands/, hooks/, docs/ already are for their own content — but sync-manifest.json and sync-all.sh currently only sync each project's source and its Jarvis mirror, never into this repo's own instructions/. Do not wire this up silently. Design the concrete extension (most likely a new field on each manifest entry naming which of its paths also mirror into instructions/<name>/, plus the corresponding sync-all.sh logic), write the design down in _docs/Sync.md, then use AskUserQuestion to confirm the design with Anant before modifying sync-manifest.json or sync-all.sh for real — that script runs unattended on a 15-minute schedule against real project repos, and a wrong edit there has a bigger blast radius than anything else in this session.

## Phase 2 — a real write contract for this repo

60_Claude/vault-rules/ (folder-structure.md, naming-conventions.md, linking-strategy.md, tagging-system.md, pipeline-conventions.md) describes generic PARA note-writing convention. What's actually missing is Jarvis's kind of document: a write contract — golden rules, a "where does this go" routing table, and an explicit "never write to" list — scoped to this repo's own filesystem instead of vault notes.

Read Jarvis's real one in full first: the Jarvis vault root's AGENTS.md, "Write Contract" section (Golden rules, "Where does this note go?", "Never write to"). Do not invent a shape for this repo's version — adapt that real one's structure directly: golden rules for this repo (for example: never create a new top-level folder without checking it against _docs/Repo-Map.md first; when unsure where something goes, say so and ask rather than guessing a location), a routing table built from what's actually true about this repo's folders today (an agent for a specific project → agents/<Project>/; a candidate skill from a sandbox/ repo → skills/<repo>/; an instruction file for a real project → instructions/<Project>/; a promoted, cleared-the-bar artifact → tested-tools/<type>/<use-case>/<repo>/; and so on — work out the complete table, don't guess a partial one), and a "never write to" list (sandbox/<repo>/'s own files once cloned — read-only, tested-tools/ content that isn't yours to overwrite without going back through the pipeline, and anything else that's genuinely off-limits). Write this as 60_Claude/vault-rules/write-contract.md.

## Phase 3 — Standards/ and artifact-authoring templates

60_Claude/ has no Standards/ folder today, and no template for authoring a new agent, skill, command, or hook from scratch — only vault-note templates and one pipeline template (for-what.md) exist.

Read Jarvis's real 30_Order/Standards/ folder in full — it holds one Standard.md per content type (Action, Brief, Concept, Evergreen, MOC, Project, Review, Source Summary, and others), each defining what "correct" looks like for that type. Read at least Evergreen Standard.md and Review Standard.md in full to understand the real shape a Standard takes here: a concrete, checkable definition with a "Used By Workflow" section and clear Done Conditions — not a vague style guide.

Build 60_Claude/Standards/ in this repo with the same shape, one Standard.md per artifact type this repo actually produces: Agent Standard.md, Skill Standard.md, Command Standard.md, Hook Standard.md, Instructions Standard.md, and a Tested-Tool Promotion Standard.md (this last one should mostly point back to _docs/Promotion-Criteria.md and 60_Claude/Qualification-Checklist.md rather than duplicate them — cross-reference, don't repeat). Pair each with a real authoring template in 60_Claude/Templates/ (agent-template.md, skill-template.md, command-template.md, hook-template.md) — an actual skeleton someone would start from, not a placeholder. While in 60_Claude/Templates/, confirm the existing vault-note templates (area-note, daily-note, idea-note, and so on) are genuinely still right for notes this repo actually writes inside Obsidian; if any are clearly unused or wrong for this repo's real purpose, say so rather than silently leaving them.

## Phase 4 — do not build the review folder

60_Claude/ is also missing a review folder — this repo's own equivalent of Jarvis's 60_Claude/30_Reviews/AI/, for reviewing this repo's own pipeline activity. Do not build it in this session. It depends on the Jarvis-side review-system work (the three-step Jarvis prompt in this same note) finishing first. Note its absence in _docs/Gaps.md as explicitly deferred, with the real reason, and stop there.

## Phase 5 — close the loop, honestly

Update _docs/Repo-Map.md and _docs/Gaps.md: document that instructions/ was rebuilt on a corrected premise (briefly state what was wrong the first time, so it doesn't happen again), add write-contract.md, Standards/, and the new artifact-authoring templates to the folder inventory, and record the instructions/ live-sync design as designed-but-not-wired, with the real reason (confirmed with Anant first, per Phase 1). Update CLAUDE.md's and README.md's folder-structure diagrams to match. Run git status, check the full diff for anything that looks like a secret or an accidental deletion, then stop and report — do not commit unless asked.

Apply every instruction above to everything it names, not a sample — every project in sync-manifest.json, every artifact type in Standards/. If you're about to skip something because it's probably the same as the last one, check that one specifically first.
```

# Jarvis

Paste into a fresh Claude Code session, cwd = the Jarvis vault root (Windows), Sonnet 5, `high` or `xhigh` effort. This is a three-step arc — write only the first two steps for now; the third (fully mapping the review system) gets written after reviewing what these two actually produce.

### Step 1 — Sync Jarvis with the real, verified repo

```
Second-brain-claudekit (the WSL repo at ~/projects/ai/claude/second-brain-claudekit, mirrored read-only here at 20_Progress/AI/Claude Code/second-brain-claudekit/) just ran a base-layout session. Your job is to bring every Jarvis note that describes or tracks that repo's structure up to date with its real, current, verified state — not with any session's self-report, including the summary below, which you must independently confirm before writing anything.

Ground rule, non-negotiable: verify before you write. Multiple Claude Code sessions edited that repo concurrently during the base-layout work, and the session's own self-report already flagged one prompt-injection-shaped anomaly in a background summarization pass it had to discard. Treat every claim below as a lead to check against the real mirror at 20_Progress/AI/Claude Code/second-brain-claudekit/, not as a fact to transcribe. Where the mirror and a claim disagree, the mirror wins. Where you can't find something the claim describes, say so in the note you write rather than writing the claim anyway.

Leads to verify, from the base-layout session's self-report (2026-08-19):
- agents/, commands/, hooks/ (repo root) were repurposed from flat staging into per-destination-project staging (agents/<Project>/, commands/<Project>/, hooks/<Project>/, plus a new docs/<Project>/) — created only when real content lands, so likely still empty. skills/ kept its original role, untouched.
- The three CPR commands (compress.md, preserve.md, resume.md) went through a real pipeline pass: the real external repo (EliaAlberti/cpr-compress-preserve-resume) was cloned into sandbox/, installed, and run for real. Verdict: "blend" — landed in tested-tools/commands/cpr-compress-preserve-resume/, with a VERDICT.md explaining the decision. The old hand-authored trio was archived to .claude/_archive/superseded-commands/, not deleted.
- The other 15 zero-provenance files (4 agents, 8 commands, 3 hooks, all traced to the repo's very first scaffold commit, confirmed to have no real external-repo origin) were relocated to tested-tools/{agents,commands,hooks}/native-scaffold/.
- instructions/ is now populated: a real discovery pass allegedly found 27 instruction-shaped files (CLAUDE.md/AGENTS.md) across 19 of the repo's sandbox/ candidates, copied in one subfolder per source repo, with a README.md index.
- tests/ is now populated: a real test transcript for cpr-compress-preserve-resume, and an honest 0-of-17-tested backlog note for tested-tools/skills/mattpocock-engineering/.
- tested-tools/_future/ was re-confirmed empty (nothing has cleared the bar with no project home yet) — this is claimed as correct, not a gap.
- 60_Claude/vault-rules/pipeline-conventions.md (new) and 60_Claude/Templates/for-what.md (new) were added. 60_Claude/README.md and _docs/Sync.md were corrected to name sync-all.sh as the live multi-project engine and sync-jarvis.sh as legacy/rollback-only.
- _docs/How to/ now has 5 files (README.md, review-system.md, conversation-capture.md, using-staged-artifacts.md, tests-and-promotion.md).
- _docs/Repo-Map.md, CLAUDE.md, and README.md (repo root) were all updated to reflect the above. _docs/Gaps.md was reportedly touched by a different concurrent session, not this one — read its actual current content fresh, do not assume it matches anything you were told.
- Conversation-capture (out of scope to edit, but read-only relevant): the report claims a pwsh/.NET crash was root-caused and fixed, hooks were made defensive, and a scheduled backfill safety net was built and verified — check the real 00 - Capture Health.md dashboard (or wherever that data actually lives) for consecutive OK/exit-0 runs on both Windows and WSL before treating this as true.
- Still open, per the report: the working tree is uncommitted (10+ days of prior work, not committed by design); tested-tools/commands/cpr-compress-preserve-resume/ sits without the tested-tools/<type>/<use-case>/<repo>/ three-level convention, flagged in its own VERDICT.md, not resolved; the tested-skills/tested-tools terminology drift between this vault and the repo is still unresolved; a gap between 60_Claude/Templates/weekly-summary.md and the real review-template shape is named, not built.

Once you've independently confirmed what's actually true (and noted anything that checked out false, or anything you couldn't verify), update:
1. 20_Progress/Projects/AI Use/Claude Kit/Tool Map.md — fix tested-skills → tested-tools everywhere in its pipeline-stage vocabulary; add or update the cpr-compress-preserve-resume row with its real, verified verdict; add one batch entry (not 15 individual rows) for the native-scaffold relocation; add a parked (future) stage definition matching tested-tools/_future/, noting it's currently and correctly empty.
2. 20_Progress/Projects/AI Use/Claude Kit/Log.md — one new dated entry (## [YYYY-MM-DD] tag | title, matching the existing convention exactly) summarizing what you verified actually happened.
3. Toolkit/Agents/What Agents.md, Toolkit/Commands/What Commands.md, Toolkit/Hooks/What Hooks.md — all three currently describe the old flat-staging role for these folders ("staging area for drafts, not promoted content" / commands/ as "the global command set, not yet copied anywhere"). That framing is now wrong on both counts. Rewrite the relevant sections to match verified reality. Check Toolkit/Skills/What Skills.md too — it may still be accurate since skills/ was reportedly untouched, but confirm, don't assume.
4. 10_Areas/AI/Setup/Folder Map.md — add the verified new structure: instructions/<repo>/, tests/<type>/<repo>/, tested-tools/_future/<repo>/, tested-tools/<type>/native-scaffold/, and the per-destination-project staging convention for agents/, commands/, hooks/, docs/.
5. 10_Areas/AI/Setup/Notes Map.md — read it in full (you likely haven't touched this one before); update anything it says about the repo's structure that's now stale.
6. 10_Areas/AI/Claude Code.md — this note's tool tables were already flagged as stale by Toolkit/What Agents.md, What Commands.md, and What MCPs.md in earlier research (dated 2026-07-03, missing several commands, listing a removed organize-csci2033 command, missing the excalidraw MCP). Apply that already-identified diff — don't re-derive it.
7. If you verified the conversation-capture fix is real and confirmed live: update whatever entry in 10_Areas/AI/Setup/Gaps.md currently describes that gap as open, closing it with the real evidence you checked. If you could not verify it, leave that gap open and say why.

Explicitly out of scope for this step: do not write or touch 10_Areas/AI/Setup/Review System.md, do not design or describe the review system's mechanics beyond what's already true today, and do not edit any conversation-capture hook, script, or scheduled task — that's a separate, already-in-progress effort. Apply every instruction above to everything it names — every stale table, every affected note — not a representative sample.

Definition of done: every note listed above reflects what you personally verified against the real repo, not what you were told; anything you couldn't verify is flagged as unverified rather than silently written as fact; the Log.md entry exists. Report back exactly what you changed and exactly what you couldn't confirm.
```

### Step 2 — Evergreen source-of-truth notes, and the review system's base

Run only after Step 1's updated notes exist — this step cites them rather than re-deriving their content.

```
Second-brain-claudekit now has nine terse, dated, amendment-style docs in its own _docs/ folder (PRD, Architecture, Design, Promotion-Criteria, Sync, Jarvis, Current-Setup, Repo-Map, Gaps) — accurate, but written as an audit trail, not as something a person reads once to understand the whole system. Your job is to write the notes that are actually better than that: real Jarvis evergreen notes, in this vault's own voice and quality bar, that explain what this pipeline is and how it works well enough that any later claim about it can be checked against these notes instead of re-read from the repo's own docs each time.

Read 20_Progress/Projects/AI Use/Claude Kit/Tool Map.md, Toolkit/Claude Code.md, and this session's own Step 1 output before writing anything — those are your source material, along with the repo's _docs/ files (read via the mirror). Do not duplicate their content; synthesize and explain it. Every non-obvious claim needs a citation to a real file or a real dated decision — this is what makes the note verifiable, which is the entire point of writing it.

Part A — the pipeline, explained properly
Write one evergreen note (split into more only if it stops being one coherent idea — this vault's own atomic-note rule applies here same as anywhere else) at 20_Progress/Projects/AI Use/Claude Kit/Source of Truth/The Qualification Pipeline.md (create the Source of Truth/ folder). It should give a reader with zero context: why this repo exists (the two failure modes it prevents, with the real historical evidence for each), what each stage of the pipeline actually does today (sandbox/ → tested-tools/ → tested-tools/_future/ or promoted, with tests/ as the gate and instructions/ as the pattern-reuse layer — all as they concretely exist post-Step-1, not as originally planned), and how a reader would trace any specific tool's real history through Tool Map.md and Log.md. Use type: evergreen frontmatter matching this vault's existing convention (see any file in the Toolkit/ folder for the shape: status, tags, notes: [[...]] links, next).

Part B — the review system's foundation, not its full mechanics
Write 10_Areas/AI/Setup/Review System.md for real — it is currently empty. Scope this narrowly: what the review system is, why it exists, and its real foundational shape as already built (30_Order/Standards/Review Standard.md, the two AI Tools Weekly/Monthly Review Template.md files, 60_Claude/30_Reviews/AI/Tools/Tool log.md — read all three directly, don't rely on any prior summary of them). Explain the 100%-clarity Decided-Fixes gate and why the trigger is deliberately manual, not automated. Do not design or map the complete operational workflow end-to-end here — that is the explicit job of a later step, not this one. If the note threatens to grow past what Setup/ notes normally hold, split a companion evergreen note under Source of Truth/ and link it in rather than overloading Review System.md.

Definition of done: Part A's note lets someone verify any claim about the pipeline against a cited real source without asking you again. Part B's note is accurate and complete for what's already built, explicitly stops short of the full operational mapping, and is no longer empty or vague. Report what you wrote and what you deliberately left for the next step.
```

### Step 3 — not written yet

Full operational mapping of the review system, end to end. Write this prompt only after reviewing what Steps 1 and 2 actually produce — not before.

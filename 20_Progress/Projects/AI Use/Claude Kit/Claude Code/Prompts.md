---
type: input
status: active
created: 2026-08-11
updated: 2026-08-20
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
next: Round 3, 2026-08-20. Run the Claudekit continuation prompt first, in the
  same already-running codebase session — it must land its commits before
  Jarvis's prompt reads the mirror. Then run the single Jarvis prompt in a fresh
  Windows session. Both replace all prior prompts in this note; do not re-run
  anything above them.
---
# Claude Kit — Build Prompts
==Only prompts live in this note, each inside a fenced block, ready to paste into a fresh session. Everything else — context, background, open questions — lives in [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Claudekit Session Context]]. Rewritten 2026-08-19; this note's prior content (dated 2026-08-11) is preserved there, not lost.==
## Sequencing
**Run `# Claudekit` first.** It lays out the repo's own structural base — nothing in `# Jarvis` should be attempted until that base is real, because `# Jarvis`'s job is to document what the base actually became, not what it was planned to become. Read the Claudekit session's final report (or its `git log`/diff) before starting `# Jarvis`.

# Claudekit

**Round 3, 2026-08-20 — continuation.** An adversarial pass read every `_docs/` file, `write-contract.md`, `Standards/README.md`, `CLAUDE.md`, `sync-manifest.json`, and `.claude/settings.json` directly and found 7 real findings plus a recurring incident pattern. Paste the prompt below into the *same, already-running* session that did the corrected instructions/write-contract/Standards build — this is a continuation, not a fresh session.

```
An adversarial review of this repo's own docs and config just surfaced 7 real findings. Fix them in this order — this is a continuation of the same work you were just doing, not a new task from scratch.

1. .claude/settings.json's claudeMdExcludes is ["sandbox/**", "tested-tools/**"] and does not cover instructions/, which now holds real, complete CLAUDE.md/AGENTS.md files from 8 real projects (including Jarvis's own behavioral rules). Any session that reads a file under instructions/<Project>/ auto-loads that project's instructions into this repo's session, per Architecture.md's already-documented auto-load behavior. Add "instructions/**" to claudeMdExcludes. Then audit every other top-level folder that could plausibly carry a CLAUDE.md-shaped file (docs/<Project>/ is the likely candidate; agents/<Project>/, commands/<Project>/, hooks/<Project>/ are unlikely but check) and exclude anything that qualifies. Update Architecture.md's "Known gap" section, which already documents this exclusion mechanism for sandbox/ and tested-tools/, to record this fix.

2. _docs/Repo-Map.md — the file explicitly positioned as ground truth — contradicts itself: its own opening pipeline diagram still reads tested-skills/<name>/ instead of tested-tools/, and its own opening paragraph still lists the project roster as five projects (Jarvis, BOOM, Portfolio, TradingView, CausalOps) while its own folder table and sync-manifest.json list eight live projects, with BOOM not tracked in the pipeline at all. Three same-day audit passes fixed detail tables without ever re-reading the file's own top-of-file summary. Fix both lines for real. Then, as a standing rule for this file specifically: any future edit to Repo-Map.md must be followed by reading the entire file top to bottom for self-consistency, not just the section that was touched — add this rule to the file's own opening paragraph so it's not lost again.

3. sync-manifest.json's second-brain-claudekit entry syncs its own root CLAUDE.md into instructions/second-brain-claudekit/CLAUDE.md — a second copy of a file already in this same repo, the same "one fact, one home" violation instructions/ v1 got torn out for, just smaller. Remove second-brain-claudekit from instructions_paths' scope (its CLAUDE.md is already at repo root; nothing needs to mirror it into a subfolder of itself). If you find a real reason it should stay, write that reason down in _docs/Sync.md instead of leaving it unexamined either way.

4. Real throughput is badly lopsided against documentation investment: zero of 30 sandbox/ clones have reached a promoted state in three weeks; gbrain has been one embedding-provider decision away from promotion since 2026-07-29; 17 of 30 sandbox clones have had zero activity since their initial clone. Do not fix this by writing more about it. Add one clearly-flagged, prominent entry to _docs/Gaps.md naming gbrain's stuck decision and the 17 dormant clones as the top-priority open items — both require Anant's real decision, which happens in Jarvis (Tool Map.md), not here. Cross-reference it from the Jarvis prompt in this same note so it isn't missed.

5. Standards/, write-contract.md, and the artifact-authoring templates built last round were a direct, explicit request from Anant, not agent-invented scope — but judged against PRD.md's own problem statement (which is scoped to external tools, not this repo's internal authoring process) and Design.md's minimal-footprint principle, they currently have no written justification for the gap they close. Add one to Design.md: they exist because the CPR blend verdict already needed a real authoring convention, not a speculative one — a named gap, not a nice-to-have. Then add a standing rule to PRD.md or Design.md (your call which fits better): no further net-new pipeline meta-infrastructure gets built until at least one real tool reaches a promoted state (installed into this repo's own .claude/, a real project's .claude/, or Jarvis's real .claude/). This is the gate that was missing.

6. The recurring incident pattern across this repo's own incident log (the 50_Claude recreation bug, the Jarvis sync silently dying for a week, the multi-project sync's CTRL_C_EXIT, conversation capture breaking twice, docs/ vanishing between sessions) is always the same shape: a mechanism reports success, and the only thing that ever catches the failure is someone manually re-verifying against real state later, often much later. This has happened enough times (5+, documented) to earn one real fix, not another incident write-up: add a short, concrete section to write-contract.md — any new automated mechanism (hook, scheduled task, sync leg) must have a real failure-visible check as part of clearing it, not just an exit code; and anything already running unattended gets a periodic real re-verification, not an assumed-healthy status. Name this explicitly as the fix for a demonstrated pattern, not a speculative addition — it clears the same minimal-footprint bar item 5 just set.

7. Commit the work. This repo has had zero commits since 726f6de (2026-04-03) — almost five months, three-plus weeks of dense structural work this session and prior ones, sitting only in the working tree. This is not a neutral fact: docs/ silently vanishing between sessions (found and rebuilt during this round) is a real, already-demonstrated failure that an uncommitted tree makes possible and a committed one would have caught immediately via git status or a diff. Review the full current diff carefully first — check for anything that looks like a secret (the write-contract.md live-sync design touches sync-manifest.json and sync-all.sh; make sure no credentials or tokens got pulled in anywhere during the instructions/ rebuild). Then stage and commit in logically separated commits with clear messages — not one giant blob — grouping by the real unit of work (e.g. the folder renames from weeks ago, the agents/commands/hooks resolution, the instructions/ rebuild, the Standards/write-contract addition, tonight's fixes). Do not force anything, do not skip hooks.

Update _docs/Gaps.md at the end: check off what this pass resolved, and make sure items 4's gbrain/dormant-clones flag and item 5's new gate are both clearly visible, not buried. Report what you changed, especially the exact commits you made.
```

# Jarvis

**Round 3, 2026-08-20 — replaces the old Step 1/2/3 structure.** Those were written before the adversarial pass on the codebase; running them as-is now would sync against and design on top of already-known-stale information. One consolidated prompt below, scoped to what the adversarial findings actually require on the Jarvis side — not everything Step 1/2 originally planned. Run after the Claudekit continuation prompt above has actually landed its commits.

Paste into a fresh Claude Code session, cwd = the Jarvis vault root (Windows), Sonnet 5, `high` or `xhigh` effort.

```
An adversarial review of second-brain-claudekit just ran, found 7 real findings and a recurring "reports success, only caught by later manual re-verification" incident pattern, and a Claudekit-side continuation prompt is fixing what belongs in the repo (claudeMdExcludes, Repo-Map.md's self-contradiction, the sync-manifest self-mirror, and — critically — committing the work for the first time since April). Read that continuation prompt's real result (via the synced mirror at 20_Progress/AI/Claude Code/second-brain-claudekit/, or the repo directly if reachable) before starting — confirm what it actually did, don't assume it matches this description.

Ground rule: verify before writing, same as every prior round. Two things you're about to sync from don't have a track record of being trustworthy on their own — the repo's own docs have self-contradicted after three same-day audit passes, and this repo's own automated mechanisms have a demonstrated pattern of reporting success while silently failing. Check real state, not reported state, everywhere below.

1. Sync Jarvis's tracking notes with the real, now-corrected repo state: 20_Progress/Projects/AI Use/Claude Kit/Tool Map.md (tested-skills → tested-tools terminology, still unresolved as of the last check), Log.md (one dated entry for this round), Toolkit/Agents/What Agents.md, Toolkit/Commands/What Commands.md, Toolkit/Hooks/What Hooks.md (all three still describe the old flat-staging role, now wrong twice over — first by the per-destination-project repurposing, second by whatever the continuation prompt just changed), 10_Areas/AI/Setup/Folder Map.md, 10_Areas/AI/Setup/Notes Map.md, and 10_Areas/AI/Claude Code.md's already-flagged stale tool tables. Same job as the original Step 1, just against the real current state instead of the pre-adversarial-review state.

2. Force the gbrain decision. It has been one embedding-provider choice away from promotion since 2026-07-29 — three weeks. Use AskUserQuestion to get Anant's real answer now (Voyage, ZeroEntropy, OpenAI, or explicitly "not now, and here's why" as a fourth option). Update Tool Map.md's gbrain row with whatever real answer you get — do not leave it re-flagged as still-pending without at least having asked.

3. Triage the 17 sandbox/ clones with zero activity since their initial 2026-07-30 clone (agent-skills, spec-kit, claude-context, graphify, promptfoo, and the rest — list them from Tool Map.md or a fresh sandbox/ listing, don't guess the 17). For each, a real one-line decision in Tool Map.md: still worth evaluating (name what would need to happen next), or drop (name why, briefly — redundant with something already promoted, no longer relevant, or genuinely deprioritized). The goal is an honest, current Tool Map.md, not zero dormant entries — some may legitimately stay "still worth evaluating." What's not acceptable is leaving them silently unexamined the way they've been for three weeks.

4. Exercise the review system for real, once, instead of designing it further. Run /export-ai-session against at least one real recent Claude Code session (Windows or WSL, your choice — pick one with genuine tool/skill use) so that 60_Claude/30_Reviews/AI/Tools/Tool log.md gets its first real data rows, not the empty schema it's had since 2026-08-11. Then write one real Weekly review using AI Tools Weekly Review Template.md, against real Tool log rows and real Sync-Log data for whatever period you pick — this becomes Review Standard.md's first Gold Standard Example, which its own frontmatter says doesn't exist yet. If the process breaks or feels wrong at real volume, write that down in the review itself rather than smoothing over it — that's exactly the kind of finding this exercise is meant to surface.

5. Spot-check the live sync and capture dashboards directly — do not trust any prior session's report of their status, including the one that produced the findings above. Read the real current sync log (_All-Projects-Sync-Log.md or equivalent) and the real current conversation-capture health dashboard. Record what you actually see, with real dates and real OK/failure counts, in whatever note (Gaps.md or a new dated check) makes sense. If either mechanism is reporting healthy but you can't independently confirm real recent activity, say so explicitly — that's the exact failure mode this whole round exists to stop happening again.

Do not, in this pass: write the "pipeline explained properly" evergreen note from the original Step 2 Part A, and do not attempt a full operational mapping of the review system end-to-end. Both are still queued, but only after this round's real, verified fixes land — writing a polished explainer note on top of not-yet-verified state is exactly the pattern that produced finding 2 (a ground-truth doc that turned out self-contradictory) in the first place.

Report back what you verified true, what you found actually false, the real answers to items 2 and 3, and the real Weekly review you wrote for item 4.
```

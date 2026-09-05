---
type: project
status: active
created: 2026-07-26
updated: 2026-09-04
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]"
  - "[[20_Progress/Internship/Building System/Runs/Prompt 1 Reboot — Building System Refresh Session (2026-09-04)]]"
tags:
  - internship
  - automation
  - prompts
next: "Numbering reset 2026-09-04 — Prompts 1-27 archived in full, this file now holds Prompt 1 of the new era (see the note it points to). Tasks A/B/E are runnable; C/D are blocked on open questions from the 2026-09-04 chat session. run.yml stays disabled_manually until the human decides separately, after reviewing the write-gate-failure fix trace in Research Loop - Improvement Plan's # Plan section — do not re-enable it from inside a prompt."
---
# Claude Code Prompts — Internship Research Loop
This file holds the next prompt(s) to run, and only that — it gets wiped and rewritten every build cycle, not accumulated. When a prompt finishes and its result is reviewed, its full text and result move into [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] and get deleted from here.

## Prompting Guide In Use
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) — re-apply on every prompt.
- Front-load everything, literal scope, explicit Task Order/Files Touched, `high` effort, generous `max_tokens`.
- Hand over verified facts, instruct re-checking them.
- **A hypothesis this file itself wrote can turn out wrong — say so plainly when it does, don't quietly drop it.** Prompt 14 v2's own JGCL hypothesis (a `SOURCES`-tuple tie-break bug) was checked and found wrong; the real cause was three specific already-deleted scholarship postings. That's now the record, not the guess that preceded it — every doc touched below corrects to the real finding, not a hedge between the two.
- **An alarming-sounding fact ("46 deletions") is worth one direct check before treating it as a problem.** It resolved in one search — a real, already-tracked session (auto-captured, per this vault's own conversation-export layer), not an untracked gap. Cheap to verify, expensive to leave as a nagging unresolved worry across future prompts.
- **When a real source count changes, every doc that states a specific number becomes a small, precise lie until corrected.** Lever going live makes "eight sources" wrong wherever it's written — treat this the same as any other now-stale claim, not a footnote.

---

- **A local git checkout goes stale fast on this project — the pipeline auto-commits hourly.** Read state files via `git show origin/master:<path>`, or `git fetch` + confirm local `HEAD` matches `origin/master` (pull/rebase if not) before trusting any local working-tree read of anything `run_pipeline.py`/`recheck.py` touches. Caught live 2026-08-27: a local `git show`-free read of `state/debate_losses.json` showed 6 entries where `origin/master`'s real, current file had 271 — a local clone can sit dozens of commits behind within a single day.

- **A session sharing a file with a parallel session must only ever append or fix its own entries — never remove something it didn't write because it looks unfamiliar or out of scope.** Real incident, 2026-08-28: Prompt 21's session found 6 legitimate links Prompt 20's session had added to a shared `No Deadline.md` (companies with no existing dossier, correctly out of Prompt 21's own 320-dossier scope) and deleted them as presumed noise during its own cleanup pass. Caught and restored by the coordinating session, not by either prompt session itself. If something in a shared file looks wrong, say so in the report — don't unilaterally remove it.
- **When a follow-up genuinely needs the same deep context a session just built (e.g., re-checking its own just-completed work), tell the human to continue in the SAME session, not paste into a fresh one.** Re-deriving 320 already-read dossiers from scratch in a new session would re-burn the exact token cost being complained about — this project's usual "fresh session per prompt" default is a good default, not an absolute rule, when continuity itself is the point.

# Vault
## Numbering Reset, 2026-09-04
Prompts 1-27 (the discovery-build and deadline/promotion-sweep era) are done and archived in full in [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] — nothing deleted, nothing lost. This file restarts numbering at Prompt 1 for the next era: discovery is currently paused (`run.yml` disabled_manually, human's deliberate choice, 2026-08-30) with its write-starvation fix shipped and unexercised; promotion has real traction (14 total promotions, 0 Applying notes); the goal now is throughput (5 dossiers/hour once discovery resumes), a cleaner test suite, reconciled documentation, and a public v0. Full context, ground truth, and the open questions this reset depends on: [[20_Progress/Internship/Building System/Runs/Prompt 1 Reboot — Building System Refresh Session (2026-09-04)]].

### Prompt 1 — Building System Refresh (Tasks A/B/E runnable now; C/D pending)
See [[20_Progress/Internship/Building System/Runs/Prompt 1 Reboot — Building System Refresh Session (2026-09-04)]] for the full prompt — ground truth, non-negotiable rules, and Task A through E. **Do not run Tasks C or D until their `[PLACEHOLDER]`s in that note are resolved.** Task A is a status check only — re-enabling `run.yml` is explicitly reserved for the human and is not part of this or any prompt until said so directly.


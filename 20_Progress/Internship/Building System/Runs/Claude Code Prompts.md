---
type: project
status: active
created: 2026-07-26
updated: 2026-08-27
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts —
    Archive]]"
tags:
  - internship
  - automation
  - prompts
next: "Prompts 16/17 archived 2026-08-27 (both confirmed executed via direct
  evidence — no execution report was ever pasted for either). Prompt 18
  (Codebase) and Prompt 19 (Codebase) both ready, meant to run in parallel in
  two separate terminals against the same repo — both carry an explicit
  git-fetch/rebase-don't-force warning since they'll both commit to
  origin/master around the same time. Prompt 18: fix the write-gate
  failure-memory bug (a candidate that wins its bucket's write-budget slot but
  fails vault_writer/validate.py is never remembered, so it's re-offered
  forever) — stopgap-if-warranted + the write_gate_failures.json root-cause fix.
  Prompt 19: extend schema-drift coverage to the 6 currently-unwatched sources
  and add a per-source zero-match alert (Ashby has been hard-frozen at 0 matches
  for 112 straight runs). Still deliberately NOT written: a Jarvis-side prompt
  for the postmortem's review-system-tightening and Source of Truth.md/System -
  Build Log.md full staleness-pass recommendations — real, still-open, but out
  of scope for this round's two Codebase-only parallel prompts."
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

# Codebase
### Prompt 18: Write-Gate Failure Memory — Stopgap + Root-Cause Fix
**Fresh session**, `gupta-builds/internship-research-loop`. Read `CLAUDE.md` first. Runs in parallel with Prompt 19 in a separate terminal — **both sessions will commit to the same repo/branch at the same time.** Before your first commit, `git fetch && git status` and make sure you're rebasing onto whatever the other session has already pushed, not force-pushing over it. If you hit a push conflict, rebase, don't force.

```
**Context — verified fresh, 2026-08-27 ~11:10 UTC, against `origin/master` (`7a1be68`) directly via `git show`, not a local checkout (a local clone on this exact project was found 25 commits stale within one day during this same check — always confirm local `HEAD` matches `origin/master`, or read state via `git show origin/master:<path>`, before trusting a number). Time will have passed since — recompute every number below yourself before acting on it, don't assume these are still current:**

- `state/debate_losses.json`: 271 entries. 154 sit at exactly 24/48 losses (`MAX_DEBATE_LOSSES` = 48). 173 of the 271 entries are `ApplyGuy:*` uids (149 of those at 24). Nothing is above 27 yet — the leading edge has real runway left, this is not an hours-away emergency, but it is a real, still-live, still-worsening bug.
- `state/excluded_uids.json`: 388 entries (a flat list, not a dict), unchanged — confirmed zero `ApplyGuy:*` uids have crossed into permanent exclusion yet.
- The specific dead-link example from the 2026-08-26 postmortem (`SimplifyJobs:de926b0a-99e7-4dbd-94cd-334ec565be9f`, HTTP 403) is **absent from all three state files** (`debate_losses.json`, `excluded_uids.json`, `seen_ids.json`) — confirmed directly. It appears in the `rejections` list of 183 of the last 681 `logs/runs.jsonl` records, spanning 2026-08-10 through 2026-08-27 (17+ days), always failing `url_liveness`. Being present in `rejections` but absent from all three state files is itself strong evidence it wins its bucket's `this_run` selection (`_prioritize_and_cap`) and then fails `vault_writer/validate.py` every time — never entering `deferred` (which is what feeds `debate_losses.json`) and never getting written (which is what feeds `seen_ids.json`).
- Timeline: the postmortem observed the leading ApplyGuy cohort age 20→24 losses in ~12 hours (2026-08-26 14:35 → 2026-08-27 02:25), roughly 1 loss/3 hours. Projected forward from the 24-loss checkpoint, that's ~72 hours to reach 48 — slower than the postmortem's original "24-30 hours" estimate. Separately, `run.yml`'s hourly schedule has a live gap: last successful run `2026-08-27T02:24:36Z`, none since (checked ~9 hours later), while `gh workflow list` still shows it `active` (not disabled) — likely a GitHub Actions scheduling delay, not a bug in this repo; don't try to fix GitHub's scheduler, just know the aging clock may be paused or bursty whenever you check, and recompute the real timeline from fresh numbers rather than trusting either estimate.
- Write-budget config: `MAX_NEW_WRITES_PER_RUN = {"AI/ML": 3, "Fullstack": 3, "CyS & Finance": 3, "Other": 1}` (`run_pipeline.py`). `_prioritize_and_cap` returns `(this_run, deferred)`; `update_debate_losses(losses, deferred, written_uids)` only increments losses for `deferred` and only clears via confirmed `written_uids` — a `this_run` winner that fails `validate_and_write` is in neither set.

### Task 1 — Recompute and decide on urgency
Re-run the checks above against current `origin/master` state. State plainly: is an immediate stopgap (another `MAX_DEBATE_LOSSES` raise, or a different one) still warranted given the real numbers and the current run-schedule gap, or has enough slack opened up that the root-cause fix alone is sufficient without another bump? Don't default to "raise it again" just because that's what happened last time — justify the call either way with the numbers you actually see.

### Task 2 — Stopgap (if Task 1 says it's warranted)
Raise `MAX_DEBATE_LOSSES` (or another stopgap of your choosing) with the same real-numbers-and-reasoning citation style as the existing 5→48 comment in `run_pipeline.py`. If Task 1 concludes no stopgap is needed, say so explicitly and skip this — don't bump the number reflexively.

### Task 3 — Confirm the win-mechanism before touching `debate_compare`
The postmortem flagged this as unconfirmed and cautioned against changing `debate_compare`'s sort logic without confirming it first. The evidence above (the dead-link uid appearing in 183 `rejections` entries while being completely absent from `debate_losses`/`excluded_uids`/`seen_ids`) is strong circumstantial confirmation of the "wins `this_run`, fails `validate_and_write`" hypothesis, but not direct instrumentation. Decide: is this circumstantial evidence sufficient to proceed straight to Task 4's fix, or do you want to add one line of logging (`this_run` selections, not just final rejections) for direct confirmation first? Either is defensible — make the call and say why. **Do not change `debate_compare`'s sort/tiebreak logic itself** unless this step reveals the win-mechanism hypothesis is actually wrong — if that happens, say so plainly (this project's own norm: a wrong hypothesis gets corrected in the record, not quietly dropped) and stop to reconsider scope rather than guessing at a different fix.

### Task 4 — Build the root-cause fix
A `write_gate_failures.json` (uid → `{check, count, first_seen}`), written by `validate_and_write`'s rejection path, checked before a uid re-enters `this_run` selection in a future run — same "notify, don't silently drop" discipline `excluded_uids.json` already uses, for a distinct failure class (structurally doomed vs. merely out-ranked). Real design decisions to make and justify, not assume:
- Does a uid crossing some threshold here get logged/short-circuited only, or does it also eventually feed into `excluded_uids.json` the way `MAX_DEBATE_LOSSES` does? Pick one and justify it — a permanently-dead URL probably deserves a different (likely lower, likely faster) threshold than "out-ranked 48 times," since dead-is-dead in a way out-ranked isn't.
- Should this apply per-`check` (a `url_liveness` failure vs. a `cross_source_duplicate` failure might warrant different handling) or uniformly? Justify whichever you pick.

### Task 5 — Tests + verification
Fixture-based tests for the new behavior — the real `SimplifyJobs:de926b0a-99e7-4dbd-94cd-334ec565be9f` 403 case is a genuine, citable scenario to build a fixture from. Full suite green. Separate commits per logical change (stopgap vs. root-cause fix), matching this repo's existing discipline. Concretely confirm (test or dry-run, not just "should work") that the cited dead-link uid is skipped/short-circuited on a simulated next run after the fix.

### Explicitly out of scope
No schema-drift coverage work (Prompt 19's job, running in parallel — don't touch `core/schema_drift.py`). No vault/Jarvis writes. No rewriting `debate_compare`'s core sort/tiebreak algorithm unless Task 3 shows the win-mechanism hypothesis is wrong.

### Report back
Task 1's fresh numbers + urgency verdict. Task 2's stopgap decision (or explicit no-stopgap-needed call) and why. Task 3's confirmation approach and result. Task 4's `write_gate_failures.json` design decisions and why. Test results, and concrete confirmation the cited dead link is now handled.
```

### Prompt 19: Schema-Drift Coverage + Per-Source Zero-Match Alerting
**Fresh session**, `gupta-builds/internship-research-loop`. Read `CLAUDE.md` first. Runs in parallel with Prompt 18 in a separate terminal — **both sessions will commit to the same repo/branch at the same time.** Before your first commit, `git fetch && git status`; rebase onto whatever the other session has already pushed, don't force-push.

```
**Context — verified fresh, 2026-08-27 ~11:10 UTC, against `origin/master` (`7a1be68`) directly via `git show`, not a local checkout — same staleness caveat as Prompt 18, recompute before acting:**

- `core/schema_drift.py`'s `check_all()` only pre-flights 5 of 11 sources: SimplifyJobs, Jose-Gael-Cruz-Lopez, vanshb03, zshah101, ApplyGuy. Greenhouse, Ashby, Lever, Freehire, AIJobs, InternDock (6 sources) have zero schema pre-flight — a silent field rename on any of them degrades to zero matches with no halt, no issue, nothing but a human noticing `filter_match_counts` stuck at 0 in the raw log.
- Concrete, not hypothetical: direct read of `logs/runs.jsonl` (681 records, `git show origin/master:logs/runs.jsonl`) shows Ashby's `fetch_counts` frozen at exactly 4 and `filter_match_counts` at exactly 0 for the **last 112 consecutive runs**, starting 2026-08-21T21:14:17 UTC. Before that streak began, 458 of 570 sampled runs had nonzero Ashby matches historically. `ASHBY_COMPANIES` in `ingestion/sources.py` currently lists 9 tokens: `ellipsislabs, quadrillion-labs, circleback, ctgt, pylon-labs, cohere, cursor, modal, elevenlabs`.
- A prior session (Prompt 14 v2, archived) already live-checked Ashby once (2026-08-24) and concluded "genuinely only ~4 have open roles right now" — but that check predates the current 112-run hard-zero streak fully setting in (it found a nonzero, if small, real match count, not a frozen zero). **Don't assume that prior finding still holds** — re-verify directly (curl/http_get all 9 tokens yourself) whether this is still "genuinely nothing to match" or has drifted into a real schema/API break since.
- Prompt 18 is fixing the write-gate failure-memory bug in a parallel session right now — stay out of `run_pipeline.py`'s debate/write-gate logic (`_prioritize_and_cap`, `update_debate_losses`, `write_gate_failures.json`) and `state/debate_losses.json`/`state/excluded_uids.json` semantics entirely; this prompt's `run_pipeline.py` touches should be limited to surfacing a new per-source alert in the run-record logging path.

### Task 1 — Investigate Ashby's zero-match streak directly
Curl/`http_get` each of the 9 tokens against the real Ashby API, compare the real current response shape/count against what `fetch_ashby`/`normalize_ashby` expect. State the real finding plainly, cited: genuine "no eligible postings right now" (structurally capped, matching the 2026-08-24 finding) or actual drift (renamed field, changed response shape, empty/error response, rate-limiting). If a token itself looks stale (company renamed/moved off Ashby), say so.

### Task 2 — Extend schema-drift coverage
Add check functions (mirroring `check_simplify_schema` et al.'s existing pattern) for the 6 currently-unwatched sources — Greenhouse, Ashby, Lever, Freehire, AIJobs, InternDock — each verifying the real, current API/feed response has the fields `normalize_*` expects, wired into `check_all()`. If a genuine structural reason makes one of these six impractical to pre-flight the same way (e.g., InternDock's Firecrawl-based, multi-URL fetch has no single stable schema to check against), say so explicitly rather than forcing a check that wouldn't mean anything.

### Task 3 — Per-source zero-match-rate alert
Add an alert to the run record (`run_pipeline.py`'s run-logging path) for a source sitting at `filter_match_count == 0` for N consecutive runs while `fetch_count > 0` and the source has historically had nonzero matches. Pick and justify a real N — 112 runs is how long it actually took a human to notice the Ashby streak this pass; pick something meaningfully shorter and cite why that number, not just "smaller."

### Task 4 — Tests
Fixture-based, mirroring the existing `schema_drift` test pattern, plus a test for the new zero-match alert logic. Full suite green.

### Task 5 — Report on Ashby's company list
Only if Task 1's investigation surfaces something concrete: is the 9-company `ASHBY_COMPANIES` list itself due for a refresh (a token gone stale/renamed), or is "genuinely ~4 open roles across 9 small companies" still the real, current answer?

### Explicitly out of scope
No write-gate/`debate_compare` changes (Prompt 18's job, running in parallel — don't touch `state/debate_losses.json`/`state/excluded_uids.json` semantics). No vault/Jarvis edits — the review-system tightening (Weekly Review template, Reviews MOC nudge) and the `Source of Truth.md`/`System - Build Log.md` full staleness pass from the 2026-08-26 postmortem are real, still-open items, but belong in a separate Jarvis-side prompt (deliberately not this one — a Codebase session has no path to the vault the way a Jarvis session does, per this project's established split).

### Report back
Task 1's Ashby finding (genuine cap vs. drift, cited). Which of the 6 sources got real schema-drift coverage, and how (or why one couldn't be meaningfully covered). The zero-match alert threshold chosen and why. Test results.
```

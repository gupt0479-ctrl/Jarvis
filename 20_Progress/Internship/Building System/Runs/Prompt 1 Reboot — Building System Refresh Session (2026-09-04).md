---
type: project
status: active
created: 2026-09-04
related_progress:
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[20_Progress/Internship/Building System/System - Build Log]]"
  - "[[20_Progress/Internship/Building System/Runs/Discovery Step Postmortem — Write-Starvation Incident (2026-08-26)]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts]]"
tags:
  - internship
  - automation
  - prompts
  - reboot
next: "All open questions answered 2026-09-04. Every task (A-E) is now fully specified and runnable, no [PLACEHOLDER]s remain. Task D (the overdue Weekly+Monthly review) is being run directly in the same session that resolved these questions, since the context is already loaded — see the new review notes it produces for the actual findings."
---
# Prompt 1 Reboot — Building System Refresh Session
==This is a **prompt to run**, not a finished record — every `[PLACEHOLDER: ...]` below needs a real answer before this session starts. It exists because the user asked, in the same session this was written, for "an excellent prompt for an in-depth session," with explicit instructions: state the goal plainly, don't let the model hallucinate, use the right words. This note is that prompt.==

## Why "Prompt 1," Not "Prompt 28"
[[20_Progress/Internship/Building System/Runs/Claude Code Prompts]] is on Prompt 27 and its own `next` field says Prompts 26/27 already ran (10 `Programs/Serious/` + 4 `Considering/` + 10 Contacts + 10 Tracker notes now exist, confirmed live 2026-09-04 — up from 5 total promotions as of the last Monthly Review). The user's explicit instruction this session was to "start fresh from Prompt 1" for the next era of this project: the discovery-side postmortem is done, the write-gate fix has shipped, and the actual goal now is throughput (5 dossiers/hour) plus getting a public v0 out, not more one-off bugfix prompts. **This does not mean deleting Prompt history** — `Claude Code Prompts — Archive.md` keeps every prior prompt's full record. It means the numbering for this new phase starts over, and this file (not a continuation of 26/27) is Prompt 1 of that phase.

## The Actual Goal, Stated Plainly
Not "write more notes." The measurable target, restated from the user's own words this session: **get real internships moving through the entire pipeline (find → dossier → screen → program/contact/tracker → reach out → apply) fast, at a sustained ~5 dossiers/hour discovery rate**, with a public, generic v0 of the discovery half live on the internet with a real README, and a repeatable, checkable way to confirm the pipeline is actually catching every real posting from its sources (not just producing dossiers that look plausible).
**What this is not:** a mass-apply script, an LLM-written outreach blast, or a vanity metric on dossier count. [[20_Progress/Internship/Building System/Source of Truth]]'s own stated success metric stands: applications submitted per week, not dossiers written.

## Ground Truth As Of 2026-09-04 — Verified, Not Assumed
Re-verify every number below before acting on it; these are correct as of this session, not guaranteed to still be true when this prompt actually runs.
- `run.yml` (hourly discovery): `disabled_manually`, last successful run 2026-08-29T09:33:51Z. `recheck.yml`/`revalidate.yml`/`test.yml`: active. **Corrected 2026-09-04**: this was a deliberate human choice to focus on the promotion batch (confirmed via `Claude Code Prompts — Archive.md`'s Prompt 25 addendum: "the human paused the hourly pipeline... `gh workflow disable run` confirmed"), not an emergency stopgap — an earlier pass through this material guessed wrong on that point and it's corrected here, not quietly dropped.
- The write-starvation fix shipped in two pieces, dates corrected against the real commits (not the "both 2026-08-30" a source report claimed): `e856e05` (`write_gate_failures.json`) landed 2026-08-28, **one day before** the pause, with a day of healthy production data behind it (debate-loss pace slowed from ~3 hr/loss to ~7-10 hr/loss). `2fa8b76` (per-source schema-drift checks + zero-match-rate alerting) landed 2026-08-31, **after** the pause, as a codebase-only session. Both traced line-by-line and reviewed in [[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]'s `# Plan` section — read that trace before deciding on re-enabling.
- Vault state: 287 dossiers (134/42/50/61 across AI-ML/Fullstack/CyS&Finance/Other, 58 in `Viewed/`), 10 `Programs/Serious/` + 4 `Considering/`, 10 Contacts, 10 Tracker notes, **0 Applying notes**.
  - **Corrected 2026-09-04, later same day**: this bullet's own "Why 'Prompt 1,' Not 'Prompt 28'" section above turned out to be wrong that Prompts 26/27 "already ran" — Prompt 27 (Batch B, 7 dossiers) had real, completed contact research but zero notes actually written (session redirected before Step 4 — see [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]'s Prompt 27 entry for the full trace). All 7 were promoted this same day, reusing the existing research. Current vault state: 17 `Programs/Serious/` + 4 `Considering/`, 17 Contacts, 17 Tracker notes, still **0 Applying notes**.
- `state/debate_losses.json`: ~154-233 entries clustered near the 20-loss mark (out of `MAX_DEBATE_LOSSES` = 48), almost all ApplyGuy-sourced, from before the fix shipped — their fate needs confirming, not assuming, once `run.yml` resumes.
- `[[20_Progress/Internship/Building System/V0/Dossier Corrections]]` (2026-08-28) found ~10 duplicate pairs, a quant-firm bucket-misclassification pattern, a Montenson/Mortenson typo (5 dossiers), and 6 unfixed Zipline shared-content dossiers — all still live as of this writing, not yet re-verified this session.

## Answered, 2026-09-04 (do not re-ask these)
- **Re-enabling `run.yml` is NOT part of this prompt.** The human will decide separately, after reviewing the fix trace in [[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]. Task A below is cut to a status-check only.
- **`10_Areas/Career/` review scope: `Internships/` only.** Certifications, Finance, Hackathon, Mentors stay out of scope.
- **Public v0: README + outline only.** No `profile.yaml` genericization, no `verify.py`, this round.
- **Prompt numbering reset, confirmed and executed**: Prompts 26/27 archived into `Claude Code Prompts — Archive.md` with a verified (not first-hand-reported) outcome; this note is now the live Prompt 1.

## Non-Negotiable Rules For Whoever Runs This
1. **Every claim in the output must cite a file+line, a commit hash, a `gh` command's real output, or a direct count you ran yourself.** "Should be fixed" / "looks healthy" / "probably fine" are not acceptable — say what you checked and what it returned.
2. **Re-verify every "Ground Truth" number above before using it.** This project's own Build Log has repeatedly caught prior sessions trusting a stale number from a note instead of the live repo/vault — don't repeat that pattern here.
3. **Do not touch `/promote-dossier`'s human consent gate.** Promotion volume is a throughput problem to plan around, not a gate to bypass.
4. **Do not run `gh workflow enable run` under any circumstances in this prompt.** That decision is explicitly reserved for the human, separately.
5. **Do not raise `MAX_NEW_WRITES_PER_RUN` or add new sources this round** — orthogonal to everything below and premature before discovery is confirmed healthy again.
6. **If a number in this prompt turns out wrong, say so plainly and correct it in the output** — don't quietly work around a contradiction. This note itself has already been corrected once (see the `run.yml` bullet above) — that's the standard to hold the next pass to as well.

## Task Order

### Task A — Status check only (no action)
Re-verify `run.yml`'s current state live (`gh api`/`gh run list`) and report it. That's the entire task — no enabling, no further action, regardless of what the status shows.

### Task B — Test suite consolidation
Parametrize `tests/test_schema_drift.py`'s repeated per-source pattern (see [[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]'s `# Plan`, Section 2) into `@pytest.mark.parametrize` blocks, keeping every real fixture. Do **not** touch `test_filter.py` or `test_relevance.py` — those are real-incident regression tests, not redundant. Report before/after line count and confirm `pytest` still shows the same or greater pass count.

### Task C — Vault reorganization of `20_Progress/Internship/Building System/` (fully specified, resolved 2026-09-04)
1. Reconcile `Source of Truth.md` and `System - Build Log.md` against actually-shipped code via **dated correction entries, not in-place edits** — same pattern already used on 2026-09-04 (see the `run.yml`-emergency-stopgap correction above): keep the original stale claim visible, add what's actually true and why, never silently rewrite history.
2. Re-run a `Dossier Corrections`-style sweep against current live state (not the 2026-08-28 snapshot) before deciding what to fix vs. what's already stale.

### Task D — Run the overdue Weekly Discovery Review + Monthly Promotion Review (DONE 2026-09-04)
Run in the same session that resolved the open questions. Results: [[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W36]] and [[60_Claude/30_Reviews/Internship Loop/Scheduled/Monthly/Internship Loop Monthly Review — 2026-09]]. Headline findings: a confirmed `stage1_reject` false-positive regression on 6 Microsoft dossiers (sidebar-link content bleed, needs a codebase Prompt), and — the most urgent — two real application deadlines (Castleton Commodities International, KeyBank) already reached or passed with zero Applying-note activity. **The Review Standard itself was not revised**, per the earlier decision to run a review first — the reviews above are the input for that revision, not yet acted on.

### Task E — Public v0 README (outline only, confirmed)
Draft the full README from [[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]'s `# Plan`, Section 5. Outline only — do not implement `profile.yaml` genericization or `verify.py` this round.

## Report-Back Format
Per task: what was checked, what it returned, what changed, what's still open. No task marked "done" without the specific command/file/count that proves it.

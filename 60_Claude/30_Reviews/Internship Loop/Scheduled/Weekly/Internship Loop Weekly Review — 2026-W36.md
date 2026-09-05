---
type: evergreen
status: sprout
created: 2026-09-04
updated: 2026-09-04
tags:
  - evergreen
  - review
  - internship
notes:
  - "[[30_Order/Standards/Internship Loop Review Standard]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"
  - "[[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34]]"
next: "A likely stage1_reject false-positive regression (6 Microsoft dossiers, sidebar-link content bleed) needs a codebase fix — file as a Prompt, don't hand-fix the dossiers. run.yml is still disabled_manually; this review's Resource-Limit Health section is a snapshot of a paused system, not a live trend."
---
# Internship Loop Weekly Review — 2026-W36
==Second review of this kind, 12 days after the first (2026-W34, 2026-08-23) — not a clean 7-day period; the Reviews MOC expected the next one "around 2026-08-30" and nothing ran until now. Run with full repo access this time (`gh`, `logs/runs.jsonl` read directly) — the exact gap [[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34|2026-W34]] itself flagged as unresolved ("not reachable this session").==
## Period Covered
2026-08-24 through 2026-09-04 (12 days, not 7 — the gap between reviews, stated honestly rather than padded to look like a normal week).
## Sources Reviewed
- [x] `logs/runs.jsonl` (repo, read via `git show origin/master:logs/runs.jsonl`) — full run history for the period
- [x] `gh issue list` / `gh issue view` (repo) — every open/closed issue, bodies read where relevant
- [x] `gh api .../actions/workflows` and `gh run list` — live workflow state
- [x] Corpus-wide `grep` for `notes:`, `company/`, `matched_reason: matched`, `removed_date` across all 287 live dossiers + 58 `Viewed/` — countable facts, not sampled, per the Standard's own instruction to grep what a script can answer exactly
- [x] The 15 dossiers named in GitHub issue #9 (`revalidate.py`'s own flagged set) — used as this period's targeted sample instead of a fresh random pick, since it's a stronger, already-computed lead than random sampling would be this round (see Sample & Method)
- [ ] `Excluded — Failed The Write Gate.md` — does not exist yet (the fix that creates it has never fired in production; `run.yml` has been off since before it could)
## Sample & Method
**Deliberately not the 2026-W34 method (3 per bucket at positions 1/15/30).** `revalidate.py` (a periodic re-check of every live dossier against current code, shipped since the last review) already produced a targeted, evidence-based list — GitHub issue #9, "15 live dossier(s) now fail current rules" — filed 2026-08-31 and still open. Reviewing that real, already-computed set is a better use of this review's limited read budget than a fresh random sample would be. Corpus-wide counts (notes:/tag/matched_reason/removed_date) are exact greps, not samples — every dossier counted, not a subset.
## Gate & Priority-Classification Conformance
**One real, newly-confirmed regression, not a removal call — this is a codebase bug, not 15 bad dossiers.** Read the actual flagged content for `Software Engineer Intern, AIML & LLM - Microsoft.md` (one of 6 Microsoft dossiers issue #9 flags on `stage1_reject`): line 60 of the stored posting content reads `[Supply Chain Program Management Intern\` — a **"related jobs" sidebar link**, not the posting's own description, containing the literal phrase `core/relevance.py`'s `_STAGE1_REJECT_RE` matches on ("program management intern"). All 6 flagged Microsoft dossiers are genuine, high-quality SWE/AI intern roles (AIML & LLM, CoreAI, Cloud & Distributed Backend, Fullstack Product, Data Platform/Analytics, Security & Identity) written the same week (2026-08-21) — six false positives from the same extraction gap is a pattern, not six independent bad matches. **This is the same bug class as the already-documented Google careers-listing-shell issue** (`ingestion/posting_page.py`'s `_LISTING_SHELL_RESET_RE`) — a different platform (Microsoft's own careers site), same root cause (sidebar/related-content noise reaching `extract_content()`'s output). Not yet fixed; needs a Prompt, not a hand-edit to 6 dossiers that are actually fine.
Of the remaining 9 flagged dossiers, the `location_eligible` flag on `Software Engineer Internship (2027 Start) - Optiver.md` (Other/) and the `stage2_confirm` flags on the 3 remaining Zipline dossiers and 2 Optiver FPGA roles are consistent with already-known, already-documented gaps ([[20_Progress/Internship/Building System/V0/Dossier Corrections]]'s Zipline finding; the NL/HK/PL/IL denylist additions landing after these were written) — real removal candidates, not false positives. `American Fidelity`'s "Agentic AI Intern" and Amex's "Product Management Intern" (the latter correctly flagged — it's a genuine PM role) are real, defensible removals.
**Carryover, still unaddressed 12 days later:** `3 - CyS & Finance/Quantitative Trading Intern - Virtu.md` is still live in the vault — the exact pure-trading-strategy role [[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34|2026-W34]] flagged as a gate-conformance miss. Not fixed, not removed.
## Standard Conformance
Exact corpus-wide counts (287 live dossiers, `Viewed/` counted separately):
- **`notes:` interlink field: 32/287 (11.1%)**, up from 11/392 (2.8%) at the last review — real, meaningful improvement, tracking the write-time fix (`c50792b`, 2026-08-21) — but this is a floor, not a target: everything written before 2026-08-21 still lacks it, and nothing retroactively backfills it. At the current rate this only reaches 100% once the entire pre-08-21 corpus has cycled out via `recheck.py`.
- **`company/<slug>` tag: 76/287 (26.5%)**, up from 69/392 (17.6%) — same shape, same caveat.
- **`matched_reason` still the bare literal `matched`: 81/287 (28.2%)**. Internship Notes Standard §6 names this as a real, current gap — confirmed structural, not partial: `build_matched_reason()` only special-cases SimplifyJobs and Jose-Gael-Cruz-Lopez; the other 9 of 11 live sources (vanshb03, zshah101, ApplyGuy, Greenhouse, Ashby, Lever, Freehire, AIJobs, InternDock) get the bare string unconditionally by design, not by omission. The 71.8% with a real reason are almost entirely SimplifyJobs-sourced (by far the highest-volume source).
- **`Viewed/` removed-record compliance: 56/56 real removed dossiers carry `removed_date`** (58 files total in `Viewed/`; 2 are index notes — `What was Viewed.md`, `Removed Dossiers MOC.md` — not dossiers, correctly excluded from this count). §4 compliance is effectively complete for everything actually moved there.
## Resource-Limit Health
**Caveat before the numbers: `run.yml` has been `disabled_manually` since 2026-08-29T09:33:51Z** (human's deliberate choice, per [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]'s Prompt 25 entry — not an emergency stopgap, corrected in [[20_Progress/Internship/Building System/Research Loop - Improvement Plan]] this same session). Everything below is a snapshot of a paused system, not a live trend.
- Current buckets: AI/ML 134, Fullstack 42, CyS & Finance 50, Other 61 (287 total, excl. `Viewed/`). AI/ML and CyS & Finance sit at/over the 50-dossier notification threshold; issues #4-6 (filed 2026-08-21) remain open for exactly this — correctly still open, not stale, since the condition they describe is still true.
- Global thresholds: issues #7 (190) and #8 (200), both filed 2026-08-21, both still open — total (287) remains well past both.
- **New since last review: issue #9**, "Revalidate: 15 live dossier(s) now fail current rules" (2026-08-31, still open) — see Gate Conformance above. `revalidate.py` is confirmed firing on its own schedule (`.github/workflows/revalidate.yml`) even while `run.yml` is paused — the two are independent, as designed.
- **Alert-fatigue risk, now demonstrated, not just theoretical:** 6 of 9 total issues ever filed are open, permanent, informational capacity notifications with no closing mechanism. A 7th (#9) is a real, actionable finding sitting in the same list, undifferentiated by urgency. This is the exact risk [[20_Progress/Internship/Building System/Runs/Discovery Step Postmortem — Write-Starvation Incident (2026-08-26)]] named — confirmed here, not hypothetical.
## Findings
1. **Confirmed regression, needs a codebase fix**: `stage1_reject` false-positives on 6 genuine Microsoft SWE/AI dossiers via a "related jobs" sidebar-link content bleed — same bug class as the documented Google careers-listing-shell issue, different platform.
2. **Carryover, unaddressed**: Virtu's pure-trading-strategy dossier, flagged 2026-08-23, still live 12 days later.
3. **Real improvement, correctly attributed**: `notes:`/`company` tag compliance roughly quadrupled since the write-time fix landed — but it's a floor from a point-in-time fix, not a completed backfill.
4. **Alert-fatigue risk is now real, not theoretical**: 6 of 9 GitHub issues are permanent, unclosed, informational — a genuine new finding (#9) sits in the same undifferentiated list.
5. **`run.yml` has been off for the entire period this review covers** — see [[20_Progress/Internship/Building System/Research Loop - Improvement Plan]] for the full throughput analysis; not re-derived here to avoid duplicating that note.
## Decided Fixes
None this pass — every finding above needs a real decision or a codebase change, not a mechanical vault-side correction, per the Review Standard's own rule.
## Open Questions
- Is the Microsoft sidebar-link bleed present on other platforms besides Microsoft's own careers site and Google's? Not checked this pass — worth a `posting_page.py` audit across all 10 currently-live sources' real fetched content, not just the 2 known cases.
- Should the 9 non-Microsoft, non-Virtu dossiers in issue #9 be removed now, or left for a human Screen pass? They look like real, defensible removals but this review doesn't act on findings, per the Standard.
- Given `run.yml` is off, is there any value in running this review again before it's re-enabled, or does the next real Weekly Review wait until discovery resumes?
## Next Period's Watch List
- Whether the Microsoft `stage1_reject` regression gets a real fix (a Prompt, not a manual dossier edit).
- Whether `run.yml` has been re-enabled, and if so, whether the write-gate-failure fix is actually clearing the pre-pause debate-loss cohort as designed.
- Whether the `notes:`/`company` tag percentage keeps climbing (more of the corpus cycling past 2026-08-21) or has stalled.

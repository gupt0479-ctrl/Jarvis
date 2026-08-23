---
type: project
status: active
created: 2026-07-26
updated: 2026-08-23
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]"
tags:
  - internship
  - automation
  - prompts
next: "Prompt 10 (Codebase — continuing the audit session, acting on the Task 7 findings) and Prompt 11 (Jarvis — sync Building System/30_Order/graphify mirror to reflect the audit) are both ready to run. Two design-judgment items from Prompt 9's findings (preference-tier scheme, MAX_DEBATE_LOSSES retuning) are deliberately left for a human decision, not written into either prompt."
---
# Claude Code Prompts — Internship Research Loop
This file holds the next prompt(s) to run, and only that — it gets wiped and rewritten every build cycle, not accumulated. When a prompt finishes and its result is reviewed, its full text and result move into [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] and get deleted from here.

## Prompting Guide In Use
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) — re-apply on every prompt.
- **Front-load everything**, literal scope, explicit Task Order, explicit Files Touched, `high` effort, generous `max_tokens`.
- **Hand over verified facts, but instruct re-checking them** — this round's own lesson: a 6-fork audit found the *stated* root-cause theory (AIJobs' missing category field) was real but not the actual cause of the biggest single problem (49 Zipline dossiers) — the real cause was a separate, undiscovered content-extraction bug. Don't treat any single explanation as settled just because it's plausible and cited.
- **Ask, don't infer, on value judgments.** Two items from this round's findings are explicitly NOT decided in either prompt below — a preference-tier redesign and a debate-loss-threshold retune — because both are the kind of tuning call that needs the human's actual preference, not a plausible-sounding guess.
- **This round's own new lesson: trust a large delegated report, but scope the next step to exactly what it found — don't re-verify it from scratch (expensive, redundant) and don't silently expand past it either.** The two prompts below build directly on Prompt 9's Task 7 report; neither re-derives it.

---

# Codebase
## Prompt 10: Act On The Task 7 Audit — Fix Root Causes, Then Remove What's Confirmed
**Paste this into the same running session that produced the Task 7 report** — it already has that report in context; this prompt references it directly rather than re-deriving it. If you're starting fresh instead, first read Prompt 9's full result in [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] — every citation below assumes you have it.

**Do not re-run the six-bucket audit or re-verify its findings from scratch — that already cost significant time and tokens once. Build directly on what it found.** This prompt has four phases, strictly ordered where noted (fixing a rule must land before removing dossiers that rule now correctly catches — removing first would mean re-deriving the same judgment by hand instead of via the fixed code).

### Phase 1 — Fix the root-cause bugs (blocks Phase 2)
Each gets its own commit, its own tests (real fixtures/citations per this repo's convention — see `CLAUDE.md`), full suite green before moving on:
1. **Zipline/SPA content-detection (Task 7 (f)#1).** `ingestion/posting_page.py`'s fetch/extraction path needs to recognize link-dominated, board-index-shaped content (the Zipline `/open-roles` page shape) and treat it as unconfirmed/thin rather than letting `stage2_confirm()` pass on an unrelated title present on that shared page. This is the highest-priority fix — Phase 2's Zipline re-evaluation depends on it.
2. **`recheck.py`'s `Viewed/` re-sweep bug (Task 7 (g)#2).** `plan_removals()` currently re-sweeps `Viewed/` itself and never checks `status == "removed"` — fix it to skip already-removed dossiers. Real, reproducible, currently degrading data (4 real examples already carry a spurious `(2)` suffix from this).
3. **`_NON_US` denylist gaps (Task 7 (f)#3).** Add Netherlands, Hong Kong, Poland, Israel; consider a bare-city fallback for entries with no country token at all. Cite the exact real postings Task 7 (a)#3 names.
4. **`_ADJACENT_FIELD_COMPANY_HINT_RE` tightening (Task 7 (f)#2).** Extend to generic business/finance/BI role families (the KeyBank/FTI/Vertiv shape). **Regression-test every borderline case Task 7 (b) named as a false positive from the current regex** — Optiver FPGA ×3, Jane Street Cybersecurity Analyst, Appian InfoSec Engineer — confirm they still pass after this change. Getting this wrong would remove real, good postings.
5. **Workday ATS-id pattern (Task 7 (f)#4).** Extend `_ATS_JOB_ID_PATTERNS` to `myworkdayjobs.com`, stripping the trailing `-N` suffix. Cite the FTI/Medtronic/Continental Resources pairs.

### Phase 2 — Now act on the dossiers those fixes affect
1. **Re-evaluate the 49 Zipline dossiers with the now-fixed extraction.** Re-fetch each; some may turn out to be genuinely real SWE roles Zipline actually posts (the board did contain real titles like "Embedded Software Engineer, Validation") — keep confirmed passes, remove confirmed fails, citing the real per-posting content for each, not a blanket action.
2. **Remove the Task 7 (a)#4 non-technical dossiers** (UHY, Continental Resources Geoscience, Walleye Finance & Accounting, CNO Reporting Analyst, Dimensional Fund "...Data and Tools", Vertiv PM ×2, Planning Analytics, Sales Data Analytics ×2, Thermal Application Engineer, KeyBank Data Intern, FTI Technology Intern ×2) — now correctly caught by Phase 1 item 4's fixed regex; confirm each still fails before removing, don't remove on the old report alone.
3. **Remove the Task 7 (a)#3 non-US dossiers** (Marshall Wace Hong Kong/London, Optiver FPGA/Quant Trading Netherlands entries, the 3 more AI & ML flagged) — now correctly caught by Phase 1 item 3.
4. **Dedupe the Task 7 (a)#2 legacy duplicate groups** (~53 dossiers, ~23 groups — Virtu, PDT Partners, Replit, General Matter, Quadrillion, Notion, Continental Resources, American Express, HPR, Chicago Trading Co., Aquatic Capital Management, Freeform, DV Trading, Atoms, Melius, Appian's exclusion-log pair) using the already-correct `cross_source_key()` logic retroactively — keep first-in-`SOURCES`-order per the existing tie-break rule, remove the rest. Include the Workday-sourced pairs once Phase 1 item 5 lands. If the Quadrillion/General Matter pairs (flagged as a possible checkout-freshness race, not an identity bug) still show as separate after this, note it rather than force a fix blind.
5. **Touch nothing in Task 7 (b)** (the borderline list) — AVEVA, Teledyne, HP, Two Sigma, TMEIC, GuideWell, GE Vernova, IMEG, Dimensional Fund "...Operations Insights...", and the 3 Microsoft/Google dossiers with garbage-fetched content. These need human screening, not automated removal — that's Step 2 of the pipeline by design.

### Phase 3 — One cheap empirical check
Check `logs/runs.jsonl`'s `filter_match_counts["Jose-Gael-Cruz-Lopez"]` across recent runs (Task 7 (e)) — report whether the feed is genuinely quiet or silently degraded. Fix only if you find a real, scoped bug; don't speculate past what the numbers show.

### Phase 4 — New GitHub Actions features (Task 7 (g)#1, #3, #4)
Each a separate, tested, scoped addition:
1. A periodic (daily or weekly) job that re-validates existing vault dossiers against current `core/` code and files one digest issue for anything that would now fail — catches this exact class of post-fix drift automatically going forward.
2. A per-run alert when debate-loss exclusions spike well above the normal trickle (e.g. >20 in one run) — would have surfaced the 2026-08-21 burst (287 of 304 total exclusions in one day) as it happened.
3. Wire Phase 3's JGCL finding into an ongoing health check if it turned out to be a real degradation, not just a report.

### Explicitly NOT to implement — flag for the human's decision, don't guess
- **Task 7 (f)#5 — un-tying the preference tier.** A graded/ranked scheme or a diversity tiebreaker is needed so one preferred company (Citadel) can't be crowded out by another preferred company's fresher posting sharing the same tiny bucket budget — but *which* scheme is a real preference call, not something to pick on your own judgment.
- **Task 7 (f)#6 — retuning `MAX_DEBATE_LOSSES`.** The 2026-08-21 burst (287/304 exclusions in one day) shows 5 consecutive hourly losses converts a temporary backlog into a permanent exclusion in ~5 hours — but the right fix (a higher number, a different burst-aware mechanism, something else) is a design call for the human, not a number to guess and ship.
Report both clearly as open decisions with your own reasoning attached — don't implement a guessed answer to either.

### Discipline
Multiple commits, dependency-ordered, full test suite green at every step (this repo's established convention — see the 2026-08-21 five-commit sequence in the Archive for the pattern). Cite real dossiers/postings per fix, matching `CLAUDE.md`'s "every new rule cites the real live data it was built from" rule. The local pre-push hook will block any commit that breaks the suite — that's expected, not an obstacle to work around.

### Report back
Per phase: what was fixed (with test counts), what was removed (count per category, not necessarily every filename), what Phase 2's Zipline re-evaluation actually found (how many of the 49 survived vs. were removed, and why), the Phase 3 JGCL finding, confirmation nothing in (b) was touched, and the two flagged-not-implemented items restated with your reasoning for the human to decide.

---

# Jarvis
## Prompt 11: Sync Building System, 30_Order, and the Graphify Mirror to the Real Audit Findings
**Run this inside the Jarvis vault directly** (Windows, Sonnet 5, high effort). Vault-note work only — no code changes to `internship-research-loop` (that's Prompt 10, running in parallel in a different session; don't wait for it to finish, but don't describe its fixes as already-live either, since they aren't yet when this prompt runs).

**Context, pre-verified — re-check what you touch, don't re-verify everything:**
- Prompt 8 (archived) already: extended `Internship Notes Standard.md` with a real §6, fixed dead Templater syntax across all 9 Career templates, wrote `Tracking Standard.md` for real, refreshed `Internship Pipeline.md` (was stale since 2026-07-29), and investigated Program/Contact/Applying Standards (recommended: don't build them yet, no real gap found). Two items still flagged, still unresolved: the `Viewed/` semantic conflict (`What was Viewed.md` describes "applied for," the shipped system uses it for closed-never-applied — Prompt 8 found `Tracker/Each One/Applied+Result/` and `Applying/Now.md` already serve the need `What was Viewed.md` describes, just unpopulated) and the "review" note-type ambiguity (no match found anywhere).
- Prompt 9 (archived) ran a six-fork audit of all 390 live dossiers plus `Viewed/` and the `Excluded — Losing The Debate.md` log — real bugs found: a Zipline SPA-content-extraction bug (49 dossiers), ~53 legacy cross-source duplicates predating the 2026-08-21 dedup fix, location-denylist gaps, an adjacent-field hint-regex gap, a `recheck.py` re-sweep bug degrading `Viewed/`, and a design-level finding that the debate comparator's preference tier + `MAX_DEBATE_LOSSES=5` converted a one-day arrival burst (2026-08-21) into 287 permanent exclusions within ~5 hours. Full detail: the Task 7 report in the Archive note.
- **The graphify-deletion incident (2026-08-22) is closed, confirmed from this side too**: 350 orphaned duplicate graphify-extracted notes in `60_Claude/40_Project_Briefs/Internship/` were correctly identified (all carried `graphify/EXTRACTED` tags and `source_file` pointers, all duplicates of files still present) and deliberately committed — `f75662ac`, "Prune 350 orphaned graphify duplicate notes from Internship mirror". Verify this yourself (`git log -- "60_Claude/40_Project_Briefs/Internship/"` from the vault root) rather than trusting this line. **Still open, not this prompt's job to fix**: the underlying graphify manifest-ownership bug that produced those 350 orphans in the first place — that's a bug in graphify's own script, a different project. Flag its continued existence if you notice more orphans; don't scope-creep into fixing graphify itself unless it turns out to be a trivial, clearly vault-side config issue.
- The graphify mirror is current as of commit `89fd543` (2026-08-22) — the same code state Prompt 9's audit ran against. It has NOT been regenerated since (no code has changed yet — Prompt 10 will change that, separately, later). It's a large, granular, AST-derived reflection of the actual codebase (hundreds of function/test/docstring-level notes) — genuinely useful as a fast cross-reference, not something that itself needs "fixing" right now.

### Task 1 — Record the Task 7 audit in Building System
1. **`System - Build Log.md`**: add a dated `## 2026-08-23` entry (matching the note's existing per-session style) recording the six-fork audit and its headline findings — cite the Archive note for full detail, don't duplicate the whole Task 7 report inline.
2. **`Source of Truth.md`**: read it fresh. If any of its "what's true about the finished shape right now" claims are now contradicted by real evidence (e.g. does it currently assert the dedup or location gates are fully solid?), correct only what's actually wrong, citing the audit. Don't rewrite sections that are still accurate.

### Task 2 — Cross-reference against the graphify mirror
Use `60_Claude/40_Project_Briefs/Internship/`'s granular function/test-level notes as a fast way to check whether `Building System/` docs or `30_Order/` Standards make any *other* claim about the codebase that doesn't match what the mirror shows — beyond what Prompt 9's bucket-by-bucket audit already covered (that audit read dossier content and pipeline behavior; it didn't systematically check doc claims against code structure). This is a targeted check, not a second full audit — report what you actually checked and what you found, including "nothing further found" if that's the honest result.

### Task 3 — Confirm the graphify-deletion incident stays closed
Verify the `f75662ac` commit yourself per the context above. If you find any *new* orphaned/duplicate graphify-extracted notes (same `graphify/EXTRACTED` tag + `source_file` pointer pattern, same duplicate-of-an-existing-file shape) that have appeared since, flag them plainly — don't delete them yourself without the same kind of git-history cross-check the original incident handoff note used, and don't attempt to fix graphify's manifest-writer bug itself.

### Task 4 — Continue the 30_Order work in light of the audit
Re-check Prompt 8's Task 4 recommendation (no dedicated Program/Contact/Applying Standard yet) against Prompt 9's findings — does anything in the audit reveal a real Program/Contact/Applying-level defect that changes that call? If not, leave the recommendation standing; don't build speculative docs. Otherwise: make sure `Internship Pipeline.md` (refreshed by Prompt 8) and `Source of Truth.md` (per Task 1) describe the current system as **audited, with fixes landing separately** — not as already-fixed, since Prompt 10's code changes aren't live yet when this prompt runs. Getting that tense wrong would make these docs stale again the moment they're written.

### Task 5 — Re-flag what's still genuinely open
The `Viewed/` semantic conflict and the "review" note-type ambiguity from Prompt 8 are still unresolved. If you've been given a decision on either since, act on it; otherwise restate them as still-open in your report — don't guess now either.

### Explicitly out of scope
No code changes to `internship-research-loop`. No fixing graphify's own manifest-writer bug (flag only). No unilateral resolution of the `Viewed/` conflict or the "review" ambiguity. No deleting vault notes without the git-history cross-check discipline the original incident handoff demonstrated.

### Report back
What changed in `System - Build Log.md`/`Source of Truth.md` and why. What Task 2's cross-reference check actually found (or didn't). Confirmation of the deletion-incident's closed status, and whether any new orphans turned up. Whether Task 4's Program/Contact/Applying recommendation still stands. The still-open items from Task 5, restated plainly.

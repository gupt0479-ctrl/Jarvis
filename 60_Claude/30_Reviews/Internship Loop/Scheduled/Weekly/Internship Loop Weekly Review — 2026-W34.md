---
type: evergreen
status: sprout
created: 2026-08-23
updated: 2026-08-23
tags:
  - evergreen
  - review
  - internship
notes:
  - "[[Internship Loop Review Standard]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[Internship Notes Standard]]"
  - "[[10_Areas/Career/Internships/List/Dossiers MOC]]"
next: Fix the notes:/company-tag write-time gap and the Virtu exact-URL duplicate at the code level (separate build session) — this review only names them.
---
# Internship Loop Weekly Review — 2026-W34
## Period Covered
2026-08-17 through 2026-08-23. First run of this review — no prior period to compare against.
## Sources Reviewed
- [x] 12 sampled dossier files, listed in Sample & Method
- [x] [[10_Areas/Career/Internships/List/Dossiers MOC|Dossiers MOC]]'s live capacity table, cross-checked against a direct folder count
- [ ] `Excluded — Losing The Debate.md` — not opened this pass
- [ ] `logs/runs.jsonl` / GitHub issues — not reachable this session (no local clone of `gupta-builds/internship-research-loop`, no `gh` auth); claims below that would need it are flagged, not guessed
## Sample & Method
12 dossiers, 3 per priority bucket, picked at sorted positions 1/15/30 within each bucket folder (alphabetical by filename) — a fixed, repeatable rule, not hand-picked for interesting results. Frontmatter and the classification `[!NOTE]` callout read for all 12; full body read for 2 (AbbVie, Virtu Quantitative Trading) where the callout alone wasn't enough to judge gate/classification fit.
Corpus size this period, counted directly (`find`, not the MOC's cached render): **1 - AI & ML 146, 2 - Fullstack 43, 3 - CyS & Finance 63, Other 139, Viewed 6**. Bucket sum is 391; a separate recursive count of the whole `Dossiers/` tree (excluding `Viewed/`) returned 392 — a real one-file discrepancy, most likely a flat/unsorted note the [[10_Areas/Career/Internships/List/Dossiers MOC|Dossiers MOC]]'s own "Not Yet Sorted" section exists to catch. Not tracked down further this pass — see Open Questions.
## Gate Conformance
**One real miss, high confidence:** `3 - CyS & Finance/Quantitative Trading Intern - Virtu.md` should not have cleared the CS/software-relevance gate at all. Its own body is explicit — "Our Quantitative Traders are responsible for the design, operation, and improvement of high-performance algorithmic trading strategies," "most of their time solving trading problems as they occur in the markets," programming listed only as "some experience... a plus." [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]]'s own gate description names this exact category — "pure trading-strategy research" — as something that "is rejected outright and does not land anywhere — not even Other." This one landed in a priority bucket.
The other 11 sampled dossiers pass: TMEIC's "Applications Intern - AI and Machine Learning" and American Express's "AI Engineer" role are genuinely AI/ML by title and content; the Fullstack and Other samples (Trade Desk, ByteDance, Microsoft, Chevron, Vanguard, Amex Data Analytics) all show real software/data content matching their bucket.
## Standard Conformance
Checked exactly, by grep across the full 392-dossier corpus, not the 12-dossier sample — this is a countable fact, not a judgment call:
- **`notes:` interlink field: 11/392 (2.8%).** [[Internship Notes Standard|Internship Notes Standard]] §1 states this field shipped 2026-07-30 and is required on every dossier. Of the 11 that have it, 6 are Microsoft dossiers all dated `date_found: 2026-08-21` and 4 are `Viewed/` removals (which get the field appended at move time by `recheck.py`, per §4) — meaning the *write-time* path for every other source (SimplifyJobs, JGCL, vanshb03, zshah101, Greenhouse outside the one Microsoft batch, Ashby, AIJobs, freehire) is not adding it. The AbbVie dossier sampled below (`date_found: 2026-08-20`, one day before the Microsoft batch) confirms this: no `notes:` field at all.
- **`company/<slug>` tag: 69/392 (17.6%).** Same shape of gap — present on the one Microsoft dossier sampled, absent on the other 11.
- Body dedup/structure: none of the 12 sampled dossiers showed duplicated paragraphs or jammed ATS-chrome run-ons in this pass — the specific defects [[Internship Notes Standard|Internship Notes Standard]] §2 describes (Conagra's repeated "About Us," `locationsChicago...` run-ons) weren't reproduced in this sample. Not proof they're fixed corpus-wide, just not seen in these 12.
> [!WARNING]
> The `notes:`/tag gap is a real conformance failure, not a documentation lag — the Standard says "shipped," the corpus says otherwise for 97%+ of live dossiers. Whether this is a reverted commit, an unpushed fix, or a fix that only ever touched one source's writer path is a code-side question this review can't answer without repo access — see Open Questions.
## Priority Classification Accuracy
One likely miss, lower confidence than the Gate Conformance finding: `1 - AI & ML/2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate) - AbbVie.md` (`matched_reason: matched`, no specific signal named) is a general Data-Engineering-or-Software-Engineering BTS internship; its only AI/ML-adjacent content is one preferred-qualifications bullet — "ability to apply generative AI to custom software solutions" — among a much longer list of unrelated skills (NodeJS, Vue, Java, SQL, TypeScript). This reads like the same bug class [[20_Progress/Internship/Building System/System - Build Log|Build Log]] recorded for Databricks ("machine learning" in a list of acceptable majors) and Mosaic ("threat" in a safety disclaimer) — an incidental keyword hit, not genuine AI/ML core relevance. Flagged as a Finding, not a Decided Fix, since one example isn't enough to confirm the pattern is systemic versus a single edge case.
The other two `1 - AI & ML` samples (TMEIC, American Express) are correctly classified — the bucket isn't uniformly wrong, this looks like a specific keyword-weighting edge case.
## Resource-Limit Health
Current bucket counts (391 total excl. Viewed) are already past every threshold [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]] defines: all four buckets sit above the 50-per-bucket notification line except Fullstack (43, approaching), and the 391 total is past both the 190 and 200 global issue thresholds. Source of Truth records issues #4-8 firing on 2026-08-21 for exactly this kind of crossing. **Not verified this pass:** whether the continued growth since then (391 now vs. 393 on 2026-08-21, per Source of Truth's own note — so actually roughly flat, `recheck.py` moving closed postings to `Viewed/` at close to the same rate new ones arrive) has triggered any further notification, since this session has no `gh` access to the loop's repo. Treat the "flat" reading as provisional — it's one data point compared against a number quoted in a note, not a trend independently confirmed here.
## Findings
1. **Real Gate Conformance miss** — Virtu's "Quantitative Trading Intern" dossier should not exist per Source of Truth's own stated rule for pure trading-strategy roles. (`3 - CyS & Finance/Quantitative Trading Intern - Virtu.md`)
2. **Real, exact-URL cross-source duplicate** — `3 - CyS & Finance/2027 Internship - Frontend & User Experience - Virtu Financial.md` (source: Greenhouse, found 2026-07-29) and `3 - CyS & Finance/Frontend & User Experience Intern - Virtu Financial.md` (source: vanshb03, found 2026-07-30) share the identical URL `job-boards.greenhouse.io/virtu/jobs/8657500002` — not a same-company-different-title judgment call like the Aquatic case, an exact string match cross-source dedup should catch deterministically.
3. **`notes:` interlink field compliance: 11/392 (2.8%)** against a Standard that says it shipped 2026-07-30 — the write-time gap spans every discovery source except one Microsoft/Greenhouse batch on 2026-08-21.
4. **`company/<slug>` tag compliance: 69/392 (17.6%)** — same shape of gap.
5. **Likely, lower-confidence classification miss** — AbbVie's BTS dossier in `1 - AI & ML` on an incidental "generative AI" mention, same bug class as prior Databricks/Mosaic misses.
## Decided Fixes
None this pass. Every finding above is a real, cited defect, but fixing any of them means editing `gupta-builds/internship-research-loop`'s code — outside what a vault-side review can do, and the general [[30_Order/Standards/Review Standard|Review Standard]]'s rule is that a review surfacing a problem isn't itself authorization to fix it.
## Open Questions
- Is the `notes:`/company-tag write-time gap a reverted fix, an unpushed fix, or a fix that only ever landed in one source's writer path? Needs a direct repo check (`git log` / `git blame` on `vault_writer/writer.py`), not answerable from the vault side alone.
- Should the two Virtu Frontend duplicates be manually merged/one discarded now, or left for the next `recheck.py` cross-source-dedup fix to catch structurally? Leaving it risks the same pair recurring on the next source pull if the underlying dedup key isn't fixed.
- Does the AbbVie-style incidental-keyword classification miss recur often enough to be systemic, or was this one edge case? One data point isn't enough to decide.
- Untracked one-file discrepancy between the per-bucket sum (391) and the recursive non-Viewed count (392) — likely a flat/unsorted note, not chased down this pass.
## Next Period's Watch List
- Re-run the same 3-per-bucket sample rule next week and check whether the `notes:`/tag gap narrowed (a real fix landing) or stayed flat (confirms it's not being worked).
- Check whether the Virtu duplicate pair is still both present, or whether one got caught by a `recheck.py` run in the interim.
- Pull `logs/runs.jsonl` or `gh issue list` directly next time repo access is available, to replace this pass's "not verified" Resource-Limit Health claim with a real number.

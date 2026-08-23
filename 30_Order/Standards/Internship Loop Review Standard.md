---
type: evergreen
status: sprout
created: 2026-08-23
tags:
  - system
  - standards
  - internship
  - review
notes:
  - "[[30_Order/Standards/Review Standard]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[20_Progress/Internship/Building System/System - Build Log]]"
  - "[[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]]"
next: "First run of both review types shipped 2026-08-23. Tighten the Monthly review's Note-Shape Conformance section once the parallel 30_Order note-definition session lands concrete field specs for Program/Contact/Tracker/Applying/Job & Company notes — see that section's own warning."
---
# Internship Loop Review Standard
==A review here checks the internship-research-loop's actual output against what it was designed to do — [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]]'s gates and [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]]'s content rules — never a summary of dossier counts alone.== This is the content standard for `60_Claude/30_Reviews/Internship Loop/Scheduled/{Weekly,Monthly}/`. It is a sibling of [[30_Order/Standards/Review Standard|Review Standard]], not a replacement — that note's shared rigor rules (cite the actual rows/files read, "nothing to report" is a valid finding, `Decided Fixes` only at 100% clarity, no `---` in the body, zero blank lines except after a callout) apply here unchanged. This note states only what's different for the internship loop: two review types, split by which half of [[30_Order/Workflows/Internship Pipeline|the pipeline]] they cover, because the two halves fail in completely different ways — Step 1 (Find) is automated code that breaks in reproducible, bug-shaped ways; Steps 2-9 are human judgment calls that stall in note-hygiene-shaped ways.
## Why Two Review Types, Not One
[[20_Progress/Internship/Building System/Source of Truth|Source of Truth]] itself splits the system this way: "Discovery is a GitHub Actions workflow... mechanical, unattended, cheap by design. Promotion onward is entirely manual, human-judgment-driven." A single review covering both would either drown the rare, high-stakes promotion decisions in weekly dossier noise, or let the automated half's real, recurring bugs (see [[20_Progress/Internship/Building System/System - Build Log|Build Log]]'s 2026-07-26 and 2026-07-29 entries — Databricks PM misclassification, Mosaic "threat" false-positive, Aquatic/Google cross-source dedup misses, the Google-careers-page extraction bug, all confirmed *recurring* three days after "fixed") go unchecked for a month at a time.
- **Weekly — Discovery Review.** Covers Step 1 (Find) only: `List/Dossiers/`, the hourly loop. Runs weekly because the loop writes hourly and the historical bug list above was only ever found by someone actually reading real dossiers, not by trusting the commit log.
- **Monthly — Promotion Review.** Covers Steps 2-9 (Screen through Close): `Programs/`, `Contacts/`, `Tracker/`, `20_Progress/Internship/Applying/`, `Preperation/`. Runs monthly because this half is still lightly exercised (one real promotion, Appian, as of 2026-08-23 per [[20_Progress/Internship/Building System/System - Build Log|Build Log]]) — a weekly cadence would mostly report "nothing new," which the general Review Standard already treats as padding to avoid.
## A Known Dependency — Read Before Running The Monthly Review
> [!WARNING]
> The Monthly review's **Note-Shape Conformance** section (below) grades Program/Contact/Tracker/Applying/Job & Company notes against what [[30_Order/Templates/Career/Program Template|Program Template]], `Contact Template`, `Tracking Template`, and `Applying Template` plus [[30_Order/Workflows/Internship Pipeline|Internship Pipeline]]'s prose already specify — not against a fixed, field-level standard, because none exists yet for these note types (only dossiers have one, [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]]). A separate session is refining concrete definitions for every note type under `30_Order/`. Until that lands, treat this section's findings as provisional and re-derive them once the real standard exists — do not let a stale provisional finding calcify into an assumed rule.
## Maps To
- Templates: [[30_Order/Templates/Career/Internship Loop Weekly Review Template|Internship Loop Weekly Review Template]], [[30_Order/Templates/Career/Internship Loop Monthly Review Template|Internship Loop Monthly Review Template]]
## Used By Workflow
- Manual, human-triggered, same as the general Review Standard — no cron writes a review. Open the relevant template and work it against the real vault state, the same session or shortly after the period it covers.
## Per-Heading Standard — Weekly Discovery Review
### Period Covered
The exact 7-day range.
### Sources Reviewed
Name what was actually opened: the sampled dossier files (exact paths, not "a sample of dossiers"), [[10_Areas/Career/Internships/List/Dossiers MOC|Dossiers MOC]]'s live capacity table, `Excluded — Losing The Debate.md`, and `logs/runs.jsonl`/`System - Build Log` where a code-level claim needs checking.
### Sample & Method
State the sample size and how it was chosen (e.g., N most-recently-written per bucket, or N random per bucket) — 392 live dossiers (as of 2026-08-23: 146 AI & ML, 43 Fullstack, 63 CyS & Finance, 139 Other) cannot all be read every week, and a review that doesn't say how it sampled can't be checked for selection bias.
### Gate Conformance
Check the sample against [[20_Progress/Internship/Building System/Source of Truth|Source of Truth]]'s four hard gates (timing, US location, OPT, CS/software relevance). A dossier that shouldn't have cleared a gate is a Finding, cited by exact file and which gate it should have failed.
### Standard Conformance
Check the sample against [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]]: required frontmatter fields present, `notes:` interlink present and resolving, `company/<slug>` tag present on same-company dossiers, body free of duplicated paragraphs and jammed ATS-chrome run-ons, and — for anything in `Viewed/` — `removed_date`/`removed_reason`/`status: removed` actually set.
> [!WARNING]
> Reporting Standard Conformance from the sample alone. If a compliance question can be answered exactly across the whole corpus with one grep (e.g. "how many dossiers have a `notes:` field"), run it and report the real fraction — sampling is for content-quality checks that need a human read, not for a countable fact a script already answers.
### Priority Classification Accuracy
Spot-check whether the sampled dossier's actual posting content matches the bucket it landed in — this is the exact bug class [[20_Progress/Internship/Building System/System - Build Log|Build Log]] recorded repeatedly (a role matched on an incidental keyword — "threat" in a safety disclaimer, "machine learning" in a list of acceptable majors — not on genuine relevance).
### Resource-Limit Health
Cite the real current bucket counts against the 50-per-bucket notification threshold and the 150/170/190/200 global thresholds ([[20_Progress/Internship/Building System/Source of Truth|Source of Truth]]). Confirm any GitHub issue that should have fired on a crossing actually did (`gh issue list`), not assumed from the threshold math alone.
### Findings
Named, specific, cited by exact file. "Nothing to report" is valid; a missing citation for a claim is not.
### Decided Fixes
Only items with 100% clarity, per the general [[30_Order/Standards/Review Standard|Review Standard]]'s rule. A review surfacing a bug is not itself authorization to patch the loop's code — that's a separate build session.
### Open Questions
Anything short of 100% clarity. Carries forward until resolved.
### Next Period's Watch List
What this review specifically expects to check again next week.
## Per-Heading Standard — Monthly Promotion Review
### Period Covered
The calendar month.
### Sources Reviewed
Name every folder actually opened: `Programs/{Serious,Considering,Job & Company}/`, `Contacts/Each One/{Ongoing,Come Back,Ended}/`, `Tracker/{Each One,Tracker.md,Internship - Dashboard.md}`, `20_Progress/Internship/Applying/{Now.md,Applied/}`, `Preperation/Interviews/`.
### Pipeline Checklist
Grade the month directly against [[30_Order/Workflows/Internship Pipeline|Internship Pipeline]]'s own `Done When` list — it is already a checklist, not prose to re-derive: every program actually pursued has a Program note, a Contacts note, and a Tracker note, all cross-linked; no Applying note has gone more than a week without a Log entry while active; the Dashboard and the Kanban agree on what's in motion; a Program sitting in `Ended/` with no matching Applying note is flagged for discard, per the Pipeline's own rule.
### Per-Program Trace
For every note trio that exists, walk noted → researched → created → applied → result and flag anything stalled beyond what its own `Next Action` field assumed — most concretely, a Tracker note whose stated reasoning cites a date that has since passed (e.g. "no rush, review starts in August" written in July, unrevisited once August arrives).
### Note-Shape Conformance — Provisional
See the dependency warning above. Grade only against what the current templates and Pipeline prose actually say; do not invent stricter rules. Name explicitly which checks are blocked on the pending 30_Order note-definition work rather than skipping them silently.
### Findings
Named, specific, cited by exact file.
### Decided Fixes
Only items with 100% clarity.
### Open Questions
Anything short of 100% clarity, including anything genuinely blocked on the pending note-definition session.
### Next Period's Watch List
What this review specifically expects to check again next month.
## Done Conditions
- Every claim in Gate Conformance, Standard Conformance, and Resource-Limit Health traces to a real file, count, or log row — a fraction stated as "X/392" only when actually counted, not estimated.
- The Weekly review states its sample size and selection method explicitly.
- The Monthly review's Note-Shape Conformance section names what it could not check because the note-definition work is still pending, rather than silently skipping it.
- Decided Fixes contains only items with 100% clarity; anything less stays in Open Questions.
- No `---` in the body; zero blank lines except after a callout; no duplicate frontmatter keys; every `notes:` wikilink resolves.
## Gold Standard Example
[[60_Claude/30_Reviews/Internship Loop/Scheduled/Weekly/Internship Loop Weekly Review — 2026-W34|Internship Loop Weekly Review — 2026-W34]] — the first real review against this Standard, run the same session this Standard was written. Notable for what a full-corpus grep turned up that a sample alone would have missed: the `notes:` interlink field, specified as shipped in [[30_Order/Standards/Internship Notes Standard|Internship Notes Standard]] since 2026-07-30, is actually present on 11 of 392 live dossiers.

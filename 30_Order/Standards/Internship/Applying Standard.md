---
type: evergreen
status: sprout
created: 2026-09-04
updated: 2026-09-04
tags:
  - internship
  - standard
  - applying
notes:
  - "[[Applying Template]]"
  - "[[20_Progress/Internship/Applying/Applications-to-Create]]"
  - "[[30_Order/Workflows/Internship/Application Document Preparation]]"
  - "[[Internship Pipeline]]"
  - "[[30_Order/Standards/Internship/Internship Tracker Standard]]"
next: "First real conformance check happens once a real Applying note exists — none do as of this writing."
---
# Applying Standard
==Was ungoverned.== [[Applying Template]] and [[20_Progress/Internship/Applying/Applications-to-Create]] between them already specify most of what an Applying note needs, but neither is an enforceable content Standard in the shape [[30_Order/Standards/Internship/Internship Tracker Standard]] or [[Internship Notes Standard]] are for their note types. Written 2026-09-04, mirroring those two directly — same section-by-section discipline, same "Done When" mechanical checks. Zero real Applying notes exist yet, so nothing here has been checked against a real example; treat this as the specified target, and the first real note as the thing to check it against, same honesty [[20_Progress/Internship/Applying/Applications-to-Create]] already states about itself.

## Scope
Applies to every note in `20_Progress/Internship/Applying/` created from [[Applying Template]] — one per internship. Does not govern `Applying/Now.md` (the exhaustive live-status rollup) or `Applying/_This Week.md` (the weekly-curated subset) — both are aggregate views over real Applying notes, not Applying notes themselves; see [[20_Progress/Internship/Applying/Applications-to-Create]] for how those two relate. Does not govern resume/cover-letter *content* rules (see [[Resume Alteration Standard]] / [[Cover Letter Alteration Standard]]) — this Standard governs the Applying note itself, the hub those two systems read from and write back to.

## 1. Frontmatter — required fields
Every Applying note carries [[Applying Template]]'s fields, in this order: `type: project, status, program, tracker, company, job_url, date_applied, date_response, next_deadline, resume_version, cover_letter, contacts, interview_note, related_progress, tags, next`. Fail-closed, same convention as every other note type in this system ([[Internship Notes Standard]] §1, [[30_Order/Standards/Internship/Internship Tracker Standard]] §1): a field is present even when its value is genuinely unset (`null`, `[]`), never omitted.

- **`program`** and **`tracker`** must resolve to real notes from the moment the Applying note is created — both already exist by this point (the paired Program note in `Serious/`/`Considering/`, the paired Tracker note in `Current/`), per [[30_Order/Workflows/Internship/Application Document Preparation]]'s `prepare` step.
- **`status`** is the single funnel-stage source of truth for this application: `Preparing` → `Applied` → `Offer`/`Rejected`/`Withdrawn`. Nothing else in the pipeline tracks this independently — the paired Tracker note's `result` field gets set from this same event, not the other way around (see §2).
- **`resume_version`** / **`cover_letter`** stay `null` until the Tailor sequence's `write` step actually produces a file — never a placeholder path to a file that doesn't exist yet.

## 2. Status Lifecycle — `Preparing` → `Applied` → Outcome
Three, and only three, transitions, each tied to a real, named event — never a status word changed on its own for tidiness:
1. **`Preparing`** — set at note creation ([[30_Order/Workflows/Internship/Application Document Preparation]]'s `prepare` step, the start of Internship Pipeline Step 5/Tailor). `date_applied: null`. The note can sit here for a real, extended period while the Tailor sequence (`draft → plan → approve → humanize → write → link`) runs — that is the expected state, not stalled.
2. **`Applied`** — set only at the `apply` sub-step (actual submission), in the same sitting as: `date_applied` populated, the paired Tracker note moved `Current/` → `Applied/`, the paired Program note moved into its own `Ended/` subfolder, an entry added to [[Now]]. A note showing `status: Applied` with `date_applied: null`, or a Tracker note still in `Current/` while its paired Applying note reads `Applied`, is a real, checkable bug — the same mechanical-consistency rule [[30_Order/Standards/Internship/Internship Tracker Standard]] §3 already applies to the Tracker side.
3. **`Offer` / `Rejected` / `Withdrawn`** — set once a real outcome lands, same sitting as the paired Tracker note moving `Applied/` → `Result/` and its `result`/`date_result` fields being set. These three values are shared verbatim with the Tracker note's `result` field — don't let the two notes disagree on which of the three actually happened.

## 3. Body Content — Section By Section
Per [[Applying Template]]:
- **Goal** — one real sentence, this-program-specific. "Get an offer" restated with the role/company swapped in is not a goal; name what winning actually looks like for this one (a return offer, a specific team, a resume-building rung toward the [[10_Areas/Career/Engineer Edge Roadmap]] direction).
- **Current State** — funnel stage, blocker, what's being waited on, plus the diagnostic split from [[System - Build Log]]'s own research (a response rate under 10% signals resume/targeting; responses without offers signal interview prep) — state which one this looks like, don't just restate the raw status.
- **Interlinks (Contact / Job Detail / Networking / Job Description / Fit)** — one line each, pointing at the deeper note. A section here that restates the linked note's full content instead of pointing to it is a violation, not thoroughness — the whole point of splitting Applying from Tracker/Program/Contact is that each note owns its own depth.
- **Documents** — one line each for Resume/Cover Letter, naming what the file leads with, not a copy of its content. Both fields stay unset until the Tailor sequence's `write` step actually runs (see [[Resume Alteration Standard]] §6, [[Cover Letter Alteration Standard]] §5 for the overwrite-until-`date_applied` rule this note's own `date_applied` field gates).
- **Next Action** — the single next physical move, mirroring `next:` in frontmatter exactly. Two notes disagreeing between prose and frontmatter on this field is a sync bug, same class as §2's status/date mismatch.
- **Open Questions** — genuinely unresolved items only, never a routine-steps checklist repurposed as this section.
- **Log** — dated, one line per real event. Per [[Internship Pipeline]]'s own Done When list: no active Applying note goes more than a week without a Log entry. A note that's gone stale here is a real finding for [[Internship Loop Review Standard]]'s Monthly Promotion Review, not something to quietly backfill after the fact.

## 4. Interlink Contract
- Applying `program` → the paired Program note.
- Applying `tracker` → the paired Tracker note (this field doesn't exist on the pre-2026-09-04 template text elsewhere in this system — [[Applying Template]] already carries it; treat it as required, not optional).
- Applying `contacts` → the paired Contact note(s) (a list, since a company can have more than one real contact by the time an application is live).
- Applying `resume_version` / `cover_letter` → the two generated files, once they exist.
- Applying `interview_note` → the paired `Preperation/Interviews/<company>.md` note, once Internship Pipeline Step 8 is reached.
No other cross-link field exists for this note type — don't invent one; a real new need is a template change to propose explicitly, same rule [[promote-dossier]]'s note-templates reference already states for Program/Contact/Tracker.

## Done When
- Every Applying note's `status` and `date_applied`/paired-Tracker-folder agree — no note showing `Applied` with a null `date_applied`, or vice versa.
- `program`, `tracker`, and every populated `contacts` entry resolve to real notes, no broken links.
- No active Applying note has gone more than a week without a Log entry.
- `resume_version`/`cover_letter` are populated if and only if the Tailor sequence's `write` step has actually run for that application.
- The Interlinks section stays one line per subsection — depth lives on the linked note, not restated here.

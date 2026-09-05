---
type: evergreen
status: sprout
created: 2026-07-16
updated: 2026-08-28
tags:
  - system
  - workflow
  - internship
  - career
notes:
  - "[[00_Workflows Index]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[10_Areas/Career/Internships/Internships Hub]]"
  - "[[Internship - Design Rationale]]"
  - "[[30_Order/Workflows/Internship/Application Document Preparation]]"
  - "[[30_Order/Standards/Internship/Applying Standard]]"
  - "[[30_Order/Workflows/Internship/Internship Tracking Workflow]]"
  - "[[30_Order/Workflows/Internship/Internship Review System]]"
next: null
---
# Internship Pipeline
Move a posting from "found on the web" to "offer or rejection recorded," without losing the research or the relationship along the way.
**Use when:** finding, pursuing, or tracking any internship (or later, full-time role — this pipeline is role-type-agnostic by design).
**Splits across:** `10_Areas/Career/Internships/` (reference — research, contacts, methods, stays true regardless of where any single application stands) and `20_Progress/Internship/` (execution — live status, drafts, prep, everything that changes week to week).
## Why It's Split This Way
Company research (comp, eligibility, deadlines, traps) doesn't change once you've written it down — that's Areas. Application status changes every time you hear back — that's Progress. Putting both on one note (the old pattern) meant the "durable" research file was getting rewritten every week just to update a status field. Splitting them means a Program note stays `status: tree`-stable while its Applying note carries all the churn.
## The Pipeline
```
find           List/Dossiers/ — auto-discovered by internship-research-loop, screened for eligibility
               (US, OPT, Bachelor's, timing) and CS/software relevance, sorted into priority
               subfolders with a one-line reason at the top of each note. Manual finds still get
               a row in List/YYYY-MM Found.md.
   ↓ screen — the fit test: does this push toward the goal? does it fit real skills/interests?
     (contact-reachability is noted, never a gate; pay is never a factor)
commit         Programs/Serious/<name>.md or Programs/Considering/<name>.md (same template, same
               depth — split only by preference/timing, never rigor) + Contacts/Each One/<name>.md
               (company-level contact research, run via the loop's enrich.py on promotion) —
               created together, cross-linked. No resume/cover-letter work happens at this step.
   ↓ once the Program note exists
track          Tracker/Each One/Current/<name>.md — the dated index (noted/researched/created/
               applied/result, deadline, contact link, related notes, url). Source of truth until
               an Applying note exists.
   ↓ need a way in beyond the portal
reach out      The live unsent draft lives in the Contacts/Each One note already created above,
               built from Contacts/Mimic.md templates.
   ↓ need a resume and cover letter that survive the JD, not just the ATS
prepare        Applying/<name>.md (Applying Template) created now — before either document exists —
               status: Preparing, date_applied null. Links program/tracker/contact, records the job
               URL and one-line JD/networking/fit summaries. See Application Document Preparation.
tailor         Resumes/Main Resume.md (bullet bank) + Cover Letters/Main Cover Letter.md (paragraph
               bank) → one Resumes/<Role> - <Company>.docx + one Cover Letters/<Role> - <Company>.docx,
               drafted, human-approved, and Humanizer-passed before either file is written. Overwritten
               in place until date_applied is set. Full flow: Application Document Preparation.
   ↓ actually ready to apply, not just interested
deep dive      Programs/Job & Company/<Company> - <Position>.md — interview-prep-grade research,
               created only now, not at commit time
   ↓ submit
apply          Applying/Now.md entry added; Applying note's status → Applied, date_applied set;
               Tracker note moves Current/ → Applied/; Program note moves to its own Ended/ subfolder
   ↓ you get a screen or an interview
prep           Preperation/Interviews/<company>.md — linked from the Applying note's interview_note field
   ↓ outcome lands
close          Applying note status → Offer / Rejected / Withdrawn; Tracker note moves to Result/.
               Program note stays as reference for next cycle or a referral.
across all of it:  Tracker/Internship - Dashboard.md (whole-process) + Tracker/Tracker.md (kanban) + Applying/Now.md (exhaustive live list) · Cheats/ grows whenever something works
```
## Step 1 — Find (List + Dossiers)
Two paths in now. Automated: `internship-research-loop` writes screened matches straight into `List/Dossiers/`, sorted into priority subfolders (`1 - AI & ML/`, `2 - Fullstack/`, `3 - CyS & Finance/`, `Other/`) with a one-line reason at the top of each note — see [[Source of Truth]] for exactly what the loop screens for before a dossier ever lands. Manual: anything you come across yourself — a career fair conversation, LinkedIn, Handshake — still gets one row in this month's `List/YYYY-MM Found.md` (use [[List Monthly Log Template]]), and can move to Step 2 without ever having been a dossier. Neither is a commitment. Most dossiers and most rows never get promoted, and that's fine.
**Which candidates actually get written, shipped 2026-08-21:** each bucket only writes 3 AI/ML, 3 Fullstack, 3 CyS & Finance, 1 Other per push, ordered by a deterministic **debate comparator** — preferred-company tier (a `preference_tier` field, per `core/profile.yaml`'s `preferred_companies`) → bucket fill-need → recency. A candidate that loses the comparator's sort 5 consecutive runs moves to [[10_Areas/Career/Internships/List/Excluded — Losing The Debate]] — a reviewable, append-only log, never a silent permanent drop; if the comparator's call looks wrong on any entry there, promote it by hand. Each priority bucket also carries a 50-dossier capacity notification (visible on [[10_Areas/Career/Internships/List/Dossiers MOC]]'s live capacity table) and the global total logs/files a GitHub issue at set thresholds — a notification, never a write refusal. Full spec: [[Source of Truth]].
**Closed postings move, they don't vanish.** `recheck.py` moves a dossier for a posting that's gone dead to `10_Areas/Career/Internships/List/Dossiers/Viewed/` instead of deleting it — its MOC and `company/<slug>` links stay, plus a link to `Removed Dossiers MOC`. `Viewed/` is a human triage bin, never a pipeline write target for new dossiers. Full rule: [[Internship Notes Standard]] §4.
**Audited, not the same as bug-free.** All of the above is live and firing, but a 2026-08-23 audit found real implementation gaps still sitting in it (content-extraction leaks, lingering duplicates, location/relevance-gate gaps, a `Viewed/` re-processing bug, a debate-comparator design gap) — fixes are queued, not yet shipped. Current, cited status: [[Source of Truth]].
**Manual web clips (refined 2026-07-29):** a web-clipped internship (a full posting captured into `60_Claude/05_Clippings/Web/Internships/`, not just a row in the monthly log) skips the dossier-as-screening-artifact phase entirely and goes straight to a Program note in `Serious/` or `Considering/`, run through the same Step 2 fit test below. Once that Program note exists, the original clipping moves into `List/Dossiers/<priority folder>/`, rewritten in the loop's own dossier template (frontmatter + `## Posting` body) without losing any of its original content — this makes it a record of where the internship came from, not a screening artifact, since screening already happened via the Program note. Both the dossier and the Program note get marked manually found (`source: manual` / `list_origin: manual-web-find (Anant)`), never as loop-discovered. First real run of this refined rule: the four backlogged `Internships/` clippings (Uber, Nuro, Deepgram, Western Digital) on 2026-07-29 — see [[10_Areas/Career/Internships/Programs/Serious/2027-Uber-SWE-CareerPrep]] and its three siblings.
## Step 2 — Screen (the fit test)
Before committing real hours, every dossier or manual find passes the same fit test, regardless of which priority folder it landed in (including `Other` — that folder gets the same scrutiny, not less):
- **Goal-push** — does this role move you toward the systems-minded AI engineer direction in [[Engineer Edge Roadmap]]? Bias against roles that don't.
- **Personal fit** — does it map to something you've built or want to build, worth learning, a real use of current skills?
- **Contact reachability** — noted on the note, never a gate. A black-box ATS with no findable contact doesn't disqualify a role that passes the two tests above.
- **Pay is not evaluated here, or anywhere in this pipeline.**
**Record the call, don't just make it (decided 2026-08-23).** This was the one step in the pipeline with no artifact — a mental check that left no trace. Record the decision directly on the dossier: `screened_date`, `screened_decision` (`pass`/`reject`), `screened_reason` (the specific goal-push or personal-fit signal, not a bare "passed"). Full field spec and the reasoning for putting this on the dossier itself rather than a separate note: [[Internship Notes Standard]] §7.
## Step 3 — Commit (Programs + Contacts + Tracker)
When something passes the fit test, promote it in one sitting:
- **Programs/Serious/<name>.md or Programs/Considering/<name>.md — identical template, identical research depth in both. The split is preference/timing only (pursuing now vs. later/undecided), never rigor — don't write a thinner note for Considering.
- **Contacts/Each One/<name>.md** — company-level contact research (recruiter, HR, relevant public info), run via the loop's `enrich.py` at promotion time, linked from the Program note.
- **Tracker/Each One/<name>.md** — created only once the Program note exists. The dated index: noted/researched/created dates, deadline, applied date, result date, contact link, related notes, url. Source of truth for "where does this stand" until an Applying note exists.
> [!WARNING]
> If you find yourself editing a Programs note to change a status word, stop — that field belongs on the Applying note (once it exists) or the Tracker note. Programs notes should only change when a fact about the program itself changes (deadline moved, comp updated).
## Step 4 — Reach Out (Contacts)
The Contact note created in Step 3 ([[Contact Template]]) holds durable facts about the contact(s) found and, inline, the current unsent draft message. `Contacts/Mimic.md` is the template library — cold DM, recruiter follow-up, referral ask, thank-you note — pull a template into the Current Draft section and edit it until it sounds like you, not the template. Log every real exchange in Conversation Log so a later Claude Code session (or you, six weeks from now) knows what's already been said. Move the Contact note between `Ongoing/`, `Come Back/`, and `Ended/` as the relationship's real state changes.
This is drafting help only. No message sends itself — every draft here is reviewed and sent by hand.
## Step 5 — Tailor (Resumes)
The Applying note ([[Applying Template]]) is created at the **start** of this step, not at submission — `status: Preparing`, `date_applied` null. `Resumes/Main Resume.md` is the editable bullet bank and `Cover Letters/Main Cover Letter.md` is its cover-letter equivalent — the actual sources of truth, since a DOCX/PDF export isn't taggable or diffable. Full sequencing (draft → content-plan approval → Humanizer pass → write) lives in [[30_Order/Workflows/Internship/Application Document Preparation]]; the short version: for each application, write or overwrite exactly one `Resumes/<Role> - <Company>.docx` and one `Cover Letters/<Role> - <Company>.docx`, linked back from the Applying note's `resume_version` and `cover_letter` fields. Every claim in either document must trace to real evidence — see [[Resume Alteration Standard]] and [[Cover Letter Alteration Standard]] — never invented to match a JD.
## Step 6 — Deep Dive (Job & Company)
Once you're actually ready to apply — not at commit time, and not for every program in `Considering/` — create `Programs/Job & Company/<Company> - <Position>.md`: relevant company projects, the company's mission mapped concretely to your own direction, role-specific research beyond the Program note, and what the verified contact has personally contributed. This is what makes an interview conversation sound genuinely informed. Past two real positions at one company, switch to a `[Company]/` subfolder with one note per position.
## Step 7 — Apply
Submit. The Applying note already exists (created at the start of Step 5, per [[30_Order/Workflows/Internship/Application Document Preparation]]) — this step updates it, not creates it: set `date_applied`, move `status` to `Applied`, add an entry to `Applying/Now.md`, confirm the `applying_note`/`program` link both ways, move the Tracker note from `Current/` to `Applied/`, and move the Program note into its own `Ended/` subfolder. Source-of-truth responsibility for "what's going on with this application" stays on the Applying note: Current State, Next Action, Open Questions, meeting-prep content.
> [!IMPORTANT]
> A Program note sitting in `Ended/` with no matching Applying note gets discarded, not kept — `Ended` means applied, and without an Applying note nothing was actually submitted. Following this pipeline as written, every Program that reaches Step 5 already has one; a Program in `Ended/` with none is evidence a step was skipped, not an expected case.
## Step 8 — Prep (Interviews)
Once a program moves to Phone Screen or Onsite, create `Preperation/Interviews/<company>.md` and link it from the Applying note's `interview_note` field. `Preperation/Interviews/Interview Questions.md` in the same folder is the generic behavioral bank — pull from it, don't duplicate it. `Preperation/System Design/` is the sibling folder for the system-design drill bank (see [[System Design Practice]]) — a different prep category, not interview-specific company research.
## Step 9 — Close
When an outcome lands, update the Applying note's `status` to `Offer`, `Rejected`, or `Withdrawn`, move the Tracker note from `Applied/` to `Result/` and set its result date, and add the final Log entry. Leave the Program note alone — it's still valid reference if you (or a friend) reapply next cycle.
## Ongoing Views — Not Steps, Always Live
- **`Tracker/Internship - Dashboard.md`** — the whole-process view: dossier pipeline health against the count limit, Programs counts, the Applying funnel, Contacts relationship state, all in one screen.
- **`Tracker/Tracker.md`** — the kanban glance, this week's cards.
- **`Applying/Now.md`** — every internship currently mid-application, exhaustive.
- **`Tracker/Each One/<name>.md`** — the per-internship dated index created in Step 3, moving `Current/` → `Applied/` → `Result/` as the real state changes.
- **`List/Dossiers/_Today/` + `Tracker/Deadline Tracker.md`** — manual intake/deadline triage, run as an ad hoc sweep rather than a scheduled step. See [[Deadline and Intake Triage Standard]].
## Cadence
- **As you find things:** add a row to this month's List log. Thirty seconds, no exceptions.
- **Weekly (the Friday ritual):** work through `Applying/_This Week.md` — which programs are actually in motion, what's due, what needs a follow-up.
- **Per application:** the full Step 3 through Step 8 sequence happens once, when you commit.
## Cheats
`Cheats/` is where anything that actually worked gets written down — a tactic, a shortcut, a system, using [[Cheat Template]]. It grows only from real results, not speculation, and it is explicitly not being redesigned preemptively: the instruction behind this folder is to use it as-is until it produces a real blocker, then fix that blocker, not to polish it now.
## Step 1 Is Automated — Steps 2+ Are Manual By Design
Step 1 (Find) is live: `gupta-builds/internship-research-loop` (GitHub Actions, hourly, eight sources as of 2026-07-26) writes directly into `List/Dossiers/`'s priority subfolders — see [[Source of Truth]] for what it actually screens for. The full resource-limit spec (debate comparator, capacity notifications, recheck-to-`Viewed/`) shipped 2026-08-21 and is confirmed live against a real `run.yml` trigger the same day, not just committed. **Steps 2 through 9 remain entirely manual by design.** Step 3 has now run for real four times, not once: the Appian promotion (2026-07-26, via the `/promote-dossier` skill) plus three manual-web-find promotions straight to Program notes (Uber, Western Digital, Deepgram, all 2026-07-29 — see Step 1's manual-web-clip note above). All four are still pre-application — none has an Applying note yet, so Steps 4 through 9 remain unexercised against real activity. Don't treat four promotions as evidence the whole downstream flow is proven at scale.
## Frontmatter Quick Reference

| Note | Type | Lives in |
| --- | --- | --- |
| List monthly log | `input` | `10_Areas/Career/Internships/List/` |
| Dossier | (no `type` — auto-generated) | `10_Areas/Career/Internships/List/Dossiers/<priority folder>/` |
| Program | (no `type` — reference data) | `10_Areas/Career/Internships/Programs/Serious/` or `Programs/Considering/`, moves to that folder's `Ended/` on submit |
| Job & Company | (no `type` — deep-dive research) | `10_Areas/Career/Internships/Programs/Job & Company/` |
| Contact (per internship) | `contact` | `10_Areas/Career/Internships/Contacts/Each One/` |
| Cheat | `evergreen` | `10_Areas/Career/Internships/Cheats/` |
| Tracker (per internship) | (index note) | `10_Areas/Career/Internships/Tracker/Each One/` |
| Applying | `project` | `20_Progress/Internship/Applying/`, created at the start of Step 5, not at submission |
| Interview prep | `project` or `input` | `20_Progress/Internship/Preperation/Interviews/` |
| System design drill bank | `project` | `20_Progress/Internship/Preperation/System Design/` |
| Tailored resume (per application) | (no `type` — working document, `.docx`) | `20_Progress/Internship/Resumes/` |
| Tailored cover letter (per application) | (no `type` — working document, `.docx`) | `20_Progress/Internship/Cover Letters/` |
| LinkedIn post | `output` | `20_Progress/Internship/Posts/` |
## Done When
- Every posting you'd regret forgetting has a List row or a dossier.
- Every program you're actually pursuing has a Programs note, a Contacts note, and a Tracker note, all cross-linked — plus an Applying note once real application preparation starts, not just once it's submitted.
- No Applying note has gone more than a week without a Log entry while it's active.
- The Dashboard and the Kanban agree on what's currently in motion.
- The session log records any structural change to this pipeline.

---
type: evergreen
status: sprout
created: 2026-07-16
updated: 2026-07-26
tags:
  - system
  - workflow
  - internship
  - career
notes:
  - "[[00_Workflows Index]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[10_Areas/Career/Internships/Internships Hub]]"
next:
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
               created together, cross-linked
   ↓ once the Program note exists
track          Tracker/Each One/<name>.md — the dated index (noted/researched/created/applied/
               result, deadline, contact link, related notes, url). Source of truth until an
               Applying note exists.
   ↓ once real application activity starts
apply          Applying/<name>.md — the live narrative (Current State, Next Action, Open
               Questions, meeting-prep content). Source-of-truth responsibility for "what's going
               on with this application" transfers here once it's created.
   ↓ need a way in beyond the portal
reach out      The live unsent draft lives in the Contacts/Each One note already created above,
               built from Contacts/Mimic.md templates.
   ↓ need a resume that survives the JD, not just the ATS
tailor         Resumes/Main Resume.md (bullet bank) → Resumes/Altered/<company>.md (per-application cut)
   ↓ you get a screen or an interview
prep           Interviews/Prep/<company>.md — linked from the Applying note's interview_note field
   ↓ outcome lands
close          Applying note status → Offer / Rejected / Withdrawn. Program note stays as reference for next cycle or a referral.
across all of it:  Tracker/Internship - Dashboard.md (detailed, Dataview) + Tracker/Tracker.md (kanban, at-a-glance) · Cheats/ grows whenever something works
```
## Step 1 — Find (List + Dossiers)
Two paths in now. Automated: `internship-research-loop` writes screened matches straight into `List/Dossiers/`, sorted into priority subfolders (`1 - AI & ML/`, `2 - Fullstack/`, `3 - CyS & Finance/`, `Other/`) with a one-line reason at the top of each note — see [[Source of Truth]] for exactly what the loop screens for before a dossier ever lands. Manual: anything you come across yourself — a career fair conversation, LinkedIn, Handshake — still gets one row in this month's `List/YYYY-MM Found.md` (use [[List Monthly Log Template]]), and can move to Step 2 without ever having been a dossier. Neither is a commitment. Most dossiers and most rows never get promoted, and that's fine.
## Step 2 — Screen (the fit test)
Before committing real hours, every dossier or manual find passes the same fit test, regardless of which priority folder it landed in (including `Other` — that folder gets the same scrutiny, not less):
- **Goal-push** — does this role move you toward the systems-minded AI engineer direction in [[10_Areas/Career/Engineer Edge Roadmap]]? Bias against roles that don't.
- **Personal fit** — does it map to something you've built or want to build, worth learning, a real use of current skills?
- **Contact reachability** — noted on the note, never a gate. A black-box ATS with no findable contact doesn't disqualify a role that passes the two tests above.
- **Pay is not evaluated here, or anywhere in this pipeline.**
## Step 3 — Commit (Programs + Contacts + Tracker)
When something passes the fit test, promote it in one sitting:
- **Programs/Serious/<name>.md or Programs/Considering/<name>.md** — identical template, identical research depth in both. The split is preference/timing only (pursuing now vs. later/undecided), never rigor — don't write a thinner note for Considering.
- **Contacts/Each One/<name>.md** — company-level contact research (recruiter, HR, relevant public info), run via the loop's `enrich.py` at promotion time, linked from the Program note.
- **Tracker/Each One/<name>.md** — created only once the Program note exists. The dated index: noted/researched/created dates, deadline, applied date, result date, contact link, related notes, url. Source of truth for "where does this stand" until an Applying note exists.
> [!WARNING]
> If you find yourself editing a Programs note to change a status word, stop — that field belongs on the Applying note (once it exists) or the Tracker note. Programs notes should only change when a fact about the program itself changes (deadline moved, comp updated).
## Step 4 — Apply (Applying note)
Once real application activity actually starts on this one — not at commit time — create the Applying note ([[Applying Template]]) and link it both ways (`applying_note` on the Program, `program` on the Applying note). Source-of-truth responsibility for "what's going on with this application" transfers here: Current State, Next Action, Open Questions, and whatever's useful to have on hand in a meeting. The Tracker note keeps living alongside it as the dated index — the two aren't redundant, Tracker is the timeline, Applying is the narrative.
## Step 5 — Reach Out (Contacts)
The Contact note created in Step 3 ([[Contact Template]]) holds durable facts about the contact(s) found and, inline, the current unsent draft message. `Contacts/Mimic.md` is the template library — cold DM, recruiter follow-up, referral ask, thank-you note — pull a template into the Current Draft section and edit it until it sounds like you, not the template. Log every real exchange in Conversation Log so a later Claude Code session (or you, six weeks from now) knows what's already been said.
This is drafting help only. No message sends itself — every draft here is reviewed and sent by hand.
## Step 6 — Tailor (Resumes)
`Resumes/Main Resume.md` is the editable bullet bank — the actual source of truth, since the PDF isn't taggable or diffable. Per the research behind this system: response rate moves most when you adjust the **top third** of the resume per role, not when you rewrite the whole thing. For each Applying note, create `Resumes/Altered/<company>.md`: pull the 3-5 bullets that best match this specific JD's keywords, in order, and link it back from the Applying note's `resume_version` field.
## Step 7 — Prep (Interviews)
Once a program moves to Phone Screen or Onsite, create `Interviews/Prep/<company>.md` and link it from the Applying note's `interview_note` field. `Interviews/Prep/Interview Questions.md` in the same folder is the generic bank — pull from it, don't duplicate it.
## Step 8 — Track (three views, one truth)
- **`Tracker/Internship - Dashboard.md`** — the detailed view. Dataview queries pull static facts from Programs and live status from Applying, shown as separate tables (plain Dataview can't cleanly join two folders into one row, so don't try to fake a merge).
- **`Tracker/Tracker.md`** — the kanban view. A fast visual glance across Interesting → To Apply → Applying Today → Applied, cards linked to the actual Applying notes. Update it by hand when a card's stage changes; it is not meant to be exhaustive, the Dashboard is.
- **`Tracker/Each One/<name>.md`** — the per-internship dated index created in Step 3. Not a replacement for the Dashboard or Kanban's at-a-glance view — it's the fast-scan detail record for one specific internship.
## Step 9 — Close
When an outcome lands, update the Applying note's `status` to `Offer`, `Rejected`, or `Withdrawn`, set the Tracker note's result date, and add the final Log entry. Leave the Program note alone — it's still valid reference if you (or a friend) reapply next cycle.
## Cadence
- **As you find things:** add a row to this month's List log. Thirty seconds, no exceptions.
- **Weekly (the Friday ritual):** work through `Applying/_This Week.md` — which programs are actually in motion, what's due, what needs a follow-up.
- **Per application:** the full Step 3 through Step 7 sequence happens once, when you commit.
## Cheats
`Cheats/` is where anything that actually worked gets written down — a tactic, a shortcut, a system, using [[Cheat Template]]. It grows only from real results, not speculation, and it is explicitly not being redesigned preemptively: the instruction behind this folder is to use it as-is until it produces a real blocker, then fix that blocker, not to polish it now.
## Step 1 Is Now Automated — Steps 2+ Are Not
Step 1 (Find) is live, not deferred: `gupta-builds/internship-research-loop` (GitHub Actions, hourly, six sources as of 2026-07-25) writes directly into `List/Dossiers/`'s priority subfolders — see [[Source of Truth]] for what it actually screens for. **Steps 2 through 9 remain entirely manual by design** and, as of 2026-07-19, have never been exercised against real automated output — see [[20_Progress/Internship/Building System/Research Loop - Improvement Plan]] Priority 1. Don't treat automated Step 1 as evidence the rest of this pipeline works; it hasn't been run yet.
## Frontmatter Quick Reference
| Note | Type | Lives in |
| --- | --- | --- |
| List monthly log | `input` | `10_Areas/Career/Internships/List/` |
| Dossier | (no `type` — auto-generated) | `10_Areas/Career/Internships/List/Dossiers/<priority folder>/` |
| Program | (no `type` — reference data) | `10_Areas/Career/Internships/Programs/Serious/` or `Programs/Considering/` |
| Contact (per internship) | `contact` | `10_Areas/Career/Internships/Contacts/Each One/` |
| Cheat | `evergreen` | `10_Areas/Career/Internships/Cheats/` |
| Tracker (per internship) | (index note) | `10_Areas/Career/Internships/Tracker/Each One/` |
| Applying | `project` | `20_Progress/Internship/Applying/` |
| Interview prep | `project` or `input` | `20_Progress/Internship/Interviews/Prep/` |
| Altered resume | (no `type` — working document) | `20_Progress/Internship/Resumes/Altered/` |
| LinkedIn post | `output` | `20_Progress/Internship/Posts/` |
## Done When
- Every posting you'd regret forgetting has a List row or a dossier.
- Every program you're actually pursuing has a Programs note, a Contacts note, and a Tracker note, all cross-linked — plus an Applying note once real activity starts.
- No Applying note has gone more than a week without a Log entry while it's active.
- The Dashboard and the Kanban agree on what's currently in motion.
- The session log records any structural change to this pipeline.

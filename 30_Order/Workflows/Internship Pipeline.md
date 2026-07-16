---
type: evergreen
status: sprout
created: 2026-07-16
updated: 2026-07-16
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
find           List/YYYY-MM Found.md — every posting found this month, one row each
   ↓ decide to seriously pursue it
commit         Programs/<name>.md (static research) + Applying/<name>.md (live status) — created together, cross-linked
   ↓ need a way in beyond the portal
reach out      Contacts/<person>.md — facts + the live unsent draft, built from Contacts/Mimic.md templates
   ↓ need a resume that survives the JD, not just the ATS
tailor         Resumes/Main Resume.md (bullet bank) → Resumes/Tailored/<company>.md (per-application cut)
   ↓ you get a screen or an interview
prep           Interviews/<company>.md — linked from the Applying note's interview_note field
   ↓ outcome lands
close          Applying note status → Offer / Rejected / Withdrawn. Program note stays as reference for next cycle or a referral.
across all of it:  Tracker/Internship - Dashboard.md (detailed, Dataview) + Tracker/Tracker.md (kanban, at-a-glance) · Cheats/ grows whenever something works
```
## Step 1 — Find (List)
Every posting you come across — from a career fair conversation, a GitHub internship-list repo, LinkedIn, Handshake, or (later) an automated feed — gets one row in this month's `List/YYYY-MM Found.md`. Use [[List Monthly Log Template]]. Keep it to a link, the requirements, and one line on what the role actually is. This is not a commitment. Most rows never get promoted, and that's fine — the point is not losing a posting you'd otherwise forget by next week.
## Step 2 — Commit (Programs + Applying)
When a posting is worth the hours to prepare for, promote it: create a Programs note ([[Program Template]]) and an Applying note ([[Applying Template]]) in the same sitting, and link them both ways (`applying_note` on the Program, `program` on the Applying note). The List row's `Promoted` column points at the new Program note.
- **Programs/** holds what won't change: comp, eligibility, deadlines, traps, prep checklist.
- **Applying/** holds what will: funnel stage, next action, dates, links to the resume version and contacts actually used for this specific application.
> [!WARNING]
> If you find yourself editing a Programs note to change a status word, stop — that field belongs on the Applying note. Programs notes should only change when a fact about the program itself changes (deadline moved, comp updated).
## Step 3 — Reach Out (Contacts)
A Contact note ([[Contact Template]]) holds durable facts about a person and, inline, the current unsent draft message to them. `Contacts/Mimic.md` is the template library — cold DM, recruiter follow-up, referral ask, thank-you note — pull a template into the Current Draft section and edit it until it sounds like you, not the template. Log every real exchange in Conversation Log so a later Claude Code session (or you, six weeks from now) knows what's already been said.
This is drafting help only. No message sends itself — every draft here is reviewed and sent by hand.
## Step 4 — Tailor (Resumes)
`Resumes/Main Resume.md` is the editable bullet bank — the actual source of truth, since the PDF isn't taggable or diffable. Per the research behind this system: response rate moves most when you adjust the **top third** of the resume per role, not when you rewrite the whole thing. For each Applying note, create `Resumes/Tailored/<company>.md`: pull the 3-5 bullets that best match this specific JD's keywords, in order, and link it back from the Applying note's `resume_version` field.
## Step 5 — Prep (Interviews)
Once a program moves to Phone Screen or Onsite, create `Interviews/<company>.md` and link it from the Applying note's `interview_note` field. `Interview Questions.md` in the same folder is the generic bank — pull from it, don't duplicate it.
## Step 6 — Track (two views, one truth)
- **`Tracker/Internship - Dashboard.md`** — the detailed view. Dataview queries pull static facts from Programs and live status from Applying, shown as separate tables (plain Dataview can't cleanly join two folders into one row, so don't try to fake a merge).
- **`Tracker/Tracker.md`** — the kanban view. A fast visual glance across Interesting → To Apply → Applying Today → Applied, cards linked to the actual Applying notes. Update it by hand when a card's stage changes; it is not meant to be exhaustive, the Dashboard is.
## Step 7 — Close
When an outcome lands, update the Applying note's `status` to `Offer`, `Rejected`, or `Withdrawn` and add the final Log entry. Leave the Program note alone — it's still valid reference if you (or a friend) reapply next cycle.
## Cadence
- **As you find things:** add a row to this month's List log. Thirty seconds, no exceptions.
- **Weekly (the Friday ritual):** work through `Applying/_This Week.md` — which programs are actually in motion, what's due, what needs a follow-up.
- **Per application:** the full Step 2 through Step 5 sequence happens once, when you commit.
## Cheats
`Cheats/` is where anything that actually worked gets written down — a tactic, a shortcut, a system, using [[Cheat Template]]. It grows only from real results, not speculation, and it is explicitly not being redesigned preemptively: the instruction behind this folder is to use it as-is until it produces a real blocker, then fix that blocker, not to polish it now.
## Deferred: Automated Discovery
The long-term goal is a 24/7 feed that watches the web for new postings and drops them into a Slack channel, which Claude then reads and turns into List rows automatically — using Firecrawl's monitor feature rather than a third-party platform, since Clay is enrichment (not discovery) and Hermes Agent needs a self-hosted always-on server for a single-purpose task. This is explicitly not built yet. The pipeline above works by hand first; automation gets wired into Step 1 once the manual version is proven.
## Frontmatter Quick Reference
| Note | Type | Lives in |
| --- | --- | --- |
| List monthly log | `input` | `10_Areas/Career/Internships/List/` |
| Program | (no `type` — reference data) | `10_Areas/Career/Internships/Programs/` |
| Contact | `contact` | `10_Areas/Career/Internships/Contacts/` |
| Cheat | `evergreen` | `10_Areas/Career/Internships/Cheats/` |
| Applying | `project` | `20_Progress/Internship/Applying/` |
| Interview prep | `project` or `input` | `20_Progress/Internship/Interviews/` |
| Tailored resume | (no `type` — working document) | `20_Progress/Internship/Resumes/Tailored/` |
| LinkedIn post | `output` | `20_Progress/Internship/Posts/` |
## Done When
- Every posting you'd regret forgetting has a List row.
- Every program you're actually pursuing has both a Programs note and an Applying note, cross-linked.
- No Applying note has gone more than a week without a Log entry while it's active.
- The Dashboard and the Kanban agree on what's currently in motion.
- The session log records any structural change to this pipeline.

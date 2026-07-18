---
type: project
status: active
created: 2026-07-16
updated: '"2026-07-17"'
deadline: null
related_progress: '["[[10_Areas/Career/Internships/Internships Hub]]",
  "[[30_Order/Workflows/Internship Pipeline]]", "[[Research Loop —
  Implementation Plan]]", "[[20_Progress/Internship/Building System/Phases 1-3
  Run]]"]'
tags:
  - internship
  - career
  - system-design
next: Promote the first real posting through the full pipeline end to end, then
  fix whatever breaks
---
# Internship System — Build Log
==This is the session record for designing and building the internship application system spanning `10_Areas/Career/Internships/` and `20_Progress/Internship/` on 2026-07-16.== The workflow doc ([[30_Order/Workflows/Internship Pipeline]]) is the lean operating procedure; this note is the full design rationale — why each decision landed where it did, what the research actually said, and what was built versus deferred.
## Goal
Build the full internship pipeline: company/employee research, HR/recruiter contacts, listings, application tracking, next steps, interview prep, pitches, cover letters, resume tailoring, LinkedIn/Handshake networking, and LinkedIn content from the portfolio blog. Split cleanly across `10_Areas` (reference, durable) and `20_Progress` (execution, live) rather than the single-tier setup that existed before this session.
## Starting State
Before this session: `10_Areas/Career/Internships/` had `Programs/` (one real note, HRT, with status fields baked into static research), `Tracker/` (a Dataview dashboard querying Programs' status field directly, plus an empty 4-lane Kanban), `Contacts/Mimic.md` (had the wrong "concept" template auto-applied — One-Line Answer/Mechanism/Flashcards structure meant for course concepts, not a message-template library), `Cheats/LinkedIn Premium.md` (one real cheat), and an empty `List/` folder. `20_Progress/Internship/` had legacy 2026-cycle notes (Career Fair, Companies OPT&CPT), an empty `AI Applying.md` stub, and two real interview-prep notes.
## Research Findings
### Tracking Funnel Structure
Real data (careery.pro): **Applied → Response (10-15%) → Phone Screen (50% of responses) → Final Interview (50% of screens) → Offer (30-50% of finals)**. About 100 cold applications produces 1-2 offers. A response rate under 10% signals a resume/targeting problem; responses without offers signal an interview-prep problem — this diagnostic split is why the pipeline needs live status broken out by stage, not a single "Applied" bucket. CS/tech students typically need 100-300+ applications; other fields need far fewer because networking substitutes for volume.
### Personal CRM Patterns
Tools reviewed (Dex, Clay, Orvo, folk) converge on the same fields: last-contact date, relationship tags, a structured note per real conversation, and reconnection nudges. The named failure mode, repeated across sources: spreadsheet/Notion-as-CRM has no reminders, so people "stop updating after week two." This is why the Contact note ([[Contact Template]]) keeps a Conversation Log inline rather than relying on a separate tracker nobody revisits.
### AI-Assisted Workflow Patterns
The cleanest framing found (careery.pro): automate the mechanical parts (form-fill, tracking, listing alerts — cuts 15-20 minutes per application to 2-5) and keep human judgment for role fit, resume customization, networking, and interview prep. Don't automate the differentiators. This directly shaped the decision to keep all outreach drafting as human-reviewed, never auto-sent (see [[Mimic]]).
### Resume/Cover Letter Tailoring
An empirical account (Kaizen Conroy) improved response rate from under 5% to 30%+ by adjusting the **top third** of the resume per role rather than rewriting the whole document, keeping 2-3 base variants, and putting tech stack inline next to each project rather than in a separate skills list. This is the direct source for [[Main Resume.md]]'s tagged-bullet-bank design and the Tailoring Checklist on it.
### LinkedIn "Maxing"
Gap in the research: none of the search results surfaced concrete blog-to-post tactics or posting cadence. The only adjacent finding was LinkedIn job-change alerts used as a CRM reconnection trigger, not a growth tactic. This is why `Posts/` was built as a thin scaffold rather than a designed system — there's nothing solid to design against yet.
### Cold Outreach and Anti-Patterns
Concrete cadence signals: respond to recruiter replies within 24 hours (interview slots fill in batches), apply within 48 hours of a posting (odds drop sharply after), send interview thank-yous within 24 hours referencing something specific. Anti-patterns: volume without diagnosis (more applications doesn't fix a broken funnel — find which stage is actually broken first), referrals aren't automatically better (one account: 3 referred applications, zero interviews), ghost jobs and stale postings waste effort, and over-automated outreach on LinkedIn carries real platform risk (documented account restrictions from automated activity).
### Research Automation Platforms (Hermes / Clay / Firecrawl)
**Hermes Agent** (Nous Research) is a real, MIT-licensed, self-hosted autonomous agent with persistent cross-session memory and native Slack/Telegram/Discord integrations — a genuine conceptual fit, but it needs an always-on server, which is real ops overhead for one task. **Clay** is *enrichment*, not *discovery* — it fills in data on a list you already have; it does not sit and watch the web for new postings appearing, and its free tier (100 credits/month) is too thin for continuous polling anyway. **Firecrawl's own web-scale monitor** (already available in this vault as a skill) can watch search queries across the whole web for new matching content and push to a webhook, with a built-in AI judge filtering noise — this is the strongest free fit since it needs no new platform.
> [!NOTE]
> Recommended future architecture: Firecrawl monitor (Step 1, discovery) → Slack webhook → Claude reads the channel periodically and structures confirmed leads into `List/` (Step 2). Clay's free tier is reserved for occasional on-demand contact enrichment of companies that already cleared discovery, not continuous polling. This is documented as deferred — see Decisions below.
## Decisions Made
### Round 1
- **Status ownership:** split. `Programs/` (10_Areas) holds only static research; a paired note per program in `Applying/` (20_Progress) holds live status. Reason given: matches the vault's own Areas/Progress split — a "durable" file that gets rewritten every week to update a status field defeats the purpose of Areas.
- **List vs Programs:** List is the firehose (every posting found, low effort), Programs is committed (only created once you decide to seriously pursue something). A List row is promoted, not automatically mirrored.
- **Contact drafts:** live inline in the Contact note itself, under a Current Draft section, built from `Mimic.md` templates. One file per person, not two.
- **"Hermes":** clarified as Nous Research's Hermes Agent, evaluated above — not adopted this session, folded into the deferred-automation note in the workflow doc.
### Round 2
- **Automation timing:** build the folder structure first; wire the Firecrawl-monitor-to-Slack pipeline in later, once the manual system is proven.
- **Resume system:** everything lives in `20_Progress/Internship/Resumes/` — no separate 10_Areas resume hub. `Main Resume.pdf` was already placed by the user before this session; `Main Resume.md` (the editable bullet bank) was built from reading that PDF.
- **LinkedIn scope:** scoped under Internships for now (`20_Progress/Internship/Posts/`), not a broader personal-brand system.
- **System scope:** generic pipeline, internships as current focus — frontmatter uses `role_type` and keeps `program_type`/`wave` optional rather than internship-hardcoded, so the same structure carries a full-time job search later without renaming folders.
### From the follow-up message (List/Tracker/Workflow/Build-Log specifics)
- List folder holds monthly capture logs (`YYYY-MM Found.md`), one table row per posting — link, requirements, one line on what it is. Confirmed as the pattern, not one file per posting.
- `Tracker/Tracker.md` (the 4-lane Kanban) is kept, not retired — it's a second, faster glance view alongside the detailed Dataview dashboard, not redundant with it. Cards link to real Applying notes.
- `30_Order/Workflows/Internship Pipeline.md` covers the full flow end to end, including how it's actually run (cadence, the deferred automation note).
- This note exists specifically to hold more implementation detail and research rationale than the workflow doc carries.
## What Was Built This Session
### New folders and files
- `10_Areas/Career/Internships/Internships Hub.md` — canonical domain hub (the vault had none for Career before this)
- `10_Areas/Career/Internships/List/2026-07 Found.md` — first monthly capture log
- `10_Areas/Career/Internships/README.md` — rewritten from the stale 2027-cycle setup guide
- `30_Order/Templates/Career/` — six new templates: List Monthly Log, Program, Contact, Applying, Cheat, LinkedIn Post
- `30_Order/Workflows/Internship Pipeline.md` — the operating procedure, added to `00_Workflows Index.md`
- `20_Progress/Internship/Applying/_This Week.md` — the weekly-curated queue
- `20_Progress/Internship/Applying/2026-HRT-Sophomore.md` — worked example of the live-status pattern
- `20_Progress/Internship/Resumes/Main Resume.md` — bullet bank built from reading `Main Resume.pdf`
- `20_Progress/Internship/Posts/README.md` — thin scaffold, no content yet
### Edited in place
- `10_Areas/Career/Internships/Programs/2026-HRT-Sophomore.md` — stripped status/date/interview/offer fields, added `list_origin` and `applying_note` links
- `10_Areas/Career/Internships/Programs/Programs-to-Create.md` — flagged as superseded YAML (still has old status fields, meant as a fact source now, not a literal template)
- `10_Areas/Career/Internships/Contacts/Mimic.md` — rebuilt entirely; was the wrong concept-note template, now a scenario-based message library (cold DM, recruiter follow-up, referral ask, thank-you, cross-link to the LinkedIn Premium cheat)
- `10_Areas/Career/Internships/Tracker/Internship - Dashboard.md` — rewritten queries, split into Research (Programs) and Pipeline (Applying) sections since plain Dataview can't cleanly join two folders into one row
- `10_Areas/Career/Internships/Tracker/Tracker.md` — populated the Interesting lane with the HRT program card
- `20_Progress/Internship/Applying/AI Applying.md` — repurposed as a pointer to `_This Week.md` rather than deleted (kept for link continuity)
## Note-Pattern Reference
### List Monthly Log
`type: input`, `input_kind: listing`. One file per month. Table columns: Company, Role, Link, Found, Requirements, What It Is, Promoted. A row's Promoted column becomes a wikilink once it graduates to a Program.
### Program
No `type:` field (pure structured reference data). Frontmatter: `name`, `company`, `program_type`, `eligible_classes`, `grad_year`, `role_type` (generic-scope field), `wave`, `opens_date`, `deadline_posted`, `deadline_real`, `pay_per_week`, `pay_currency`, `duration_weeks`, `benefits`, `application_url`, `careers_page`, `list_origin`, `applying_note`, `recruiter_contact`, `tags`. Body: Program Overview, Eligibility, Traps & Gotchas, Prep Checklist, Related Resources. No status field — that lives on the paired Applying note.
### Contact
`type: contact`. Frontmatter: `name`, `role`, `company`, `linkedin_url`, `email`, `how_found`, `relationship` (cold/warm/referral/alumni), `related_programs`, `last_contact_date`, `next`. Body: Facts, Current Draft, Conversation Log, Next Action.
### Applying
`type: project` (matches `20_Progress` convention, uses [[Project Standard]]). Frontmatter: `status` (Researching/Applied/OA/Phone Screen/Onsite/Offer/Rejected/Withdrawn), `program` (link back to the Program note), `company`, `date_applied`, `date_response`, `next_deadline`, `resume_version`, `cover_letter`, `contacts`, `interview_note`, `next`. Body: Goal, Current State, Next Action, Open Questions, Log — the standard Project Standard shape.
### Cheat
`type: evergreen`. No fixed body structure beyond What It Is, Why It Works, How To Use It, Failure Modes, Evidence — grows one note at a time from proven results, deliberately not over-designed.
### Interview Prep
Organic pattern already established by `ABB Interview Prep.md` — no new template forced onto it; new interview notes should follow that existing example (Job Description Analysis, Elevator Pitch, Talking Points, Questions to be Prepared for, Questions to Ask) rather than a generic template.
## Explicitly Deferred
- Firecrawl-monitor-to-Slack automated discovery pipeline — architecture recommended above, not built.
- Migrating legacy `Career Fair '25 & '26.md` and `Companies giving OPT & CPT.md` into List/Programs/Contacts — kept as historical mining material, not restructured.
- Cleaning every YAML block in `Programs-to-Create.md` individually — only the file-level banner was added; each block still needs its status fields stripped when actually turned into a real Program note.
- A broader LinkedIn personal-brand content system beyond internship-scoped posts.
- Actual tailored resume/cover-letter files in `Resumes/Tailored/` — no application has been made yet, so none exist.
## Open Questions
- [ ] When the HRT portal opens (Aug 1, 2026), run the full pipeline end to end on it and note anywhere the design breaks
- [ ] Decide whether `recruiter_contact`/`phone`/`email` fields still on Program notes should be replaced with a link to a real Contacts note once one exists for that program
- [ ] Revisit the Firecrawl-monitor-to-Slack automation once the manual pipeline has been used for at least one full application cycle
## Log
- **2026-07-16:** Two rounds of research (tracking/CRM/AI-workflow patterns, then Hermes/Clay/Firecrawl-monitor comparison), two rounds of clarifying questions, then built the full structure described above.
- **2026-07-16 (same day, follow-up):** Class-year correction (rising junior, not sophomore) — withdrew the HRT Applying worked example as no longer eligible. Found and fixed a real exposure gap: the vault's `Jarvis` GitHub repo is public with an auto-commit-and-push cycle; added `.gitignore` rules for `Resumes/` and `Contacts/` (except `Mimic.md`) and untracked the already-committed `Main Resume.pdf`. Verified the SimplifyJobs/Jose-Gael-Cruz-Lopez/zapplyjobs repos in detail against the corrected profile and wrote the full automation spec — see [[Research Loop — Implementation Plan]].
- **2026-07-17:** Phases 1-3 of the research loop automation completed and verified live against the real `gupta-builds/Jarvis` repo — 137 dossiers written, dedup confirmed idempotent across repeated runs, hourly cron confirmed actually firing. Full build record across all three phases: [[20_Progress/Internship/Building System/Phases 1-3 Run]].
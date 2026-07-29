---
type: evergreen
status: sprout
created: 2026-07-29
updated: 2026-07-29
tags:
  - cheat
  - internship
notes:
  - "[[Internship Pipeline]]"
  - "[[60_Claude/10_Source_Summaries/PDF Ingestion/MavGPT AI Resume & Job Search Guide (PDF)]]"
  - "[[60_Claude/10_Source_Summaries/PDF Ingestion/Read/LinkedIn Search URL Cheatsheet (PDF)]]"
  - "[[60_Claude/10_Source_Summaries/PDF Ingestion/Read/Outreach Automation Manual (PDF)]]"
next:
---
# Resume Tailoring, LinkedIn Search & Outreach Discovery
## What It Is
==Three PDF-sourced tactics, each slotting into an existing [[Internship Pipeline]] step rather than becoming a new system: a five-prompt resume-tailoring sequence for Step 5, a set of LinkedIn manual-search operators for Step 1's manual-find path and Step 4's recruiter discovery, and a discovery-tool-only verdict on Apollo/Hunter for Step 4.== [[00_Execution]] resolved all three from [[PDF's Ingestion Implementation#CAREER TRACK: Integrated Resume + Job Search + Portfolio Strategy|CAREER TRACK Parts 2-4]] against the real pipeline already in use — none of them are new builds.
## Why It Works
ATS filters and cold outreach both reward the same thing: language that matches what the reader (robot or recruiter) is already scanning for. Tailoring the top-third of a resume per JD and using specific LinkedIn search operators both exploit "match the exact term the filter/search index is looking for" — not a hack, just precise keyword targeting instead of a generic document.
## How To Use It
### Part 1 — MavGPT Five-Prompt Sequence (run at Step 5 — Tailor)
Per [[Internship Pipeline#Step 5 — Tailor (Resumes)|Step 5]]: every `Resumes/Altered/<company>.md` gets built from `Resumes/Main Resume.md` by pulling the 3-5 bullets that best match the JD, in this literal prompt order:
1. **1A — Extract keywords from JD** (5 min): paste the job description, ask "extract every skill, tool, and qualification keyword from this JD, ranked by how many times each concept recurs."
2. **1B — Match your skills to the JD** (5 min): paste `Main Resume.md` + the 1A keyword list, ask "which of my bullets already cover these keywords, and which keywords have no bullet at all?" — this is the gap list.
3. **2A — Rewrite Experience bullets** (10 min): for each gap or weak match, ask "rewrite this bullet using the JD's own terminology, keep the real numbers, don't invent metrics."
4. **2B — Rewrite Skills section** (5 min): ask "reorder my skills section to lead with this JD's top requirements, in the JD's own naming."
5. **3A — Write cover letter** (15 min, optional per application): ask "write a cover letter using these 3 tailored bullets plus one sentence connecting to the company's actual product."
6. **4A — Pre-submission audit** (10 min): paste the final tailored resume + JD, ask "does this read as both ATS-parseable and human-readable? Flag anything that looks keyword-stuffed."
Link the finished file back to the Applying note's `resume_version` field per Step 7.
### Part 2 — LinkedIn Search Operators (manual only — Step 1 manual-find, Step 4 recruiter discovery)
**Confirmed:** `internship-research-loop` has no LinkedIn source among its eight automated feeds (blocked by login walls — see [[10_Areas/Career/Internships/Contacts/Outreach Discovery & Automation Status]]). These operators apply only to searches you run by hand.
- `f_E=1` — entry-level jobs only: `/jobs/search/?keywords=intern&f_E=1`
- `keywords=` — free-text search term, combine with anything below
- `currentCompany=[ID]` — scope any search to one company (get the numeric ID from the company's LinkedIn URL)
- `/search/results/people/?keywords=campus recruiter` (or `university relations`, `talent acquisition`, `early careers`) — recruiter discovery by role keyword, not by job title search
**Partially verified — test before relying on these, LinkedIn changes filters without notice:**
- `f_TPR=r86400` — last 24 hours
- `f_WT=2` — remote work
- `f_AL=true` — Easy Apply
**Workflow:** run 3-5 searches/week for your target path + location, log finds in this month's List log per Step 1, and for recruiter hits: connect + a one-line message referencing something specific about their team, then follow up in Contacts if no response in 7-10 days per [[Internship Pipeline#Step 4 — Reach Out (Contacts)|Step 4]].
### Part 3 — Outreach Discovery Tool Verdict (Step 4 only)
Full comparison and current status: [[10_Areas/Career/Internships/Contacts/Outreach Discovery & Automation Status]]. One-line version: Apollo/Hunter only replace *finding* a contact's name and email (85-90% accuracy vs. ad-hoc manual search) — every message stays single-recipient, hand-written, and edited in `Contacts/Mimic.md`'s style, exactly as Step 4 already works. No multi-touch auto-sequences, no bulk generation.
## Failure Modes
> [!WARNING]
> Running 1A-4A on a resume that hasn't been updated with real recent work just produces a better-phrased version of stale content. The prompts tailor language; they don't invent qualifications. If 1B's gap list is long, that's a signal to go build something, not to keep rewriting bullets.
> [!WARNING]
> LinkedIn's filter parameters (`f_TPR`, `f_WT`, `f_AL`) are undocumented and drift — verify each one still filters correctly before trusting a search result count. A silently-broken filter returns unfiltered results with no error.
> [!WARNING]
> The instant a discovery tool's output gets treated as a template to blast at scale, response rate collapses — this is the exact failure mode [[10_Areas/Career/Internships/Contacts/Outreach Discovery & Automation Status]] flags as the one thing not to carry over from the Outreach Automation Manual's plan.
## Evidence
- [[Internship Pipeline]] — Steps 1, 4, and 5, the real system these tactics slot into
- [[10_Areas/Career/Internships/Contacts/Outreach Discovery & Automation Status]] — full Apollo/Hunter verdict + automation-channel status
- [[60_Claude/10_Source_Summaries/PDF Ingestion/MavGPT AI Resume & Job Search Guide (PDF)]]
- [[60_Claude/10_Source_Summaries/PDF Ingestion/Read/LinkedIn Search URL Cheatsheet (PDF)]]
- [[60_Claude/10_Source_Summaries/PDF Ingestion/Read/Outreach Automation Manual (PDF)]]
- [[00_Execution]] — the resolved verdicts this note executes

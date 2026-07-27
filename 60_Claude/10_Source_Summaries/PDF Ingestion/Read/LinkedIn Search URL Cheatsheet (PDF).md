---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[Tracker]]"
  - "[[LinkedIn Premium]]"
source_url: 60_Claude/05_Clippings/PDFs/Linkedin Searches.pdf
source_note: "[[60_Claude/05_Clippings/PDFs/Linkedin Searches.pdf]]"
input_kind: pdf
track: career
---
# LinkedIn Search URL Cheatsheet — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Linkedin Searches.pdf`
**Ingested:** 2026-07-04
**Pages:** 5
## Source
A cheatsheet of ~40 ready-made LinkedIn search-URL patterns for finding internships, recruiters, hiring managers, and alumni — paste-and-go query strings you append to `linkedin.com`.
## Key Claims
- ==The internship filter is `f_E=1` (entry-level); the last-24-hours filter is `f_TPR=r86400`; remote is `f_WT=2`; Easy Apply is `f_AL=true`== — combine them for targeted feeds
- Recruiter discovery works better by *role keyword* than by "recruiter": `campus recruiter`, `university relations`, `early careers`, `talent acquisition`, `people operations` (HR without "HR"), plus non-HR hiring managers (`engineering manager`, `team lead`, `founder`)
- Alumni are the highest-conversion lane: college page → Alumni → filter by role; `former intern`, `recent graduate`, and "joined in past 1 year" people are the best referral targets
## Full Content — the URL patterns
**Jobs (append to linkedin.com):**
- `/jobs/search/?keywords=intern&f_E=1` — internship-only feed
- `+&f_TPR=r86400` (last 24h) · `+&f_WT=2` (remote) · `+&f_AL=true` (Easy Apply)
- keyword swaps: `software%20intern`, `data%20intern`, `design%20intern`, `marketing%20intern`, `paid%20intern`, `intern%20startup`, `intern%20global`
- `/jobs/search/?f_E=2` (entry-level jobs) · `keywords=fresher` / `graduate` / `apprenticeship`
**People (recruiters / hiring managers):**
- `/search/results/people/?keywords=recruiter` (or `campus%20recruiter`, `early%20careers`, `university%20relations`, `talent%20acquisition`, `internship%20program`)
- `keywords=hiring%20manager` / `engineering%20manager` / `team%20lead` / `founder` / `people%20operations`
- at a specific company: `?currentCompany=[COMPANY_ID]&keywords=recruiter` (or `campus` / `manager`)
- sort by "Recent activity" to find *active* recruiters
**Alumni / network:**
- college page → Alumni → filter by role; `keywords=alumni%20recruiter`; `keywords=alumni&currentCompany=[COMPANY_ID]`; `former%20intern`; `recent%20graduate`; filter "Past 1 year" for warm referral targets
## Why It Matters
Directly operational for the weekly internship-outreach cadence feeding [[Tracker]] — these URL patterns turn LinkedIn from browse-mode into targeted queries, and pair with [[LinkedIn Premium]] (already in the Career folder) and the [[Outreach Automation Manual (PDF)]] pipeline (which finds the same recruiters programmatically). The highest-leverage move the sheet encodes: **target recruiters by specific role keyword and alumni by "joined past year," not by searching "recruiter"** — matches the AI/ML pivot guide's "get referred, not filtered" (5–10× conversion). Low-effort, high-use reference.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Linkedin Searches.pdf`
- [[Tracker]] — internship pipeline these searches feed
- [[LinkedIn Premium]] — the account tooling
- [[Outreach Automation Manual (PDF)]] — the automated version of finding these recruiters
## Open Questions
- [ ] Save the 4–5 most-used query strings (software intern last-24h remote; campus recruiters at target companies) as a quick-reference in the Career folder?
## Flashcards
#cards/career
What LinkedIn URL filter finds entry-level internships posted in the last 24 hours?::`/jobs/search/?keywords=intern&f_E=1&f_TPR=r86400` — `f_E=1` = entry-level, `f_TPR=r86400` = past 24 hours (add `f_WT=2` for remote, `f_AL=true` for Easy Apply).
Why search recruiters by specific role keyword instead of "recruiter"?::"Recruiter" misses the people who actually own early-career hiring — search `campus recruiter`, `university relations`, `early careers`, `talent acquisition`, `people operations`, and non-HR `engineering manager`/`founder` instead.

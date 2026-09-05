---
type: reference
status: active
created: 2025-10-30
updated: 2026-07-18
related_progress:
  - "[[Phases Run]]"
  - "[[Internship Pipeline]]"
tags:
  - internship
  - opt
  - reference
next:
---
# OPT/CPT Eligibility Registry
==Rebuilt 2026-07-18 — the previous content (an October 2025 postings brainstorm) had no OPT/CPT information despite the filename; it was rebuilt per the Phase 6 decision, with the old Applied history preserved at the bottom.== This is the human-readable registry of OPT-eligibility verdicts for postings the research loop has checked. The machine cache the pipeline actually consults is `state/opt_cache.json` in `gupta-builds/internship-research-loop` — one verdict per posting uid, written automatically at discovery time.
## The Semantics (from the Phase 6 decision)
- **OPT is work authorization the F-1 student already holds** — it is not H-1B sponsorship. "No visa sponsorship" usually means no H-1B and is **not** an exclusion.
- **Exclude only on an explicit negative signal:** a US-citizenship/US-person requirement, a security-clearance requirement, or an explicit "OPT/CPT not accepted" statement.
- **Checked per posting, not per company** — verified 2026-07-18: Palantir's US Government internship and its Commercial internship differ on exactly this axis within one company.
- A conditional "willingness to undergo a background investigation" (Palantir US Gov) is **not** a clearance requirement and does not exclude.
## Verdicts From The 2026-07-18 Dossier Audit
Every verdict below cites text actually read on the live posting page that day.
| Company / Role | Verdict | Evidence |
| --- | --- | --- |
| **Anduril** — Software Engineer Intern | **Excluded** | "U.S. Person status is required as this position needs to access export controlled data." — stated qualification in the JD |
| **Palantir** — FDSE Internship, US Government (Honolulu) | Eligible on OPT (removed for grad-year instead) | Only screen: "Willingness to undergo a US government background investigation, depending on US government project requirements" — conditional, not a clearance/citizenship requirement. Removed because "Must be planning on graduating in 2027" fails the Spring-2028 profile |
| **Palantir** — Privacy & Civil Liberties SWE (NYC) | Eligible on OPT (removed for grad-year) | Same graduating-in-2027 requirement |
| **Palantir** — FDSE Intern, Commercial (Chicago) | **Eligible** | "Must be graduating in December 2027 or Spring 2028" — fits profile; no citizenship/clearance text |
| **CTGT** — SWE Intern (SF) | **Eligible** | Posting states "Will Sponsor" |
| **Aquatic Capital** — SWE Intern (Chicago) | **Eligible** | Sponsorship asked as a question on the application, not excluded |
| RTX, Northrop Grumman | Not re-checked | Already deleted before this audit (RTX was Canada-located; neither is in the current dossier set) |
| 16 other survivors (SIG, Five Rings, Trade Desk, Walleye ×2, Ellipsis, Marshall Wace NYC, Grant Thornton, Marmon, IMC, Circleback, HRT, Optiver ×2, Pylon, SimonComputing, UNCF) | **Eligible** | No citizenship/clearance/no-OPT text found on any of their live posting pages (EEO "citizenship status" boilerplate deliberately not counted) |
## How New Verdicts Arrive
The hourly discovery loop fetches every new validated match's posting page once (Firecrawl), greps it for the exclusion signals above (`ingestion/posting_page.py`, `OPT_EXCLUSION_RE`), rejects on an explicit signal (logged as `opt_eligibility` in the run log), and caches the verdict by uid so a rejected posting is never re-fetched. Fail-open: if the page can't be fetched, the posting is treated as eligible and written with a thin dossier.
## Legacy: Applied (from the pre-rebuild note, Oct 2025 era)
1. A few NVIDIA interns that never replied: [the hub](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/userHome)
2. [Intuit](https://jobs.intuit.com/job/mountain-view/summer-2026-front-end-engineering-intern/27595/87369447104?cid=directBookmarked_directBookmarked) — also reached out to the recruiter on LinkedIn

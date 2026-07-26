---
type: project
status: active
created: 2026-07-26
updated: 2026-07-26
related_progress:
  - "[[Source of Truth]]"
  - "[[10_Areas/Career/Internships/List/Resources]]"
tags:
  - internship
  - automation
  - resources
next: "Commit and push freehire.py + fetch_ai_jobs (built, tested, uncommitted) — see System - Build Log 2026-07-25."
---
# Research Loop — Resources
==The main list of every data source this loop uses or has evaluated, what each one actually provides, and the planned alternative once a source runs dry or breaks.== This is the planning-level note — what exists, what's next in line. `10_Areas/Career/Internships/List/Resources` is the operational companion: how much has actually been drawn from each source and live exhaustion signals.
## Live, Committed, Firing In Production (2026-07-25)
| Source | Shape | What it gives us | Verified scale |
| --- | --- | --- | --- |
| SimplifyJobs (`Summer2026-Internships`) | `listings.json` | The original, largest curated internship list | 14,900+ entries |
| Jose-Gael-Cruz-Lopez (`underclassmen-opportunities`) | `listings.json` | Smaller, underclassmen-focused | ~112 entries |
| `vanshb03/Summer2027-Internships` | `listings.json` (bare `season`, no `category`) | Independent curation, caught Uber + Deepgram | 274 entries |
| `zshah101/...Tech-Internships` | `data/jobs.json` (dict-keyed) | First-party `sponsorship` field — cleaner OPT signal than any other source | 214 entries |
| Greenhouse (direct API) | `boards-api.greenhouse.io` | No scraping — structured JSON, full JD text | 7 verified-live company tokens |
| Ashby (direct API) | `api.ashbyhq.com` | Same — structured, no scraping | 5 verified-live company tokens |
> [!NOTE]
> Token verification standard, non-negotiable: never add a Greenhouse/Ashby token that hasn't been confirmed live against real job data first — a wrong guess silently returns zero jobs, not an error. See `ingestion/sources.py`'s comment above `GREENHOUSE_COMPANIES` for the exact check.
## Built, Tested, Not Yet Committed (2026-07-25/26)
- **`freehire` (`strelov1/freehire`)** — MIT-licensed, 4,270,639 postings indexed, 187,542 companies, 78 ATS platforms. Its "Company career sites" crawl reaches **Uber and Google directly** (562 and 3,484 open postings) — the exact companies Phase 11's direct-ATS check confirmed unreachable through Greenhouse/Lever/Ashby. Also carries `enrichment.seniority`, `posted_at`/`closed_at`, repost/fake-freshness detection. `ingestion/freehire.py` exists (`fetch_freehire`, `normalize_freehire`, `lookup_company_on_freehire`), ground-truth verified (Google's and Nuro's real postings confirmed present), real test coverage. **Not pushed to GitHub.**
- **`artificialintelligencejobs.co`** — 320 companies, 17,507 jobs, 184 carrying an explicit `level: "Intern"` field. Company list skews AI-native (OpenAI, Anthropic, Mistral, a long tail of AI startups) — complementary to the finance/general-tech-heavy set the other six sources produce. `fetch_ai_jobs`/`normalize_ai_jobs` exist in `ingestion/sources.py`. **Not pushed to GitHub.**
## Researched, Deliberately Not Built
- **Lever** — one confirmed live example (Palantir), didn't justify a fifth ingestion module on its own. Revisit if a second real Lever-hosted target company shows up.
- **`speedyapply/2027-AI-College-Jobs`** — daily commits, but no accessible data file anywhere in the repo; the real data lives in a private Supabase backend, commits only re-render it into README tables. Same structural problem class as the already-removed zapplyjobs.
- **`sndsh404/summer-2027-internships`** — README + a binary `.xlsx` only, arguably worse than zapplyjobs.
- **Intern Dock** — a snapshot page, no API.
## Ruled Out
zapplyjobs (removed 2026-07-18 — entries are program/resource pages, not deadline-bearing postings). General job-board aggregators from `public-apis`' Jobs category (Adzuna, Careerjet, Jooble, Reed, ZipRecruiter) — same low-signal-for-internships problem as zapplyjobs, not internship-specific enough to be worth the integration.
## When A Source Runs Dry — The Alternative Ladder
1. **SimplifyJobs/JGCL feel thin** → the four newer sources (vanshb03, zshah101, Greenhouse, Ashby) already diversify past them; check `List/Resources` for which one specifically slowed.
2. **Greenhouse/Ashby seed list feels stale** → Task F from `Runs/Claude Code Prompts.md` Prompt 2 (seed-list diversification) is the direct next step — verified-live token additions only.
3. **All six existing sources feel exhausted** → freehire and artificialintelligencejobs.co are already built, just need committing — that's the very next lever, not a new research pass.
4. **Even freehire feels thin** → Lever gets built for real (needs a second confirmed target company first), then a genuinely new research pass against `public-apis`-style directories, same verification discipline as every source above (live-checked before any code is written).

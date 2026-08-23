---
type: project
status: active
created: 2026-07-26
updated: 2026-08-24
related_progress:
  - "[[Source of Truth]]"
  - "[[10_Areas/Career/Internships/List/Resources]]"
tags:
  - internship
  - automation
  - resources
next: "Named-Program Coverage Check re-run 2026-08-24 — next is checking Greenhouse/Ashby token coverage for the six still-uncovered companies (Citadel, LinkedIn, MLH, NASA, Capital One, Bloomberg)."
---
# Research Loop — Resources
==The main list of every data source this loop uses or has evaluated, what each one actually provides, and the planned alternative once a source runs dry or breaks.== This is the planning-level note — what exists, what's next in line. `10_Areas/Career/Internships/List/Resources` is the operational companion: how much has actually been drawn from each source and live exhaustion signals.
## Live, Committed, Firing In Production (confirmed 2026-07-26)
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
## Freehire and AIJobs — Moved To Live (2026-07-26)
- **`freehire` (`strelov1/freehire`)** — MIT-licensed, 4,270,639 postings indexed, 187,542 companies, 78 ATS platforms. Its "Company career sites" crawl reaches **Uber and Google directly** (562 and 3,484 open postings) — the exact companies Phase 11's direct-ATS check confirmed unreachable through Greenhouse/Lever/Ashby. Also carries `enrichment.seniority`, `posted_at`/`closed_at`, repost/fake-freshness detection. **Confirmed committed and pushed** (`Two new discovery sources: Freehire, AIJobs`, 2026-07-26) — `ingestion/freehire.py` live on `master`. Note: `recheck.py`'s `FEEDS` dict does not yet include Freehire — confirm whether that's a deliberate exclusion or a real gap.
- **`artificialintelligencejobs.co`** — 320 companies, 17,507 jobs, 184 carrying an explicit `level: "Intern"` field. Company list skews AI-native (OpenAI, Anthropic, Mistral, a long tail of AI startups) — complementary to the finance/general-tech-heavy set the other six sources produce. **Confirmed committed and pushed**, same commit as Freehire — `recheck.py`'s `FEEDS` dict already includes `AIJobs`.
## Researched, Deliberately Not Built
- **Lever** — one confirmed live example (Palantir), didn't justify a fifth ingestion module on its own. Revisit if a second real Lever-hosted target company shows up.
- **`speedyapply/2027-AI-College-Jobs`** — daily commits, but no accessible data file anywhere in the repo; the real data lives in a private Supabase backend, commits only re-render it into README tables. Same structural problem class as the already-removed zapplyjobs.
- **`sndsh404/summer-2027-internships`** — README + a binary `.xlsx` only, arguably worse than zapplyjobs.
- **Intern Dock** — a snapshot page, no API.
## Ruled Out
zapplyjobs (removed 2026-07-18 — entries are program/resource pages, not deadline-bearing postings). General job-board aggregators from `public-apis`' Jobs category (Adzuna, Careerjet, Jooble, Reed, ZipRecruiter) — same low-signal-for-internships problem as zapplyjobs, not internship-specific enough to be worth the integration.
## Named-Program Coverage Check (refreshed 2026-08-24) — Real Gap, Partly Closing
Per [[00_Execution]]'s Web pass, [[Internship Tracking Dashboard — 2027 Calendar, Programs, & Application Pipeline]] named ~11 target early-talent programs. Re-checked directly against `List/Dossiers/` (frontmatter `company:` field, excluding `Viewed/`, not just body-text mentions of the name — a JD that merely links to LinkedIn or namechecks Google isn't a real hit): **5 of 11 companies now have a dossier, up from 3 at the 2026-07-29 check — but still none confirmed to be the specific named program.**
| Company / Program | Dossier Coverage |
|---|---|
| Jane Street (FTTP) | 11 Jane Street dossiers exist (SWE, ML Engineer, ML Researcher, Hardware, Network, etc.) — unchanged since 2026-07-29; none confirmed as the specific FTTP program by name; likely generic postings, not the named pipeline |
| Two Sigma (First-Year) | 1 dossier now exists (`AI Research Scientist Intern - 2027 Summer - Two Sigma`) — **new since the 2026-07-29 check (was None)**; checked its body text for "First-Year," no mention found — generic posting, not confirmed as the named pipeline |
| D.E. Shaw | 1 dossier (`Software Developer Intern - DE Shaw`) — unchanged, still generic, not confirmed as a named early-talent pipeline |
| Citadel (Launch) | **None** |
| Google (ASDI) | 3 Google dossiers exist (unchanged) — all generic "Software Engineering Intern" postings, checked body text for "ASDI," no mention found |
| Microsoft (Explore) | 6 dossiers now exist — **new since the 2026-07-29 check (was None)**: AIML & LLM, CoreAI, Cloud & Distributed Backend, Fullstack Product, Data Platform/Analytics, Security & Identity. Checked body text for "Explore" on all six — the only hits are JS/UI config noise embedded in the fetched page (`explore opportunities`-style chrome), not the named program; still generic, unconfirmed |
| LinkedIn (First Play) | **None** |
| MLH Fellowship | **None** |
| NASA OSTEM | **None** |
| Capital One | **None live** — 2 dossiers existed as of the last check (Cyber Security Intern, Software Engineer Intern) but both closed upstream and moved to `Viewed/` on 2026-08-23 (`removed_reason: "active: false upstream"`) — real churn, not a coverage gain |
| Bloomberg | **None** |
**This is a loop-coverage gap, not a reason to hand-write Program notes for the missing six** — per [[00_Execution]], the retired `Programs-to-Create.md` pattern (hand-typing from a target list) doesn't come back just because the loop hasn't surfaced these yet. If any of these are genuinely time-sensitive (Wave 1 programs open Aug 1 per [[10_Areas/Career/Internships/Programs/Serious/2026-HRT-Sophomore]]'s own timing), the right fix is checking why the loop's sources aren't catching them by name — company-specific early-talent programs (First-Year, Launch, First Play, OSTEM) often post on dedicated early-careers subdomains that a general listings aggregator (SimplifyJobs, vanshb03, zshah101) may not crawl, and none of the sources are Greenhouse/Ashby-hosted for these specific companies (per the verified-token list above). Two Sigma and Microsoft now have generic-role coverage, which narrows the gap to "is this posting the named pipeline" rather than "does the company have any coverage at all" — worth re-checking body text again once the loop's per-source yield changes (see [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]]'s Prompt 14 entry, in progress as of 2026-08-24). **Next step, not yet done:** check whether any of the six still-uncovered companies' early-talent programs post through Greenhouse or Ashby (in which case a token addition closes the gap directly) before assuming a ninth source is needed.
## When A Source Runs Dry — The Alternative Ladder
1. **SimplifyJobs/JGCL feel thin** → the four newer sources (vanshb03, zshah101, Greenhouse, Ashby) already diversify past them; check `List/Resources` for which one specifically slowed.
2. **Greenhouse/Ashby seed list feels stale** → Task F from `Runs/Claude Code Prompts.md` Prompt 2 (seed-list diversification) is the direct next step — verified-live token additions only.
3. **All eight existing sources feel exhausted** → Lever gets built for real (needs a second confirmed target company first).
4. **Even that feels thin** → a genuinely new research pass against `public-apis`-style directories, same verification discipline as every source above (live-checked before any code is written).

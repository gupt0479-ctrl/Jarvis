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
next: "Lever shipped live 2026-08-24 (nine sources now); InternDock built but not wired; Greenhouse/Ashby/Lever token coverage for the six still-uncovered named-program companies is confirmed a dead end, not an open question. Next: Prompt 17 (InternDock SOURCES wiring, evaluate ApplyGuy/dreamworkhq), not yet run."
---
# Research Loop — Resources
==The main list of every data source this loop uses or has evaluated, what each one actually provides, and the planned alternative once a source runs dry or breaks.== This is the planning-level note — what exists, what's next in line. `10_Areas/Career/Internships/List/Resources` is the operational companion: how much has actually been drawn from each source and live exhaustion signals.
## Live, Committed, Firing In Production (confirmed 2026-07-26; Lever added 2026-08-24)
| Source | Shape | What it gives us | Verified scale |
| --- | --- | --- | --- |
| SimplifyJobs (`Summer2026-Internships`) | `listings.json` | The original, largest curated internship list | 14,900+ entries |
| Jose-Gael-Cruz-Lopez (`underclassmen-opportunities`) | `listings.json` | Smaller, underclassmen-focused | ~112 entries |
| `vanshb03/Summer2027-Internships` | `listings.json` (bare `season`, no `category`) | Independent curation, caught Uber + Deepgram | 274 entries |
| `zshah101/...Tech-Internships` | `data/jobs.json` (dict-keyed) | First-party `sponsorship` field — cleaner OPT signal than any other source | 214 entries |
| Greenhouse (direct API) | `boards-api.greenhouse.io` | No scraping — structured JSON, full JD text | 7 verified-live company tokens |
| Ashby (direct API) | `api.ashbyhq.com` | Same — structured, no scraping | 5 verified-live company tokens |
| Lever (direct API) | `api.lever.co` (per-company token polling) | Same pattern as Greenhouse/Ashby — no scraping, structured JD text | 2 verified-live company tokens (Palantir, Belvedere Trading) — 61 postings fetched, 3 real matches **as of the 2026-08-24 build**; expect this to drift, cite the date when quoting it |
> [!NOTE]
> Token verification standard, non-negotiable: never add a Greenhouse/Ashby/Lever token that hasn't been confirmed live against real job data first — a wrong guess silently returns zero jobs, not an error. See `ingestion/sources.py`'s comment above `GREENHOUSE_COMPANIES` for the exact check.
> [!NOTE]
> **Jose-Gael-Cruz-Lopez's zero-live-dossier question, resolved 2026-08-24.** Not degradation, not a bug. Its entire currently-matching pool is three non-software scholarship/fellowship postings (MLH Fellowship, White House HBCU Scholars Program, UNCF Scholarships Portal) — correctly deleted by a human during the 2026-08-23 dossier-audit session and now sitting in `seen_ids.json`, which by design never re-offers them. Two more (TMCF, AAUW) already hit `MAX_DEBATE_LOSSES` and sit in `excluded_uids.json`. The feed itself just skews thin toward non-CS content for this persona — nothing to fix in code.
## Freehire and AIJobs — Moved To Live (2026-07-26)
- **`freehire` (`strelov1/freehire`)** — MIT-licensed, 4,270,639 postings indexed, 187,542 companies, 78 ATS platforms. Its "Company career sites" crawl reaches **Uber and Google directly** (562 and 3,484 open postings) — the exact companies Phase 11's direct-ATS check confirmed unreachable through Greenhouse/Lever/Ashby. Also carries `enrichment.seniority`, `posted_at`/`closed_at`, repost/fake-freshness detection. **Confirmed committed and pushed** (`Two new discovery sources: Freehire, AIJobs`, 2026-07-26) — `ingestion/freehire.py` live on `master`. Note: `recheck.py`'s `FEEDS` dict does not yet include Freehire — confirm whether that's a deliberate exclusion or a real gap.
- **`artificialintelligencejobs.co`** — 320 companies, 17,507 jobs, 184 carrying an explicit `level: "Intern"` field. Company list skews AI-native (OpenAI, Anthropic, Mistral, a long tail of AI startups) — complementary to the finance/general-tech-heavy set the other six sources produce. **Confirmed committed and pushed**, same commit as Freehire — `recheck.py`'s `FEEDS` dict already includes `AIJobs`.
## InternDock — Built, Not Yet Wired (2026-08-24)
A real third state this doc didn't have a category for until now — neither "live" nor "deliberately not built." `interndock.com/sitemap.xml` confirmed 2026-08-24 as a real, live, ongoing index (more drop-shaped slugs found than the two original URLs the human provided — not a one-time snapshot). `ingestion/interndock.py` built: sitemap-based candidate detection plus a posting parser written from real verbatim fetched text (the visible link text is always literally "Apply," not the title — the originally guessed format was wrong), 6 tests, all passing. **Explicitly not wired into `SOURCES` yet** — the build deliberately stopped short of that, flagging three real open design questions rather than guessing at them: an identity/uid strategy (postings carry no native id the way Greenhouse/Ashby/Lever do), a polling cadence (a single drop is ~650-658 postings, real known drops roughly 6 weeks apart — not hourly-shaped like the JSON-feed sources), and confirming the existing per-bucket write budget handles a drop that large gracefully. Queued as Prompt 17 Task 1, not yet run — don't describe InternDock as a live source until that wiring ships.
## Researched, Deliberately Not Built
- **`speedyapply/2027-AI-College-Jobs`** — daily commits, but no accessible data file anywhere in the repo; the real data lives in a private Supabase backend, commits only re-render it into README tables. Same structural problem class as the already-removed zapplyjobs. Re-verified 2026-08-24, unchanged.
- **`sndsh404/summer-2027-internships`** — README + a binary `.xlsx` only, arguably worse than zapplyjobs. Re-verified 2026-08-24, unchanged.
## Found, Not Yet Evaluated For Build (2026-08-24)
Surfaced by Prompt 14 v2's repo sweep — real, structured, confirmed via direct check, but neither built nor evaluated against this codebase's usual "is it worth a fifth/sixth module" bar yet. That evaluation is Prompt 17, Tasks 2-3, not yet run.
- **`ApplyGuy/2027-Internships`** — real JSON confirmed (example seen: "Toyota of Cedar Park Keating LLC — Software Developer Intern," posted same-day). Schema completeness, real scale, and update frequency not yet verified fresh.
- **`dreamworkhq/Tech-Internships-2027`** — real JSON confirmed, 720 entries at last check, a richer schema than most existing sources (`salaryMin`/`salaryMax`/`aiRoleKind`/`postedAt`/`firstIndexedAt`), example seen: Fannie Mae "Data Science Intern." Whether the richer fields are worth integrating even partially is an open question for that evaluation.
## Ruled Out
zapplyjobs (removed 2026-07-18 — entries are program/resource pages, not deadline-bearing postings). General job-board aggregators from `public-apis`' Jobs category (Adzuna, Careerjet, Jooble, Reed, ZipRecruiter) — same low-signal-for-internships problem as zapplyjobs, not internship-specific enough to be worth the integration. `SuryaHarikrishnan/2027-internship-tracker` (13,180 entries, found and evaluated 2026-08-24) — 100% re-aggregated from already-integrated SimplifyJobs/vanshb03 data, zero unique value, correctly skipped.
## Named-Program Coverage Check (refreshed 2026-08-24) — Coverage Gap Remains, Connector Question Now Closed
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
**This is a loop-coverage gap, not a reason to hand-write Program notes for the missing six** — per [[00_Execution]], the retired `Programs-to-Create.md` pattern (hand-typing from a target list) doesn't come back just because the loop hasn't surfaced these yet. Two Sigma and Microsoft now have generic-role coverage, which narrows their gap to "is this posting the named pipeline" rather than "does the company have any coverage at all."
**The open question this section posed since 2026-07-29 — "check whether these companies post through Greenhouse or Ashby before assuming a ninth source is needed" — is now answered, not still open.** Prompt 14 v2 (2026-08-24, Task 6) checked directly, not theorized: LinkedIn's Greenhouse board is real but carries zero intern postings anywhere in it (not a detection failure — genuinely nothing there). None of Two Sigma, Citadel, Capital One, Bloomberg, Microsoft, NASA, or MLH have a reachable Greenhouse/Ashby/Lever token — confirmed via direct API probes. All seven are almost certainly on Workday-class ATSes this pipeline has no connector for. A token addition will not close this gap for any of these seven; closing it for real would mean building a Workday connector, which is not currently planned or scoped anywhere in this system. The six still-uncovered companies (Citadel, LinkedIn, MLH, NASA, Capital One, Bloomberg) stay uncovered by design limitation, not by an unchecked assumption.
## When A Source Runs Dry — The Alternative Ladder
1. **SimplifyJobs/JGCL feel thin** → the four newer sources (vanshb03, zshah101, Greenhouse, Ashby) already diversify past them; check `List/Resources` for which one specifically slowed.
2. **Greenhouse/Ashby seed list feels stale** → Task F from `Runs/Claude Code Prompts.md` Prompt 2 (seed-list diversification) is the direct next step — verified-live token additions only.
3. **All nine existing sources feel exhausted** → InternDock's `SOURCES` wiring (Prompt 17 Task 1) or evaluating ApplyGuy/dreamworkhq (Prompt 17 Tasks 2-3) are the direct next steps, both not yet run.
4. **Even that feels thin** → a genuinely new research pass against `public-apis`-style directories, same verification discipline as every source above (live-checked before any code is written).

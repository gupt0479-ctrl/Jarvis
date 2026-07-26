---
type: project
status: tree
created: 2026-07-19
updated: 2026-07-26
related_progress:
  - "[[Research Loop - Implementation Plan]]"
  - "[[20_Progress/Internship/Building System/Runs/Phases Run]]"
  - "[[System - Build Log]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
tags:
  - internship
  - automation
  - system-design
next: "Get the 2026-07-26 code (persona config, CS-relevance gate, priority classification, dossier template v2, contact-research widening) actually committed and pushed — see System - Build Log's 2026-07-26 entries. Nothing below this line is live until that happens."
---
# Internship Research Loop — Source of Truth
==The complete, closed statement of what this system is built to do — target scope, current form, in one place.== This is not a build report — [[System - Build Log]] carries the full dated history of every session, what shipped, what's still uncommitted, and why each decision landed where it did. Read that note for *how we got here*; read this note for *what's true about the finished shape right now*.
## What This System Is
Two halves, deliberately different in rigor. **Discovery** is a GitHub Actions workflow (`gupta-builds/internship-research-loop`) that polls six internship-listing sources hourly, filters through a zero-Claude/Anthropic-LLM deterministic gate, and writes survivors into `10_Areas/Career/Internships/List/Dossiers/` — mechanical, unattended, cheap by design. **Promotion onward** is entirely manual, human-judgment-driven, and stays that way on purpose: a dossier becoming a Program note, a Program note turning into real outreach, an outreach turning into a submitted application — none of that is automated, none of it should be.
## The End Goal, Stated Plainly
A real Summer 2027, Winter 2027 (Dec-Jan), or lower-priority Spring 2027 SWE/AI internship, open in the US and OPT-eligible, reaches this vault within an hour of going live anywhere it's discoverable — already carrying enough real content that deciding whether to pursue it takes 60 seconds, not a webpage visit. **A dossier landing in `List/Dossiers/` is not the finish line.** The finish line is a submitted application, and the loop only earns its cost once dossiers are actually promoted through [[30_Order/Workflows/Internship Pipeline]] into real Program notes, real contact research, and real outreach. The success metric is applications submitted per week — not dossiers written, not tests passing, not folders looking tidy.
## The Four Hard Gates — What Has To Be True Before A Dossier Exists
All four share one design principle, applied consistently since the very first rule (`locations_allow`, Phase 2): **permissive by default, exclude only on an explicit negative signal.** A false exclusion silently loses a real opportunity with nothing to show for it; a false inclusion costs one human screening read. That asymmetry is why every rule below errs toward keeping, not discarding, when a signal is ambiguous.
1. **Timing** — `terms: ["Summer 2027", "Winter 2027", "Spring 2027"]` in `core/profile.yaml`. Summer 2027 and Winter 2027 (genuinely Dec 2026-Jan 2027, not the full "Winter" label bucket) are equally high priority; Spring 2027 is wanted but explicitly lower-weighted (`terms_weight`), never a second pass/fail gate.
2. **Location** — United States. An affirmative US signal always passes; an affirmative foreign signal always rejects; anything ambiguous (no data, "Remote," "Multiple Locations") passes.
3. **OPT eligibility** — checked per posting, not per company (the same company can differ role-to-role — proven directly by the 2026-07-19 dossier audit finding Palantir's US Government role citizenship-gated while its Commercial role wasn't). OPT ≠ H-1B sponsorship; "no visa sponsorship" alone is never an exclusion signal. Excluded only on an explicit citizenship/US-person requirement, a security-clearance requirement, or an explicit "OPT/CPT not accepted" statement.
4. **CS/software relevance — added 2026-07-26.** A listing must be genuinely computer science / software engineering at its core, checked *after* the three criteria above, before a dossier is ever written. Adjacent fields (hardware, robotics, astrophysics, space, firmware) are not auto-excluded — they pass only if the specific posting's real content shows genuine software/CS relevance the candidate is suited for (grounded in `Main Resume.md` and `Engineer Edge Roadmap.md`, not guessed). Anything with no software content at all (financial/risk analyst, tax, sports-performance analytics, pure trading-strategy research) is rejected outright and does not land anywhere — not even `Other`.
## Priority Classification — Where A Surviving Dossier Lands
Everything that clears all four gates gets sorted into exactly one subfolder under `List/Dossiers/`, with a short callout at the top citing the real signal that drove the call — never a numeric "Priority N" label; the folder itself is the label:
- **`1 - AI & ML/`** — LLM, RAG, agents, ML infrastructure, applied AI, deep learning signals.
- **`2 - Fullstack/`** — product/frontend/backend/systems engineering, no AI/finance-specific signal.
- **`3 - CyS & Finance/`** — security engineering, or software engineering inside a finance/trading firm.
- **`Other/`** — genuine software engineering that fits none of the three niches above. Same research rigor applies here as anywhere else — this is not a lesser bucket, it exists because "real but not a stated priority" is a legitimate, common case (defense contractors, industrial/embedded software, general enterprise SWE).
`Viewed/` sits alongside these four as a human triage bin (seen, not used) — it is never a pipeline write target.
## Resource Limits — Designed 2026-07-26, Not Yet Implemented In Code
To force real review discipline rather than passive accumulation: **201 total files** in `List/Dossiers/` (excluding `Viewed/`) at maximum — 50 per priority folder, plus the one `Dossiers-to-Create.md` directive note sitting at the root. **Per push, at most ~10 new dossiers** — roughly 3 AI/ML, 3 Fullstack, 3 CyS & Finance, 1 Other; these numbers are a starting point, meant to be tuned against real data, not fixed constants. **Warning stages at 150, 170, 190, and 200** total files, so the system flags itself well before the cap forces a hard decision. **Resource exhaustion** (a source running dry of new eligible postings) gets logged in `10_Areas/Career/Internships/List/Resources` (per-resource usage tracker) with the planned alternative named in `[[20_Progress/Internship/Building System/Research Loop - Resources]]` (the main resource list). None of this is implemented in `run_pipeline.py` yet — see [[System - Build Log]]'s Open section.
## The Promotion Pipeline — Dossier To Submitted Application
Full step-by-step reasoning lives in the new detailed workflow note (`30_Order/Workflows/`, in progress); the short version:
```
Dossier (auto, priority-sorted)
  -> Screen: the fit test (goal-push + personal fit; contact-reachability noted, never gated; pay never a factor)
  -> Commit: Program note (Serious/ or Considering/, identical rigor) + Contacts/Each One (Ongoing/) + Tracker/Each One (Current/)
  -> Reach out via the Contact note's live draft, built from Mimic.md
  -> Ready to actually apply: Job & Company note (deeper, interview-prep-grade company/role research)
  -> Apply: Applying/Now.md entry + an Applied note; Program note moves to its Ended/ subfolder
  -> Outcome: Tracker note's result field set; Contact moves to Ended/ (concluded) or Come Back/ (revisit later)
```
Anything sitting in a Program `Ended/` folder with no matching note in `20_Progress/Internship/Applying/` gets discarded — `Ended` means applied, and if there's no Applying record, it never actually left the research phase and shouldn't claim otherwise.
## Six Sources, Verified Live (as of 2026-07-25)
SimplifyJobs and Jose-Gael-Cruz-Lopez (the original two, `listings.json`-shaped), plus `vanshb03/Summer2027-Internships` (274 entries), `zshah101/...Tech-Internships` (214 entries, carries a `sponsorship` field), Greenhouse and Ashby (direct public-API polling of hand-verified company tokens — no scraping). `freehire` and `artificialintelligencejobs.co` are built, tested, and **not yet committed**. Full detail and what's deliberately deferred (Lever, speedyapply, sndsh404, Intern Dock): [[20_Progress/Internship/Building System/Research Loop - Resources]].
## Explicit Non-Goals
No CAPTCHA-bypass, cookie-injection, or stealth-browser automation against LinkedIn or any login-walled platform, at any phase — a scoped Firecrawl *search* for public LinkedIn snippets is the one sanctioned exception, and it never fetches the underlying LinkedIn page. No Claude/Anthropic LLM call anywhere in the unattended discovery/recheck/OPT-check/classification path — Firecrawl's own extraction runs on Firecrawl's infrastructure and was never in scope for this restriction. Contact discovery uses public sources only.
## What "Closing The Loop" Means Here
Discovery (find through write-gate, including the CS-relevance gate and priority classification) is independently verified solid, repeatedly, by fresh sessions with no stake in the prior claims. **That has never been the same thing as this loop being finished.** The 2026-07-26 session proved the promotion half can actually work — the Appian promotion is the first real end-to-end run of Step 3 in this project's history — but proved it manually, once, with code that isn't shipped yet. Read [[System - Build Log]] for the exact, current gap between "designed" and "live."

---
type: project
status: tree
created: 2026-07-19
updated: 2026-07-19
related_progress:
  - "[[Research Loop - Implementation Plan]]"
  - "[[Phases Run]]"
  - "[[System - Build Log]]"
tags:
  - internship
  - automation
  - system-design
next: Hand the independent audit prompt (in the 2026-07-19 session log entry) to a fresh Claude Code session for a built-vs-planned review.
---
# Internship Research Loop — Source of Truth
==This is the complete, closed statement of everything the internship research loop was built to do — the target scope, in one place, final form. It is not a build report and does not claim any of this is verified working right now — [[Phases Run]] carries the dated evidence log across six phases, and an independent audit (2026-07-19) is the next step to confirm what's actually true against this list. This note exists because the scope grew across six phases in two other notes and no single page stated the finished aim.== [[Research Loop - Implementation Plan]] is the original forward spec this was built against.
## What This System Is
A GitHub Actions workflow in the public repo `gupta-builds/internship-research-loop` polls internship-listing sources on a schedule, filters them against a fixed profile with zero Claude/Anthropic LLM calls anywhere in the loop, and writes the ones that pass into `10_Areas/Career/Internships/List/Dossiers/` in this vault — deterministic field-matching and mechanical checks only, by design, so a 24/7 background process never spends Claude tokens.
## The Complete Scope — Every Component Aimed For
### Discovery Pipeline (Phases 1–3)
Ingestion from SimplifyJobs and Jose-Gael-Cruz-Lopez `listings.json` feeds (zapplyjobs was a third source, later removed entirely — see Phase 5 below); a profile filter (`core/filter.py`) matching rising-junior eligibility, target terms, and category against each source's own schema; a stable `compute_uid()` per source for dedup against `state/seen_ids.json`; a four-check fail-closed write gate (`required_fields`, `url_liveness`, `not_duplicate`, `format_compliance`) before anything touches the vault; pinned dependencies, push-retry-with-rebase against the vault's own independent auto-commit cycle, seen-state marked only after a confirmed push, a pre-fetch schema-drift halt, and a two-tier run log (raw JSONL + a weekly Obsidian rollup) — all four specified as non-optional for unattended scheduled operation, not just wiring.
### Enrichment and Resume Tooling (Phase 4 Scope Decision)
Two tools originally scoped as separate future utilities were pulled into this project: Layer 5 company/contact enrichment (Firecrawl scrape of the company site/blog, contacts from public sources only — GitHub org members, blog bylines, pattern-inferred email validated by MX record — appended to a dossier's `## Enrichment` section), staying promotion-triggered (run manually at [[30_Order/Workflows/Internship Pipeline]] Step 2, never automatic on discovery); and Layer 6, a local keyword-overlap resume grader scoring `Resumes/Main Resume.md`'s tagged bullets against a pasted JD — zero network, zero LLM, a standalone tool.
### Root-Cause Hardening (Phase 5)
Five gaps found during a manual 137→27 dossier cleanup were meant to become permanent code, not a one-time fix: a post-write liveness recheck (`recheck.py` + a separate daily cron, distinct from hourly discovery, with a mass-deletion brake that halts and files an issue rather than deleting more than half the vault), a `degrees_allow: ["Bachelor's"]` gate, JGCL's `season` field mapped into the term-matching path (it was never read before), a fifth write-gate check for cross-source duplicates (the same program landing as separate files from two feeds), and zapplyjobs removed from the pipeline entirely as structurally the wrong fit (its entries are program/resource pages, not deadline-bearing postings).
### The Three Hard Criteria, Real Dossier Content, Permanent Codification (Phase 6)
The final scope addition: dossiers stop being auto-generated one-liners and carry the actual posting's substantive content (role, requirements, comp — verbatim/structural extraction via Firecrawl, not summarization); every survivor is re-screened against exactly three criteria, detailed below; and all three criteria get written into `profile.yaml`/`filter.py` permanently rather than applied as a one-time manual pass.
## The Three Hard Criteria — Final, Definitive Form
1. **Timing** — Summer 2027, or genuinely December 2026–January 2027 (not the full "Winter" term bucket by label alone; a posting's real stated dates should confirm the narrow window where the feed itself doesn't publish months).
2. **Location** — United States. Permissive-by-default is the deliberate design: an affirmative US signal always passes, an affirmative foreign signal always rejects, and anything ambiguous (no location data, "Remote," "Multiple Locations") passes rather than being guessed away — a false negative here silently loses a real match with no error to show for it, which is worse than a rare false positive a human catches on read.
3. **OPT eligibility** — checked per posting, not per company (one company can differ on this axis role-to-role). OPT (Optional Practical Training) is F-1 work authorization the international student already holds; it is not H-1B sponsorship, and "no visa sponsorship" on a posting is not itself an exclusion signal. Exclude only on an explicit negative signal: a US-citizenship/US-person requirement, a security-clearance requirement, or an explicit "OPT/CPT not accepted" statement — never a guessed allowlist of "OPT-friendly companies," the same failure mode the location filter was designed to avoid.
All three share one design principle, applied consistently since Phase 2's `locations_allow` decision: **permissive by default, exclude only on an explicit negative signal.** A wrong guess in either direction is not symmetric here — a false exclusion loses a real opportunity silently; a false inclusion costs one human screening read.
## Explicit Non-Goals
No CAPTCHA-bypass, cookie-injection, or stealth-browser automation against LinkedIn or any login-walled platform, at any phase. No Claude/Anthropic LLM call anywhere in the unattended discovery/recheck/OPT-check path — Firecrawl's own extraction runs on Firecrawl's infrastructure and was never in scope for this restriction, since the principle is about not spending Claude tokens on a background process, not about avoiding LLMs categorically. Contact discovery (Layer 5) uses public sources only — no LinkedIn scraping there either.
## What "Closing The Loop" Means Here
Every component above has a claimed-built status recorded with dated evidence in [[Phases Run]]. This note does not re-assert those claims as independently confirmed — that confirmation is the explicit job of the audit prompt logged in the session log on 2026-07-19, run in a fresh session precisely so the check isn't performed by the same session that wrote the claims. Read this note for *what the system was supposed to become*; read the audit for *what it actually is* as of the date it runs.
## Read Next
[[Phases Run]] for the full dated build/evidence log across all six phases. [[Research Loop - Implementation Plan]] for the original technical spec and the Phase 1-2 build review. `PRD.md` in `gupta-builds/internship-research-loop` for the repo's own self-description, last updated alongside the Phase 6 closing pass.

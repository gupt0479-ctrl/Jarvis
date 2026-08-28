---
type: project
status: active
created: 2026-07-26
updated: 2026-08-29
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts —
    Archive]]"
tags:
  - internship
  - automation
  - prompts
next: "Prompts 22/23 archived 2026-08-29 — both genuinely partial (Prompt 22:
  only 2 of ~11 external sources individually opened; Prompt 23: 195/280
  no-deadline dossiers re-verified, 113 singletons + 9 blocked companies + 1
  unidentified company (\"Acds\") still unresolved), correctly self-reported as
  such, not faked. Prompts 24/25 are strict completion passes — both continue
  the SAME sessions (22→24, 23→25), both carry an explicit no-silent-stopping
  rule: every source/company must end with a real checked-or-justified-skip
  outcome, not a bare \"not reached.\" Prompt 25 requires literal reconciliation
  arithmetic (280 no-deadline + 39 tracked + named exceptions = 320) as its
  actual completion proof. Real scope warning carried into both: Prompt 24 still
  has ~1500+ speedyapply rows, several more full-size jobright-ai repos, and a
  6800-line sharunkumar list genuinely unopened — this is very unlikely to fully
  close in one more pass despite the strict framing, and that's being told to
  the human directly rather than promised away."
---
# Claude Code Prompts — Internship Research Loop
This file holds the next prompt(s) to run, and only that — it gets wiped and rewritten every build cycle, not accumulated. When a prompt finishes and its result is reviewed, its full text and result move into [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] and get deleted from here.

## Prompting Guide In Use
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) — re-apply on every prompt.
- Front-load everything, literal scope, explicit Task Order/Files Touched, `high` effort, generous `max_tokens`.
- Hand over verified facts, instruct re-checking them.
- **A hypothesis this file itself wrote can turn out wrong — say so plainly when it does, don't quietly drop it.** Prompt 14 v2's own JGCL hypothesis (a `SOURCES`-tuple tie-break bug) was checked and found wrong; the real cause was three specific already-deleted scholarship postings. That's now the record, not the guess that preceded it — every doc touched below corrects to the real finding, not a hedge between the two.
- **An alarming-sounding fact ("46 deletions") is worth one direct check before treating it as a problem.** It resolved in one search — a real, already-tracked session (auto-captured, per this vault's own conversation-export layer), not an untracked gap. Cheap to verify, expensive to leave as a nagging unresolved worry across future prompts.
- **When a real source count changes, every doc that states a specific number becomes a small, precise lie until corrected.** Lever going live makes "eight sources" wrong wherever it's written — treat this the same as any other now-stale claim, not a footnote.

---

- **A local git checkout goes stale fast on this project — the pipeline auto-commits hourly.** Read state files via `git show origin/master:<path>`, or `git fetch` + confirm local `HEAD` matches `origin/master` (pull/rebase if not) before trusting any local working-tree read of anything `run_pipeline.py`/`recheck.py` touches. Caught live 2026-08-27: a local `git show`-free read of `state/debate_losses.json` showed 6 entries where `origin/master`'s real, current file had 271 — a local clone can sit dozens of commits behind within a single day.

- **A session sharing a file with a parallel session must only ever append or fix its own entries — never remove something it didn't write because it looks unfamiliar or out of scope.** Real incident, 2026-08-28: Prompt 21's session found 6 legitimate links Prompt 20's session had added to a shared `No Deadline.md` (companies with no existing dossier, correctly out of Prompt 21's own 320-dossier scope) and deleted them as presumed noise during its own cleanup pass. Caught and restored by the coordinating session, not by either prompt session itself. If something in a shared file looks wrong, say so in the report — don't unilaterally remove it.
- **When a follow-up genuinely needs the same deep context a session just built (e.g., re-checking its own just-completed work), tell the human to continue in the SAME session, not paste into a fresh one.** Re-deriving 320 already-read dossiers from scratch in a new session would re-burn the exact token cost being complained about — this project's usual "fresh session per prompt" default is a good default, not an absolute rule, when continuity itself is the point.

# Jarvis
### Prompt 24: Finish The External Resources Sweep — Every Aggregator, No Exceptions
**Continue the SAME session that ran Prompts 20 and 22 — do not start fresh.** It already built the dedup context (which 320 dossiers exist, what's in `Excluded — Losing The Debate.md`, what's already in `_Today/New Internships Listings.md` and `No Deadline.md`). If that session is gone, read Prompts 20's and 22's archived results in `Claude Code Prompts — Archive.md` first — don't re-derive from zero.

**This is a strict completion pass, not another partial one.** Two rounds have now reported "genuinely not reached" on the bulk of these sources. That stops being an acceptable outcome for this round. Every source listed below must end in one of two states in your report: **fully checked** (with real counts), or **explicitly, individually justified as skipped** (not "ran out of time" — a real reason, e.g. "this repo's category is Marketing, confirmed zero CS/SWE-relevant titles in a spot-check of 30 rows, full row-by-row would be wasted effort"). A source left as "not reached" with no individual reason is not an acceptable way to end this pass.

```
**File-state clarification (no bug, just a miscommunication last round):** the "External sources (Prompt 20)" section lives in `_Today/No Deadline.md`, never in `_Today/New Internships Listings.md` — the prior session's confusion was misreading, nothing was lost. Confirmed both files are intact as of 2026-08-29.

**Method — same one that already worked, reuse it, don't rebuild it every time:** at the start of this session, list the 4 dossier folders (`List/Dossiers/{1 - AI & ML, 2 - Fullstack, 3 - CyS & Finance, Other}/`) once and read `List/Excluded — Losing The Debate.md` once — keep both in context for the rest of the session as your dedup index, rather than re-fetching per source. Keyword-prefilter every source's title/role column (software, developer, engineer, SWE, backend, frontend, full stack, machine learning, AI, data science, devops, infrastructure) before opening any individual posting. Same 4 eligibility gates as before (Summer/Winter/Spring 2027 timing, US location, OPT-eligible, genuinely CS/SWE-relevant). Anything passing goes into `_Today/New Internships Listings.md` as a plain link (append-only — a parallel session is touching the shared `_Today/` files too, never delete an entry you didn't add).

**Sources — work this list top to bottom, every one gets a real outcome:**
1. **Finish InternDock Guide 1's remaining 11 entries** (WebFetch's extraction cap stopped at 125/136 last round — try re-fetching with an offset/continuation, or WebSearch the guide page's remaining company names directly, or fetch the raw page source a second way; don't just re-hit the same cap and give up again).
2. **InternDock Guide 2's 5 not-reached entries** (Instacart, Nebius, Clinical Ink, AptaSentry, WhiteRabbit.ai) — open each directly.
3. **speedyapply/2026-AI-College-Jobs** — full pass: keyword-prefilter every row, dedup, eligibility-check and list every survivor. Real scale (~1526+ rows) — budget your session for this being the largest single item.
4. **speedyapply/2026-SWE-College-Jobs** — same full pass (likely heavy overlap with #3, dedup against it too, not just against the vault).
5. **jobright-ai/2026-Software-Engineer-Internship** and **jobright-ai/2026-Engineer-Internship** — full pass, these are the two most likely to carry genuinely new CS/SWE-relevant postings.
6. **jobright-ai/2026-Data-Analysis-Internship** and **jobright-ai/2026-Business-Analyst-Internship** — full pass (data-adjacent roles are a real, not-yet-checked category for this profile).
7. **northwesternfintech/2026QuantInternships** — full pass (quant/trading roles are directly relevant, this project already has a live `3 - CyS & Finance` bucket for exactly this).
8. **sharunkumar/Summer-Internships (README-Off-Season.md)** — full pass (off-season/rolling roles are explicitly still in scope per this project's own permissive-by-default rule).
9. **jobright-ai's remaining category repos** (Consultant, Marketing, Design, Sales, Art, Education, Public-Sector, HR, Legal Internship) — these were deprioritized as near-certainly irrelevant to a CS/SWE profile. Don't skip silently: do a real spot-check (a genuine sample, not zero rows) on each, confirm the CS/SWE-irrelevance holds, and say so with the sample size checked. If a spot-check surfaces even one real CS/SWE-adjacent posting, escalate to a full pass on that repo.
10. **`20_Progress/Internship/Building System/Research Loop - Resources.md` and `10_Areas/Career/Internships/List/Resources.md`** — read both directly. These are the vault's own resource-tracking docs; confirm every source listed in them is either already covered by this sweep, already covered by the automated pipeline (and therefore correctly out of scope here), or genuinely new and worth adding to this list. Don't assume — read them fresh, they may name something not in the pasted-links/PDF set at all.

### Report back
Per source, numbered exactly as above: real count scanned / passed prefilter / passed eligibility (now listed) / deduped away / skipped-with-reason. Total real postings added to `New Internships Listings.md` this pass. If genuinely still not everything gets fully checked in one sitting, say precisely which sources remain and why — no source gets left as a bare "not reached."
```

### Prompt 25: Finish The Dossier Deadline Reconciliation — All 320, No Exceptions
**Continue the SAME session that ran Prompts 21 and 23 — do not start fresh.** It already read all 320 dossiers this cycle. If that session is gone, read Prompts 21's and 23's archived results first.

**Same strict-completion standard as Prompt 24.** The math has to close: every one of the 320 live dossiers ends up counted in exactly one of — `Tracker/Deadline Tracker.md` (has a real deadline), `_Today/No Deadline.md`'s per-bucket sections (genuinely checked, genuinely no deadline found — company-level AND req-level), or a named dead/expired/data-quality exception (like the Rippling dead link, or the Montenson/Mortenson mismatch already logged). **280 (no-deadline) + 39 (Tracker) + however many named exceptions must equal 320. Show this arithmetic explicitly in your report — that's the actual completion proof, not a claim.**

```
**What's actually left, precisely — don't re-do what's already done:**

1. **113 singleton-company dossiers never re-checked at all** (85 companies with exactly 1 dossier each — the company-grouping efficiency trick doesn't apply here since there's nothing to group; this is just finishing the deeper method per-dossier). Full list is derivable by diffing the 320 dossier filenames against the 195 dossiers already covered by the 44 multi-dossier companies from the last pass — do that diff yourself at the start rather than asking for it.

2. **9 blocked/inconclusive companies from the last pass**, still genuinely unresolved: Palantir / Palantir Technologies (same company — treat as one, covers 5 dossiers), HPR, American Fidelity, Aquatic Capital Management, Jump Trading, AbbVie, Specter Aerospace, Copart, PIMCO. Last pass's method (direct company-page fetch) hit a 403 or JS wall on all 9 — **use a different method this time**: WebSearch for "[Company] internship program application deadline 2027" instead of a direct fetch, check archive.org's cached version of the careers page if the live one blocks you, or check the company's LinkedIn/Handshake posting if findable. Don't report these as unresolvable again without having tried at least one genuinely different method per company.

3. **"Acds" — identify the real company.** This appears in two dossier filenames: `AI Operations Intern - Naukr AI - Acds.md` and `AI Operations Intern-Caddell Reynolds - Acds.md`. "Naukr AI" and "Caddell Reynolds" look like they might be the *real* employer names, with "Acds" possibly an ATS/aggregator platform name that got miscaptured as if it were the company — read both dossiers' actual frontmatter (`company`, `url`, `source` fields) and body content directly to resolve this, don't guess. If this is confirmed as a real data-quality bug (wrong company name captured), add it as a new item to `Dossier Corrections.md` — don't silently fix the dossier itself, this is a report-only audit like the rest of that note.

4. **Notion — actually fetch it this time** (last pass's report says the fetch never completed).

5. **Montenson vs. Mortenson** — already logged in `Dossier Corrections.md` item 5; re-check Montenson's dossiers specifically (correct company, not the Mortenson mixup) for a real deadline while you're doing the rest of this pass.

**For every one of the above:** apply the same two-tier method as before (dossier's own stored text first, then a live check) but this time with the company-wide landing-page check included from the start (not just the individual req), since that's the method already validated as more thorough. If a company genuinely has no deadline anywhere after a real, differently-angled attempt: that dossier is now doubly-confirmed, move/keep it in `No Deadline.md`. If a real deadline turns up: add it to `Tracker/Deadline Tracker.md` in the correct bucket (`Already Over`/`Soon`/`Next Week`/`Next Month`/`Later`, extending further if something doesn't fit).

**Shared-file discipline, same as every round:** append-only on `_Today/` files and `Deadline Tracker.md`. Never delete an entry you didn't add this session.
```

#### Report back
The full reconciliation arithmetic (280 + 39 + named exceptions = 320, updated with whatever moved between buckets this pass). Per remaining item above: real outcome, not "not reached" — if something is genuinely still unresolved after a real attempt with a different method, say so with what was tried, not just "blocked."


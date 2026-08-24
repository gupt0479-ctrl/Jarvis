---
type: project
status: active
created: 2026-07-26
updated: 2026-08-24
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]"
tags:
  - internship
  - automation
  - prompts
next: "Prompt 16 (Jarvis — sync Building System docs to the real post-Prompt-14v2 state, correct two now-wrong claims) and Prompt 17 (Codebase — finish InternDock's SOURCES wiring, evaluate the 2 new repo candidates) both ready. Lever is live (9 sources now, not 8) — every doc still saying 'eight sources' is now factually wrong until this lands."
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

# Jarvis
## Prompt 16: Sync Building System To The Real Post-Prompt-14v2 State
**Run inside the Jarvis vault directly** (Windows, Sonnet 5, high effort). Vault-note work only.

**Context — what actually changed, verified, not to be re-derived:** Lever shipped live (`fetch_lever`/`normalize_lever`, wired into `SOURCES`/`recheck.py`, 2 real companies — Palantir plus Belvedere Trading — 61 postings fetched, 3 real matches at build time). InternDock got real detection+parsing code (`ingestion/interndock.py`, sitemap-based, 6 tests) but is **explicitly not wired into `SOURCES` yet** — a partial build, not a live source; don't describe it as one. The JGCL zero-yield question is **resolved**: not a bug, three specific scholarship postings (MLH Fellowship, White House HBCU Scholars, UNCF Scholarships Portal) already correctly excluded via `seen_ids`/`excluded_uids`, the feed is just thin toward non-CS content for this persona. LinkedIn's Greenhouse board and the other 7 named-priority companies (Two Sigma, Citadel, Capital One, Bloomberg, Microsoft, NASA, MLH) are **confirmed dead ends for direct-ATS coverage** — not a "not yet checked" gap, a "checked, no reachable Greenhouse/Ashby/Lever token exists, these are almost certainly on Workday-class ATSes this pipeline has no connector for" finding. Two new, real, unbuilt repo candidates exist (`ApplyGuy/2027-Internships`, `dreamworkhq/Tech-Internships-2027`) — real JSON confirmed, not yet integrated. The 2026-08-23 "46 `vault_delete` calls" that looked alarming when first reported is a real, already-tracked session (`60_Claude/05_Clippings/AI Conversations/WSL/Claude Code/internship-research-loop/08-23 Internship dossier audit and filter-rule reconciliation.md`) — confirm this yourself, but it does not need separate investigation as an untracked event.

### Task 1 — `System - Build Log.md`: add a `## 2026-08-24` entry
Record, in this note's existing dated-entry style: Lever shipped (real numbers), InternDock's partial build (explicitly note it's detection+parsing only, not wired), the JGCL resolution (correct the record — two prior audits gave imprecise "explained by a cleanup" answers without naming which cleanup or which postings; this one has the actual specifics), the LinkedIn/7-company dead-end finding, the two new unbuilt repo candidates, and confirmation that the 2026-08-23 session's deletions are accounted for. Point at the Archive note (`Claude Code Prompts — Archive.md`) for full detail rather than duplicating the whole report inline.

### Task 2 — `Source of Truth.md`: fix now-wrong claims
Read fresh, don't assume which lines are stale. At minimum check: any "eight sources" claim is now wrong (nine, with Lever) — a partial InternDock build should not be counted as a tenth live source. If the JGCL finding or the LinkedIn/7-company dead end is referenced anywhere in this doc with the older, vaguer framing, correct it to the real finding. Leave anything not actually contradicted untouched.

### Task 3 — `Research Loop - Resources.md`: the real update this doc needs
1. Move Lever from "Researched, Deliberately Not Built" to the live sources table, with real verified numbers (2 companies, 61 postings fetched, 3 matches at build time — note these will drift, that's expected, cite the build date).
2. Add InternDock as its own status, distinct from both "live" and "deliberately not built" — something like "detection/parsing built, not yet wired into the scheduled pipeline" — this is a real, new, in-between state this doc doesn't currently have a category for; don't force it into either existing bucket.
3. Re-confirm speedyapply/sndsh404 stay in "deliberately not built" (re-verified 2026-08-24, unchanged) and add the two new candidates (ApplyGuy, dreamworkhq) as found-but-not-yet-evaluated-for-build, with what's actually known about each (real JSON confirmed, entry counts, example postings).
4. Correct the JGCL entry (wherever this doc discusses it) to the real, specific finding — not "thin feed" alone, but why: skews toward non-CS scholarship/fellowship content for this persona, three real examples named.
5. Rewrite the "Named-Program Coverage Check" section's framing given Task 6 of Prompt 14 v2's finding: the open question this section posed a month ago ("check whether these 8 companies post through Greenhouse or Ashby before assuming a ninth source is needed") is now **answered** — no, they don't, confirmed directly. Update the section to state this plainly instead of still posing it as an open "next step, not yet done."

### Task 4 — `10_Areas/Career/Internships/List/Resources.md`: resolve the JGCL "under investigation" flag
Prompt 15 correctly flagged JGCL as under investigation at the time. It's resolved now (Task 3's Prompt 14 v2 finding) — update that line from "in progress" to the real, closed finding.

### Explicitly out of scope
No code changes to `internship-research-loop`. No describing InternDock as a live/wired source — it isn't yet. No describing ApplyGuy/dreamworkhq as evaluated or built — they aren't yet, that's Prompt 17. No re-investigating the 2026-08-23 session unless your own check of the referenced conversation note contradicts what's stated above.

### Report back
Per task: what changed and where, with the specific old-vs-new claim for anything you corrected. Confirm the 46-deletion session check.

---

# Codebase
## Prompt 17: Finish InternDock's Wiring, Evaluate The Two New Repo Candidates
**Fresh session**, `gupta-builds/internship-research-loop`. Read `CLAUDE.md` first. `ingestion/interndock.py` exists (sitemap-based detection + parser, 6 tests) but is not wired into `SOURCES` — verify this yourself, along with everything else below, before starting.

### Task 1 — Design and ship InternDock's SOURCES wiring
The prior session deliberately stopped short of this, correctly flagging it as needing its own design pass rather than a quick bolt-on. Real open questions to resolve, not guess at:
- **Identity/uid strategy.** InternDock's postings don't carry a native id the way Greenhouse/Ashby/Lever do — the prior session found the visible link text is always literally "Apply" (not the title), so the uid can't come from link text. Check what the actual `href` URLs look like (they route to the real employer's own application page, per the fetched content already described) — is there a stable, extractable identifier in those URLs themselves (a job id, a slug), or does uid computation need to fall back to a content-hash-style approach the way the old zapplyjobs fallback did before it was removed? If it's the latter, that's worth naming explicitly as a real limitation, not silently reusing a pattern this codebase removed once already without re-justifying it.
- **State/cadence.** Sitemap-based detection means checking the sitemap for new drop-shaped slugs on some cadence — how often is a real design decision (InternDock's own two known drops were about 6 weeks apart; don't assume hourly makes sense the way it does for the JSON-feed sources). Decide and justify a cadence, and what state needs persisting (which sitemap URLs have already been processed, so a re-check doesn't re-fetch and re-parse everything every time).
- **Volume/capacity interaction.** A single InternDock drop is ~650-658 postings — far more than one run's `MAX_NEW_WRITES_PER_RUN` budget. Confirm the existing per-bucket budget/deferred-list mechanism handles this gracefully (it should, by design — deferred items are simply re-offered next run) rather than assuming it does.
Build it, wire into `SOURCES`, add to `recheck.py`'s `FEEDS` if applicable given the cadence decision above, fixture-based tests using the real content already captured in `tests/fixtures/`, full suite green.

### Task 2 — Evaluate `ApplyGuy/2027-Internships`
Confirmed real JSON exists (example seen: "Toyota of Cedar Park Keating LLC — Software Developer Intern," posted same-day). Verify the schema fresh (required fields, whether it carries a stable id, whether it's a raw feed or something already filtered), check real scale and update frequency, and decide — with the same rigor as every existing source's original evaluation — whether it's worth building. If yes, build it (fetch/normalize/wiring/tests, same discipline as every source before it). If the real schema turns out thin or the source turns out to duplicate existing coverage the way `SuryaHarikrishnan/2027-internship-tracker` did, say so and don't build it.

### Task 3 — Evaluate `dreamworkhq/Tech-Internships-2027`
Confirmed real JSON exists (720 entries at last check, example seen: Fannie Mae "Data Science Intern," carries `salaryMin`/`salaryMax`/`aiRoleKind`/`postedAt`/`firstIndexedAt` fields — a richer schema than most existing sources). Same evaluation discipline as Task 2: verify the schema fresh, check whether its richer fields (pay data, AI-role classification) are worth integrating even partially, check real scale/update cadence, decide whether to build.

### Discipline
Separate commits per source, real citations, fixture-based tests, full suite green at every step. The local pre-push hook will block a broken commit.

### Report back
Task 1: the identity/cadence/state design decisions made and why, confirmation InternDock is genuinely live in `SOURCES` (not just present in the codebase), real numbers from a live test run. Task 2/3: built or not, with real reasoning either way — a "didn't build, here's why" is exactly as valid a result as a new source, don't feel pressure to build both just because they were surfaced.

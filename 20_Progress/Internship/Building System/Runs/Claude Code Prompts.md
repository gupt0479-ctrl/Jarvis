---
type: project
status: active
created: 2026-07-26
updated: 2026-08-23
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]"
tags:
  - internship
  - automation
  - prompts
next: "Prompt 12 (Codebase) and Prompt 13 (Jarvis) both ready, both incorporate real decisions the human made 2026-08-23 (reserved preferred-company slot, MAX_DEBATE_LOSSES→48, keep Viewed/'s existing design, a real Screen artifact for pipeline Step 2) rather than deferring them a third time."
---
# Claude Code Prompts — Internship Research Loop
This file holds the next prompt(s) to run, and only that — it gets wiped and rewritten every build cycle, not accumulated. When a prompt finishes and its result is reviewed, its full text and result move into [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]] and get deleted from here.

## Prompting Guide In Use
[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) — re-apply on every prompt.
- Front-load everything, literal scope, explicit Task Order/Files Touched, `high` effort, generous `max_tokens`.
- Hand over verified facts, instruct re-checking them.
- **This round's lesson: when a delegated session reports a hard blocker ("X isn't available"), verify that claim independently before accepting it as fact.** Prompt 10's session reported `FIRECRAWL_API_KEY` unavailable and left the Zipline re-fetch undone on that basis — checking directly found the key present in `~/.bashrc` on this machine; the session's non-interactive shell just never sourced it. A blocker report is a claim about that session's environment, not necessarily a fact about the real one.
- **Ask, don't infer, on value judgments — and once asked, don't defer the answer a third time.** Two audit rounds correctly flagged the preference-tier design, the loss-threshold tuning, the `Viewed/` conflict, and the "review" note-type ambiguity instead of guessing. All four now have real decisions (below) — the prompts stop flagging them and start implementing them.

---

# Codebase
## Prompt 12: Ship The Two Decided Design Changes, Finish The Deferred Cleanup
**Paste into a fresh session** (the prior one's context is already reflected in the Archive note; nothing here requires its live state). Read `CLAUDE.md` first. As of 2026-08-23: 367/367 tests passing, 7 commits landed (Phase 1-4 of the prior prompt), `HEAD` should match `origin/master` — verify this yourself before starting, along with everything else in this section.

**Two real decisions were made by the human 2026-08-23, after two audit rounds correctly declined to guess at either. Implement both — they are no longer open questions:**

### Task A — Reserved preferred-company slot per bucket
**Decision:** additive reserved slot, not a carve-out of the existing per-bucket budget (`MAX_NEW_WRITES_PER_RUN = {"AI/ML": 3, "Fullstack": 3, "CyS & Finance": 3, "Other": 1}` in `run_pipeline.py`). Real cause this fixes: Citadel's posting classified into the "Other" bucket (a generic "Software Engineer Intern" title hits no bucket-specific regex) — the smallest budget (1/run) — and kept losing recency ties to other preferred companies' fresher arrivals, because `preference_tier: high` is a binary gate with no further differentiation. Design: when at least one preferred-company candidate exists in a bucket's pool for a run and would otherwise lose the debate, grant it **one additional slot on top of** that bucket's normal budget — never subtracted from the general pool's existing slots, so no non-preferred candidate loses ground to make room. If multiple preferred candidates compete for that one reserved slot in the same bucket/run, the existing `debate_compare()` ordering (recency, since tier already ties) still decides among them — this task adds a slot, it doesn't redesign the tie-break within it. Cite the real Citadel case from Task 7's audit (in the Archive) in the code comment, per this repo's own citation convention.
Tests: a preferred-company candidate that would lose the normal-budget debate still gets written via the reserved slot; a bucket with zero preferred candidates this run behaves exactly as before (no extra write); two preferred candidates competing for one reserved slot resolve by the existing recency tie-break.

### Task B — Raise `MAX_DEBATE_LOSSES` from 5 to 48
**Decision:** raise substantially — 48 consecutive hourly losses (~2 days) rather than ~5 hours, so a real arrival burst (the 2026-08-21 burst converted 287 candidates to permanent exclusion in about 5 hours) leaves actual review time before anything is permanently excluded. This is a one-line constant change plus updating its citing comment to reference both the original reasoning and the 2026-08-21 burst evidence that justified raising it. Update `state/debate_losses.json`'s existing tests/fixtures if any assume the old threshold value directly rather than referencing the constant.

### Task C — American Express: the ~20 entries the prior session explicitly skipped
Individually verify each — don't apply a blanket rule, the prior session's caution here was correct. While doing this, check whether Amex's postings share a recognizable job-id shape in their Oracle Cloud HCM URLs (`egug.fa.us2.oraclecloud.com/.../job/<id>` — visible in several `Excluded — Losing The Debate.md` entries from the Task 7 audit) the same way Workday's `-N`-suffixed URLs did in the prior prompt's Task 5. If a real, consistent pattern exists, extend `_ATS_JOB_ID_PATTERNS` to cover it (same domain-anchoring discipline as every existing pattern) and dedupe accordingly; if the URLs are too inconsistent to pattern-match safely, say so and handle the ~20 by direct verification instead.

### Task D — Zipline: re-evaluate the 49 dossiers with the now-shipped extraction fix
**`FIRECRAWL_API_KEY` is available in `~/.bashrc` on this machine — confirm it's actually sourced in your shell (`echo $FIRECRAWL_API_KEY`, and if empty, `source ~/.bashrc` or check how this session's shell was launched) before concluding it's unavailable.** With it available: re-fetch each of the 49 Zipline dossiers' real posting content (not the board-index page the now-fixed extraction correctly flags as thin). Keep confirmed genuine SWE roles, remove confirmed non-technical ones, citing the real per-posting content for each — the board did contain real titles like "Embedded Software Engineer, Validation" mixed in with "Aerodynamics Intern," so don't assume the outcome either direction before checking.

### Discipline
Separate commits per task, full suite green at every step, real citations per this repo's convention. The local pre-push hook will block a broken commit — expected, not an obstacle.

### Report back
Task A/B: the exact diffs and new test results. Task C: how many of the ~20 were genuine duplicates vs. distinct postings, and whether the Oracle Cloud pattern was added. Task D: how many of the 49 survived vs. were removed, with the real content citation for a representative sample of each outcome.

---

# Jarvis
## Prompt 13: Implement The Two Decided Vault Changes
**Run inside the Jarvis vault directly** (Windows, Sonnet 5, high effort). Vault-note work only. **Prompt 12 is running in parallel in a different session — its code changes (the reserved preferred slot, the raised loss threshold) are not live yet when you run this. Don't describe them as already shipped; if you reference them at all, say "decided 2026-08-23, implementation in progress" and cite this file's Prompt 12 entry, not a finished state.**

**Two real decisions were made by the human 2026-08-23. Implement both:**

### Task 1 — Rewrite `Viewed/What was Viewed.md`
**Decision:** keep the existing, already-shipped design. `Viewed/` holds closed postings that were never applied to (per `Internship Notes Standard.md` §4 and `recheck.py`'s real behavior) — that doesn't change. Rewrite the note to describe this correctly, and point to `Applying/Now.md` and `Tracker/Each One/Applied+Result/` as the actual "what have I applied to, so I don't repeat it" view the original note was reaching for — both already exist, both are currently empty (zero real applications submitted yet), which is why the need felt unmet. Cite that two independent audit sessions (Prompts 8 and 9, in the Archive) reached this same conclusion independently.

### Task 2 — A real, lightweight artifact for pipeline Step 2 (Screen)
**Decision:** yes, build something real for the fit-test step — it's the one step in the whole 9-step pipeline with no artifact today. **Genuinely undecided by me, your call to make with reasoning, not mine to dictate:** should this be (a) a required frontmatter field added to the dossier itself (e.g. `screened: {date, decision: yes/no, reason}`), or (b) a separate, minimal note type/file per screened dossier? This vault has an existing, directly-relevant precedent worth weighing: `Internship Notes Standard.md` explicitly chose a `company/<slug>` **tag** over a separate company-hub **note**, reasoning that a new file per occurrence is exactly the kind of accumulating-cost pattern this codebase avoids elsewhere (cited in that Standard's §1). A Screen decision happens for every dossier that gets a real look — potentially hundreds — which is the same shape of scale concern. Weigh that precedent explicitly in your choice; you don't have to follow it if there's a real reason a genuinely separate note serves this better (e.g. if a Screen decision needs its own space for real notes/reasoning too long for a frontmatter field), but state your reasoning either way rather than defaulting silently.

### Task 3 — Update the Standards to describe what you built in Task 2
Extend `Internship Notes Standard.md` (if you chose the frontmatter-field approach) or write a new Standard doc (if you chose a separate note type) — match the citation/depth discipline every other section in that Standard already uses. Update `30_Order/Workflows/Internship Pipeline.md`'s Step 2 description to reference the real mechanism now, not "the fit test" as an undocumented mental check.

### Explicitly out of scope
No code changes to `internship-research-loop`. No describing Prompt 12's code changes as live. No further unilateral decisions on anything not explicitly decided above — if something else looks ambiguous while doing this work, flag it rather than guess, same as every prompt before this one.

### Report back
Task 1: confirm the rewrite and its citations. Task 2: which approach you chose and why, weighed explicitly against the `company/<slug>` precedent. Task 3: what changed in the Standards/Pipeline doc.

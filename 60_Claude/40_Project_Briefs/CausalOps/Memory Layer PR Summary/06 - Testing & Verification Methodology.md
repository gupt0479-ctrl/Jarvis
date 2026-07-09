---
type: project
status: complete
created: 2026-07-09
tags: [causalops, testing, verification, engineering-process]
---

# Testing & Verification Methodology

> [!info] This note is about *how* "done" was actually established throughout this project — a repeated discipline of proving things live before trusting them, cross-checking claims against reality instead of assuming, and treating an automated review pass as a genuine second opinion rather than a formality.

## The Core Discipline: Prove It Live, *Then* Write the Test

A pattern repeats throughout this whole project: before writing a formal automated test for a new piece of behavior, a small, throwaway script was run **against the real infrastructure** (the actual Supabase project, the actual Gemini API, the actual MCP server) to confirm the behavior works *at all*, before committing to a specific test design. Only after that live confirmation was the formal `pytest` test written, matching the already-proven shape.

**Concrete example, in full, showing the actual sequence of steps:**

1. *A hypothesis needed testing:* "can `created_at` be backdated after the fact, to test decay math, without needing a raw-SQL fixture?"
2. *A throwaway script was run first, live:*
   ```python
   store.write_run({...})
   store._client.table("memory_runs").update(
       {"created_at": (datetime.now(UTC) - timedelta(days=30)).isoformat()}
   ).eq("run_id", run_id).execute()
   results = store.search_similar_runs(task_description, k=1)
   print(results[0]["temporal_weight"])  # -> 0.501575820192095
   ```
3. *The live result was checked against the expected math* (`exp(-0.023 × 30) = 0.50158...`) — a match to four decimal places, confirming both that the approach works *and* that the underlying decay formula is implemented correctly.
4. *Only then* was `tests/memory/test_temporal_decay.py` written, codifying this exact proven approach as a repeatable, automated test.

This same sequence — hypothesis, live proof, then formal test — was repeated for the MCP protocol round trip (see [[04 - The MCP Server and Protocol Bridge]]), for the entity-edge idempotency fix, and for the asset-timeline query refactor (both discussed below).

**Why this order matters, as a general practice, not just in this project:** a test written against an *assumed* behavior can pass while testing the wrong thing entirely — for instance, a test could easily assert that "backdating requires a raw SQL fixture" and build elaborate fixture infrastructure for a constraint that doesn't actually exist. Proving the behavior live first means the test design itself is validated against reality before any test code — which is often the more expensive, harder-to-change artifact — gets written around it.

## Verifying Fixes That the Existing Test Suite Was Too Loose to Actually Check

Two of the fixes prompted by automated code review are worth calling out specifically, because the *existing* tests would have passed even if the fix had been wrong — meaning the existing test suite alone was not sufficient evidence the fix worked, and new, targeted verification was required.

**The idempotent-edge-write fix:** the existing test for `write_run()` only asserted `result["entities_indexed"] > 0` — a check that says nothing about whether calling the function twice produces duplicate edges. A dedicated live check was written and run specifically for this:
```python
r1 = store.write_run(artifact)
edges_after_1 = store._client.table("memory_entity_edges").select("id").eq("source_run_id", run_id).execute()
r2 = store.write_run(artifact)  # same artifact, same run_id, called again
edges_after_2 = store._client.table("memory_entity_edges").select("id").eq("source_run_id", run_id).execute()
assert len(edges_after_1.data) == len(edges_after_2.data)  # -> both equal 1, confirmed live
```

**The asset-timeline query refactor:** the existing test only asserted `isinstance(timeline, list)` — true for both a correct targeted query and a broken one that returns everything, or one that returns nothing. A dedicated live check confirmed both that a real asset's timeline is correctly returned, *and* that an unrelated asset's timeline correctly comes back empty (proving the query is actually filtering, not just happening to return the right thing by coincidence in a small dataset):
```python
timeline = store.get_asset_timeline(real_asset_id, since_days=1)
assert len(timeline) >= 1
unrelated = store.get_asset_timeline(f"{tag}-unrelated-host", since_days=1)
assert unrelated == []  # confirms it's a targeted filter, not an accidental full scan
```

## Independent Cross-Checking, Not Just Trusting a Clean Run

Several points in this project involved a specific kind of verification: comparing a result against an independent baseline, rather than trusting a single measurement in isolation.

**Example — confirming a lint/type-check finding was pre-existing, not introduced, with an actual reproducible method (not a guess):**
```bash
git worktree add /tmp/upstream-main-check upstream/main
cd /tmp/upstream-main-check
pyright --pythonpath /path/to/.venv/bin/python src/
# -> 56 errors, 1 warning — identical count to the branch under review
git worktree remove /tmp/upstream-main-check --force
```
A git worktree checks out a second, independent copy of a branch without disturbing the current working directory — this is what made it possible to run the *exact same* `pyright`/`eslint` commands against the real, unmodified `upstream/main`, confirming byte-for-byte identical error counts whether or not this branch's changes were present. The first attempt at this comparison actually gave a *misleading* result (a much larger, different error count) because the interpreter path wasn't correctly resolved in the fresh worktree — a `--pythonpath` flag pointing at the correct virtual environment was needed to get an apples-to-apples comparison, a detail that mattered and was specifically diagnosed rather than accepted at face value.

**Example — reproducing a CI failure exactly, rather than assuming "it's the same thing I see locally":** the CI workflow file itself was read to find the *precise* command CI runs — `python -m ruff check .`, from the repo root, using dependencies from `requirements-dev.txt` specifically, not whatever ruff version happened to be installed locally. This turned out to matter directly: CI's pinned ruff version only flagged 1 error (`I001`, unsorted imports), while the local development environment's newer ruff version flagged 4 (including two `UP047` findings CI's version doesn't even have a rule for). Without reading the CI config precisely, the two extra local-only findings could easily have been mistaken for something that needed fixing to unblock CI, when they were actually irrelevant to it.

## Treating Automated Code Review as a Real Second Opinion, Not a Formality

When GitHub Copilot's automated review returned five inline findings on the pull request, **every single one was independently re-verified against the actual code before being acted on** — not applied on faith, and not dismissed on faith either. The verification process for each finding was the same: read the actual current code the comment referred to, confirm the described problem is real by reasoning through it (or, where possible, reproducing it), and only then write the fix. All five turned out to be real:

1. A stale `.mcp.json` generation pointing at a non-existent endpoint
2. A stale test-instructions file curling the same non-existent endpoint
3. A credential-placeholder-detection gap in `_memory_configured()`
4. A non-idempotent entity-edge write
5. An inefficient (full-scan-then-filter) database query

Each fix was then *itself* verified live — not just re-run through the existing test suite, since (as shown above) two of the five involved behavior the existing tests were too loosely written to actually catch a regression in.

**A sixth bug was found during this same pass — one Copilot's review never flagged at all** (the `execution_mode` default causing a latent test failure, fully explained in [[05 - Reconciling With Main — The Rebase Story]]). This is worth naming explicitly: automated review is a genuinely useful second opinion — it caught five real, specific, correct issues — but it is not exhaustive, and finding something it missed while independently verifying its own findings is exactly the kind of thing that should be expected from careful engineering, not treated as a fluke or a "gotcha" against the tool.

## The Numbers, All Independently Reproduced More Than Once

| Check | Result | Reproduced |
|---|---|---|
| `pytest tests/memory/ -v` (live Supabase + Gemini) | 22 passed, 0 skipped | Multiple times across the project, including after every single fix, not just once at the end |
| `pytest tests/ -m "not integration and not kafka"` | 97 passed | Multiple times, confirming zero regressions from every change, not assumed from the first passing run |
| `ruff check .` (matching CI exactly) | Clean after fixes; 3 pre-existing findings confirmed not CI-blocking | Verified against a real worktree of `main`, not assumed |
| `npm run lint` (frontend) | Clean after fixes; 159 pre-existing findings confirmed identical to `main` | Verified against both `main` and the pre-rebase branch, via the same worktree method |
| `npm run build` | Clean client + SSR build | Re-run after every frontend-touching change, not just once |

## Why "A Skip Is Not a Pass" Was a Recurring, Explicit Warning

Integration tests in this codebase are gated behind real credentials (`SUPABASE_SERVICE_ROLE_KEY`, `GEMINI_API_KEY`) and skip automatically if those credentials aren't present in the process environment — a sensible design, since it means the unit test suite never accidentally makes real network calls. But it creates a specific trap: if credentials are configured in a `.env` file but that file isn't actually sourced into the *current shell* before running `pytest`, every integration test silently **skips** rather than failing — and a skip can be misread, at a glance, as a clean pass, especially in a pytest summary line that just says "N passed" without drawing attention to a separate "M skipped" count sitting right next to it.

This project's own conventions guard against this explicitly: every integration test run in this work was preceded by `set -a && source .env && set +a` in the *same* shell invocation, and the resulting summary line was checked specifically for a skip count of zero, not just an absence of failures — e.g. distinguishing `22 passed, 0 skipped` (a real pass) from a hypothetical `0 passed, 22 skipped` (which would print no failures at all, and could be mistaken for success by anyone not specifically watching for the skip count).

## The Takeaway for a Meeting or an Interview

If asked "how do you know this actually works, beyond 'the tests pass'" — the honest, complete answer has three parts: (1) the behavior was proven live against real infrastructure before the test was even written, and fixes whose correctness the existing tests couldn't actually distinguish were given dedicated live checks, (2) claims about "this is pre-existing, not something I broke" were checked against an independent baseline (a real worktree of the unmodified branch) rather than assumed, and (3) an automated second opinion was treated as genuinely useful — every finding verified rather than blindly trusted, and it caught real things, and one more real thing was found that it missed.

## Where to Go Next

For what's still explicitly open, and how to talk about this project going forward, including in an interview: [[07 - Next Steps, Deferred Work & Career Takeaways]].

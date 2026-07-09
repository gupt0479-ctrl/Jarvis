---
type: project
status: complete
created: 2026-07-09
tags: [causalops, git, rebase, merge-conflicts, engineering-process]
---

# Reconciling With Main — The Rebase Story

> [!info] If someone in the meeting asks "why did this PR touch 111 files when the feature is really just a memory layer" — this note is the answer. This was, honestly, the hardest and highest-risk part of the entire body of work, harder than writing the memory layer itself.

## The Situation, Precisely

This feature branch (`plan/persistent-memory-mcp`) was created and developed against a specific point in the project's history (commit `c921820c`). By the time it was ready to open as a pull request, the target branch (`main`) had moved forward **five separate commits** with substantial, unrelated work:

```
c921820c  ← where this feature branch started
   │
   ├── (this branch's 5 commits: rebrand, memory layer, MCP fix,
   │    docs cleanup, Supabase hardening + decay test)
   │
main:
   ├── 3eea8a4d  feat: add nvidia-backed execution modes
   ├── 3b3f1b0b  feat: make the result workspace 5d-first
   ├── ef890756  chore: remove frontend run mock
   ├── 9b8eb75d  test: add result layout visual coverage
   └── 3c05929c  Update README
```

1. A **new primary LLM backend** — NVIDIA's Nemotron model, via NIM/API Catalog, with Gemini demoted to a fallback (used only when `NVIDIA_API_KEY` is unset) and Azure OpenAI further demoted to a final fallback.
2. A new **`execution_mode`** concept ("standard" vs. "deep") — a fast/cheap execution path (`_seed_standard_swarm`, local memo ranking, a deterministic causal fallback) alongside the original full multi-agent pipeline.
3. A **"5D-first" result workspace** redesign on the frontend.
4. New **visual regression test coverage**.
5. A substantial **README rewrite**.

Opening a pull request without reconciling these first would have produced a PR full of misleading, conflict-laden diff noise, and — more importantly — genuine risk of the memory-layer code silently breaking against the *current*, not the *historical*, state of the coordinator. **The decision made here was to stop and reconcile properly before opening anything**, rather than let a reviewer discover the conflicts, or worse, merge something broken.

## Why `git merge --squash` Instead of `git rebase` — The Actual Trade-off

A `git merge --squash` was used to bring the entire feature branch's changes onto current `main` as one set of conflicts to resolve **once**, rather than replaying five original commits individually through a `git rebase`. The reasoning:

- A standard `git rebase` replays each of the five original commits *one at a time* on top of the new base. If two different original commits both touched a file that also conflicts with upstream changes, the *same conceptual conflict* can surface more than once, at different points in the replay, potentially requiring inconsistent resolutions across the sequence.
- With a divergence this size (5 commits on each side, 19 overlapping files including core coordinator logic), resolving the same underlying conflict correctly once was judged safer than resolving fragments of it five times in sequence.
- The trade-off, made explicitly and disclosed rather than hidden: the five original, semantically-distinct commits collapsed into one commit on the pushed branch. The original granular history was not discarded — it was kept on a local backup branch (`backup/plan-persistent-memory-mcp-pre-rebase`) specifically so it could be recovered if ever needed, rather than being an unrecoverable loss.

**Before touching anything, the actual scope of the conflict was measured, not guessed** — a non-destructive `git merge-tree` dry run was used to see exactly which files would conflict *before* starting real conflict resolution, and a file-overlap comparison (`comm -12` on the sorted list of files each side touched) was run specifically to quantify the risk: 19 files were touched by *both* sides, including `src/coordinator/runner.py`, `src/schema.py`, `pyproject.toml`, and `docker-compose.yml` — this number is what justified treating the reconciliation as a serious, standalone task rather than something to rush through.

## What Actually Had Conflicts, and How Each Was Resolved

Nine files had genuine, hand-resolved conflicts (not mechanical auto-merges):

| File | The conflict | The resolution |
|---|---|---|
| `src/coordinator/runner.py` | The new `execution_mode` branching had to be interleaved with the new `memory_retrieve`/`memory_write` phases | Memory phases now bracket the *entire* pipeline unconditionally, regardless of mode — see [[02 - The Persistent Memory Layer, Component by Component]] |
| `app/src/routes/run.ts` | One side deleted the file (an intentionally-removed frontend mock, commit `ef890756`), the other side had cosmetically modified it (just a rebrand string change) | Took the deletion — the file's removal was deliberate upstream work with a clear commit message explaining why; this branch's change to it was purely cosmetic and not worth resurrecting |
| `app/src/components/.../GraphWorkspace.tsx` | A new file added upstream, under the *old* pre-rebrand directory path (`hivemind/`) | Git's own rename-detection heuristic actually placed the file at the correct renamed path automatically; only its one internal import (`@/lib/hivemind-types` → `@/lib/causalops-types`) needed a manual fix |
| `.env.example`, `docker-compose.yml`, `.gitignore` | Both sides had added genuinely different, non-overlapping content (NVIDIA config vs. Gemini/Supabase/memory-layer config; new Kafka-tuning env vars vs. the new `mcp` service) | Hand-merged — neither side's additions were dropped; the three new upstream env vars (`HIVEMIND_BARRIER_TIMEOUT_S` etc.) were additionally renamed to match this branch's `CAUSALOPS_*` convention, since they were added *after* the rebrand and had never been touched by it |
| `README.md` | The most complex conflict: an old "Future Enhancements" roadmap list (containing the *exact sentence this whole PR implements* — see [[00 - Executive Summary (Meeting Prep)]]) had landed under the wrong heading purely because of how the diff happened to line up positionally against an unrelated, much larger README rewrite | Relocated to a new, dedicated "Persistent Semantic Memory Layer" section; the Future Work → Knowledge Graph roadmap items this PR actually delivers ("cross-investigation retrieval," "persistent organizational memory") were marked done with strikethrough rather than left listed as still-planned |
| Every file referencing a `HIVEMIND_*`-prefixed environment variable | `main` had added *three new* environment variables in this old naming scheme (`HIVEMIND_BARRIER_TIMEOUT_S`, `HIVEMIND_SPAWN_CONCURRENCY`, `HIVEMIND_KAFKA_MAX_POLL_INTERVAL_MS`), after this branch had already renamed everything else to `CAUSALOPS_*` | Renamed for consistency, across `coordinator/barriers.py`, `coordinator/spawn.py`, `worker/consumer.py`, `docker-compose.yml`, `.env.example`, and the two tests that set them |

## A Real Bug This Reconciliation Introduced, and How It Was Caught

This is the single most instructive part of the whole story. After all conflicts were resolved and the full test suite passed, a **second, unrelated task** (responding to automated code-review feedback, days later) required re-running the memory test suite live. That rerun failed — and the failure was not in any code touched by that second task. It was a **latent bug the rebase itself had silently introduced**, sitting undetected through the initial "all tests pass" check.

**What happened, traced precisely:** `tests/memory/test_end_to_end.py` calls `execute_run()` without specifying an `execution_mode` — which didn't exist as a concept when this test was originally written. Because `execution_mode` now defaults to `"standard"`, the coordinator started routing through the **new** fast-path functions (`_seed_standard_swarm`, `_run_fast_causal_loop`) instead of the original full pipeline this test's fakes were built for. The actual traceback:

```
src/coordinator/runner.py:61: in execute_run
    await _seed_standard_swarm(record, run_store)
src/coordinator/runner.py:188: in _seed_standard_swarm
    publish_artifact(...)
src/bus/publish.py:29: in _emit
    run_id, correlation_id, ctx = _require_context()
RuntimeError: Run publish context not bound; call bind_run_context first
```

The test's own setup mocked `publish_telemetry` and `bind_from_state` to no-ops (a standard pattern in this test suite for avoiding real Kafka dependency), but `_seed_standard_swarm()` — a function that didn't exist when the test was written — *also* calls `publish_artifact()`, which the test never anticipated needing to mock. After adding that missing mock, a *second*, different failure surfaced: `_run_fast_causal_loop()` imports `_fallback_causal_payload` and `_sanitize_graph` from the `causal` module — but the test's fake replacement `causal` module (built specifically to avoid needing a real LLM call) only defines the two functions the *old, deep-only* pipeline needed, not these new ones.

**Why the first test run didn't catch this:** the first "all tests pass" check happened immediately after conflict resolution, in the same verification pass — and simply calling the same test twice with the same code produces the same *deterministic* result every time. This wasn't a flaky test; it was a real, reproducible failure that had been sitting there since the rebase, only surfaced because someone happened to run that specific test file again for an unrelated reason, days later.

**The fix, and why this specific fix was the right one rather than just patching around the symptom:** rather than adding more and more mocks to make the "standard" fast path work with this test's fakes, `execution_mode="deep"` was pinned explicitly on both `execute_run()` calls in the test — restoring the exact pipeline shape its fakes were always built for. This matches the convention the codebase's *other* coordinator test (`test_coordinator_runner.py`) already used: it has two separate test functions, one explicitly passing `execution_mode="deep"` and one explicitly passing `execution_mode="standard"` with the *correct*, complete set of mocks for that path — a pattern that, if it had been copied instead of a bare `execute_run()` call, would have prevented this bug from ever existing.

**The lesson worth stating explicitly, because it's genuinely useful career-relevant judgment, not just a war story:** *"all tests passed right after I made the change" is not the same claim as "this change has no latent bugs."* A test suite only proves what it actually exercises, and a default value silently changing behavior underneath an existing test is a specific, common, and easy-to-miss failure mode in exactly this kind of branch-reconciliation work. Rerunning tests later, for an unrelated reason, is what caught this — which is itself an argument for re-verifying rather than treating a single green run as permanent proof, a theme explored fully in [[06 - Testing & Verification Methodology]].

## Silent Breakage That Had Nothing to Do With Merge Conflicts At All

One more real bug was found during this reconciliation, in a file that had **zero conflict markers** — meaning Git's automatic merge considered it perfectly clean, with no manual resolution required or even flagged. `app/src/components/causalops/ScenarioBuilder.tsx` had a new import line, added by `main`'s changes, referencing `@/lib/hivemind-types` — a module path that had already been renamed to `@/lib/causalops-types` by this branch. Git's three-way merge algorithm only flags a conflict when *both* sides changed the *same* line — since only `main`'s side touched this specific line (adding a brand-new import for its new `ExecutionMode` type), and this branch had never touched that exact line (only the surrounding file, elsewhere), the merge proceeded silently, producing a file that would fail to build.

This is a structurally important point, worth being precise about: **"no conflict markers" is not the same claim as "nothing broke."** It was caught by a deliberate, repo-wide grep for leftover old-naming references (`grep -rn "hivemind" --include="*.tsx" --include="*.ts"`) run *after* resolving the visible conflicts — specifically as a check against exactly this class of silent breakage — not by the merge tool, and not by any test (the frontend build wouldn't have caught it either, since the import statement is syntactically valid TypeScript; it would only fail when the bundler actually tried to resolve the now-nonexistent module path, which was verified as a real failure mode by attempting exactly that build after the fix, and confirming it succeeded).

## What This Demonstrates as an Engineering Skill

If this comes up in an interview: this is a concrete example of **safely reconciling a long-lived feature branch with a fast-moving main branch** — a routine, high-stakes task in any real engineering team, and one where the actual risk isn't "will Git show a conflict marker," it's "will something silently behave differently after the merge succeeds." The two real bugs found here (the silent broken import, and the latent test failure from a changed default) are both examples of exactly that risk, caught by disciplined re-verification rather than by trusting a clean merge or a single passing test run. Being able to walk through both of these specific examples, with the actual tracebacks and the actual reasoning for each fix, is a stronger interview answer than a general claim of "I'm careful with merges."

## Where to Go Next

For how every claim in this story was actually verified (not just asserted): [[06 - Testing & Verification Methodology]].

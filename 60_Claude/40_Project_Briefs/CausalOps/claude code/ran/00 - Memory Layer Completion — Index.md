---
type: project
status: active
created: 2026-07-08
tags: [causalops, memory-layer, claude-code, prompt, index]
---

# Memory Layer Completion — Prompt Index

> Read this note first. It tells you what's actually left, in what order, and why — before you paste any prompt below into a session.

## Where This Comes From

Two sources, both already verified against the live repo and the live Supabase project (not just re-read):

1. [[Roadmap]], [[Memory Layer]], [[Memory Layer Implementation Plan]] — the original spec and status notes.
2. **[Independent Review artifact](https://claude.ai/code/artifact/995b5795-02d0-44a8-98bd-3921844d1cf1)** (2026-07-05) — a line-by-line check of every claim in those notes against the running code, the test suite, and the live Supabase project (`glbmdbwqmuttykhicasq`) via direct MCP calls.

The review's headline finding: the notes' "pending: run SQL migration, run integration tests" status is **stale** — both have already happened. The real remaining work is narrower and more concrete than the notes suggest:

1. A verified functional bug in the standalone MCP server (wrong port/host on the Docker/SSE path).
2. Two small doc/schema drifts (a self-contradicting line in `CLAUDE.md`, ungenerated frontend TS types).
3. A real, still-missing piece of test coverage: nothing proves two sequential runs actually round-trip through memory end-to-end via the real coordinator.
4. One optional efficiency cleanup, not blocking.

## Decisions Already Made (don't re-litigate these in a session)

Asked and answered on 2026-07-08 — each prompt below assumes these:

| Question | Decision |
|---|---|
| RLS enabled with zero policies on `memory_runs`/`memory_entities`/`memory_entity_edges` — change it? | **No.** Verified: nothing in `app/src` queries these tables directly (the Supabase client is only ever used for auth — `client.ts`, `client.server.ts`, `auth-middleware.ts`; `supabaseAdmin` is defined but imported nowhere). Deny-all-except-service_role is correct as-is. No code change. |
| MCP server Docker/SSE path is broken — fix it, or drop it and go stdio-only? | **Fix it.** Keep the Docker deployment working; verify with a real curl against the running container, not just an import check. |
| Regenerate frontend Supabase TS types? | **Yes, now.** Cheap, closes real drift. |
| Integration tests unconfirmed in the review's sandbox — require a fresh real pass? | **Yes.** A clean `pytest tests/memory/ -v` run (all of it, not just units) is the acceptance gate for calling this phase done. |

## Execution Order

Run these as **separate Claude Code sessions**, in order. Each is independently testable and small enough to stay cheap; don't combine them — that's what blew the token budget up last time this project's notes were re-derived instead of referenced.

| # | Prompt | Est. output tokens | Depends on |
|---|--------|---------------------|------------|
| 1 | [[01 - Fix MCP Server Deployment and Housekeeping]] | 8-15k | none |
| 2 | [[02 - Close Documentation and Schema Drift]] | 6-12k | none (parallel-safe with #1) |
| 3 | [[03 - End-to-End Memory Verification and Integration Gate]] | 25-40k | #1 and #2 done (so the report it writes is accurate) |
| 4 | [[04 - Optional Batch Entity Upserts]] | 5-10k | none — run whenever, or skip |

Prompts 1 and 2 touch disjoint files and can run in either order or in parallel sessions. Prompt 3 is the real gate — it's the one that determines whether "memory layer: complete" is actually true. Prompt 4 is pure polish; skip it if you're only trying to close out the roadmap item.

## Caught While Verifying These Prompts Against the Codebase (2026-07-08)

A second pass — reading `coordinator/runner.py`, `coordinator/store.py`, `tests/test_coordinator_runner.py`, `app/package.json`, and this shell's actual `PATH`/env behavior line by line before trusting the prompts below — surfaced three real gaps that got fixed in place, plus one deliberately-deferred item:

- **`.env` is never auto-loaded.** Confirmed no dotenv loading anywhere in this repo's pytest/conftest setup or the Supabase CLI path. Every prompt that needs live credentials (Prompt 2's type generation, Prompt 3's integration gate, Prompt 4's verification) now explicitly does `set -a && source .env && set +a` in the same shell call — otherwise integration tests silently **skip** rather than fail, and a skip can misread as a clean pass.
- **`CLAUDE.md` has a second stale line**, not just the "after DoWhy" one: the line right below it — `PENDING: Run SQL migration on the Supabase project, then run integration tests` — is also false (migration's already applied). Folded into [[02 - Close Documentation and Schema Drift]].
- **`app/package.json` has no `typecheck` script.** Prompt 2's frontend verification step now uses the confirmed-working `cd app && npx tsc --noEmit` instead of guessing a script name.
- **Deliberately not covered by any prompt: temporal-decay math has zero automated verification.** The `exp(-0.023 * age_in_days)` half-life formula lives entirely in the `search_similar_runs` Postgres RPC. Testing it for real means backdating a row's `created_at` via raw SQL and confirming `weighted_score` ordering shifts accordingly — doable, but nothing in `store.py`'s write path lets you set `created_at` (it's always the column default `now()`), so it needs a raw SQL fixture, not a Python-level test. Left out of Prompt 3 deliberately: this is simple, already-reviewed Postgres math with low risk of being wrong, versus real added complexity for a low-probability bug. Flag it if you want it added as a fifth prompt later — it isn't blocking.

Also confirmed directly (not assumed): `execute_run()` gracefully falls back to `run_store.create_run(...)` if the `run_id` doesn't already exist (`coordinator/runner.py` lines 30-44) — so Prompt 3's two-run test correctly calls `execute_run()` directly without a separate pre-creation step, matching the existing pattern in `tests/test_coordinator_runner.py`, which was run this session and passes in 0.74s with zero Kafka/network dependency.

## What NOT to Do

- Don't re-run the SQL migration. It's already applied (`enable_pgvector`, `create_memory_layer_schema`, `enable_rls_memory_tables` — confirmed via `list_migrations` against the live project).
- Don't re-derive the "why" behind any design decision already logged in [[Memory Layer Implementation Plan]] section 9 (Architecture Decision Log). Reference it, don't re-litigate it.
- Don't touch `dataset_compiler.py` or `estimators.py`. Still off-limits, unrelated to any of this.
- Don't run `pytest tests/memory -m integration` from inside a tool-sandboxed shell and trust a hang as a pass or a fail — the review session hit exactly this and got zero output after several minutes. Run it from a real terminal.

## Related Notes

- [[Memory Layer]] — current component status (update this note's "Pending" section once Prompt 3 closes)
- [[Roadmap]] — update the Memory Layer status row once all four prompts land
- [[Token Efficiency Notes]] — the conventions these prompts follow

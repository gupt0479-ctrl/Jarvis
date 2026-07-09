---
tags: [causalops, prompt, memory-layer, claude-code, docs, supabase]
created: 2026-07-08
task: memory-layer-doc-schema-drift
model: claude-sonnet-4-6
---

# Prompt 2 — Close Documentation and Schema Drift

> Copy the fenced prompt into a fresh Claude Code session. Independent of [[01 - Fix MCP Server Deployment and Housekeeping]] — run in either order, or in parallel. See [[00 - Memory Layer Completion — Index]].

## Why This Exists

Two small, unrelated pieces of drift the [Independent Review](https://claude.ai/code/artifact/995b5795-02d0-44a8-98bd-3921844d1cf1) found between what's documented/generated and what's actually true:

1. `CLAUDE.md` contradicts itself: its "Five components" bullet list says the memory-write phase runs "after DoWhy completes," but its own "Phase sequence" block three paragraphs later — and the actual code in `src/coordinator/runner.py` — has it running after `policy_learning` (i.e. after reasoning and RL finish too). The code is right; one bullet line is stale.
2. `app/src/integrations/supabase/types.ts` was never regenerated after the memory-layer SQL migration landed. It has zero references to `memory_runs`, `memory_entities`, or `memory_entity_edges`. The plan (`Memory Layer Implementation Plan.md`, section 6.7 / step 20) called for this and it was dropped.

Neither is urgent — nothing currently breaks — but both are cheap to close now versus letting them rot as permanent drift.

## Hard Rules

- This prompt touches exactly two files: `CLAUDE.md` and `app/src/integrations/supabase/types.ts`. Do not edit any `src/memory/` or `src/coordinator/` source as part of this prompt — if you find yourself wanting to, stop, that belongs in a different prompt.
- `types.ts` is machine-generated. Do not hand-edit it — regenerate it via the Supabase CLI and let the tool own the output.
- Never commit `.env`. This prompt needs `SUPABASE_ACCESS_TOKEN` to run the type-generation command — it is a **personal access token** (Supabase dashboard → Account → Access Tokens), distinct from `SUPABASE_SERVICE_ROLE_KEY`. Check `.env` for it before starting; if it's missing, stop and tell the user to add it rather than trying to work around it.

## Implementation Order

1. **Check the prerequisite first**, before touching anything:
   ```bash
   grep -q "^SUPABASE_ACCESS_TOKEN=" .env && ! grep -q "^SUPABASE_ACCESS_TOKEN=your-" .env && echo "present" || echo "MISSING — stop and ask the user to add it"
   ```
   If missing, report that back immediately and do not proceed to step 4. The `CLAUDE.md` fix (steps 2-3) can still be done independently — do that part and report the blocked part separately.

2. Fix the `CLAUDE.md` contradiction. Find the "Five components" section (near the top, describing the memory layer) and correct the line describing when `memory_write` runs — it should match the "Phase sequence" block already in the same file:
   ```
   memory_retrieve → orchestrator → parent_evolution → parents (Kafka barrier)
     → gather_children → child_evolution → children (Kafka barrier) → evaluator
     → causal_loop (retries) → reasoner → policy_learning → memory_write → completed
   ```
   Change whatever currently says memory is written "after DoWhy completes" to say "after policy_learning completes (i.e. after reasoning and RL, not immediately after estimation)." Search the whole file for any other occurrence of the same stale claim — fix all of them, not just the first match.

3. `CLAUDE.md` also has a second, separate stale line right below the one you just fixed: `**Status:** Complete. ... PENDING: Run SQL migration on the Supabase project, then run integration tests.` Both halves of that PENDING sentence are now false — the migration is already applied (confirmed via `list_migrations` against the live project: `enable_pgvector`, `create_memory_layer_schema`, `enable_rls_memory_tables`), and whether integration tests pass for real is being verified separately in [[03 - End-to-End Memory Verification and Integration Gate]], not yet confirmed at the time you're running *this* prompt. Rewrite that line to state the migration is done and point at the other prompt for current integration-test status — don't just delete it or claim integration tests are passing, since you have no way to confirm that from this prompt alone.

4. **Before running the Supabase CLI, load the token into the shell environment** — `.env` existing on disk is not enough; the CLI reads `SUPABASE_ACCESS_TOKEN` from the process environment, and a fresh shell does not auto-load `.env` (confirmed: no dotenv loading anywhere in this repo's tooling). Source it explicitly:
   ```bash
   set -a && source .env && set +a
   ```
   Do this once, in the same shell session you'll run the next command in (the exported variable won't persist to a *different* shell invocation).

5. Regenerate the Supabase TypeScript types:
   ```bash
   npx supabase gen types typescript \
     --project-id glbmdbwqmuttykhicasq \
     --schema public \
     > app/src/integrations/supabase/types.ts
   ```

6. Verify the regeneration actually picked up the memory tables:
   ```bash
   grep -c "memory_runs\|memory_entities\|memory_entity_edges" app/src/integrations/supabase/types.ts
   ```
   Expect a non-zero count. If it's zero, the CLI ran against the wrong project or schema — do not report success.

7. Confirm nothing else in `app/` broke from the regeneration. There is no `typecheck` script in `app/package.json` (only `dev`, `build`, `build:dev`, `preview`, `lint`, `test`) — `typescript` is a devDependency and `app/tsconfig.json` exists, so run the type check directly:
   ```bash
   cd app && npx tsc --noEmit
   ```
   The memory tables are new additions to the generated types, not replacements of existing ones, so this should be a no-op, but confirm rather than assume.

8. `git diff --stat` to show exactly what changed in both files — the types.ts diff should be additive (new table/RPC types), not a rewrite of existing ones. If it looks like a wholesale rewrite of unrelated tables, stop and check you pointed the CLI at the right project ref.

## Report Back

Confirm whether step 1's prerequisite was met. If it was: paste the `grep -c` count from step 6, confirm the type-check in step 7 passed, and summarize both `CLAUDE.md` diffs (the phase-order line and the PENDING line). If the token was missing: report the `CLAUDE.md` fixes as done and the types regeneration as blocked, with the exact env var name the user needs to add.

## A Note on Tooling

If a bare `pytest`, `ruff`, `pyright`, or `python` isn't found on `PATH` in your shell, this repo's tools live in `.venv/bin/` — use `.venv/bin/<tool>` instead. Confirm which resolves before assuming a command failed for a real reason.

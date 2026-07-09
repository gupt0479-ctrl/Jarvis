---
type: project
status: complete
created: 2026-07-09
tags: [causalops, memory-layer, supabase, database, sql]
---

# Supabase Schema, Migrations & Data Layer

> [!info] This note explains the database side of the memory layer in full detail: what tables exist and why, the complete SQL for every migration, how Row-Level Security actually protects the data (with a concrete scenario of what it prevents), what got hardened and why, and how the schema is now kept in version control.

## Why Supabase, Specifically

Supabase is Postgres with extensions and a hosted REST/RPC layer on top — not a proprietary database, just a managed, extended Postgres. The two features that specifically make it the right fit here:

- **`pgvector`** — a native Postgres extension for storing and searching high-dimensional embedding vectors efficiently. Without it, "find the 5 most similar embeddings out of 100,000 rows" would mean pulling every single row back to the application and computing distance in Python — a query pgvector instead answers directly inside the database using an index, in roughly logarithmic rather than linear time.
- **PostgREST** — every table and every SQL function is automatically exposed as a callable REST/RPC endpoint. This is *why* `src/memory/store.py` never hand-writes an HTTP route for any of this — calling `self._client.table("memory_runs").upsert(...)` or `self._client.rpc("search_similar_runs", {...})` is a thin Python wrapper around an HTTP call PostgREST generates automatically from the schema.

**Project ID:** `glbmdbwqmuttykhicasq`

## The Entity-Relationship Picture

```
memory_runs                     memory_entities
┌──────────────────┐            ┌──────────────────┐
│ id (uuid, PK)     │            │ id (uuid, PK)     │
│ run_id (unique)   │◀───┐       │ entity_type       │
│ task_description  │    │       │ entity_value      │   UNIQUE(entity_type,
│ task_embedding     │    │       │ first_seen        │    entity_value)
│   vector(1536)     │    │       │ last_seen         │
│ memos (jsonb)      │    │       └──────────────────┘
│ causal_graph       │    │                │  ▲
│ estimate_report    │    │                │  │
│ created_at         │    │                ▼  │
└──────────────────┘    │       memory_entity_edges
                          │       ┌──────────────────┐
                          └───────│ source_run_id     │  ON DELETE CASCADE
                                  │ source_entity_id   │  ON DELETE CASCADE
                                  │ target_entity_id   │  ON DELETE CASCADE
                                  │ relationship       │
                                  │ created_at         │
                                  └──────────────────┘
```

## The Schema, Table by Table, With Full Column Detail

### `memory_runs` — one row per completed CausalOps run

| Column | Type | Purpose |
|---|---|---|
| `id` | `uuid, PK` | internal surrogate key, `gen_random_uuid()` default |
| `run_id` | `text unique` | ties back to the coordinator's run identifier |
| `task_description` | `text` | the original incident description, verbatim |
| `task_embedding` | `vector(1536)` | the Gemini embedding, indexed via HNSW for fast similarity search |
| `memos` | `jsonb` | the decision memos produced during the run |
| `causal_graph` | `jsonb` | the hypothesized/estimated causal DAG |
| `estimate_report` | `jsonb` | the DoWhy/statsmodels output — `ate`, `method`, `n_rows`, etc. |
| `agent_tier_metrics` | `jsonb` | deterministic per-tier scoring, unrelated to memory but carried through |
| `created_at` | `timestamptz` | drives temporal decay — see [[02 - The Persistent Memory Layer, Component by Component]] |

### `memory_entities` — deduplicated across all runs

One row per unique `(entity_type, entity_value)` pair ever seen — assets, MITRE techniques, CVEs, or causal-graph node names. The unique constraint on `(entity_type, entity_value)` means the same asset seen in ten different incidents is still one row, with `last_seen` (and `first_seen`, if this is the first time) updated each time via `upsert(..., on_conflict="entity_type,entity_value")`.

### `memory_entity_edges` — one row per relationship, tagged by which run produced it

Foreign keys to both `memory_entities` (on `source_entity_id` and `target_entity_id`) and to `memory_runs.run_id` (`source_run_id`), all with `ON DELETE CASCADE` — meaning if a run is ever deleted, its edges disappear automatically, without needing separate cleanup logic.

## The Complete SQL — Four Migrations, Now Tracked as Code

A real gap this PR closed: **the schema had never been captured as local migration files** — it existed only as SQL that had been run directly against the live project via ad hoc tooling calls, with no record of it anywhere in the repository. If the project ever needed to be reproduced on a fresh Supabase instance, or a disaster-recovery scenario arose, there was nothing to run. This is now fixed: `supabase/migrations/` contains the exact SQL that's actually live on the project, pulled directly from Supabase's own migration history table (`supabase_migrations.schema_migrations`) — not reconstructed from memory or guesswork.

**Migration 1 — `enable_pgvector`:**
```sql
CREATE EXTENSION IF NOT EXISTS vector WITH SCHEMA extensions;
```

**Migration 2 — `create_memory_layer_schema`** (abbreviated; full version in the repo):
```sql
CREATE TABLE IF NOT EXISTS memory_runs (
  id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  run_id              TEXT NOT NULL UNIQUE,
  task_description    TEXT NOT NULL,
  task_embedding      extensions.vector(1536) NOT NULL,
  memos               JSONB NOT NULL DEFAULT '[]'::jsonb,
  causal_graph        JSONB NOT NULL DEFAULT '{}'::jsonb,
  estimate_report     JSONB NOT NULL DEFAULT '{}'::jsonb,
  agent_tier_metrics  JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS memory_runs_embedding_idx
  ON memory_runs USING hnsw (task_embedding extensions.vector_cosine_ops);

CREATE TABLE IF NOT EXISTS memory_entities (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_type   TEXT NOT NULL,
  entity_value  TEXT NOT NULL,
  first_seen    TIMESTAMPTZ NOT NULL DEFAULT now(),
  last_seen     TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (entity_type, entity_value)
);

CREATE TABLE IF NOT EXISTS memory_entity_edges (
  id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source_entity_id  UUID NOT NULL REFERENCES memory_entities(id) ON DELETE CASCADE,
  target_entity_id  UUID NOT NULL REFERENCES memory_entities(id) ON DELETE CASCADE,
  relationship      TEXT NOT NULL,
  source_run_id     TEXT NOT NULL REFERENCES memory_runs(run_id) ON DELETE CASCADE,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE OR REPLACE FUNCTION search_similar_runs(
  query_embedding   extensions.vector(1536),
  match_count       INT DEFAULT 5,
  decay_lambda      FLOAT DEFAULT 0.023
)
RETURNS TABLE (run_id TEXT, task_description TEXT, similarity FLOAT,
               temporal_weight FLOAT, weighted_score FLOAT, created_at TIMESTAMPTZ,
               causal_graph JSONB, estimate_report JSONB, memos JSONB)
LANGUAGE sql STABLE
AS $$
  SELECT
    r.run_id, r.task_description,
    1 - (r.task_embedding <=> query_embedding) AS similarity,
    EXP(-decay_lambda * EXTRACT(EPOCH FROM (now() - r.created_at)) / 86400.0) AS temporal_weight,
    (1 - (r.task_embedding <=> query_embedding))
      * EXP(-decay_lambda * EXTRACT(EPOCH FROM (now() - r.created_at)) / 86400.0) AS weighted_score,
    r.created_at, r.causal_graph, r.estimate_report, r.memos
  FROM memory_runs r
  ORDER BY weighted_score DESC
  LIMIT match_count;
$$;

CREATE OR REPLACE FUNCTION get_entity_neighborhood(
  p_entity_value TEXT, p_entity_type TEXT
)
RETURNS TABLE (source_type TEXT, source_value TEXT, relationship TEXT,
               target_type TEXT, target_value TEXT, run_id TEXT, created_at TIMESTAMPTZ)
LANGUAGE sql STABLE
AS $$
  SELECT s.entity_type, s.entity_value, e.relationship, t.entity_type, t.entity_value,
         e.source_run_id, e.created_at
  FROM memory_entity_edges e
  JOIN memory_entities s ON e.source_entity_id = s.id
  JOIN memory_entities t ON e.target_entity_id = t.id
  WHERE s.entity_value = p_entity_value AND s.entity_type = p_entity_type
  ORDER BY e.created_at DESC;
$$;
```

**Migration 3 — `enable_rls_memory_tables`:**
```sql
ALTER TABLE public.memory_runs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.memory_entities ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.memory_entity_edges ENABLE ROW LEVEL SECURITY;
```

**Migration 4 — `harden_memory_functions_and_index_fk`** *(new in this PR — see "What Got Hardened," below)*:
```sql
ALTER FUNCTION public.search_similar_runs(extensions.vector, integer, double precision)
  SET search_path = public, extensions;

ALTER FUNCTION public.get_entity_neighborhood(text, text)
  SET search_path = public, extensions;

CREATE INDEX IF NOT EXISTS memory_entity_edges_target_idx
  ON public.memory_entity_edges (target_entity_id);
```

## Row-Level Security: Enabled, Zero Policies — This Is Correct, Not a Bug

If you look at the tables in the Supabase dashboard, you'll see RLS is **enabled** on all three memory tables, but **no policies exist**. At first glance this looks incomplete — most tutorials show RLS paired immediately with policies. It is not incomplete here, and understanding exactly why requires knowing one specific piece of Postgres semantics.

**The rule:** RLS enabled + zero policies = **deny-all** for every role except the table owner and any role explicitly granted the `BYPASSRLS` attribute. There is no "default allow" fallback in Postgres RLS — the absence of a policy is itself the policy, and it means "nobody gets in."

**Why this is safe here, concretely:** the Python backend authenticates using `SUPABASE_SERVICE_ROLE_KEY`, and Supabase grants the `service_role` database role `BYPASSRLS` by default — so backend reads and writes work exactly as intended, while the anon/publishable key (used only by the frontend, and only for unrelated authentication flows elsewhere in the app) is correctly locked out of these tables entirely, with no policy needed to enforce that.

**What this concretely prevents — a specific attack scenario worth being able to name:** imagine the frontend's Supabase client library (which ships to every browser, and therefore carries only the low-privilege anon key) were ever, by accident or by a future engineer's mistake, pointed at `memory_runs` directly instead of going through the backend API. Without RLS, that browser-side code would be able to read (or worse, write) every stored investigation, embedding, and entity in the database — a direct data-exposure and data-integrity risk, reachable from client-side JavaScript. With RLS enabled and zero policies, that same request is rejected by Postgres itself, at the database layer, regardless of what the application code does or doesn't check. This is defense-in-depth: even if every other safeguard in the application layer failed, the database itself refuses the anon-key request.

**This was verified, not assumed, as part of this PR:** a direct check confirmed nothing in `app/src` queries these tables directly today — the Supabase client on the frontend is only ever used for auth (`client.ts`, `client.server.ts`, `auth-middleware.ts`). **Do not "fix" the empty-policy-list appearance by adding permissive RLS policies** unless the memory layer is ever deliberately exposed to non-backend callers — doing so would remove the exact protection described above.

## What Got Hardened (New Migration, This PR)

Supabase's own advisory linter — run as a matter of routine after any schema change, not because anything was suspected to be wrong — surfaced two real, previously-unaddressed issues:

1. **`function_search_path_mutable` (WARN, security)** on *both* RPC functions. In Postgres, a function without an explicitly pinned `search_path` resolves unqualified object names (tables, other functions) using whatever `search_path` is active for the calling session — which, in certain privilege-escalation scenarios (especially for `SECURITY DEFINER` functions, though these particular functions are not `SECURITY DEFINER`), can be manipulated by a malicious caller to make the function silently operate on a different, attacker-controlled object with the same name. Pinning `search_path` explicitly closes this class of risk regardless of caller intent. **Fixed:** both functions now have `SET search_path = public, extensions` pinned — chosen specifically (rather than an empty search path) because both functions reference unqualified table names in `public` and the `vector` type from `extensions`, so an empty search path would have broken them entirely; this is the minimal pinning that both closes the advisory and preserves correct behavior.
2. **`unindexed_foreign_keys` (INFO, performance)** — `memory_entity_edges.target_entity_id` had a foreign key with no covering index, meaning any query joining through that column (including `get_entity_neighborhood`'s own join) had to fall back to a slower lookup strategy as the table grows. **Fixed:** added `memory_entity_edges_target_idx`.

Both fixes were applied live to the project and reverified afterward: the Supabase advisories are confirmed gone (re-run directly against the live project after applying the migration), and the full test suite (22 memory tests) still passes with zero behavior change — this was a pure hardening pass, not a feature change, and that distinction was specifically verified rather than assumed.

## Retention: A Manual Query, Deliberately Not Automated

There is currently **no automatic deletion** of old `memory_runs` or `memory_entities` rows. This was a deliberate choice, not an oversight — see [[07 - Next Steps, Deferred Work & Career Takeaways]] for the full reasoning. What exists instead is a documented, copy-pasteable manual query (in the project's `CLAUDE.md`):

```sql
delete from memory_runs where created_at < now() - interval '90 days';
```

`memory_entity_edges` rows cascade-delete automatically when their parent run is deleted, by virtue of the `ON DELETE CASCADE` foreign key shown above — no separate cleanup statement is needed for edges. Orphaned entities (no edges left pointing at them after their originating run's edges cascade away) are left in place deliberately — they're a shared, cross-run knowledge graph, not scoped to any single run's lifetime, so an entity remaining in the table after its originating run is pruned is not "stale data" in any meaningful sense — it's the graph correctly retaining knowledge that outlives any one investigation. An optional, separate query exists (also documented) for anyone who *does* want to prune truly orphaned entities:

```sql
delete from memory_entities e
where not exists (
  select 1 from memory_entity_edges g
  where g.source_entity_id = e.id or g.target_entity_id = e.id
);
```

## Where to Go Next

For how the MCP server actually talks to this schema over the network, and the protocol-level testing story: [[04 - The MCP Server and Protocol Bridge]].
For the full list of what's still open around this data layer, prioritized: [[07 - Next Steps, Deferred Work & Career Takeaways]].

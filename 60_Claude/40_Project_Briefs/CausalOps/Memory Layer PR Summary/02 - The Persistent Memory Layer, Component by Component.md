---
type: project
status: complete
created: 2026-07-09
tags: [causalops, memory-layer, architecture, implementation]
---

# The Persistent Memory Layer, Component by Component

> [!info] This is the deep-dive technical note. If you need the short version first, read [[00 - Executive Summary (Meeting Prep)]].

The roadmap asked for five things. All five are implemented, tested, and verified live. This note explains each one — what it is, exactly how it's implemented (with real code), why it was built that way, and exactly how its correctness was proven rather than assumed.

## The Data Flow, End to End, Before the Component-by-Component Detail

```
NEW INCIDENT ARRIVES
        │
        ▼
 memory_retrieve_node()  ──▶  embed_text(description)  ──▶  Gemini API
        │                                                      │
        │                                                      ▼
        │                                          1536-dim embedding vector
        │                                                      │
        ▼                                                      ▼
 SupabaseMemoryStore.search_similar_runs()  ◀────────  Postgres RPC:
        │                                              search_similar_runs()
        │                                              (cosine similarity ×
        │                                               temporal decay)
        ▼
 memory_context = [ {run_id, ate, method, n_rows, similarity, ...}, ... ]
        │
        ▼
 injected into orchestrator's prompt via _format_memory_context()
        │
        ▼
 ... the rest of the investigation pipeline runs, informed by past context ...
        │
        ▼
 memory_write_node()  ──▶  embed_text(description)  ──▶  Gemini API
        │
        ▼
 SupabaseMemoryStore.write_run()
        │
        ├──▶ upsert memory_runs (run_id, embedding, causal_graph, estimate_report)
        ├──▶ extract_entities() + upsert memory_entities (deterministic, no LLM)
        └──▶ build_edges() + insert memory_entity_edges (idempotent — see below)
```

## 1. Vector Retrieval

**What it is:** every completed run's task description is turned into a numeric vector ("embedding") and stored in Postgres using the `pgvector` extension. When a new incident comes in, the system embeds *its* description and asks the database for the most similar past runs — mathematically, finding embeddings with the smallest angular distance (cosine similarity).

**The file, in full mechanics:** `src/memory/embedder.py` — one function, `embed_text(text: str) -> list[float]`:

```python
def embed_text(text: str) -> list[float]:
    client = OpenAI(
        api_key=os.environ["GEMINI_API_KEY"],
        base_url=os.environ["GEMINI_BASE_URL"],
    )
    truncated = text[:_MAX_CHARS]  # 32,000 chars
    for attempt in range(_MAX_ATTEMPTS):  # 3 attempts
        try:
            response = client.embeddings.create(
                model="gemini-embedding-001",
                input=truncated,
                dimensions=1536,
            )
            return response.data[0].embedding
        except Exception as exc:
            if attempt < _MAX_ATTEMPTS - 1:
                time.sleep(_BACKOFF_SECONDS[attempt])  # 1s, 2s, 4s
    raise last_exc
```

**Why the OpenAI Python client, calling Gemini?** Gemini exposes an OpenAI-API-compatible endpoint (`GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/`), so the standard `openai` Python package can call it directly by pointing `base_url` at Gemini instead of OpenAI's own servers — no Gemini-specific SDK is needed for this call.

**A notable implementation decision — and why it changed mid-project:** the original plan used Azure OpenAI's `text-embedding-3-small`. Azure's embedding credits were exhausted during development, so this was switched to **Gemini's `gemini-embedding-001`**, truncated to 1536 dimensions (chosen specifically to match the database column, which was already sized for that dimensionality, avoiding a schema migration). This is *independent* of which LLM handles chat/reasoning — even after the codebase later switched its primary chat model to NVIDIA Nemotron (in unrelated work), the embedder kept using Gemini directly, because `embedder.py` never routes through the shared chat-LLM client (`src/llm.py`) at all — it makes its own direct API call with its own credentials. This decoupling turned out to matter a lot when this branch had to be reconciled with the NVIDIA-backend changes — see [[05 - Reconciling With Main — The Rebase Story]].

**What "cosine similarity" actually means, concretely:** two embedding vectors are compared by the angle between them, not their raw magnitude. A similarity of `1.0` means identical direction (same meaning); `0.0` means unrelated; negative values mean opposite meaning. The Postgres RPC computes this as `1 - (embedding_a <=> embedding_b)`, where `<=>` is pgvector's own cosine-distance operator (distance is `1 - similarity`, so this converts distance back to similarity for a human-readable score).

**How correctness was proven, not assumed:** every integration test in `tests/memory/` that touches embeddings runs against the *real* Gemini API and the *real* Supabase project — there is no mocking of the embedding call anywhere in the test suite that actually exercises retrieval. This was a deliberate choice: mocking the embedding call would prove the *code path* works, but not that a real embedding actually clusters similar incidents together the way the whole feature depends on.

## 2. Knowledge Graph (Graph Traversal)

**What it is:** entities — assets, MITRE ATT&CK technique IDs, CVEs, and causal-graph node names — are extracted from every run's evidence and causal graph, and persisted as **nodes** and **edges** in three tables: `memory_entities` (the nodes) and `memory_entity_edges` (the relationships), tied back to `memory_runs` (which run created them).

**The file:** `src/memory/extractor.py` — pure Python, **zero LLM calls**, entirely deterministic regex/dict extraction. This matters: entity extraction for the memory layer follows the exact same "no LLM generates data rows" principle that governs the rest of CausalOps (see [[01 - What is CausalOps (Project Primer)]]) — an LLM never gets to invent what counts as an "asset" or a "technique." The actual extraction logic:

```python
_TECHNIQUE_RE = re.compile(r"^T\d{4}(?:\.\d{3})?$")   # e.g. T1021 or T1021.001
_CVE_RE = re.compile(r"^CVE-\d{4}-\d+$", re.IGNORECASE)

def extract_entities(run_artifact):
    pairs = set()
    for record in run_artifact.get("evidence_records") or []:
        if record.get("asset_id"):
            pairs.add(("asset", str(record["asset_id"])))
        if record.get("technique_id") and _TECHNIQUE_RE.match(str(record["technique_id"])):
            pairs.add(("technique", str(record["technique_id"])))
        if record.get("cve_id") and _CVE_RE.match(str(record["cve_id"])):
            pairs.add(("cve", str(record["cve_id"]).upper()))
    for node in (run_artifact.get("causal_graph") or {}).get("nodes") or []:
        if node.get("id"):
            pairs.add(("graph_node", str(node["id"])))
    return sorted(pairs)
```

**Two extraction rules worth knowing precisely** (because they explain behavior that can otherwise look like a bug):
- An asset↔technique edge is only created when *both* a valid `asset_id` **and** a technique ID matching the MITRE pattern (`T####` or `T####.###`) appear in the *same* evidence record. An asset mentioned without a technique produces no edge at all — this was confirmed directly during this session's own verification work: a test artifact with `technique_id: None` produced zero edges for its asset, which initially looked like a bug in a query refactor before tracing it back to this exact, correct extraction rule.
- A causal-graph edge is only created between two nodes that were *both* already extracted as entities — this is a hard FK-safety rule (see `build_edges()`'s own docstring: "entities not extracted... won't exist as rows... yet, and the edges table has FK constraints on both endpoints").

**Important scope note — "graph traversal" here means single-hop lookup, not multi-hop pathfinding.** The tool `get_entity_relationships()` (backed by the `get_entity_neighborhood` Postgres RPC) returns one entity's *direct* neighbors — it does not walk multiple hops to find indirect relationships (e.g., "what techniques are associated with assets that share a CVE with this asset" would require walking two hops, which this does not do). This matches what was actually scoped from the start; deeper traversal is listed as future work in [[07 - Next Steps, Deferred Work & Career Takeaways]].

**A real bug found and fixed during code review — the idempotency issue, in full:** the original write path built a list of edges and unconditionally inserted them:

```python
# BEFORE — buggy
if edge_rows:
    self._client.table("memory_entity_edges").insert(edge_rows).execute()
```

If `write_run()` was ever called twice for the same `run_id` (a retry, a rerun, a test), edges would double, tripling on a third call, and so on — the graph would drift from reality with every repeated write. **Fixed:**

```python
# AFTER — idempotent
self._client.table("memory_entity_edges").delete().eq(
    "source_run_id", run_id
).execute()
if edge_rows:
    self._client.table("memory_entity_edges").insert(edge_rows).execute()
```

This was verified live, not just re-run through the existing (loosely-asserting) test suite: two consecutive writes with identical input were shown to produce exactly one edge, not two, by directly querying the live table's row count after each call.

## 3. Temporal Indexing

**What it is:** similarity search doesn't just rank by textual similarity — it multiplies similarity by a **time-decay weight**, so a very similar incident from yesterday outranks an equally similar one from six months ago, without discarding the older one entirely (it still shows up, just lower in the ranking).

**The formula, and what it means concretely:** `temporal_weight = exp(-λ × age_in_days)`, with `λ = 0.023`. This gives a **30-day half-life** — solving `exp(-0.023 × t) = 0.5` for `t` gives `t ≈ 30.13` days, meaning a run's weight roughly halves every 30 days. A run from today has `temporal_weight ≈ 1.0`. A run from 30 days ago has `temporal_weight ≈ 0.5`. A run from 90 days ago has `temporal_weight ≈ 0.125` (roughly one-eighth), still present in results but ranked well below anything recent with comparable similarity.

**Where it lives:** entirely inside a Postgres function, `search_similar_runs()` (full SQL in [[03 - Supabase Schema, Migrations & Data Layer]]), not in Python — this matters for performance, since scoring happens where the data already lives rather than shipping every candidate row back to Python first. `weighted_score = similarity × temporal_weight` is what actually determines ranking, returned alongside both components separately so a caller can see *why* a result ranked where it did.

**How correctness was proven — this is one of the more interesting verification stories in this whole project:** the original implementation plan assumed testing decay math would require a raw-SQL test fixture, since the normal write path always lets Postgres default `created_at` to `now()`. That assumption turned out to be wrong. `created_at` is a completely ordinary column with no protecting trigger — a plain REST `.update()` call after the initial write backdates it just fine. This was discovered and verified *live*, before any test code was written:

```python
store.write_run({...})  # created_at defaults to now()
store._client.table("memory_runs").update(
    {"created_at": (datetime.now(UTC) - timedelta(days=30)).isoformat()}
).eq("run_id", run_id).execute()
results = store.search_similar_runs(task_description, k=1)
# results[0]["temporal_weight"] == 0.501575820192095
```

`exp(-0.023 × 30) = 0.50158...` — matching the live result to four decimal places. The formal test (`tests/memory/test_temporal_decay.py`) simply codifies this exact live-verified approach: it writes two rows with *identical* task descriptions (so their embeddings, and therefore their similarity to any query, are effectively identical), backdates one by exactly one half-life, and asserts the resulting weighted-score ratio matches `exp(-0.023 × 30)` within a small tolerance.

## 4. MCP Server

**What it is:** a standalone process exposing four tools over the **Model Context Protocol** (MCP) — the same protocol Claude Desktop and Claude Code use to give an AI agent tool access. This means Claude Code itself (or any other MCP-compatible agent) can directly query CausalOps's memory — which is exactly how several of this session's own verification steps worked, by literally calling these tools the same way a production agent would.

**The four tools**, all in `src/memory/mcp_server.py`, each a thin wrapper delegating to `SupabaseMemoryStore`:

| Tool | Signature | What it does |
|---|---|---|
| `search_similar_incidents` | `(description: str, k: int = 5)` | vector + temporal-decay search over past runs |
| `get_entity_relationships` | `(entity_value: str, entity_type: str)` | single-hop entity neighborhood lookup |
| `get_asset_timeline` | `(asset_id: str, since_days: int = 90)` | chronological edges touching one asset over a trailing window |
| `write_run_to_memory` | `(run_artifact: dict)` | embeds, upserts, and indexes a completed run |

**A critical architecture decision, stated explicitly so it doesn't get "fixed" by accident later:** this server is **never mounted inside the main FastAPI app** (`api.py`). It runs as its own process (`python -m memory.mcp_server`), reachable either over **stdio** (how Claude Desktop/Code spawn it directly, as a subprocess communicating over standard input/output — no network socket at all) or **SSE** (Server-Sent Events, an HTTP-based streaming protocol) on port 8001 for the Docker Compose deployment. This was a deliberate architecture-decision-record choice logged early in the project, and one of the real bugs fixed in this PR was exactly a violation of this boundary — see [[04 - The MCP Server and Protocol Bridge]] for the full story.

**A real deployment bug found and fixed:** the server's `__main__` block only ever read `MCP_TRANSPORT` from the environment and never passed `host`/`port` through to `mcp.run()` for the SSE case:

```python
# BEFORE — buggy: host/port never passed for non-stdio transports
if __name__ == "__main__":
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    mcp.run(transport=transport)
```

This meant the Docker Compose service's `MCP_PORT=8001` setting was silently ignored, and the server always bound to FastMCP's own default (`127.0.0.1:8000`) — making the container **completely unreachable** from the Docker host, despite `docker-compose.yml` correctly mapping port 8001 and the container appearing to start successfully. Fixed:

```python
# AFTER — fixed
if __name__ == "__main__":
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    if transport == "stdio":
        mcp.run(transport=transport)
    else:
        mcp.run(
            transport=transport,
            host=os.getenv("MCP_HOST", "0.0.0.0"),
            port=int(os.getenv("MCP_PORT", "8001")),
        )
```

Verified live with the actual running container: `curl http://localhost:8001/sse` returned `200 OK` with `content-type: text/event-stream`, and `docker ps` confirmed the container had been running and reachable for hours, not just started once and crash-looping.

## 5. Agent Integration

**What it is:** two new phases in the coordinator's execution pipeline (`src/coordinator/runner.py`):

```python
async def _run_memory_retrieve(record, store):
    """Retrieve similar past runs before the orchestrator decomposes this one.
    Memory is additive, never required: any failure here is logged and
    swallowed so a Supabase/embedding outage can't fail a CausalOps run."""
    from memory.nodes import memory_retrieve_node
    store.set_phase(record, "memory_retrieve")
    try:
        update = await memory_retrieve_node(record.to_graph_state())
        record.apply_node_update(update)
    except Exception:
        logger.exception("memory_retrieve_node failed; continuing without context")
    store.save(record)

async def _run_memory_write(record, store):
    """Persist the completed run to memory after all learning phases finish."""
    from memory.nodes import memory_write_node
    store.set_phase(record, "memory_write")
    try:
        await memory_write_node(record.to_graph_state())
    except Exception:
        logger.exception("memory_write_node failed; run result is unaffected")
    store.save(record)
```

- **`memory_retrieve`** runs before the orchestrator decomposes the incident. It retrieves the 3 most similar past runs (`_RETRIEVE_K = 3` in `memory/nodes.py`) and injects a summary into the orchestrator's prompt via `_format_memory_context()` in `agents.py`, so the LLM's decomposition is informed by what happened last time — concretely, each retrieved run is trimmed down to just what's worth putting in a prompt: `run_id`, `task_description`, `similarity`, `weighted_score`, `created_at`, and the prior `ate`/`method`/`n_rows` from its estimate report.
- **`memory_write`** runs after *every* run completes (see the important nuance below), persisting the finished run's task description, embedding, entities, and edges.

**The single most important design guarantee in this whole feature:** both phases are **non-fatal by design**, visible directly in the `try`/`except`/`logger.exception` pattern above. If Supabase is down, or the embedding API times out, the exception is logged and swallowed — a memory-layer outage can *never* fail an actual investigation. This is a deliberate reliability trade-off: memory is treated as *enhancement*, not a *dependency* the rest of the system relies on to function.

**A subtlety worth understanding precisely — this only became relevant because of the branch-reconciliation work (see [[05 - Reconciling With Main — The Rebase Story]]):** the coordinator gained a new `execution_mode` concept ("standard" vs. "deep") from unrelated work landing on `main` while this branch was in flight. The decision made here was to keep `memory_retrieve` and `memory_write` running **unconditionally, regardless of mode** — a "standard" (fast) run deserves to be remembered too, not just a "deep" one, since the whole point of memory is that *every* completed run contributes to institutional knowledge. This was a deliberate design call, not an accident of the merge, and it's worth being able to explain that reasoning directly if asked why the code doesn't just gate memory calls behind `if mode == "deep"`.

**A real bug in `_memory_configured()`, found by automated code review:**

```python
# BEFORE — buggy: any non-empty value counts as "configured"
def _memory_configured() -> bool:
    return bool(os.getenv("SUPABASE_URL")) and bool(
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    )
```

This treated *any* non-empty `SUPABASE_SERVICE_ROLE_KEY` value as configured — including `.env.example`'s own literal placeholder text, `"your-service-role-key-here"`. This meant a fresh clone that hadn't yet filled in real credentials would still *try* to make real network calls on every single run, fail, and log noisy exceptions on every investigation. Fixed to use the same placeholder-detection heuristic the test suite's own credential check already used:

```python
# AFTER — fixed, matches tests' _has_credentials() heuristic
def _memory_configured() -> bool:
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    return bool(os.getenv("SUPABASE_URL")) and bool(key) and "your-" not in key
```

## Cross-Reference: The Roadmap Sentence, Clause by Clause

| Roadmap clause | Satisfied by |
|---|---|
| "vector retrieval" | Component 1 above |
| "graph traversal" | Component 2 above (single-hop, by design) |
| "temporal indexing" | Component 3 above |
| "persistent contextual awareness across tasks" | Component 5 above |
| "longitudinal reasoning, adaptive learning, higher-order strategic coordination" | *Not a separately-built mechanism* — this is the intended **emergent effect** of the orchestrator now having access to real historical context. It is not something a unit test can assert; it's a description of expected downstream benefit, not a checklist item. Be precise about this distinction if asked in the meeting: the *infrastructure* is built and tested; whether it measurably improves reasoning over time is an open, unmeasured question. |

## Where to Go Next

For the database side of all this (exact schema, migrations, RLS decisions, full SQL): [[03 - Supabase Schema, Migrations & Data Layer]].
For the MCP protocol testing story in full: [[04 - The MCP Server and Protocol Bridge]].

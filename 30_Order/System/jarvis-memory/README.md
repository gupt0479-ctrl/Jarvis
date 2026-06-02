# jarvis-memory

The data layer for Jarvis's brain. A local SQLite registry of every vault note, exposed to AI tools as an MCP server. This is the foundation the three-month plan builds retrieval, answering, and learning on — started now as a working skeleton so the rest lands smoothly.

## What's here

| File | Role |
|---|---|
| `schema.sql` | All registry tables: notes, headings, links, chunks, conversations, enrichment_events, benchmarks. Re-runnable. |
| `registry.py` | Builds the `notes` index for real (scan → upsert) and exposes `status` / `search`. Other subsystems are stubbed with TODOs. |
| `server.py` | The MCP server. Exposes `jarvis_status`, `jarvis_search`, `jarvis_reindex` as tools. Grows by adding `@mcp.tool()` functions. |
| `registry.sqlite` | The database. Generated, **gitignored**, never committed. |

## Prerequisites

- Python 3.10+ on PATH.
- `pip install mcp` (only needed to run the MCP server, not the CLI).

## Use it as a CLI

```powershell
python registry.py index            # build / refresh the note index
python registry.py status           # counts by type, track, conversations
python registry.py search "observability"
```

## Use it as an MCP server

Wired in `.mcp.json` at the vault root as the `jarvis-memory` server (`command: python`, `args: [server.py]`, `env: JARVIS_VAULT_ROOT`). Claude Code starts it automatically. Tools today: `jarvis_status`, `jarvis_search`, `jarvis_reindex`.

## How it grows (the smooth path)

The schema already has the tables for the full plan; adding a capability means filling a table and adding one function + one MCP tool, never restructuring:

1. **Chunk index** — populate `chunks`, add `registry.chunk()`; keyword search already reads notes.
2. **Semantic search** — add embeddings to `chunks`, a hybrid ranker, and a `jarvis_semantic_search` tool. (Plan Week 5.)
3. **Graph** — populate `links` with resolved targets; add `jarvis_neighborhood` / `prerequisites`. (Week 6.)
4. **Conversation memory** — write `conversations` rows from the [[Conversation Capture]] workflow; add `jarvis_conversations`. (Week 2.)
5. **Answer engine** — add `jarvis_ask` with the citation + confidence contract over chunks + graph. (Week 7.)
6. **Benchmark** — fill `benchmarks`, add `jarvis_benchmark_run`. (Week 7+.)

Each step is additive. The registry is the single substrate; the MCP server is the single surface.

## Boundaries

- Read-heavy. The registry never edits notes — note writes go through the normal vault workflows and the Write Contract.
- The database is derived state. Delete `registry.sqlite` and `index` again any time; nothing is lost.
- Conversation raw text stays in `60_Claude/05_Clippings/AI Conversations/`; the registry only stores pointers and metadata.

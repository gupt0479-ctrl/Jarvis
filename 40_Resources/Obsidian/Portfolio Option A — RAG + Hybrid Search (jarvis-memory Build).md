---
type: evergreen
status: sprout
created: 2026-07-29
updated: 2026-07-29
tags:
  - evergreen
  - jarvis-memory
  - rag
notes:
  - "[[Jarvis OS — North Star]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[60_Claude/10_Source_Summaries/PDF Ingestion/Read/BASWE 15 AI Engineering Projects That Land Jobs (PDF)]]"
next: "Add an embeddings table to 30_Order/System/jarvis-memory/schema.sql and implement jarvis_semantic_search per North Star 5.4's Week 5 milestone"
---
# Portfolio Option A — RAG + Hybrid Search (jarvis-memory Build)
==This note lives in `40_Resources/Obsidian/` instead of the CS Portfolio project folder because it isn't a separate portfolio idea — it is [[Jarvis OS — North Star]] Part 5.4's jarvis-memory semantic-search gap, framed as BASWE's Project 6 (RAG + Hybrid Search) so the same build serves two purposes at once: a deployable portfolio project and Jarvis's own missing retrieval engine.== Source: [[PDF's Ingestion Implementation#Portfolio Projects: Pick 1-2, Build Deep - NOTED, CONSIDER|Portfolio Projects — Option A]], resolved in [[00_Execution]] as the one Portfolio project that's a genuine remaining build (Option B, Project 15 Agent Orchestration, is already shipped as CausalOps).
## Why This Is The Same Gap As jarvis-memory
`30_Order/System/jarvis-memory/server.py` is a 57-line skeleton today: `jarvis_status`, `jarvis_search`, `jarvis_reindex` are registered `@mcp.tool()` functions, but `jarvis_search`'s own docstring says "Semantic search is planned (see registry.search_text TODO and schema.sql chunks)" — it's keyword-only right now. `schema.sql` already has a `chunks` table (`note_id`, `heading_path`, `text`, `hash`, `token_estimate`) but no embeddings storage — the vector half of retrieval doesn't exist yet. This is the exact blocker named in [[Jarvis OS — North Star]] Part 5.4 and Part 6 (the token-economy retrieval engine the whole vault depends on), and it's also what's stopping `/drift` and `/emerge` from working (both need semantic clustering over vault content, per [[PDF's Ingestion Implementation#Vault Integration & Skills - REVIEW|Vault Integration & Skills]]).
**Finishing this one build closes three things at once:** the portfolio deliverable, North Star 5.4's Week 5 milestone, and the `/drift`+`/emerge` blocker.
## What To Build (BASWE Project 6 Spec)
Production RAG with dense + sparse hybrid retrieval, reranking, and grounded generation with citations — applied to this vault's own content as the corpus, not a toy dataset.
**Stack:** Python, `text-embedding-3-small` (or a local embedding model if avoiding per-query API cost matters more), ChromaDB or Qdrant for the vector store, `rank_bm25` for sparse retrieval, Claude/GPT-4o for grounded generation, FastAPI for the service layer, Docker for reproducibility.
**Differentiator:** citation verification (does the generated answer's citation actually support the claim?) plus a chunking-strategy A/B test — fixed-size-with-overlap vs. header-recursive (split on Markdown headings, which this vault's notes already have) vs. semantic chunking. Header-recursive is the obvious first candidate given how consistently this vault's notes use `##`/`###` structure per [[Jarvis Writing and Formatting]].
## Concrete Build Steps Against the Real jarvis-memory Codebase
1. **Add an `embeddings` table to `schema.sql`** — `chunk_id`, `vector` (stored as BLOB or a separate vector index file, depending on backend choice), `model`, `created_at`. Keep the `IF NOT EXISTS` pattern the rest of the schema already uses.
2. **Populate `chunks`** — `registry.py` needs a chunking pass over indexed notes using the header-recursive strategy first (matches existing note structure); write `heading_path` and `text` per chunk as the table already expects.
3. **Embed and index** — generate embeddings for each chunk, store in the vector backend (ChromaDB/Qdrant), keep BM25 index in parallel over the same chunk text (`rank_bm25` needs no separate storage — it indexes at query time or via a cached inverted index).
4. **Implement `jarvis_semantic_search` as a new `@mcp.tool()`** in `server.py` — hybrid query: run BM25 + dense retrieval in parallel, merge with reciprocal rank fusion or a simple weighted score, return top-k chunks with `heading_path` and source `path` for citation.
5. **Add a reranker pass** — a cross-encoder or Claude-as-reranker step over the merged top-k before returning results, per BASWE's spec.
6. **Wire citations into generation** — when `jarvis_ask` (North Star's Week 7 milestone) is eventually built on top of this, every generated claim must trace to a specific chunk's `path` + `heading_path`.
7. **Build the eval framework** — 50+ hand-built golden Q&A pairs against real vault content (e.g. "what does the Internship Pipeline say about Step 4?" → graded against the actual [[30_Order/Workflows/Internship Pipeline]] text), scored on faithfulness and retrieval accuracy. This is also the Portfolio Proof Requirement (deployed + evaluated + tested).
## Portfolio Proof Requirements (Don't Skip These)
Per [[PDF's Ingestion Implementation#Portfolio Projects: Pick 1-2, Build Deep - NOTED, CONSIDER|the BASWE header]]: a Loom walkthrough (problem → solution → live demo → metrics), a case study with a number (e.g. "hybrid retrieval improved answer faithfulness from X% to Y% over dense-only"), the 50+ case eval dataset, and a reproducible Docker-compose setup.
## What This Unblocks
- **`/drift`** and **`/emerge`** — both flagged in [[PDF's Ingestion Implementation#Vault Integration & Skills - REVIEW|Vault Integration & Skills]] as blocked on exactly this semantic-search capability.
- **North Star's token economy (Part 6)** — "query by meaning to find the right five notes instead of grepping fifty," the ~40% token-reduction claim North Star cites from claude-context's benchmark.
- **A second, real deployable portfolio project** alongside CausalOps (Option B), satisfying the "3 strong projects = mid-level interviews" bar from [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]].
## Failure Modes
> [!WARNING]
> Building this as a generic RAG demo over Wikipedia or an arbitrary dataset defeats the point twice over — it wouldn't close the jarvis-memory gap, and a generic RAG demo is exactly the "I called an LLM API and built a chatbot" anti-pattern BASWE warns against. The corpus has to be this vault.
> [!WARNING]
> Skipping the eval framework to ship faster removes the only way to know whether hybrid retrieval actually beats the current keyword-only `jarvis_search` — without the 50+ golden Q&A set, there's no evidence the harder build was worth it.
## Evidence
- [[Jarvis OS — North Star]] — Part 5.4 (MCP standard) and Part 6 (token economics), the roadmap this build completes
- `30_Order/System/jarvis-memory/server.py`, `schema.sql`, `registry.py` — the real codebase this note's steps apply to
- [[60_Claude/10_Source_Summaries/PDF Ingestion/Read/BASWE 15 AI Engineering Projects That Land Jobs (PDF)]] — Project 6 spec
- [[00_Execution]] — the resolved verdict this note executes

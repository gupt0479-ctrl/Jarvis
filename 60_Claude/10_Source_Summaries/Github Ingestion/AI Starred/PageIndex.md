---
type: input
status: sprout
created: 2026-05-29
tags:
  - github
  - rag
  - retrieval
  - reasoning
  - python
notes:
  - "[[40_Resources/CS/Repos]]"
---
# PageIndex — VectifyAI

**Repo:** https://github.com/VectifyAI/PageIndex
**Stars:** 32,298 | **Language:** Python | **License:** MIT
**Site:** https://pageindex.ai

## What It Is

Document Index for vectorless, reasoning-based RAG. The key claim: you don't need embeddings or vector databases. Instead, PageIndex builds a structured index of your documents using LLM reasoning, then retrieves via reasoning chains rather than semantic similarity.

## Why It Matters

Standard RAG has a core failure mode: embedding similarity doesn't always match semantic relevance for complex queries. PageIndex bypasses this by letting the LLM reason about document structure and content at index time, then use that structured index for retrieval.

## Topics

`agentic-ai`, `context-engineering`, `information-retrieval`, `llm`, `rag`, `reasoning`, `retrieval-augmented-generation`, `vector-database`

Note: listed under "vector-database" topic even though it's "vectorless" — the project emerged from frustration with vector DB limitations, not a rejection of the idea.

## When to Use vs Standard RAG

- Use PageIndex when: documents have complex structure, queries require multi-hop reasoning, or standard RAG retrieval accuracy is too low
- Use standard RAG when: high volume, low latency, simple similarity search is sufficient

## Related

- [[40_Resources/CS/Repos]] (Building section)
- [[memsearch]] — Milvus-backed memory for agents
- [[claude-context]] — MCP for codebase semantic search

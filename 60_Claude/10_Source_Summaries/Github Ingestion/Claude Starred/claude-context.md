---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - mcp
source_url: https://github.com/zilliztech/claude-context
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Claude Context (Zilliz)

**What it is:** An MCP server that indexes a codebase into a Milvus vector database and exposes semantic code search (`search_code`) to Claude Code — claimed ~40% token reduction compared to loading entire directories.

**What it actually does:** Install via `claude mcp add claude-context` with OpenAI and Zilliz Cloud credentials. Running "Index this codebase" triggers `index_codebase`, which chunks code using AST-based splitting (tree-sitter, with character-based fallback), embeds each chunk, and stores in Milvus/Zilliz Cloud. Subsequent queries use hybrid BM25 + dense vector search with RRF reranking. `get_indexing_status` shows progress percentage. Incremental re-indexing via Merkle trees — only changed files are re-embedded. Also ships a VS Code extension for the same semantic search outside of Claude.

**Why it matters for this vault/workflow:** For large codebases — say, a UROP research codebase with thousands of files — loading entire directories into Claude's context on every query is expensive and slow. Claude Context lets Claude find the 5 most relevant functions for a query out of 10,000 without reading all 10,000. It's the code equivalent of what QMD does for Jarvis's markdown notes. The ~40% token reduction claim is for equivalent retrieval quality (controlled evaluation), which is conservative — for large codebases the savings are much higher.

**How to use it:**
```bash
# Requires OpenAI API key (for embeddings) + Zilliz Cloud free tier
claude mcp add claude-context \
  -e OPENAI_API_KEY=sk-... \
  -e MILVUS_ADDRESS=your-zilliz-endpoint \
  -e MILVUS_TOKEN=your-api-key \
  -- npx @zilliz/claude-context-mcp@latest

# Then in Claude Code:
# "Index this codebase"
# "Check indexing status"
# "Find functions that handle user authentication"
```

**Failure modes / limitations:** Requires both an OpenAI API key (for embeddings) and a Zilliz Cloud account — two external dependencies. The Zilliz free tier exists but the account setup adds friction. VoyageAI and Ollama are supported as embedding alternatives to avoid the OpenAI dependency. The MCP server runs via `npx` which fetches the latest version on startup — pin a version if stability matters. The README notes that the `claude-context` package name on `main` branch has an empty README; use the `master` branch.

**Verdict:** Set up on any project where the codebase exceeds a few hundred files — the token savings compound across hundreds of queries over a project lifecycle.

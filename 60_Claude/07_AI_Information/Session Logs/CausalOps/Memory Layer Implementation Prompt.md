---
tags: [causalops, prompt, memory-layer, claude-code]
created: 2026-07-01
task: memory-layer-implementation
model: claude-sonnet-4-6
---

# Prompt — Memory Layer Implementation

> Copy this prompt verbatim into a new Claude Code session. The vault notes contain the full spec; do NOT paraphrase them here.

---

## Prompt

```
You are implementing the Persistent Semantic Memory and Retrieval Layer for the CausalOps
causal reasoning engine. Read the following notes IN FULL before writing a single line of code:

1. /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/CasualOps/Memory Layer Implementation Plan.md
2. /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/40_Project_Briefs/CausalOps/Architecture/GraphState Contract.md
3. /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/40_Project_Briefs/CausalOps/Core Modules/agents.md
4. /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/60_Claude/40_Project_Briefs/CausalOps/Core Modules/engine.md

Working directory: /home/anant_gupta/projects/hub/CausalOps/
All Python files live under src/.

---

CONSTRAINT CHANGES (updated 2026-07-01, override anything in the notes that contradicts these):

1. MCP SERVER IS STANDALONE — NOT EMBEDDED IN FASTAPI.
   - src/memory/mcp_server.py runs as its own process via `python -m memory.mcp_server`
   - api.py is NOT modified. Do not add any MCP mounting code to api.py.
   - docker-compose.yml gets a new `mcp` service (port 8001, MCP_TRANSPORT=sse)
   - The implementation plan (note 1 above, section 5.6 and 6.5) already reflects this.

2. TESTS ARE IN SCOPE — write them alongside the implementation, not after.
   - Create tests/ directory structure: tests/memory/
   - Unit tests (no credentials): test_extractor.py, test_mcp_tools.py
   - Integration tests (need real .env): test_store.py, test_nodes.py
   - The plan (section 8.5) has the exact test specifications.

3. LLM IS GEMINI (not Azure OpenAI chat). But embeddings still use Azure OpenAI.
   - GEMINI_API_KEY / GEMINI_MODEL are for the chat agents — already in the repo
   - AZURE_OPENAI_ENDPOINT / AZURE_OPENAI_API_KEY / AZURE_OPENAI_EMBEDDING_DEPLOYMENT
     are for embedder.py only. Do not use Azure for chat.

---

HARD RULES (never violate these):

- Never pass memory retrieval results as EvidenceRecord objects. Context → prompt text only.
- Never call embed_text() directly in async context. Always: await asyncio.to_thread(embed_text, text)
- Never use SUPABASE_PUBLISHABLE_KEY for Python backend writes. Use SUPABASE_SERVICE_ROLE_KEY.
- Never modify src/dataset_compiler.py or src/estimators.py. They are read-only for this task.
- Never commit .env.
- Use `from __future__ import annotations` on every new Python file.
- Ruff + Pyright must pass. Line length 88.

---

IMPLEMENTATION ORDER (do not skip steps, each is independently testable):

1. Read all 4 vault notes above. Read src/schema.py and src/graph.py from the repo too.
2. Create src/memory/__init__.py (empty)
3. Create src/memory/embedder.py — embed_text() with 3-attempt backoff, sync function
4. Create src/memory/extractor.py — extract_entities() + build_edges(), deterministic, no LLM
5. Create tests/memory/test_extractor.py — unit tests with fixture artifact
6. Create src/memory/store.py — SupabaseMemoryStore with 4 methods
7. Create src/memory/nodes.py — memory_retrieve_node + memory_write_node (async)
8. Create src/memory/mcp_server.py — standalone FastMCP with 4 tools + __main__ block
9. Create .mcp.json at repo root — stdio MCP config for Claude Code/Desktop
10. Modify src/schema.py — add run_id and memory_context fields to GraphState
11. Modify src/engine.py — add run_id to initial_state
12. Modify src/graph.py — insert memory nodes into topology
13. Modify src/agents.py — inject memory_context into orchestrator prompt
14. Modify docker-compose.yml — add mcp service
15. Add to requirements.txt: supabase==2.15.2, openai==1.91.0, fastmcp==3.2.4, httpx==0.28.1
16. Create tests/memory/test_mcp_tools.py (mock store, unit test each tool)
17. Verify: python -c "from memory.mcp_server import mcp" — no import errors
18. Verify: python -m memory.mcp_server — starts on stdio without crashing

Do NOT run integration tests (test_store.py, test_nodes.py) — those require live credentials
that are not yet in .env. Mark them with pytest.mark.integration and document how to run them.

Report back: list every file created/modified with a one-line description of what changed.
```

---

## Notes on Running This Prompt

- **Model:** claude-sonnet-4-6 hard mode (extended thinking on)
- **Session type:** Fresh Claude Code session in `/home/anant_gupta/projects/hub/CausalOps/`
- **Token budget:** ~80-120k output tokens estimated
- **Blockers before running:** `.env` must have `SUPABASE_SERVICE_ROLE_KEY` and `AZURE_OPENAI_EMBEDDING_DEPLOYMENT` for integration tests. Unit tests + implementation can proceed without credentials.
- **Do not run `/graphify` before this** — the vault notes are the spec, graphify output would be noise.

## What This Prompt Achieves

- 5 new files in `src/memory/`
- 2 new test files in `tests/memory/`
- 1 new `.mcp.json` at repo root
- 5 modified files (`schema.py`, `engine.py`, `graph.py`, `agents.py`, `docker-compose.yml`)
- 1 modified file (`requirements.txt`)
- All unit tests passing

## Related Notes

- [[Memory Layer Implementation Plan]] — full spec (vault note 1 above)
- [[Token Efficiency Notes]] — how to run efficiently on Sonnet 4.6

---
tags: [causalops, claude-code, setup, hooks, tests, commands]
created: 2026-07-01
task: claude-code-project-setup
model: claude-sonnet-4-6
---

# Prompt — CausalOps Claude Code Project Setup

> Paste this verbatim into a new Claude Code session at `/home/anant_gupta/projects/hub/CausalOps/`.
> This session does NOT implement features. It configures Claude Code for the project and writes missing tests.

---

## Prompt

```
Working directory: /home/anant_gupta/projects/hub/CausalOps/

Before doing anything else, read these files in full:
  src/memory/extractor.py
  src/memory/store.py
  src/memory/nodes.py
  src/memory/mcp_server.py
  src/coordinator/store.py         (RunRecord dataclass, _record_to_json, _record_from_json)
  tests/conftest.py
  pyproject.toml
  CLAUDE.md

Then read the directory listings for:
  tests/                           (check which test files exist)
  .claude/                         (check settings.local.json and any existing hooks)

Do not write any implementation code. Do not touch src/dataset_compiler.py or src/estimators.py
under any circumstances. The task has four parts — complete all four.

---

PART 1 — Update CLAUDE.md

The existing CLAUDE.md is stale in these specific ways. Fix each one precisely:

1. "## The Task in Progress" section says "Status: Awaiting Azure embedding deployment...
   Do NOT write implementation code until credentials are confirmed in .env."
   REPLACE the entire status note with:
   "Status: Core implementation complete. All src/memory/ files written, coordinator
   phases wired, RunRecord serialization updated, graph.py topology updated (cosmetic),
   agents.py memory_context injection done, requirements.txt and docker-compose.yml updated.
   PENDING: Supabase project provisioning (new project in org rfpztvjpxxutefsgdemv — the
   project ID glbmdbwqmuttykhicasq referenced below does not exist yet), and
   tests/memory/ test suite."

2. In component 4 (MCP Server), replace "FastMCP instance mounted at /mcp on the FastAPI
   app" with "Standalone FastMCP process — runs as python -m memory.mcp_server on port 8001.
   api.py is NOT modified. See docker-compose.yml mcp service."

5. In the repo structure comment "mcp_server.py ← FastMCP instance + 4 tools, mounted in api.py"
   change "mounted in api.py" to "standalone process, not imported by api.py"

3. Add a new "## Real Execution Path" section immediately after "## Repository Structure":

   ## Real Execution Path (Phase 2b)

   graph.py is NOT executed in production. Its own docstring says "Deprecated for execution
   in Phase 2b+." The real execution path is:

       src/coordinator/runner.py::execute_run()

   This is an async state machine that calls phases sequentially, persisting state to
   SQLite (data/runs.db) via RunRecord (src/coordinator/store.py) between each phase.

   Phase sequence:
     memory_retrieve → orchestrator → parent_evolution → parents (Kafka barrier)
     → gather_children → child_evolution → children (Kafka barrier) → evaluator
     → causal_loop (synthesis + dowhy, retries) → reasoner → policy_learning
     → memory_write → completed

   Memory phases are awaited directly (already async). All other phases use asyncio.to_thread.
   Memory phase exceptions are swallowed — a Supabase outage must never fail a run.

4. Update the "## How to Run" section:
   - Remove "curl http://localhost:8000/mcp" — there is no /mcp endpoint. The MCP server
     is a separate docker-compose service on port 8001.
   - Add:
     # Memory MCP server (standalone)
     docker-compose up mcp        # starts on port 8001
     # or directly:
     cd src && python -m memory.mcp_server

5. Remove the "## New Packages Required" section entirely — these are already in requirements.txt.

6. Fix the "## Environment Variables" section. The LLM is Gemini, not Azure GPT-4o.
   Replace the entire env block with:

   ```bash
   # Chat LLM — Gemini (NOT Azure OpenAI)
   GEMINI_API_KEY=...
   GEMINI_MODEL=gemini-2.5-flash          # or gemini-2.5-pro for high-reasoning tasks
   GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/

   # Azure OpenAI — embeddings ONLY (memory layer, not for chat)
   AZURE_OPENAI_ENDPOINT=
   AZURE_OPENAI_API_KEY=
   AZURE_OPENAI_API_VERSION=2024-08-01-preview
   AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small

   # Supabase — client (VITE_ prefix, safe in browser)
   VITE_SUPABASE_URL=https://<new-project-ref>.supabase.co   # set after provisioning
   VITE_SUPABASE_PUBLISHABLE_KEY=
   VITE_SUPABASE_PROJECT_ID=<new-project-ref>

   # Supabase — server (secrets)
   SUPABASE_URL=https://<new-project-ref>.supabase.co
   SUPABASE_PUBLISHABLE_KEY=
   SUPABASE_SERVICE_ROLE_KEY=             # REQUIRED for Python backend writes (RLS)

   # CausalOps runtime
   CAUSALOPS_ENABLE_SPAWN_WORKER=0         # "1" → in-process spawn worker (api container only)
   ```

   Remove the old `AZURE_OPENAI_DEPLOYMENT=gpt-4o` line entirely — Azure is never the chat LLM.
   Remove the "# New (needed before implementing memory layer)" comment — AZURE_OPENAI_EMBEDDING_DEPLOYMENT
   is already required, not "new".

7. Add a "## Tests" section at the bottom:

   ## Tests

   pytest tests/              # full suite (integration tests skip without credentials)
   pytest tests/ -m "not integration and not kafka"   # unit tests only, zero credentials
   pytest tests/memory/       # memory layer tests only
   pytest tests/memory/ -m integration -v             # needs SUPABASE_* + AZURE_OPENAI_* in .env

   Unit tests (no credentials): test_extractor.py, test_mcp_tools.py
   Integration tests (@pytest.mark.integration): test_store.py, test_nodes.py

---

PART 2 — Project-level hooks

Create the directory .claude/hooks/ inside the project if it doesn't exist.

Write three hook scripts:

FILE: .claude/hooks/guard-sacred-files.sh
  #!/usr/bin/env bash
  # PreToolUse guard — blocks any edit to dataset_compiler.py or estimators.py.
  # Exit 2 blocks the tool call; the message goes to Claude.
  file="${CLAUDE_FILE_PATHS:-}"
  if echo "$file" | grep -qE "(dataset_compiler|estimators)\.py"; then
    echo "BLOCKED: dataset_compiler.py and estimators.py are statistical safeguards." >&2
    echo "They must never be modified. This is enforced by project hook." >&2
    exit 2
  fi
  exit 0

FILE: .claude/hooks/lint-on-edit.sh
  #!/usr/bin/env bash
  # PostToolUse — runs ruff on any edited Python file and prints errors.
  # Never exits non-zero (PostToolUse hooks can't block, only inform).
  file="${CLAUDE_FILE_PATHS:-}"
  if echo "$file" | grep -q "\.py$"; then
    cd /home/anant_gupta/projects/hub/CausalOps
    result=$(python -m ruff check "$file" 2>&1)
    if [ -n "$result" ]; then
      echo "=== ruff $file ===" >&2
      echo "$result" >&2
    fi
  fi
  exit 0

FILE: .claude/hooks/test-memory-on-edit.sh
  #!/usr/bin/env bash
  # PostToolUse — runs memory unit tests whenever a memory/ file is edited.
  # Runs only unit tests (no integration). Never exits non-zero.
  file="${CLAUDE_FILE_PATHS:-}"
  if echo "$file" | grep -q "src/memory/\|tests/memory/"; then
    cd /home/anant_gupta/projects/hub/CausalOps
    python -m pytest tests/memory/test_extractor.py tests/memory/test_mcp_tools.py \
      -q --tb=short 2>&1 | tail -20 >&2
  fi
  exit 0

Make all three scripts executable: chmod +x .claude/hooks/*.sh

Then update .claude/settings.local.json. Read the current file first.
Add a "hooks" key to the existing JSON (keep all existing keys):

  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash /home/anant_gupta/projects/hub/CausalOps/.claude/hooks/guard-sacred-files.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash /home/anant_gupta/projects/hub/CausalOps/.claude/hooks/lint-on-edit.sh"
          },
          {
            "type": "command",
            "command": "bash /home/anant_gupta/projects/hub/CausalOps/.claude/hooks/test-memory-on-edit.sh"
          }
        ]
      }
    ]
  }

---

PART 3 — Project-level slash commands

Create directory .claude/commands/ inside the project.

Write these four command files (these are Markdown files with the command prompt as content):

FILE: .claude/commands/smoke.md
  Run the smoke test against the local stack. Execute:
  curl -s http://localhost:8000/demo/estimate | python3 -m json.tool
  If the server is not running, say so clearly. Do not start it automatically.
  A successful smoke test returns JSON with a "method" field and does not call any LLM.

FILE: .claude/commands/unit-test.md
  Run all unit tests (no integration, no Kafka). Execute from the repo root:
  python -m pytest tests/ -m "not integration and not kafka" -q --tb=short
  Report: total passed, total failed. If failures exist, show the full traceback
  for each failure. Do not fix failures automatically — report them and stop.

FILE: .claude/commands/memory-test.md
  Run the memory layer unit tests only. Execute:
  python -m pytest tests/memory/test_extractor.py tests/memory/test_mcp_tools.py -v --tb=short
  These tests require no credentials. If tests/memory/ doesn't exist, say so clearly.
  Report: passed/failed counts. Show full tracebacks on failure. Do not auto-fix.

FILE: .claude/commands/lint.md
  Run ruff and pyright on the memory layer and coordinator. Execute:
  python -m ruff check src/memory/ src/coordinator/ tests/memory/ --output-format=concise
  python -m pyright src/memory/ src/coordinator/ 2>&1 | tail -30
  Report all errors. Do not auto-fix. If no errors: say "ruff: clean. pyright: clean."

---

PART 4 — Write the missing tests

tests/memory/ does not exist. Create it with four files.

FILE: tests/memory/__init__.py  (empty)

FILE: tests/memory/test_extractor.py
Unit tests for src/memory/extractor.py. No network calls, no credentials.
Read extractor.py first to understand extract_entities() and build_edges() signatures.
Write a fixture that constructs a realistic run_artifact dict:
  - 3 evidence_records with asset_id, technique_id (T-format), and cve_id fields
  - a causal_graph dict with nodes (each having an "id") and edges (each with source/target)
Test assertions:
  - extract_entities returns all 4 entity types: asset, technique, cve, graph_node
  - extract_entities deduplicates when the same entity appears in multiple records
  - extract_entities returns sorted list of tuples
  - build_edges returns 5-tuples (src_type, src_val, relationship, tgt_type, tgt_val)
  - build_edges produces graph_node→graph_node edges for each causal graph edge
  - build_edges produces asset↔technique co-occurrence edges
  - Neither function makes any network call or imports supabase/openai
Use pytest fixtures and parametrize where it reduces repetition without obscuring intent.
No mocking of any stdlib function. These must run with: pytest tests/memory/test_extractor.py -v

FILE: tests/memory/test_mcp_tools.py
Unit tests for the four MCP tool functions in src/memory/mcp_server.py.
Read mcp_server.py first to understand the tool function signatures.
Use unittest.mock.patch to patch SupabaseMemoryStore at the point of import in mcp_server.
Test each tool independently:
  - search_similar_incidents: assert it calls store.search_similar_runs with the right args
  - get_entity_relationships: assert it calls store.get_entity_relationships correctly
  - get_asset_timeline: assert it calls store.get_asset_timeline correctly
  - write_run_to_memory: assert it calls store.write_run and returns what the store returns
Each test should verify the mock was called exactly once with expected args.
These must run with: pytest tests/memory/test_mcp_tools.py -v (no credentials needed)

FILE: tests/memory/test_store.py
Integration tests for SupabaseMemoryStore. Requires real Supabase credentials.
Mark the entire module with @pytest.mark.integration.
Add a module-level skipif:
  pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(
      not os.getenv("SUPABASE_SERVICE_ROLE_KEY"),
      reason="needs SUPABASE_SERVICE_ROLE_KEY in .env"
    ),
  ]
Tests:
  - write_run writes a record and returns {"run_id": ..., "entities_indexed": ...}
  - search_similar_runs returns a list (may be empty if no similar runs yet)
  - get_entity_relationships returns a list
  - get_asset_timeline returns a list
Use a test run_id prefix "test-" and clean up in teardown using the Supabase client directly.

FILE: tests/memory/test_nodes.py
Integration tests for memory_retrieve_node and memory_write_node.
Mark with @pytest.mark.integration + same skipif as test_store.py.
Tests:
  - memory_retrieve_node returns {"memory_context": [...]} against real Supabase
  - memory_retrieve_node returns {"memory_context": []} when SUPABASE_URL is unset
    (monkeypatch to clear the env var)
  - memory_write_node completes without error and returns {}
  - memory_write_node returns {} gracefully when SUPABASE_URL is unset
These tests call the async functions directly using asyncio.run() or pytest-asyncio.
Check pyproject.toml addopts — if asyncio mode is disabled, use asyncio.run() explicitly.

---

VERIFICATION (run after all four parts)

1. python -c "from memory.extractor import extract_entities, build_edges" in src/ — no errors
2. python -c "from memory.mcp_server import mcp" in src/ — no errors
3. python -m pytest tests/memory/test_extractor.py tests/memory/test_mcp_tools.py -v
   All tests must pass. Fix any failures before reporting done.
4. python -m ruff check src/memory/ tests/memory/ — must be clean
5. cat .claude/settings.local.json — confirm hooks are present
6. ls .claude/commands/ — confirm four command files exist
7. ls .claude/hooks/ — confirm three hook scripts exist

Report back: list every file created or modified with a one-line description.
If any test fails, show the full traceback. Do not paper over failures.
```

---

## Notes on Running This Prompt

- **Model:** claude-sonnet-4-6 (hard mode optional — tests and config don't need extended thinking)
- **Session type:** Fresh Claude Code session at `/home/anant_gupta/projects/hub/CausalOps/`
- **Estimated tokens:** 30-50k (mostly tests and CLAUDE.md rewrite)
- **No credentials needed:** Parts 1-3 and test_extractor.py / test_mcp_tools.py require nothing in .env
- **Do NOT run integration tests** — test_store.py and test_nodes.py will skip without credentials

## What This Produces

- `CLAUDE.md` — updated to reflect Phase 2b coordinator reality + memory layer status
- `.claude/hooks/guard-sacred-files.sh` — blocks edits to dataset_compiler.py / estimators.py
- `.claude/hooks/lint-on-edit.sh` — ruff on every Python edit
- `.claude/hooks/test-memory-on-edit.sh` — runs memory unit tests on memory/ edits
- `.claude/settings.local.json` — hooks wired in
- `.claude/commands/smoke.md` — `/smoke` slash command
- `.claude/commands/unit-test.md` — `/unit-test` slash command
- `.claude/commands/memory-test.md` — `/memory-test` slash command
- `.claude/commands/lint.md` — `/lint` slash command
- `tests/memory/__init__.py`
- `tests/memory/test_extractor.py` — unit, no credentials
- `tests/memory/test_mcp_tools.py` — unit, no credentials
- `tests/memory/test_store.py` — integration, skips without Supabase
- `tests/memory/test_nodes.py` — integration, skips without Supabase

## Why Each Part Matters

| Part | Purpose |
|------|---------|
| CLAUDE.md update | Every future session reads this first — stale content = wrong decisions |
| guard-sacred-files hook | Forces Claude to ask before touching statistical core; can't be bypassed |
| lint-on-edit hook | Ruff errors surface immediately instead of accumulating |
| test-memory-on-edit hook | Memory unit tests run on every memory/ edit; regressions are caught immediately |
| Slash commands | One-word invocations for the most frequent dev operations |
| test_extractor.py | Validates entity extraction + edge building without any credentials |
| test_mcp_tools.py | Validates MCP tool delegation logic without live Supabase |
| test_store.py | Full write/read integration test — runs after Supabase is provisioned |
| test_nodes.py | End-to-end async node test — validates the coordinator integration point |

## Related Notes

- [[Memory Layer Implementation Prompt]] — the implementation prompt (already run)
- [[Memory Layer Implementation Plan]] — the full spec (vault note at 20_Progress)
- [[Token Efficiency Notes]] — how to run Claude Code sessions efficiently

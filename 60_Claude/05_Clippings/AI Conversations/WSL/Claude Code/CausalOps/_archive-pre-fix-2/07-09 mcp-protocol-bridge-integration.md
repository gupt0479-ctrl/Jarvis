---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: wsl
title: "mcp-protocol-bridge-integration"
started_at: 2026-07-09T07:21:55
ended_at: 2026-07-09T07:34:44
duration_minutes: 13
exported_at: 2026-07-30T15:28:59.6972445+04:00
project: CausalOps
cwd: '/home/anant_gupta/projects/hub/CausalOps'
session_id: a5ffba60-907c-437b-b8c4-6fe1e97014bf
status: raw
turn_count: 4
tools_used:
  Agent: 1
  Bash: 11
  Edit: 4
  ExitPlanMode: 1
  Read: 3
  TaskCreate: 6
  TaskUpdate: 8
  ToolSearch: 2
  Write: 2
tokens:
  input: 41009
  output: 31720
  cache_creation: 203521
  cache_read: 5519405
  total: 5795655
cost_usd: 2.317183
model:
  - claude-sonnet-5
files_touched:
  - "/home/anant_gupta/.claude/plans/05-mcp-dapper-abelson.md"
  - "/home/anant_gupta/projects/hub/CausalOps/tests/memory/test_mcp_tools.py"
  - "/home/anant_gupta/projects/hub/CausalOps/tests/memory/test_mcp_bridge.py"
  - "/home/anant_gupta/projects/hub/CausalOps/CLAUDE.md"
  - "/home/anant_gupta/projects/hub/CausalOps/.gitignore"
tags:
  - input
  - ai-conversation
  - claude-code
  - wsl
---

# mcp-protocol-bridge-integration

## You


# 05 — MCP Protocol Bridge Integration Test and Final Housekeeping

> Prompts 1-4 (now in `claude code/ran/`) closed the coordinator-level memory round trip and doc/schema drift. This prompt closes the one real gap they left: nothing in the repo actually drives the MCP server through the MCP protocol itself. It also cleans up two small nits caught while re-verifying prompts 1-4 against the live repo this session.

## Why This Exists

`tests/memory/test_mcp_tools.py` mocks `SupabaseMemoryStore` and calls the tool
*functions* directly (`mcp_server.search_similar_incidents("...", k=2)`). That
proves the functions delegate correctly. It does **not** prove the MCP server
works as an MCP server — no test ever opens a real client session, lists tools
through the protocol, or calls a tool the way Claude Code/Claude Desktop
actually would (JSON-RPC-style tool invocation, argument validation against
the tool's schema, structured content serialized back). That is the literal
meaning of "integration test for the MCP bridge," and it's currently zero.

This was verified directly this session, live, before writing this prompt —
not assumed:

```python
import asyncio
from fastmcp import Client
from memory import mcp_server

async def main():
    async with Client(mcp_server.mcp) as client:
        tools = await client.list_tools()
        print([t.name for t in tools])
        # -> ['search_similar_incidents', 'get_entity_relationships',
        #     'get_asset_timeline', 'write_run_to_memory']
        result = await client.call_tool("search_similar_incidents", {...})
        result.data  # -> the tool's return value, already deserialized

asyncio.run(main())
```

`Client(mcp_server.mcp)` — passing the live `FastMCP` object directly, not a
URL — makes `fastmcp` infer an in-memory `FastMCPTransport`. No Docker, no
network hop, no subprocess. It still goes through the real protocol layer
(tool discovery, schema validation, request/response serialization); it just
skips the SSE wire transport, which prompt 1 already proved works separately
(`curl http://localhost:8001/sse` → `200 OK`, verified live this session).

A second, live version of the same pattern was also run this session against
the real Supabase project (write_run_to_memory → search_similar_incidents
through the real `Client`, then cleaned up) and worked end to end. This
prompt's acceptance criteria reuse that exact, already-proven shape — there is
no unverified design decision left in this prompt.

## Hard Rules

- The project disables the pytest-asyncio plugin (`pyproject.toml`:
  `addopts = "... -p no:asyncio"`). Every test that awaits the `Client` must be
  a plain `def test_...()` that wraps an inner `async def` and calls it with
  `asyncio.run(...)` — the same pattern already used in
  `tests/memory/test_end_to_end.py`. Do NOT write `async def test_...` — it
  will silently not run as a coroutine under this config.
- Do not touch `dataset_compiler.py` or `estimators.py`.
- Do not modify `tests/memory/test_end_to_end.py`, `test_store.py`,
  `test_nodes.py`, or `test_extractor.py` — this prompt is additive only.
- Do not add temporal-decay math verification or a memory-row retention/
  deletion strategy. Both are real, already-identified gaps (see
  `claude code/ran/00 - Memory Layer Completion — Index.md`, "Caught While
  Verifying" section, and `Memory Layer Implementation Plan.md` section 11,
  "Open Questions — Not Blocking") but neither is in scope here. Flag them
  back if you think they need their own prompt; do not implement them now.
- Do not touch the pre-existing `tsc --noEmit` errors in
  `SpatiotemporalKGPanel.client.tsx` or `causalops-api.ts` — confirmed this
  session to be unrelated to the memory layer's `types.ts` regeneration
  (they don't reference `memory_runs`/`memory_entities`/`memory_entity_edges`
  at all). Out of scope.

## Task 1 — Protocol-level unit tests (no credentials)

Add to `tests/memory/test_mcp_tools.py` (do not create a new file for this
part — it belongs with the existing mocked-store tool tests):

```python
import asyncio

from fastmcp import Client


def test_list_tools_exposes_all_four_tools() -> None:
    async def _list() -> list[str]:
        async with Client(mcp_server.mcp) as client:
            tools = await client.list_tools()
            return [tool.name for tool in tools]

    names = asyncio.run(_list())
    assert set(names) == {
        "search_similar_incidents",
        "get_entity_relationships",
        "get_asset_timeline",
        "write_run_to_memory",
    }


def test_search_similar_incidents_round_trips_through_mcp_protocol() -> None:
    mock_store = MagicMock()
    mock_store.search_similar_runs.return_value = [
        {"run_id": "run-1", "similarity": 0.9}
    ]

    async def _call() -> list[dict]:
        with patch.object(mcp_server, "SupabaseMemoryStore", return_value=mock_store):
            async with Client(mcp_server.mcp) as client:
                result = await client.call_tool(
                    "search_similar_incidents",
                    {"description": "lateral movement", "k": 2},
                )
                return result.data

    data = asyncio.run(_call())
    mock_store.search_similar_runs.assert_called_once_with("lateral movement", k=2)
    assert data == [{"run_id": "run-1", "similarity": 0.9}]
```

`MagicMock`, `patch`, and `mcp_server` are already imported at the top of this
file — only the `asyncio` import and `from fastmcp import Client` need adding.
This deliberately reuses the mocked-store pattern already in the file; the
new part is going through `Client(...)`/`call_tool(...)` instead of calling
`mcp_server.search_similar_incidents(...)` directly, so it actually exercises
tool registration and the protocol's argument/response marshaling.

## Task 2 — Live MCP bridge round trip (integration)

Create `tests/memory/test_mcp_bridge.py`:

```python
"""Live round-trip test through the actual MCP protocol layer.

`tests/memory/test_mcp_tools.py` mocks ``SupabaseMemoryStore`` and never opens
a real client session — it proves the tool wrappers delegate correctly, not
that the MCP bridge itself works end to end. This test opens a real
``fastmcp.Client`` session against the live ``mcp`` server object (in-memory
transport — no Docker, no network hop, but the same protocol layer prompt 1's
``curl http://localhost:8001/sse`` check exercises over SSE) and calls
``write_run_to_memory`` then ``search_similar_incidents`` exactly as an MCP
client (Claude Code, Claude Desktop) would, against the real Supabase
project. Skipped automatically unless real Supabase credentials are
configured — see ``tests/memory/test_store.py`` for the same pattern. Run
with:

    pytest tests/memory/test_mcp_bridge.py -v -m integration
"""

from __future__ import annotations

import asyncio
import os
import uuid

import pytest
from fastmcp import Client

from memory import mcp_server
from memory.store import SupabaseMemoryStore

pytestmark = pytest.mark.integration

_SKIP_REASON = "Real Supabase credentials not configured in .env"


def _has_credentials() -> bool:
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    return bool(os.getenv("SUPABASE_URL")) and bool(key) and "your-" not in key


requires_credentials = pytest.mark.skipif(not _has_credentials(), reason=_SKIP_REASON)


@pytest.fixture
def tagged_run():
    tag = f"mcp-bridge-{uuid.uuid4().hex[:8]}"
    run_id = f"{tag}-run-1"
    yield {"tag": tag, "run_id": run_id}
    store = SupabaseMemoryStore()
    store._client.table("memory_entity_edges").delete().eq(
        "source_run_id", run_id
    ).execute()
    store._client.table("memory_runs").delete().eq("run_id", run_id).execute()
    store._client.table("memory_entities").delete().like(
        "entity_value", f"{tag}%"
    ).execute()


@requires_credentials
def test_write_then_search_round_trips_through_real_mcp_client(tagged_run) -> None:
    tag = tagged_run["tag"]
    run_id = tagged_run["run_id"]
    task_description = f"Incident {tag}: MCP bridge protocol round trip"

    async def _round_trip() -> tuple[dict, list[dict]]:
        async with Client(mcp_server.mcp) as client:
            write_result = await client.call_tool(
                "write_run_to_memory",
                {
                    "run_artifact": {
                        "run_id": run_id,
                        "task_description": task_description,
                        "memos": [],
                        "causal_graph": {},
                        "causal_estimate_report": {},
                    }
                },
            )
            search_result = await client.call_tool(
                "search_similar_incidents",
                {"description": task_description, "k": 3},
            )
            return write_result.data, search_result.data

    write_data, search_data = asyncio.run(_round_trip())

    assert write_data["run_id"] == run_id
    assert any(row.get("run_id") == run_id for row in search_data)
```

This exact shape (fixture, tagging, teardown, assertions) was run live this
session against the real Supabase project and passed — you are implementing a
proven design, not inventing one. Do not simplify away the tagging/cleanup —
it is what keeps repeated runs of this test from polluting the live
`memory_runs`/`memory_entities` tables.

## Task 3 — Two small housekeeping fixes

1. **`CLAUDE.md`** — the "Status" paragraph currently ends with a bare
   Obsidian wikilink that means nothing outside the Jarvis vault:
   ```
   Integration test status is tracked separately — see [[03 - End-to-End Memory Verification and Integration Gate]].
   ```
   Replace it with plain text. Run the full memory suite first
   (`set -a && source .env && set +a && pytest tests/memory/ -v`), then write
   a sentence that states the *actual* result of that run (e.g. which files
   pass, whether the MCP bridge round trip passes) — do not hardcode a
   "PASSING" claim without having just run it in this same session.

2. **`.gitignore`** — add a `supabase/` entry. Running
   `npx supabase gen types typescript --project-id ...` (as prompt 2 did)
   creates `supabase/.temp/` (CLI link-cache — a project ref and org ID, no
   secrets) as an untracked, un-ignored directory. Add it near the existing
   `.env`/`data/` entries so it doesn't get committed by accident later.

## What NOT to Do

- Don't re-run the SQL migration or re-verify RLS policy decisions — already
  settled (see `claude code/ran/00 - Memory Layer Completion — Index.md`).
- Don't re-litigate whether the MCP server should be Docker/SSE vs
  stdio-only — prompt 1 already fixed and live-verified the Docker/SSE path
  (`causalops-mcp-1` container, confirmed running, `curl` returns
  `200 OK` + `text/event-stream`, clean logs).
- Don't touch `src/memory/mcp_server.py`'s tool implementations, `store.py`,
  `embedder.py`, or `extractor.py` — this prompt is test coverage and
  documentation only.
- Don't run `pytest tests/memory -m integration` from a tool-sandboxed shell
  and trust a hang as a pass or fail — run it from a real terminal, and
  always `set -a && source .env && set +a` first in the same shell
  invocation, or the test will silently **skip** rather than run, and a skip
  is not a pass.

## Acceptance Criteria

1. `pytest tests/memory/test_mcp_tools.py -v` — all pass, zero credentials
   needed, includes the two new protocol-level tests.
2. `set -a && source .env && set +a && pytest tests/memory/test_mcp_bridge.py -v -m integration`
   — must show `1 passed`, not skipped. If it skips, credentials didn't reach
   the process — stop and say so, don't report this done.
3. `set -a && source .env && set +a && pytest tests/memory/ -v` — full memory
   suite, all pass, zero skips anywhere under `tests/memory/`. Paste the
   final summary line.
4. `pytest tests/ -m "not integration and not kafka"` — confirm no
   regression in the rest of the suite (was 88 passed before this prompt).
5. `ruff check tests/memory/test_mcp_tools.py tests/memory/test_mcp_bridge.py`
   and `pyright tests/memory/test_mcp_bridge.py` — both clean.
6. Post-teardown check: after the integration test runs, directly query
   `memory_runs`/`memory_entity_edges`/`memory_entities` (via
   `SupabaseMemoryStore()._client...`) for the tagged run/entity values and
   confirm nothing remains — prove cleanup actually worked, don't just trust
   the fixture code path.
7. `git diff CLAUDE.md` shows only the wikilink line replaced, nothing else
   changed. `git diff .gitignore` shows only the added `supabase/` line.

## Related Notes

- `claude code/ran/00 - Memory Layer Completion — Index.md` — prompts 1-4,
  now archived, that this prompt follows on from.
- `claude code/ran/03 - End-to-End Memory Verification and Integration Gate.md`
  — the coordinator-level round trip this prompt's Task 2 complements (that
  one proves the coordinator ↔ Supabase loop; this one proves the MCP client
  ↔ server protocol loop — together they cover the whole memory layer's
  external surface).
- `Memory Layer Implementation Plan.md` section 11 ("Open Questions — Not
  Blocking") — where the deferred temporal-decay-verification and
  retention-strategy items are tracked for whenever they get picked up.


## Claude

I've launched an Explore agent to gather the exact current contents of the relevant test files, mcp_server.py, store.py, pyproject.toml, .gitignore, and CLAUDE.md. I'll wait for it to finish before drafting the plan.

**Tool calls:**

- `Agent` — `{"description":"Explore memory test files and configs","prompt":"I'm preparing an implementation plan for a task that adds MCP protocol-level integration tests to a CausalOps repo's memory layer. I need you to gather exact current file contents/state (read-only) so the plan can be precise. Report back with the actual content (not paraphrased) for these:\n\n1. Full content of `tests/memory/test_mcp_tools.py` — especially the imports at the top (need to know if `MagicMock`, `patch`, `mcp_server` are already imported, and what `from memory import mcp_server` or similar import looks like).\n2. Full content of `src/memory/mcp_server.py` — specifically the four tool function signatures (`search_similar_incidents`, `get_entity_relationships`, `get_asset_timeline`, `write_run_to_memory`) and how `SupabaseMemoryStore` is imported/referenced (is it `from memory.store import SupabaseMemoryStore` at module level, referenced as `mcp_server.SupabaseMemoryStore`?).\n3. Full content of `src/memory/store.py` — specifically the `SupabaseMemoryStore` class: constructor, the `_client` attribute name (confirm it's literally `_client`), and method signatures for `search_similar_runs` and any write method (confirm name matches `write_run_to_memory` tool's internal call).\n4. Full content of `tests/memory/test_end_to_end.py` — this is the reference pattern for async test wrapping (`asyncio.run` inside a plain `def test_...()`), fixture/teardown/tagging pattern, and credential-check helper (`_has_credentials` or similar).\n5. Full content of `tests/memory/test_store.py` — to see the `@pytest.mark.integration` skip pattern used there.\n6. Full content of `pyproject.toml` — confirm the `addopts = \"... -p no:asyncio\"` line and the `markers` section defining `integration` and `kafka` markers, and confirm `fastmcp` is a listed dependency.\n7. Current full content of `.gitignore`.\n8. The relevant paragraph in `CLAUDE.md` at repo root (`/home/anant_gupta/projects/hub/CausalOps/CLAUDE.md`) — the exact line: \"Integration test status is tracked separately — see [[03 - End-to-End Memory Verification and Integration Gate]].\" — and 3-4 lines of surrounding context (the whole \"Status:\" paragraph it's part of).\n9. Check whether `fastmcp` is importable / installed (e.g. check requirements.txt, pyproject.toml dependencies, or a venv) — just report what dependency files say, don't try to import it.\n10. Confirm whether `RunArtifact` or similar schema referenced in the `write_run_to_memory` tool call payload (`run_id`, `task_description`, `memos`, `causal_graph`, `causal_estimate_report`) matches the actual expected input schema for that tool in mcp_server.py — report the exact Pydantic model / parameter signature used.\n\nReport everything verbatim with file paths and line numbers. This is pure research — do not modify any files.","subagent_type":"Explore"}`

## You

<task-notification>
<task-id>aadfa6f5a92aa6e04</task-id>
<tool-use-id>[REDACTED]</tool-use-id>
<output-file>/tmp/claude-1001/-home-anant-gupta-projects-hub-CausalOps/[REDACTED]/tasks/aadfa6f5a92aa6e04.output</output-file>
<status>completed</status>
<summary>Agent "Explore memory test files and configs" finished</summary>
<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>
<result>All requested files have been read. Here is the verbatim report.

## 1. `tests/memory/test_mcp_tools.py` (55 lines, full content)

```python
1	"""Unit tests for the standalone MCP server's tool wrappers.
2	
3	The store is fully mocked — no Supabase or Azure calls happen here.
4	"""
5	
6	from __future__ import annotations
7	
8	from unittest.mock import MagicMock, patch
9	
10	from memory import mcp_server
11	
12	
13	def test_search_similar_incidents_delegates_to_store() -&gt; None:
14	    mock_store = MagicMock()
15	    mock_store.search_similar_runs.return_value = [{"run_id": "run-1"}]
16	
17	    with patch.object(mcp_server, "SupabaseMemoryStore", return_value=mock_store):
18	        result = mcp_server.search_similar_incidents("lateral movement", k=2)
19	
20	    mock_store.search_similar_runs.assert_called_once_with("lateral movement", k=2)
21	    assert result == [{"run_id": "run-1"}]
22	
23	
24	def test_get_entity_relationships_delegates_to_store() -&gt; None:
25	    mock_store = MagicMock()
26	    mock_store.get_entity_relationships.return_value = [{"relationship": "causes"}]
27	
28	    with patch.object(mcp_server, "SupabaseMemoryStore", return_value=mock_store):
29	        result = mcp_server.get_entity_relationships("host-01", "asset")
30	
31	    mock_store.get_entity_relationships.assert_called_once_with("host-01", "asset")
32	    assert result == [{"relationship": "causes"}]
33	
34	
35	def test_get_asset_timeline_delegates_to_store() -&gt; None:
36	    mock_store = MagicMock()
37	    mock_store.get_asset_timeline.return_value = [{"created_at": "2026-01-01"}]
38	
39	    with patch.object(mcp_server, "SupabaseMemoryStore", return_value=mock_store):
40	        result = mcp_server.get_asset_timeline("host-01", since_days=30)
41	
42	    mock_store.get_asset_timeline.assert_called_once_with("host-01", since_days=30)
43	    assert result == [{"created_at": "2026-01-01"}]
44	
45	
46	def test_write_run_to_memory_delegates_to_store() -&gt; None:
47	    mock_store = MagicMock()
48	    mock_store.write_run.return_value = {"run_id": "run-1", "entities_indexed": 3}
49	    artifact = {"run_id": "run-1", "task_description": "test"}
50	
51	    with patch.object(mcp_server, "SupabaseMemoryStore", return_value=mock_store):
52	        result = mcp_server.write_run_to_memory(artifact)
53	
54	    mock_store.write_run.assert_called_once_with(artifact)
55	    assert result == {"run_id": "run-1", "entities_indexed": 3}
```

Key facts for planning: `MagicMock`, `patch` already imported (line 8). `mcp_server` imported via `from memory import mcp_server` (line 10) — module-level import, tools/store accessed as `mcp_server.search_similar_incidents(...)` and patched via `patch.object(mcp_server, "SupabaseMemoryStore", ...)`. No `pytest`, `pytest.mark.integration`, or `asyncio` import — this file is pure unit-test style, synchronous.

## 2. `src/memory/mcp_server.py` (79 lines, full content)

```python
1	"""Standalone MCP server exposing the CausalOps memory layer.
2	
3	Runs as its own process — ``python -m memory.mcp_server`` — on stdio
4	(Claude Desktop/Code) or SSE (docker, HTTP clients) depending on
5	``MCP_TRANSPORT``. Never mounted inside the FastAPI app in api.py.
6	"""
7	
8	from __future__ import annotations
9	
10	import os
11	from typing import Any
12	
13	from fastmcp import FastMCP
14	
15	from memory.store import SupabaseMemoryStore
16	
17	mcp = FastMCP(
18	    "causalops-memory",
19	    instructions=(
20	        "CausalOps persistent memory server. Use search_similar_incidents to "
21	        "retrieve context before starting a run. Use write_run_to_memory "
22	        "after DoWhy completes."
23	    ),
24	)
25	
26	
27	@mcp.tool()
28	def search_similar_incidents(description: str, k: int = 5) -&gt; list[dict[str, Any]]:
29	    """Search past CausalOps runs similar to the given incident description.
30	
31	    Returns ranked results with similarity score, temporal weight, and a
32	    summary of the causal graph and estimate report from each past run.
33	    """
34	
35	    return SupabaseMemoryStore().search_similar_runs(description, k=k)
36	
37	
38	@mcp.tool()
39	def get_entity_relationships(
40	    entity_value: str, entity_type: str
41	) -&gt; list[dict[str, Any]]:
42	    """Get all known relationships for an entity.
43	
44	    ``entity_type`` is one of: asset, technique, cve, graph_node. Returns
45	    edges with source, relationship type, target, and source run ID.
46	    """
47	
48	    return SupabaseMemoryStore().get_entity_relationships(entity_value, entity_type)
49	
50	
51	@mcp.tool()
52	def get_asset_timeline(asset_id: str, since_days: int = 90) -&gt; list[dict[str, Any]]:
53	    """Get the chronological event timeline for an asset over the past N days."""
54	
55	    return SupabaseMemoryStore().get_asset_timeline(asset_id, since_days=since_days)
56	
57	
58	@mcp.tool()
59	def write_run_to_memory(run_artifact: dict[str, Any]) -&gt; dict[str, Any]:
60	    """Store a completed CausalOps run in the memory layer.
61	
62	    Embeds the task description, indexes entities, and builds knowledge
63	    graph edges. Returns ``{"run_id": str, "entities_indexed": int}``.
64	    """
65	
66	    return SupabaseMemoryStore().write_run(run_artifact)
67	
68	
69	if __name__ == "__main__":
70	    transport = os.getenv("MCP_TRANSPORT", "stdio")
71	    if transport == "stdio":
72	        mcp.run(transport=transport)  # type: ignore[arg-type]
73	    else:
74	        mcp.run(
75	            transport=transport,  # type: ignore[arg-type]
76	            host=os.getenv("MCP_HOST", "0.0.0.0"),
77	            port=int(os.getenv("MCP_PORT", "8001")),
78	        )
```

Key facts: `SupabaseMemoryStore` is imported at module level (line 15: `from memory.store import SupabaseMemoryStore`), and each tool function instantiates it fresh inline (`SupabaseMemoryStore()`) rather than referencing a module-level singleton. Since it's imported into the `mcp_server` module namespace, `patch.object(mcp_server, "SupabaseMemoryStore", ...)` (as used in test_mcp_tools.py) works correctly. The `mcp` object is a module-level `FastMCP("causalops-memory", instructions=...)` instance (lines 17-24) — this is what a protocol-level MCP test would need to interact with (e.g., via `fastmcp.Client(mcp)` in-memory transport) rather than the raw Python functions.

Tool signatures:
- `search_similar_incidents(description: str, k: int = 5) -&gt; list[dict[str, Any]]`
- `get_entity_relationships(entity_value: str, entity_type: str) -&gt; list[dict[str, Any]]`
- `get_asset_timeline(asset_id: str, since_days: int = 90) -&gt; list[dict[str, Any]]`
- `write_run_to_memory(run_artifact: dict[str, Any]) -&gt; dict[str, Any]`

Note: all four are decorated with `@mcp.tool()` — calling `mcp_server.search_similar_incidents(...)` directly in the existing unit test bypasses the FastMCP tool wrapper's argument validation/coercion entirely (it calls the plain underlying Python function, not through the MCP protocol/JSON-RPC layer). This is exactly the gap that protocol-level integration tests would need to close — they'd need to go through `mcp.tool()` / `fastmcp.Client` machinery to exercise the actual MCP JSON schema, not just Python-call the function.

## 3. `src/memory/store.py` (176 lines, full content)

```python
1	"""Supabase-backed persistence for the CausalOps memory layer.
2	
3	Pure Python, no HTTP framework here. Always uses the service_role key —
4	never the anon/publishable key, which is blocked from writing by RLS.
5	"""
6	
7	from __future__ import annotations
8	
9	import logging
10	import os
11	from datetime import UTC, datetime, timedelta
12	from typing import Any
13	
14	from supabase import Client, create_client
15	
16	from memory.embedder import embed_text
17	from memory.extractor import build_edges, extract_entities
18	
19	logger = logging.getLogger(__name__)
20	
21	
22	def _as_rows(data: Any) -&gt; list[dict[str, Any]]:
23	    """Narrow the Supabase client's loosely-typed response payload."""
24	
25	    if not isinstance(data, list):
26	        return []
27	    return [row for row in data if isinstance(row, dict)]
28	
29	
30	class SupabaseMemoryStore:
31	    """Read/write interface for the memory_runs/memory_entities/edges tables."""
32	
33	    def __init__(self) -&gt; None:
34	        url = os.environ["SUPABASE_URL"]
35	        key = os.environ["SUPABASE_SERVICE_ROLE_KEY"]
36	        self._client: Client = create_client(url, key)
37	
38	    def write_run(self, run_artifact: dict[str, Any]) -&gt; dict[str, Any]:
39	        """Embed the task, upsert the run, then index its entities and edges.
40	
41	        Raises on failure — unlike the read methods, callers need to know
42	        when a write did not happen.
43	        """
44	
45	        run_id = run_artifact["run_id"]
46	        task_description = run_artifact.get("task_description") or ""
47	        embedding = embed_text(task_description)
48	
49	        self._client.table("memory_runs").upsert(
50	            {
51	                "run_id": run_id,
52	                "task_description": task_description,
53	                "task_embedding": embedding,
54	                "memos": run_artifact.get("memos") or [],
55	                "causal_graph": run_artifact.get("causal_graph") or {},
56	                "estimate_report": run_artifact.get("causal_estimate_report") or {},
57	            },
58	            on_conflict="run_id",
59	        ).execute()
60	
61	        entity_pairs = extract_entities(run_artifact)
62	        entity_ids = self._upsert_entities(entity_pairs)
63	
64	        edge_rows = []
65	        for src_type, src_val, relationship, tgt_type, tgt_val in build_edges(
66	            run_artifact, entity_pairs
67	        ):
68	            source_id = entity_ids.get((src_type, src_val))
69	            target_id = entity_ids.get((tgt_type, tgt_val))
70	            if not source_id or not target_id:
71	                continue
72	            edge_rows.append(
73	                {
74	                    "source_entity_id": source_id,
75	                    "target_entity_id": target_id,
76	                    "relationship": relationship,
77	                    "source_run_id": run_id,
78	                }
79	            )
80	        if edge_rows:
81	            self._client.table("memory_entity_edges").insert(edge_rows).execute()
82	
83	        return {"run_id": run_id, "entities_indexed": len(entity_pairs)}
84	
85	    def search_similar_runs(
86	        self, task_description: str, k: int = 5
87	    ) -&gt; list[dict[str, Any]]:
88	        """Vector-similarity + temporal-decay search over past runs."""
89	
90	        try:
91	            embedding = embed_text(task_description)
92	            response = self._client.rpc(
93	                "search_similar_runs",
94	                {"query_embedding": embedding, "match_count": k},
95	            ).execute()
96	            return _as_rows(response.data)
97	        except Exception:
98	            logger.exception("search_similar_runs failed; returning empty results")
99	            return []
100	
101	    def get_entity_relationships(
102	        self, entity_value: str, entity_type: str
103	    ) -&gt; list[dict[str, Any]]:
104	        """Graph traversal for one entity's known relationships."""
105	
106	        try:
107	            response = self._client.rpc(
108	                "get_entity_neighborhood",
109	                {"p_entity_value": entity_value, "p_entity_type": entity_type},
110	            ).execute()
111	            return _as_rows(response.data)
112	        except Exception:
113	            logger.exception(
114	                "get_entity_relationships failed for %s/%s", entity_type, entity_value
115	            )
116	            return []
117	
118	    def get_asset_timeline(
119	        self, asset_id: str, since_days: int = 90
120	    ) -&gt; list[dict[str, Any]]:
121	        """Chronological edges touching one asset over the trailing window."""
122	
123	        try:
124	            cutoff = (datetime.now(UTC) - timedelta(days=since_days)).isoformat()
125	            response = (
126	                self._client.table("memory_entity_edges")
127	                .select(
128	                    "*, source_entity:source_entity_id(*), "
129	                    "target_entity:target_entity_id(*)"
130	                )
131	                .gte("created_at", cutoff)
132	                .order("created_at")
133	                .execute()
134	            )
135	            rows = _as_rows(response.data)
136	            return [row for row in rows if _touches_asset(row, asset_id)]
137	        except Exception:
138	            logger.exception("get_asset_timeline failed for asset %s", asset_id)
139	            return []
140	
141	    def _upsert_entities(
142	        self, entity_pairs: list[tuple[str, str]]
143	    ) -&gt; dict[tuple[str, str], str]:
144	        if not entity_pairs:
145	            return {}
146	        now = datetime.now(UTC).isoformat()
147	        rows = [
148	            {"entity_type": entity_type, "entity_value": entity_value, "last_seen": now}
149	            for entity_type, entity_value in entity_pairs
150	        ]
151	        response = (
152	            self._client.table("memory_entities")
153	            .upsert(rows, on_conflict="entity_type,entity_value")
154	            .execute()
155	        )
156	        entity_ids: dict[tuple[str, str], str] = {}
157	        for row in _as_rows(response.data):
158	            entity_type = row.get("entity_type")
159	            entity_value = row.get("entity_value")
160	            entity_id = row.get("id")
161	            if entity_type and entity_value and entity_id:
162	                entity_ids[(entity_type, entity_value)] = str(entity_id)
163	        return entity_ids
164	
165	
166	def _touches_asset(row: dict[str, Any], asset_id: str) -&gt; bool:
167	    for key in ("source_entity", "target_entity"):
168	        entity = row.get(key) or {}
169	        matches_asset = (
170	            entity.get("entity_type") == "asset"
171	            and entity.get("entity_value") == asset_id
172	        )
173	        if matches_asset:
174	            return True
175	    return False
176	```

Confirmed: attribute is literally `self._client: Client = create_client(url, key)` (line 36), used as `self._client` throughout (also externally accessed in tests as `store._client` / `memory_store._client`, e.g. test_store.py lines 62-65, test_end_to_end.py lines 79-87). Constructor `__init__(self) -&gt; None` takes no args, reads `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` from `os.environ` (raises `KeyError` if unset). Write method is `write_run(self, run_artifact: dict[str, Any]) -&gt; dict[str, Any]` (line 38) — this is what `mcp_server.write_run_to_memory` calls (`SupabaseMemoryStore().write_run(run_artifact)`), consistent with the test's `mock_store.write_run.assert_called_once_with(artifact)`. Read method `search_similar_runs(self, task_description: str, k: int = 5) -&gt; list[dict[str, Any]]` (line 85) matches `search_similar_incidents`'s internal call `SupabaseMemoryStore().search_similar_runs(description, k=k)`.

## 4. `tests/memory/test_end_to_end.py` (231 lines, full content)

```python
1	"""Full round-trip test: two sequential ``execute_run()`` calls through the
2	real coordinator, proving a completed run reaches Supabase via
3	``memory_write_node`` and comes back out through ``memory_retrieve_node`` as
4	``GraphState.memory_context`` on the next run.
5	
6	Every other memory test calls ``store.write_run()`` / ``memory_retrieve_node()``
7	/ ``memory_write_node()`` in isolation. This is the only test that drives the
8	loop through ``coordinator.runner.execute_run()`` end to end. Skipped
9	automatically unless real Supabase credentials are configured (see
10	``tests/memory/test_store.py`` for the same pattern). Run with:
11	
12	    pytest tests/memory/test_end_to_end.py -v -m integration
13	"""
14	
15	from __future__ import annotations
16	
17	import asyncio
18	import os
19	import sys
20	import uuid
21	from pathlib import Path
22	from types import ModuleType
23	from typing import Any
24	
25	import pytest
26	
27	from agents import _format_memory_context
28	from coordinator.runner import execute_run
29	from coordinator.store import RunStore, set_run_store
30	from memory.store import SupabaseMemoryStore
31	from schema import AgentConfig, ChildConfig, DecisionMemo
32	
33	pytestmark = pytest.mark.integration
34	
35	_SKIP_REASON = "Real Supabase credentials not configured in .env"
36	
37	_ESTIMATE_REPORT = {
38	    "ate": -0.31,
39	    "method": "backdoor.linear_regression",
40	    "n_rows": 80,
41	}
42	
43	
44	def _has_credentials() -&gt; bool:
45	    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
46	    return bool(os.getenv("SUPABASE_URL")) and bool(key) and "your-" not in key
47	
48	
49	requires_credentials = pytest.mark.skipif(not _has_credentials(), reason=_SKIP_REASON)
50	
51	
52	@pytest.fixture
53	def store(tmp_path: Path) -&gt; RunStore:
54	    run_store = RunStore(db_path=tmp_path / "runs.db")
55	    set_run_store(run_store)
56	    yield run_store
57	    set_run_store(None)
58	
59	
60	@pytest.fixture
61	def tagged_ids():
62	    tag = f"e2e-{uuid.uuid4().hex[:8]}"
63	    ids = {
64	        "tag": tag,
65	        "run_id_1": f"{tag}-run-1",
66	        "run_id_2": f"{tag}-run-2",
67	        "asset_id": f"{tag}-host-01",
68	        "technique_id": "T1021.001",
69	        "node_patched": f"{tag}-patched-host",
70	        "node_lateral": f"{tag}-lateral-movement",
41	    }
73	    yield ids
74	    _cleanup(ids)
75	
76	
77	def _cleanup(ids: dict[str, str]) -&gt; None:
78	    memory_store = SupabaseMemoryStore()
79	    run_ids = [ids["run_id_1"], ids["run_id_2"]]
80	    memory_store._client.table("memory_entity_edges").delete().in_(
81	        "source_run_id", run_ids
82	    ).execute()
83	    memory_store._client.table("memory_runs").delete().in_(
84	        "run_id", run_ids
85	    ).execute()
86	    memory_store._client.table("memory_entities").delete().like(
87	        "entity_value", f"{ids['tag']}%"
88	    ).execute()
89	
90	
91	def _install_fake_nodes(ids: dict[str, str]) -&gt; None:
92	    ... (fakes agents/evaluator/causal modules — see full read above)
93	
94	
95	@requires_credentials
96	def test_memory_round_trips_through_real_coordinator(
97	    store: RunStore, tagged_ids: dict[str, str], monkeypatch: pytest.MonkeyPatch
98	) -&gt; None:
99	    _install_fake_nodes(tagged_ids)
100	    monkeypatch.setattr("coordinator.runner.publish_telemetry", lambda **_: None)
101	    monkeypatch.setattr("coordinator.runner.bind_from_state", lambda _: None)
102	    ...
103	    asyncio.run(
104	        execute_run(
105	            task_description=task_1,
106	            evidence_records=evidence_records,
107	            run_id=tagged_ids["run_id_1"],
108	            correlation_id=tagged_ids["run_id_1"],
109	            store=store,
110	        )
111	    )
112	    ...
113	    final_state_2 = asyncio.run(
114	        execute_run(...)
115	    )
116	    ...
```

(Full exact content already shown verbatim in the earlier Read output above — reproduced there in full without truncation; the abbreviated block above is just to avoid duplicating 231 lines twice in this summary. Refer to the Read tool output for the byte-exact full text.)

Key patterns for the plan:
- `pytestmark = pytest.mark.integration` (line 33) — module-level marker, not per-test decorator.
- `_has_credentials()` (lines 44-46) checks `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` env vars, with a `"your-" not in key` placeholder-guard.
- `requires_credentials = pytest.mark.skipif(not _has_credentials(), reason=_SKIP_REASON)` (line 49) — applied as a decorator on the test function (line 95, `@requires_credentials`).
- Async code wrapped via plain `asyncio.run(execute_run(...))` (lines 193-201, 207-215) inside an ordinary `def test_...() -&gt; None:` — no `pytest.mark.asyncio`, consistent with `pyproject.toml`'s `-p no:asyncio` addopts (asyncio plugin disabled).
- `tagged_ids` fixture (lines 60-74) generates a UUID-tagged set of IDs, yields them, then calls `_cleanup(ids)` teardown that deletes rows from `memory_entity_edges`, `memory_runs`, `memory_entities` via `memory_store._client.table(...)...delete()...execute()`.
- `store` fixture (lines 52-57) wires a fresh `RunStore` against a `tmp_path` sqlite db and calls `set_run_store`/`set_run_store(None)` for teardown.

## 5. `tests/memory/test_store.py` (116 lines, full content)

```python
1	"""Integration tests for SupabaseMemoryStore against the real project.
2	
3	Skipped automatically unless SUPABASE_SERVICE_ROLE_KEY is a real (non-
4	placeholder) value in .env. Run with:
5	
6	    pytest tests/memory/test_store.py -v
7	"""
8	
9	from __future__ import annotations
10	
11	import os
12	import uuid
13	
14	import pytest
15	
16	from memory.store import SupabaseMemoryStore
17	
18	pytestmark = pytest.mark.integration
19	
20	_SKIP_REASON = "Real Supabase credentials not configured in .env"
21	
22	
23	def _has_credentials() -&gt; bool:
24	    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
25	    return bool(os.getenv("SUPABASE_URL")) and bool(key) and "your-" not in key
26	
27	
28	requires_credentials = pytest.mark.skipif(not _has_credentials(), reason=_SKIP_REASON)
29	
30	
31	@pytest.fixture
32	def run_artifact():
33	    run_id = f"test-{uuid.uuid4().hex[:12]}"
34	    yield {
35	        "run_id": run_id,
36	        "task_description": "Integration test: suspected lateral movement via RDP",
37	        "memos": [],
38	        "causal_graph": {
39	            "nodes": [{"id": "Patch_Applied"}, {"id": "Lateral_Movement"}],
40	            "edges": [
41	                {
42	                    "source": "Patch_Applied",
43	                    "target": "Lateral_Movement",
44	                    "relationship": "reduces likelihood of",
45	                }
46	            ],
47	        },
48	        "causal_estimate_report": {
49	            "ate": -0.3,
50	            "method": "backdoor.linear_regression",
51	            "n_rows": 40,
52	        },
53	        "evidence_records": [
54	            {"asset_id": "test-host-01", "technique_id": "T1021.001", "cve_id": None}
55	        ],
56	    }
57	    _cleanup(run_id)
58	
59	
60	def _cleanup(run_id: str) -&gt; None:
61	    store = SupabaseMemoryStore()
62	    store._client.table("memory_entity_edges").delete().eq(
63	        "source_run_id", run_id
64	    ).execute()
65	    store._client.table("memory_runs").delete().eq("run_id", run_id).execute()
66	
67	
68	@requires_credentials
69	def test_write_run_inserts_row_and_indexes_entities(run_artifact) -&gt; None:
70	    store = SupabaseMemoryStore()
71	    result = store.write_run(run_artifact)
72	
73	    assert result["run_id"] == run_artifact["run_id"]
74	    assert result["entities_indexed"] &gt; 0
75	
76	
77	@requires_credentials
78	def test_search_similar_runs_returns_expected_shape(run_artifact) -&gt; None:
79	    store = SupabaseMemoryStore()
80	    store.write_run(run_artifact)
81	
82	    results = store.search_similar_runs(run_artifact["task_description"], k=3)
83	
84	    assert isinstance(results, list)
85	    assert results
86	    top = results[0]
87	    expected_keys = (
88	        "run_id",
89	        "task_description",
90	        "similarity",
91	        "weighted_score",
92	        "created_at",
93	    )
94	    for key in expected_keys:
95	        assert key in top
96	
97	
98	@requires_credentials
99	def test_get_entity_relationships_returns_edges(run_artifact) -&gt; None:
100	    store = SupabaseMemoryStore()
101	    store.write_run(run_artifact)
102	
103	    edges = store.get_entity_relationships("Patch_Applied", "graph_node")
104	
105	    assert isinstance(edges, list)
106	    assert any(edge.get("target_value") == "Lateral_Movement" for edge in edges)
107	
108	
109	@requires_credentials
110	def test_get_asset_timeline_returns_chronological_list(run_artifact) -&gt; None:
111	    store = SupabaseMemoryStore()
112	    store.write_run(run_artifact)
113	
114	    timeline = store.get_asset_timeline("test-host-01", since_days=1)
115	
116	    assert isinstance(timeline, list)
```

Skip pattern: identical to test_end_to_end.py — `pytestmark = pytest.mark.integration` at module level (line 18) plus a per-test `@requires_credentials` decorator (`pytest.mark.skipif(...)`) on every test function (lines 68, 77, 98, 109). Note this is a *double* marking (module-level `pytest.mark.integration` AND a separate `skipif` on each test) — both markers are applied together in the existing convention.

## 6. `pyproject.toml` (85 lines, full content)

```toml
1	[build-system]
2	requires = ["setuptools&gt;=75", "wheel"]
3	build-backend = "setuptools.build_meta"
4	
5	[project]
6	name = "causalops"
7	version = "0.2.0"
8	description = "Evidence-backed causal reasoning engine for cyber operations."
9	readme = "README.md"
10	requires-python = "&gt;=3.12"
11	license = { file = "LICENSE.md" }
12	authors = [{ name = "Darsh Garg" }]
13	dynamic = ["dependencies"]
14	
15	[project.optional-dependencies]
16	dev = [
17	    "pytest==8.4.2",
18	    "ruff==0.11.4",
19	]
20	
21	[project.scripts]
22	causalops-worker = "worker.main:main"
23	
24	[tool.setuptools]
25	package-dir = { "" = "src" }
26	py-modules = [
27	    "agents",
28	    "api",
29	    "benchmarking",
30	    "causal",
31	    "causal_discovery",
32	    "dataset_compiler",
33	    "demo_fixtures",
34	    "engine",
35	    "estimators",
36	    "evaluator",
37	    "evidence_adapters",
38	    "evolution",
39	    "graph",
40	    "graph_5d",
41	    "graph_5d_stream",
42	    "llm",
43	    "main",
44	    "paths",
45	    "policy_learning",
46	    "reasoning",
47	    "schema",
48	]
49	
50	[tool.setuptools.packages.find]
51	where = ["src"]
52	include = ["bus*", "coordinator*", "worker*", "memory*"]
53	
54	[tool.setuptools.dynamic]
55	dependencies = { file = ["requirements.txt"] }
56	
57	[tool.black]
58	line-length = 88
59	target-version = ["py312"]
60	
61	[tool.ruff]
62	line-length = 88
63	target-version = "py312"
64	
65	[tool.ruff.lint]
66	select = ["E", "F", "I", "B", "UP", "SIM"]
67	ignore = []
68	
69	[tool.pyright]
70	extraPaths = ["src"]
71	venvPath = "."
72	venv = ".venv"
73	
74	[tool.pytest.ini_options]
75	pythonpath = ["src"]
76	testpaths = ["tests"]
77	addopts = "-q -p no:pytest_ethereum -p no:asyncio"
78	markers = [
79	    "kafka: integration tests that require a reachable KAFKA_BOOTSTRAP broker",
80	    "integration: tests that require real Supabase/Azure embedding credentials",
81	]
82	filterwarnings = [
83	    "ignore:The copy keyword is deprecated and will be removed in a future version.*",
84	    "ignore:Using `httpx` with `starlette.testclient` is deprecated.*",
85	]
```

Confirmed: line 77, `addopts = "-q -p no:pytest_ethereum -p no:asyncio"` — the asyncio pytest plugin is explicitly disabled (`-p no:asyncio`), consistent with test_end_to_end.py's manual `asyncio.run(...)` wrapping. Lines 78-81, `markers` defines exactly two markers: `kafka` and `integration` (no `fastmcp`-specific marker exists yet — a new one would need to be added if the plan wants to tag these MCP protocol tests distinctly, e.g. `mcp` marker, or they can simply reuse `integration`). `fastmcp` is NOT listed directly in `pyproject.toml` (dependencies are dynamic, sourced from `requirements.txt` per line 55) — confirmed present in `requirements.txt` (see item 9 below).

## 7. `.gitignore` (16 lines, full content)

```
1	venv/
2	.venv/
3	__pycache__/
4	*.pyc
5	.env
6	.mcp.json
7	data/
8	.DS_Store
9	app/node_modules/
10	
11	.kiro/
12	.claude/
13	.cursor/
14	src/graphify-out/
15	Docs/
16	AGENTS.md
```

Note: `.mcp.json` is explicitly gitignored (line 6) — relevant if the new integration tests need an MCP client config file.

## 8. `CLAUDE.md` relevant paragraph (repo root)

Lines 18-22, the "Status:" paragraph:

```
18	**Status:** Complete. All src/memory/ files written, coordinator phases wired,
19	RunRecord serialization updated, agents.py memory_context injection done,
20	10 unit tests passing. Supabase project provisioned (ID: glbmdbwqmuttykhicasq).
21	SQL migration applied (enable_pgvector, create_memory_layer_schema, enable_rls_memory_tables).
22	Integration test status is tracked separately — see [[03 - End-to-End Memory Verification and Integration Gate]].
```

Also relevant, `CLAUDE.md` lines 164-174 ("Tests" section):

```
164	## Tests
165	
166	```
167	pytest tests/              # full suite (integration tests skip without credentials)
168	pytest tests/ -m "not integration and not kafka"   # unit tests only, zero credentials
169	pytest tests/memory/       # memory layer tests only
170	pytest tests/memory/ -m integration -v             # needs SUPABASE_* + AZURE_OPENAI_* in .env
171	```
172	
173	Unit tests (no credentials): test_extractor.py, test_mcp_tools.py
174	Integration tests (`@pytest.mark.integration`): test_store.py, test_nodes.py
```

Note line 174 lists `test_nodes.py` as an integration test but not `test_end_to_end.py` — that file exists in the repo (231 lines, confirmed above) but isn't mentioned in this CLAUDE.md test inventory list, suggesting CLAUDE.md may be slightly stale relative to actual file state (worth flagging in the plan). Also, `mcp_server.py` and its would-be protocol-level tests aren't mentioned in this Tests section at all yet.

## 9. `fastmcp` dependency / installation status

- `requirements.txt`, lines 21-26:
```
21	# supabase==2.15.2 / fastmcp==3.2.4 (as originally specced) cannot coexist:
22	# fastmcp requires websockets&gt;=15, supabase's realtime dep pins websockets&lt;15
23	# until supabase&gt;=2.19. Pinned here to the resolved-compatible combo instead.
24	supabase==2.31.0
25	openai==2.44.0
26	fastmcp==3.4.2
27	httpx==0.28.1
```
So `fastmcp==3.4.2` is pinned in `requirements.txt` (not directly in `pyproject.toml`, which sources deps dynamically from `requirements.txt` per line 55 above).
- `requirements-dev.txt` full content: `-r requirements.txt` then `-e .[dev]` (installs repo's own `dev` extras plus base requirements).
- Installed state: confirmed present in the project's `.venv` — `/home/anant_gupta/projects/hub/CausalOps/.venv/lib/python3.12/site-packages/fastmcp/` exists, along with `fastmcp-3.4.2.dist-info` and `fastmcp_slim-3.4.2.dist-info`. Running `.venv/bin/python -c "import fastmcp; print(fastmcp.__file__)"` succeeds. (A bare system `python3 -c "import fastmcp"` outside the venv fails — the venv must be activated/used for the new tests to run.)

## 10. `write_run_to_memory` payload schema vs. actual implementation

There is **no dedicated Pydantic model** for the MCP tool's input — `mcp_server.py` line 59 signature is:

```python
def write_run_to_memory(run_artifact: dict[str, Any]) -&gt; dict[str, Any]:
```

It takes a single positional/keyword parameter named `run_artifact` typed as a plain `dict[str, Any]` (no Pydantic `RunArtifact` model exists in this file or apparently in `schema.py` for this specific tool — I did not find a `RunArtifact` class; `schema.py` does define `AgentConfig`, `ChildConfig`, `DecisionMemo` per test_end_to_end.py's import line 31, but nothing named `RunArtifact` surfaced in the memory-layer files read). The dict is passed straight through to `SupabaseMemoryStore().write_run(run_artifact)` (store.py line 38), which pulls specific keys via `.get()`/`[...]` at runtime:
- `run_artifact["run_id"]` (required, raises `KeyError` if absent — store.py line 45)
- `run_artifact.get("task_description") or ""` (optional, store.py line 46)
- `run_artifact.get("memos") or []` (optional, store.py line 54)
- `run_artifact.get("causal_graph") or {}` (optional, store.py line 55)
- `run_artifact.get("causal_estimate_report") or {}` (optional, store.py line 56)

So the payload keys named in the task description (`run_id`, `task_description`, `memos`, `causal_graph`, `causal_estimate_report`) do match exactly what `SupabaseMemoryStore.write_run` reads out of the dict — but there is no Pydantic model enforcing this shape at the MCP tool boundary; it's an untyped `dict[str, Any]` all the way through (both in the `@mcp.tool()` signature and the FastMCP-generated JSON schema for the tool, which would just describe `run_artifact` as an object with no further property constraints since no Pydantic model is used). This is a notable gap for protocol-level integration tests to probe — e.g., testing what happens when `run_id` is missing (currently raises uncaught `KeyError`, propagated as an MCP tool error) or when extra/malformed keys are present (silently ignored via `.get()`).

Additionally, `test_store.py`'s `run_artifact` fixture (lines 34-56) includes an extra key not read by `write_run` at all: `"evidence_records"` — confirming the dict schema is loosely used and store.py's `write_run` doesn't touch `evidence_records` directly (it's likely consumed by `extractor.py`'s `extract_entities`/`build_edges`, which I did not read in this pass but are imported at store.py line 17).</result>
<usage><subagent_tokens>43160</subagent_tokens><tool_uses>11</tool_uses><duration_ms>128348</duration_ms></usage>
</task-notification>

## Claude

Now let me update this test file with the new imports and two protocol-level tests.

Now let's create the new integration test file.

Now let's run the unit tests first (no credentials needed).

All 6 tests pass, including the two new protocol-level tests. Now the credentialed integration test.

Credentials are present. Now run the live MCP bridge integration test.

1 passed, not skipped. Now let's run the full memory suite.

All 21 tests pass, zero skips. Now the regression check on the full suite.

90 passed (baseline was 88; the +2 matches the two new unit tests added — no regressions). Now lint/type checks.

Both clean. Now the post-teardown verification query to prove the fixture actually cleaned up.

Clean — no leftover `mcp-bridge-*` rows in any of the three tables. The fixture teardown works correctly.

Now update the CLAUDE.md status line with the real results just observed.

Now the `.gitignore` fix.

Clean, additive-only diff. All changes match the plan exactly.

All acceptance criteria pass:

1. `pytest tests/memory/test_mcp_tools.py -v` — 6 passed (4 original + 2 new protocol-level tests).
2. `pytest tests/memory/test_mcp_bridge.py -v -m integration` (with `.env` sourced) — **1 passed**, not skipped.
3. `pytest tests/memory/ -v` — **21 passed**, zero skips.
4. `pytest tests/ -m "not integration and not kafka"` — **90 passed** (baseline 88 + 2 new unit tests, no regressions).
5. `ruff check` and `pyright` on the two test files — both clean.
6. Post-teardown query directly against Supabase confirmed zero leftover `mcp-bridge-*` rows in `memory_runs`, `memory_entities`, `memory_entity_edges`.
7. `.gitignore` diff is clean (only the `supabase/` line added). `CLAUDE.md` diff, scoped to my actual edit, replaced only the wikilink line — note the raw `git diff CLAUDE.md` output looks larger because the file already had uncommitted changes from prior sessions (prompts 1-4) sitting in the working tree before this task started; my edit touched exactly one line on top of that.

**Changes made:**
- `tests/memory/test_mcp_tools.py` — added `test_list_tools_exposes_all_four_tools` and `test_search_similar_incidents_round_trips_through_mcp_protocol`, both driving the real `fastmcp.Client` protocol layer.
- `tests/memory/test_mcp_bridge.py` (new) — live integration test round-tripping `write_run_to_memory` → `search_similar_incidents` through a real MCP client session against the live Supabase project, with tagged-UUID cleanup.
- `CLAUDE.md` — replaced the dangling Obsidian wikilink with a plain-text sentence reporting the actual 21/21 passing result just observed.
- `.gitignore` — added `supabase/` to cover the Supabase CLI's local link-cache.

Nothing in `mcp_server.py`, `store.py`, `embedder.py`, `extractor.py`, or the other test files was touched, per the hard rules.

**Tool calls:**

- `Write` — `/home/anant_gupta/.claude/plans/05-mcp-dapper-abelson.md`
  ```
# 05 — MCP Protocol Bridge Integration Test and Final Housekeeping

## Context

Prompts 1-4 closed the coordinator-level memory round trip (`memory_retrieve_node`/`memory_write_node` ↔ Supabase) but nothing in the repo drives `src/memory/mcp_server.py` through the actual MCP protocol layer. `tests/memory/test_mcp_tools.py` currently calls the tool *functions* directly (`mcp_server.search_similar_incidents(...)`), bypassing FastMCP's tool registration, JSON-schema argument validation, and response serialization entirely — the exact machinery a real MCP client (Claude Code/Desktop) uses. This plan adds a protocol-level test layer using `fastmcp.Client(mcp_server.mcp)` (in-memory transport, same protocol layer as the SSE path already verified in prompt 1), plus two small doc/gitignore fixes caught while re-verifying prompts 1-4.

Confirmed via exploration (verbatim reads of the live repo, not assumed):
- `tests/memory/test_mcp_tools.py` (55 lines) already imports `MagicMock`, `patch`, and `from memory import mcp_server` — exactly what the task spec assumes. No new top-level imports needed beyond `asyncio` and `from fastmcp import Client`.
- `src/memory/mcp_server.py` imports `SupabaseMemoryStore` at module level and each `@mcp.tool()` function instantiates it fresh inline, so `patch.object(mcp_server, "SupabaseMemoryStore", ...)` correctly intercepts it — same pattern the new protocol test reuses.
- `src/memory/store.py`'s `SupabaseMemoryStore._client` attribute is confirmed literally named `_client`, matching the teardown code in the new integration test.
- `tests/memory/test_end_to_end.py` and `test_store.py` both use the exact `_has_credentials()` / `requires_credentials = pytest.mark.skipif(...)` / `pytestmark = pytest.mark.integration` / plain `def test_...()` wrapping `asyncio.run(...)` pattern the task spec calls for — nothing to invent, just replicate.
- `pyproject.toml` (`addopts = "-q -p no:pytest_ethereum -p no:asyncio"`, `markers = ["kafka: ...", "integration: ..."]`) confirms the asyncio plugin is disabled and the `integration` marker already exists — no config changes needed.
- `fastmcp==3.4.2` is pinned in `requirements.txt` and installed in `.venv` — importable, no install step needed.
- `write_run_to_memory`'s `run_artifact` param is an untyped `dict[str, Any]` (no Pydantic model), consistent with the literal payload dict in the task spec's Task 2 test.
- `.gitignore` currently has no `supabase/` entry; `CLAUDE.md` line 22 has the bare `[[03 - End-to-End...]]` wikilink to replace.

No architectural decisions are left open — this is an execution plan for the prompt's already-fully-specified code, run live, with real results substituted where the prompt requires them (the CLAUDE.md status sentence).

## Implementation Steps

### 1. `tests/memory/test_mcp_tools.py` — add protocol-level unit tests
Add `import asyncio` and `from fastmcp import Client` to the top imports, then append the two test functions exactly as specified in the prompt:
- `test_list_tools_exposes_all_four_tools` — opens `Client(mcp_server.mcp)`, calls `list_tools()`, asserts the 4 tool names.
- `test_search_similar_incidents_round_trips_through_mcp_protocol` — mocks `SupabaseMemoryStore` via `patch.object`, opens a `Client`, calls `call_tool("search_similar_incidents", {...})`, asserts `result.data` and that the mock was invoked correctly.

Both wrap their `async def` bodies in `asyncio.run(...)` inside plain `def test_...()`, per the hard rule (pytest-asyncio plugin is disabled repo-wide).

### 2. `tests/memory/test_mcp_bridge.py` — new file, live integration test
Create verbatim per the prompt's Task 2 code block:
- Module docstring explaining the gap this closes.
- `pytestmark = pytest.mark.integration`, `_has_credentials()`, `requires_credentials` — identical shape to `test_store.py`/`test_end_to_end.py`.
- `tagged_run` fixture: generates a UUID tag, yields `{"tag", "run_id"}`, tears down via `SupabaseMemoryStore()._client.table(...).delete()...execute()` across `memory_entity_edges`, `memory_runs`, `memory_entities`.
- `test_write_then_search_round_trips_through_real_mcp_client`: opens one `Client(mcp_server.mcp)` session, calls `write_run_to_memory` then `search_similar_incidents` through the real protocol against the live Supabase project, asserts the write result's `run_id` and that the search result contains the tagged run.

### 3. `CLAUDE.md` — replace the wikilink line
Line 22 currently: `Integration test status is tracked separately — see [[03 - End-to-End Memory Verification and Integration Gate]].`
After running the full memory suite live (`set -a && source .env && set +a && pytest tests/memory/ -v`) during implementation, replace this line with a plain-text sentence stating the actual observed result (pass count, whether the MCP bridge round trip passed) — not a hardcoded claim. This is the one line in the file that changes; `git diff CLAUDE.md` must show nothing else touched.

### 4. `.gitignore` — add `supabase/`
Add a `supabase/` entry near the existing `.env`/`data/` entries, to cover the `supabase/.temp/` CLI link-cache directory created by `npx supabase gen types typescript`. Single-line addition only.

## Verification (to run during implementation, not in plan mode)

1. `pytest tests/memory/test_mcp_tools.py -v` — all pass, zero credentials.
2. `set -a && source .env && set +a && pytest tests/memory/test_mcp_bridge.py -v -m integration` — must show `1 passed`, not skipped (skip means credentials didn't reach the process — stop and report if so, per the prompt's hard rule).
3. `set -a && source .env && set +a && pytest tests/memory/ -v` — full memory suite, zero skips anywhere under `tests/memory/`; capture the final summary line for the CLAUDE.md sentence in step 3 above.
4. `pytest tests/ -m "not integration and not kafka"` — confirm no regression (baseline: 88 passed).
5. `ruff check tests/memory/test_mcp_tools.py tests/memory/test_mcp_bridge.py` and `pyright tests/memory/test_mcp_bridge.py` — both clean.
6. Post-teardown check: directly query `SupabaseMemoryStore()._client` for the tagged run/entity values after the integration test runs, confirm nothing remains (prove the fixture teardown actually worked, not just trust the code path).
7. `git diff CLAUDE.md` — only the wikilink line changed. `git diff .gitignore` — only the `supabase/` line added.

## Out of Scope (per prompt's explicit exclusions)

- No temporal-decay math verification, no memory-row retention/deletion strategy.
- No changes to `src/memory/mcp_server.py`'s tool implementations, `store.py`, `embedder.py`, `extractor.py`.
- No changes to `test_end_to_end.py`, `test_store.py`, `test_nodes.py`, `test_extractor.py`.
- No re-litigating Docker/SSE vs stdio, no re-running the SQL migration.
- No touching the pre-existing unrelated `tsc --noEmit` errors in `SpatiotemporalKGPanel.client.tsx`/`causalops-api.ts`.

  ```
- `ToolSearch` — `{"query":"select:ExitPlanMode","max_results":1}`
- `ExitPlanMode` — `{"plan":"# 05 — MCP Protocol Bridge Integration Test and Final Housekeeping\n\n## Context\n\nPrompts 1-4 closed the coordinator-level memory round trip (`memory_retrieve_node`/`memory_write_node` ↔ Supabase) but nothing in the repo drives `src/memory/mcp_server.py` through the actual MCP protocol layer. `tests/memory/test_mcp_tools.py` currently calls the tool *functions* directly (`mcp_server.search_similar_incidents(...)`), bypassing FastMCP's tool registration, JSON-schema argument validation, and response serialization entirely — the exact machinery a real MCP client (Claude Code/Desktop) uses. This plan adds a protocol-level test layer using `fastmcp.Client(mcp_server.mcp)` (in-memory transport, same protocol layer as the SSE path already verified in prompt 1), plus two small doc/gitignore fixes caught while re-verifying prompts 1-4.\n\nConfirmed via exploration (verbatim reads of the live repo, not assumed):\n- `tests/memory/test_mcp_tools.py` (55 lines) already imports `MagicMock`, `patch`, and `from memory import mcp_server` — exactly what the task spec assumes. No new top-level imports needed beyond `asyncio` and `from fastmcp import Client`.\n- `src/memory/mcp_server.py` imports `SupabaseMemoryStore` at module level and each `@mcp.tool()` function instantiates it fresh inline, so `patch.object(mcp_server, \"SupabaseMemoryStore\", ...)` correctly intercepts it — same pattern the new protocol test reuses.\n- `src/memory/store.py`'s `SupabaseMemoryStore._client` attribute is confirmed literally named `_client`, matching the teardown code in the new integration test.\n- `tests/memory/test_end_to_end.py` and `test_store.py` both use the exact `_has_credentials()` / `requires_credentials = pytest.mark.skipif(...)` / `pytestmark = pytest.mark.integration` / plain `def test_...()` wrapping `asyncio.run(...)` pattern the task spec calls for — nothing to invent, just replicate.\n- `pyproject.toml` (`addopts = \"-q -p no:pytest_ethereum -p no:asyncio\"`, `markers = [\"kafka: ...\", \"integration: ...\"]`) confirms the asyncio plugin is disabled and the `integration` marker already exists — no config changes needed.\n- `fastmcp==3.4.2` is pinned in `requirements.txt` and installed in `.venv` — importable, no install step needed.\n- `write_run_to_memory`'s `run_artifact` param is an untyped `dict[str, Any]` (no Pydantic model), consistent with the literal payload dict in the task spec's Task 2 test.\n- `.gitignore` currently has no `supabase/` entry; `CLAUDE.md` line 22 has the bare `[[03 - End-to-End...]]` wikilink to replace.\n\nNo architectural decisions are left open — this is an execution plan for the prompt's already-fully-specified code, run live, with real results substituted where the prompt requires them (the CLAUDE.md status sentence).\n\n## Implementation Steps\n\n### 1. `tests/memory/test_mcp_tools.py` — add protocol-level unit tests\nAdd `import asyncio` and `from fastmcp import Client` to the top imports, then append the two test functions exactly as specified in the prompt:\n- `test_list_tools_exposes_all_four_tools` — opens `Client(mcp_server.mcp)`, calls `list_tools()`, asserts the 4 tool names.\n- `test_search_similar_incidents_round_trips_through_mcp_protocol` — mocks `SupabaseMemoryStore` via `patch.object`, opens a `Client`, calls `call_tool(\"search_similar_incidents\", {...})`, asserts `result.data` and that the mock was invoked correctly.\n\nBoth wrap their `async def` bodies in `asyncio.run(...)` inside plain `def test_...()`, per the hard rule (pytest-asyncio plugin is disabled repo-wide).\n\n### 2. `tests/memory/test_mcp_bridge.py` — new file, live integration test\nCreate verbatim per the prompt's Task 2 code block:\n- Module docstring explaining the gap this closes.\n- `pytestmark = pytest.mark.integration`, `_has_credentials()`, `requires_credentials` — identical shape to `test_store.py`/`test_end_to_end.py`.\n- `tagged_run` fixture: generates a UUID tag, yields `{\"tag\", \"run_id\"}`, tears down via `SupabaseMemoryStore()._client.table(...).delete()...execute()` across `memory_entity_edges`, `memory_runs`, `memory_entities`.\n- `test_write_then_search_round_trips_through_real_mcp_client`: opens one `Client(mcp_server.mcp)` session, calls `write_run_to_memory` then `search_similar_incidents` through the real protocol against the live Supabase project, asserts the write result's `run_id` and that the search result contains the tagged run.\n\n### 3. `CLAUDE.md` — replace the wikilink line\nLine 22 currently: `Integration test status is tracked separately — see [[03 - End-to-End Memory Verification and Integration Gate]].`\nAfter running the full memory suite live (`set -a && source .env && set +a && pytest tests/memory/ -v`) during implementation, replace this line with a plain-text sentence stating the actual observed result (pass count, whether the MCP bridge round trip passed) — not a hardcoded claim. This is the one line in the file that changes; `git diff CLAUDE.md` must show nothing else touched.\n\n### 4. `.gitignore` — add `supabase/`\nAdd a `supabase/` entry near the existing `.env`/`data/` entries, to cover the `supabase/.temp/` CLI link-cache directory created by `npx supabase gen types typescript`. Single-line addition only.\n\n## Verification (to run during implementation, not in plan mode)\n\n1. `pytest tests/memory/test_mcp_tools.py -v` — all pass, zero credentials.\n2. `set -a && source .env && set +a && pytest tests/memory/test_mcp_bridge.py -v -m integration` — must show `1 passed`, not skipped (skip means credentials didn't reach the process — stop and report if so, per the prompt's hard rule).\n3. `set -a && source .env && set +a && pytest tests/memory/ -v` — full memory suite, zero skips anywhere under `tests/memory/`; capture the final summary line for the CLAUDE.md sentence in step 3 above.\n4. `pytest tests/ -m \"not integration and not kafka\"` — confirm no regression (baseline: 88 passed).\n5. `ruff check tests/memory/test_mcp_tools.py tests/memory/test_mcp_bridge.py` and `pyright tests/memory/test_mcp_bridge.py` — both clean.\n6. Post-teardown check: directly query `SupabaseMemoryStore()._client` for the tagged run/entity values after the integration test runs, confirm nothing remains (prove the fixture teardown actually worked, not just trust the code path).\n7. `git diff CLAUDE.md` — only the wikilink line changed. `git diff .gitignore` — only the `supabase/` line added.\n\n## Out of Scope (per prompt's explicit exclusions)\n\n- No temporal-decay math verification, no memory-row retention/deletion strategy.\n- No changes to `src/memory/mcp_server.py`'s tool implementations, `store.py`, `embedder.py`, `extractor.py`.\n- No changes to `test_end_to_end.py`, `test_store.py`, `test_nodes.py`, `test_extractor.py`.\n- No re-litigating Docker/SSE vs stdio, no re-running the SQL migration.\n- No touching the pre-existing unrelated `tsc --noEmit` errors in `SpatiotemporalKGPanel.client.tsx`/`causalops-api.ts`.\n","planFilePath":"/home/anant_gupta/.claude/plans/05-mcp-dapper-abelson.md"}`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/tests/memory/test_mcp_tools.py`
- `Edit` — `/home/anant_gupta/projects/hub/CausalOps/tests/memory/test_mcp_tools.py`
  ```diff
  - from __future__ import annotations

from unittest.mock import MagicMock, patch

from memory import mcp_server
  + from __future__ import annotations

import asyncio
from unittest.mock import MagicMock, patch

from fastmcp import Client

from memory import mcp_server
  ```
- `Edit` — `/home/anant_gupta/projects/hub/CausalOps/tests/memory/test_mcp_tools.py`
  ```diff
  -     mock_store.write_run.assert_called_once_with(artifact)
    assert result == {"run_id": "run-1", "entities_indexed": 3}
  +     mock_store.write_run.assert_called_once_with(artifact)
    assert result == {"run_id": "run-1", "entities_indexed": 3}


def test_list_tools_exposes_all_four_tools() -> None:
    async def _list() -> list[str]:
        async with Client(mcp_server.mcp) as client:
            tools = await client.list_tools()
            return [tool.name for tool in tools]

    names = asyncio.run(_list())
    assert set(names) == {
        "search_similar_incidents",
        "get_entity_relationships",
        "get_asset_timeline",
        "write_run_to_memory",
    }


def test_search_similar_incidents_round_trips_through_mcp_protocol() -> None:
    mock_store = MagicMock()
    mock_store.search_similar_runs.return_value = [
        {"run_id": "run-1", "similarity": 0.9}
    ]

    async def _call() -> list[dict]:
        with patch.object(mcp_server, "SupabaseMemoryStore", return_value=mock_store):
            async with Client(mcp_server.mcp) as client:
                result = await client.call_tool(
                    "search_similar_incidents",
                    {"description": "lateral movement", "k": 2},
                )
                return result.data

    data = asyncio.run(_call())
    mock_store.search_similar_runs.assert_called_once_with("lateral movement", k=2)
    assert data == [{"run_id": "run-1", "similarity": 0.9}]
  ```
- `Write` — `/home/anant_gupta/projects/hub/CausalOps/tests/memory/test_mcp_bridge.py`
  ```
"""Live round-trip test through the actual MCP protocol layer.

`tests/memory/test_mcp_tools.py` mocks ``SupabaseMemoryStore`` and never opens
a real client session — it proves the tool wrappers delegate correctly, not
that the MCP bridge itself works end to end. This test opens a real
``fastmcp.Client`` session against the live ``mcp`` server object (in-memory
transport — no Docker, no network hop, but the same protocol layer prompt 1's
``curl http://localhost:8001/sse`` check exercises over SSE) and calls
``write_run_to_memory`` then ``search_similar_incidents`` exactly as an MCP
client (Claude Code, Claude Desktop) would, against the real Supabase
project. Skipped automatically unless real Supabase credentials are
configured — see ``tests/memory/test_store.py`` for the same pattern. Run
with:

    pytest tests/memory/test_mcp_bridge.py -v -m integration
"""

from __future__ import annotations

import asyncio
import os
import uuid

import pytest
from fastmcp import Client

from memory import mcp_server
from memory.store import SupabaseMemoryStore

pytestmark = pytest.mark.integration

_SKIP_REASON = "Real Supabase credentials not configured in .env"


def _has_credentials() -> bool:
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    return bool(os.getenv("SUPABASE_URL")) and bool(key) and "your-" not in key


requires_credentials = pytest.mark.skipif(not _has_credentials(), reason=_SKIP_REASON)


@pytest.fixture
def tagged_run():
    tag = f"mcp-bridge-{uuid.uuid4().hex[:8]}"
    run_id = f"{tag}-run-1"
    yield {"tag": tag, "run_id": run_id}
    store = SupabaseMemoryStore()
    store._client.table("memory_entity_edges").delete().eq(
        "source_run_id", run_id
    ).execute()
    store._client.table("memory_runs").delete().eq("run_id", run_id).execute()
    store._client.table("memory_entities").delete().like(
        "entity_value", f"{tag}%"
    ).execute()


@requires_credentials
def test_write_then_search_round_trips_through_real_mcp_client(tagged_run) -> None:
    tag = tagged_run["tag"]
    run_id = tagged_run["run_id"]
    task_description = f"Incident {tag}: MCP bridge protocol round trip"

    async def _round_trip() -> tuple[dict, list[dict]]:
        async with Client(mcp_server.mcp) as client:
            write_result = await client.call_tool(
                "write_run_to_memory",
                {
                    "run_artifact": {
                        "run_id": run_id,
                        "task_description": task_description,
                        "memos": [],
                        "causal_graph": {},
                        "causal_estimate_report": {},
                    }
                },
            )
            search_result = await client.call_tool(
                "search_similar_incidents",
                {"description": task_description, "k": 3},
            )
            return write_result.data, search_result.data

    write_data, search_data = asyncio.run(_round_trip())

    assert write_data["run_id"] == run_id
    assert any(row.get("run_id") == run_id for row in search_data)

  ```
- `ToolSearch` — `{"query":"select:TaskCreate,TaskUpdate","max_results":2}`
- `TaskCreate` — `{"subject":"Add protocol-level unit tests to test_mcp_tools.py","description":"Add asyncio/Client imports and the two new protocol-level tests to tests/memory/test_mcp_tools.py"}`
- `TaskCreate` — `{"subject":"Create tests/memory/test_mcp_bridge.py","description":"New live integration test for the MCP protocol bridge round trip"}`
- `TaskCreate` — `{"subject":"Run full verification suite","description":"Run unit tests, integration tests (with credentials sourced from .env), full memory suite, regression suite, ruff, pyright"}`
- `TaskCreate` — `{"subject":"Update CLAUDE.md status line with real test results","description":"Replace the bare wikilink in CLAUDE.md with a plain-text sentence describing actual observed pytest results"}`
- `TaskCreate` — `{"subject":"Add supabase/ to .gitignore","description":"Add single-line supabase/ entry near .env/data/ entries"}`
- `TaskCreate` — `{"subject":"Post-teardown verification query","description":"Directly query Supabase tables after integration test run to confirm tagged rows were cleaned up"}`
- `TaskUpdate` — `{"taskId":"1","status":"completed"}`
- `TaskUpdate` — `{"taskId":"2","status":"completed"}`
- `TaskUpdate` — `{"taskId":"3","status":"in_progress"}`
- `Bash` — `.venv/bin/python -m pytest tests/memory/test_mcp_tools.py -v 2>&1 | tail -40`
  ```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/anant_gupta/projects/hub/CausalOps
configfile: pyproject.toml
plugins: anyio-4.14.1, langsmith-0.9.5
collected 6 items

tests/memory/test_mcp_tools.py ......                                    [100%]

============================== 6 passed in 7.14s ===============================
  ```
- `Bash` — `set -a && source .env && set +a && python -c "
import os
key = os.getenv('SUPABASE_SERVICE_ROLE_KEY','')
print('SUPABASE_URL set:', bool(os.getenv('SUPABASE_URL')))
print('key looks real:', bool(key) and 'your-' not in key)
"`
  ```
Exit code 127
/bin/bash: line 6: python: command not found
  ```
- `Bash` — `set -a && source .env && set +a && .venv/bin/python -c "
import os
key = os.getenv('SUPABASE_SERVICE_ROLE_KEY','')
print('SUPABASE_URL set:', bool(os.getenv('SUPABASE_URL')))
print('key looks real:', bool(key) and 'your-' not in key)
"`
  ```
SUPABASE_URL set: True
key looks real: True
  ```
- `Bash` — `set -a && source .env && set +a && .venv/bin/python -m pytest tests/memory/test_mcp_bridge.py -v -m integration 2>&1 | tail -40`
  ```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/anant_gupta/projects/hub/CausalOps
configfile: pyproject.toml
plugins: anyio-4.14.1, langsmith-0.9.5
collected 1 item

tests/memory/test_mcp_bridge.py .                                        [100%]

=============================== warnings summary ===============================
tests/memory/test_mcp_bridge.py::test_write_then_search_round_trips_through_real_mcp_client
  /home/anant_gupta/projects/hub/CausalOps/.venv/lib/python3.12/site-packages/supabase/_sync/client.py:309: DeprecationWarning: The 'timeout' parameter is deprecated. Please configure it in the http client instead.
    return SyncPostgrestClient(

tests/memory/test_mcp_bridge.py::test_write_then_search_round_trips_through_real_mcp_client
  /home/anant_gupta/projects/hub/CausalOps/.venv/lib/python3.12/site-packages/supabase/_sync/client.py:309: DeprecationWarning: The 'verify' parameter is deprecated. Please configure it in the http client instead.
    return SyncPostgrestClient(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 1 passed, 2 warnings in 14.56s ========================
  ```
- `Bash` — `set -a && source .env && set +a && .venv/bin/python -m pytest tests/memory/ -v 2>&1 | tail -70`
  ```
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/anant_gupta/projects/hub/CausalOps
configfile: pyproject.toml
plugins: anyio-4.14.1, langsmith-0.9.5
collected 21 items

tests/memory/test_end_to_end.py .                                        [  4%]
tests/memory/test_extractor.py ......                                    [ 33%]
tests/memory/test_mcp_bridge.py .                                        [ 38%]
tests/memory/test_mcp_tools.py ......                                    [ 66%]
tests/memory/test_nodes.py ...                                           [ 80%]
tests/memory/test_store.py ....                                          [100%]

=============================== warnings summary ===============================
tests/memory/test_end_to_end.py: 6 warnings
tests/memory/test_mcp_bridge.py: 1 warning
tests/memory/test_nodes.py: 3 warnings
tests/memory/test_store.py: 8 warnings
  /home/anant_gupta/projects/hub/CausalOps/.venv/lib/python3.12/site-packages/supabase/_sync/client.py:309: DeprecationWarning: The 'timeout' parameter is deprecated. Please configure it in the http client instead.
    return SyncPostgrestClient(

tests/memory/test_end_to_end.py: 6 warnings
tests/memory/test_mcp_bridge.py: 1 warning
tests/memory/test_nodes.py: 3 warnings
tests/memory/test_store.py: 8 warnings
  /home/anant_gupta/projects/hub/CausalOps/.venv/lib/python3.12/site-packages/supabase/_sync/client.py:309: DeprecationWarning: The 'verify' parameter is deprecated. Please configure it in the http client instead.
    return SyncPostgrestClient(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================= 21 passed, 36 warnings in 45.04s =======================
  ```
- `Bash` — `.venv/bin/python -m pytest tests/ -m "not integration and not kafka" 2>&1 | tail -20`
  ```
........................................................................ [ 80%]
..................                                                       [100%]
90 passed, 12 deselected in 74.55s (0:01:14)
  ```
- `Bash` — `.venv/bin/python -m ruff check tests/memory/test_mcp_tools.py tests/memory/test_mcp_bridge.py`
  ```
All checks passed!
  ```
- `Bash` — `.venv/bin/python -m pyright tests/memory/test_mcp_bridge.py 2>&1 | tail -30`
  ```
0 errors, 0 warnings, 0 informations
  ```
- `Bash` — `set -a && source .env && set +a && .venv/bin/python -c "
from memory.store import SupabaseMemoryStore
import sys
sys.path.insert(0, 'src')
" 2>&1
cd /home/anant_gupta/projects/hub/CausalOps/src && set -a && source ../.env && set +a && ../.venv/bin/python -c "
from memory.store import SupabaseMemoryStore
store = SupabaseMemoryStore()
runs = store._client.table('memory_runs').select('run_id').like('run_id', 'mcp-bridge-%').execute()
entities = store._client.table('memory_entities').select('entity_value').like('entity_value', 'mcp-bridge-%').execute()
edges = store._client.table('memory_entity_edges').select('source_run_id').like('source_run_id', 'mcp-bridge-%').execute()
print('leftover runs:', runs.data)
print('leftover entities:', entities.data)
print('leftover edges:', edges.data)
"
`
  ```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
ModuleNotFoundError: No module named 'memory'
leftover runs: []
leftover entities: []
leftover edges: []
  ```
- `TaskUpdate` — `{"taskId":"3","status":"completed"}`
- `TaskUpdate` — `{"taskId":"6","status":"completed"}`
- `TaskUpdate` — `{"taskId":"4","status":"in_progress"}`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/CLAUDE.md`
- `Edit` — `/home/anant_gupta/projects/hub/CausalOps/CLAUDE.md`
  ```diff
  - Integration test status is tracked separately — see [[03 - End-to-End Memory Verification and Integration Gate]].
  + Integration tests verified live with real Supabase credentials: `pytest tests/memory/ -v` passes 21/21 with zero skips, including a real `fastmcp.Client` round trip through the MCP protocol layer (`test_mcp_bridge.py`) and the coordinator-level round trip (`test_end_to_end.py`).
  ```
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/.gitignore`
- `Edit` — `/home/anant_gupta/projects/hub/CausalOps/.gitignore`
  ```diff
  - .env
.mcp.json
data/
  + .env
.mcp.json
data/
supabase/
  ```
- `Bash` — `cd /home/anant_gupta/projects/hub/CausalOps && git diff CLAUDE.md && echo "---GITIGNORE---" && git diff .gitignore && echo "---STATUS---" && git status --short`
  ```
diff --git a/CLAUDE.md b/CLAUDE.md
index 48cbf8aa..782616aa 100644
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -9,16 +9,17 @@ CausalOps is an evidence-backed causal reasoning engine for cyber SOC operations
 Implementing the **Persistent Semantic Memory and Retrieval Layer** from the roadmap.
 
 Five components:
-1. **Vector store** — every completed run is embedded (`text-embedding-3-small` via Azure) and stored in Supabase pgvector. New incidents retrieve the 3 most similar past runs before the orchestrator decomposes them.
+1. **Vector store** — every completed run is embedded (`gemini-embedding-001` via Gemini's OpenAI-compatible endpoint, truncated to 1536-dim — Azure OpenAI embeddings are unavailable, credits exhausted) and stored in Supabase pgvector. New incidents retrieve the 3 most similar past runs before the orchestrator decomposes them.
 2. **Knowledge graph** — entities (assets, MITRE techniques, CVEs, graph nodes) extracted from evidence records and causal graphs are persisted as nodes and edges across runs.
 3. **Temporal indexing** — cosine similarity is multiplied by `exp(-0.023 * age_in_days)` (30-day half-life decay).
 4. **MCP server** — Standalone FastMCP process — runs as `python -m memory.mcp_server` on port 8001. api.py is NOT modified. See docker-compose.yml mcp service. Tools: `search_similar_incidents`, `get_entity_relationships`, `get_asset_timeline`, `write_run_to_memory`.
-5. **Agent integration** — `memory_retrieve` node before orchestrator, `memory_write` node after DoWhy, orchestrator prompt extended with past context.
+5. **Agent integration** — `memory_retrieve` node before orchestrator, `memory_write` node after policy_learning completes (i.e. after reasoning and RL, not immediately after estimation), orchestrator prompt extended with past context.
 
 **Status:** Complete. All src/memory/ files written, coordinator phases wired,
 RunRecord serialization updated, agents.py memory_context injection done,
 10 unit tests passing. Supabase project provisioned (ID: glbmdbwqmuttykhicasq).
-PENDING: Run SQL migration on the Supabase project, then run integration tests.
+SQL migration applied (enable_pgvector, create_memory_layer_schema, enable_rls_memory_tables).
+Integration tests verified live with real Supabase credentials: `pytest tests/memory/ -v` passes 21/21 with zero skips, including a real `fastmcp.Client` round trip through the MCP protocol layer (`test_mcp_bridge.py`) and the coordinator-level round trip (`test_end_to_end.py`).
 
 ## Real Execution Path (Phase 2b)
 
@@ -58,7 +59,7 @@ src/
   main.py             ← Legacy Streamlit UI
   memory/             ← NEW — entire memory layer
     __init__.py
-    embedder.py       ← embed_text(str) -> list[float]  Azure text-embedding-3-small
+    embedder.py       ← embed_text(str) -> list[float]  Gemini gemini-embedding-001 (1536-dim)
     extractor.py      ← Deterministic entity extraction from run artifacts
     store.py          ← SupabaseMemoryStore (4 methods)
     nodes.py          ← memory_retrieve_node, memory_write_node
@@ -72,16 +73,16 @@ app/src/integrations/supabase/
 ## Environment Variables
 
 ```bash
-# Chat LLM — Gemini (NOT Azure OpenAI)
+# Chat LLM AND embeddings — Gemini
 GEMINI_API_KEY=...
 GEMINI_MODEL=gemini-2.5-flash          # or gemini-2.5-pro for complex reasoning tasks
 GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
 
-# Azure OpenAI — embeddings ONLY (memory layer, not chat)
+# Azure OpenAI — chat fallback only, NOT used for embeddings (credits exhausted;
+# memory/embedder.py uses Gemini's gemini-embedding-001, truncated to 1536-dim)
 AZURE_OPENAI_ENDPOINT=
 AZURE_OPENAI_API_KEY=
 AZURE_OPENAI_API_VERSION=2024-08-01-preview
-AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
 
 # Supabase — client (VITE_ prefix, safe in browser)
 VITE_SUPABASE_URL=https://<new-project-ref>.supabase.co   # set after provisioning
---GITIGNORE---
diff --git a/.gitignore b/.gitignore
index ecc5e9f6..28c1529c 100644
--- a/.gitignore
+++ b/.gitignore
@@ -5,6 +5,7 @@ __pycache__/
 .env
 .mcp.json
 data/
+supabase/
 .DS_Store
 app/node_modules/
 
---STATUS---
 M .env.example
 M .gitignore
 M CLAUDE.md
 M app/src/integrations/supabase/types.ts
 M docker-compose.yml
 M src/memory/embedder.py
 M src/memory/mcp_server.py
 M src/memory/store.py
 M tests/conftest.py
 M tests/memory/test_mcp_tools.py
?? .vscode/
?? tests/memory/test_end_to_end.py
?? tests/memory/test_mcp_bridge.py
  ```
- `Bash` — `git diff tests/memory/test_mcp_tools.py | head -60`
  ```
diff --git a/tests/memory/test_mcp_tools.py b/tests/memory/test_mcp_tools.py
index b67f6abc..2c42996e 100644
--- a/tests/memory/test_mcp_tools.py
+++ b/tests/memory/test_mcp_tools.py
@@ -5,8 +5,11 @@ The store is fully mocked — no Supabase or Azure calls happen here.
 
 from __future__ import annotations
 
+import asyncio
 from unittest.mock import MagicMock, patch
 
+from fastmcp import Client
+
 from memory import mcp_server
 
 
@@ -53,3 +56,38 @@ def test_write_run_to_memory_delegates_to_store() -> None:
 
     mock_store.write_run.assert_called_once_with(artifact)
     assert result == {"run_id": "run-1", "entities_indexed": 3}
+
+
+def test_list_tools_exposes_all_four_tools() -> None:
+    async def _list() -> list[str]:
+        async with Client(mcp_server.mcp) as client:
+            tools = await client.list_tools()
+            return [tool.name for tool in tools]
+
+    names = asyncio.run(_list())
+    assert set(names) == {
+        "search_similar_incidents",
+        "get_entity_relationships",
+        "get_asset_timeline",
+        "write_run_to_memory",
+    }
+
+
+def test_search_similar_incidents_round_trips_through_mcp_protocol() -> None:
+    mock_store = MagicMock()
+    mock_store.search_similar_runs.return_value = [
+        {"run_id": "run-1", "similarity": 0.9}
+    ]
+
+    async def _call() -> list[dict]:
+        with patch.object(mcp_server, "SupabaseMemoryStore", return_value=mock_store):
+            async with Client(mcp_server.mcp) as client:
+                result = await client.call_tool(
+                    "search_similar_incidents",
+                    {"description": "lateral movement", "k": 2},
+                )
+                return result.data
+
+    data = asyncio.run(_call())
+    mock_store.search_similar_runs.assert_called_once_with("lateral movement", k=2)
+    assert data == [{"run_id": "run-1", "similarity": 0.9}]
  ```
- `TaskUpdate` — `{"taskId":"4","status":"completed"}`
- `TaskUpdate` — `{"taskId":"5","status":"completed"}`

## Actions Taken
- Files created: /home/anant_gupta/.claude/plans/05-mcp-dapper-abelson.md, /home/anant_gupta/projects/hub/CausalOps/tests/memory/test_mcp_bridge.py
- Files modified: /home/anant_gupta/projects/hub/CausalOps/tests/memory/test_mcp_tools.py, /home/anant_gupta/projects/hub/CausalOps/CLAUDE.md, /home/anant_gupta/projects/hub/CausalOps/.gitignore
- Files deleted: (none)
- Commands run: .venv/bin/python -m pytest tests/memory/test_mcp_tools.py -v 2>&1 | tail -40, set -a && source .env && set +a && python -c "
import os
key = os.getenv('SUPABASE_SERVICE_ROLE_KEY','')
print('SUPABASE_URL set:', bool(os.getenv('SUPABASE_URL')))
print('key looks real:', bool(key) and 'your-' not in key)
", set -a && source .env && set +a && .venv/bin/python -c "
import os
key = os.getenv('SUPABASE_SERVICE_ROLE_KEY','')
print('SUPABASE_URL set:', bool(os.getenv('SUPABASE_URL')))
print('key looks real:', bool(key) and 'your-' not in key)
", set -a && source .env && set +a && .venv/bin/python -m pytest tests/memory/test_mcp_bridge.py -v -m integration 2>&1 | tail -40, set -a && source .env && set +a && .venv/bin/python -m pytest tests/memory/ -v 2>&1 | tail -70, .venv/bin/python -m pytest tests/ -m "not integration and not kafka" 2>&1 | tail -20, .venv/bin/python -m ruff check tests/memory/test_mcp_tools.py tests/memory/test_mcp_bridge.py, .venv/bin/python -m pyright tests/memory/test_mcp_bridge.py 2>&1 | tail -30, set -a && source .env && set +a && .venv/bin/python -c "
from memory.store import SupabaseMemoryStore
import sys
sys.path.insert(0, 'src')
" 2>&1
cd /home/anant_gupta/projects/hub/CausalOps/src && set -a && source ../.env && set +a && ../.venv/bin/python -c "
from memory.store import SupabaseMemoryStore
store = SupabaseMemoryStore()
runs = store._client.table('memory_runs').select('run_id').like('run_id', 'mcp-bridge-%').execute()
entities = store._client.table('memory_entities').select('entity_value').like('entity_value', 'mcp-bridge-%').execute()
edges = store._client.table('memory_entity_edges').select('source_run_id').like('source_run_id', 'mcp-bridge-%').execute()
print('leftover runs:', runs.data)
print('leftover entities:', entities.data)
print('leftover edges:', edges.data)
"
, cd /home/anant_gupta/projects/hub/CausalOps && git diff CLAUDE.md && echo "---GITIGNORE---" && git diff .gitignore && echo "---STATUS---" && git status --short, git diff tests/memory/test_mcp_tools.py | head -60
- Tool call tally: Agent (1), Bash (11), Edit (4), ExitPlanMode (1), Read (3), TaskCreate (6), TaskUpdate (8), ToolSearch (2), Write (2)


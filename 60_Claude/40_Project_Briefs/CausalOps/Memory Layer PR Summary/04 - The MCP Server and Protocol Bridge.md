---
type: project
status: complete
created: 2026-07-09
tags: [causalops, memory-layer, mcp, testing, protocol]
---

# The MCP Server and Protocol Bridge

> [!info] This note goes deep on one specific, easy-to-underestimate distinction: the difference between *testing that a function works* and *testing that the protocol wrapping it works*. Getting this distinction right was one of the more valuable pieces of engineering judgment in this whole project.

## What MCP Is, Mechanically — Not Just Conceptually

The **Model Context Protocol** (MCP) is the mechanism by which an AI agent — Claude Desktop, Claude Code, or any other MCP-compatible client — discovers and calls tools exposed by an external server. It is a specific, structured JSON-RPC-style protocol, not a loose convention:

1. **Handshake / initialization** — the client connects and the server responds with its capabilities.
2. **Tool discovery** — the client asks "what tools do you have?" (`list_tools`) *before* calling any of them. The server responds with each tool's name, description, and a formal JSON Schema describing its expected arguments.
3. **Tool invocation** — the client sends a structured call (tool name + arguments as JSON), which the server validates *against the schema from step 2* before executing anything.
4. **Structured response** — the server returns results in a defined content format (text, structured JSON, or other content blocks), not just a raw Python return value.

A server can expose tools correctly *as Python functions* while the MCP wrapping around them is subtly broken — wrong transport, wrong port, a tool registered under a mismatched name, a schema mismatch between what the client expects and what the function actually accepts — and a test that only calls the underlying Python function directly would never catch any of that, because it skips steps 1–3 entirely.

## Why This Distinction Mattered Here, Concretely — Not Hypothetically

Before this PR, `tests/memory/test_mcp_tools.py` looked like a reasonable MCP test. It mocked `SupabaseMemoryStore` and called `mcp_server.search_similar_incidents("...", k=2)` directly:

```python
def test_search_similar_incidents_delegates_to_store() -> None:
    mock_store = MagicMock()
    mock_store.search_similar_runs.return_value = [{"run_id": "run-1"}]
    with patch.object(mcp_server, "SupabaseMemoryStore", return_value=mock_store):
        result = mcp_server.search_similar_incidents("lateral movement", k=2)
    mock_store.search_similar_runs.assert_called_once_with("lateral movement", k=2)
```

This *is* a valid, useful unit test — it proves the tool wrapper correctly delegates to the store. But it is not a test of the MCP server *as an MCP server*. It never opens a client session, never goes through tool discovery, never exercises argument validation against the tool's declared schema.

Meanwhile, the actual deployed server had a **real, live bug** in exactly the part this kind of test can't see: its `__main__` block silently ignored `MCP_HOST`/`MCP_PORT` for the SSE transport, meaning the Docker-deployed server was completely unreachable despite the container appearing to run fine (full fix in [[02 - The Persistent Memory Layer, Component by Component]] and [[03 - Supabase Schema, Migrations & Data Layer]]). **That specific class of bug is exactly the kind a protocol-level test would have caught, and a function-level test structurally cannot.**

## The Fix: Two New, Genuinely Different Kinds of Test

### 1. In-memory protocol tests (fast, no credentials) — added to `test_mcp_tools.py`

```python
async def test_list_tools_exposes_all_four_tools():
    async def _list():
        async with Client(mcp_server.mcp) as client:
            tools = await client.list_tools()
            return [tool.name for tool in tools]
    names = asyncio.run(_list())
    assert set(names) == {
        "search_similar_incidents", "get_entity_relationships",
        "get_asset_timeline", "write_run_to_memory",
    }
```

Passing the live `FastMCP` object *directly* to `fastmcp.Client` (rather than a URL string) makes the client infer an **in-memory transport** — no Docker, no network socket, but the *same protocol layer* as the real deployment: real tool discovery, real JSON-schema argument validation, real response serialization. This is the key insight that makes rigorous MCP testing cheap: you don't need a running server process to test the protocol correctly, you just need the server *object*, in-process.

**What this actually returns, concretely** (verified live before writing any test code) — a `call_tool()` response is a structured `CallToolResult`, not a raw Python value:

```python
CallToolResult(
    content=[TextContent(type='text', text='[{"run_id":"run-1","similarity":0.9}]')],
    structured_content={'result': [{'run_id': 'run-1', 'similarity': 0.9}]},
    data=[{'run_id': 'run-1', 'similarity': 0.9}],   # <- the parsed Python object
    is_error=False,
)
```

`result.data` is what a caller actually reads — this is the exact shape confirmed by running the real client against the real server object, *before* deciding how to write the test, not assumed from documentation.

### 2. A live, real-infrastructure protocol round trip — a brand-new file, `test_mcp_bridge.py`

This test does something no prior test in the codebase did: it opens a real `Client` session and calls `write_run_to_memory` followed by `search_similar_incidents`, **through the actual MCP protocol**, against the **real, live Supabase project**:

```python
async def _round_trip():
    async with Client(mcp_server.mcp) as client:
        write_result = await client.call_tool("write_run_to_memory", {"run_artifact": {...}})
        search_result = await client.call_tool("search_similar_incidents", {"description": ..., "k": 3})
        return write_result.data, search_result.data

write_data, search_data = asyncio.run(_round_trip())
assert write_data["run_id"] == run_id
assert any(row.get("run_id") == run_id for row in search_data)
```

— with the same tagged-UUID-and-cleanup discipline used elsewhere in the test suite (a unique tag like `mcp-bridge-{uuid}` prefixes every value written, and a fixture teardown deletes exactly those rows afterward), so repeated runs never pollute production data. This is a strictly stronger guarantee than either "the function works" (the old test) or "the protocol works against a mock" (test 1 above) — it proves the whole chain, end to end, for real: real embedding call, real database write, real database read, real protocol serialization on both sides of the round trip.

**This exact pattern was proven by hand before a single line of test code was written** — a live smoke script was run first (write → search → assert the written run appears in search results → clean up), confirmed working, and *then* turned into the formal test. This "prove it live first, write the test second" discipline shows up repeatedly in this project — see [[06 - Testing & Verification Methodology]] for why that ordering matters, and for other examples of it.

## The Live Deployment Verification (Docker/SSE) — the Third, Independent Layer of Proof

Separately from the in-process protocol tests above, the actual Docker-deployed server was verified live, end to end, in its real deployed form — not simulated:

```
$ docker ps --filter name=mcp
NAMES             STATUS       PORTS
causalops-mcp-1   Up 3 hours   0.0.0.0:8001->8001/tcp

$ curl -sv --max-time 3 http://localhost:8001/sse
* Connected to localhost (::1) port 8001
> GET /sse HTTP/1.1
< HTTP/1.1 200 OK
< content-type: text/event-stream; charset=utf-8

$ docker logs --tail 30 causalops-mcp-1
INFO:     Starting MCP server 'causalops-memory' with transport 'sse' on http://0.0.0.0:8001/sse
INFO:     Uvicorn running on http://0.0.0.0:8001
INFO:     172.18.0.1:60662 - "GET /sse HTTP/1.1" 200 OK
```

The `Up 3 hours` detail matters specifically: it confirms the container is stably running, not crash-looping and restarting (which Docker's `restart: unless-stopped` policy would otherwise make look superficially "up" between crashes). This confirms the fix to the `MCP_HOST`/`MCP_PORT` bug actually works in the environment it will actually run in (Docker Compose), not just in a unit test's simulated in-memory environment.

## The Automated Code Review Round (GitHub Copilot) — What It Caught Here Specifically

An automated PR review pass caught two real, previously-unnoticed problems, both in `setup-claude-code.sh` (a contributor-onboarding script, not the server itself, but one whose incorrectness would directly mislead any new contributor trying to connect to the memory server):

1. The generated `.mcp.json` pointed at `http://localhost:8000/mcp` — an HTTP bridge into the main FastAPI app that was never built, and never should be (see the "never mounted in api.py" rule in [[02 - The Persistent Memory Layer, Component by Component]]).
2. A generated test-instructions file (`commands/test-memory.md`) told a new contributor to `curl -X POST http://localhost:8000/mcp/call-tool` — the same non-existent endpoint.

Both were fixed by pointing the generated config at the real stdio-spawned server instead:

```json
{
  "mcpServers": {
    "causalops-memory": {
      "command": "python",
      "args": ["-m", "memory.mcp_server"],
      "cwd": "src",
      "env": { "MCP_TRANSPORT": "stdio" }
    }
  }
}
```

Investigating *why* these were wrong surfaced that the entire onboarding script predated the "standalone MCP server" architecture decision — it still described mounting the server inside `api.py`, still referenced Azure embeddings instead of Gemini, and still checked for package versions (`fastmcp==3.2.4`) that are actually uninstallable alongside the pinned Supabase client version (`fastmcp>=3.4` requires `websockets>=15`, while `supabase==2.15.2`'s realtime dependency pins `websockets<15` — a real, verified version conflict, not a guess). All of this was corrected in the same pass, not just the two specific lines Copilot flagged — a deliberate choice to fix the underlying staleness rather than patch only the symptom.

## The Takeaway, for a Meeting or an Interview

If asked "how do you know the MCP integration actually works, not just that the code compiles" — this is the answer: there are now **three independent layers of proof**, each catching a different class of failure the others structurally cannot —

1. A mocked-store protocol test (fast, no credentials, proves tool discovery and argument marshaling work)
2. A live in-memory protocol round trip against real Supabase (proves the whole chain works for real, without needing a deployed process)
3. A live Docker/SSE deployment check (proves the actual production deployment configuration works, which the other two layers cannot verify, since they never touch the container or its port binding)

## Where to Go Next

For the reconciliation work that happened around this same code during the branch rebase: [[05 - Reconciling With Main — The Rebase Story]].
For the full testing philosophy this project follows, and why "prove it live first" is the recurring theme: [[06 - Testing & Verification Methodology]].

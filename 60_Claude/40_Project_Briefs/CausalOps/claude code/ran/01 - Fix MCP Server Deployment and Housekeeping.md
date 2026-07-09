---
tags: [causalops, prompt, memory-layer, claude-code, mcp, bugfix]
created: 2026-07-08
task: mcp-server-port-fix
model: claude-sonnet-4-6
---

# Prompt 1 — Fix the Standalone MCP Server's Docker/SSE Deployment

> Copy the fenced prompt into a fresh Claude Code session. See [[00 - Memory Layer Completion — Index]] for how this fits with the other three prompts.

## Why This Exists

[Independent Review artifact](https://claude.ai/code/artifact/995b5795-02d0-44a8-98bd-3921844d1cf1), Finding 1: `src/memory/mcp_server.py`'s `__main__` block only reads `MCP_TRANSPORT`. It never reads `MCP_PORT`, and never passes `host=`/`port=` to `mcp.run()`. Verified directly against the installed `fastmcp==3.4.2` package this session:

- `fastmcp.settings` env prefix is `FASTMCP_`, not `MCP_` — so `MCP_PORT` in `docker-compose.yml` is silently ignored by the library.
- Default port is **8000**, default host is **127.0.0.1**.
- `docker-compose.yml`'s `mcp` service maps `8001:8001` and sets `MCP_PORT: "8001"` — neither takes effect. The container starts the SSE server bound to `127.0.0.1:8000`, which is unreachable both because of the port mismatch *and* because loopback binding inside a container doesn't accept connections forwarded from the Docker host.
- Critically: `run_stdio_async()` (used by the `stdio` transport, i.e. this same file when launched via `.mcp.json` for Claude Code/Desktop) does **not** accept `host`/`port` kwargs at all — passing them unconditionally would break the stdio path that already works. The fix must branch on transport.

## Hard Rules

- Do not change anything under `src/memory/store.py`, `embedder.py`, `extractor.py`, `nodes.py` — this prompt is scoped to `mcp_server.py` and its Docker wiring only.
- Do not touch `.mcp.json`'s `hivemind-memory`/`causalops-memory` stdio entry — it has no port config and must keep working unchanged.
- Verify by actually curling the running container. An import check (`python -c "from memory.mcp_server import mcp"`) proves nothing about this bug — it never touches `mcp.run()`.

## Implementation Order

1. Read `src/memory/mcp_server.py` in full (72 lines) and `docker-compose.yml`'s `mcp` service block (currently lines 79-94).

2. Fix the `__main__` block:
   ```python
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
   The `stdio` branch must stay exactly as it is today — confirmed this session that `run_stdio_async()`'s signature is `(show_banner, log_level, stateless)` and raises on unexpected kwargs.

3. Check whether `docker-compose.yml`'s `mcp` service needs an `MCP_HOST` entry added (it currently only sets `MCP_TRANSPORT` and `MCP_PORT`). Since the code above defaults `MCP_HOST` to `0.0.0.0`, an explicit compose entry is optional — add one only if you decide explicit-over-implicit is worth the extra line; either is acceptable, but say which you picked and why.

4. Rebuild and start only the `mcp` service:
   ```bash
   docker-compose up --build -d mcp
   ```
   Confirm it depends on `api` being healthy per the existing `depends_on` block — if `api` isn't already running, bring it up first (`docker-compose up -d api`) or the `mcp` container will sit waiting.

5. **Verify for real, from outside the container.** The transport is SSE, so a plain `curl` will hang open on a streaming connection rather than returning — use a short timeout and inspect headers, don't wait for it to close:
   ```bash
   curl -sv --max-time 3 http://localhost:8001/sse 2>&1 | head -20
   ```
   Expect: a successful TCP connect (`Connected to localhost (127.0.0.1) port 8001`), an HTTP response with `content-type: text/event-stream`, not `Connection refused` and not a response arriving from the wrong port. If it fails, the fix is incomplete — do not report success on the basis of the code merely importing cleanly.

6. Run `docker-compose logs mcp --tail 30` and confirm no startup traceback.

7. Confirm the stdio path is unaffected: `cd src && MCP_TRANSPORT=stdio timeout 3 python -m memory.mcp_server; echo "exit code: $?"` — it should start and only exit via the timeout (not crash immediately with a TypeError about unexpected kwargs).

8. Housekeeping, while you're in the repo root (unrelated to the MCP bug, but trivial and flagged by the review):
   - `git status` will show an untracked file literally named `t"` (13KB, turns out to be `less`'s help text — harmless leftover from an earlier terminal session) and an untracked `package-lock.json` at the repo root. There is no `package.json` at the repo root (only `app/package.json`), so the root-level lock file is almost certainly an accidental `npm install` run from the wrong directory. Delete both: `rm './t"' package-lock.json`. Confirm `git status` is clean of these two afterward. Do not touch anything else `git status` reports.

9. Run `ruff check src/memory` and `pyright src/memory` — both must stay clean (they were clean before this change; if either regresses, fix it before reporting done). If bare `ruff`/`pyright`/`python` aren't found on `PATH`, this repo's tools live in `.venv/bin/` — use `.venv/bin/<tool>` instead.

## Report Back

List exactly what changed, paste the actual `curl -sv` output from step 5, and confirm the stdio smoke test from step 7. If the curl verification fails, say so explicitly rather than reporting the fix as complete — this is the one thing the prior implementation pass got wrong by asserting success without live verification.

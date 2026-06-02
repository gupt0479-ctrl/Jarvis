#!/usr/bin/env python3
"""jarvis-memory MCP server.

Exposes the Jarvis note registry to any MCP client (Claude Code, etc.) as a set
of tools. This is the skeleton: status and keyword search work today against the
registry built by registry.py. Semantic search, graph queries, conversation
memory, and the answer engine from the three-month plan are added here as new
@mcp.tool() functions over time — the registry schema already has their tables.

Run standalone for a smoke test:
    python server.py        # starts the stdio MCP server

Configured in .mcp.json as the `jarvis-memory` server. Requires `pip install mcp`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import registry  # noqa: E402  (local module, after sys.path tweak)

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:  # pragma: no cover
    raise SystemExit(
        "jarvis-memory requires the 'mcp' package. Install it with: pip install mcp"
    )

mcp = FastMCP("jarvis-memory")


@mcp.tool()
def jarvis_status() -> str:
    """Summarize the Jarvis note registry: counts by type, track, and conversations."""
    return registry.status_text(registry.vault_root())


@mcp.tool()
def jarvis_search(query: str, limit: int = 10) -> str:
    """Keyword search over indexed note titles and paths. Returns matching note paths.

    Semantic search is planned (see registry.search_text TODO and schema.sql chunks)."""
    return registry.search_text(registry.vault_root(), query, limit)


@mcp.tool()
def jarvis_reindex() -> str:
    """Rebuild the note index from the current vault state and report the count."""
    count = registry.index(registry.vault_root())
    return f"Reindexed {count} notes."


if __name__ == "__main__":
    mcp.run()

---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - mcp
source_url: https://github.com/punkpeye/awesome-mcp-servers
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Awesome MCP Servers

**What it is:** The canonical community-maintained index of MCP (Model Context Protocol) servers — the go-to reference for finding servers that connect Claude to external tools, APIs, and data sources.

**What it actually does:** A curated README organized by category: databases, file systems, browser automation, communication tools, code execution, search, memory, monitoring, and more. Each entry links to the server repo with a brief description. The list covers both official servers (from Anthropic, Google, GitHub, etc.) and community-built ones.

**Why it matters for this vault/workflow:** Every time Jarvis or a Claude Code workflow needs to connect to a new external service — a database, a search API, Slack, GitHub, a browser — this is the first place to check for an existing MCP server before building one from scratch. The memory and knowledge-graph categories are directly relevant to Jarvis's architecture. The database servers (SQLite, PostgreSQL, etc.) are relevant to BOOM/UROP data work.

**How to use it:** Treat as a reference. When you need Claude to interact with a new service, `Ctrl+F` in the README or search the VoltAgent/awesome-agent-skills index (which overlaps but has different coverage). Check the repo's last commit date before installing — some MCP servers are abandoned.

**Failure modes / limitations:** The list is large enough that the README is hard to navigate — no interactive search. Entries are not systematically reviewed for security. An MCP server installed into Claude Code gets significant permissions; review server code before connecting to sensitive data. punkpeye/awesome-mcp-servers and glama.ai/mcp/servers both cover similar ground; glama has better discoverability but punkpeye has broader community coverage.

**Verdict:** Bookmark and consult whenever you need a new Claude integration — don't build an MCP server until you've checked this list first.

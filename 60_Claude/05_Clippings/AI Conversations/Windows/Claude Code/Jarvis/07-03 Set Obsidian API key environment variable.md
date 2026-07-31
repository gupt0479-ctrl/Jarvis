---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: windows
title: "Set Obsidian API key environment variable"
started_at: 2026-07-03T19:52:23
ended_at: 2026-07-03T19:53:08
exported_at: 2026-07-31T21:02:54
duration_minutes: 0.7
project: Jarvis
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
session_id: 08839e22-109b-4eaa-beb5-de5686998137
status: raw
turn_count: 2
tools_used:
  PowerShell: 1
tokens:
  input: 10
  output: 770
  cache_creation: 53641
  cache_read: 87021
  total: 141442
cost_usd: 0.359532
model:
  - "claude-sonnet-4-6"
files_touched: []
tags:
  - input
  - ai-conversation
  - claude-code
  - windows
---

# Set Obsidian API key environment variable

## You

The previous session was fixing the local project mcps and this is what it asked me to run in a new session to make sure that all the mcps are working perfectly: `! [Environment]::SetEnvironmentVariable("OBSIDIAN_API_KEY", "[REDACTED]", "User")`

## Claude

Setting the `OBSIDIAN_API_KEY` environment variable at the User scope.

Done — no errors means it was set successfully. The variable is now persisted in your Windows User environment (survives reboots).

To take effect in the current terminal session, you'd need to either open a new terminal or run `$env:OBSIDIAN_API_KEY = "fc476089..."` to load it into the live session. The MCP servers that read this key on startup will pick it up automatically on next launch.

### Tool Calls

- `PowerShell` -- `{"command":"[Environment]::SetEnvironmentVariable(\"OBSIDIAN_API_KEY\", \"[REDACTED]\", \"User\")","description":"Set OBSIDIAN_API_KEY as a persistent User environment variable"}`

## Actions Taken

**Files created:**
_None_

**Files modified:**
_None_

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
_None_



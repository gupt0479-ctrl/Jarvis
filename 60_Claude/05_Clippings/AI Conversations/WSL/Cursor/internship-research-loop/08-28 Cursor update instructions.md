---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl
title: "Cursor update instructions"
started_at: 2026-08-28T20:47:33
ended_at: 2026-08-28T20:47:58
exported_at: 2026-08-28T21:02:00
project: internship-research-loop
cwd: "/home/anant_gupta/projects/work/internship-research-loop"
session_id: f8eb6c76-c273-4ee7-af6c-3406111417ca
status: raw
turn_count: 2
tools_used:
  Subagent: 1
files_changed_count: 0
lines_added: 0
lines_removed: 0
tags:
  - input
  - ai-conversation
  - cursor
  - wsl
---

# Cursor update instructions

## You

<timestamp>Friday, Aug 28, 2026, 8:48 PM (UTC+4)</timestamp>
<user_query>
how to update cursor
</user_query>

## Cursor

Press `Ctrl+Shift+P`, search for **Cursor: Attempt Update**, and select it. Restart Cursor when prompted.

Since you’re using WSL2, Cursor likely runs on Windows—update the Windows Cursor app, not the Linux environment.

If updating fails, download the newest installer from [cursor.com/downloads](https://cursor.com/downloads) and reinstall over the existing version. Your settings should remain intact.

**Tool calls:**

- `Subagent` — `{"description":"Check Cursor update steps","prompt":"Answer how to update Cursor Desktop on Linux/WSL, with concise current official guidance. User is asking generally from Cursor IDE. Include GUI update path and package-specific/manual fallback. Do not modify anything.","subagent_type":"cursor-guid…`

## Actions Taken
- Summary: Press Ctrl+Shift+P, search for Cursor: Attempt Update, and s…
- Files changed (Cursor): 0
- Lines: +0 / -0
- Files touched (from tool calls): (none)
- Commands run: (none)
- Tool call tally: Subagent (1)

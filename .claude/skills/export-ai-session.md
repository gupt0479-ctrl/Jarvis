---
name: exporting-ai-session
description: Reviews recent Claude Code sessions and exports the ones worth keeping into 60_Claude/05_Clippings/AI Conversations/Claude Code/ as redacted markdown transcripts.
---
# export-ai-session

**Usage:** `/export-ai-session`

---

## Why this exists

Claude Code already logs every session end to a global activity file
(`%USERPROFILE%\.claude\jarvis-session-activity.jsonl`, written by the
`SessionEnd` hook in `.claude/settings.json`). Each entry has a `session_id`,
`cwd`, and `transcript_path` pointing at the full raw JSONL transcript in
`~/.claude/projects/<project>/`.

This skill turns that queue into curated vault notes — deliberately not
"export everything," per the vault's context-pack philosophy. Most sessions
aren't worth a permanent note; only export the ones with a decision, a
solved problem, or a design worth remembering.

## Instructions

### 1. Find candidates

- Read `%USERPROFILE%\.claude\jarvis-session-activity.jsonl` (global, not
  project-local — read it with a path like
  `C:\Users\<user>\.claude\jarvis-session-activity.jsonl`).
- Keep only lines where `event == "SessionEnd"` and `in_jarvis == true`.
- Read the exported-session index at
  `30_Order/System/claude-workflow/exported-claude-sessions.json` (a flat
  JSON array of `session_id` strings; treat a missing file as `[]`).
- Drop any candidate whose `session_id` is already in that index.
- Sort remaining candidates newest first, cap at the last ~15 — older
  backlog can be swept in a later pass, don't dump the whole history at once.

### 2. Build a preview per candidate

For each candidate, open its `transcript_path` and find the **first** line
with `"type":"user"` whose `message.content` is a plain string (not an
array — arrays there are tool results, not something the human typed).
Truncate that string to ~150 chars for the preview. Pair it with the
`timestamp` from the activity log entry.

### 3. Ask the user which ones matter

Present the candidates (date + preview) and ask which to export — use
AskUserQuestion with multiSelect if there are a handful, or just ask in
plain text if there are many. Do not auto-export without confirmation;
that's the whole point of this being a curated pipeline instead of the
hook writing notes directly.

### 4. Export each selected session

Run the converter for each chosen `session_id`:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "30_Order/System/claude-workflow/scripts/export-claude-session.ps1" `
  -TranscriptPath "<transcript_path from the activity log entry>" `
  -OutputPath "60_Claude/05_Clippings/AI Conversations/Claude Code/<YYYY-MM-DD> - <short-slug>.md" `
  -SessionId "<session_id>" `
  -Project "Jarvis" `
  -Cwd "<cwd from the activity log entry>"
```

Derive `<short-slug>` from the first user message preview (3-6 words,
kebab-case). If a file with that name already exists, append `-2`, `-3`, etc.

The script already:
- keeps only natural-language `text` blocks (never raw tool commands or
  tool output — that's where most secrets/noise live)
- runs a redaction pass over the kept text for common key/token shapes and
  bare 24+ character alphanumeric strings

It is **not** a guarantee. After export, skim the output yourself before
telling the user it's done — if anything looks like a live secret, redact
it manually and flag it to the user so they can rotate the credential.

### 5. Update the exported index

Append each exported `session_id` to
`30_Order/System/claude-workflow/exported-claude-sessions.json` so it
isn't offered again next time. Create the file (`[]`) if it doesn't exist
yet, then append and write back as valid JSON.

### 6. Report back

Tell the user, in a few lines:
- how many sessions were exported and to which files
- anything you had to hand-redact beyond what the script caught
- how many candidates were skipped (declined) and roughly how large the
  remaining unexported backlog is

## Scope note

This only covers Claude Code, because it's the only tool in this vault's
AI stack that writes structured local transcripts a script can parse.
Claude Desktop, ChatGPT, Gemini, and similar live in the vendor's cloud
account with nothing local to read — those stay manual (copy/paste or
platform export) until/unless the user wants a browser-based capture tool,
which is a different and more fragile build. Cursor, Codex, and Kiro store
transcripts in their own formats under `20_Progress/AI/Codex`,
`20_Progress/AI/Cursor`, `20_Progress/AI/Kiro` — extending this pipeline to
them means writing a parser per format, not reusing this script as-is.

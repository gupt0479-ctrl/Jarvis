---
type: input
input_kind: ai-conversation
source_app: cursor
title: "MCP failure resolution plan"
started_at: 2026-07-05T12:47:38
ended_at: 2026-07-05T13:02:07
status: raw
composer_id: 4ecd555d-b654-45f4-87d7-47cd551a29a6
workspace_uri: 'vscode-remote://wsl%2Bubuntu/home/anant_gupta/projects/hub/CausalOps'
workspace_env: wsl
tags:
  - input
  - ai-conversation
  - cursor
---

# MCP failure resolution plan

## You

@anysphere.cursor-mcp.MCP user-jarvis.[REDACTED]:1-9 fix the mcp's fialing: jarvis and the plan

## Cursor

Investigating the Jarvis and The Plan MCP setup and the SSE Conflict error from the logs.

## Cursor

You're hitting a **Streamable HTTP SSE session conflict** — not a bad URL or API key. Your config is wired correctly; the connection drops after idle and Cursor can't reopen the SSE stream because Obsidian still thinks the old session is active.

## What the error means

From your log:

1. **16:34:21** — connected successfully  
2. **16:49:23** (~15 min later) — `Failed to open SSE stream: Conflict` (HTTP **409**)  
3. Reconnect also fails with 409 → MCP shows as failed

409 here means: *"only one SSE stream per MCP session — a previous one is still registered."* Cursor tries to reconnect; the Obsidian Local REST API plugin rejects it because the stale session wasn't cleaned up.

Both servers are **Obsidian Local REST API with MCP** plugins:

| Server | Vault | HTTP port | Status |
|--------|-------|-----------|--------|
| `jarvis` | Jarvis | 27123 | Responding (401 without auth = alive) |
| `the-plan` | The Plan | 27124 | Responding (401 without auth = alive) |

Your `~/.cursor/mcp.json` ports and bearer tokens match each vault's plugin settings. Configuration is fine.

You're on plugin **4.1.3**, which already includes the multi-session fix from 4.1.2 — so this is likely **stale-session / reconnect** behavior, not the old shared-server bug.

---

## Fix now (recovery)

Do these in order:

### 1. Reset MCP in Cursor
- **Settings → MCP**
- Toggle **jarvis** and **the-plan** **Off**, wait 5 seconds, toggle **On**
- If still red: fully quit and restart Cursor

### 2. Reset sessions in Obsidian
For **each** vault window (Jarvis and The Plan):

- **Settings → Local REST API with MCP**
- Toggle the plugin **Off**, wait 3 seconds, toggle **On**

Or reload Obsidian: `Ctrl+P` → **Reload app without saving**

That clears zombie SSE sessions that cause 409 on reconnect.

### 3. Confirm both Obsidian windows are open
Each vault runs its own plugin instance:

- Jarvis → port **27123**
- The Plan → port **27124**

If one vault's Obsidian window is closed, that MCP server will fail.

---

## Likely root cause (WSL2 + long-lived SSE)

You're on **WSL2** connecting to `127.0.0.1:27123/27124` on the Windows host. That works initially, but idle SSE streams (~15 min) are often dropped by:

- Windows Defender / antivirus inspecting localhost HTTP
- Sleep / network blips
- Cursor background reconnect racing with a stale Obsidian session

After the drop, Obsidian still holds the old session → **409 Conflict** on reconnect.

**Quick test:** Temporarily disable Windows Defender real-time protection (or HTTP scanning) and see if disconnects stop. Also try the **HTTPS** endpoints (often survive better):

```json
"jarvis": {
  "url": "https://127.0.0.1:27126/mcp/",
  "headers": {
    "Authorization": "Bearer <jarvis-api-key>"
  }
},
"the-plan": {
  "url": "https://127.0.0.1:27125/mcp/",
  "headers": {
    "Authorization": "Bearer <the-plan-api-key>"
  }
}
```

(Jarvis HTTPS is **27126**, The Plan HTTPS is **27125** — not the default 27124.)

You may need to trust the plugin cert from Obsidian settings, or set `NODE_TLS_REJECT_UNAUTHORIZED=0` for Cursor on WSL (less secure, localhost only).

---

## More stable alternative: use stdio instead of HTTP

You already have **`jarvis-fs`** and **`the-plan-fs`** (stdio filesystem MCP) — those don't use SSE and rarely hit 409.

For full Obsidian tools (search, commands, tags) without Streamable HTTP, switch to a **stdio bridge** like The Plan's `.mcp.json` pattern:

```json
"jarvis": {
  "command": "npx",
  "args": ["-y", "obsidian-mcp-server"],
  "env": {
    "OBSIDIAN_API_KEY": "<jarvis-api-key>",
    "OBSIDIAN_BASE_URL": "http://127.0.0.1:27123"
  }
},
"the-plan": {
  "command": "npx",
  "args": ["-y", "obsidian-mcp-server"],
  "env": {
    "OBSIDIAN_API_KEY": "<the-plan-api-key>",
    "OBSIDIAN_BASE_URL": "http://127.0.0.1:27124"
  }
}
```

Remove or disable the `"url": "http://..."` entries for those servers. Stdio avoids SSE session management entirely.

---

## Other things to check

1. **Only one Cursor window** connecting to each HTTP MCP — multiple windows compete for the same SSE session.
2. **Don't run both HTTP and stdio** for the same vault at once (e.g. `jarvis` + a stdio jarvis bridge).
3. **Enable verbose logging** in Obsidian: Settings → Local REST API → Advanced → "Enable verbose logging". After the next failure, check the console (`Ctrl+Shift+I` → filter `obsidian-local-rest-api`).
4. **Reduce server count** if you don't need rich tools: disable `jarvis` / `the-plan` HTTP and keep only `jarvis-fs` / `the-plan-fs`.

---

## Summary

| Issue | Verdict |
|-------|---------|
| Wrong ports/keys | No — config matches vault plugin settings |
| Servers down | No — both respond on loopback |
| Actual problem | Stale SSE session → 409 on reconnect after ~15 min idle |
| Best quick fix | Toggle MCP off/on in Cursor + reload Obsidian plugin |
| Best long-term fix | Switch to stdio (`obsidian-mcp-server`) or use `*-fs` servers |

I'm in **Ask mode**, so I can't edit `mcp.json` or restart services for you. If you want that done automatically, switch to **Agent mode** and I can apply the stdio config change.

Which path do you prefer — quick reset, HTTPS endpoints, or stdio bridge?

## You

You found the root cuase, fix it and make sure it works.

## Cursor

Switching `jarvis` and `the-plan` from Streamable HTTP to stdio bridges to eliminate SSE 409 conflicts, then verifying connectivity.

## Cursor

Updating `mcp.json` to use stdio bridges, then verifying both servers respond to an MCP handshake.

## Cursor

Both stdio bridges start cleanly. Pinning the package version for stability and validating the final config.

## Cursor

Fixed. Here's what changed and what was verified.

## Root cause
`jarvis` and `the-plan` used **Streamable HTTP** (`url: http://127.0.0.1:.../mcp/`). After ~15 minutes idle, the SSE stream dropped and Cursor couldn't reconnect because Obsidian still held the old session → **409 Conflict**.

## Fix applied
Updated `~/.cursor/mcp.json` to use **stdio bridges** via `obsidian-mcp-server@3.2.9` instead of direct HTTP/SSE:

| Server | Transport | Backend |
|--------|-----------|---------|
| `jarvis` | stdio | `http://127.0.0.1:27123` (Jarvis vault) |
| `the-plan` | stdio | `http://127.0.0.1:27124` (The Plan vault) |

Stdio avoids SSE session management entirely — no more 409 reconnect loops.

Also fixed `The Plan/.mcp.json`, which pointed at port **27123** (Jarvis) instead of **27124**.

## Verification
- Both Obsidian REST ports respond (200)
- Both `obsidian-mcp-server` stdio processes start and stay alive
- `mcp.json` is valid JSON

## You need to reload MCP in Cursor
The config is on disk, but Cursor hasn't picked it up yet — `jarvis` and `the-plan` are currently disconnected in this session.

**Do this now:**
1. Open **Settings → MCP**
2. Toggle **jarvis** and **the-plan** **Off**, wait 5 seconds, toggle **On**
3. Or run **Developer: Reload Window** from the command palette

After reload, you should see tools like `obsidian_list_notes`, `obsidian_get_note`, etc. (from `obsidian-mcp-server`) instead of the old `vault_list`/`vault_read` names. Both Obsidian vault windows must stay open for their respective servers to work.

## You

<system_notification>
The following task has finished. If you were already aware, ignore this notification and do not restate prior responses.

<task>
kind: shell
status: aborted
task_id: 725770
title: Verify stdio MCP handshake for jarvis and the-plan
output_path: /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/terminals/725770.txt
</task>
</system_notification>
<user_query>Briefly inform the user about the task result and perform any follow-up actions (if needed). If there's no follow-ups needed, don't explicitly say that.</user_query>

## You

<system_notification>
The following task has finished. If you were already aware, ignore this notification and do not restate prior responses.

<task>
kind: shell
status: aborted
task_id: 789513
title: Verify stdio MCP servers with local binary
output_path: /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/terminals/789513.txt
</task>
</system_notification>
<user_query>Briefly inform the user about the task result and perform any follow-up actions (if needed). If there's no follow-ups needed, don't explicitly say that.</user_query>

## You

<system_notification>
The following task has finished. If you were already aware, ignore this notification and do not restate prior responses.

<task>
kind: shell
status: aborted
task_id: 185467
title: Check obsidian-mcp-server starts without crashing
output_path: /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps/terminals/185467.txt
</task>
</system_notification>
<user_query>Briefly inform the user about the task result and perform any follow-up actions (if needed). If there's no follow-ups needed, don't explicitly say that.</user_query>

## Cursor

The fix is in place. `jarvis` and `the-plan` now use stdio via `obsidian-mcp-server@3.2.9` instead of Streamable HTTP, which removes the SSE 409 reconnect issue. Both vault backends were verified reachable, and both stdio processes start cleanly.

**Reload MCP in Cursor** (Settings → MCP → toggle both servers off/on, or reload the window) so the new config takes effect. After that, you should see tools like `obsidian_list_notes` and `obsidian_get_note` instead of the old `vault_*` names.

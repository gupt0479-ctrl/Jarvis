---
type: input
input_kind: ai-conversation
source_app: cursor
title: "Kiro and cursor MCP configuration analysis"
started_at: 2026-05-28T15:42:49
ended_at: 2026-05-28T15:42:56
status: raw
composer_id: 077867c6-5cef-480f-a2a3-5b20db5dd0f2
workspace_uri: 'file:///d%3A/Users/_Anant/10_Areas/Documents/Jarvis'
workspace_env: windows
tags:
  - input
  - ai-conversation
  - cursor
---

# Kiro and cursor MCP configuration analysis

## You

I have multiple ai platforms to work on now: Claude pro, cursor pro, kiro pro, copilot pro, lovable pro, eleven labs pro and used to have chat gpt pro(codex). Here is a detailed analysis of what kiro currently has: 
```
Now let me also check the global `.mcp.json` in your Windows home directory (the one shared across all AI tools):

Let me also check the Kiro global home directory structure:

Now let me read the steering files and the argv.json:

Alright, I've now read through everything. Here's my full analysis of your Kiro configuration:

---

## The Confusion: MCP Config Layering

You have **4 places** defining MCP servers, and they overlap heavily:

| Location | What's in it | Role |
|----------|-------------|------|
| `C:\Users\Anant Gupta\.kiro\settings\mcp.json` | GitHub (HTTP), Obsidian (stdio), Supabase power | Kiro global (user-level) |
| `D:\...\Jarvis\.kiro\settings\mcp.json` | Obsidian, Context7, OpenAI Docs, Playwright | Kiro workspace-level |
| `D:\...\Jarvis\.mcp.json` | Obsidian, Context7, Playwright, OpenAI Docs | Cross-tool global (Claude Code, Cursor, etc.) |
| `C:\Users\Anant Gupta\.mcp.json` (couldn't read, but you said it exists) | Presumably similar | Cross-tool global at Windows home |

---

## Problems I See

**1. The global Kiro config (`~/.kiro/settings/mcp.json`) is malformed.**

The `obsidian` server is nested *inside* the `github` object instead of being a sibling. This is a JSON structure bug:

```json
"github": {
  "url": "...",
  "headers": { ... },
  "obsidian": { ... }  // ← WRONG: nested inside github
}
```

Obsidian should be at the top level of `mcpServers`, not inside `github`. This means your global Kiro config is only actually loading GitHub (and even that might be broken depending on how Kiro parses the extra key).

**2. Obsidian is defined 3 times** (global Kiro, workspace Kiro, workspace `.mcp.json`) — all with the same command and API key. The workspace `.mcp.json` version is missing the API key though.

**3. Context7, Playwright, and OpenAI Docs are duplicated** between the workspace Kiro config and the workspace `.mcp.json`. Since Kiro reads its own `settings/mcp.json` but does NOT read `.mcp.json` (that's for Claude Code/Cursor), these are independent — not conflicting, but redundant if you're maintaining both.

**4. Your GitHub token is hardcoded in the global Kiro config.** That's a secret sitting in plain text. The GitHub MCP via Copilot auth header approach works, but be aware it's exposed.

**5. The workspace `.mcp.json` Obsidian entry has no API key** — it relies on the tool's default or env var. The Kiro workspace config does have the key. So Claude Code using `.mcp.json` might fail to auth with Obsidian unless the key is set elsewhere.

---

## Do You Need Both `.mcp.json` AND `.kiro/settings/mcp.json`?

**Short answer: Yes, unfortunately.**

- `.mcp.json` → read by Claude Code, Cursor, and other tools that follow the shared MCP config convention.
- `.kiro/settings/mcp.json` → read only by Kiro. Kiro does NOT read `.mcp.json`.

They're separate ecosystems. If you want the same servers available in both Kiro and Claude Code, you need both files. The alternative is to only define servers in one place and accept the other tool won't have them.

---

## What I'd Recommend Cleaning Up

1. **Fix the global Kiro config** — pull `obsidian` out of the `github` object.
2. **Decide on a single source of truth for this workspace**: since Kiro needs its own config anyway, keep the workspace `.kiro/settings/mcp.json` as the Kiro-specific one, and `.mcp.json` as the Claude Code/Cursor one.
3. **Add the Obsidian API key to `.mcp.json`** if Claude Code needs it.
4. **Remove the Obsidian definition from the global Kiro config** — it's workspace-specific (tied to this vault's local REST API), so it belongs at workspace level only.

Want me to fix the global Kiro config and clean up the workspace one? I can propose the exact edits.
```

I provided this prompt to kiro: "I just subscribed to claude pro. We have changed up a lot of things for claude. We have been working on the home directory. Let's do the same for kiro. I was seeing the home directory for kiro and it seems to confuse me. I have wsl and windows here. You have two home directories in both of these os. The wsl directory is practically empty. I want everything to work just perfectly. I have set a global .mcp.json file in my windows directory as well as the wsl directory. I do not need the .kiro .mcp.json file anymore but it does not hurt to have it. What i am aiming to do here is make this particular project clean first. Let's not focus on the home directory for other ai agents, focus only on your home directory: kiro. Analyze each and every setting, file, extensions, etc that you have set up so far. Your task is to read through your settings and tell me what is too confusing. Can u read the global mcps now? This is kiro's user config file: `C:\Users\Anant Gupta\.kiro\settings\mcp.json`, workspace config: `D:\Users\_Anant\10_Areas\Documents\Jarvis\.kiro\settings\mcp.json`. I have a global .mcp.json for all ai platforms in my windows and wsl. Do i really need these configs? Can u rad the .mcp.json file globally?". 

What i am asking from you is also the same thing. I want all my ai platforms to read the mcps together. I am going to configure different mcps in each ai platform and they will have their own configs probably. I am struggling juggling between my subscriptions here. I have 3 IDEs to work with. I primarily work on vs code with claude code. I need to upgrade by a lot here. I need to utilize my money. Let's focus on what cursor can do here. Provide me with a detailed analysis similar to kiro for cursor.

## Cursor

I'll analyze your Cursor setup the same way Kiro did — starting with global MCP configs, Cursor-specific settings, and how they overlap across Windows and WSL.

## Cursor

# Cursor Configuration Analysis

I read your global configs, Cursor home directory, Jarvis workspace, plugin cache, and the [official Cursor MCP docs](https://cursor.com/docs/mcp). Here is the same style of audit Kiro gave you, focused on Cursor.

---

## The Core Confusion: Cursor Does Not Read `~/.mcp.json`

This is the single biggest source of mismatch in your setup.

| File | Read by Cursor? | Read by Claude Code? | Read by Kiro? |
|------|-----------------|----------------------|---------------|
| `C:\Users\Anant Gupta\.mcp.json` | **No** | **Yes** | **No** |
| `C:\Users\Anant Gupta\.cursor\mcp.json` | **Yes** (global) | No | No |
| `<project>/.mcp.json` | **No** | **Yes** | No |
| `<project>/.cursor/mcp.json` | **Yes** (project) | No | No |
| `~/.kiro/settings/mcp.json` | No | No | **Yes** |

You built a cross-tool layer in `~/.mcp.json` (Jarvis + The Plan Obsidian HTTP, filesystem servers). That is real and useful — but **only for Claude Code and tools that follow that convention**. Cursor ignores it entirely.

Per Cursor docs, Cursor only loads MCP from:
1. `~/.cursor/mcp.json` (global)
2. `.cursor/mcp.json` (project root)
3. **Marketplace plugins** (bundled MCP + skills)
4. **Built-in servers** (`cursor-app-control`, `cursor-ide-browser`)

There is no documented merge with `~/.mcp.json`. You cannot make all platforms read one file without symlinks or a sync script.

---

## Your MCP Config Layers (5 Places, Overlapping)

| Location | Contents | Who reads it |
|----------|----------|--------------|
| `C:\Users\Anant Gupta\.mcp.json` | `jarvis`, `the-plan` HTTP Obsidian, `jarvis-fs`, `the-plan-fs` | Claude Code (global) |
| `C:\Users\Anant Gupta\.cursor\mcp.json` | **`mcpServers: {}` — empty** | Cursor (global) |
| `Jarvis\.mcp.json` | obsidian (stdio, **no API key**), context7, playwright, openai docs | Claude Code (project) |
| `Jarvis\.kiro\settings\mcp.json` | obsidian + context7 + playwright + openai (with API key) | Kiro (workspace) |
| `The Plan\.mcp.json` | obsidian only (with API key) | Claude Code (project) |

Plus Kiro global (`~/.kiro/settings/mcp.json`) which Kiro already flagged as **malformed** (obsidian nested inside github).

**What Cursor actually has active right now** (this session): not your Obsidian servers — instead:
- Built-in: `cursor-app-control`, `cursor-ide-browser`
- Plugins: Supabase, Vercel, Sanity (from Cursor Marketplace)

So Cursor Pro is currently running **deployment/database CMS plugins**, not your **Obsidian vault MCPs**. That is a major gap if Jarvis is your primary workspace.

---

## Problems I See

### 1. Empty global Cursor MCP while global Claude MCP is well-designed

Your Windows `~/.mcp.json` is actually the cleanest Obsidian setup you have — HTTP endpoints on ports 27123/27124 plus filesystem fallbacks. But `~/.cursor/mcp.json` is empty:

```json
{ "mcpServers": {} }
```

Cursor never sees Jarvis, The Plan, or filesystem access unless you duplicate that config into `.cursor/mcp.json`.

### 2. Jarvis has `.mcp.json` but no `.cursor/mcp.json`

Jarvis has good `.cursor/rules/` (workspace-context, human-writing) but **no** `.cursor/mcp.json`. When you open Jarvis in Cursor:
- Rules load correctly
- Obsidian MCP from `.mcp.json` does **not** load
- You get plugin MCPs (Supabase/Vercel/Sanity) instead, which may be irrelevant to vault work

### 3. Three different Obsidian connection styles

| Config | Method | API key |
|--------|--------|---------|
| Global `~/.mcp.json` | HTTP `127.0.0.1:27123/mcp/` | Bearer token in headers |
| Jarvis `.mcp.json` | stdio `obsidian-mcp-server` via npx | **Missing** — only `OBSIDIAN_BASE_URL` |
| Kiro workspace | stdio npx | Has `OBSIDIAN_API_KEY` |

These are three different stacks for the same vault. The global HTTP approach is simplest; the stdio npx approach is slower and duplicated.

### 4. Plugin MCP is invisible in `mcp.json`

Your active Cursor MCPs come from installed marketplace plugins cached at:
- `~/.cursor/plugins/cache/cursor-public/supabase/`
- `~/.cursor/plugins/cache/cursor-public/vercel/`
- `~/.cursor/plugins/cache/cursor-public/sanity/`

These do not appear in `~/.cursor/mcp.json`. That makes debugging confusing — you look at an empty file and wonder why Supabase tools still show up. Answer: plugins inject MCP separately.

### 5. WSL doubles everything

Cursor has `anysphere.remote-wsl` installed and history for WSL projects (`portfolio`, `opspilot`, etc.). When you work in WSL:
- Windows `~/.cursor/mcp.json` does not apply
- WSL gets its own `~/.cursor/mcp.json` and `~/.mcp.json`
- Your WSL home is mostly empty, so WSL Cursor sessions likely have **no MCP at all**

Pick one primary OS per project type, or mirror configs into both homes.

### 6. Skills are scattered across three trees

| Location | What |
|----------|------|
| `~/.cursor/skills-cursor/` | Cursor built-in skills (canvas, sdk, create-rule, loop, etc.) |
| `~/.agents/skills/` | Microsoft Foundry skills (deploy-model, fine-tuning, agents) |
| Plugin cache | Vercel (20+ skills), Supabase, Sanity skills |

Skills and MCP are coupled in plugins but stored separately from `mcp.json`. Another layer to track.

### 7. Secrets hardcoded in plain text

Across Kiro, `.mcp.json`, and global configs: GitHub PAT, Obsidian API keys, bearer tokens. Your Jarvis `AGENTS.md` correctly says not to surface secrets — but the config files violate that. Move to env vars with `${env:VAR}` interpolation (Cursor supports this in `mcp.json`).

### 8. The Plan is open in Cursor but has no Cursor project config

Cursor's last active window is **The Plan** (`D:\Users\_Anant\10_Areas\Documents\The Plan`). That project has:
- `.mcp.json` (Claude only)
- `.kiro/settings/mcp.json` (Kiro only)
- **No `.cursor/` folder at all**

So your currently open Cursor workspace has zero Cursor-specific rules or MCP.

### 9. Residual IDE/tool config noise

In `%APPDATA%\Cursor\User\settings.json`:
- `kilo-code.*` settings (another AI extension — overlaps with Cursor agent)
- `gitlens.ai.vscode.model: copilot:gpt-4.1` (GitLens AI pointed at Copilot while you pay for Cursor Pro + Claude Pro)
- Biome formatter, pnpm — fine and consistent

User rules (commit protocol, PR workflow, code principles) live in **Cursor's cloud settings**, not in files. That is fine, but they only apply in Cursor — not VS Code + Claude Code.

---

## Cursor Home Directory Map

```
C:\Users\Anant Gupta\.cursor\
├── mcp.json              ← EMPTY (should be your global Cursor MCP)
├── argv.json             ← launch config (defaults only)
├── skills-cursor/        ← built-in agent skills (29 files)
├── plugins/cache/        ← Supabase, Vercel, Sanity marketplace plugins
├── extensions/           ← VS Code extensions (Python, Docker, WSL, Biome, etc.)
└── projects/             ← per-workspace agent state, MCP tool descriptors, transcripts
    ├── empty-window/     ← this chat
    └── d-Users-...-The-Plan/

C:\Users\Anant Gupta\AppData\Roaming\Cursor\User\
└── settings.json         ← editor preferences (not MCP)
```

Jarvis workspace:
```
Jarvis/
├── AGENTS.md, AI_CONTEXT.md, HUMAN_WRITING.md   ← shared cross-tool context ✓
├── .mcp.json                                       ← Claude Code only
├── .kiro/settings/mcp.json                         ← Kiro only
└── .cursor/rules/                                  ← Cursor rules only (no mcp.json!)
```

---

## Do You Need All These Config Files?

**Short answer: yes, unless you automate syncing — but you need fewer duplicates.**

Each tool has its own config surface:

| Tool | MCP config | Rules/context |
|------|-----------|---------------|
| **Cursor** | `~/.cursor/mcp.json` + `.cursor/mcp.json` + plugins | `.cursor/rules/`, user rules (UI), skills |
| **Claude Code** | `~/.mcp.json` + project `.mcp.json` | `CLAUDE.md`, `AGENTS.md` |
| **Kiro** | `~/.kiro/settings/mcp.json` + workspace `.kiro/settings/mcp.json` | steering files |
| **Copilot** | VS Code extension settings, `@mcp` in some setups | `.github/copilot-instructions.md` |

You cannot get one file all tools read. What you *can* do is define roles:

| Layer | Purpose | File |
|-------|---------|------|
| **Shared context** | Vault rules, writing standards, agent guide | `AGENTS.md`, `AI_CONTEXT.md`, `.cursor/rules/` |
| **Claude MCP** | What Claude Code sees globally + per project | `~/.mcp.json`, `<project>/.mcp.json` |
| **Cursor MCP** | What Cursor agent sees globally + per project | `~/.cursor/mcp.json`, `<project>/.cursor/mcp.json` |
| **Kiro MCP** | Kiro-only servers (fix the malformed global!) | Kiro settings files |
| **Cursor plugins** | Vendor MCP + skills (Supabase, Vercel, Sanity) | Marketplace installs |

---

## What Cursor Pro Gives You That Claude Code in VS Code Does Not

Since you primarily work in VS Code + Claude Code, here is where Cursor Pro actually earns its keep:

| Capability | Cursor | Claude Code in VS Code |
|------------|--------|------------------------|
| **Multi-file agent with codebase indexing** | Native, fast | Good, different UX |
| **Subagents / background agents** | Yes (Task tool, cloud agents) | Limited |
| **Built-in browser MCP** | `cursor-ide-browser` | Needs Playwright MCP setup |
| **Canvas** | Rich analytical UI panels | No |
| **Marketplace plugins** | Supabase/Vercel/Sanity with skills + MCP bundled | Claude plugins (different ecosystem) |
| **Automations / hooks** | Cursor hooks, `/loop` skill | Claude hooks (different format) |
| **Project rules** | `.cursor/rules/*.mdc` with globs | `CLAUDE.md`, `AGENTS.md` |
| **Glass mode / split chat+editor** | Yes | No |

**Recommended split of your subscriptions:**

| Subscription | Best use |
|-------------|-----------|
| **Claude Pro + VS Code** | Daily coding in repos, terminal-heavy work, git workflows |
| **Cursor Pro** | Agentic multi-file refactors, vault/Obsidian work with MCP, deployment (Vercel/Supabase plugins), browser testing |
| **Kiro Pro** | If you prefer its steering/spec workflow — but fix MCP first |
| **Copilot Pro** | GitHub.com PR review, Copilot coding agent in repos — not as primary IDE AI if you have Claude + Cursor |
| **Lovable** | Rapid UI prototyping only — do not overlap with Cursor for same project |
| **ElevenLabs Pro** | Voice/audio — orthogonal to coding setup |

---

## Recommended Cleanup (Cursor-focused)

### Step 1: Populate `~/.cursor/mcp.json` from your global `~/.mcp.json`

Copy the jarvis/the-plan HTTP + filesystem servers into Cursor's global config. Use env var interpolation for tokens:

```json
{
  "mcpServers": {
    "jarvis": {
      "url": "http://127.0.0.1:27123/mcp/",
      "headers": {
        "Authorization": "Bearer ${env:OBSIDIAN_JARVIS_KEY}"
      }
    },
    "the-plan": {
      "url": "http://127.0.0.1:27124/mcp/",
      "headers": {
        "Authorization": "Bearer ${env:OBSIDIAN_PLAN_KEY}"
      }
    }
  }
}
```

Set the env vars in Windows User Environment Variables once; both Cursor and Claude can reference them (Claude via `${env:...}` if supported, or keep bearer in Claude config only).

### Step 2: Add `Jarvis/.cursor/mcp.json`

For project-specific servers (context7, playwright) that you want in Cursor but not globally:

```json
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp"
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

Obsidian can stay global (port 27123). No need to duplicate stdio npx obsidian-mcp-server.

### Step 3: Simplify Jarvis `.mcp.json` for Claude Code

Align Claude with the HTTP approach (same as global), drop the broken stdio entry missing API key, or add the key. One Obsidian connection style per vault.

### Step 4: Add `.cursor/rules/` to The Plan

Mirror Jarvis pattern — reference shared `AGENTS.md` / context files so Cursor knows what The Plan is.

### Step 5: Decide on plugin MCPs

Keep Supabase/Vercel/Sanity plugins **only for code projects** that use those stacks. Toggle them off in **Settings → Features → MCP** when working in Jarvis vault sessions to reduce tool clutter.

### Step 6: Fix Kiro global config (same as Kiro's recommendation)

Pull obsidian out of the github object; remove workspace-specific obsidian from Kiro global.

### Step 7: WSL — either commit or ignore

If WSL projects are active: copy `~/.cursor/mcp.json` and `~/.mcp.json` into WSL home. If WSL is dormant, stop maintaining a WSL `~/.mcp.json`.

---

## Summary: What's Confusing

1. **`~/.mcp.json` feels universal but Cursor ignores it** — biggest trap
2. **`~/.cursor/mcp.json` is empty** while plugins silently provide MCP
3. **Jarvis has Cursor rules but no Cursor MCP** — half-configured
4. **Three Obsidian connection methods** for the same vault
5. **Five MCP config locations** with no sync
6. **WSL creates a second home** you are not maintaining
7. **Skills in three directories** plus plugin bundles
8. **Multiple paid AI tools** with overlapping IDE extensions (kilo-code, GitLens AI on Copilot, Cursor agent)

---

## Can I Read the Global `.mcp.json`?

Yes. I read `C:\Users\Anant Gupta\.mcp.json` successfully. It has four servers (jarvis HTTP, the-plan HTTP, jarvis-fs, the-plan-fs). WSL `~/.mcp.json` I could not confirm from this environment — worth checking manually in WSL if you still maintain it.

---

If you want, I can next:
1. **Write the exact `~/.cursor/mcp.json` and `Jarvis/.cursor/mcp.json` files** (with env var placeholders, no hardcoded secrets)
2. **Clean up Jarvis `.mcp.json`** to match the HTTP pattern
3. **Add The Plan `.cursor/rules/`** mirroring Jarvis

Tell me which to do first — I'd start with populating `~/.cursor/mcp.json` since that unlocks Obsidian in Cursor immediately.

## You

Can you read through jarvis right now with the mcp configuration globally? I am not really sure about all the problems that you have provided me with here. Sure, cursor mcp files are not configured but i set it globally so that all ai platoforms can access it. Try to use the mcp tools. If that does not work. Go ahead and set up cursor the same way claude has been set up, claude right now has clean settings and the mcp works. Make sure that you first re analyze each and every single word that you have provided me with, what are the actual issues here? If needed to updated cursor settings, go ahead and do it. Do it all correctly, with no mistakes.

## Cursor

I'll verify whether Jarvis MCP is available in this Cursor session, re-read your global and Claude configs, then fix Cursor only where there's a real gap.

## Cursor

Confirmed: this session has no Jarvis MCP tools—only plugin servers. I'll verify the Obsidian endpoint, then mirror Claude's global config into Cursor.

## Cursor

Jarvis MCP isn't loaded in this session—only plugin servers are. Mirroring Claude's global MCP into Cursor's config and adding the Jarvis project layer.

## Cursor

## MCP test result (this session)

I tried to use Jarvis MCP in this chat. **It was not available.**

Available MCP servers here were only:
- Supabase, Vercel, Sanity (plugins)
- `cursor-app-control`, `cursor-ide-browser` (built-in)

There were **no** `jarvis`, `jarvis-fs`, or Obsidian vault tools. That is because `~/.cursor/mcp.json` was empty when this session started. Cursor does **not** read `~/.mcp.json` — your global Claude setup was correct, but Cursor needed its own file.

I **could** read Jarvis via the filesystem (`00_Dashboard.md`, `AGENTS.md`, session log, etc.). That is normal file access, not Obsidian MCP.

---

## Corrected analysis: what was actually wrong

| Earlier claim | Verdict |
|---------------|---------|
| Global `~/.mcp.json` strategy is wrong | **Wrong.** It works for Claude Code. The gap was only that Cursor uses a different path. |
| `~/.cursor/mcp.json` was empty | **Correct.** That was the real Cursor bug. |
| Jarvis missing `.cursor/mcp.json` | **Correct** for project-level servers (context7, playwright, etc.). |
| Jarvis `.mcp.json` missing Obsidian API key | **Minor.** Claude likely uses global `jarvis` HTTP (port 27123), not the stdio `obsidian` entry in the project file. Not why Claude fails. |
| Kiro malformed global config | **Real for Kiro only** — unrelated to Cursor. |
| WSL duplicate homes | **Only matters if you code in WSL** — Jarvis is on `D:\`, so not your main issue. |
| Plugin MCP “invisible” | **Not a problem** — expected. |
| Three Obsidian connection styles | **Theoretical clutter**, not a failure if global HTTP is what Claude uses. |

**Bottom line:** Your global MCP design is sound. The only Cursor mistake was not copying it into `~/.cursor/mcp.json` (and project `.cursor/mcp.json`).

---

## What I changed

### 1. `C:\Users\Anant Gupta\.cursor\mcp.json`
Mirrored your working Claude global config exactly:
- `jarvis` — HTTP Obsidian @ `127.0.0.1:27123`
- `the-plan` — HTTP @ `127.0.0.1:27124`
- `jarvis-fs` / `the-plan-fs` — filesystem MCP for both vault paths

### 2. `D:\Users\_Anant\10_Areas\Documents\Jarvis\.cursor\mcp.json`
Mirrored `Jarvis\.mcp.json` exactly (same as Claude project layer):
- `obsidian`, `context7`, `playwright`, `openaiDeveloperDocs`

Cursor now matches Claude’s two-layer setup:
- **Global** → `~/.mcp.json` (Claude) / `~/.cursor/mcp.json` (Cursor)
- **Jarvis project** → `Jarvis/.mcp.json` (Claude) / `Jarvis/.cursor/mcp.json` (Cursor)

---

## What you need to do (required for MCP to load)

MCP config is read when Cursor starts a session. **This chat will not gain Jarvis tools until you reload.**

1. **Reload MCP:** `Ctrl+Shift+J` → **Features → Model Context Protocol** → refresh, or restart Cursor.
2. **Open the Jarvis folder** as the workspace (`D:\Users\_Anant\10_Areas\Documents\Jarvis`).
3. **Obsidian running** with Local REST API enabled on port **27123** (and 27124 for The Plan if you use that vault).
4. **Start a new Agent chat** and check **Available Tools** for `jarvis`, `jarvis-fs`, etc.
5. If something fails: **Output panel** (`Ctrl+Shift+U`) → **MCP Logs**.

---

## Jarvis read-through (filesystem, not MCP)

From the vault files I could read:

- **Purpose:** AI-assisted Obsidian PKM (“second brain”), not a code repo.
- **Control panel:** `00_Dashboard.md` (updated 2026-05-26) links vault OS, Claude workflow, enrichment dashboards.
- **Agent contract:** `AGENTS.md` — read `AI_CONTEXT`, dashboard, session log before assuming state; don’t invent Cursor-only context.
- **Continuity:** `60_Claude/10_Session_Logs/log.md` — append-only session history since 2026-04-08.
- **Cursor rules already good:** `.cursor/rules/workspace-context.mdc` and `human-writing.mdc` point at shared `AGENTS.md` / `HUMAN_WRITING.md`.

After reload, a new chat should be able to query notes via the `jarvis` HTTP MCP instead of only raw files.

---

## After reload — quick verification

In a **new** chat with Jarvis open, ask:

> “Use the jarvis MCP to list notes or search the vault.”

If tools appear and return vault data, setup is correct. If not, paste the **MCP Logs** error and I can fix the next issue (usually Obsidian not running, wrong port, or auth token mismatch).

I did not change your Claude configs, Kiro configs, or `~/.mcp.json` — only added the Cursor equivalents Claude already had.

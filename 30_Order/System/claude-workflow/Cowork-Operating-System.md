---
type: evergreen
status: tree
created: 2026-06-05
updated: 2026-06-05
tags:
  - system
  - cowork
  - claude
notes:
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[CLAUDE.md]]"
  - "[[AGENTS]]"
  - "[[HUMAN_WRITING]]"
---

# Cowork Operating System — Project Instructions (Jarvis)

**Use:** Paste this entire note into Claude Desktop → Cowork → Project instructions for the **Jarvis** space.  
**Connected folder (required):** `D:\Users\_Anant\10_Areas\Documents\Jarvis` — native Windows path only. Never `\\wsl.localhost\...`.

---

## 0. Your job in one sentence

Execute the user's task on **this Windows machine** using **verified tools and paths**, with **minimal scope**, **vault-safe writes**, and **zero improvisation** when access fails.

---

## 1. What Cowork is for on this machine (and what it is not)

| Use Cowork for | Do NOT use Cowork for |
|----------------|------------------------|
| Jarvis vault read/write via **jarvis** MCP | Code repos under **WSL** (`/home/anant_gupta/...`) |
| The Plan vault via **the-plan** MCP | `pnpm` / `npm build` / git-heavy dev loops on WSL projects |
| Files on **D:** or **C:** (native NTFS paths) | Folders attached as `\\wsl$\` or `\\wsl.localhost\` |
| Documents, briefs, reviews, vault maintenance | Replacing **Claude Code CLI** for terminal-native work |

**If the task requires shell access to a WSL project:** stop, say so in one paragraph, and tell the user to run **Claude Code inside WSL** (`cd` to project → `claude`). Do not burn tokens retrying bash, Glob, or folder re-selection on UNC paths.

---

## 2. Pre-flight (every session, before acting)

Run this mental checklist. If any step fails, **stop and report** — do not guess.

1. **Connected folder** is a **Windows drive letter path** (e.g. `D:\Users\_Anant\10_Areas\Documents\Jarvis`). If you see `\\wsl.localhost\` or `\\wsl$\`, **abort** and ask the user to reconnect a native path or switch to Claude Code in WSL.
2. **Obsidian is running** on Windows (required for jarvis / the-plan HTTP MCP).
3. **MCP status:** jarvis, the-plan, jarvis-fs, the-plan-fs should connect. If jarvis/the-plan fail, check Obsidian Local REST API (ports **27123** / **27124**).
4. **Read spine** (via jarvis MCP, in order — do not skip):
   - `AGENTS.md`
   - `CLAUDE.md`
   - `HUMAN_WRITING.md`
   - `60_Claude/07_AI_Information/AI_CONTEXT.md`
   - `00_Dashboard.md`
   - Last **30 lines** of `60_Claude/07_AI_Information/Session Logs/log.md` (or latest session log path in AI_CONTEXT)
5. **State the task** in one sentence and list **files you will touch** before editing.

---

## 3. Filesystem map (Anant's machine)

### Native Windows (Cowork-safe)

| Path | Purpose |
|------|---------|
| `D:\Users\_Anant\10_Areas\Documents\Jarvis` | **Jarvis vault** — primary Cowork workspace |
| `D:\Users\_Anant\10_Areas\Documents\The Plan` | The Plan vault (the-plan MCP) |
| `D:\Users\_Anant\Downloads` | Downloads |
| `D:\Users\_Anant\10_Areas\Documents` | Documents (redirected) |
| `C:\Users\Anant Gupta\AppData\Roaming\Claude` | Claude Desktop data (config, VM bundle — **do not delete**) |
| `C:\Users\Anant Gupta\Claude` | Cowork user files (`Scheduled\`, outputs) |

### WSL (Cowork-unsafe — Claude Code only)

| Path | Purpose |
|------|---------|
| `/home/anant_gupta/projects/hub/portfolio` | Next.js portfolio (use **Claude Code in WSL**) |
| `/home/anant_gupta/projects/hub/*` | Other dev repos |
| `/home/anant_gupta/.mcp.json` | Claude **Code** MCP config (not Desktop) |

**Rule:** Never assume WSL paths are reachable from Cowork file tools or workspace bash.

---

## 4. MCP tools — use the right one

| Server | Use when | Do not use when |
|--------|----------|-----------------|
| **jarvis** | Read/write/search **Jarvis vault** notes via Obsidian | Arbitrary paths outside vault |
| **the-plan** | The Plan vault | Jarvis content |
| **jarvis-fs** | Raw file ops under `D:\...\Jarvis` if jarvis MCP lacks a tool | Bypassing vault routing rules |
| **the-plan-fs** | Raw file ops under The Plan | Same |
| **github** | GitHub API (issues, PRs, repo content) | Local git replace |
| **workspace bash** | Commands inside Cowork Linux VM for **mounted** Windows folder | WSL UNC paths; long build pipelines |

**Default for vault work:** prefer **jarvis** (Obsidian-aware) over jarvis-fs unless you need a tool jarvis does not expose.

**Never** invent MCP servers or shell commands not available in this session.

---

## 5. Vault write contract (non-negotiable)

From [[40_Resources/Obsidian/Jarvis Vault Architecture]] and `CLAUDE.md`:

1. **Never create** a new top-level file or folder at the vault root. Root allows only: `00_Dashboard.md`, `AGENTS.md`, `CLAUDE.md`, `HUMAN_WRITING.md`, numbered folders `10_`–`60_`, `.claude/`, `.obsidian/`, etc. — not new root-level project folders.
2. **Unsure where a note goes?** → `60_Claude/00_Inbox/`. Never invent a folder.
3. **Search before create** — extend existing notes by heading.
4. **Patch by heading** — preserve frontmatter and wikilinks.
5. **Read `HUMAN_WRITING.md`** before any prose meant for the vault.
6. **`50_Archive/`** — never read or write unless explicitly instructed.
7. **`60_Claude/`** is the AI workshop; promote stable knowledge to `40_Resources/` or `10_Areas/` when appropriate.
8. **Log meaningful sessions** — append a short entry to the session log when the task changed vault state or setup.

---

## 6. Session discipline

1. **Scope:** Do only what the user asked. No drive-by refactors, no "while I'm here" edits.
2. **Verify writes:** After creating or editing a note, read back the changed section via jarvis.
3. **No slop:** No generic AI filler, no duplicate notes, no empty scaffolding files.
4. **Secrets:** Never paste API keys, tokens, or `.env` contents into vault notes or chat logs. Config lives in `claude_desktop_config.json` only.
5. **Git:** Do not commit unless the user explicitly asks. Do not force-push.
6. **When blocked:** Report exactly — tool name, error text, path attempted, one recommended next step. Max **one** retry with a different *documented* approach, then stop.

---

## 7. Tool failure playbook

| Symptom | Cause | Action |
|---------|-------|--------|
| `UNC paths are not supported` | WSL or network UNC folder | Stop. User must use native Windows path or Claude Code in WSL. |
| Glob/Read empty on connected folder | Wrong or empty subfolder (e.g. `Portfolio (1)`) | Confirm connected path matches **repo/vault root**. |
| jarvis MCP red / timeout | Obsidian not running or wrong port | Ask user to start Obsidian; verify 27123. |
| `outside connected folders` | Path not under connected folder or MCP allowlist | Use jarvis MCP or jarvis-fs within `D:\...\Jarvis`. |
| workspace bash unavailable | VM bundle issue | User runs `Test-Path` on `rootfs.vhdx`; do not loop reinstall scripts. |

**Forbidden loops:** Do not retry the same failed bash command more than twice. Do not re-request folder access on UNC paths. Do not write workaround scripts to random outputs folders when the user asked for in-repo execution.

---

## 8. Context pack for task types

### Vault maintenance / notes / plans
- Spine (§2) + task-specific notes linked from `00_Dashboard.md`
- Write to correct layer per architecture table

### Summer OS / life plans (`10_Areas/Life/Plans/`)
- Read `00 - Summer Plans Index` and the specific plan file for the task
- Do not rewrite `Summer Grind` source; operationalize into plan files

### Reviews
- Use `.claude/skills/weekly-review.md` pattern if user invokes weekly review
- Output to `60_Claude/50_Reviews/`

### External project brief in vault
- Read `60_Claude/40_Project_Briefs/` entry first
- Cross-check `20_Progress/` for active status

---

## 9. Output quality

- Match voice in `HUMAN_WRITING.md` for anything human-facing in the vault.
- Use wikilinks `[[Note Name]]` for internal references.
- Use YAML frontmatter on new evergreen notes (`type`, `status`, `created`, `tags`, `notes`).
- Prefer tables and short sections over walls of text.
- End substantive tasks with: **Done** / **Blocked** / **Needs user**, plus files touched.

---

## 10. Quick reference — paths

```
Jarvis vault:     D:\Users\_Anant\10_Areas\Documents\Jarvis
The Plan vault:   D:\Users\_Anant\10_Areas\Documents\The Plan
Cowork outputs:   C:\Users\Anant Gupta\Claude
Desktop MCP cfg:  C:\Users\Anant Gupta\AppData\Roaming\Claude\claude_desktop_config.json
Claude Code (WSL): /home/anant_gupta — use terminal claude, not Cowork
```

---

## 11. First message template (use when starting cold)

When the user opens a Cowork session without a detailed prompt, reply:

> I've loaded the Jarvis Cowork OS rules. Connected folder is [path]. I'll read AGENTS → CLAUDE → HUMAN_WRITING → AI_CONTEXT → Dashboard → log tail before editing. What is the single outcome you want from this session?

Then execute §2 pre-flight before any writes.

---

*Canonical copy lives in the vault. Update this note when machine paths or MCP setup change.*

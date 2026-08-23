---
type: reference
status: active
created: 2026-08-22
updated: 2026-08-22
tags:
  - claude-kit
  - wsl
  - environment-map
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Prompts]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Windows Environment]]"
next: null
---
# WSL Environment — Reference Map
Rich, concrete, verified-by-direct-read context on what lives inside the WSL Ubuntu home directory, so instruction-writing for that side (global `CLAUDE.md`, agents, skills, commands, `settings.json`) doesn't happen blind. This is source material, not the instructions themselves — [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Prompts#Cursor — Grok 4.6 → Sonnet 5|the Cursor/Grok/Sonnet prompt pair]] hands this off for the real setup work. Companion: [[20_Progress/Projects/AI Use/Claude Kit/Claude Code/Windows Environment]]. **Verified 2026-08-22 by direct `cat`/`ls` of every file named below — not secondhand.** Re-verify before trusting if this note is more than a few weeks old; this environment changes daily.

## Identity
- Distro: Ubuntu 24.04.4 LTS (noble), systemd on, Windows interop on with PATH passthrough (`/etc/wsl.conf`).
- Home: `/home/anant_gupta` — from Windows/Cursor: `\\wsl$\Ubuntu\home\anant_gupta`.
- User `anant_gupta` maps to the Windows user "Anant Gupta" (`/mnt/c/Users/Anant Gupta`).

## AI coding tool configs at home root
| Dir | Tool | Notes |
|---|---|---|
| `.claude/` | Claude Code | global `CLAUDE.md`, `agents/` (3), `commands/` (7), `skills/` (28), `hooks/` (3 scripts), `settings.json`/`settings.local.json` |
| `.cursor/` | Cursor IDE | `agents/`, `hooks/`, `hooks.json`, `mcp.json` (mirrors `~/.mcp.json` — same live credentials, see below), `plans/`, `skills/`, `skills-cursor/`, `worktrees/` |
| `.codex/` | OpenAI Codex CLI | `config.toml`, sessions, memories, `rules/`, `skills/` |
| `.gemini/`, `.kiro/`, `.copilot/` | Gemini CLI, Kiro, Copilot CLI | present, not inspected in depth this pass |
| `.agents/` | cross-tool shared skill staging | currently just `skills/graphify/` |
| `.gbrain/`, `.promptfoo/` | other evaluated tools | see `second-brain-claudekit/tested-tools/` for verdicts |

## `~/.claude/CLAUDE.md` — currently 226 bytes, one rule
Verbatim: a graphify skill-trigger instruction ("any input to knowledge graph, trigger `/graphify`"). Nothing else. Whatever a rewritten global CLAUDE.md says, it needs to still carry this trigger (or an equivalent) since it's real and in active use.

## `~/.claude/agents/` — all 3 are Obsidian-vault-specific, not general-purpose
| Agent | Model | Tools |
|---|---|---|
| `obsidian-architect` | opus | `mcp__jarvis__{search_query,search_simple,vault_read,vault_list,vault_write,vault_patch,tag_list,vault_get_document_map}` |
| `obsidian-researcher` | sonnet | same read/search subset, no write/patch |
| `obsidian-session-archivist` | sonnet | `vault_list,vault_read,vault_write,vault_append,vault_patch,tag_list` |

All three are scoped entirely to Jarvis vault work via `mcp__jarvis__*` tools — none is project-code-specific, so "global, no regard to which project is open" genuinely holds for these three, unlike some of what's in `settings.json` (below).

## `~/.claude/commands/` — 7, all Obsidian/second-brain workflow
`obsidian-daily-review`, `obsidian-session-review`, `second-brain-capture`, `second-brain-compress`, `second-brain-graduate`, `second-brain-resume`, `second-brain-review`. Same story as agents: genuinely global by content, not leaking project specifics.

## `~/.claude/skills/` — 28 real folders
Two clusters: Cloudflare platform skills (`agents-sdk`, `cloudflare`, `cloudflare-email-service`, `cloudflare-one`, `cloudflare-one-migrations`, `durable-objects`, `sandbox-sdk`, `workers-best-practices`, `wrangler`) and Obsidian/vault skills (`graphify`, `obsidian-class-{biol1012,csci3923,csci4041,mgmt3001,ocaml,umn-hub}`, `obsidian-project-{arc,career,guitar,mentorship,portfolio,projects}`, `obsidian-remember`, `obsidian-review`, `obsidian-search`, `second-brain-obsidian-integration`), plus `turnstile-spin`, `web-perf`. The `obsidian-class-*` skills are explicitly single-course helpers (BIOL 1012, CSCI 3923/4041/2041-OCaml, MGMT 3001) — global scope is defensible here only because "which UMN course" isn't project-scoped the way a code repo is; still worth a second look for whether a finished/dropped course's skill should be archived.

## `~/.claude/settings.json` — real hooks, real plugins, and one confirmed global/project-scope leak
- `"model": "sonnet"` — global default is already Sonnet.
- `effortLevel: "high"`, `theme: "dark"`, `autoCompact: true`.
- Hooks wired for real: `PostToolUse` (Write/Edit/MultiEdit) → `after-edit-log.ps1`; `Stop` → both `wsl-session-export.ps1` and `session-wrapup.ps1`; `SessionEnd` → `wsl-session-export.ps1`. All three scripts confirmed present in `~/.claude/hooks/` (845B, 571B, 29810B respectively).
- `enabledPlugins`: `linter`, `smart-connections`, `claudian`, `otel-monitoring` (all `@anthropic-tools`), `vercel@claude-plugins-official`, `pyright-lsp@claude-plugins-official`, `ponytail@ponytail`.
- **Confirmed leak, verified 2026-08-22 — global config that is actually one-project-specific:** `autoMode.environment` and `autoMode.soft_deny` are entirely about `internship-research-loop`/`gupta-builds` — its repo visibility, its CI secret names (`FIRECRAWL_API_KEY`, `JARVIS_PUSH_TOKEN`), its GitHub Actions workflows, and a Jarvis-vault consent flow specific to that project's `promote-dossier` skill. None of this is true "with no regard to which project is open" — it's real evidence that at least one whole block has drifted from project-scoped into global. Likely not the only instance; anything else in `settings.json` should be checked against the same test.

## `~/.mcp.json` and `~/.cursor/mcp.json` — identical global MCP servers, hold live secrets
`jarvis` (HTTP `:27123`), `the-plan` (HTTP `:27124`), `jarvis-fs`/`the-plan-fs` (filesystem MCP scoped to the two vault paths on `D:`), `github` (PAT). **Both files hold live bearer tokens and a GitHub PAT in plaintext — never echo either file's contents into a note, a prompt, or a chat reply, not even partially.**

## Cross-OS mounts
- `/mnt/c/Users/Anant Gupta` = Windows user home (`C:\Users\Anant Gupta`).
- `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis` = this vault (`D:\Users\_Anant\10_Areas\Documents\Jarvis`) — every `mcp__jarvis__*` tool call operates here.
- `/mnt/d/Users/_Anant/10_Areas/Documents/The Plan` = second vault, same pattern via `the-plan`/`the-plan-fs`.

## Real project tree (`~/projects/`) — not vault-managed
- `ai/claude/second-brain-claudekit` — the tooling-qualification pipeline repo itself.
- `ai/claude/everything-claude-code` — real ECC 2.0 Rust control-plane scaffold, still un-evaluated.
- `ai/claude/claude-ai` — **unrelated pre-existing Next.js/Prisma project, explicitly off-limits to second-brain-claudekit work.**
- `ai/jan` — Jan (local-LLM desktop app), unrelated.
- `hackathon/{Resq,opspilot,safereach}` — hackathon-era repos, each with independent `.claude/`/`.cursor/`/`.kiro/`.
- `hub/{CausalOps,tradingview,portfolio,DNA_BJJ_APP,GymMangment_app_demo,Learning-Tracker-Tool,Assisto_website}` — main active real projects, each independently configured for multiple AI tools.
- `umn/boom` — UROP research project, tracked in Jarvis's `20_Progress/UROP/`, outside this pipeline.
- `work/{gupta-builds,internship-research-loop}` — the source of the confirmed `settings.json` leak above.

Eight of these (`second-brain-claudekit`, CausalOps, Jarvis, Portfolio, Trading View, Resq, OpsPilot, The Plan) are the live entries in `second-brain-claudekit/60_Claude/scripts/sync-manifest.json` — each project's real `.claude/{agents,commands,hooks}` and main instruction files get one-way-mirrored into that repo's `agents/<Name>/`, `commands/<Name>/`, `hooks/<Name>/`, `instructions/<Name>/`, and into a parallel Jarvis-side mirror, via Unison (`sync-all.sh`, ~every 15 min).

## What this means for writing WSL-side instructions
- A global `~/.claude/CLAUDE.md`/`settings.json` rule should hold only what's true with no regard to which project is open (`second-brain-claudekit/_docs/Design.md`'s own global-vs-project-scoped rule). Agents/commands/skills mostly pass this test already (they're Obsidian/vault-generic); `settings.json`'s `autoMode` block does not.
- Never quote `~/.mcp.json`'s or `~/.cursor/mcp.json`'s tokens in any instruction doc.
- `second-brain-claudekit`'s sync pipeline already treats `~/.claude` as the canonical `.claude_wsl` entry — a rewritten global config should stay something that entry can keep mirroring as real content, not a placeholder.

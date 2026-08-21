# Current Setup — MCP servers, plugins, and marketplaces actually connected

Written up 2026-08-09 from a direct `/config`-style capture of this session's Claude Code environment. This is what's actually wired in, not a wishlist — treat it the same way `_docs/PRD.md` treats `Tool Map.md`: a live snapshot, refresh it when the setup changes rather than letting it drift.

## MCP servers (18 total)

### Project-scoped (`.mcp.json`, this repo)

| Server | Tools | Status | What it's for |
|---|---|---|---|
| `github` | 26 | Connected | GitHub repo operations — issues, PRs, file/branch/commit access. |
| `jarvis` | 16 | Connected | Read/write/search access to the Jarvis Obsidian vault via its own Obsidian-bridge tools (`vault_read`, `vault_write`, `search_query`, etc.) — separate from, and complementary to, the direct filesystem access this repo's WSL session also has at `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis`. |
| `jarvis-fs` | 14 | Connected | Direct filesystem-level access to the Jarvis vault (`read_file`, `write_file`, `directory_tree`, etc.) — the lower-level counterpart to `jarvis`'s Obsidian-aware tools. |
| `the-plan` | 16 | Connected | Same Obsidian-bridge tool shape as `jarvis`, pointed at "The Plan" — Anant's personal-life vault (see `_docs/PRD.md`'s "who this is for"). |
| `the-plan-fs` | 14 | Connected | Filesystem-level counterpart to `the-plan`, matching the `jarvis`/`jarvis-fs` split. |

### User-scoped (`~/.claude.json`)

| Server | Tools | Status | What it's for |
|---|---|---|---|
| `graphify` | 7 | Connected | Knowledge-graph construction from content — the same tool tracked as a "to use" candidate in `20_Progress/Projects/AI Use/Claude Kit/Tool Map.md`, and the basis of the planned `60_Claude/40_Project_Briefs/Claude Kit/` integration (`_docs/Jarvis.md`). |
| `pencil` | 6 | Connected | `.pen` design-file editor (web/mobile app and website design). Not part of this repo's qualification-pipeline mission — a general-purpose tool available in the session, unrelated to Claude Kit tracking. |

### claude.ai connectors

| Connector | Tools | Status |
|---|---|---|
| Cloudflare Developer Platform | 23 | Connected |
| Context7 | 2 | Connected |
| Sanity | 33 | Connected |
| Supabase | 29 | Connected |
| Gmail | — | Needs authentication |
| Google Calendar | — | Needs authentication |
| Google Drive | — | Needs authentication |
| Miro | — | Needs authentication |
| QuickNode | — | Needs authentication |
| Vercel | — | Hidden — same URL as the `plugin:vercel:vercel` plugin server below; use the plugin instead |

One additional connector listed as available but not expanded in this session's capture ("Show unused connectors (1)") — not identified, not guessed at here.

### Built-in

| Server | Tools | Status |
|---|---|---|
| `plugin:vercel:vercel` | 33 | Connected |

## Plugins

| Plugin | Scope | Status |
|---|---|---|
| `pyright-lsp` | Project (`claude-plugins-official`) | Enabled, not used in 29 days |
| `ponytail` | User (`ponytail` marketplace) | Enabled |
| `vercel` | User (`claude-plugins-official`) | Enabled — provides the `vercel` MCP above |

## Marketplaces

| Marketplace | Source | Available / Installed | Last updated |
|---|---|---|---|
| `claude-plugins-official` | `anthropics/claude-plugins-official` | 284 available, 2 installed | 2026-08-08 |
| `ecc` | `https://github.com/affaan-m/ECC.git` | 1 available | 2026-07-29 |
| `ponytail` | `DietrichGebert/ponytail` | 1 available, 1 installed | 2026-07-18 |

The `ecc` marketplace is a separate connection point from `sandbox/ecc/` (the real clone of `affaan-m/everything-claude-code` this repo's pipeline is evaluating, per `20_Progress/Projects/AI Use/Claude Kit/Tool Map.md`) — worth checking both stay consistent as ECC's evaluation progresses, not assumed to already be in sync.

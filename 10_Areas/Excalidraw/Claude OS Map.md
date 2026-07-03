---
type: index
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - claude-os
  - ai-infrastructure
  - excalidraw
notes:
  - "[[Claude OS]]"
  - "[[20_Progress/AI/Claude OS Dashboard|Claude OS Dashboard]]"
next: "Draw the canvas from this blueprint in Excalidraw when there's a reason to navigate visually — the blueprint is the source of truth, the drawing is a render"
---
# Claude OS Map — canvas blueprint
Text blueprint for the Claude OS Excalidraw canvas. Hand-authoring `.excalidraw` JSON is fragile, so this note specifies every node, connection, and branch; draw it manually (or with the Excalidraw plugin's text-to-diagram) when needed. Until then this note *is* the map.
## Layout
Hub-and-spoke. **Jarvis** is the center node. Four platform branches radiate out (Claude Code top-right, Cursor bottom-right, Kiro bottom-left, Codex top-left). Each platform node fans out to project sub-nodes; the Claude Code branch additionally fans to component sub-branches (skills / agents / hooks / MCP). Cross-links (dashed arrows) mark where two tools share one context layer.
## Nodes and edges
### Center
- **JARVIS (hub)** → links [[Jarvis OS — North Star]], [[Claude OS]], [[00_Dashboard]]
  - solid edge to each of the four platform nodes
  - side chip: "shared canon: AGENTS.md · HUMAN_WRITING.md · AI_CONTEXT.md"
### Branch 1 — Claude Code (primary; largest branch)
- **Claude Code** → [[10_Areas/AI/Claude Code]]
  - **Skills (14)** — sub-node per shape: `directory ×3` (startday, closeday, ingesting-clipping) highlighted green; `flat ×11` grey. Edge label: ".claude/commands/ → .claude/skills/"
  - **Agents (5)** — research-distiller, anti-slop-editor, vault-curator, learning-agent, career-operator. All green (frontmatter complete).
  - **Hooks (2)** — session-continuity (SessionStart+End), write-guard (PreToolUse). Edge label: "code lives in 30_Order/System/claude-workflow/hooks/"
  - **MCP (5)** — obsidian, filesystem, git, fetch, **jarvis-memory** (green ✅ verified; dashed edge to future node "semantic search — chunks/embeddings TODO")
  - **Projects** — Jarvis (this), CausalOps (3 agents/4 commands/3 hooks), Resq+OpsPilot (canon layer), Portfolio (empty dump — red), TradingView (empty dump — red)
  - **WSL Home** — graphify, second-brain-claudekit (7 commands, 3 obsidian agents), everything-claude-code marketplace (~240 skills, amber "triage done, adoption pending")
### Branch 2 — Cursor
- **Cursor** → [[10_Areas/AI/Cursor]]
  - **Jarvis rules (5)** — workspace-context, human-writing, vault-behavior, note-creation, plugin-rules. Amber: "duplicate vault canon — shrink to pointers"
  - **SafeReach** — 7 lifecycle hooks + 8 skills. Green star: "reference hook architecture"
  - **CausalOps** — hivemind-core.mdc evidence guardrail + 2 skills
  - **Portfolio** — 3 agents + 3 skills + rules
  - **Empty** — DNA App, Trading View (red)
### Branch 3 — Kiro
- **Kiro** → [[10_Areas/AI/Kiro]]
  - **Resq** — agent JSON mounting `.claude/` canon; canon-gate/demo-safety/secret-hygiene/finance-guard hooks. Green star: "cross-tool canon pattern"
  - **Assisto** — 5 steering + 3 hooks + spend spec
  - **Portfolio / SafeReach / TradingView / OpsPilot** — smaller chips
  - **Jarvis .kiro** — amber: "stub; steering duplicates canon, no agent — build out or freeze"
### Branch 4 — Codex
- **Codex** → [[10_Areas/AI/Codex]]
  - **Assisto** — .agents/ + credential-free config.toml (green star: "repo-local config done right")
  - **Portfolio** — 9 source-command-* migrated skills
  - **OpsPilot / Resq** — supabase skills chips
  - Amber banner: "no usage signal — verify before investing"
### Cross-links (dashed)
- Resq: Kiro agent ⇄ Claude Code `.claude/` canon ("one context layer, two tools")
- SafeReach: Cursor hooks ⇄ Kiro steering via `kiro-cursor-contract.md`
- Portfolio: Codex source-command-* ⇄ original Claude Code commands ("same gates, either agent")
- Jarvis: Cursor rules + Kiro steering ⇄ AGENTS.md/HUMAN_WRITING ("should be pointers, currently copies")
## Color code
- Green = verified working. Amber = exists but needs a decision. Red = empty/dead dump. Star = pattern worth copying to other projects.

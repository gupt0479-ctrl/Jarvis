---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - ai-agents
  - automation
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# AI Automation and Local Interfaces

Copilot, QuickAdd AI, and Local REST API can make Obsidian programmable. They also create the highest safety risk in this plugin set.

Use them only when the user explicitly asks for automation through Obsidian or when a workflow has already been approved.

## Source Of Truth

The source of truth is the vault, not AI memory.

Read in this order:

1. [[AI_CONTEXT]]
2. [[HUMAN_WRITING]]
3. [[40_Resources/Obsidian/Vault Operating System]]
4. [[00_Dashboard]]
5. [[log]]
6. relevant source, project, course, or concept notes

Copilot memory, chat history, embeddings, provider context, and recent files are secondary. They can suggest where to look; they do not overrule the notes.

## Copilot

Observed safe facts:

- Installed and lazy-loaded with long delay.
- Conversations are saved under `50_Archive/copilot/copilot-conversations`.
- Custom prompts are under `50_Archive/copilot/copilot-custom-prompts`.
- Autosave chat is enabled.
- Inline citations are enabled.
- Saved memory is enabled.
- Autonomous agent mode is enabled.

Docs describe Copilot as supporting vault QA, citations, memory, custom prompts, and agent-like tool use. In Jarvis, this is useful for human-in-Obsidian questioning, but it should not become an unlogged parallel agent.

Rules:

- Treat `50_Archive/copilot` as read-only historical context unless the user asks.
- Do not copy provider credentials, auth material, memory internals, or generated indexes into notes.
- Prefer vault notes and dashboards over Copilot memory when facts conflict.
- Treat autonomous tools as high-risk until the user approves a specific workflow.

## Local REST API

Observed safe facts:

- Secure port: `27124`.
- Insecure port: `27123`.
- Insecure server: enabled.
- API credential material exists and must not be exposed.

The plugin documentation describes local HTTP endpoints for vault file operations, search, commands, and note/block/heading style updates. In Jarvis, this is a possible bridge for external automation, but direct filesystem edits are easier to audit in Codex.

Rules:

- Do not call Local REST API unless the user explicitly asks.
- Do not expose credential values.
- Prefer filesystem edits for documentation work.
- Treat insecure port `27123` as a risk surface and `needs verification`.
- If an automation later uses the API, constrain it to exact paths and operations.

Needs verification:

- Whether insecure server on `27123` should remain enabled.
- Which local tools are expected to use the API.
- Whether command endpoints should be allowed for any AI workflow.

## QuickAdd AI

QuickAdd can run capture choices, macros, and scripts. The current settings show no choices, while AI provider configuration exists.

Safe first step after approval:

1. Add non-AI capture choices.
2. Test destinations and templates.
3. Only then consider AI-assisted transforms.

Agents should not configure AI providers, add credentials, or write macros during documentation work.

## What Agents May Use

Agents may:

- read safe documentation and plugin settings
- document observed non-secret behavior
- write Markdown docs in approved folders
- suggest QuickAdd/REST/Copilot workflows as recommendations
- log meaningful vault changes

Agents may not:

- call Local REST API without explicit approval
- expose credential material
- change Copilot memory or autonomous settings
- edit plugin `data.json`
- enable Templater system commands
- write raw clippings or archive material unless explicitly asked
- run Obsidian commands through an API as a shortcut

## Safe Automation Pattern

Before automating:

1. Define the destination folders.
2. Define allowed operations: read, create, append, patch heading, search, or command.
3. Exclude `.obsidian`, secrets, clippings, archive folders, and Git operations unless explicitly included.
4. Add dry-run output for broad changes.
5. Log meaningful edits in `60_Claude/10_Session_Logs/log.md`.

Automation should make the vault easier to audit, not harder.

## Risk Surfaces

| Surface | Risk | Jarvis rule |
|---|---|---|
| Copilot autonomous tools | Parallel writes and hidden context drift. | Use only after workflow approval. |
| Copilot memory | Stale or unreviewed facts. | Vault notes beat memory. |
| Local REST API secure port `27124` | Programmatic writes. | Do not call unless asked. |
| Local REST API insecure port `27123` | Local unauthenticated or weaker transport risk depending setup; needs verification. | Review whether it should remain enabled. |
| QuickAdd AI | Capture macros can mix raw and processed material. | Configure capture first, AI later. |
| DataviewJS/HTML | Executable dashboard behavior. | Prefer plain Dataview. |

## Integration Map
- **Copilot ↔ vault (one-way trust):** Copilot reads the vault and stores memory under `50_Archive/copilot/`; the vault never trusts Copilot memory back. When facts conflict, notes win. Copilot's autonomous mode could write notes in parallel — that is the drift risk, so treat it as off until a workflow is approved.
- **Local REST API ↔ MCP/filesystem:** the API exposes the same vault operations an agent already has via filesystem edits. For documentation and note work, prefer filesystem edits — they are easier to audit than HTTP calls. The API is a bridge for *external* tools, not a shortcut for an in-editor agent.
- **Secrets ↔ `.gitignore`:** `copilot`, `quickadd`, and `local-rest-api` `data.json` files are gitignored precisely because they can hold credentials. This is why these docs describe behavior, never values. See [[Git Recovery and Vault Safety]].
## Gold-Standard Example
The correct pattern is restraint, so the example is a boundary, not a feature: `50_Archive/copilot/copilot-conversations` is read-only historical context — an agent may read it for continuity but must not treat it as a write target or as authority over current notes. There is no approved automation workflow in the vault yet, which is itself the honest current state: the safe default is "filesystem edits, logged."
## Verified Open State
- Should the Local REST API insecure server on port `27123` remain enabled, and which local tool needs it? — *security decision; insecure server is currently on*
- Should Copilot's autonomous agent mode be allowed to make vault edits, or stay human-facing Q&A? — *unresolved; high-risk until scoped*
- Which, if any, AI workflow is approved to call command endpoints? — *none currently approved*
## Sources

- [Copilot docs](https://www.obsidiancopilot.com/en/docs)
- [Copilot Vault QA](https://www.obsidiancopilot.com/en/docs/vault-qa)
- [Local REST API README](https://github.com/coddingtonbear/obsidian-local-rest-api)
- [Local REST API docs](https://coddingtonbear.github.io/obsidian-local-rest-api/)
- [QuickAdd docs](https://quickadd.obsidian.guide/docs/)
- [QuickAdd Capture choice](https://quickadd.obsidian.guide/docs/Choices/CaptureChoice)
- [[AI_CONTEXT]]
- [[Agent Operating Guide]]

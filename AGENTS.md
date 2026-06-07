---
type: ai
status: sprout
created: 2026-03-19
updated: 2026-06-07
tags:
  - "#ai"
  - "#evergreen"
  - "#ai-infrastructure"
related:
  - "[[CLAUDE]]"
  - "[[HUMAN_WRITING]]"
---
# Jarvis Agent Guide

This vault is an AI-assisted second brain built in Obsidian. Treat it as a knowledge system first and a file tree second.

## Priority Files

- Read [[60_Claude/07_AI_Information/Vault Map]] first — the five-minute orientation for any agent.
- Read [[40_Resources/Obsidian/Jarvis Vault Architecture]] for where every note goes (the placement source of truth).
- Read `30_Order/` before writing any note — its `Workflows/` and `Templates/` are the structural half of [[HUMAN_WRITING]].
- Read [[AI_CONTEXT]] for the shared cross-tool context manifest.
- Read [[00_Dashboard]] for the current control panel.
- Read [[CLAUDE]] for the existing Claude-layer workflow.
- Read [[40_Resources/Obsidian/Vault Operating System]] for the property schema before creating or restructuring notes.
- Read [[HUMAN_WRITING]] before drafting or rewriting prose.

## Folder Roles

Jarvis is six layers. Each folder answers one question; every note belongs to exactly one.

- `10_Areas/` — **Identity.** Canonical truth per domain (Career, Trading, Life, UMN). Lean, link-dense hubs that point out to active work and reference. Patch by heading; never add top-level files without explicit instruction. Holds `Excalidraw/` (visual layer).
- `20_Progress/` — **Execution.** Everything actively in motion, each with a `next:`. AI writes project notes here, drawn from briefs and distilled notes.
- `30_Order/` — **Rules and machinery.** Templates, the per-folder writing `Workflows/`, and CLI tooling. **Read this before writing any note.** Read-only unless the task is building a template, workflow, or tool.
- `40_Resources/` — **Reference hub.** Curated guides, concepts, links — the lookup shelf the work depends on. Add single backlinked entries; never bulk-dump AI output here.
- `50_Archive/` — **Dead.** Never read, never write.
- `60_Claude/` — **AI workshop.** Where any AI captures, drafts, distills, and coordinates. Knowledge is promoted out to the layers above; only machinery stays.

`60_Claude/` subfolders: `00_Inbox/` (default landing zone), `05_Clippings/` (raw, read-only after capture), `07_AI_Information/` (agent map + memory; holds `AI_CONTEXT.md` and `Session Logs/log.md`), `10_Source_Summaries/`, `20_Distilled_Notes/`, `35_Outputs/`, `40_Project_Briefs/`, `44_Indexes/`, `50_Reviews/`.

Full per-folder definitions: [[40_Resources/Obsidian/Jarvis Vault Architecture]].

## Write Contract

Every agent follows this, regardless of which tool is driving. Full version: [[40_Resources/Obsidian/Jarvis Vault Architecture]].

### Golden rules

1. **Never create a new top-level file or folder at the vault root.** Root holds only `00_Dashboard.md`, `AGENTS.md`, `CLAUDE.md`, `HUMAN_WRITING.md`, and the numbered folders `10_Areas`–`60_Claude`. This is the single most damaging mistake an agent can make.
2. **When unsure where a note goes, write it to `60_Claude/00_Inbox/`.** Unsure is the trigger to use the Inbox, never to invent a location.
3. **Read `30_Order/` before writing** — its `Templates/` and `Workflows/` are the structural half of [[HUMAN_WRITING]].
4. **Search before creating.** Extend an existing canonical note instead of duplicating.
5. **Preserve frontmatter and wikilinks. Patch by heading.**

### Where does this note go?

| If the note is… | Write it to… | Standards doc to read first |
| --- | --- | --- |
| Raw clip, paste, web capture, video, imported source | `60_Claude/05_Clippings/` |  |
| Quick AI output you're unsure how to file | `60_Claude/00_Inbox/` |  |
| Summary of one source | `60_Claude/10_Source_Summaries/` | [[Source Summary Standard]] |
| Reusable distilled knowledge (a concept, not a source) | `60_Claude/20_Distilled_Notes/` → promote to `40_Resources/` or `10_Areas/` once stable | [[Evergreen Standard]] |
| Stable reference material (guide, cheat sheet, plugin doc, link) | `40_Resources/` + backlink to its `10_Areas/` domain |  |
| Active project, internship, research, mentorship work | `20_Progress/` under the matching project | [[Project Standard]] |
| Canonical fact about a life domain | `10_Areas/` — patch by heading; no new top-level files without instruction |  |
| Synthesized project brief | `60_Claude/40_Project_Briefs/` |  |
| Reusable output artifact (story, bullet, prompt) | `60_Claude/35_Outputs/` with `source_concepts:` provenance |  |
| Daily / weekly / monthly review | `60_Claude/50_Reviews/` |  |
| Dashboard or index | `60_Claude/44_Indexes/` |  |
| Session log entry | append to `60_Claude/07_AI_Information/Session Logs/log.md` |  |
| New template, writing workflow, or CLI tool | `30_Order/` (only when explicitly building one) |  |
| Visualization for a concept / project / source | `10_Areas/Excalidraw/` |  |
| Information about the whole vault for any AI tool | `60_Claude/07_AI_Information/` |  |

### Never write to

- The vault root — no new files or folders directly inside `D:\Users\_Anant\10_Areas\Documents\Jarvis\`.
- `50_Archive/` — never read, never write.
- `60_Claude/05_Clippings/` after capture — raw sources are read-only.
- `40_Resources/` in bulk — curated hub; add one backlinked entry at a time, never a batch of AI distillations.
- `.obsidian/`, `.claude/`, `.cursor/`, `.kiro/`, `.codex`, `.git/` — settings and tooling only, never notes.

## Working Rules

- Search before creating a note. Prefer extending an existing canonical note over making duplicates.
- Preserve frontmatter and use the vault schema fields consistently.
- Prefer Obsidian wikilinks for internal references.
- Update `updated:` when a note changes meaningfully.
- Use `next:` on project, plan, and active progress notes when a concrete next step exists.
- For continuity, read `AI_CONTEXT.md`, `00_Dashboard.md`, and `60_Claude/07_AI_Information/Session Logs/log.md` before making assumptions about current state.
- Keep raw capture separate from distillation:
  - raw or imported material -> `60_Claude/05_Clippings`
  - source-grounded summary -> `60_Claude/10_Source_Summaries`
  - durable concept synthesis -> `60_Claude/20_Distilled_Notes`
- Do not modify `60_Claude/05_Clippings` unless the user explicitly asks.
- Treat `50_Archive/` as historical reference unless the task is archival cleanup.
- Do not write AI slop. Follow `HUMAN_WRITING.md`: cut filler, prefer mechanism and contrast, use real examples from this vault, and leave notes denser and more human than before.
- After meaningful vault changes, append a concise continuity entry to `60_Claude/07_AI_Information/Session Logs/log.md`.

## Retrieval Rules

- Prefer structured fields over ad hoc prose when the information should be queryable.
- Prefer backlinks and MOC/index notes over duplicate summaries.
- Use dashboards and indexes under `60_Claude/44_Indexes/` to find gaps before inventing new structure.

## Safety

- This vault contains local plugin configuration. Do not surface or copy secrets from plugin data files.
- Prefer env vars and ignored local config for credentials, never vault notes.

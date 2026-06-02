---
type: evergreen
status: tree
created: 2026-05-31
updated: 2026-05-31
tags:
  - system
  - ai-agents
  - vault-map
notes:
  - "[[AI_CONTEXT]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[Agent Operating Guide]]"
  - "[[HUMAN_WRITING]]"
---
# Vault Map — Read Me First

If you are an AI tool working in Jarvis, start here. This is the five-minute orientation: what this vault is, where things live, how to write into it, and what never to touch. It points at the deeper docs rather than repeating them.

Jarvis is a personal knowledge operating system in Obsidian. Anant uses it to learn, build, and run his life. It is a knowledge system first and a file tree second: live dashboards, metadata, backlinks, source layers, and AI-generated synthesis. Work with that system, not around it.

## Read order on a cold start

1. **This file** — orientation.
2. [[Vault Rules — Complete AI Ruleset]] — the governing specification for all AI behavior. Read before writing a single character.
3. [[40_Resources/Obsidian/Jarvis Vault Architecture]] — where every note goes (placement source of truth).
4. `30_Order/Workflows/` — how to write each note type (read [[00_Workflows Index]]).
5. [[HUMAN_WRITING]] — how prose must sound; [[Jarvis Writing and Formatting]] for Obsidian formatting.
6. [[AI_CONTEXT]] — the manifest of live context sources.
7. [[00_Dashboard]] and `60_Claude/07_AI_Information/Session Logs/log.md` — what is happening right now.

For the full runbook (session checklist, plugin choices, stop conditions), read [[Agent Operating Guide]].

## The six layers

Every folder answers one question. Every note belongs to exactly one layer.

| Folder | Layer | Question |
|---|---|---|
| `10_Areas/` | Identity | Who am I, what are my domains? (canonical hubs; holds `Excalidraw/`) |
| `20_Progress/` | Execution | What am I actively doing? (each note has a `next:`) |
| `30_Order/` | Rules | How are notes written and structured? (templates + workflows + CLI) |
| `40_Resources/` | Reference | What do I look up to do the work? (curated hub) |
| `60_Claude/` | AI workshop | Where does AI capture, draft, distill, coordinate? |
| `50_Archive/` | Dead | What is done? (never read, never write) |

Inside `60_Claude/`: `00_Inbox/` (default landing zone), `05_Clippings/` (raw), `07_AI_Information/` (this layer — agent map + memory), `10_Source_Summaries/`, `20_Distilled_Notes/`, `35_Outputs/`, `40_Project_Briefs/`, `44_Indexes/`, `50_Reviews/`.

The core motion: **knowledge is born in `60_Claude`, matures, and is promoted out to Identity / Execution / Reference. The workshop is not a warehouse.**

## How to write a note

1. Decide the layer, then check the routing table in [[40_Resources/Obsidian/Jarvis Vault Architecture]] for the exact folder.
2. Open the matching workflow in `30_Order/Workflows/` and follow its steps.
3. Use the matching template in `30_Order/Templates/` and the frontmatter schema in [[40_Resources/Obsidian/Vault Operating System]].
4. Write in the voice of [[HUMAN_WRITING]]; format per [[Jarvis Writing and Formatting]].
5. Wikilink sources, neighbors, and the project or domain it serves.
6. Append one line to `60_Claude/07_AI_Information/Session Logs/log.md`.

`30_Order` is mandatory pre-write reading: it holds the templates and the per-folder procedures. `HUMAN_WRITING` is the voice; `30_Order` is the structure.

## Conventions in one place

- **Wikilinks, not plain mentions.** Link when the target note helps future retrieval. Use aliases (`[[Long Note|short]]`) when prose reads better.
- **Frontmatter is the query surface.** Always set `type`, `status`, `created`, `tags`. Add `track`, `source_status`, `enrichment_status`, `next` where the note type calls for it. Do not hide queryable facts only in prose.
- **Maturity:** `seed` → `sprout` → `tree`. Be conservative editing `tree` notes; propose big restructures first.
- **Honesty:** mark claims source-grounded, inferred, or uncertain. Never fake a finished note.

## What this folder (07_AI_Information) is

The AI operating and memory layer — how agents read this vault and what has happened before. The **map** (this file, [[Agent Operating Guide]], [[AI_CONTEXT]], [[Jarvis Writing and Formatting]], [[60_Claude/07_AI_Information/Plugins]]) and the **memory** (`Session Logs/log.md`, `AI Conversations/`). It points at `30_Order` for the writing rules; it does not duplicate them. Rules live in `30_Order`; orientation and history live here.

## Never do this

- Create a new file or folder at the vault root.
- Invent a folder when unsure — write to `60_Claude/00_Inbox/` instead.
- Read or write `50_Archive/`.
- Rewrite a raw clipping in `60_Claude/05_Clippings/`.
- Bulk-dump AI output into `40_Resources/` (curated; one backlinked entry at a time).
- Touch `.obsidian/`, `.claude/`, `.cursor/`, `.kiro/`, `.codex`, `.git/`, or copy any plugin secret into a note.

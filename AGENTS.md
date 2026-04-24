# Jarvis Agent Guide

This vault is an AI-assisted second brain built in Obsidian. Treat it as a knowledge system first and a file tree second.

## Priority Files

- Read [[AI_CONTEXT]] for the shared cross-tool context manifest.
- Read [[00_Dashboard]] for the current control panel.
- Read [[CLAUDE]] for the existing Claude-layer workflow.
- Read [[40_Resources/Obsidian/Vault Operating System]] before creating or restructuring notes.
- Read [[HUMAN_WRITING]] before drafting or rewriting prose.

## Folder Roles

- `10_UMN/`: active coursework and school planning.
- `20_Progress/`: active projects, career work, mentorship, execution notes.
- `30_Order/`: templates and structural patterns.
- `40_Resources/`: stable reference knowledge and system docs.
- `50_Archive/`: historical material; prefer read-only behavior.
- `60_Claude/00_Inbox/`: staging area for AI outputs that still need review.
- `60_Claude/05_Clippings/`: raw source captures; do not rewrite in place.
- `60_Claude/10_Session_Logs/`: session records.
- `60_Claude/20_Distilled_Notes/`: durable AI-generated knowledge.
- `60_Claude/30_Source_Summaries/`: source-grounded summaries.
- `60_Claude/40_Project_Briefs/`: synthesized project briefs.
- `60_Claude/50_Reviews/`: daily, weekly, monthly reviews.
- `60_Claude/60_Indexes/`: dashboards and indexes.

## Working Rules

- Search before creating a note. Prefer extending an existing canonical note over making duplicates.
- Preserve frontmatter and use the vault schema fields consistently.
- Prefer Obsidian wikilinks for internal references.
- Update `updated:` when a note changes meaningfully.
- Use `next:` on project, plan, and active progress notes when a concrete next step exists.
- For continuity, read `AI_CONTEXT.md`, `00_Dashboard.md`, and `60_Claude/10_Session_Logs/log.md` before making assumptions about current state.
- Keep raw capture separate from distillation:
  - raw or imported material -> `05_Clippings`
  - source-grounded summary -> `30_Source_Summaries`
  - durable concept synthesis -> `20_Distilled_Notes`
- Do not modify `05_Clippings` unless the user explicitly asks.
- Treat `50_Archive/` as historical reference unless the task is archival cleanup.
- Do not write AI slop. Follow `HUMAN_WRITING.md`: cut filler, prefer mechanism and contrast, use real examples from this vault, and leave notes denser and more human than before.
- After meaningful vault changes, append a concise continuity entry to `60_Claude/10_Session_Logs/log.md`.

## Retrieval Rules

- Prefer structured fields over ad hoc prose when the information should be queryable.
- Prefer backlinks and MOC/index notes over duplicate summaries.
- Use dashboards and indexes under `60_Claude/60_Indexes/` to find gaps before inventing new structure.

## Safety

- This vault contains local plugin configuration. Do not surface or copy secrets from plugin data files.
- Prefer env vars and ignored local config for credentials, never vault notes.

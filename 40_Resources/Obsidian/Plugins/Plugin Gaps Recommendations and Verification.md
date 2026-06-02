---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - plugins
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# Plugin Gaps Recommendations and Verification

This is the action register for plugin gaps, risks, optional additions, and unresolved settings.

Do not scatter recommendations across the plugin docs. Link here and keep one canonical list.

## High Impact / Low Risk

### QuickAdd capture menu

Current state: installed, lazy-loaded, hotkeyed with `Alt+Q`, but `choices` is empty.

Recommended first choices:

- Inbox capture -> `60_Claude/00_Inbox`
- Source clipping -> `60_Claude/05_Clippings`
- Project note -> `20_Progress`
- Concept note -> `40_Resources` or `60_Claude/20_Distilled_Notes`
- Daily review -> `60_Claude/50_Reviews/Daily`
- Flashcard candidate -> current note or inbox

Start without AI actions. Capture correctness matters more than clever macros.

### Tasks dashboard conventions

Current state: Tasks is configured, but `00_Dashboard` still uses a Dataview `TASK` block for open tasks.

Recommendation: keep Dataview where it is metadata-driven, but add canonical Tasks query examples for due soon, in progress, and high priority.

### Spaced Repetition review cadence

Current state: `#cards` exists as a review surface, and Spaced Repetition is configured, but cadence and card quality rules need adoption.

Recommendation: add cards only after distillation, then connect `#cards`, `last_drilled`, `next_drill`, and review notes.

### Excalidraw visual templates

Current state: Excalidraw has folder, template, autosave, scripts folder, and wikilink embeds configured.

Recommendation: create one or two templates after approval:

- system architecture map
- course concept/PDF annotation map

## High Impact / Needs Decision

### Local REST API security

Current state: secure port `27124`, insecure port `27123`, insecure server enabled.

Decision needed: whether the insecure server should remain enabled and which local tools need it.

### Omnisearch and Text Extractor

Current state: PDF, Office, image, and AI image indexing are disabled.

Decision needed: whether source PDFs, screenshots, and Office files should become searchable. If yes, evaluate Text Extractor and performance/privacy tradeoffs.

### Copilot autonomous tools

Current state: Copilot autonomous agent mode and saved memory are enabled.

Decision needed: whether Copilot can make vault edits, or whether it should stay as human-facing Q&A with citations.

### Obsidian Git auto-push

Current state: auto-push interval is `5`, auto-pull interval is `10`, pull-before-push is enabled.

Decision needed: whether this cadence is still desirable while multiple AI tools edit the vault.

## Optional

| Option | Why consider it | Do not add unless |
|---|---|---|
| Text Extractor | Helps Omnisearch index PDFs/images. | Attachments become central to retrieval. |
| Calendar | Better visual Periodic Notes navigation. | Daily/weekly review navigation becomes painful. |
| Recent Edits | Better edit-trail review than Recent Files. | Human/agent edits need faster audit. |
| Excalibrain | Visual graph-style concept exploration. | Existing Excalibrain references are intentional. |
| Commander | Command/ribbon customization. | Plugin commands become hard to access. |

## Risk Register

| Risk | Current evidence | Mitigation |
|---|---|---|
| DataviewJS and HTML enabled | Dataview settings allow both. | Prefer plain Dataview; document any JS near the block. |
| Local REST API insecure server | `enableInsecureServer` is true. | Review need; do not call REST endpoints without approval. |
| Copilot autonomous tools | Copilot autonomous agent mode is enabled. | Vault notes beat Copilot memory; no unapproved parallel writes. |
| Obsidian Git auto-push | Auto-push interval is `5`. | Check status before broad edits; never stage unrelated changes. |
| Dirty worktree | Vault often has unrelated changes. | Preserve unrelated changes and log meaningful edits. |
| QuickAdd AI providers | Provider config exists. | Configure non-AI capture first; do not expose credentials. |
| Excalidraw AI | AI enabled. | Do not expose credentials; keep text source of truth. |
| Theme/snippet coupling | AnuPpuccin, Style Settings, and snippets are active. | Keep Markdown semantic. |

## Needs Verification

- Effective plugin enabled state after Lazy Plugin Loader completes startup.
- Why UI-visible community plugins exceed direct entries in `.obsidian/community-plugins.json`.
- Lazy Plugin Loader references `excalibrain`, but no matching plugin folder was found.
- `workspaces-plus` exists but has no readable manifest.
- Whether `60_Claude/7_AI_Information` should get a Templater folder template.
- Whether QuickAdd should be configured with capture choices.
- Whether Omnisearch should enable PDF/image/Office indexing, likely with Text Extractor.
- Whether Excalidraw auto-export should be enabled.
- Whether Local REST API insecure server should remain enabled.
- Preferred Tasks date conventions for coursework vs projects.
- Preferred Tasks priority scale for coursework vs projects.
- Preferred Kanban lane names for future project boards.
- Whether Calendar is installed or only referenced by old hotkeys.
- Whether Excalibrain is intentionally absent or partially removed.
- Whether Publish is actively used and what should be publishable.
- Whether Bases should complement Dataview or remain experimental.
- Whether Workspaces Plus was intentionally removed.

## Verification Checklist

Before changing plugin settings:

- Read the relevant reference doc in this folder.
- Check the current plugin setting in Obsidian UI, not just `data.json`.
- Decide whether the change affects secrets, automation, Git, or broad appearance.
- Back up or record the old setting if the user asks for a change.
- Change only the setting the user approved.
- Log the change in `60_Claude/10_Session_Logs/log.md`.

## Recommendation Rule

A plugin recommendation is valid only if it improves one of these:

- capture speed
- retrieval reliability
- review quality
- linking clarity
- task visibility
- visual understanding
- automation safety
- backup/recovery confidence

Otherwise, skip it.

## Sources

- [Obsidian Help - Core plugins](https://help.obsidian.md/plugins)
- [QuickAdd docs](https://quickadd.obsidian.guide/docs/)
- [Tasks User Guide](https://publish.obsidian.md/tasks/)
- [Spaced Repetition README](https://github.com/st3v3nmw/obsidian-spaced-repetition)
- [Omnisearch docs](https://publish.obsidian.md/omnisearch/Index)
- [Excalidraw plugin README](https://github.com/zsviczian/obsidian-excalidraw-plugin)
- [Local REST API README](https://github.com/coddingtonbear/obsidian-local-rest-api)
- [Copilot docs](https://www.obsidiancopilot.com/en/docs)
- [Obsidian Git docs](https://publish.obsidian.md/git-doc/Features)

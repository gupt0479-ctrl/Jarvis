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
  - "[[60_Claude/7_AI_Information/Plugins]]"
---
# Plugin Reference Index

This is the stable reference layer for Obsidian plugins in Jarvis.

Use [[60_Claude/7_AI_Information/Plugins]] when an agent needs quick operating rules. Use this folder when the human or an agent needs plugin behavior, settings, source links, syntax examples, safety boundaries, and verification notes.

## Start Here

For humans:

1. Use [[Plugin Inventory and Configuration Map]] to see what is installed, enabled directly, and lazy-loaded.
2. Use the workflow map below to jump to the plugin group behind the thing you are trying to do.
3. Use [[Plugin Gaps Recommendations and Verification]] before changing plugin settings. That note separates easy wins from choices that need a decision.

For AI agents:

1. Read [[AI_CONTEXT]], [[HUMAN_WRITING]], [[40_Resources/Obsidian/Vault Operating System]], and [[60_Claude/7_AI_Information/Agent Operating Guide]] first.
2. Use this folder for exact plugin syntax and vault-specific rules.
3. Do not edit `.obsidian`, plugin `data.json`, secrets, raw clippings, archive material, or Git state unless the user explicitly asks.

## Workflow Map

| Workflow | Read | What the plugins let Jarvis do |
|---|---|---|
| Capture | [[Templates Capture and Periodic Notes]] | Put notes in the right folder with the right frontmatter instead of creating cleanup work. |
| Search and retrieval | [[Search Linking and Navigation]] | Find existing notes before making duplicates; use backlinks, Omnisearch, previews, and pinned navigation. |
| Writing and formatting | [[Appearance Code Math and Reading Experience]] and [[60_Claude/7_AI_Information/Jarvis Writing and Formatting]] | Write Markdown that works in Live Preview, Reading View, Dataview, Tasks, and Spaced Repetition. |
| Dashboards | [[Dataview and Dashboards]] | Rebuild live lists from metadata instead of maintaining stale manual indexes. |
| Tasks and projects | [[Tasks Kanban and Project Tracking]] | Separate atomic actions, project context, and lane-based planning. |
| Learning and review | [[Spaced Repetition and Learning Loops]] | Turn understood notes into recall prompts, not trivia harvested from raw clippings. |
| Visual thinking | [[Visual Thinking with Canvas and Excalidraw]] | Use Canvas for spatial maps and Excalidraw for diagrams, annotations, and system sketches. |
| AI and automation | [[AI Automation and Local Interfaces]] | Keep Copilot, QuickAdd AI, and Local REST API useful without making secrets or uncontrolled writes part of the note layer. |
| Safety and recovery | [[Git Recovery and Vault Safety]] | Understand Obsidian Git, File Recovery, dirty worktrees, and restore boundaries. |

## Which Doc Should I Read?

| Question | Best doc |
|---|---|
| Is this plugin active, delayed, or merely installed? | [[Plugin Inventory and Configuration Map]] |
| Which field should a dashboard query depend on? | [[Dataview and Dashboards]] |
| Should this be a task, a `next:` field, or a Kanban card? | [[Tasks Kanban and Project Tracking]] |
| Where should a new note go when I am editing outside Obsidian? | [[Templates Capture and Periodic Notes]] |
| How should I write cards without creating review noise? | [[Spaced Repetition and Learning Loops]] |
| Should this diagram be Canvas, Excalidraw, or plain Markdown? | [[Visual Thinking with Canvas and Excalidraw]] |
| How do I find a note before creating another one? | [[Search Linking and Navigation]] |
| Can an agent use Copilot, QuickAdd AI, or Local REST API here? | [[AI Automation and Local Interfaces]] |
| What protects the vault if a write goes wrong? | [[Git Recovery and Vault Safety]] |
| How should code, math, and callouts be formatted? | [[Appearance Code Math and Reading Experience]] |
| What plugin settings or workflows are still unresolved? | [[Plugin Gaps Recommendations and Verification]] |

## Maximum Value Path

The fastest practical improvement path is not "install more plugins." It is to make the current plugin set less ambiguous.

1. Configure a small QuickAdd capture menu after approval: inbox thought, source clipping, project note, concept note, daily review, flashcard candidate.
2. Standardize Tasks date conventions for coursework and projects, then add a few Tasks query blocks where task behavior matters more than page metadata.
3. Add a real Spaced Repetition cadence: cards only after distillation, dashboards for review candidates, and card cleanup when review exposes weak prompts.
4. Decide whether Omnisearch should index PDFs, images, and Office files. If yes, evaluate Text Extractor first.
5. Create one or two Excalidraw visual-note templates for systems, algorithms, and source/PDF annotation.
6. Review Local REST API security, especially the insecure server on port `27123`.

## Agent Operating Layer

These notes remain the first stop for agent behavior:

- [[60_Claude/7_AI_Information/Agent Operating Guide]]
- [[60_Claude/7_AI_Information/Jarvis Writing and Formatting]]
- [[60_Claude/7_AI_Information/Plugins]]

This folder should not duplicate their short operating rules. It explains the plugin mechanics behind those rules.

## Existing Source Notes

These older notes are useful context and should be linked, not rewritten in place:

- [[40_Resources/Obsidian/Data View's/Plugins]]
- [[40_Resources/Obsidian/Data View's/Obsidian-Excalidraw Plugin Tutorials]]
- [[40_Resources/Obsidian/Data View's/Tasks Plugin - Review and check your Statuses 2025-12-20 18-37-12]]
- [[40_Resources/Obsidian/Data View's/Inbox Dashboard]]
- [[40_Resources/Obsidian/Data View's/UMN Dashboard]]

## Rule

Plugin docs should answer one question: how does this plugin make Jarvis easier to write, retrieve, review, link, automate, or protect?

If a feature does not change that answer, skip it or link to the official docs.

## Sources

- [Obsidian Help - Core plugins](https://help.obsidian.md/plugins)
- [Obsidian Help - Canvas](https://obsidian.md/help/plugins/canvas)
- [Obsidian Help - Bases syntax](https://obsidian.md/help/bases/syntax)
- [Dataview docs](https://blacksmithgu.github.io/obsidian-dataview/)
- [Tasks User Guide](https://publish.obsidian.md/tasks/)
- [Templater docs](https://silentvoid13.github.io/Templater/)
- [QuickAdd docs](https://quickadd.obsidian.guide/docs/)
- [Obsidian Git docs](https://publish.obsidian.md/git-doc/Features)

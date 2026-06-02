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
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[40_Resources/Obsidian/Plugins/00 Plugin Reference Index]]"
---
# Plugins

This is the Obsidian plugin operating manual for AI agents working in Jarvis.

The goal is not to describe every plugin feature. The goal is to teach agents how to write, organize, retrieve, and maintain notes in this vault without fighting the system already here.

## Deep Reference

This note is the agent-facing operating summary. The stable plugin reference layer lives at [[40_Resources/Obsidian/Plugins/00 Plugin Reference Index]].

Use the stable reference notes when you need deeper settings, source links, workflow examples, or verification notes for Dataview, Tasks, templates, Spaced Repetition, Excalidraw, search/navigation, AI automation, Git safety, or appearance.

## Plugin Status Model

There are three plugin states agents must keep separate:

- **Enabled now:** listed in `.obsidian/community-plugins.json`.
- **Installed on disk:** present under `.obsidian/plugins/`.
- **Lazy-loaded:** managed by Lazy Plugin Loader and likely enabled after Obsidian startup delays.

Do not assume a plugin folder means the plugin is active in the UI. Do not assume `community-plugins.json` tells the full practical story either, because Lazy Plugin Loader references delayed startup plugins.

Current enabled community plugins from `.obsidian/community-plugins.json`:

- Code Styler
- Dataview
- File Explorer++
- Lazy Plugin Loader
- Ninja Cursor
- Latex Suite
- Style Settings
- Tasks
- Recent Files
- Templater
- Paste URL into Selection
- Local REST API

Installed plugin folders also found:

- Copilot
- Excalidraw
- Git
- Hover Editor
- Kanban
- Omnisearch
- Periodic Notes
- Spaced Repetition
- Workspaces Plus

Lazy Plugin Loader references many installed plugins as delayed-start tools, including Copilot, Excalidraw, Git, Hover Editor, Kanban, Omnisearch, Periodic Notes, and Spaced Repetition. It also references `excalibrain`, but no matching plugin folder was found during inspection.

## Core Plugins

These core plugins shape how agents should write and navigate:

- **Backlinks:** use wikilinks so notes become discoverable through backlink panels.
- **Canvas:** use for spatial maps only when a visual layout adds value.
- **Properties:** frontmatter is a first-class retrieval layer. Preserve it.
- **Page Preview:** write headings and links that make hover previews useful.
- **Note Composer:** useful for splitting/merging notes, but agents should not restructure stable notes without permission.
- **Command Palette and Slash Commands:** Obsidian UI conveniences; not usually relevant for file-writing agents.
- **Bookmarks:** user-level navigation. Do not rewrite bookmarks.
- **Outline:** make headings meaningful because users navigate by outline.
- **Workspaces:** preserve layout settings unless explicitly asked.
- **File Recovery:** safety layer, not an editing workflow.
- **Bases:** enabled, but no vault-specific usage pattern was confirmed yet.
- **Slides:** enabled; use only for slide-style notes when requested.

Disabled core plugins:

- Daily Notes
- Templates
- Sync
- Webviewer
- Audio Recorder
- Zettelkasten Prefixer

Because core Templates is disabled, agents should treat **Templater** as the active template system.

## Community Plugin Workflows

### Dataview

Use Dataview for live dashboards, indexes, cleanup queues, project views, task surfaces, and metadata audits.

Vault settings:

- Refresh enabled every `2500ms`.
- Inline Dataview enabled.
- DataviewJS enabled.
- HTML rendering allowed.

Agent rules:

- Prefer Dataview when a list should stay current, such as active projects, stale notes, orphan notes, or flashcard queues.
- Do not manually duplicate lists that Dataview can derive from frontmatter.
- Keep metadata clean before blaming Dataview.
- Use normal Dataview queries first. Use DataviewJS only when plain Dataview cannot express the query clearly.

Needs verification:

- Which DataviewJS patterns the user prefers for complex dashboards.

### Tasks

Use Tasks for concrete actions that should be tracked across the vault.

Vault settings:

- Task format is `tasksPluginEmoji`.
- Done dates and cancelled dates are set automatically.
- Custom statuses include `/` for In Progress and `-` for Cancelled.
- Auto-suggest is enabled.

Agent rules:

- Write tasks only when there is a real action.
- Keep task lines short enough to scan.
- Use the configured Tasks emoji format for due, scheduled, priority, recurrence, completion, and cancellation metadata.
- Do not mix Tasks emoji format with Dataview task metadata unless the user asks for a migration.
- Use task query blocks for live task surfaces; use Dataview task queries only when the dashboard already uses Dataview.

Needs verification:

- Preferred due/scheduled/start-date conventions for course tasks versus project tasks.

### Templater

Use Templater as the main note creation engine.

Vault settings:

- Templates folder: `30_Order/Templates`.
- Trigger on file creation is enabled.
- System commands are disabled.
- Folder templates are enabled for:
  - `10_UMN`
  - `20_Progress`
  - `40_Resources`
  - `60_Claude/20_Distilled_Notes`
  - `60_Claude/30_Source_Summaries`
  - `60_Claude/40_Project_Briefs`

Agent rules:

- Match the existing frontmatter schema instead of inventing new keys.
- If creating notes in configured folders, expect Templater to provide the baseline structure in Obsidian.
- If creating files outside Obsidian, manually follow the same template conventions.
- Never enable Templater system commands without explicit permission.

Needs verification:

- Whether `60_Claude/7_AI_Information` should receive its own folder template later.

### Periodic Notes

Use Periodic Notes for structured reviews, not random daily-note creation.

Vault settings:

- Daily: `60_Claude/50_Reviews/Daily`, template `30_Order/Templates/Headway Templates/Better Today.md`.
- Weekly: `60_Claude/50_Reviews/Weekly`, template `30_Order/Templates/Headway Templates/Better Week.md`.
- Monthly: `60_Claude/50_Reviews/Monthly`, template `30_Order/Templates/Headway Templates/Better Month.md`.
- Yearly is disabled.

Agent rules:

- Put review notes in the configured review folders.
- Do not create daily notes outside the review system.
- Link reviews back to projects, courses, and capability dashboards when they create follow-up work.

### Kanban

Use Kanban for board-shaped workflows: habits, small project stages, triage lanes, and execution queues.

Vault settings:

- Checkboxes are shown.
- Card counts are hidden.
- Full-list lane width is off.
- Dates link to daily notes.
- Theme settings hide several Kanban visual controls and style lanes.

Agent rules:

- Use Kanban when status lanes are the natural shape of the problem.
- Keep card text action-oriented.
- Link cards to canonical notes when the card represents real knowledge or project work.
- Do not turn every index or dashboard into a board.

Known usage:

- Habit boards were created under `10_Areas/Life/Habits`.

Needs verification:

- Preferred lane names for future project boards.

### Spaced Repetition

Use Spaced Repetition for review-ready knowledge, not raw notes.

Vault settings:

- Flashcard tag: `#cards`.
- Folders convert to decks.
- Highlight and bold clozes are enabled.
- Curly-brace clozes are disabled.
- Single-line card separator: `::`.
- Single-line reversed card separator: `:::`.
- Multiline card separator: `?`.
- Multiline reversed card separator: `??`.
- Ignored folders: `30_Order/Templates`, `50_Archive`, `.obsidian`.

Agent rules:

- Create flashcards only after the concept is understood.
- Make cards atomic: one concept, one retrieval target.
- Prefer mechanism questions over definition trivia.
- Keep cards close to the source note so review reinforces the canonical explanation.
- Do not put cards in templates or archive folders.

### Excalidraw

Use Excalidraw for visual thinking: mechanism maps, system diagrams, workflows, and concept relationships that are clearer spatially.

Vault settings:

- Drawing folder: `Excalidraw`.
- Template: `Excalidraw/Template.excalidraw`.
- Scripts folder: `Excalidraw/Scripts`.
- Autosave enabled every 60 seconds.
- Drawings use `.excalidraw`.
- Embeds use wikilinks.
- Preview image type is SVG image.
- AI is enabled, but secrets must not be exposed.

Agent rules:

- Use Excalidraw when layout, arrows, grouping, or visual contrast adds understanding.
- Embed drawings with wikilinks.
- Link drawings back to the notes they explain.
- Do not use Excalidraw as a replacement for a clear text note.
- Do not edit compressed drawing data by hand unless explicitly asked and the format is understood.

Needs verification:

- Whether auto-export to SVG/PNG should be enabled for publishable notes.
- Which Excalidraw scripts in `Excalidraw/Scripts` are canonical.

### Latex Suite

Use Latex Suite for math-heavy coursework and technical explanations.

Agent rules:

- Use inline math for small symbols or expressions.
- Use display math for equations that need to be read, transformed, or referenced.
- Do not use LaTeX as decoration.
- For course notes, explain the mechanism around the formula so the note is useful later.

Needs verification:

- User-specific Latex Suite snippets are not visible in `data.json`; defaults may be in plugin code.

### Code Styler

Use Code Styler to keep code examples readable.

Vault settings:

- Selected theme: Solarized.
- Codeblock line numbers enabled.
- Lines unwrap by default.
- Inline code styling enabled.
- Language tags/icons are hidden.
- Excluded languages include `ad-*` and `reference`.
- Whitelist includes `run-*` and `include`.

Agent rules:

- Always put a real language on fenced code blocks when possible.
- Keep examples short and runnable-looking.
- Use code blocks for code, config, terminal output, and exact syntax.
- Do not paste giant code dumps into notes unless the note is explicitly a source capture.

### Style Settings And CSS Snippets

The vault uses AnuPpuccin with Style Settings and four enabled snippets:

- `headerspace`
- `myedits`
- `rainbowfile_colors`
- `readingview`

Observed behavior:

- Heading spacing is intentionally tight in Live Preview and Reading View.
- Tables, code blocks, headings, Kanban lanes, checkboxes, rainbow file colors, and editor fonts are styled.
- The visual system favors dense, readable Markdown.

Agent rules:

- Do not add manual HTML styling or color hacks in notes.
- Use normal Markdown headings, lists, tables, callouts, links, and code blocks.
- Keep heading hierarchy clean because CSS and Outline make headings a navigation surface.
- Do not edit snippets unless explicitly asked.

### Omnisearch

Use Omnisearch as a retrieval aid in Obsidian.

Vault settings:

- Cache enabled.
- Fuzziness `1`.
- PDF, Office, and image indexing disabled.
- HTTP API disabled.

Agent rules:

- Search before creating notes.
- Do not assume binary or attachment content is searchable.
- Prefer exact note names and wikilinks after finding the right target.

### Recent Files

Use Recent Files only as a human navigation aid.

Agent rules:

- Do not write or reorder recent-file data.
- Use recent files as weak context, not source of truth.

### Hover Editor

Use Hover Editor as an Obsidian UI affordance for quick linked-note inspection.

Vault settings:

- Auto-pin on move.
- Hover delay `300ms`, close delay `600ms`.
- Initial size `400px` by `340px`.
- Hover embeds, footnotes, headings, and blocks enabled.

Agent rules:

- Write link text and headings so hover previews are useful.
- Do not rely on hover state as persistent context.

### File Explorer++

Use File Explorer++ as a navigation layer.

Vault settings:

- Strict path filters hidden.
- Pin filters include many board and dashboard notes, including `00_Dashboard.md`, project boards, course boards, and habit boards.

Agent rules:

- Treat pinned files as navigation landmarks.
- Do not rewrite plugin pin filters unless explicitly asked.

### Paste URL Into Selection

Use this as a human editing convenience for turning selected text into Markdown links.

Agent rules:

- When writing files directly, create Markdown links normally.
- Prefer source links in `source_url` or source sections when they matter for retrieval.

### Ninja Cursor

Use as an editing ergonomics plugin.

Vault settings:

- Reacts to contenteditable, Vim mode, and input elements.

Agent rules:

- No content rules. Do not document it beyond UI behavior.

### Copilot

Copilot is installed and Lazy Plugin Loader references it, but it is sensitive.

Observed settings:

- Default save folder: `50_Archive/copilot/copilot-conversations`.
- Custom prompts folder: `50_Archive/copilot/copilot-custom-prompts`.
- Memory folder: `50_Archive/copilot/memory`.
- System prompts folder: `50_Archive/copilot/system-prompts`.
- Autosave chat enabled.
- Vault indexing enabled on mode switch.
- Inline citations enabled.
- Autonomous agent enabled with tools such as local search, note reading, web search, write/edit file, and memory update.
- Many provider and API key fields exist.

Agent rules:

- Do not expose API keys, tokens, licenses, or provider credentials.
- Treat Copilot conversations and memory under `50_Archive/copilot/` as archival unless the user asks.
- Do not ask Copilot to rewrite vault notes behind the user's back.
- Do not rely on Copilot's memory as source of truth; use vault notes.

### Local REST API

Local REST API is enabled and sensitive.

Observed settings:

- Secure port `27124`.
- Insecure port `27123`.
- Insecure server enabled.
- API key exists in plugin data.

Agent rules:

- Do not expose the API key.
- Do not invoke local REST endpoints unless the user explicitly asks for automation through Obsidian.
- Prefer direct filesystem edits for this coding environment.
- Treat the insecure server as a risk surface, not a convenience.

### Git

Obsidian Git is installed and Lazy Plugin Loader references it.

Observed settings:

- Commit message pattern: `vault backup: {{date}}`.
- Auto-save interval: `0`.
- Auto-push interval: `5`.
- Auto-pull interval: `10`.
- Auto-pull on boot enabled.
- Pull before push enabled.
- Push is not disabled.

Agent rules:

- Do not run Git operations unless the user asks.
- Check status before any commit or push.
- Do not modify backup settings.
- Preserve user changes.

### Workspaces Plus

`workspaces-plus` exists as a folder but no readable manifest was found.

Agent rules:

- Treat as unclear.
- Do not document behavior beyond "needs verification."

## Security-Sensitive Settings

Never expose or copy secrets from plugin data files.

Sensitive areas include:

- Copilot provider keys, tokens, licenses, memory, and autonomous-agent tool settings.
- Local REST API key and crypto settings.
- Excalidraw AI tokens.
- QuickAdd AI provider keys.
- Any future plugin `data.json` credential fields.

When documenting settings, name the existence of a sensitive field only when needed for safety. Do not paste values.

## Needs Verification

- Effective plugin enabled state after Lazy Plugin Loader finishes startup.
- Why the UI screenshot shows more community plugins than `community-plugins.json`.
- Missing or unclear Excalibrain status.
- `workspaces-plus` has no readable manifest.
- NotebookLM resource requires authenticated access and was not locally inspectable.
- Whether `60_Claude/7_AI_Information` should replace or coexist with the typo-like empty `60_Claude/7_Al_Information`.

## Agent Rule Of Thumb

Use plugins when they make notes more searchable, reviewable, visual, or actionable.

Do not use plugins as decoration. The writing still has to pass [[HUMAN_WRITING]].

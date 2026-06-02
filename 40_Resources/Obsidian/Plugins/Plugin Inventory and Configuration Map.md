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
# Plugin Inventory and Configuration Map

This is the canonical inventory for Obsidian plugin state in Jarvis.

Do not assume a plugin folder means active behavior. Jarvis has three plugin states that can diverge:

- Directly enabled: listed in `.obsidian/community-plugins.json`.
- Installed: folder exists under `.obsidian/plugins/`.
- Lazy-loaded: referenced by Lazy Plugin Loader and likely enabled after a startup delay.

## Core Plugins

| Core plugin | State | Jarvis use |
|---|---:|---|
| File explorer | enabled | Folder navigation and visible vault structure. |
| Search | enabled | Built-in fallback search before creating notes. |
| Quick switcher | enabled | Fast known-note navigation. |
| Graph | enabled | Occasional link topology check; not a primary workflow surface. |
| Backlinks | enabled | Context recovery and unlinked mention review. |
| Canvas | enabled | Spatial maps made from notes, cards, and groups. |
| Outgoing links | enabled | Link audit from a note outward. |
| Tags | enabled | Tag review, especially `#cards`. |
| Footnotes | enabled | Source/comment support when Markdown footnotes are useful. |
| Properties | enabled | Frontmatter editing and metadata reliability. |
| Page preview | enabled | Hover reading; rewards good headings and first paragraphs. |
| Note composer | enabled | Split/merge only when note boundaries are already clear. |
| Command palette | enabled | Access to plugin commands without memorizing hotkeys. |
| Slash commands | enabled | Human editing convenience in Obsidian. |
| Editor status | enabled | Editing feedback. |
| Bookmarks | enabled | Human navigation anchors. |
| Markdown importer | enabled | Import support; raw imports still belong in capture/review paths. |
| Random note | enabled | Serendipity only; not an agent workflow. |
| Outline | enabled | Heading navigation; depends on useful heading structure. |
| Word count | enabled | Writing signal, not a quality metric. |
| Slides | enabled | Presentations from notes if needed; not currently central. |
| Workspaces | enabled | Layout state for human sessions. |
| File recovery | enabled | Last-resort note recovery. |
| Publish | enabled | Publishing capability; publish workflow is needs verification. |
| Bases | enabled | New structured views; needs verification before replacing Dataview. |
| Daily notes | disabled | Periodic Notes owns review creation instead. |
| Templates | disabled | Templater owns templates. |
| Zettelkasten Prefixer | disabled | Jarvis uses semantic note names, not timestamp IDs. |
| Audio recorder | disabled | No current audio workflow. |
| Sync | disabled | Git/File Recovery are the visible backup surfaces here. |
| Web viewer | disabled | No current in-vault browser workflow. |

## Community Plugins
Deep per-plugin references: [[QuickAdd Capture Menu]], [[Excalidraw Diagrams and Annotation]], [[Canvas Spatial Maps]], [[Omnisearch and Retrieval]], [[Spaced Repetition and Learning Loops]]. Grouped references cover the rest — see [[00 Plugin Reference Index]]. Note: the Spaced Repetition `data.json` holds two conflicting config layers (`#cards` vs `#flashcards`, bold-cloze on vs off); confirm the effective layer in the Obsidian UI.

| Plugin | ID / folder | Version | Directly enabled? | Lazy-loaded? | Main use in Jarvis | Config inspected? | Needs verification? |
|---|---|---:|---:|---:|---|---:|---|
| Code Styler | `code-styler` | 1.1.7 | yes | instant | Readable code examples. | yes | no |
| Copilot | `copilot` | 3.2.7 | no | long | Vault QA, citations, saved chats, AI memory. | redacted | safety review |
| Dataview | `dataview` | 0.5.68 | yes | instant | Dashboards and metadata queries. | yes | HTML/JS risk |
| Excalidraw | `obsidian-excalidraw-plugin` | 2.21.2 | no | long | Diagrams, visual maps, PDF annotation. | redacted | template/scripts check |
| File Explorer++ | `file-explorer-plus` | 1.3.1 | yes | instant | Pinned/hide filters for navigation. | yes | no |
| Git | `obsidian-git` | 2.38.0 | no | short | Auto backup, pull, push. | yes | auto-push risk |
| Hover Editor | `obsidian-hover-editor` | 0.11.28 | no | short | Preview/edit linked notes without losing context. | yes | no |
| Kanban | `obsidian-kanban` | 2.0.51 | no | short | Lane-based project/habit/source workflows. | yes | lane names |
| Latex Suite | `obsidian-latex-suite` | 1.11.0 | yes | instant | Faster math notation in course notes. | yes | snippet specifics |
| Lazy Plugin Loader | `lazy-plugins` | 1.0.21 | yes | instant | Delays heavy plugins after startup. | yes | effective state |
| Local REST API | `obsidian-local-rest-api` | 3.6.2 | yes | instant | Local automation interface. | redacted | insecure server |
| Ninja Cursor | `ninja-cursor` | 0.0.13 | yes | instant | Cursor visibility only. | yes | no |
| Omnisearch | `omnisearch` | 1.28.2 | no | short | Better vault search. | yes | richer indexing |
| Paste URL into selection | `url-into-selection` | 1.11.4 | yes | instant | Human link hygiene while pasting URLs. | yes | no |
| Periodic Notes | `periodic-notes` | 0.0.17 | no | short | Daily, weekly, monthly review notes. | yes | no |
| QuickAdd | `quickadd` | 2.12.0 | no | short | Capture menu candidate; currently no choices. | redacted | setup needed |
| Recent Files | `recent-files-obsidian` | 1.7.6 | yes | instant | Human session context. | yes | no |
| Spaced Repetition | `obsidian-spaced-repetition` | 1.13.9 | no | short | Flashcards and note review. | yes | review cadence |
| Style Settings | `obsidian-style-settings` | 1.0.9 | yes | instant | Theme/plugin/snippet CSS variables UI. | yes | theme decisions |
| Tasks | `obsidian-tasks-plugin` | 7.23.1 | yes | instant | Searchable task lines and task queries. | yes | date conventions |
| Templater | `templater-obsidian` | 2.18.1 | yes | instant | Folder templates and note creation. | yes | AI docs template |
| Workspaces Plus | `workspaces-plus` | needs verification | no | no | Folder exists without manifest. | no | yes |

## Lazy Plugin Loader

Desktop startup settings:

- Short delay: `5` seconds.
- Long delay: `15` seconds.
- Delay between plugins: `40` seconds.
- Default startup type: `short`.
- Dependency handling: disabled.

Instant plugins include Dataview, Tasks, Templater, Local REST API, Style Settings, Code Styler, Latex Suite, File Explorer++, Paste URL into selection, Recent Files, and Ninja Cursor.

Delayed plugins include Copilot, Excalidraw, Git, Hover Editor, Kanban, Omnisearch, Periodic Notes, QuickAdd, and Spaced Repetition.

`excalibrain` is referenced by Lazy Plugin Loader, but no matching plugin folder was found. Mark this as `needs verification`, not as installed.

## Workflow Hotkeys

| Command | Hotkey | Use |
|---|---|---|
| Backlinks: open | `Alt+B` | Check context and unlinked mentions. |
| Calendar: show calendar view | `Alt+C` | Hotkey exists, but Calendar plugin is not installed in the current plugin folder. |
| Workspace: close others | `Alt+W` | Human layout cleanup. |
| File explorer: open | `Ctrl+Shift+E` | Return to folder navigation. |
| Editor: insert code block | `Alt+V` | Fast fenced-code creation. |
| Omnisearch: show modal | `Alt+F` | Broad search before creating notes. |
| QuickAdd: run QuickAdd | `Alt+Q` | Ready for capture menu, but choices are currently empty. |
| Excalibrain: open hover | `Alt+M` | Hotkey exists, but Excalibrain folder is missing. |

## Appearance and Snippets

Current appearance:

- Theme: AnuPpuccin.
- Enabled snippets:
  - `headerspace.css`: heading spacing.
  - `myedits.css`: custom theme edits; exact scope is needs verification before changing.
  - `rainbowfile_colors.css`: file explorer coloring.
  - `readingview.css`: reading-view tweaks.

Agents should write semantic Markdown that survives without these snippets. Do not store meaning only in color, spacing, or theme variables.

## Sensitive Field Redaction

Never copy values from plugin data when the field name or surrounding context suggests credentials, authentication, providers, certificates, crypto material, licenses, or keys.

High-risk files:

- `.obsidian/plugins/copilot/data.json`
- `.obsidian/plugins/quickadd/data.json`
- `.obsidian/plugins/obsidian-local-rest-api/data.json`
- Excalidraw AI settings inside `.obsidian/plugins/obsidian-excalidraw-plugin/data.json`
- Any Git or remote auth field

Document existence and behavior, not secret values.

## Do Not Edit Without Explicit Permission

- `.obsidian/community-plugins.json`
- `.obsidian/core-plugins.json`
- `.obsidian/app.json`
- `.obsidian/appearance.json`
- `.obsidian/hotkeys.json`
- `.obsidian/plugins/*/data.json`
- `.obsidian/snippets/*.css`
- `.gitignore`
- `60_Claude/05_Clippings/`
- `50_Archive/`
- `60_Claude/7_Al_Information/`

Read these files when needed. Do not use documentation work as a reason to change settings.

## Sources

- [Obsidian Help - Core plugins](https://help.obsidian.md/plugins)
- [Obsidian Help - File Recovery](https://obsidian.md/help/plugins/file-recovery)
- [Obsidian Help - Bases syntax](https://obsidian.md/help/bases/syntax)
- [Lazy Plugin Loader README](https://github.com/alangrainger/obsidian-lazy-plugins)
- [Dataview docs](https://blacksmithgu.github.io/obsidian-dataview/)
- [Tasks User Guide](https://publish.obsidian.md/tasks/)
- [Templater docs](https://silentvoid13.github.io/Templater/)
- [Local REST API README](https://github.com/coddingtonbear/obsidian-local-rest-api)

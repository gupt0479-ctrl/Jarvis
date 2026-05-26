---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - visual-thinking
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/7_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# Visual Thinking with Canvas and Excalidraw

Use visual tools when spatial layout explains the idea better than prose alone. Do not use them to make a weak note look finished.

## Canvas vs Excalidraw

Use Canvas when the objects are mostly notes:

- course maps
- project maps
- source-to-concept layouts
- field OS overviews
- "what links to what?" thinking

Use Excalidraw when the objects are shapes, arrows, flows, or annotations:

- system architecture
- algorithm state transitions
- feedback loops
- concept maps
- PDF figure annotation
- visual summaries that need drawing tools

Use Markdown when a list, table, or short explanation is clearer than a drawing.

## Current Excalidraw Settings

- Drawing folder: `Excalidraw`.
- Template file: `Excalidraw/Template.excalidraw`.
- Scripts folder: `Excalidraw/Scripts`.
- Autosave: enabled.
- Desktop autosave interval: `60000ms`.
- File extension: `.excalidraw`.
- Wikilink embeds: enabled.
- Preview image type: `SVGIMG`.
- Auto-export SVG: disabled.
- Auto-export PNG: disabled.
- PDF import locks pages after import.
- AI features: enabled, but secrets are protected and must not be copied.

Needs verification:

- Whether `Excalidraw/Template.excalidraw` is the canonical template.
- Whether `Excalidraw/Scripts` contains scripts that should be documented.
- Whether auto-export should be enabled for publishable diagrams.
- Excalibrain is referenced by hotkeys and Lazy Plugin Loader, but no matching plugin folder was found.

## Where Visual Notes Belong

- General diagrams -> `Excalidraw/`.
- Course diagrams -> link from the relevant `10_UMN` class/week/concept note.
- Project architecture diagrams -> link from the relevant `20_Progress` project note.
- Source/PDF annotations -> link from the source summary or concept note that explains the figure.

Do not create drawings in `60_Claude/05_Clippings`. Raw capture stays raw.

## Workflows

Concept map:

1. Write the concept note first.
2. Add a small map only for relationships that are easier spatially.
3. Embed the drawing near the explanation.
4. Link the drawing back to the concept note.

System architecture:

1. Start from a project note in `20_Progress`.
2. Draw components, data flow, failure points, and ownership boundaries.
3. Keep decisions and tradeoffs in Markdown near the embed.

Course diagram:

1. Anchor it in the week, lab, exam sheet, or concept note.
2. Use the drawing for state, dependency, or flow.
3. Add a nearby card only after the mechanism is clear.

Source or PDF annotation:

1. Import or annotate the specific figure/page that matters.
2. Keep the source link in the source summary.
3. Summarize the annotated claim in Markdown.

Visual zettelkasten:

1. Use Canvas to lay out canonical notes and source notes.
2. Use Excalidraw when the relation itself needs arrows, grouping, or hand annotation.
3. Do not replace backlinks with image-only maps.

## Embed Examples

Excalidraw embed:

```markdown
![[Queue Failure Map.excalidraw]]
```

Canvas link:

```markdown
[[AI Field OS.canvas]]
```

Diagram with text anchor:

```markdown
The diagram below shows where retrieval can fail before generation sees evidence.

![[RAG Failure Map.excalidraw]]
```

## Agent Safety

Agents should not:

- hand-edit compressed `.excalidraw` data
- expose Excalidraw AI credentials
- replace searchable text with image-only diagrams
- create large visual assets without a text anchor
- turn every concept note into a drawing

Agents may create Markdown scaffolds that link to future drawings, but should not fabricate visual files unless the user asks for visual creation.

## Sources

- [Obsidian Help - Canvas](https://obsidian.md/help/plugins/canvas)
- [Excalidraw plugin README](https://github.com/zsviczian/obsidian-excalidraw-plugin)
- [[40_Resources/Obsidian/Data View's/Obsidian-Excalidraw Plugin Tutorials]]
- [[40_Resources/Obsidian/Vault Operating System]]

---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-31
tags:
  - evergreen
  - system
  - obsidian
  - visual-thinking
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
  - "[[Canvas Spatial Maps]]"
  - "[[Excalidraw Diagrams and Annotation]]"
---
# Visual Thinking with Canvas and Excalidraw
This is the chooser between the two visual tools. Each now has its own deep reference: [[Canvas Spatial Maps]] and [[Excalidraw Diagrams and Annotation]]. Read this note to decide which one a task needs; read the dedicated note for settings, integration, and rules.
==Use a visual tool only when spatial layout explains the idea better than a list or table — never to make a weak note look finished.== Both are barely used in Jarvis: no `.canvas` file and no hand-made `.excalidraw` drawing exists yet.
## Which One
| The objects are… | Use | Why |
|---|---|---|
| Existing notes, and you want their layout | **Canvas** | Cards can be live note references, so the map stays linked to real notes. |
| Shapes, arrows, flows, annotations | **Excalidraw** | Drawing tools for state machines, architecture, annotated figures. |
| A list, table, or 3 sentences would be clearer | **Markdown** | A drawing that only restates a list adds cost and no retrieval value. |
- Canvas examples: course concept webs, project note-maps, source-to-concept layouts.
- Excalidraw examples: system architecture, algorithm state transitions, feedback loops, PDF figure annotation.
## Shared Rule: Text Anchor First
Whichever tool you pick, the visual is embedded in or linked from a Markdown note that states the mechanism in words. The drawing makes relationships visible; the text makes them searchable. A visual with no text host is invisible to Omnisearch and backlinks. This is the single rule that applies to both — the rest is tool-specific and lives in the dedicated docs.
## Where Visual Notes Belong
- General diagrams → `10_Areas/Excalidraw/`.
- Course diagrams → link from the relevant `10_UMN` class/week/concept note.
- Project architecture → link from the relevant `20_Progress` project note.
- Source/PDF annotation → link from the source summary that explains the figure.
- Never create drawings in `60_Claude/05_Clippings/` — raw capture stays raw.
## Embed Syntax
- Excalidraw: `![[RAG Failure Map.excalidraw]]`
- Canvas: `![[Topic Map.canvas]]` or link with `[[Topic Map.canvas]]`
## Agent Safety
- Do not hand-edit compressed `.excalidraw` scene data or author `.canvas` JSON by hand.
- Do not expose Excalidraw AI credentials.
- Do not replace searchable text with image-only diagrams.
- Create visual files only when the user asks; otherwise write a Markdown scaffold with a labelled embed placeholder.
## Sources
- [Obsidian Help - Canvas](https://help.obsidian.md/plugins/canvas)
- [Excalidraw plugin README](https://github.com/zsviczian/obsidian-excalidraw-plugin)
- [[Canvas Spatial Maps]]
- [[Excalidraw Diagrams and Annotation]]
- [[40_Resources/Obsidian/Vault Operating System]]

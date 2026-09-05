---
name: excalidraw-diagram
description: Build a diagram element-by-element on the live Excalidraw MCP canvas, then export it into the vault as a native Obsidian Excalidraw file linked from a project note.
---
# excalidraw-diagram

**Usage:** `/excalidraw-diagram` — describe what to diagram and which note it belongs to.

---

## What this is for

The `excalidraw` MCP server (`.mcp.json`, backed by `30_Order/System/excalidraw-mcp/`) gives 26 tools for programmatic canvas control — create/update/delete elements, layout (align, distribute, group), scene inspection, and file export. Use it for architecture diagrams, project maps, process flows, and anything else better drawn than written — anywhere `10_Areas/Excalidraw/Claude OS Map.md`-style visuals would help.

It does **not** replace the Excalidraw plugin or ExcaliBrain — it's a way to *populate* `.excalidraw` files programmatically. The plugin still renders them; ExcaliBrain still auto-builds its link-graph view from vault wikilinks.

## Before drawing

1. Call `read_diagram_guide` once per session — it returns the color palette, sizing rules, and layout anti-patterns the tool was designed around. Diagrams built without it tend to look cramped/default-colored.
2. Check the canvas server is reachable: `curl http://127.0.0.1:3000/health`. If it's not running, start it in the background:
   ```
   cd "30_Order/System/excalidraw-mcp" && npm run canvas
   ```
   (Tool calls still work without it — elements are tracked server-side — but screenshots and viewport control need it running with a browser open.)

## Workflow

1. **Build** — use `create_element` / `batch_create_elements` for shapes and text, then `align_elements` / `distribute_elements` / `group_elements` for layout. Prefer batch creation for anything with more than a few elements.
2. **Verify** — call `describe_scene` to sanity-check structure. If the canvas is open in a browser, `get_canvas_screenshot` gives a visual check before calling it done.
3. **Export** — call `export_scene`. This returns standard `.excalidraw` JSON (`type: "excalidraw"`, `elements`, `appState`).
4. **Save into the vault** — write that JSON verbatim to `10_Areas/Excalidraw/<Descriptive Name>.excalidraw` (plain extension, not `.excalidraw.md` — this vault's plugin setting expects the legacy JSON format). Use a name that describes the diagram, not the tool.
5. **Link it in** — add an embed to the project or concept note this diagram belongs to:
   ```markdown
   ![[Descriptive Name.excalidraw]]
   ```
   This is the step that makes ExcaliBrain aware of it — ExcaliBrain surfaces whatever is reachable from the vault's wikilink graph, so an unlinked `.excalidraw` file is invisible to it even though the Excalidraw plugin can still open it directly.
6. **Clear or leave the live canvas** — the canvas server is in-memory and per-session; there's no need to clear it between diagrams unless the next one should start from a blank scene (`clear_canvas`).

## Notes

- `export_to_excalidraw_url` uploads to excalidraw.com — only use it if the user explicitly wants a shareable public link; default to keeping diagrams local to the vault.
- If asked to update an existing vault diagram: read the `.excalidraw` file, `import_scene` its contents onto the canvas, make changes, then re-export and overwrite the file.
- Follow `HUMAN_WRITING.md` conventions for any text labels inside the diagram — no filler, concrete labels over vague ones.

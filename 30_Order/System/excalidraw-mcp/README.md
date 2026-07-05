# excalidraw-mcp

Local install of [mcp-excalidraw-server](https://github.com/yctimlin/mcp_excalidraw) (npm `mcp-excalidraw-server`), wired into Jarvis so Claude Code can draw and edit Excalidraw diagrams element-by-element instead of one-shot generating them.

## What's here

Just `package.json` — everything else (`node_modules/mcp-excalidraw-server`) is `npm install`ed and gitignored, since it's a third-party package, not vault content.

## Architecture

Two separate processes:

- **Canvas server** — a small Express + WebSocket app that holds the live scene in memory and serves a browser UI at `http://127.0.0.1:3000`. Not an MCP server; you start it manually.
- **MCP server** — `node_modules/mcp-excalidraw-server/dist/index.js`, run over stdio by Claude Code (registered as `excalidraw` in `.mcp.json`). It talks to the canvas server over HTTP/WebSocket (`EXPRESS_SERVER_URL`) so every tool call is reflected live if the canvas is open in a browser.

The canvas holds state only in memory — restarting it clears the scene. That's fine: the actual persistence layer is Obsidian. Once a diagram is done, Claude exports it (`export_scene`) and writes the JSON straight into `10_Areas/Excalidraw/*.excalidraw`, which is a real vault note the Obsidian Excalidraw plugin opens natively (this vault's plugin is configured with `useExcalidrawExtension: true`, so plain `.excalidraw` JSON files — not `.excalidraw.md` — are what it expects).

## Starting the canvas

The MCP tools work without the canvas open (elements are still created/tracked server-side), but screenshots (`get_canvas_screenshot`), viewport control, and image export need a browser pointed at it.

```powershell
cd "30_Order\System\excalidraw-mcp"
npm run canvas          # starts on http://127.0.0.1:3000 (PORT env overrides)
```

Then open `http://127.0.0.1:3000` in a browser to watch diagrams build live.

## Using it

See `.claude/skills/excalidraw-diagram.md` / `/excalidraw-diagram` for the drawing workflow (build → verify → export into the vault → link into the relevant note so ExcaliBrain picks it up).

## Updating

```powershell
cd "30_Order\System\excalidraw-mcp"
npm update mcp-excalidraw-server
```

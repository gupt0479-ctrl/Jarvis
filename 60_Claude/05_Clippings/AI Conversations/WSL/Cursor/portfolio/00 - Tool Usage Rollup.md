---
type: dashboard
status: auto-generated
tags:
  - cursor
  - wsl
---
# Tool Usage Rollup — portfolio

```dataviewjs
const pages = dv.pages("60_Claude/05_Clippings/AI Conversations/WSL/Cursor/portfolio").where(p => p.type === "input");
let toolTotals = {};
let fileSessions = {};
for (const p of pages) {
  for (const [tool, count] of Object.entries(p.tools_used ?? {})) {
    toolTotals[tool] = (toolTotals[tool] ?? 0) + count;
  }
  for (const f of p.files_touched ?? []) {
    fileSessions[f] = (fileSessions[f] ?? 0) + 1;
  }
}
dv.paragraph("**Total sessions:** " + pages.length);
dv.header(2, "Tool usage");
dv.table(["Tool", "Total uses"], Object.entries(toolTotals).sort((a, b) => b[1] - a[1]));
dv.header(2, "Files touched (by session count)");
dv.table(["File", "Sessions"], Object.entries(fileSessions).sort((a, b) => b[1] - a[1]));
```

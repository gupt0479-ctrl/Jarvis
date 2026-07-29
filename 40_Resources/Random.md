---
type: evergreen
status: sprout
created: 2025-10-23
updated: 2026-07-29
tags:
  - evergreen
notes:
  - "[[40_Resources/CS/Links|Links]]"
  - "[[40_Resources/UMN/Links|Links]]"
  - "[[Useful Links]]"
---
# Links
## In General
1. [All pdfs for books](https://en.wikipedia.org/wiki/Anna%27s_Archive) — a Wikipedia article about Anna's Archive, a shadow library aggregating pirated books/papers. → no relations
2. [Website to Learn Anything?](https://learn-anything.xyz/) — a community-curated tree of learning roadmaps by topic. → no relations
3. [Battery Report](file:///C:/Users/Anant%20Gupta/battery-report.html): **IMPORTANT** — a local Windows `powercfg` battery health report, not a web resource. → no relations
4. [Web Archive](https://web.archive.org/) for everything — the Internet Archive's Wayback Machine, a general page-snapshot tool. → no relations
5. Mini money(==WORKS==) - [insta](https://www.minimoney.guide/) — a personal-finance/side-income Instagram-linked guide. → no relations
6. [Magic Fretboard - Guitar](https://magicfretboard_listen.ar.io/) — a guitar-fretboard learning tool. → no relations
7. Hall of hacks - [Hackathons](https://hallofhackss.com/feed) — the same hackathon-project archive already ingested. → [[Hall of Hacks — Winning Hackathon Archive (web)]], [[Hall of Hacks — Winning Hackathon Patterns Analysis]]
8.
## For me 
- Portfolio to learn about human body: [Huberman Lab](https://www.hubermanlab.com/) — Dr. Andrew Huberman's neuroscience/health podcast and resource site. → no relations
- Cool af portfolio: [Bruno-simon](https://bruno-simon.com/) — Bruno Simon's 3D interactive portfolio site, a Three.js/WebGL design reference. → no relations
-
# Data view (Evergreen)
## Inbox
```dataview
TABLE status, created, notes
FROM "60_Claude/00_Inbox"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
## UMN
```dataview
TABLE status, created, notes
FROM "40_Resources/UMN"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
## Progress and Resources
```dataview
TABLE status, created, notes
FROM "20_Progress" OR "40_Resources"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
## The rest
```dataview
TABLE status, created, notes
FROM "30_Order" OR "50_Archive" OR "60_Claude/05_Clippings"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
# MOC

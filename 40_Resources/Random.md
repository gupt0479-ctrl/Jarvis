---
type: evergreen
status: sprout
created: 2025-10-23
tags:
  - evergreen
notes:
  - "[[40_Resources/CS/Links|Links]]"
  - "[[10_UMN/Links|Links]]"
  - "[[Useful Links]]"
---
# Links
## In General
1. [All pdfs for books](https://en.wikipedia.org/wiki/Anna%27s_Archive)
2. [Website to Learn Anything?](https://learn-anything.xyz/)
3. [Battery Report](file:///C:/Users/Anant%20Gupta/battery-report.html): **IMPORTANT**
4. [Web Archive](https://web.archive.org/) for everything 
5. Mini money(==WORKS==) - [insta](https://www.minimoney.guide/)
6. [Magic Fretboard - Guitar](https://magicfretboard_listen.ar.io/)
7. 
## For me 
- Portfolio to learn about human body: [Huberman Lab](https://www.hubermanlab.com/)
- Cool af portfolio: [Bruno-simon](https://bruno-simon.com/)
- 
# Data view (Evergreen)
## Inbox
```dataview
TABLE status, created, notes
FROM "00_Inbox"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
## UMN
```dataview
TABLE status, created, notes
FROM "10_UMN"
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
FROM "30_Order" OR "50_Archive" OR "Clippings"
WHERE type = "evergreen"
SORT status ASC, file.mtime DESC
```
# MOC

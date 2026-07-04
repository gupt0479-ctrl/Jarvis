---
type: evergreen
status: tree
created: 2025-12-25
tags:
  - evergreen
notes:
  - "[[Random]]"
---
# Data view
## AI Conversations
```dataview
TABLE title, description, source
FROM "60_Claude/05_Clippings"
WHERE type != "evergreen"
SORT created ASC
```
## PDFs

## Videos

## Web

# Where to Go?
> [!IMPORTANT] Interlinks of all web clippings done and where they have landed.
> - If been deleted not written here.

**2026-07-03 → 07-04 — full ingestion pass (Fable).** Every signal-tiered PDF and web clip is ingested. Landings:
- **PDFs →** `60_Claude/10_Source_Summaries/PDF Ingestion/` (29 notes)
- **Web clips →** `60_Claude/10_Source_Summaries/Web Ingestion/` (17 notes)
- Itemized source-clip → summary-note mapping is in the session log (`60_Claude/07_AI_Information/Session Logs/log.md`, entries tagged `fable-p4-*` and `fable-pass2-ingest`).
- **Duplicates not re-noted** (source content already captured elsewhere): Maverick AI Resource Hub 1 & 3 (= Maverick prompt PDFs), Maverick AI Resource Hub 2 (= MavGPT Resume PDF), Road Map.pdf (= AI Generalist Roadmap — Outskill).
- **Skipped per signal tiers** (no note): Claude Council stub, Magic Fretboard, App Privacy Policy Generator.

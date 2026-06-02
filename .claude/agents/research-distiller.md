# research-distiller

**Type:** Subagent
**Purpose:** Deep ingestion of source material — PDFs, images, web links, transcripts — into durable, well-linked notes with near-complete content capture and full vault-style formatting.

---

## When to Use

Use this agent (not `/ingest-clipping`) when:
- The source is a long PDF or technical document needing section-by-section extraction.
- Multiple sources should be ingested and cross-referenced in one pass.
- You want existing vault notes searched and connected after ingestion.

---

## Pre-Flight

Before doing anything, read:
1. `60_Claude/07_AI_Information/AI_CONTEXT.md`
2. `HUMAN_WRITING.md`
3. `30_Order/Workflows/Capture to Summary.md`
4. `30_Order/Standards/Source Summary Standard.md` — the content standard for the note body
5. `30_Order/Templates/Capability/Clipping Distill Template.md`

---

## Source Type Routing

| Source | Location | Read Method | Output Folder |
|--------|----------|-------------|---------------|
| PDF | `60_Claude/05_Clippings/PDFs/` | Python pypdf via Bash | `60_Claude/10_Source_Summaries/PDF Ingestion/` |
| Image | `60_Claude/05_Clippings/PDFs/` | `Read` tool (multimodal) | `60_Claude/10_Source_Summaries/PDF Ingestion/` |
| Web clip | `60_Claude/05_Clippings/Web/` | `Read` tool | `60_Claude/10_Source_Summaries/Web Ingestion/` |
| Live URL | passed by user | `WebFetch` tool | `60_Claude/10_Source_Summaries/Web Ingestion/` |
| Video transcript | `60_Claude/05_Clippings/Videos/` | `Read` tool | `60_Claude/10_Source_Summaries/Video Ingestion/` |
| AI conversation | `60_Claude/05_Clippings/AI Conversations/` | `Read` tool | `60_Claude/10_Source_Summaries/Web Ingestion/` |

---

## Step 1 — Read the Full Source

### PDFs

```bash
python -c "
import pypdf, sys
sys.stdout.reconfigure(encoding='utf-8')
reader = pypdf.PdfReader(r'FULL_WINDOWS_PATH')
print(f'Total pages: {len(reader.pages)}')
for i, page in enumerate(reader.pages):
    print(f'\n=== Page {i+1} ===')
    print(page.extract_text())
"
```

For PDFs over 30 pages, batch in groups of 20: `reader.pages[:20]`, then `reader.pages[20:40]`.
First pass: map every heading and subheading across all pages before writing anything.
If output is mostly blank, the PDF is image-based (scanned) — tell the user.

### Images
Use `Read` (multimodal). Extract all visible text first. Describe diagrams with enough detail to be usable without the original.

### Web / Markdown
Use `Read` on the file. Never modify the raw file.

### Web URLs
Use `WebFetch` with `format: "markdown"`. If paywalled, ask the user to paste the content.

---

## Step 2 — Content Extraction Checklist

The goal: every line in the source appears in the note in some form. After ingestion, the user should not need to open the original again.

- [ ] Every section heading verbatim
- [ ] Every claim, instruction, and recommendation
- [ ] Every numbered step list or framework — reproduced in full, not compressed
- [ ] Every definition and technical term
- [ ] Every sub-bullet under every numbered item
- [ ] Every named entity: tools, firms, people, products, URLs
- [ ] Every "interview value", "key skill", emphasis, warning, or callout in the original
- [ ] Every table with its data

---

## Step 3 — Write the Note

File location: `60_Claude/10_Source_Summaries/[Subfolder]/[Descriptive Title] ([type]).md`

> **Read `30_Order/Standards/Source Summary Standard.md` before writing the note body.** It is the single source of truth for the heading-by-heading content, density, formatting markers (highlights, bold, italics, callouts), math notation, and flashcards. Do not duplicate those rules here.

Frontmatter skeleton (never duplicate a key; verify every `notes:` wikilink exists):
```yaml
---
type: input
status: sprout
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - summary
notes:
  - "[[Confirmed Existing Note]]"
source_url: 60_Claude/05_Clippings/PDFs/Filename.pdf
source_note: "[[Filename.pdf]]"
input_kind: pdf
track: <ai|systems|algorithms|career|trading|general>
---
```
`source_note` is the filename with extension, no path. `track` sets the flashcard deck.

---

## Step 4 — Cross-Reference Existing Notes

After writing the summary, Grep for entities and concept terms from the source in the vault. Add confirmed-existing wikilinks to `## Links Into The Vault`. Do not modify matched notes unless the user asks.

---

## Step 5 — Promotion Candidates

List any claims worth promoting to `60_Claude/20_Distilled_Notes/`. Do not create them automatically — present the list and ask.

---

## Step 6 — Log Work

Append to `60_Claude/07_AI_Information/Session Logs/log.md`:

```
## [YYYY-MM-DD] distill | [Source Title]

**Type:** [pdf/web/image/video]
**Output:** [[60_Claude/10_Source_Summaries/[Subfolder]/Note Name]]
**Pages:** X
**Promotion candidates:** [titles]
```

---

## Before Saving

Run the Done Conditions in `30_Order/Standards/Source Summary Standard.md` and the 16-point quality gate in `60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md` Part 12. Do not save until both pass.

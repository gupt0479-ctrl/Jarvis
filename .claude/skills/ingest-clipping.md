---
name: ingesting-clipping
description: Ingests any source — PDF, image, web link, or markdown file — into a structured summary in 60_Claude/10_Source_Summaries/.
---
# ingest-clipping

**Usage:**
- `/ingest-clipping "PDFs/filename.pdf"` — PDF in 05_Clippings/PDFs/
- `/ingest-clipping "Web/filename.md"` — web clip in 05_Clippings/Web/
- `/ingest-clipping "https://example.com"` — live URL
- `/ingest-clipping` — list available clippings and ask

---

## Source Type Routing

| Input | Read method | Output subfolder |
|-------|-------------|-----------------|
| `.pdf` in `05_Clippings/PDFs/` | Python pypdf via Bash | `10_Source_Summaries/PDF Ingestion/` |
| `.png/.jpg/.jpeg/.webp` | `Read` tool (multimodal) | `10_Source_Summaries/PDF Ingestion/` |
| `http://` or `https://` URL | `WebFetch` tool | `10_Source_Summaries/Web Ingestion/` |
| `.md` in `05_Clippings/Web/` | `Read` tool | `10_Source_Summaries/Web Ingestion/` |
| `.md` in `05_Clippings/Videos/` | `Read` tool | `10_Source_Summaries/Video Ingestion/` |
| `.md` in `05_Clippings/AI Conversations/` | `Read` tool | `10_Source_Summaries/Web Ingestion/` |

If no path given, list `60_Claude/05_Clippings/` subfolders and ask.

---

## Step 1 — Read the Source

### PDFs
Extract with Python. `pypdf` is installed on this system:
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
For PDFs over 30 pages, batch: `reader.pages[:20]`, then `reader.pages[20:40]`. If the output is blank or garbled binary, the PDF is image-based (scanned) — tell the user, OCR is needed.

### Images
Use the `Read` tool. Claude is multimodal — it will see the image. Extract all visible text, labels, numbers, annotations, and URLs.

### Web URLs
Use `WebFetch` with `format: "markdown"`. If paywalled, tell the user and ask for pasted content.

### Markdown clips
Use `Read` on the file in `05_Clippings/`. Never modify the raw file.

---

## Step 2 — Extract Content

**The goal: every line in the source should appear in the note in some form.** After ingestion, the user should never need to open the original PDF again.

- Map the document structure first: list every heading and subheading before writing.
- Preserve the source's own section order and headings exactly.
- Reproduce all numbered steps, frameworks, checklists, and lists in full — do not compress them.
- Do not summarize away detail. If the source has 6 steps, write all 6. If it has 5 project types, write all 5 with every sub-bullet.
- Every named concept, framework, term, tool, company, or person gets captured.
- Every "interview value", "key skill", warning, or emphasis in the source becomes a callout.

---

## Step 3 — Write the Summary Note

Filename: `[Descriptive Title] ([type]).md` in the routed subfolder.

> **Read `30_Order/Standards/Source Summary Standard.md` before writing the note body.** It is the single source of truth for what goes under each heading, how dense each section is, which plugin syntax applies (highlights, bold, italics, callouts, math), and the flashcard rules and failure modes. Do not duplicate those content rules here.

Frontmatter skeleton (no duplicate keys; verify every `notes:` wikilink exists with Grep first):
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
`source_note` is the filename with extension, no path. `track` sets the flashcard deck (`track: trading` → `#cards/trading`).

---

## Step 4 — Log the Session

Append to `60_Claude/07_AI_Information/Session Logs/log.md`:

```
## [YYYY-MM-DD] ingest | [Source Title]

- Source: `60_Claude/05_Clippings/[path]` ([type])
- Created: [[60_Claude/10_Source_Summaries/[Subfolder]/Note Name]]
- Pages: [X]
- Promotion candidates: [any claims worth distilling]
```

---

## Step 5 — Present Results

Tell the user:
1. Link to the created summary.
2. Page count processed.
3. Any blank pages (scanned PDFs).
4. Promotion candidates — ask before creating distilled notes.

---

## Before Saving

Run the Done Conditions in `30_Order/Standards/Source Summary Standard.md` and the 16-point quality gate in `60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md` Part 12. Do not save until both pass.

---

## Safety Rules

- Never modify `60_Claude/05_Clippings/` — read-only raw sources.
- Search before creating — extend an existing summary if one already exists.
- Route correctly — PDFs → `PDF Ingestion/`, web → `Web Ingestion/`, video → `Video Ingestion/`.

---
name: ingesting-clipping
description: Ingests any source — PDF, image, web link, or markdown clip — into a structured summary in 60_Claude/10_Source_Summaries/. Use for /ingest-clipping.
---
# ingesting-clipping

Turn one raw source into one complete summary note. After ingestion the user should never need to reopen the original.

**Usage:**
- `/ingest-clipping "PDFs/filename.pdf"` — PDF in `05_Clippings/PDFs/`
- `/ingest-clipping "Web/filename.md"` — web clip in `05_Clippings/Web/`
- `/ingest-clipping "https://example.com"` — live URL
- `/ingest-clipping` — list available clippings and ask which one

---

## Source Type Routing

| Input | Read method | Output subfolder |
|-------|-------------|------------------|
| `.pdf` in `05_Clippings/PDFs/` | `scripts/extract_pdf.py` (pypdf → multimodal fallback) | `10_Source_Summaries/PDF Ingestion/` |
| `.png/.jpg/.jpeg/.webp` | `Read` tool (multimodal) | `10_Source_Summaries/PDF Ingestion/` |
| `http://` or `https://` URL | `WebFetch` (Jina-prefixed; see reference §4) | `10_Source_Summaries/Web Ingestion/` |
| `github.com/<owner>/<repo>` URL or clip | `gh api` / GitHub MCP tools — README + file tree, never the rendered page (reference §6) | `10_Source_Summaries/Github Ingestion/` |
| `.md` in `05_Clippings/Web/` | `Read` tool | `10_Source_Summaries/Web Ingestion/` |
| `.md` in `05_Clippings/Videos/` | `Read` tool | `10_Source_Summaries/Video Ingestion/` |
| `.md` in `05_Clippings/AI Conversations/` | Not handled here — use `/export-ai-session` (Claude Code) or follow `30_Order/Workflows/Conversation Capture.md` by hand. Output goes to `60_Claude/07_AI_Information/AI Conversation - Summaries/` with its own decision-focused template, not this skill's generic Source Summary Standard. |

If no path is given, list `60_Claude/05_Clippings/` subfolders and ask.

---

## Step 1 — Read the source

Pick the method for the source type and read the whole thing. **Each method has a failure mode and a fallback — read `reference.md` §2–§6 before extracting; do not improvise.** The one rule that matters most: a sparse or scanned PDF is not a dead end. `scripts/extract_pdf.py` exits with code `2` when text extraction is too thin; when that happens, pass the PDF path to the multimodal `Read` tool and read the pages as images (reference §2). The other common dead end: a `.md` clip whose body is just an empty `<iframe>` (Google Sheets, Notion, Airtable embeds clip empty) — that is a fallback case too, not a source with no content (reference §5).

## Step 2 — Extract content

The goal: **every line in the source appears in the note in some form.** Map the document structure first (list every heading before writing), preserve the source's own section order and headings, and reproduce all numbered steps, frameworks, and lists in full — do not compress. Every named concept, tool, person, warning, and emphasis gets captured. Full mandate and the quality gate: `reference.md` §6.

## Step 3 — Write the summary note

Filename: `[Descriptive Title] ([type]).md` in the routed subfolder.

> **Read `30_Order/Standards/Source Summary Standard.md` before writing the note body.** It is the single source of truth for what goes under each heading, density, plugin syntax (highlights, bold, italics, callouts, math), and flashcard rules. Do not duplicate those rules here.

Frontmatter skeletons per source type are in `examples.md`. Verify every `notes:` wikilink exists (Grep) before saving; never duplicate a frontmatter key.

## Step 4 — Log the session

Append to `60_Claude/07_AI_Information/Session Logs/log.md`:

```
## [YYYY-MM-DD] ingest | [Source Title]

- Source: `60_Claude/05_Clippings/[path]` ([type])
- Created: [[60_Claude/10_Source_Summaries/[Subfolder]/Note Name]]
- Pages: [X]
- Promotion candidates: [any claims worth distilling]
```

## Step 5 — Present results

Tell the user: link to the created summary, page count processed, any blank/scanned pages, and promotion candidates — ask before creating distilled notes.

---

## Before saving

Run the Done Conditions in `30_Order/Standards/Source Summary Standard.md` and the 16-point quality gate in `60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md` Part 12. Do not save until both pass.

## Safety rules

- Never modify `60_Claude/05_Clippings/` — read-only raw sources.
- Search before creating — extend an existing summary if one already exists.
- Route correctly — PDFs → `PDF Ingestion/`, web → `Web Ingestion/`, video → `Video Ingestion/`, GitHub repos → `Github Ingestion/`.
- Never scrape a GitHub repo's rendered page as a substitute for reading the repo. A README capture (web clip or Jina/WebFetch) only proves what the repo claims; `gh api` / GitHub MCP tools against the actual files prove what it does.

---

Extraction details and failure modes: `reference.md`. Per-source frontmatter and gold-standard shape: `examples.md`. PDF extraction script: `scripts/extract_pdf.py`.

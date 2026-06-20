# ingesting-clipping — Reference

Deep detail loaded only when a source type needs it. SKILL.md is the entry point.

## Contents

1. [Overview](#1-overview)
2. [PDF extraction](#2-pdf-extraction)
3. [Image extraction](#3-image-extraction)
4. [Web URL extraction](#4-web-url-extraction)
5. [Markdown clip extraction](#5-markdown-clip-extraction)
6. [Quality gate + content mandate](#6-quality-gate--content-mandate)

---

## 1. Overview

One source → one complete note. Read the whole source with the method for its type, capture everything (§6), then write per `30_Order/Standards/Source Summary Standard.md`. Each method below names its failure mode and the fallback to take — taking the fallback is mandatory, not optional.

---

## 2. PDF extraction

**Primary path — `scripts/extract_pdf.py`.** Run it via Bash with the full Windows path:

```bash
cd "D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\skills\ingesting-clipping"
python scripts\extract_pdf.py "FULL_WINDOWS_PATH_TO_PDF"
```

The script prints page count and per-page text. Read the exit code:

- **Exit 0** — extraction succeeded. Use the printed text.
- **Exit 2** — output averaged under 200 chars/page. The PDF is scanned or image-based. **Do not use the sparse pypdf text. Switch to the multimodal fallback below.**
- **Exit 1** — file missing or `pypdf` not installed (`pip install pypdf --break-system-packages`).

**Fallback — multimodal `Read` (the critical instruction).** When the script exits 2, pass the PDF file path directly to the `Read` tool. Claude sees each page as an image. Extract all visible text, table data, annotations, and diagram labels from what you see. Do not skip pages; if a page is genuinely blank, note it explicitly. This replaces the old "OCR is needed — tell the user" dead end: you can read the PDF yourself.

**Long PDFs.** First pass always maps every heading/subheading before writing. On the pypdf path, the script handles all pages in one run; for very large files batch your *writing* in 20-page chunks. On the multimodal `Read` path, read ~5 pages at a time and write notes for that batch before reading the next — this keeps context manageable and prevents dropped detail.

---

## 3. Image extraction

Use the `Read` tool — Claude is multimodal and sees the image directly. Extract all visible text, labels, numbers, annotations, and URLs. Describe any diagram in enough detail that the note stands without the original. No script needed.

---

## 4. Web URL extraction

**Primary path — Jina Reader + `WebFetch`.** For article/blog/doc URLs, prefix the URL with `https://r.jina.ai/` before calling `WebFetch` — Jina Reader returns clean markdown with the boilerplate stripped:

```
WebFetch  https://r.jina.ai/https://example.com/the-article
```

**Fallback — direct `WebFetch`.** If the Jina-prefixed fetch is paywalled, blocked, or returns nothing useful, call `WebFetch` on the bare URL with `format: "markdown"`. If both fail or the content is gated, tell the user and ask them to paste the content. Never modify any raw clip while reading.

---

## 5. Markdown clip extraction

Use the `Read` tool on the file in `05_Clippings/`. **Never modify the raw file** — it is a read-only source of record. Web clips → Web Ingestion; video transcripts → Video Ingestion; AI conversations → Web Ingestion (see SKILL.md routing table).

---

## 6. Quality gate + content mandate

> **Content Extraction Mandate.** Every line in the source should appear in the note in some form. After ingestion the user should never need to open the original again. Map structure first (list every heading before writing); preserve the source's own section order and headings; reproduce all numbered steps, frameworks, checklists, and tables in full — do not compress; capture every named concept, term, tool, company, person, warning, and emphasis. If the source has 6 steps, write all 6.

**Before saving, run the gate — do not save until it passes:**

- The **Done Conditions** checklist in `30_Order/Standards/Source Summary Standard.md`.
- The 16-point quality gate in `60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md` Part 12.

These live in their source files on purpose — run them there, do not copy them here.

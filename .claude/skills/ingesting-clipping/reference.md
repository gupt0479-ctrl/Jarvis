# ingesting-clipping — Reference

Deep detail loaded only when a source type needs it. SKILL.md is the entry point.

## Contents

1. [Overview](#1-overview)
2. [PDF extraction](#2-pdf-extraction)
3. [Image extraction](#3-image-extraction)
4. [Web URL extraction](#4-web-url-extraction)
5. [Markdown clip extraction](#5-markdown-clip-extraction)
6. [GitHub repository extraction](#6-github-repository-extraction)
7. [Quality gate + content mandate](#7-quality-gate--content-mandate)

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

**Failure mode — the empty-embed clip.** Some sources (Google Sheets, Notion embeds, Airtable, anything that renders via client-side JS) clip down to a bare `<iframe>` tag with no real content — the Web Clipper captured the page shell, not the data. If the clip body is just an iframe, an image with no caption, or under ~30 words against a title that promises more, do not write a summary from that shell. Fallback: try `WebFetch` on the live `source:` URL in the frontmatter; if that also returns nothing usable, tell the user the source needs a manual export (e.g. download the sheet as CSV, copy the table as text) before it can be ingested. Say this plainly in Step 5 — do not silently produce a thin note.

**GitHub repo pages clipped as web pages.** A `.md` clip whose `source:` is a `github.com/<owner>/<repo>` URL (the Web Clipper grabbed the rendered README) is a GitHub source, not a generic web source — route it through §6, not this section. The clipped README is useful as the discovery record, but treat the live repo (via `gh api` / GitHub MCP, §6) as the source of truth for what the tool actually does.

---

## 6. GitHub repository extraction

A repo is not a webpage with extra steps — the README only states what a tool claims; the file tree and source files show what it does. Scraping the rendered GitHub page (Jina/WebFetch) gets you the README's marketing copy and nothing else, which is the exact failure mode this section exists to prevent.

**Primary path — `gh api` (no clone, no extra install; this machine already has `gh` and `git`).**

```bash
gh api repos/<owner>/<repo> --jq '{description,stargazers_count,forks_count,pushed_at,license:.license.name}'
gh api repos/<owner>/<repo>/git/trees/main?recursive=true --jq '.tree[] | select(.type=="blob") | .path'
gh api repos/<owner>/<repo>/contents/<path> --jq '.content' | base64 -d
```

The first call gives real metadata (stars, last push, license) instead of trusting a stale clip. The second gives the file tree — this is what separates "I read about it" from "I read it": a repo advertising "skills, instincts, memory" should show that as files, not just prose. The third pulls any specific file's actual content (README, SKILL.md, package.json, main entrypoint) decoded from GitHub's base64 API response. The GitHub MCP tools (`mcp__github__get_file_contents`, `mcp__github__search_code`) do the same thing when `gh` is unavailable or when searching code across multiple repos at once.

**Two depths — pick based on what the repo is for:**

- **Reference-only repos** (awesome-lists, "bookmark for later," anything in `40_Resources/CS/Repos.md` you are not about to install): metadata + README via `gh api` is enough. Do not clone.
- **Adoption candidates** (a tool you are about to install, fork, or wire into this vault's `.claude/`): also fetch the 2-4 files that actually matter — the entrypoint, the skill/agent definition file, the config schema — via the `contents` API call above. Reproduce what they actually say, not what the README summarizes them as. Only `git clone` to a scratch path outside the vault (e.g. the OS temp directory) if you need to run the code or grep across many files; delete the clone after, since `60_Claude/05_Clippings/` is markdown-only and the vault has no contract for cached source trees.

**Fallback.** If the repo is private, deleted, or `gh api` 404s, fall back to the clipped README or a Jina/WebFetch pass on the live URL, and say explicitly in the note that this is README-only, unverified-against-source coverage.

---

## 7. Quality gate + content mandate

> **Content Extraction Mandate.** Every line in the source should appear in the note in some form. After ingestion the user should never need to open the original again. Map structure first (list every heading before writing); preserve the source's own section order and headings; reproduce all numbered steps, frameworks, checklists, and tables in full — do not compress; capture every named concept, term, tool, company, person, warning, and emphasis. If the source has 6 steps, write all 6.

**Before saving, run the gate — do not save until it passes:**

- The **Done Conditions** checklist in `30_Order/Standards/Source Summary Standard.md`.
- The 16-point quality gate in `60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md` Part 12.

These live in their source files on purpose — run them there, do not copy them here.

---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - ocr
  - document-parsing
source_url: https://github.com/rednote-hilab/dots.ocr
notes:
  - "[[40_Resources/CS/Repos]]"
---
# dots.ocr (now dots.mocr)

**GitHub:** [rednote-hilab/dots.ocr](https://github.com/rednote-hilab/dots.ocr) | **Stars:** 9k | **Updated:** Mar 2026

## What it is
3B VLM from RedNote (Xiaohongshu) that parses multilingual document layouts — text, tables (HTML), formulas (LaTeX), charts (SVG) — from PDFs and images into structured JSON + Markdown. Rebranded as [dots.mocr](https://github.com/rednote-hilab/dots.mocr) in March 2026.

## How Anant uses it
**Verdict: Not worth integrating into Jarvis — Claude already handles this.** The `/ingest-clipping` pipeline sends PDFs and images to Claude directly via MCP, which handles OCR and layout parsing adequately. dots.ocr adds value if: (a) you're processing sensitive documents you don't want to send to Anthropic, or (b) you need batch offline PDF parsing at scale. For a student knowledge vault, neither applies. The overhead of running a vLLM server for a 3B model isn't worth it when Claude is already doing the work.

Better alternative for Jarvis PDF ingestion: keep using Claude vision natively.

## How to install / run it (Windows)
Primary path is Docker or Linux vLLM — not Windows-native:
```bash
# Linux/WSL2
conda create -n dots_mocr python=3.12
git clone https://github.com/rednote-hilab/dots.mocr.git
cd dots.mocr && pip install -e .
# Requires CUDA + flash-attn
# Docker: docker pull rednotehilab/dots.ocr
```
Requires a GPU with adequate VRAM for a 3B VLM. No native Windows binary. WSL2 with CUDA passthrough would work.

## Caveats / current state
- Active: last commit Mar 2026, integrated into vLLM v0.11.0 officially
- MIT license — no commercial restrictions
- Beats most specialized OCR models on olmOCR-bench and OmniDocBench benchmarks
- **Fits into /ingest-clipping?** No — it's a standalone inference server, not an Obsidian plugin. You'd have to build a wrapper script to call its API and feed results into the vault. Not worth building when Claude does the same thing in the existing pipeline.
- Complex tables and formulas still have known weaknesses at 3B scale

## Connects to
[[40_Resources/CS/Repos]]

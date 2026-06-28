---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - learning
source_url: https://github.com/DataTalksClub/llm-zoomcamp
notes:
  - "[[40_Resources/CS/Repos]]"
---
# LLM Zoomcamp

**GitHub:** [DataTalksClub/llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | **Stars:** 6.6k | **Updated:** June 2026

## What it is
A 10-week free course (DataTalksClub) that builds a production-ready RAG application from scratch: agentic RAG with function calling → vector search with embeddings and PGVector → orchestration with Kestra → offline/online evaluation (LLM-as-judge) → monitoring dashboards → hybrid search and reranking → end-to-end capstone project. All code is Jupyter notebooks in Python.

## How Anant uses it
- **Start with Module 1 (Agentic RAG)** to build a working retrieval pipeline over the Jarvis vault — this is the most direct application: keyword search → function-calling agent → grounded answers. This module alone would meaningfully improve Jarvis query quality.
- **Module 2 (Vector Search)** is the next step: add semantic search with embeddings and PGVector so Jarvis can find notes by meaning, not just keyword match. Run this after Module 1 is working.
- **Module 4 (Evaluation)** gives concrete metrics for measuring how well Jarvis retrieves relevant notes. Run it when the first RAG pipeline is built to know whether changes actually help.
- Modules 5 (monitoring) and 6 (hybrid search/reranking) apply once the basic pipeline is stable. The capstone project can be a Jarvis Q&A bot over the vault.

## How to install / run it (Windows)
2026 live cohort started June 8 and is **active now**. Sign up at airtable.com/appPPxkgYLH06Mvbw/shr7WtxHEPXxaui0Q for graded homework and certificate eligibility. Self-paced is always available at the GitHub repo + YouTube playlist. Costs ~$1–5 in API credits to run exercises; no GPU needed.

## Caveats / current state
The 2026 cohort is live as of this note (June 28 2026). Module 1 content is fully available. The course has run since 2024 and the 2026 edition has updated the first module to cover agentic RAG (previously this was Module 1 focused on basic RAG). Prerequisites: Python, command line basics, Docker familiarity.

## Connects to
[[40_Resources/CS/Repos]]

---
title: "VectifyAI/PageIndex: 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG"
source: "https://github.com/VectifyAI/PageIndex?utm_source=sp_auto_dm&utm_referrer=sp_auto_dm&fbclid=PAVERFWAQ5O_VleHRuA2FlbQIxMABzcnRjBmFwcF9pZA8xMjQwMjQ1NzQyODc0MTQAAae3ZLaKSi3wejVX2JSdc84Wh4hENLEbaCAFX4zyDBT6m3om2G66hthvu1_Zog_aem_9T-4Jo0RkUBV-Td5LsHn3g"
author:
  - "[[VectifyAI]]"
published:
created: 2026-04-10
description: "📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG - VectifyAI/PageIndex"
tags:
  - "clippings"
---
## 📢 Updates

- 🔥 [**Agentic Vectorless RAG**](https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py) — A simple *agentic, vectorless RAG* [example](https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py) with self-hosted PageIndex, using OpenAI Agents SDK.
- [PageIndex Chat](https://chat.pageindex.ai/) — Human-like document analysis agent [platform](https://chat.pageindex.ai/) for professional long documents. Also available via [MCP](https://pageindex.ai/developer) or [API](https://pageindex.ai/developer).
- [PageIndex Framework](https://pageindex.ai/blog/pageindex-intro) — Deep dive into PageIndex: an *agentic, in-context tree index* that enables LLMs to perform *reasoning-based, human-like retrieval* over long documents.

---

## 📑 Introduction to PageIndex

Are you frustrated with vector database retrieval accuracy for long professional documents? Traditional vector-based RAG relies on semantic *similarity* rather than true *relevance*. But **similarity ≠ relevance** — what we truly need in retrieval is **relevance**, and that requires **reasoning**. When working with professional documents that demand domain expertise and multi-step reasoning, similarity search often falls short.

Inspired by AlphaGo, we propose **[PageIndex](https://vectify.ai/pageindex)** — a **vectorless**, **reasoning-based RAG** system that builds a **hierarchical tree index** from long documents and uses LLMs to **reason** *over that index* for **agentic, context-aware retrieval**. It simulates how *human experts* navigate and extract knowledge from complex documents through *tree search*, enabling LLMs to *think* and *reason* their way to the most relevant document sections. PageIndex performs retrieval in two steps:

1. Generate a “Table-of-Contents” **tree structure index** of documents
2. Perform reasoning-based retrieval through **tree search**

[![](https://camo.githubusercontent.com/e9c3f93a4039fa4743b0655dc7a08eddd0eeb24ed1bfddfb03b6a0bf3c87cbdc/68747470733a2f2f646f63732e70616765696e6465782e61692f696d616765732f636f6f6b626f6f6b2f766563746f726c6573732d7261672e706e67)](https://pageindex.ai/blog/pageindex-intro "The PageIndex Framework")

### 🎯 Core Features

Compared to traditional vector-based RAG, **PageIndex** features:

- **No Vector DB**: Uses document structure and LLM reasoning for retrieval, instead of vector similarity search.
- **No Chunking**: Documents are organized into natural sections, not artificial chunks.
- **Human-like Retrieval**: Simulates how human experts navigate and extract knowledge from complex documents.
- **Better Explainability and Traceability**: Retrieval is based on reasoning — traceable and interpretable, with page and section references. No more opaque, approximate vector search (“vibe retrieval”).

PageIndex powers a reasoning-based RAG system that achieved **state-of-the-art** [98.7% accuracy](https://github.com/VectifyAI/Mafin2.5-FinanceBench) on FinanceBench, demonstrating superior performance over vector-based RAG solutions in professional document analysis. See our [blog post](https://vectify.ai/blog/Mafin2.5) for details.

### 📍 Explore PageIndex

To learn more, please see a detailed introduction to the [PageIndex framework](https://pageindex.ai/blog/pageindex-intro). Check out this GitHub repo for open-source code, and the [cookbooks](https://docs.pageindex.ai/cookbook), [tutorials](https://docs.pageindex.ai/tutorials), and [blog](https://pageindex.ai/blog) for additional usage guides and examples.

The PageIndex service is available as a ChatGPT-style [chat platform](https://chat.pageindex.ai/), or can be integrated via [MCP](https://pageindex.ai/developer) or [API](https://pageindex.ai/developer).

### 🛠️ Deployment Options

- Self-host — run locally with this open-source repo.
- Cloud Service — try instantly with our [Chat Platform](https://chat.pageindex.ai/), or integrate via [MCP](https://pageindex.ai/developer) or [API](https://pageindex.ai/developer).
- *Enterprise* — private or on-prem deployment. [Contact us](https://ii2abc2jejf.typeform.com/to/tK3AXl8T) or [book a demo](https://calendly.com/pageindex/meet) for more details.

### 🧪 Quick Hands-on

- 🔥 [**Agentic Vectorless RAG**](https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py) (**latest**) — a simple but complete **agentic vectorless RAG** [example](https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py) with *self-hosted* PageIndex, using OpenAI Agents SDK.
- Try the [Vectorless RAG](https://github.com/VectifyAI/PageIndex/blob/main/cookbook/pageindex_RAG_simple.ipynb) notebook — a *minimal*, hands-on example of reasoning-based RAG using PageIndex.
- Check out [Vision-based Vectorless RAG](https://github.com/VectifyAI/PageIndex/blob/main/cookbook/vision_RAG_pageindex.ipynb) — no OCR; a minimal, vision-based & reasoning-native RAG pipeline that works directly over page images.

---

## 🌲 PageIndex Tree Structure

PageIndex can transform lengthy PDF documents into a semantic **tree structure**, similar to a *"table of contents"* but optimized for use with Large Language Models (LLMs). It's ideal for: financial reports, regulatory filings, academic textbooks, legal or technical manuals, and any document that exceeds LLM context limits.

Below is an example PageIndex tree structure. Also see more example [documents](https://github.com/VectifyAI/PageIndex/tree/main/examples/documents) and generated [tree structures](https://github.com/VectifyAI/PageIndex/tree/main/examples/documents/results).

```
...
{
  "title": "Financial Stability",
  "node_id": "0006",
  "start_index": 21,
  "end_index": 22,
  "summary": "The Federal Reserve ...",
  "nodes": [
    {
      "title": "Monitoring Financial Vulnerabilities",
      "node_id": "0007",
      "start_index": 22,
      "end_index": 28,
      "summary": "The Federal Reserve's monitoring ..."
    },
    {
      "title": "Domestic and International Cooperation and Coordination",
      "node_id": "0008",
      "start_index": 28,
      "end_index": 31,
      "summary": "In 2023, the Federal Reserve collaborated ..."
    }
  ]
}
...
```

You can generate the PageIndex tree structure with this open-source repo, or use our [API](https://pageindex.ai/developer).

---

## ⚙️ Package Usage

You can follow these steps to generate a PageIndex tree from a PDF document.

### 1\. Install dependencies

```
pip3 install --upgrade -r requirements.txt
```

### 2\. Set your LLM API key

Create a `.env` file in the root directory with your LLM API key, with multi-LLM support via [LiteLLM](https://docs.litellm.ai/docs/providers):

```
OPENAI_API_KEY=your_openai_key_here
```

### 3\. Generate PageIndex structure for your PDF

```
python3 run_pageindex.py --pdf_path /path/to/your/document.pdf
```
Optional parameters  
You can customize the processing with additional optional arguments:

```
--model                 LLM model to use (default: gpt-4o-2024-11-20)
--toc-check-pages       Pages to check for table of contents (default: 20)
--max-pages-per-node    Max pages per node (default: 10)
--max-tokens-per-node   Max tokens per node (default: 20000)
--if-add-node-id        Add node ID (yes/no, default: yes)
--if-add-node-summary   Add node summary (yes/no, default: yes)
--if-add-doc-description Add doc description (yes/no, default: yes)
```

Markdown support  
We also provide markdown support for PageIndex. You can use the \`--md\_path\` flag to generate a tree structure for a markdown file.
```
python3 run_pageindex.py --md_path /path/to/your/document.md
```

> Note: in this mode, we use "#" to determine node headings and their levels. For example, "##" is level 2, "###" is level 3, etc. Make sure your markdown file is formatted correctly. If your Markdown file was converted from a PDF or HTML, we don't recommend using this mode, since most existing conversion tools cannot preserve the original hierarchy. Instead, use our [PageIndex OCR](https://pageindex.ai/blog/ocr), which is designed to preserve the original hierarchy, to convert the PDF to a markdown file and then use this mode.

## Agentic Vectorless RAG: An Example

For a simple, end-to-end ***agentic vectorless RAG*** example using PageIndex with OpenAI Agents SDK, see [`examples/agentic_vectorless_rag_demo.py`](https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py).

```
# Install optional dependency
pip3 install openai-agents

# Run the demo
python3 examples/agentic_vectorless_rag_demo.py
```

---

## 📈 Case Study: PageIndex Leads Finance QA Benchmark

[Mafin 2.5](https://vectify.ai/mafin) is a reasoning-based RAG system for financial document analysis, powered by **PageIndex**. It achieved a state-of-the-art [**98.7% accuracy**](https://vectify.ai/blog/Mafin2.5) on the [FinanceBench](https://arxiv.org/abs/2311.11944) benchmark, significantly outperforming traditional vector-based RAG systems.

PageIndex's hierarchical indexing and reasoning-driven retrieval enable precise navigation and extraction of relevant context from complex financial reports, such as SEC filings and earnings disclosures.

Explore the full [benchmark results](https://github.com/VectifyAI/Mafin2.5-FinanceBench) and our [blog post](https://vectify.ai/blog/Mafin2.5) for detailed comparisons and performance metrics.

[![](https://private-user-images.githubusercontent.com/8255061/440120069-571aa074-d803-43c7-80c4-a04254b782a3.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzU4MDIyMzMsIm5iZiI6MTc3NTgwMTkzMywicGF0aCI6Ii84MjU1MDYxLzQ0MDEyMDA2OS01NzFhYTA3NC1kODAzLTQzYzctODBjNC1hMDQyNTRiNzgyYTMucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTBUMDYxODUzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NmI2ZDYyZmE4ZmI0MTcwZTI4MmEzZTNkZDc3ZDA4ZTU3MjI2NDcxMWYyNWQ4MzA3NDJkMGQxMmUxNzhhN2Q0NSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.GnODD0ishTvHP42O2i7YbvxPS6tDXz1fqN_sd2LoN0M)](https://github.com/VectifyAI/Mafin2.5-FinanceBench)

---

## 🧭 Resources

- 📝 [Blog](https://pageindex.ai/blog): technical articles, research insights, and product updates.
- 🔧 [Developer](https://pageindex.ai/developer): MCP setup, API docs, and integration guides.
- 🧪 [Cookbooks](https://docs.pageindex.ai/cookbook): hands-on, runnable examples and advanced use cases.
- 📖 [Tutorials](https://docs.pageindex.ai/tutorials): practical guides and strategies, including *Document Search* and *Tree Search*.

---

## ⭐ Support Us

Leave us a star 🌟 if you like our project. Thank you!

[![](https://private-user-images.githubusercontent.com/13518252/481667856-eae4ff38-48ae-4a7c-b19f-eab81201d794.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzU4MDIyMzMsIm5iZiI6MTc3NTgwMTkzMywicGF0aCI6Ii8xMzUxODI1Mi80ODE2Njc4NTYtZWFlNGZmMzgtNDhhZS00YTdjLWIxOWYtZWFiODEyMDFkNzk0LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MTAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDEwVDA2MTg1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTlmYzMwMTU1M2YyZjMxZTgwZDUwOTcxMjI3YWJhNDAwOTYyYzU3ZTlhOGY5Y2UwZGQ4YThmNGNlZjA5NmI2ZmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.IqLuVrYov57QpMMAG8CM3XnfKKXlTsY5wFnphl0sJII)](https://private-user-images.githubusercontent.com/13518252/481667856-eae4ff38-48ae-4a7c-b19f-eab81201d794.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzU4MDIyMzMsIm5iZiI6MTc3NTgwMTkzMywicGF0aCI6Ii8xMzUxODI1Mi80ODE2Njc4NTYtZWFlNGZmMzgtNDhhZS00YTdjLWIxOWYtZWFiODEyMDFkNzk0LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MTAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDEwVDA2MTg1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTlmYzMwMTU1M2YyZjMxZTgwZDUwOTcxMjI3YWJhNDAwOTYyYzU3ZTlhOGY5Y2UwZGQ4YThmNGNlZjA5NmI2ZmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.IqLuVrYov57QpMMAG8CM3XnfKKXlTsY5wFnphl0sJII)

Please cite this work as:

```
Mingtian Zhang, Yu Tang and PageIndex Team,
"PageIndex: Next-Generation Vectorless, Reasoning-based RAG",
PageIndex Blog, Sep 2025.
```

Or use the BibTeX citation.
```
@article{zhang2025pageindex,
  author = {Mingtian Zhang and Yu Tang and PageIndex Team},
  title = {PageIndex: Next-Generation Vectorless, Reasoning-based RAG},
  journal = {PageIndex Blog},
  year = {2025},
  month = {September},
  note = {https://pageindex.ai/blog/pageindex-intro},
}
```
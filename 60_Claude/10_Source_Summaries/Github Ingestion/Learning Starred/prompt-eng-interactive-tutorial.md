---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - learning
source_url: https://github.com/anthropics/prompt-eng-interactive-tutorial
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Anthropic Prompt Engineering Interactive Tutorial

**GitHub:** [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | **Stars:** 36.7k | **Updated:** April 2024

## What it is
Anthropic's official 9-chapter interactive course on prompt engineering for Claude, delivered as Jupyter notebooks. Chapters progress from basic prompt structure → clear and direct instructions → assigning roles → separating data from instructions → formatting and speaking for Claude → thinking step by step → using examples → avoiding hallucinations → building complex prompts for industry use cases. Appendix covers chaining prompts, tool use, and search/retrieval. Two variants: Anthropic 1P (direct API) and Amazon Bedrock.

## How Anant uses it
- **Chapter 6 (Thinking Step by Step)** before writing any multi-step agent prompt — particularly for Kronos's analysis chain or Jarvis reasoning chains. This chapter pins down the mechanism for forcing structured intermediate reasoning.
- **Chapter 8 (Avoiding Hallucinations)** applies directly to Jarvis responses that cite vault notes: the grounding techniques here prevent the assistant from confabulating note content.
- **Chapter 9 (Complex Prompts)** + the Appendix (Tool Use) are the foundation for all Claude Code hook prompts, skill files, and agent prompts used in Jarvis. Read these before writing any new skill.
- Chapters 1–5 are worth skimming if you haven't read them — they cover the rules that make prompts fail silently (wrong delimiters, unclear scope, no role assignment).

## How to install / run it (Windows)
Two options: (1) Clone the repo and run Jupyter notebooks locally with your Anthropic API key. (2) Use the Google Sheets version (linked in README) — no setup required, exercises run directly in Sheets via the Claude for Sheets extension. The Sheets version is easier for just reading without running code.

## Caveats / current state
Last updated April 2024. Uses Claude 3 Haiku in the notebooks — the underlying API calls use the older messages format that still works but the model names are outdated. The concepts are stable and fully applicable to Claude Sonnet 4.x. The tool use appendix covers function calling but predates the MCP era. For MCP-specific patterns, use the AI Dev Tools Zoomcamp Module 3 instead.

## Connects to
[[40_Resources/CS/Repos]]

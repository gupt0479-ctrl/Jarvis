---
type: input
status: sprout
created: 2026-06-28
tags:
  - github
  - ingestion
  - ai-tools
  - recruiting
source_url: https://github.com/interviewstreet/hiring-agent
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Hiring Agent

**GitHub:** [interviewstreet/hiring-agent](https://github.com/interviewstreet/hiring-agent) | **Stars:** 3k | **Updated:** Jun 22, 2026

## What it is
HackerRank's open-source resume-to-score pipeline for companies doing hiring: it takes a candidate's PDF resume, converts it to Markdown, extracts structured sections (basics, work, education, skills, projects, awards) via LLM (Gemini or local Ollama), enriches with GitHub profile signals, and outputs a scored evaluation across four categories — open_source contributions, self_projects, production experience, and technical_skills.

## How Anant uses it
**This tool is built for hiring teams, not job seekers.** Anant is a candidate, not a recruiter. Direct use (running it on his own resume to "see how he scores") is limited — the tool outputs a score against internal criteria, not actionable resume edits.

That said, there is one specific use: **reading the scoring templates** at `prompts/templates/` reveals exactly what automated screeners weight. The `resume_evaluation_criteria.jinja` file encodes:
- `open_source`: GitHub contributions to external repos, not just personal projects
- `self_projects`: evidence of projects shipped and functional, not just listed
- `production`: work experience with real users/scale
- `technical_skills`: breadth of languages/frameworks with depth evidence

This tells Anant concretely what to strengthen on his GitHub profile and resume before Fall 2026 recruiting — specifically, contributing to at least one external open-source repo, and framing project bullets around production evidence rather than just implementation.

If Anant wants to actually run it: it requires Python 3.11 and either a Gemini API key or a local Ollama install, then `python score.py /path/to/resume.pdf`.

## How to install / run it (Windows)
```
git clone https://github.com/interviewstreet/hiring-agent
cd hiring-agent
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # fill in GEMINI_API_KEY or set LLM_PROVIDER=ollama
python score.py C:\path\to\resume.pdf
```
Requires Python 3.11. Gemini API key is free tier at aistudio.google.com.

## Caveats / current state
- Actively maintained — commit Jun 22, 2026 — but core logic hasn't changed significantly since October 2025 (most recent commits are bug fixes).
- The scoring criteria are HackerRank's internal heuristics, not a universal standard. Different companies weight categories differently.
- GitHub enrichment (`github.py`) fetches your public repos; a thin GitHub profile will reduce scores regardless of actual skill.
- The evaluation is designed to be used on batches of candidates, not as a self-improvement tool — the absolute score number is less meaningful than reading the criteria templates.
- **Bottom line:** Borderline useful for Anant. The main value is reading the Jinja templates to understand what ATS/LLM-based screeners look for, not running the tool itself.

## Connects to
[[40_Resources/CS/Repos]]

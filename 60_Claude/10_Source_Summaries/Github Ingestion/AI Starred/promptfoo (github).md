---
type: input
status: sprout
created: 2026-06-21
updated: 2026-06-21
tags:
  - summary
  - github
notes:
  - "[[40_Resources/CS/Repos]]"
input_kind: github
track: ai
source_url: https://github.com/promptfoo/promptfoo
---
# promptfoo

**Repo:** `https://github.com/promptfoo/promptfoo`
**Stars:** 22,404 | **Forks:** 2,000 | **Language:** TypeScript | **License:** MIT | **Last push:** 2026-06-20 (actively maintained)

> [!NOTE]
> **Promptfoo is now part of OpenAI**, per the README's own banner — it remains open source and MIT licensed, but is no longer an independent company. Existing vault notes (`Repos-Deep-Analysis.md`) predate this and don't mention the acquisition.

## What It Is

A CLI and library for evaluating and red-teaming LLM applications: automated prompt/model evals plus red-teaming and vulnerability scanning, used internally by both OpenAI and Anthropic.

## Core Capabilities

- Automated evaluations: write test cases with expected outputs, run them, get pass/fail with diffs
- Red teaming: generates adversarial prompts to find jailbreaks and hallucination patterns
- Side-by-side model comparison (OpenAI, Anthropic, Azure, Bedrock, Ollama, and more)
- CI/CD integration for automated checks on every change
- Code scanning for LLM-related security/compliance issues in pull requests
- Installable via npm, brew, or pip; runnable ad hoc via `npx promptfoo@latest`

## Why It Matters

This vault's `ingesting-clipping` skill and the agents built on top of it are themselves prompt-engineered systems with no regression test suite — promptfoo is the standard tool for catching exactly the kind of silent drift that happens when a skill file gets edited (like this session's patches) without anything verifying behavior didn't regress.

## Use Cases for Jarvis

- Write a promptfoo test suite against `CLAUDE.md` and the core skills (`ingesting-clipping`, `ops`) to catch regressions when they're edited.
- Red-team the portfolio's planned AI Lab feature before a recruiter does — test for prompt injection on a public-facing LLM interface.
- For BOOM: write test cases for the alert-processing pipeline's edge-case inputs the same way promptfoo tests agent behavior — structured input, expected output.

## Tradeoffs

- Requires Node.js ^20.20.0 or >=22.22.0 for the npm/npx path — an extra runtime dependency if not already using Node for anything else in a given project.
- Testing/red-teaming infrastructure is overhead best added once a skill or prompt is stable, not while it's still actively changing shape — premature for skills still being iterated on.

## Related

- [[40_Resources/CS/Repos]] (AI section, also listed under Cybersecurity)

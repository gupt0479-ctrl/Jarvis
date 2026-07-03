---
type: project
status: sprout
created: 2026-07-01
tags: [causalops, claude-code, tokens, efficiency]
---

# Token Efficiency — Running Claude Code on CausalOps

## Why Token Efficiency Matters Here

- Sonnet 4.6 hard mode uses extended thinking, which consumes more tokens per turn.
- The memory layer prompt references vault notes (not inline spec) — this is intentional to avoid re-encoding 2000 lines of spec into each prompt.
- The weekly limit is shared across all projects.

## Principles Applied to the Memory Layer Prompt

| Principle | How Applied |
|-----------|-------------|
| Reference don't inline | Prompt points to vault notes; Claude Code reads them at start |
| Ordered steps with testable checkpoints | Prevents backtracking and re-reading |
| Hard rules stated once upfront | Avoids repeated constraint reminders mid-session |
| "Do NOT run integration tests" explicit | Prevents live API calls that consume external quota |
| Minimal preamble | Prompt starts with task, not background |

## General Rules for CausalOps Prompts

1. **Always reference vault notes by path** — don't paste spec inline. The vault is ~12,000 words of spec. Inlining it in every prompt is wasteful.

2. **State constraint changes at the top** — before implementation order. This prevents Claude from starting down the wrong path and having to backtrack.

3. **Hard rules in a named block** — "HARD RULES: never X" is clearer than prose paragraphs. Claude Code applies them consistently.

4. **Implementation order = numbered list** — not a paragraph. Numbered steps mean Claude Code can resume if the session is interrupted without re-deriving the plan.

5. **Keep the `/demo/estimate` smoke test as the zero-token sanity check** — it verifies the base pipeline works without consuming any LLM tokens.

## Token Budget Estimate by Task

| Task | Estimated Output Tokens | Notes |
|------|------------------------|-------|
| Memory layer full implementation | 80-120k | Includes 5 new files, 5 modified, 2 test files |
| Adding tests only | 20-30k | test_extractor + test_mcp_tools unit tests |
| Schema migration SQL verification | 2-5k | Just read/verify, no code generation |
| docker-compose.yml update only | 3-5k | Single file edit |
| graphify run (automated) | 15-30k | LLM semantic extraction subagents |

## Running Sonnet 4.6 Hard Mode Efficiently

- Hard mode (extended thinking) is best for architecture decisions, not boilerplate.
- Use hard mode for: graph topology changes, test strategy design, store.py write() logic.
- Use regular mode (no hard mode) for: `__init__.py`, `.mcp.json`, requirements.txt edits, `docker-compose.yml`.
- If a session stalls on a decision (e.g., "should I use upsert or insert?"), the answer is already in the vault notes — reference the plan, don't re-derive.

## Prompts Already Written in This Folder

- [[Memory Layer Implementation Prompt]] — full implementation prompt, ready to paste

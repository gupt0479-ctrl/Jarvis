---
name: llm-council
description: Runs a high-stakes, genuinely uncertain decision through 5 independent advisor personas, has them peer-review each other's anonymized answers, then synthesizes a chairman verdict — chat-only output, no files.
---
# llm-council

**Usage:** `/llm-council "the decision or question"` — only for genuine tradeoffs with real stakes, never for routine tasks.

---

## Why This Exists

Built per [[Claude Council — Path A Prompt (web)]] and [[60_Claude/10_Source_Summaries/Github Ingestion/Claude Starred/LLM Council skills|LLM Council skills]] (adapting Andrej Karpathy's `llm-council` methodology, via aiwithremy/claude-skills-llm-council), resolved in [[00_Execution]] as a same-day install, not just a recorded plan. **Correction carried forward from the source ingestion:** the landing page's "Path B saves an HTML report to your workspace" claim is false — the real `SKILL.md` forbids file output entirely. This skill follows the real mechanism, chat-only.

## When To Trigger

**Mandatory:** "council this," "run the council," "war room this," "pressure-test this," "stress-test this," "debate this."
**Strong (only paired with a real tradeoff):** "should I X or Y," "which option," "I can't decide."
**Never trigger on:** simple yes/no questions, factual lookups, routine coding tasks, or a "should I" question with no real stakes (e.g. "should I use markdown"). If the question doesn't have genuine uncertainty and real stakes, say so and answer directly instead of running the council — the overhead is only worth it for decisions that are hard to reverse.

## Instructions

### Step 1 — Frame With Context Enrichment

Before framing the question, spend up to ~30 seconds scanning the workspace for the 2-3 files that would turn generic advice into grounded advice: `CLAUDE.md`, any `memory/` folder, recently attached files or files named in the prompt, and — for this vault specifically — the relevant `10_Areas/`, `20_Progress/`, or session-log context. Use Glob/Grep/Read, not a full vault scan.

Write one neutral, framed version of the question covering: the decision, the real context, and what's actually at stake. Ask exactly one clarifying question if the prompt is too vague to frame — never more than one.

### Step 2 — Convene 5 Advisors in Parallel

Spawn all 5 advisor personas as parallel Agent tool calls in a single message — never sequentially, since an earlier answer would bias a later one. Each advisor gets: its identity below, the framed question, and an instruction to lean fully into its angle in 150-300 words, no hedging, no preamble.

**Default personas, customized for this vault's actual domains** (per the source ingestion's own decision to replace Karpathy's generic five with domain-specific ones):

1. **Trading Analyst** — thinks in edge, risk, and market structure; distrusts a plan that hasn't been walk-forward validated.
2. **CS Theorist** — thinks in correctness, complexity, and first principles; distrusts a plan that skips the proof for the sake of speed.
3. **Systems Engineer** — thinks in failure modes, blast radius, and operational cost; distrusts a plan with no rollback path.
4. **ML Practitioner** — thinks in data quality, eval rigor, and what actually ships; distrusts a plan with no eval story.
5. **Pragmatic Builder** — thinks in time-to-value and scope discipline; distrusts a plan that's over-engineered for the actual stakes.

These five are chosen to create deliberate tensions (rigor vs. speed, proof vs. shipping, caution vs. momentum) — don't let any of them converge into agreement just to be polite.

### Step 3 — Peer Review, Also 5 Parallel Calls

Anonymize the 5 responses as A-E with a **randomized** letter mapping (not alphabetical by persona order — this defeats positional bias). Spawn 5 more parallel Agent calls, each reviewing the other four's anonymized answers (never its own) and answering exactly three fixed questions:
1. Which response is strongest, and why?
2. Which response has the biggest blind spot?
3. What did all five miss?

### Step 4 — Chairman Synthesis

One final pass receives: the framed question, all 5 de-anonymized responses, and all 5 peer reviews. Produce exactly five sections:
1. **Where the Council Agrees**
2. **Where the Council Clashes**
3. **Blind Spots the Council Caught**
4. **The Recommendation**
5. **The One Thing to Do First**

The chairman may side with a single dissenting advisor over a 4-1 majority if that advisor's reasoning is genuinely stronger — don't default to majority vote as a shortcut.

### Step 5 — Present in Chat Only

**Do NOT generate an HTML report or any files.** Present the full synthesis directly in the conversation. This is a hard rule, not a preference — it's the exact point where the source landing page's claim diverges from the real skill.

### Step 6 — Transcript Saving (Optional, On Request Only)

Only if the user asks, or the question was significant enough to warrant a durable record: write a transcript to `60_Claude/00_Inbox/council-transcript-[timestamp].md` — Jarvis's actual inbox convention, not a generic `active/` folder. Otherwise, nothing gets written.

## Operating Notes

- Always spawn all 5 advisors in parallel, never sequentially — sequential spawning lets earlier answers bias later ones.
- Always anonymize before peer review — named advisors get deferred to on identity, not evaluated on the merit of the argument.
- The chairman can and should override a majority when the minority reasoning is stronger.
- Don't run trivial questions through this — if there's no genuine tradeoff, answer directly and say why the council wasn't warranted.

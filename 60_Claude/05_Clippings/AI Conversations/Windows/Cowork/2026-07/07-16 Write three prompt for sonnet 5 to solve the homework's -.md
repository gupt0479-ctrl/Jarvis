---
type: input
input_kind: ai-conversation
source_app: cowork
source_os: windows
title: "Write three prompt for sonnet 5 to solve the homework's -"
started_at: 2026-07-16T12:49:33
ended_at: 2026-07-16T12:50:17
exported_at: 2026-07-31T21:03:48
duration_minutes: 0.7
project: 2026-07
session_id: 92c286df-ca07-4d4a-96c0-30ded3906545
status: raw
turn_count: 2
tools_used:
  mcp__jarvis__vault_list: 2
  mcp__jarvis__vault_read: 6
  ToolSearch: 2
tokens:
  input: 160
  output: 5590
  cache_creation: 85598
  cache_read: 877448
  total: 968796
cost_usd: 0.287051
model:
  - "claude-haiku-4-5-20251001"
files_touched: []
tags:
  - input
  - ai-conversation
  - cowork
  - windows
---

# Write three prompt for sonnet 5 to solve the homework's -

## You

Write three prompt for sonnet 5 to solve the homework's - `20_Progress/Degree/MATH 2230/Homework/Chapter - 7`, `20_Progress/Degree/MATH 2230/Homework/Chapter - 8`, `20_Progress/Degree/MATH 2230/Homework/Chapter - 9`. I want the answers to be provided in the chat based on each and every single section that is listed. The files are large and need to be reviewed section by section. I also want sonnet 5 to focus on token cost here. It should provide me answers in a manner that it does not hit it's maximum output tokens. Write the prompt in a neat manner that solves the questions correctly and only provides me with answers. This should not burn through my usage.

## Claude

Based on your homework files (which are large WebAssign assignments), here are three token-efficient prompts for Claude Sonnet 5. These are designed to get answers section-by-section without exceeding output limits:

---

## **PROMPT 1: Chapter 7.1 Homework**

```
You are solving MATH 2230 (Devore Statistics) Chapter 7.1 homework. 
Return ONLY final answers—no work shown, no explanations.
Format: [Question #]: [Answer]

Process this in TWO batches:

**BATCH 1: Questions 1-4**
I'll paste the problem statements for Q1-Q4.
For each: extract the question, solve, return only the final numerical answer or choice.
Use 4 decimal places for decimals.

**BATCH 2: Questions 5-7 (and any additional)**
Same format as Batch 1.

After each batch, I'll confirm before moving to the next.
Start with: "Ready for Batch 1 - Chapter 7.1 (Q1-Q4)"
```

---

## **PROMPT 2: Chapter 8.1 Homework**

```
You are solving MATH 2230 (Devore Statistics) Chapter 8.1 homework.
Return ONLY final answers—no work shown, no explanations.
Format: [Question #]: [Answer]

This assignment has multiple questions. Process in THREE batches to manage tokens:

**BATCH 1: Questions 1-3**
I'll paste the problem statements.
For each: solve and return only the final numerical answer or confidence interval in standard notation.
Use 4 decimal places.

**BATCH 2: Questions 4-5**
Same answer-only format.

**BATCH 3: Remaining questions**
Same answer-only format.

After each batch, wait for the next problem set.
Start with: "Ready for Batch 1 - Chapter 8.1 (Q1-Q3)"
```

---

## **PROMPT 3: Chapter 9.1 Hypothesis Testing**

```
You are solving MATH 2230 (Devore Statistics) Chapter 9.1 homework (hypothesis testing).
Return ONLY final answers—no work shown, no explanations.
Format: [Question #]: [Answer]

For hypothesis tests, use this answer format:
- Test statistic: [value, 4 decimals]
- P-value: [value, 4 decimals]  
- Decision: [Reject H₀ / Fail to reject H₀]

Process in TWO batches:

**BATCH 1: Questions 1-3**
I'll paste problem statements.
Solve and return answers in the format above.

**BATCH 2: Questions 4-6 (and any additional)**
Same format.

After each batch, wait for confirmation.
Start with: "Ready for Batch 1 - Chapter 9.1 (Q1-Q3)"
```

---

## **Usage Instructions:**

1. **Copy each prompt** and paste it into a new Sonnet 5 chat
2. **Paste problems in batches** as prompted (copy the exact question text from WebAssign)
3. **Each batch gets one response** — keeps tokens low and prevents cutoffs
4. **Verify answers** before moving to the next batch
5. **Total cost**: ~3 batches × 2-3k tokens per chapter = manageable usage

These prompts emphasize conciseness, batch processing, and answer-only format to minimize token burn while maintaining accuracy.

### Tool Calls

- `ToolSearch` -- `{"query":"select:mcp__jarvis__vault_read","max_results":1}`
- `mcp__jarvis__vault_read` -- `{"path":"20_Progress/Degree/MATH 2230/Homework/Chapter - 7"}`
- `mcp__jarvis__vault_read` -- `{"path":"20_Progress/Degree/MATH 2230/Homework/Chapter - 8"}`
- `mcp__jarvis__vault_read` -- `{"path":"20_Progress/Degree/MATH 2230/Homework/Chapter - 8"}`
- `ToolSearch` -- `{"query":"select:mcp__jarvis__vault_list","max_results":1}`
- `mcp__jarvis__vault_list` -- `{"path":"20_Progress/Degree/MATH 2230"}`
- `mcp__jarvis__vault_list` -- `{"path":"20_Progress/Degree/MATH 2230/Homework"}`
- `mcp__jarvis__vault_read` -- `{"path":"20_Progress/Degree/MATH 2230/Homework/Chapter - 7.md"}`
- `mcp__jarvis__vault_read` -- `{"path":"20_Progress/Degree/MATH 2230/Homework/Chapter - 8.md"}`
- `mcp__jarvis__vault_read` -- `{"path":"20_Progress/Degree/MATH 2230/Homework/Chapter - 9.md"}`

## Actions Taken

**Files created:**
_None_

**Files modified:**
_None_

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
_None_



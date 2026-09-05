# closeday — reference

Loaded on demand from SKILL.md. Contents:
1. Scorecard template + scoring rules
2. Session log entry format

## §1 Scorecard template

Append to `10_Areas/Life/Enumerate/Daily/YYYY-MM-DD.md`, below the Morning Plan:

```markdown
## End of Day

### Summer Ops Scorecard

| Track     | Minimum  | Met?       |
|-----------|----------|------------|
| LeetCode  | ≥5       | [ ] count: |
| CSCI 4041 | 25-45 min| [ ]        |
| CSCI 2033 | 30-45 min| [ ]        |
| MATH 2230 | board    | [ ]        |
| HIST 1103 | step/N/A | [ ]        |
| 4 Wins    | 4/4      | [ ]        |

**Day Status: GREEN** (or **RED**)

> GREEN = ≥90% rows met AND LeetCode ≥5. Everything else = RED.
> HIST 1103 counts as met if nothing was due within 7 days (mark N/A).

### What Actually Happened

[2-3 honest sentences about the day — what got done, what didn't, no inflation]

### Friction Fix
*(Fill if RED — one concrete behavioral change for tomorrow)*

### Preview Tomorrow
- [Top priority for tomorrow — pulled from session log carryover or plan sequence]
```

Fill checkboxes from Step 1 auto-gather + Step 2 answers. No signal for a row → leave unchecked, note "(unverified)".

Scoring:
- GREEN if LeetCode ≥5 AND ≥4 of the other 5 rows met
- RED otherwise

If RED: the friction fix must be a specific behavioral change ("Do LeetCode before opening any browser tab", not "be more disciplined").

## §2 Session log entry format

Append to `60_Claude/07_AI_Information/Session Logs/log.md`:

```markdown
## [YYYY-MM-DD] closeday | Daily close

- Note: [[10_Areas/Life/Enumerate/Daily/YYYY-MM-DD]]
- Status: GREEN / RED
- LeetCode: N problems (topic) — lc_count: N
- Study: N hours — study_today: N
- Wins: N/4 — wins_done: N
- Habits: [list from habits_done]
- Open carryover: [any unclosed items rolling to tomorrow]
- Tomorrow: [top priority]
```

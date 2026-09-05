---
name: strategy
description: Runs a decision through four strategic lenses — SWOT, WARGAME, PARETO, LEVERAGE — to find the highest-impact move and the scenarios that could break it.
---
# strategy

**Usage:** `/strategy "the project, decision, or positioning question"`

---

## Why This Exists

[[Maverick Skills Analysis - Cross-Reference with GitHub Repos]] flagged `/strategy` as a real gap the PDF pass's `/challenge` didn't cover — a second, distinct pressure-test for market-facing and resource-allocation decisions (trading strategy, portfolio positioning, project prioritization), as opposed to `/challenge`'s belief/plan pressure-test. [[00_Execution]] queued it alongside `/challenge` and `/ideas`; this is that build, written the same way against this vault's own pattern rather than a templated repo install.

## How This Differs From `/challenge`

`/challenge` (see `.claude/skills/challenge.md`) pressure-tests whether a plan survives scrutiny — premortem, red-team, blindspots, invert. `/strategy` assumes the plan is sound and asks a different question: **where is the highest-leverage move, and what happens if the environment around it changes?** Run `/challenge` first if the plan itself is in doubt; run `/strategy` once you're deciding where to point real effort.

## Instructions

When this skill is invoked:

### 1. Identify the target

State back in one sentence what's being strategized — a project, a trade/position, a career move, a resource-allocation call. If `$ARGUMENTS` is empty, use the most recent concrete decision under discussion.

### 2. Gather real context

Search the vault for what's actually already true about this decision — active project notes, prior session log entries, existing tracking. A strategy analysis built on assumptions instead of real vault state just produces generic advice.

### 3. Run all four lenses

**SWOT** — Strengths, Weaknesses, Opportunities, Threats. Ground each in something concrete: a Strength is a real asset already in hand (a shipped project, a specific skill), not a vague trait; a Threat is a specific, nameable risk, not "competition."

**WARGAME** — Simulate how the environment responds to this move. For a trading strategy: what does the market do if this signal becomes crowded? For a project: what does a competitor or the market do next? For a career move: how does the specific company/team likely react? Run at least a base case and one adverse case — don't stop at the optimistic scenario.

**PARETO** — Of everything that could be done here, what's the 20% that drives 80% of the value? Rank candidate actions by leverage, not by completeness. Explicitly name what falls in the discardable 80%.

**LEVERAGE** — Find the hidden leverage point: the one lever in the system that, if moved, changes everything downstream (a bottleneck, a single high-trust relationship, a piece of infrastructure that unlocks multiple other things). This is often not the most obvious action from the SWOT or PARETO pass.

### 4. Cross-check against real constraints

Before finalizing, check the four lenses against real vault constraints (time budget, existing commitments per `20_Progress/`, stated priorities in the relevant `10_Areas/` hub). A strategically "correct" move that ignores actual bandwidth isn't actionable.

### 5. Deliver a ranked recommendation

Don't just list four analyses — synthesize them into one ranked recommendation: the single highest-leverage next action, with the WARGAME scenario that would change that recommendation stated explicitly (so it's clear what to watch for).

---

## Output Shape

```markdown
## Strategy: [target, one sentence]

### SWOT
- Strengths: ...
- Weaknesses: ...
- Opportunities: ...
- Threats: ...

### WARGAME
- Base case: ...
- Adverse case: ...

### PARETO
- Highest-leverage 20%: ...
- Discardable 80%: ...

### LEVERAGE
[the hidden leverage point, and why it's not the obvious first move]

### Recommendation
**[the single highest-leverage next action]** — valid unless [the WARGAME scenario that would change it].
```

## Guardrails

- Ground every claim in real vault state or the stated decision — no generic business-strategy filler ("focus on your core competencies").
- WARGAME must include at least one scenario where the plan doesn't work, not just the optimistic path.
- If the four lenses genuinely converge on the same action, say so plainly instead of manufacturing artificial tension between them.
- File the output only if the user asks to keep it — this is a working analysis, not automatically a permanent note.

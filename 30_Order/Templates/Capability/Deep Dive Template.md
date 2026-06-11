---
type: concept
status: seed
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - concept
notes: []
track: []
prerequisites: []
used_in: []
evidence: []
difficulty:
mastery_level: novice
mastery_score:
last_drilled:
next_drill:
drill_interval:
---
# <% tp.file.title %>

*Gold standard: see [[40_Resources/Capability/Capability Engine Guide]] for how this template fits the Capability Engine.*

## One-Sentence Version

==The definition in one sentence. What would you tell someone with ten seconds? This becomes an SR cloze.==

*Example:* ==Dynamic programming solves problems by breaking them into overlapping subproblems and caching results to avoid redundant computation.==

## Teach It To A Beginner

The most important intuition, with no jargon. A concrete analogy or story that actually works. If you can't explain it without using the term itself, you don't have the mental model yet.

*Example:* Imagine you're computing the 10th Fibonacci number by recursion. You end up computing fib(3) dozens of times. DP is just writing those results on a sticky note so you never recompute them.

## What It Is

The formal or technical definition. Precision over simplicity here. Include the notation or algorithm if relevant.

## Why It Matters

Connect to a real problem you'd fail to solve without this concept. Avoid "it's widely used in industry" — that's not a reason.

*Example:* Without DP, the naive solution to sequence alignment runs in exponential time. With DP (edit distance), it's O(mn). This is the difference between bioinformatics being computationally feasible or not.

## Mental Model

The key lens for thinking about this concept. One mental image, metaphor, or structural insight that makes the whole thing snap into place.

### Real Example

A concrete worked example, preferably from your coursework or a project. Not "here is a toy example" — use the vault's actual material.

## Implementation

Code, equations, algorithm pseudocode, or step-by-step procedure. Use actual syntax. If this is math-heavy, use LaTeX: $O(mn)$.

```python
# example stub — replace with real implementation
```

## Contrast With

What this is NOT. The concept you'd confuse it with and why that confusion is wrong.

*Format:* **[This concept]** does X. **[Contrast concept]** does Y. The difference matters when Z.

## Failure Modes

What breaks this concept in practice. Common misapplication. The trap most people fall into.

> [!WARNING]
> The most common failure mode: …

## Diagnostic Questions

Questions that test actual understanding — not "what is X?" but "when would you use X instead of Y?" and "what breaks if you do Z?".

- When would you use X instead of Y?
- What breaks if you skip step Z?
- What does this assume that might not hold?

## Interview Angle

The question a recruiter or interviewer is really asking when they name this concept. The trap in the standard phrasing. The answer that separates someone who memorized from someone who understood.

## Related Projects

Wikilinks to vault projects or notes where this concept appears in practice.

- [[ ]]

## Source Anchors

Wikilinks to source summaries this note is distilled from. Grep for the concept name before adding.

- [[ ]]

## Drill Cards

#cards/<% tp.frontmatter.track %>
<% tp.file.title %>::[one-line answer testing understanding, not label recall]

## Next Drill

Target date: `<% tp.date.now("YYYY-MM-DD") %>`
Target mastery: novice → competent

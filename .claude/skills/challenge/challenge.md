---
name: challenge
description: Pressure-tests a belief, plan, or decision by running premortem, red-team, blindspot, and inversion passes against it, then checks the verdict against real vault evidence.
---
# challenge

**Usage:** `/challenge "belief or plan to pressure-test"` or `/challenge` on the current note/conversation context.

---

## Why This Exists

Confirmed gap from the PDF ingestion pass ([[PDF's Ingestion Implementation#Vault Integration & Skills - REVIEW|Vault Integration & Skills]]) and independently again from [[GitHub Ingestion Implementation]]'s Jarvis section — two unrelated sources converged on the same missing command. [[00_Execution]] resolved it as buildable now, without waiting on the unbuilt repo installs (mattpocock-skills, gstack) that were originally proposed as templates: write it directly against this vault's own skill pattern, the same way `/remove-ai-slop` and `/distill-note` were written.

## Instructions

When this skill is invoked:

### 1. Identify the target

- If `$ARGUMENTS` names a belief, plan, or claim, use that directly.
- If empty, pressure-test the most recent concrete decision or plan stated in the current conversation.
- State the target back in one sentence before proceeding — if you can't compress it to one sentence, ask which specific claim to test.

### 2. Search the vault for existing evidence

Before generating any critique, use MCP search (`jarvis_search` or `search_query`) for notes that already touch this claim — active projects, session log entries, prior decisions. A pressure-test that ignores what the vault already knows just re-derives what's already settled.

### 3. Run all four passes

Do not skip a pass because it feels redundant with another — they surface different failure classes.

**Premortem** — Assume it is one year from now and this failed completely. Write the most plausible failure story in 2-4 sentences: what broke, when, and why it wasn't caught earlier.

**Red Team** — Argue against the plan as a motivated adversary, not a neutral reviewer. What's the strongest case that this is the wrong call? Attack the weakest assumption, not a strawman.

**Blindspots** — List the assumptions the plan depends on that are never stated outright. For each, ask: is this actually true, or just convenient to believe? Cross-reference against real vault state (e.g., "assumes `internship-research-loop` covers LinkedIn — it doesn't, per [[Internship Pipeline]]").

**Invert** — State the opposite of the current approach and ask what would have to be true for the opposite to be the better call. If inverting reveals the current plan already dominates on every axis, say so explicitly instead of manufacturing a fake tension.

### 4. Weigh the passes against vault evidence

For each pass, note whether the vault already contains evidence that confirms, contradicts, or is silent on the concern raised. A blindspot the vault already resolves isn't a real gap — flag it as closed, not open.

### 5. Deliver a verdict

End with one of three calls, stated plainly:

- **Survives** — the plan holds; state the strongest counter-argument that failed to break it.
- **Survives with a fix** — name the one change that closes the biggest gap found.
- **Does not survive** — name the failure mode that actually breaks it and what the plan should be instead.

### 6. File only if durable

If the pressure-test changes a real decision (not just a passing conversation), offer to log the outcome to the relevant project note or `60_Claude/00_Inbox/` — don't create a new note for a one-off gut check.

---

## Output Shape

```markdown
## Challenge: [target, one sentence]

### Premortem
[failure story]

### Red Team
[strongest adversarial case]

### Blindspots
- [assumption] — [confirmed / contradicted / open, with vault evidence if any]

### Invert
[opposite case, and what would have to be true]

### Verdict
**[Survives / Survives with a fix / Does not survive]** — [why, in one to two sentences]
```

## Guardrails

- Do not manufacture disagreement where the vault evidence is already one-sided — a pressure test that finds nothing wrong is a valid, useful result.
- Do not soften the verdict to avoid conflict with a plan the user already committed to. The point is to find what actually breaks, not to be agreeable.
- Ground every claim in either the stated plan or real vault evidence — no generic "consider the risks" filler.

---
name: ideas
description: Generates a grounded idea report — tools worth building, people worth meeting, topics worth investigating — filtered against real vault gaps instead of generic brainstorming.
---
# ideas

**Usage:** `/ideas` for a general scan, or `/ideas "domain"` to scope the report (e.g. `/ideas trading`, `/ideas career`).

---

## Why This Exists

Same confirmed gap as [[.claude/skills/challenge.md|/challenge]] — flagged independently by [[PDF's Ingestion Implementation#Vault Integration & Skills - REVIEW|Vault Integration & Skills]] and [[GitHub Ingestion Implementation]], resolved in [[00_Execution]] as buildable now against this vault's own patterns rather than templated off unbuilt repo installs (agent-skills-addyosmani's brainstorm template, GSD's PARETO filtering). The point of this skill isn't idea volume — the vault already has 100+ ingested sources sitting unconverted into action. The point is filtering: find the 20% of possible next moves that actually close a named gap in active work.

## Instructions

When this skill is invoked:

### 1. Load current state

Read, in order:
- `60_Claude/07_AI_Information/AI_CONTEXT.md` and `00_Dashboard.md` for active projects and current focus
- Tail of `60_Claude/07_AI_Information/Session Logs/log.md` for what just happened
- If `$ARGUMENTS` scopes a domain, read that domain's hub note in `10_Areas/` and its active work in `20_Progress/`

### 2. Generate candidates across three categories

Do not brainstorm freely — every candidate must trace to something real: an open question already logged somewhere, a gap between two existing notes, or a stated but unbuilt next step.

**Tools to build** — A skill, script, or integration that closes a gap between two things the vault already has. Example shape: "X exists (per [[note]]) and Y exists (per [[note]]), but nothing connects them — build Z."

**People to meet** — A category of person (not a name you don't have) worth reaching out to, grounded in an active goal. Example shape: "The [[Internship Pipeline]] recruiter-discovery step has no current targets in [[some Program note]] — worth finding a specific alum at that company."

**Topics to investigate** — A named open question already sitting unresolved in the vault (an `(*HOW USEFUL?*)` tag, an unchecked open question, a flagged-but-undecided item), not a fresh topic invented for this report.

### 3. Filter ruthlessly (PARETO pass)

For every candidate, ask: does this unblock something already in motion, or does it just sound interesting? Cut anything that doesn't trace to a real, named gap. Keep the list short — 3-5 ideas per category, ranked, not 20 unranked ones.

### 4. Ground each surviving idea

For each idea that survives the filter, state:
- **What gap it closes** (name the specific vault note or project)
- **What it would take** (rough time/effort, not a full plan)
- **What it unblocks** (the next thing that becomes possible)

### 5. Rank and report

Order each category by leverage — the idea that unblocks the most, first. Don't pad the report with weak filler ideas just to hit a count.

### 6. File only if requested

This report is disposable by default — a scan, not a deliverable. Only write it to `60_Claude/00_Inbox/` if the user asks to keep it; otherwise it lives in the conversation.

---

## Output Shape

```markdown
## Ideas: [scope, or "general scan"]

### Tools to Build
1. **[idea]** — closes [gap, with wikilink] · [effort] · unblocks [what]

### People to Meet
1. **[category of person]** — grounded in [wikilink] · why now

### Topics to Investigate
1. **[open question]** — already flagged in [wikilink] · why it matters now
```

## Guardrails

- Never invent a "gap" that isn't real — if a category has fewer than 3 grounded candidates, report fewer. Padding with generic ideas defeats the purpose.
- Prefer one well-grounded idea over five vague ones.
- If the vault's own `(*HOW USEFUL?*)` / open-question backlog already covers the domain (e.g. `40_Resources/CS/Repos.md`'s unresolved tier), surface those directly instead of generating new ones on top.

---
type: evergreen
status: sprout
created: 2026-05-04
tags:
  - evergreen
  - ai
  - learning
  - second-brain
related:
  - "[[AI AGENT]]"
  - "[[CLAUDE]]"
  - "[[60_Jarvis/00_Control_Center/Jarvis Operating Rules|Jarvis Operating Rules]]"
  - "[[60_Jarvis/40_Promoted_Notes/Promotion Criteria|Promotion Criteria]]"
---
# AI Learning Across Vaults

This note records the discussion about what this vault is supposed to become, how it should relate to Jarvis, and how AI should be used for learning without replacing my own thinking.

## Core realization
This vault is not supposed to be just a folder of notes. It is supposed to become a living second brain.

The problem is not that there is no information here. There is already a lot: class notes, project notes, daily captures, AI-generated plans, templates, dashboards, and unfinished ideas. The problem is that much of this information has not yet been turned into **trusted understanding**, **recallable knowledge**, **project execution**, or **proof**.

The goal is not merely to store knowledge. The goal is to learn from it, test it, connect it, use it, and make it available when I need it.

The right vision is:

> The Plan is my trusted second brain. Jarvis is my AI-powered processing engine. My job is to capture honestly, think actively, make decisions, and approve what becomes trusted. AI's job is to reduce friction, expose gaps, test understanding, connect notes, and help me execute.

## The role of each vault
There should be a clear difference between **The Plan** and **Jarvis**.

### The Plan
The Plan is the trusted personal knowledge system.

It should contain:
- my real class notes,
- my project plans,
- my current decisions,
- my reflections,
- my trusted summaries,
- my learning maps,
- my career/project proof,
- my final distilled understanding.

The Plan should be the place I actually live in, read from, study from, and use to make decisions.

### Jarvis
Jarvis is the AI-powered knowledge hub.

It should contain:
- raw AI processing,
- source ingestion,
- enrichment attempts,
- generated summaries,
- search/indexing outputs,
- rough project scaffolds,
- knowledge tests,
- note audits,
- promotion candidates.

Jarvis can hold more than The Plan because Jarvis is allowed to be messy, experimental, and automated. It is a machine room.

### The boundary
Jarvis should be allowed to know almost everything from The Plan, but The Plan should not automatically absorb everything from Jarvis.

That means:

- **The Plan -> Jarvis**: broad sync is allowed, except protected folders like `00_Inbox` and operational exceptions.
- **Jarvis -> The Plan**: only promoted, reviewed, useful, grounded material should move back.

The Plan is the trusted memory. Jarvis is the processing layer.

## Why filtering matters
If everything from Jarvis comes back into The Plan, then The Plan becomes polluted with unreviewed AI output. It stops being trusted. It becomes a generated wiki.

If nothing from Jarvis comes back into The Plan, then Jarvis becomes disconnected from real life. It becomes an impressive tool that does not change my actual learning or execution.

The answer is a promotion pipeline.

Material from Jarvis should enter The Plan only when it passes these questions:

1. Is this grounded in a source, project, class note, command result, or real experience?
2. Is this useful for learning, deciding, building, reviewing, or remembering?
3. Is this stable enough that I would trust it later?
4. Has it been checked for hallucination, unsupported certainty, or stale claims?
5. Does it improve an existing note, or does it deserve a new note?
6. Can I explain it in my own words?

If the answer is no, it stays in Jarvis or gets archived.

## The promotion ladder
Knowledge should move through stages.

### 1. Capture
This is raw input.

Examples:
- class notes,
- quick thoughts,
- project ideas,
- copied links,
- rough questions,
- AI transcripts,
- screenshots,
- messy outlines.

Capture does not need to be beautiful. It just needs to exist.

### 2. Process
Jarvis can help process the capture.

AI can:
- summarize,
- group,
- title,
- extract claims,
- create links,
- identify missing pieces,
- ask clarification questions,
- generate tests,
- compare against source notes.

This is where AI is useful. It reduces the friction of turning mess into structure.

### 3. Test
The knowledge should be tested before it becomes trusted.

Testing can include:
- recall questions,
- application problems,
- explaining the idea from memory,
- comparing my explanation against the source,
- using the idea in a project,
- solving homework or exam-style problems,
- creating a working demo.

This is the most important missing layer. A second brain should not just store facts. It should help me check whether I actually know them.

### 4. Promote
Only after processing and testing should a note become trusted in The Plan.

A promoted note should have:
- a clear purpose,
- strong links,
- my own explanation,
- examples,
- common mistakes,
- test questions or proof,
- a next action if it is still active.

### 5. Recall
The final goal is fast recall.

A note is successful when I can:
- recognize the concept quickly,
- explain it without rereading the whole note,
- apply it to a problem,
- connect it to related ideas,
- retrieve it later through links, search, or a dashboard.

## How to use AI without outsourcing thinking
The danger is using AI as a replacement brain. That makes me feel productive while weakening my own recall.

Bad AI use:
- "Explain this entire chapter to me."
- "Write this note for me."
- "Summarize everything."
- "Make this project plan."
- "Generate flashcards" without me answering them.

Better AI use:
- "Ask me questions about this note."
- "Find what I do not understand."
- "Challenge my explanation."
- "Compare my answer to the source."
- "Give me a harder example."
- "Turn my messy notes into a structure, but preserve my thinking."
- "Create a test from this note and grade my answers."
- "Find contradictions across these notes."
- "Show me what is missing before this can be trusted."

The rule:

> AI should make me think more clearly, not think instead of me.

## The AI learning loop
This is the learning loop I should use across the vault.

### Step 1: Capture honestly
During class, during projects, or during the day, write the raw thought.

Do not try to make it perfect immediately.

Useful markers:
- `??` for confusion,
- `!!` for important insight,
- `ACTION` for something to do,
- `SOURCE` for where the idea came from,
- `TEST` for something I should be able to answer later.

### Step 2: Ask AI to expose gaps
Prompt:

> Using only this note and its linked notes, identify what I do not understand yet. Ask me questions instead of rewriting the note.

This forces the note to become a learning surface.

### Step 3: Explain in my own words
Every serious learning note should have:

```md
## My Understanding

## Still Confused

## Example

## Common Mistakes
```

If I cannot fill these sections, I do not know the topic yet.

### Step 4: Test recall
Ask AI:

> Create a recall test from this note. Do not show answers until I answer first.

Then answer from memory.

AI should grade, correct, and point back to the exact note sections.

### Step 5: Apply
Knowledge becomes stronger when used.

For class notes:
- solve a practice problem,
- explain an algorithm,
- compare two concepts,
- make a mini-proof,
- derive a runtime.

For projects:
- build a feature,
- write a test,
- make a demo,
- explain an architecture decision,
- record a failure and fix.

### Step 6: Promote or archive
After testing, decide:

- Promote to trusted note.
- Keep as active work.
- Archive as historical reference.
- Delete if it is noise.

## How to learn faster
The goal is not to read more. The goal is to shorten the cycle between exposure, understanding, testing, and recall.

Fast learning requires:

1. **Active recall**
   - I should be asked questions constantly.

2. **Spaced review**
   - Important notes should resurface after time passes.

3. **Interlinking**
   - A concept should connect to prerequisites, applications, projects, and mistakes.

4. **Compression**
   - Long notes should have short summaries.

5. **Expansion**
   - Short summaries should link to deeper details.

6. **Application**
   - Knowledge should lead to solved problems or built things.

7. **Feedback**
   - AI should grade, critique, and reveal gaps.

This is how the second brain becomes alive: it does not just hold knowledge, it keeps making me retrieve and use it.

## What a strong note should contain
For learning notes:

```md
## Core Idea
## Why It Matters
## My Understanding
## Example
## Common Mistakes
## Mini-Test
## Related Concepts
## Where I Used This
```

For project notes:

```md
## Why This Exists
## Final Demo
## Current State
## Next 3 Actions
## Decisions
## Tests / Proof
## Risks
## Evidence
## Reflection
```

For class boards:

```md
## What This Course Was Really About
## Main Concept Map
## Best Notes
## Weak Notes
## Exam / Project Proof
## Archived Material
## What I Can Now Do
```

## UMN direction
For UMN, the goal is not to keep every weekly note equally active.

The semester is winding down, so each course should be consolidated into a small number of strong surfaces:

1. Course board
2. Concept map
3. Problem/test sheet
4. Project/lab summary
5. Archive index

Old weekly notes can stay, but they should link into the stronger course-level files. This lets the course become a knowledge system instead of a folder of disconnected notes.

The courses to prioritize:
- CSCI 2033
- CSCI 4041
- CSCI 2011
- CSCI 2021
- CSCI 3923
- MGMT 3001
- CSCI 2041
- The Plan itself

The target is not literal perfection. The target is that each course has enough structure that I can reopen it later and quickly understand:
- what the course taught,
- what I learned,
- what I still need to review,
- what problems I can solve,
- what projects or proofs came out of it.

## Project direction
Projects need more than ideas. They need endpoints.

Every project should answer:

1. What is the final demo?
2. Who is it for?
3. What problem does it solve?
4. What is the smallest working version?
5. How will I test it?
6. What proof will it create for my career?
7. What is the next action?

If I cannot describe the final demo, I will probably not finish the project.

Before building, ask AI:

> Do not help me code yet. Force me to define the final demo, user, success criteria, risks, and proof that this project works.

This makes AI a clarity tool instead of a distraction tool.

## What Jarvis should do
Jarvis should be based on workflows, not just knowledge collection.

Core workflows:

1. **Learn**
   - Turn notes into tests, explanations, examples, and review plans.

2. **Build**
   - Turn project ideas into demos, tasks, decisions, tests, and proof.

3. **Review**
   - Run daily and weekly reviews across active notes.

4. **Promote**
   - Move only trusted, useful, reviewed material into The Plan.

5. **Audit**
   - Find stale claims, unsupported notes, broken links, placeholders, and missing next actions.

6. **Retrieve**
   - Answer questions from the vault with citations and links.

Jarvis should not be a chatbot floating above the vault. Jarvis should be a set of repeatable workflows that make The Plan stronger.

## What The Plan should do
The Plan should be where I:
- think,
- study,
- plan,
- decide,
- recall,
- build,
- reflect.

It should answer:

- What matters right now?
- What am I learning?
- What am I building?
- What do I understand?
- What am I confused about?
- What proof do I have?
- What is the next move?

## The final vision
The Plan should become an alive brain.

Not a static vault.
Not a dumping ground.
Not a generated encyclopedia.
Not a place where AI writes everything and I understand nothing.

It should be a system where:
- I capture reality,
- AI organizes and challenges it,
- I test my understanding,
- useful knowledge gets promoted,
- weak knowledge gets reviewed,
- projects become demos,
- classes become concept maps,
- thoughts become decisions,
- decisions become action.

The highest standard is not "I have a note on this."

The standard is:

> I can recall it, explain it, use it, test it, and connect it.

That is what learning with AI across these vaults should mean.

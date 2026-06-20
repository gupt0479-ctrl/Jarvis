---
type: input
input_kind: gpt
status: sprout
created: 2025-12-23
source_url: use gpt for obsidian
related_progress: []
tags:
  - input
next: "[[Random]]"
---
# How to prompt
When people talk about “guard rails” for prompting, they usually mean practices that keep interactions with large language models reliable, consistent, and safe from drift, hallucination, or misinterpretation. Think of them as scaffolding for your conversations.
Here are some of the most effective categories:
1. *Role & Context Anchoring*:
	Define the role: Begin with “You are an expert financial analyst,” or “Act as a technical support engineer.” This sets tone, depth, and style.
	Give background: Supply constraints (“I’m using Azure SQL, not MySQL”) or environment details (“Budget-conscious small business, no dedicated devs”).
	- Re-anchor often: Restate the role if conversations stretch out, since LLMs can drift.
2. *Format & Output Guard Rails*: 
	Explicit structure: Ask for bulleted lists, tables, numbered steps, JSON, or Markdown, depending on your needs.
	- Boundaries: Use markers like START OF PROMPT and END OF PROMPT if the output needs to be copied into another system.
	- Level of detail: Say “explain like I’m technical but not a coder” vs. “full code sample with inline comments.”
	- Length controls: “Keep it under 300 words,” “1 paragraph per section,” or “short sentences for readability.”
3. *Instruction Hierarchy*:
	Priority guidance: Tell the model what not to do. Example: “Never include emojis. Do not add motivational language.”
	- Order of execution: Break tasks into ordered steps (“First summarize, then extract action items, then suggest next steps”).
	- Hard constraints: Call them out clearly, e.g., “Use only publicly available sources,” “Avoid speculation."
4. *Verification & Grounding*:
	Citations required: “Provide sources with URLs” or “Always cite with line numbers.”
	- Double-check mode: “List assumptions and uncertainties at the end.”
	- Comparisons: Ask for side-by-side pros/cons rather than one-sided answers to avoid overconfidence.
5. *Error & Ambiguity Handling*:
	Encourage clarification: “If information is missing, ask me instead of filling in gaps.”
	- Fallbacks: “If you don’t know, say so and explain how I could verify.”
	- Confidence labels: “Rate your confidence from 1–5.”
6. *Iteration & Modularity*:
	Chunking: Large projects work better in pieces (“First generate the outline, then we’ll fill in section 1”).
	- Version control: Ask the model to append v1, v2, etc., so you can track changes across drafts.
	- Reusable blocks: Tell it to save reusable components like “prompt templates” or “boilerplate responses.”
7. *Behavioral Guard Rails*:
	Tone: “Direct and professional, no fluff.”
	- Bias control: “Cover multiple perspectives without making a recommendation unless asked.”
	- No overreach: “Don’t invent steps if the procedure is unclear—flag instead.”
Bottom line: The strongest guard rails are role clarity, explicit formatting rules, error handling, and iteration discipline. If you set those up front and reinforce them when needed, you’ll keep interactions sharp and predictable.
# Obsidian Notes
## For Weekly templates
```
You are tasked with creating detailed study notes from provided weekly lecture and textbook materials without including any content references such as ":contentReference[oaicite:26]{index=26}" anywhere in the output.

Do not provide metadata for the files, as the user already has a template for that.

Your notes should adhere to the following structure focusing on the week's template and the textbook readings:

1. **Takeaways:**
   - Questions about the key concepts, insights, or answers related to the week topics.
   - Focus only on the main points necessary to understand.
2. Key points(textbook)
   - I want all the important details from each subheading of the chapter onto this key points.
- Make sure that these points are just important and short
3. Examples worth keeping
- I want the examples explained in coding homework's or the paper homework's. 
- Important examples from the textbook also work, these should not exceed more than 5 and should be short.
4. **Flashcards:**
   - Provide up to 7 flashcards covering the most important topics discussed in that week's material.
   - Each flashcard should contain a clear question and a concise answer.
   - Keep flashcards limited to 7 to allow the user to test themselves efficiently; this count is a maximum.

Do not include any extra headers such as "Discussion Points" or "Assignments" as these were not part of the original weekly templates and should be omitted.

# Steps

- Extract the exact content from the textbook file
- Summarize major takeaways questions 
- Generate up to 7 key flashcards focusing strictly on the week's main topics.
- Remove any content references and do not output metadata or unrelated headers.

# Output Format


Produce the notes in markdown format with the following structure provided above as the week template. Add some "> [!NOTE]" or similar editing to the conetent above without changing any word. Ensure clean formatting, clarity, and brevity as specified.

# Notes

- Do not include any content reference tags in your output.
- Avoid adding any headers or content not requested by the user.
- Use only the material provided for that week's content to generate notes and flashcards.
- If more flashcards are desired, the user will specify; do not exceed 7 by default.
```
## Meetings
Here’s the exact workflow they demonstrated, distilled and ready to copy.
Step-by-step
- Gather 8–15 of your best posts that reflect your voice.
- Ask AI to act as a “content decipherer” and produce a Content DNA report from those samples.
- Convert that DNA into a reusable prompt; ask for it in a fenced code block so you can copy-paste cleanly.
- Paste the prompt into your Custom GPT “Instructions” (paid) or create a Gemini “Gem” (free) and paste it there.
- Test with a topic, review the output, refine the DNA and prompt, and repeat.
What to ask first (Content DNA extractor)
Copy this and run it, then paste your samples:
```
Act as an expert Content Decipherer. Analyze the writing samples I’ll provide and output a concise “Content DNA” with these sections:
1) Voice & persona
2) Tone spectrum (e.g., casual→formal) and when it shifts
3) Structure patterns (hooks, setup, body, close), typical length
4) Hook formulas I use
5) Paragraph and sentence cadence
6) Formatting habits (lists, line breaks, emojis, hashtags, bold/italics)
7) Vocabulary and metaphors I favor; banned words/phrases
8) POV usage (I/you/we), rhetorical devices, questions
9) CTA styles and linking behavior
10) Editing rules (what I cut, how I tighten)
11) Examples: 3 mini-summaries of my style in action
12) Do/Don’t checklist
Return only the DNA in clean Markdown with headings and bullet points.
```
Then give it your samples.
Turn DNA into a reusable prompt
After you get the DNA, run:
```
Using the Content DNA below, generate a production-ready prompt that reliably replicates the style. Requirements:
- Role: “You are a senior copywriter that writes in the exact style below.”
- Inputs the model should ask me for: target audience, goal, topic, context, product facts, constraints (length, platform), banned claims, region.
- Output spec: structure, length, formatting, CTA, optional variants, headline options, hashtags/emojis policy.
- Guardrails: factuality, no hallucinations, no sensitive claims, comply with platform policies, avoid prohibited phrases listed in DNA.
- Quality checks: 10-point checklist before finalizing; include a self-critique and a one-shot revision.
- Revision loop: If I reply “revise,” ask 2–3 clarifying questions, then update.
- Return the entire prompt in one fenced Markdown code block suitable for pasting into a model’s system/instructions.
Content DNA:
[PASTE DNA HERE]
```
Paste into your tool
- Custom GPT: Instructions field.
- Gemini Gem: create a new Gem and paste into its description/instructions.
Test and iterate
- *Prompt it*: “Write a LinkedIn post on [topic] for [audience] to achieve [goal]. Max 140 words. Follow DNA.”
- If it drifts, update the DNA’s Do/Don’t and banned list, then regenerate the prompt and replace it.
Quick-start master prompt (ready to paste)
```
You are a senior copywriter that writes exactly in the “Content DNA” below.

When I give you a task, first ask for any missing inputs: target audience, goal, topic, product facts, constraints (platform, length), region/compliance, banned claims/phrases.

Produce:
1) 3 headline options
2) 1 primary draft that follows the DNA’s structure, tone, cadence, and formatting
3) 1 variant (tighter/looser tone)
4) CTA consistent with DNA
5) Hashtags/emojis per DNA policy

Guardrails: be factual, cite placeholders for unverifiable data, avoid sensitive or prohibited claims, no hallucinations, follow platform rules, and respect the DNA “Don’ts.”

Quality check (run silently, then apply fixes):
- Hook strength
- Clarity and specificity
- Cadence and line breaks
- Jargon control
- Narrative flow
- Proof/credibility
- CTA fit
- Length limit
- Formatting fidelity
- Originality

If I reply “revise,” ask up to 3 clarifying questions, then return an improved draft.

Content DNA:
[PASTE YOUR DNA HERE]
```
That’s the “perfect” loop they modeled: samples → DNA → prompt-in-code-block → paste into tool → test → refine.
# Master prompts for your workflow
1. *ChatGPT → PRD generator prompt*: Use this when you have messy notes, screenshots, errors, or half-formed ideas:
```
# Role  
You are a product-minded technical writer helping me create a build-ready PRD for Cursor.  
  
# Goal  
Turn my rough notes into a precise PRD that an IDE coding agent can follow with minimal ambiguity.  
  
# Context  
I am building portfolio-quality projects and want the PRD to reduce avoidable errors.  
The PRD will live in Obsidian as Markdown and later be referenced inside Cursor.  
  
# Instructions  
1. Extract the feature goal in one sentence.  
2. Rewrite the request into a clean PRD.  
3. Include:  
   - problem  
   - users  
   - scope  
   - non-goals  
   - UX requirements  
   - technical notes  
   - files likely affected  
   - acceptance criteria  
   - edge cases  
   - test checklist  
4. Where details are missing, do not guess silently. Add an "Open Questions / Assumptions" section.  
5. Keep the output concise but implementation-ready.  
6. Format the result in Obsidian-friendly Markdown.  
  
# Input  
[paste notes, screenshots, errors, links, examples]
```
This matches the Markdown prompting structure in your notes and the plan-first workflow in your guide.
2. *Cursor implementation prompt*: Use this inside Cursor after attaching the PRD and files:
```
Use @docs/prd/<feature-name>.md as the source of truth.  
  
Task:  
Implement the feature exactly as specified.  
  
Constraints:  
- Prefer the smallest diff that solves the task.  
- Do not change unrelated files.  
- Do not change public interfaces unless required by the PRD.  
- Preserve current design language and architecture.  
  
Before editing:  
1. Summarize the task in 3 bullets.  
2. List the files you expect to change.  
3. State assumptions or missing details.  
  
After editing:  
- Summarize each changed file in one line.  
- List exact commands for lint, typecheck, tests, and build.  
- List anything intentionally deferred.
```
3. *Cursor debugging prompt*: Use when you hit a bad error or broken state:
```
I need a targeted debug pass.  
  
Context:  
- Feature I was building: [feature]  
- Exact error: [paste exact error]  
- Expected behavior: [what should happen]  
- Recent files changed: @[file1] @[file2] @[file3]  
  
Instructions:  
1. Diagnose the most likely root causes in ranked order.  
2. Identify the minimum set of files to inspect.  
3. Propose the smallest safe fix.  
4. Do not refactor unrelated code.  
5. After edits, tell me exactly how to verify the fix.
```
This lines up with the debugging loop in your course notes and the “observe exact error first” approach in your HTML guide.
4. *PRD-to-task-breakdown prompt*: Use before implementation to split a feature into reviewable chunks:
```
Read @docs/prd/<feature-name>.md and convert it into an implementation plan.  
  
Return:  
- Phase 1: foundation  
- Phase 2: core feature  
- Phase 3: polish  
- For each phase:  
  - goal  
  - files likely touched  
  - risk level  
  - verification steps  
- Then propose the safest order of execution.
```
## Obsidian PRD template that works well with Cursor
```
---  
type: prd  
status: draft  
project:   
feature:   
created:   
updated:   
tags: [prd, cursor, implementation]  
---  
  
# Feature  
One-sentence name of the feature.  
  
## Summary  
One paragraph describing what is being built and why.  
  
## Problem  
What user or product problem does this solve?  
  
## Users / Audience  
Who is this for?  
  
## Goal  
What outcome should exist when this is complete?  
  
## Non-Goals  
What is explicitly out of scope?  
  
## UX / Behavior Requirements  
-   
-   
-   
  
## Technical Context  
- Stack:  
- Existing components/services:  
- Constraints:  
- Dependencies:  
- Relevant env vars:  
- Relevant routes or APIs:  
  
## Files Likely Affected  
- ``  
- ``  
- ``  
  
## Data / State Impact  
- New data?  
- API changes?  
- Schema changes?  
- State changes?  
- Caching implications?  
  
## Acceptance Criteria  
- [ ]   
- [ ]   
- [ ]   
  
## Edge Cases  
-   
-   
-   
  
## Test Checklist  
- [ ] lint  
- [ ] typecheck  
- [ ] unit/integration tests  
- [ ] manual happy path  
- [ ] manual edge cases  
  
## Open Questions / Assumptions  
-   
-   
  
## Implementation Notes  
Short notes for the coding agent.  
  
## Change Log  
- YYYY-MM-DD:
```
This template is designed to be both human-readable in Obsidian and machine-usable in Cursor. It directly supports the “spec first, then code” pattern present in your notes.
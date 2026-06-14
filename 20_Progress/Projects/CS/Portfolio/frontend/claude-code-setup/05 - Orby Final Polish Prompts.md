---
type: concept
status: active
created: 2026-06-14
updated: 2026-06-14
tags:
  - portfolio
  - claude-setup
  - frontend
  - prompts
notes:
  - "[[03 - Per-Phase Build Prompts]]"
  - "[[06 - Tool System & Generative UI]]"
  - "[[04 - Orby Integration]]"
  - "[[03 - Context Engine, Grounding & Personas]]"
---
# Orby Final Polish Prompts — make Orby a living being (last chatbot pass)
> The model setup (V1) and Orby wiring (V2) are built. This is the **final** chatbot pass: clean output rendering, Orby actually reacting on every send, and the persona prompts/voices. Two prompts, run each in its own `/clear` session, paste verbatim, `pnpm typecheck`, report. **Claude Code does NOT deploy.** After F2 reports green, the chatbot is done.
Path prefixes:
`FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend`
`NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot`
## What's broken (from the live screenshots)
1. Replies render as **raw text** — `**bold**`, `### headings`, and giant `|markdown tables|` show as literal tokens. Unreadable.
2. Orby **does nothing on send** — no navigation to the asked-about section, no catchy line. The whole "living Orby" feature is dead.
3. Friend's fixed prompt (techlit) is weak; recruiter/ceo power-prompts aren't strong enough; weirdo refuses with the flat grounded line instead of being funny.
F1 fixes the mechanics (1, 2). F2 fixes the content (3). Both reference the now-updated notes as source of truth.
## F1 — Clean rendering + Orby comes alive
```
NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot
FE = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend
Read NB/06 - Tool System & Generative UI.md (the "Output rendering" section), NB/04 - Orby Integration.md, NB/09 - Orby UI Fixes.md, and FE/12 - Orby Friction Fixes.md fully. frontend-builder for UI, ai-engineer for the route/prompt.

A) OUTPUT RENDERING (two blocks, never raw):
- Render assistant message text as MARKDOWN via react-markdown + remark-gfm, with themed styled components: bold, italics, headings, bullet/numbered lists, inline code, fenced code blocks, and GFM tables all render properly. The visitor must NEVER see literal **, ###, or |---| tokens. (Add the deps with pnpm if missing.)
- Layout = two stacked blocks per reply: the prose markdown bubble on TOP, and any evidence card/box rendered BELOW it (not a table stuffed in the bubble). Style the card to match the lab (the violet panel) — readable, padded, rounded.
- Update the system/persona prompt so the model returns SHORT prose and pushes structured/tabular detail into a card via the tool layer instead of dumping a multi-row markdown table into the text. A 12-row table in a chat bubble is the failure we're killing.

B) ORBY ACTS ON EVERY SEND (the living-being behavior — currently does nothing):
- On submit, the model must produce IN THE SAME TURN: (i) a per-request `orbyMessage` — a short, catchy, in-persona line, AI-generated fresh each time, grounded and length-capped; and (ii) a `navigate(sectionId)` from the closed Sanity-nav enum whenever the question maps to a section.
- Wire the pipeline from NB/04: Orby glides back to its portfolio-button home → the page scrolls to that section → Orby pops the catchy `orbyMessage` on arrival (after scroll-end). Keep this fully separate from the existing scroll popups.
- Fail-safe: a malformed/absent navigate → answer in text only, no fake scroll, no desync. One navigation per turn. Respect prefers-reduced-motion (jump, still speak).

VERIFY (report each): (a) a typed question renders markdown cleanly with the card BELOW the prose; (b) no raw **/###/| tokens anywhere; (c) "show me your projects" scrolls to the Projects section AND Orby says a unique catchy line on arrival; (d) a malformed navigate degrades to text only.
Run pnpm typecheck. Report. Do not deploy.
```
## F2 — Persona prompts & voices (the showcase + the funny)
```
NB = /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot
Read NB/03 - Context Engine, Grounding & Personas.md (the "Finalized fixed prompts & persona voice" section) fully. ai-engineer for prompts/route, eval-runner for the eval cases.

1) FRIEND fixed chip — replace the techlit prompt with exactly: "Did Anant vibe code this portfolio?"
   Friend-voice answer: funny, honest, TILTED TO NO — he architected and hand-built the bulk of it, but it spiraled near the end (Orby especially was a saga) and he leaned on AI help to actually finish it. Lands on: not vibe-coded, but not a solo flex either. (Generated each time in friend voice, not hard-coded verbatim.)

2) RECRUITER + CEO power-prompts — replace the current ones with the two author-written blocks verbatim from the note (the [Recruiter lens] and [CEO lens] blocks). They force evidence-ranking/prioritization (make the model think), require opening a portfolio section (navigation test), and end by showing a card — so the reply renders as TWO BLOCKS (tight prose + evidence card, per F1). Confirm paste detects the persona marker and locks recruiter/ceo.

3) WEIRDO voice — it must NOT use the default "I don't have that in Anant's record" refusal opener. On an odd or unknown question it opens with: "What a funny question, here is my thought process:" then reasons playfully. HARD RULE preserved: still grounded — it can admit a gap quirkily but NEVER invents a fact. Only the tone changes, not the truth. On the saved/default prompts, a quirky funny reply.

Keep all four personas on the SAME grounding + safety guardrails; only voice/prompt changes. Add/refresh eval cases: friend prompt text, recruiter/ceo two-block + correct section, weirdo funny-opener + no-fabrication.

VERIFY (report each): friend chip shows the new question and answers tilted-to-no; recruiter/ceo paste → a think-y two-block answer that opens the right section + card; weirdo opens with the funny line and never fabricates.
Run pnpm typecheck and /eval. Report. Do not deploy.
```
## Done definition
After F1 + F2 report green: replies render with real formatting and a card below, Orby reacts on every send (catchy line + navigation), and the four personas read distinctly — recruiter/ceo as a prompt-engineering flex, friend funny-honest, weirdo quirky-but-grounded. That is the chatbot complete. Remaining portfolio work (performance, README, deployment, clean GitHub, Sanity polish, write-ups, publishing) is non-chatbot and lives in the next pass of [[03 - Per-Phase Build Prompts]].

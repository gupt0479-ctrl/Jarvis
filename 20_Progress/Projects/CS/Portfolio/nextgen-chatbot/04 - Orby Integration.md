---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - ai
  - orby
notes:
  - "[[00 - Nextgen Chatbot — Build Plan]]"
  - "[[06 - Tool System & Generative UI]]"
---
# Orby Integration
This note owns how Orby connects to the chatbot. It is the fix for premortem failure 4 (intent/page desync). The whole feature is one deterministic pipeline; the danger is wiring it loosely through three triggers instead of one.
## Two channels that must stay separate
Orby has two unrelated reasons to speak. Confusing them is the main risk.
- **Scroll popups (existing, untouched).** Orby reacts to scroll position with pre-written lines. We already have plenty of these. This channel knows nothing about the chatbot and we do not change it.
- **Chat-driven navigation + speech (new).** Fires *only* while the visitor is talking to the chatbot. The agent decides to send the visitor somewhere, the page scrolls there, and Orby speaks a line tied to that specific reply.
Rule: a chat-driven Orby message is a property of a **chat turn**. It must never be triggered by scroll, and a scroll popup must never be triggered by a chat turn. Keep them in separate code paths with separate state so they cannot cross-fire.
## The deterministic pipeline
Orby physically drifts as the visitor scrolls — it starts at the bottom-left next to the portfolio button and wanders toward the bottom-right as if floating in space (existing behavior). The chat-driven sequence choreographs that movement deliberately. Four ordered steps, one source of truth:
1. **Orby returns home.** When the agent decides to navigate, Orby first glides back to its home position next to the portfolio button — a visible "I'm taking you somewhere" beat. This re-anchors it before the jump so the motion reads as intentional, not random drift.
2. **Model emits one `navigate(sectionId)` tool call.** `sectionId` is constrained to the closed enum of Sanity nav links (see [[06 - Tool System & Generative UI]]) — the model cannot invent a section. The same tool result carries the per-request `orbyMessage` string for this reply.
3. **The page scrolls to that section.** The handler looks up the real Sanity nav target and scrolls. Navigation is the only side effect.
4. **On arrival, Orby pops its message.** The pop-up appears *after* the scroll lands (scroll-end / intersection callback), at the section — never before, so Orby never talks about a place the visitor has not reached.
## Fail-safe behavior
If the `navigate` call is malformed or names a section that does not resolve, the pipeline **does nothing visual** and Orby just answers in text. It never half-scrolls, never fires a message for a section it did not reach, never pretends to navigate. A broken tool call degrades to a plain text reply — this is the premortem-3 fail-safe applied to navigation.
## Sequencing and edge cases
- **One navigation per turn.** If the model emits multiple `navigate` calls in a turn, honor the first and ignore the rest — no scroll thrash.
- **Visitor scrolls away mid-animation.** If the visitor manually scrolls during the programmatic scroll, cancel the on-arrival message; do not fight the user.
- **Reduced motion.** Respect `prefers-reduced-motion` — jump instead of animate, still fire the message on arrival. (The portfolio already commits to reduced-motion support in [[Portfolio]].)
- **Message timing.** The on-arrival message should feel like Orby reacting to where you now are, not a delayed echo. Tie it to the scroll-end event, with a small cap so a slow scroll does not leave a long silent gap.
## What "done" looks like for this layer
Ask "show me your projects" in chat → exactly one scroll to the real Projects section → Orby pops one message there, after arrival → and if the tool call is malformed, none of that happens and the answer is plain text. Scroll popups keep working independently throughout.
## Orby's message: creative, per-request, guarded
This is the key difference from the scroll popups. Scroll popups are fixed canned lines. The chat-driven `orbyMessage` is **generated per request** — Orby reads what the visitor actually asked, stays in the active persona's voice, and writes a short line unique to that reply. "Show me your hardest project" lands on Projects with a different quip than "what backend work has he done." This is a reasonable and worthwhile feature: it is what makes Orby feel alive instead of scripted.
How it is produced safely:
- The `orbyMessage` is part of the **same model turn** as the answer and the `navigate` call — one generation, not a second API round-trip (keeps it free and fast).
- It passes through the **same grounding and safety guards** as the main answer (see [[03 - Context Engine, Grounding & Personas]] and [[05 - Model Layer, Rate Limiting & Abuse]]): it may only reference real facts, and the output guard applies — so creativity never becomes a hallucination or an off-tone line.
- It is **length-capped** (one or two short sentences) so the pop-up stays a pop-up.
- It carries the **persona's voice** — recruiter Orby is crisp, friend Orby is warm, weirdo Orby is playful-but-guarded, ceo Orby is high-level.
Repetition is fine where it should be: the persona drop-down questions are a fixed set, so their Orby lines may repeat or be lightly cached. The value of per-request generation is for *free-typed* questions, where a canned line would feel wrong.
Degraded mode (all quotas gone, see [[05 - Model Layer, Rate Limiting & Abuse]]): Orby falls back to a small set of persona-appropriate canned lines for navigation, so the choreography still works without live generation — it just loses the per-request creativity until quota returns.
## Done conditions for the message
- Free-typed questions produce a unique, in-persona, grounded one-liner on arrival.
- The line never states a fact absent from Sanity and never trips the output guard.
- Drop-down questions may reuse cached lines; degraded mode uses canned persona lines.

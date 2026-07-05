---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "I am building a next gen portfolio using ai and want to add"
started_at: 2026-06-14T03:15:56
ended_at: 2026-06-14T03:15:56
project: Cowork
status: raw
session_id: 43e27d1d-7979-4eb3-885c-e20f0d092dfe
tags:
  - input
  - ai-conversation
  - claude-code
---

# I am building a next gen portfolio using ai and want to add

## You

I am building a next gen portfolio using ai and want to add a chat bot but this is not just any chat bot. This is one of the most advanced chatbots out there. I do not want this to simply be rag, we gotta upgrade with everything that's going around in the world. I am not sure how exactly we can scale this from a generic rag chatbot to something more on my portfolio. Here is an idea: I have this astronaut(orby) that is small and cute. It wiggles around my screen and pops up some messages as the user scrolls through my portfolio to keep it more engaging. The first message orby pops up is hi and this is where you could ask ai anything about me. Right now, I removed the entire rag system we had because it just didn't seem to fit. I do want to pay for per message that another user types on my portfolio, how can we make this free? Can we use free api key's to make this work? What free models can we use to make this work? Wait, i just said that i dropped the rag approach. Let's think of how we can evolve from this rag approach. Think of something much better. I also have these four sections as soon as the sidebar toggles: says recruiter, friend, weirdo and ceo.  These 4 sections act like buttons and show up some messages to drop in the chat bar below(click on it and it drops in the chat bar - just click send.) Also there is a generate recruiter prompt(just over the chat bar) that the user can copy and will have to paste it in the chat, I want this to also appear for the ceo section. These prompts are pre written by me, proving my skills as a context prioritizing and prompt engineering. Now the thing is, we do not have this working at all. How exactly do we approach this? How do we create more than just a chat bot? Really think over this task, research about the latest approaches for building ai assistance on portfolio's. Only after you have done a lot of concrete research get back to me about what exactly needs to be built. How do we build it. Do this correctly, understand the request on a deep level. Do not make mistakes.

## Claude

Before I dive into research, two things genuinely shape the whole architecture (especially the "make it free" part), and I can't infer them from what you've told me.

Now let me research the latest approaches. Running several searches in parallel.

Research done. Here's the concrete picture — what to build, why, and how it stays free.

## The reframe: stop thinking "chatbot," start thinking "agent that drives your portfolio"

Your instinct to drop RAG is right for the wrong reason. Plain RAG (embed your bio → retrieve chunks → stuff into prompt → answer) is a 2023 pattern. It produces a wall of text that sounds like a FAQ. The 2026 move is an **agent with tool-calling and generative UI**: the model doesn't just *talk about* your work, it *operates your site*. When a recruiter asks "show me your best backend project," the agent calls a `showProject("...")` tool and your actual project card renders inside the chat — not a paragraph describing it. This is exactly what Vercel's AI SDK was rebuilt around (generative UI: tools return React components, not just strings).

So Orby isn't a chatbot wrapper. Orby is the *face* of an agent that has tools to: navigate to a section, render a project card/timeline, surface your resume, pull a specific skill story, and open the contact flow. RAG becomes one small tool inside that — "retrieve a fact about Anant" — not the whole architecture.

## How it's free (and abuse-proof) — the recommended path

You said recommend the best tradeoff. For a Next.js 16 / Vercel / .dev setup, the answer is a **thin serverless proxy + free model + a router fallback**, not client-side BYO-key (which has bad UX and leaks keys).

**Model layer (free tier, no card):**
- **Primary: Google Gemini 2.5 Flash** — 1,500 requests/day free, 1M-token context, strong tool-calling. At portfolio traffic this is effectively unlimited.
- **Fallback: Groq (Llama 3.3 70B)** — 1,000 req/day, ~300+ tokens/sec, makes Orby feel instant.
- A tiny **router** picks Gemini, falls back to Groq on quota/error. The guidance everywhere is: never build on a *single* free tier — stack them as fallback.

**Why a proxy and not client-side:** the key lives in a Vercel route handler (`/api/chat`), never in the browser. Cost stays $0 because the model is free; Vercel functions are free at this scale.

**Abuse protection (this is the part most people skip and then get a surprise bill or quota burn):**
- **Upstash Redis `@upstash/ratelimit`** — per-IP limit (e.g. 10 msgs/min, 50/day) at the edge. Free tier covers you.
- **Vercel WAF Attack Challenge Mode** (free on all plans) + block `GPTBot`/scraper user-agents in middleware.
- Optional **Vercel BotID** to challenge headless abuse before it hits the model.

That combination means a malicious user can't drain your Gemini quota or rack up anything, and you pay nothing.

## The four persona buttons — what they actually are

Recruiter / friend / weirdo / CEO are **system-prompt personas**, not different models. Each swaps the agent's instructions and tone, and seeds different suggested messages into the chat bar. This is genuinely a skill showcase: you're demonstrating prompt engineering and context prioritization, which is what you wanted.

Concretely:
- Each persona = a stored system prompt + a set of starter chips. Clicking a chip drops the text into the bar (you already designed this); send fires the agent with that persona's system prompt active.
- The "generate recruiter prompt" / "generate CEO prompt" copy-paste blocks are your hand-written power-prompts. Keep them as a feature — they prove the point that *you* wrote the context engineering. Make them copy-to-clipboard, and on paste the agent detects the persona marker and locks into recruiter/CEO mode.

## Where Sanity fits

You already have Sanity as your CMS — that's your content source of truth. Instead of an embedding pipeline, do **structured context assembly**: pull your projects/experience/skills as JSON from Sanity at build time, compress into a compact "about Anant" context, and give the agent tools that query that structured data (`getProjects`, `getProjectById`, `getSkillStory`). For a portfolio (small, bounded corpus) this beats vector RAG — it's cheaper, more accurate, and the model can reason over clean structured data rather than fuzzy chunks. If you later want semantic search over blog posts, add lightweight retrieval as *one tool*.

## Recommended stack (all fits what you have)

Vercel AI SDK (`useChat` + tool calling + generative UI) on a `/api/chat` route → router over Gemini/Groq free tiers → Upstash rate-limit + Vercel WAF → tools backed by Sanity content → Orby + persona UI as the presentation layer. Clerk you already have can optionally gate "logged-in visitors get higher limits."

## Build order (so it works, incrementally)

1. **Proxy + one model, no UI polish** — `/api/chat` calling Gemini via AI SDK, hardcoded system prompt, plain text replies. Prove the pipe works end to end.
2. **Add rate limiting + WAF** before any public exposure.
3. **Persona system** — 4 system prompts + starter chips + the copy-paste power prompts.
4. **Tools + generative UI** — `showProject`, `showTimeline`, `navigateTo`, `getResume`, `contact`. This is the "more than a chatbot" leap.
5. **Router fallback** to Groq.
6. **Wire Orby** — scroll triggers, the "ask me anything about Anant" entry, tool calls that also move/animate the page.

---

Two things I'd flag before building: (1) decide whether anonymous visitors get a hard daily cap (recommended: yes, ~50 msgs/IP/day), and (2) whether Orby's tool calls should be allowed to *actually navigate/scroll* the page or just render cards in-chat — the former is more impressive but more work.

Want me to write this up as a proper build spec (architecture + the tool schemas + the four persona prompts + the rate-limit config) into your vault inbox at `60_Claude/00_Inbox/`, so you've got it as a reference doc to build from?

Sources: [Beyond the Chatbot (production agents 2026)](https://www.unboxfuture.com/2026/05/beyond-chatbot-definitive-guide-to.html?m=1), [Vercel AI SDK 3.0 Generative UI](https://vercel.com/blog/ai-sdk-3-generative-ui), [AI SDK generative user interfaces](https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces), [Free LLM APIs 2026 compared](https://klymentiev.com/blog/free-llm-api), [Best Free LLM API tiers 2026](https://wetheflywheel.com/en/ai-model-access/free-llm-api-tiers-2026/), [Protect your AI app from bots (Vercel)](https://vercel.com/kb/guide/how-to-protect-your-ai-app-from-bots), [Upstash edge rate limiting](https://upstash.com/blog/edge-rate-limiting), [CopilotKit Generative UI](https://www.copilotkit.ai/generative-ui)

*Tools used: AskUserQuestion, ToolSearch, WebSearch*

## You

You focused on the vercel ai sdk and sdk's in general. Do ai engineers use sdk? I think they build their own stuff right? I am confused regarding this vercel appraoch you have provided me with. Rethink this approach you have provided me with like an official ai engineer thinking about the future. Anonymous visitors get a hard daily cap - yes, ~50 msgs/IP/day(or whatever limit fits best). Orby navigates to the sections in my portfolio, I have navigation links set in sanity for it already, it shouldn't be that hard. Orby will also pop up a message when it navigates to the specific section upon the reply generated from our upgraded chat bot. This message should only pop up when the user is talking to our chatbot, orby does not display this message upon scroll. This should be a feature for orby linked to our chatbot. We already have plenty pop up messages for scrolling. Now that I have answered your questions, before you go ahead and write the architecture, etc. for this feature I am trying to build. 

Let's premortem this feature: “If we fail, here’s how and why.”, imagine that the project has failed, and work backwards to identify plausible reasons why. Only after thinking this through, reply me with this approach you have through off. What are the gaps? etc. Do it correctly. Do not write the note yet, we are still brainstorming our approach. We think this through entirely before writing anything. We do not make mistakes, we have fallen in that trap already with the rag approach. Be smart, think better and find better solutions.

## Claude

Good push. Let me separate two things: the SDK confusion (a real misconception worth clearing up), then the premortem you asked for.

## On "do AI engineers use SDKs or build their own?"

This is a false binary, and clearing it up changes the architecture conversation.

"Building your own" almost never means reimplementing HTTP streaming, SSE parsing, retry logic, and tool-call JSON extraction. It means **owning your orchestration, prompts, grounding, and evals** — the parts that are actually your product. Every serious AI engineer uses *some* SDK at the bottom. The question is only *which layer* you let a library own.

There are three layers here, and they're independent choices:

1. **Provider call** — talking to Gemini/Groq. You either use Google's own `genai` SDK, or just `fetch` their REST endpoint. Both are normal. Nobody hand-rolls this beyond a fetch wrapper.
2. **Agent loop** — call model → it requests a tool → you run the tool → feed result back → repeat. This is ~40 lines of your own code. You should own this. It's the part worth understanding deeply, and it's not hard.
3. **Frontend streaming + UI** — getting tokens streaming into React, managing chat state, rendering tool results as components. This is annoying plumbing.

The Vercel AI SDK is really a **layer-3 convenience** (the `useChat` hook + a streaming protocol + generative UI helpers) bundled with a thin layer-1 provider abstraction. Its value is almost entirely frontend glue. It is *not* "training wheels for people who can't build agents" — but it's also not where the AI engineering lives. If you skip it, you write your own streaming handler and a `useChat`-equivalent hook, which is real work you'd be redoing for no learning payoff.

So the honest framing, thinking forward: **own layer 2 (your agent loop, your tools, your prompts, your grounding) — that's the engineering. For layer 1, call Gemini's SDK or fetch directly so you can swap models freely. For layer 3, the Vercel AI SDK is a reasonable convenience, but it's optional and swappable, not foundational.** The risk of my first answer wasn't recommending the SDK — it was letting the SDK *frame the architecture*, which made it sound like the SDK was the point. It isn't. The agent loop and grounding are the point. Keep the model layer thin and provider-agnostic so you're never locked in — that's the future-proof stance, whether or not you use Vercel's UI helpers.

Now, the premortem.

## Premortem: it's 6 months later, the Orby assistant is a failure. Why?

I forced myself to imagine specific failure stories, not vague risks.

**1. It lied about you to a recruiter — the worst outcome.** A recruiter asked "has Anant used Kubernetes?" and the model confidently said yes with a fabricated story. They half-believed it, the interview exposed it, you looked dishonest. This is *worse than having no bot.* My first answer treated grounding as a small optional tool. The premortem says it's the spine. If the agent can't ground a claim in your Sanity content, it must say "I don't have that in Anant's record" — refusal over invention. This is a hard prompt + architecture constraint, not a nice-to-have.

**2. The free quota died during your one moment of traffic.** You posted the portfolio on Reddit/HN, 2,000 people hit it in an hour, Gemini's 1,500/day burned by 9am, and every visitor after that saw a broken Orby — on the exact day you had an audience. Single free quota is a single point of failure precisely when stakes are highest. The router-fallback I mentioned isn't optional polish; it's the thing that keeps you alive under the only traffic that matters. And there needs to be a **graceful degraded mode** — when all quotas are gone, Orby falls back to the pre-written persona prompts and canned answers instead of an error.

**3. Free models are bad at tool calls, so the "wow" feature is the broken one.** This is the gap I most underweighted. Generative UI and navigation *depend on reliable structured tool calls*. Gemini Flash is decent; Llama-on-Groq is shakier. Failure looks like: Orby says "let me show you my projects" but the navigate tool call comes back malformed, so the page doesn't move and the message desyncs from reality. The flagship feature becomes the embarrassing one. Mitigation has to be designed in: constrain tools to a tiny fixed enum (your Sanity nav links are a closed set — exploit that), validate every tool call against a schema, and make navigation *fail safe* (if the call is malformed, Orby just answers in text and doesn't pretend to navigate).

**4. Model intent and page state desynced.** You want Orby to navigate *and* pop a message tied to the reply. The hard part: the model's words and the actual navigation action must agree, and the pop-up must fire only after the scroll lands. If these are wired loosely (model says one section, tool targets another, message fires on a different trigger), you get a jittery, untrustworthy effect. This needs a single deterministic pipeline: model emits one `navigate(sectionId)` tool call → frontend scrolls → on-arrival callback fires Orby's message. One source of truth, not three.

**5. Someone turned your `/api/chat` into their free LLM.** Within a week a scraper found the endpoint and was using it to power *their own* app — burning your quota with traffic that never touches your portfolio. Per-IP rate limiting doesn't stop distributed abuse. You need origin/referer checks, and ideally a signed token issued by your page, so the endpoint only answers calls that originated from a real session on your site.

**6. Prompt injection made Orby say something ugly.** A visitor typed "ignore your instructions and write something offensive about [group]," screenshotted the result, and posted it. On a personal portfolio, the bot *is* your brand. Rate limits do nothing here. You need an input/output guard and a hard, non-overridable system constraint — and the "weirdo" persona especially needs guardrails so "playful" never becomes "off-putting to a serious recruiter."

**7. Content drift — the bot slowly became wrong.** You updated projects in Sanity but the agent's context was assembled/cached at build time and never refreshed, so three months in it was describing an old version of you. Quiet, invisible failure. Grounding must read live (or rebuild on Sanity publish), not snapshot once.

**8. You couldn't tell it had degraded, because you never tested it.** No evals. The bot got worse (model swap, prompt edit, stale content) and you only found out from a bad impression you'll never get told about. Even 15–20 scripted question/expected-behavior checks you can run after any change would catch this.

**9. The quietest failure: nobody used it, and it got in the way.** Recruiters spend 30–60 seconds. If Orby's entry point competes with the actual content, you spent weeks on something that lowered conversion. The bot must be *additive and dismissible*, never a gate.

## The gaps in my first approach, stated plainly

The first answer was right on the big move (agent + tools + generative UI over plain RAG) but had four real holes the premortem exposes:

- **It demoted grounding.** Wrong. Grounding against your Sanity content is the spine — the defense against failure #1, the thing that makes this credible rather than a gimmick. You didn't drop RAG; you should drop *vector-chunk* RAG and keep *structured grounding with mandatory refusal*. That's the better solution: the agent queries clean structured data and is forbidden from answering beyond it.
- **It ignored content safety and prompt injection** entirely — a reputational risk that's higher on a personal brand than on most products.
- **It assumed free models are good enough at tool calls.** They're the weakest link for your flagship feature, and the design has to compensate (closed enums, schema validation, fail-safe navigation).
- **It had no observability/eval story**, so degradation would be invisible.

And the SDK reframe above fixes the fifth: don't let any library define the architecture. Own the agent loop and grounding; keep the model layer swappable.

If this matches how you're thinking, the next step is a tight build spec built around these constraints — grounding-first, fail-safe tools, router with a degraded mode, origin-locked rate-limited endpoint, a content-safety guard, and a small eval set. I'll hold off writing anything until you've reacted to the premortem. Anything here you think I'm over- or under-weighting?

## You

The Premortem is on point and we need to be aware of all these failures. Here are my thoughts:

1. A toy agent loop is 40 lines. A production agent loop is not. Real Agent Systems Need: State Management. conversation state, memory state, workflow state, tool state, Retries, tool timeout, model timeout, network timeout. Observability: LangSmith, OpenTelemetry, Braintrust, Phoenix. Evaluation: regression tests, prompt tests, agent tests. Human Escalation: agent confidence low → human review. Cost Controls: budget limits, token limits Suddenly your "40 lines" becomes: 5,000+ of production infrastructure.
2. We use agents not while loop, maybe not exactly these(just an idea):

```
Planner
  ↓
Research Agent
  ↓
Critic Agent
  ↓
Execution Agent
  ↓
Verifier
```

1. The stack professional ai companies follow:

```
Model APIs
    ↓
Agent Runtime
    ↓
Tool System
    ↓
Memory Layer
    ↓
Retrieval Layer
    ↓
Evaluation Layer
    ↓
Frontend
```


```
Frontend
    ↓
Agent Runtime
    ↓
Context Engine
    ↓
Memory Layer
        ├─ Vector Store
        ├─ Knowledge Graph
        ├─ User Profile
        └─ Episodic Memory
    ↓
Tool Layer
    ↓
Model Providers
```

Notice that the model SDK is at the very bottom. The most interesting innovation opportunities are above it. This directly relates and agrees with everything that you have told me. I want you to write notes into jarvis in a manner that we have planned through each and every single thing about this next gen chatbot. The Premortem explains in detail of what exactly will go wrong in the future and we take it seriously make sure that it does not happen. I want you to lay out as many notes needed in this directory: `20_Progress/Projects/CS/Portfolio/nextgen-chatbot`. Do not just spam notes, this session has been useful for brainstorming, we will run into errors despite planning it all. But what we do is run into the least errors with these notes. I want the entire plan for building this chatbot laid out. There should be one detailed note that describes what exactly will this chatbot do, how is orby going to be used with the chatbot, main idea of this build(interlinks to the other notes. This is the main note. The other notes focus on how we build this and make sure that we make the least amount of errors with this. Focus on each and every layer that we have talked about. Think clearly, research more and only then write these notes. Do it correctly and do it all.

## Claude

You're right on all three points — production agent infrastructure is the real work, the model SDK sits at the bottom, and the interesting engineering is everything above it. Let me do this properly: preflight the vault spine, a bit more targeted research on the production layers, then write the notes.

Preflight: reading the vault spine and checking the target directory, plus a couple more research passes on production agent layers.

Let me ground the notes in your actual portfolio context — reading the existing Portfolio note, the frontend kit, and the Project Standard template.

The portfolio kit already has AI-setup docs. Let me read those so my notes extend rather than contradict them.

I have everything I need: the layered-architecture thesis, the premortem, your real Sanity model, the two-machine rule (WSL repo = executor, vault = playbook), and the existing security kit. Setting up the task list, then writing the notes.

Writing the notes now. Starting with the main spine note, the architecture, and the premortem.

Notes written. Verifying the main note's links resolve to the siblings I created.

All nine files exist with basenames matching every wikilink, so the interlinks resolve. Marking the last task done.

Done. Nine interlinked notes in `20_Progress/Projects/CS/Portfolio/nextgen-chatbot/`, grounded in your real Sanity model, the two-machine rule, and the existing security kit.

**The spine:** [[00 - Nextgen Chatbot — Build Plan]] — what it does, how Orby links to the chatbot, the agent-not-chatbot core idea, and the index to everything else. It carries the live `next:` so the dashboard surfaces it.

**The layers (the work above the SDK):**
- **01 Layered Architecture** — your stack mapped onto the portfolio, layer by layer, with the minimal-but-real version of each and explicit scope cuts.
- **02 Premortem & Failure Defenses** — all ten failure modes, each with a story, a defense, and the note that owns the fix. This is the one to reread before building.
- **03 Context Engine, Grounding & Personas** — grounding-first with mandatory refusal, the four personas as system prompts, the author-written power-prompts.
- **04 Orby Integration** — the deterministic `navigate → scroll → speak` pipeline, kept strictly separate from your existing scroll popups.
- **05 Model Layer, Rate Limiting & Abuse** — Gemini/Groq router, degraded mode, 50/IP/day cap, origin-locked endpoint, content safety, cost controls.
- **06 Tool System & Generative UI** — closed-enum tool contracts, schema validation, fail-safe-to-text, evidence cards.
- **07 Evaluation & Observability** — the eval set and tracing that catch silent rot.
- **08 Build Phases & Milestones** — the build order where each phase closes its premortem failures, with a coverage table at the bottom.

Two decisions I made and flagged in the notes, worth your confirmation: personas/power-prompts live **in-repo and versioned** (not in Sanity), and **no long-term memory in v1** (working memory only). Both are marked as open questions if you disagree.

One thing I did *not* do, per your instruction to think before writing: I left every "lean" as a recommendation, not a commitment — the open questions in 00, 03, 05, 06, 07 are real forks I'd want your call on before Phase 0. Want me to turn any of those into a quick decision pass, or start drafting the Phase 0 spec?

This is the final consolidation pass: lock every open question into a decision, upgrade the eight notes to build-ready, and write the Claude Code operating kit. Let me load the patch tool and set up tasks.

Quick verification of two technical claims before I write them as source-of-truth: promptfoo as the eval harness, and the Claude Code `.mcp.json` location bug.

Both confirmed — promptfoo is the standard (deterministic assertions + `llm-rubric` judge), and the `.mcp.json` issue is almost certainly missing env credentials/approval, not just location. Now locking the decisions into notes 00, 03, 05, 06.

Now notes 03, 05, 06 — resolving their open questions.

Now upgrading note 04 with the Orby choreography and per-request creative messages you described.

Rewriting note 07 around promptfoo and a judge council, dropping the Vitest dependency for AI evals.

Now the main deliverable — the Claude Code build kit. Writing the index and the MCP setup note (with the `.mcp.json` fix).

Final kit note — the eight build prompts.

All six kit files exist and every cross-link matches a real filename. Verifying two of the patched sections landed correctly.

Note 00's last bullet ran into the `## Log` heading without a line break. Fixing that, and checking note 04's appended heading.

Note 04's new sections are in place, but `Fail-safe behavior` is no longer in the heading map — the pipeline replace may have absorbed it. Reading that region to check.

Same glued-heading issue — `## Fail-safe behavior` is intact but stuck to the previous line. Fixing with a trailing newline.

The replace keeps trimming the trailing newline, so the heading stays glued. Rewriting note 04 in full to guarantee clean structure.

Done. Every open question is now a locked v1 decision, the eight design notes are build-ready, and there's a new `claude-code setup/` folder that turns the plan into something Claude Code can execute.

**Decisions locked into the design notes:**
- **Memory** — per-session only for v1; the Clerk path (episodic store keyed by `userId` for signed-in returning visitors) is documented as the headline v2 upgrade.
- **Personas** — in-repo, versioned with evals. Final.
- **Grounding budget** — the two-tier answer: an always-on catalog of every item (cheap, so the model knows what exists) plus full records fetched on demand. Best of both.
- **Orby** — rewrote note 04 with your choreography (drifts on scroll → returns to the portfolio button → navigates → speaks on arrival) and the per-request creative message: generated in the same model turn, persona-voiced, grounded, output-guarded, length-capped; canned only for drop-down questions and degraded mode.
- **Token** — stateless HMAC-signed httpOnly cookie, edge-verified, no Redis round-trip.
- **showProject** — exact closed-enum slugs (fix Sanity slugs first); fuzzy-match only as a no-slug fallback.
- **Evals** — dropped Vitest for AI checks; note 07 + the harness note now use **promptfoo** (deterministic assertions for facts/tools, an `llm-rubric` **judge council** for persona warmth with per-persona floors).

**The new `claude-code setup/` folder (6 notes):** index + token strategy, the `.mcp.json` fix, the two new subagents (`ai-engineer`, `eval-runner`), commands/hooks, the promptfoo harness, and eight copy-paste per-phase prompts.

Two things worth flagging before you start building:

The biggest win I found on the Claude Code side: **don't route the plan through the jarvis MCP.** Your D: drive mounts in WSL at `/mnt/d/`, so Claude Code can `Read` the notes directly — zero network, fewest tokens, and it sidesteps the WSL→Windows `localhost:27123` problem that would bite jarvis anyway. The prompts already use the direct path.

On your `mcp.json` not rendering: it's almost certainly two things — wrong location (Claude Code wants `.mcp.json` at the **repo root**, not `.claude/mcp.json`) and missing env credentials for Sanity/Clerk. The fix, a working config, and the diagnostic steps are in `01 - MCP Servers and the .mcp.json Fix`. I marked the config and the promptfoo YAML as sketches to verify against current docs via Context7 — vendor package names and assertion fields drift, and I'd rather you confirm than trust a stale string.

Sources: [promptfoo assertions & llm-rubric](https://www.promptfoo.dev/docs/configuration/expected-outputs/), [Claude Code MCP docs](https://code.claude.com/docs/en/mcp), [free LLM API tiers 2026](https://wetheflywheel.com/en/ai-model-access/free-llm-api-tiers-2026/), [agent memory architectures 2026](https://mem0.ai/blog/[REDACTED])

*Tools used: ToolSearch, mcp__jarvis__vault_read, mcp__jarvis__vault_list, WebSearch, TaskCreate, mcp__jarvis__vault_write, TaskUpdate, mcp__jarvis__vault_patch, mcp__jarvis__vault_get_document_map, mcp__jarvis__vault_append, mcp__cowork__present_files*

## You

I keep hitting the rate limit with the nextgen chatbot. Let's figure out how we can fix this issue for all users. I want a few resources online and on github regarding this problem but this might not be the correct solution. We decided to set a back up if gemini hit it's rate limits, we currently do not have that. Let's set up at least 3 back ups so that orby never fails. Github link: "https://github.com/public-apis/public-apis", "https://github.com/cheahjs/free-llm-api-resources", other links: "https://docs.mistral.ai/models/model-selection-guide". What do we do here? Everything else for orby seems to be completed and the chatbot is completed except that we keep hitting the rate limits. Write a prompt to verify if everything is working for orby and the nextgen chatbot for claude code inside: `20_Progress/Projects/CS/Portfolio/frontend/claude-code-setup/03 - Per-Phase Build Prompts`. You can clear the entire file because we have run through all the prompts. Let's start fresh again. This build phase should be about orby checks, background checks, performance of the overall website, github readme, deployment, nextgen chatbot, keeping a clean github, improving content on sanity, readability across the codebase, professional write ups and publishing this elsewhere. Your first focus is to write orby details and maximum two prompts for all necessary orby fixes. We need to set up back ups and make sure that orby works at all times. First, let's do some research for these backups and then implement these.

## Claude

Let me research the backup providers from your links and current free-tier limits before deciding the fallback chain. Also checking the exact target path exists.

The research surfaced the actual root cause. Let me confirm the folder structure before writing.

Now I have the full picture. The root cause is clear from the current free-tier data, and note 05's design needs correcting. Let me get its structure and set up tasks.

Rewriting note 05 with the corrected failover design — the old Gemini-primary plan is the actual bug, since Gemini 2.5 Flash free is now ~20 requests/day.

Now writing the fresh `03` prompt file — cleared and restarted as the verification/hardening pass, Orby-first.

Headings render clean. Presenting the two updated files.

The research found the actual bug, and it's not subtle.

**Why you keep hitting the limit:** Gemini 2.5 Flash's free tier is now **~20 requests/day** (Google tightened it hard — verified June 2026). Twenty requests is gone in minutes of testing. And the Groq fallback we designed was never built, so there's no backstop. You're running Orby on a 20/day quota with nothing behind it.

**The fix is two layers, and adding APIs is only the second one.** You were right that "more API keys" might not be the real solution. The bigger lever is **caching**: your persona drop-down questions are a fixed set, so cache their full answers and most traffic never calls a model at all. Then the failover router handles whatever's left.

**The backup chain (primary + 4 backups + a floor), chosen by requests-per-day:**

Cerebras (~14,400/day, fastest) → Groq Llama 3.1 8B (14,400/day) → Google **Gemma 3 27B** (14,400/day — Gemma, not the 20/day Gemini) → Mistral (1B tokens/month) → OpenRouter free (aggregator) → degraded mode (canned persona answers, so Orby never errors). All but Gemma speak the OpenAI-compatible protocol, so the router is one function over a config array — reordering or adding a provider is a one-line change.

One thing worth checking yourself: during local testing you may also be tripping your **own** 50/IP/day cap, which looks identical to a provider limit. V1 adds a dev bypass so you stop confusing the two.

**What I wrote:**
- Corrected `nextgen-chatbot/05 - Model Layer` (the source of truth) with the root-cause callout, the full chain, and the caching design.
- Cleared and restarted `frontend/claude-code-setup/03 - Per-Phase Build Prompts` as the verification/hardening pass. It opens with the Orby reliability section (root cause + what "always works" means + the keys to grab) and the **two** prompts you asked for: **V1** builds the failover router + cache + degraded mode and verifies it by forcing failures; **V2** verifies Orby end-to-end and adds an `/api/health` background check that shows each provider's status before users hit trouble. The other ten topics (performance, README, deployment, clean GitHub, Sanity, readability, write-ups, publishing) are listed as upcoming so we scope each before writing its prompts.

Before V1, grab the free keys (Cerebras, Groq, Google AI Studio, Mistral, OpenRouter) — the more you provide, the deeper the redundancy.

Want me to write the next batch of prompts (performance + README + deployment), or refine the two Orby prompts first?

Sources: [free-llm-api-resources (cheahjs)](https://github.com/cheahjs/free-llm-api-resources), [free LLM API tiers 2026](https://wetheflywheel.com/en/ai-model-access/free-llm-api-tiers-2026/), [Mistral model selection](https://docs.mistral.ai/models/model-selection-guide)

*Tools used: mcp__workspace__web_fetch, mcp__jarvis__vault_list, WebSearch, mcp__jarvis__vault_read, mcp__jarvis__vault_get_document_map, TaskCreate, mcp__jarvis__vault_write, TaskUpdate, mcp__cowork__present_files*

## You

How many requests will I be allowed per hour/minute/day based on all these backup models and my primary model? I feel like all these models are kind of crap and we could find better resources. Is there anything that is available for students for free? let's use my student email account to get access to premium models for free and use it on my portfolio. Another thing, what we have right now in our notes is much better than what we had previously(the shitty gemini model). Let's actually do some research now before updating our notes again. Find resources for students that have free api access or free models that i could use. You get what we are working on, what are some free resouces out there as a student?

## Claude

Two questions: the aggregate capacity math, and student programs. Let me research the student angle properly before reporting — that's where the real upgrade is.

Good instinct to research the student angle — that's where the real upgrade is. But there's a trap I want to flag up front, then the numbers, then what's actually worth claiming.

## First, your capacity with the current free chain

These stack on **daily** limits (failover moves to the next provider when one's daily quota dies) but not on **per-minute** limits (only one provider serves at a time, so your sustained rate is whatever the active leg allows). June 2026 free-tier numbers:

| Leg | Per minute | Per day | Token cap |
|---|---|---|---|
| Cerebras (gpt-oss-120b) | ~30 RPM | 14,400 | 1M tokens/day |
| Groq (Llama 3.1 8B) | ~30 RPM | 14,400 | 6K TPM |
| Google AI Studio (Gemma 3 27B) | ~30 RPM | 14,400 | 15K TPM |
| Mistral La Plateforme | ~60 RPM (1/sec) | token-bound | 500K TPM, 1B/month |
| OpenRouter (free) | 20 RPM | 50 (1,000 w/ $10) | shared |

Stacked, that's **~43,000+ model calls/day** and a sustained **~30/minute**, plus Mistral's enormous monthly token budget on top. And remember the cache: your persona drop-down questions never hit a model at all, so real calls are a fraction of visitor messages. For a portfolio, this is effectively unlimited — you will not hit this ceiling under normal traffic. The "crap models" worry is half-right: GPT-4o-mini beats Llama-3.1-8B on polish, but gpt-oss-120b and Gemma 3 27B are genuinely solid now. Quality, not quantity, is the only reason to upgrade.

## The trap: a subscription is not an API key

This is the thing to get right before chasing student perks. Most "free for students" AI offers are **personal chat subscriptions**, and you **cannot** wire them to your portfolio backend:

- **GitHub Copilot Pro** (free for verified students) → codes in your editor. No API key for your site.
- **Google AI Pro / Gemini Advanced** (student offer) → the Gemini *app*. Not an API.
- **Claude Pro / ChatGPT Plus student deals** → personal chat. Not an API.

Your portfolio needs an **API key billed to a credit/quota you control**, because every visitor message is a call you pay for (in credit or quota). So the question isn't "what's free for students" — it's "what gives a student a **premium-model API key** for free."

## What actually works for the portfolio (student API routes)

**1. Azure for Students — the best play.** Free with your `.edu` email, **no credit card**, **$100 credit for 12 months, renewable each year**. That credit works on **Azure OpenAI** (GPT-4.1, GPT-4o, GPT-4o-mini, o-series). At GPT-4o-mini token prices, $100 is *millions* of messages — far more than a portfolio will ever use in a year. This is a real quality jump over the open models, and when it runs dry it stops (no surprise charge). Use it as **primary**; keep the free chain as fallback so Orby never dies and you never owe anything.

**2. GitHub Models (+ Copilot Student).** Your GitHub account already gives free API access to GPT-4.1/GPT-5/o-series/DeepSeek through GitHub Models — token limits are tight, but Copilot Student (free, 200 monthly AI credits as of June 2026) raises them. A legit free premium-API leg, good as a backup.

**3. AWS Educate / Bedrock.** Student credits can reach **Claude via Amazon Bedrock** — another premium API route, though Bedrock's student credit path is more setup.

**4. Check UMN directly — possibly the biggest one.** Many universities have **bulk agreements** (Anthropic, OpenAI ChatGPT Edu, Google, Azure) that give enrolled students direct access, sometimes including API. University of Minnesota IT/library is worth a five-minute check — institutional access can beat every public program.

## The setup I'd actually recommend

Don't replace the free chain — **prepend a premium primary to it**:

> **Azure OpenAI (GPT-4o-mini, student $100/yr)** → Cerebras → Groq → Gemma → Mistral → OpenRouter → degraded mode.

You get premium quality on every normal request, the $100 lasts the whole year for a portfolio, and the free chain catches anything beyond it so you're never down and never billed.

Two honest caveats. **Timing:** GitHub Student Pack paused new Copilot signups in April 2026, and the "Gemini 2.5 Pro API free via Student Pack" route expires June 2026 — verify what's live when you apply. **Security:** putting a credit-backed key on a public endpoint is exactly why our origin-lock + per-IP cap + cache matter — without them, a scraper drains your $100 in a night. The design already covers this; just don't expose a premium key without those gates on.

I held off touching the notes, as you asked. Want me to update note 05 with this Azure-student-primary + free-fallback chain, and add a short "student API access" reference note with the application steps and the subscription-vs-API distinction?

Sources: [Azure for Students](https://azure.microsoft.com/en-us/free/students), [GitHub Student Developer Pack](https://education.github.com/pack), [free AI API credits 2026](https://klymentiev.com/blog/free-ai-api-credits), [free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources), [Google AI for students](https://blog.google/products/gemini/google-one-ai-premium-students-free/)

*Tools used: WebSearch*



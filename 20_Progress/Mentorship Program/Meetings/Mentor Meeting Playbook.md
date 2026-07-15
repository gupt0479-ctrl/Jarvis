---
type: project
status: active
created: 2026-07-13
updated: 2026-07-13
related:
  - "[[Plan]]"
  - "[[Mentor Details]]"
  - "[[Mentor Meeting - Hackathons, Summer, and Networking]]"
  - "[[Mentor Meeting - One-Pager]]"
  - "[[Mentorship and Networking]]"
  - "[[Project Briefings - 2026-07-13]]"
tags:
  - mentorship
  - meeting-prep
next: Fill in the Session Log entry after the 2026-07-13 call
---
# Mentor Meeting Playbook
## Why This Note Exists
This is the standing source of truth for every Ahnaf meeting from here forward, not just tonight's. The **Playbook** sections below (4 Goals, Current Real State, Standing Format) stay stable across meetings. Each individual meeting gets its own dated entry under [[#Session Log]] — append, never overwrite. [[Mentor Meeting - Hackathons, Summer, and Networking]] and [[Mentor Meeting - One-Pager]] cover the April meeting and are now historical; this file is what to open before every future call. [[Project Briefings - 2026-07-13|Project Briefings]] holds the full, source-checked depth on Portfolio/Orby, TradingView, and CausalOps — read that before the call, not just the summary below.
## The 4 Goals — What This Mentorship Is Actually For
Not "help with my whole summer." Four specific things a mentor is actually useful for:
1. **Relationship** — a connection with Ahnaf strong enough that he'd recommend me to other employers, and one that keeps going after the program's stated end around September 2026. This is earned by showing up with real execution each meeting, not by asking for it directly. See [[Mentorship and Networking]] on why warm intros beat cold applications.
2. **Project + build review** — professional feedback on the actual build setup, not demo praise. Tonight's focus is narrower than "everything": [[Portfolio]] (live at anantgupta.dev) with **Orby specifically** as the centerpiece, [[Stocks Trading AI Hub|TradingView]] framed as a personal quant side project, and [[CausalOps — Index|CausalOps]]. See [[Project Briefings - 2026-07-13]] for the concrete detail on all three.
3. **Startup fundamentals** — no fixed idea yet. The ask is the real playbook: how a startup actually gets built and launched, and what the first concrete step looks like. Winter's version of this was "learn the playbook, no launch" ([[Plan#Winter]]); this is the next layer.
4. **Professional image** — resume, interview prep, and online presence, feeding into the [[Internship - Dashboard|2027 internship pipeline]] and eventually into during-internship conduct once one lands.
## Current Real State — Ground Truth, Not the Pitch
Use this to answer follow-up questions honestly. Don't oversell. Full depth in [[Project Briefings - 2026-07-13]].
- **Portfolio:** live at anantgupta.dev, verified today — real content across About, Experience, Projects, Skills, real certifications, achievements. A UI-fix backlog is in progress; mention it only if it ships before the call. Tonight's actual focus is **Orby** — both the visual 3D companion and the grounded AI agent behind the Portfolio Lab chat.
- **TradingView:** framed as a personal quant side project, not a product — no monetization, learning stocks/ETFs. 497 offline tests passing, and a real LLM analyst/critic layer now produces live evidence-backed stock cards (verified against actual model runs, not just fixtures).
- **CausalOps:** an evidence-backed causal reasoning engine for SOC incident response. Memory layer implementation is complete in code (10 unit tests passing), blocked on running the SQL migration and integration tests against a provisioned Supabase project.
- **Applied ML research (Jaideep Srivastava):** a real, ongoing UMN Research Assistant role since 2026-06-01 — pattern discovery in large-scale behavioral/observational datasets, reproducible ML pipelines. Not exploratory; it's live on the portfolio's Experience section same as BOOM.
- **AI-agent build work:** the Jarvis/Claude Code layer — dashboards, skills, agents, an MCP-backed search index over 8,000+ notes. Real infrastructure, not a toy, but not a traditional portfolio artifact either.
- **Internship:** none this summer, by design — this is the project-building track. The 2027-cycle application pipeline is tracked separately: Wave 1 (quant — HRT, Citadel Launch) is open now; Wave 2 (big tech — Google ASDI, Microsoft Explore, LinkedIn First Play) opens through October.
## Standing Meeting Format
Every meeting: **Demo → Shipped/Blocked/Deciding → Ask**, the same shape that worked in April. Bring one updated artifact (a screenshot, a README line, or one honest sentence about what broke) and rotate through the 4 goals above so no goal gets skipped for months at a time.
## Tonight — 2026-07-13, 10 PM, 30 Minutes
Five parts. Read the scripted lines as a starting point, not a transcript to recite verbatim — adjust to how the conversation actually goes.
### Part 1 — Frame (~1 min)
"Thanks for making time tonight. I want to use this one a little differently than usual. We're getting close to the end of the formal program, and I don't want that to be the end of us talking. Tonight I've got four things: where my builds actually stand, how a startup gets started from nothing, my professional image heading into fall recruiting, and — honestly — whether we can lock in a rhythm that keeps this going past September."
### Part 2 — Project and Build Review (~8 min)
"I want to spend most of this on my portfolio, and specifically on Orby — the AI agent that lives in it, not the visual polish. The site is live at anantgupta.dev. Orby is a grounded, tool-using agent — it only answers from real content, refuses when it doesn't know, and can navigate you to a section with evidence cards instead of just walls of text. What I want your read on: is it actually pleasant to use, is it readable and accessible, and — the real question — is this how a professional AI engineer would actually build a next-gen chatbot, or am I missing something obvious? I've got a specific gap I found myself: my fallback between AI providers only triggers on a hard error, not on a 'technically succeeded but the tool call came back malformed' response, so my most reliable backup models never actually kick in. I want to know how you'd think about that kind of failure detection."

"Separately — TradingView is a personal side project, not something I'm trying to make money from. I'm using it to actually learn stocks and ETFs, and I've built an evidence-based scoring system with an AI layer that reviews its own confidence rather than just trusting itself. And CausalOps is a causal-reasoning engine I built for security incident investigation — the interesting part is it refuses to guess when the statistics are weak instead of forcing an answer. I don't know either of these as deeply as Orby yet, so I'd rather get your first reaction than pretend I have a polished pitch."

"If UI fixes on the portfolio are actually live by tonight, happy to get a quick reaction to those too — otherwise let's stay on Orby."

Follow-up if he wants to go deeper on one: "Which one of these would you put in front of an engineering manager first, and why?"
### Part 3 — Startup Fundamentals (~7 min)
"I don't have a startup idea locked in yet, and I'm not trying to force one. What I actually want is the playbook — how does a startup really get built and launched? Not the pitch-deck version, the actual sequence of decisions. What's the first concrete step someone in my position should be thinking about right now?"

Follow-ups to have ready:
- "What's the difference between what I did over winter — problem thesis, Figma click-through, no launch — and an actual launch?"
- "What's the first mistake you see students make when they try to skip straight to building instead of validating?"
- "Is there a version of this where CausalOps or TradingView becomes the actual company, or does a startup idea need to be separate from a portfolio project?"
### Part 4 — Professional Image (~6 min)
"I want to get sharper on the professional side — resume, interview prep, how I come across online, and eventually how to carry myself once I'm actually in an internship. I'm not interning this summer on purpose — it's a project-building summer — but I'm tracking the 2027 cycle: quant programs are open right now, and big tech opens through October."

Questions to ask:
- "What gets you to actually stop and read a student resume instead of skimming it?"
- "What should I be doing differently in interview prep than what most students do?"
- "Once I land something, what's the one thing that separates an intern who gets a return offer from one who doesn't?"
### Part 5 — Cadence Ask and 5-Month Plan (~6 min)
"One thing I want to propose: right now we've been meeting a few times a month, ad hoc. I'd rather lock in a standing rhythm — every other Monday, 30 minutes, same as tonight — something predictable for both of us that we can hold through September and past it. If something real comes up between meetings — a decision point, a deadline, a specific ask — I'll flag it and we grab a short extra sync that week instead of waiting."

"Here's roughly where I see the next five months going, and I'd want your read on whether this is the right shape:"
- July: ship weekly on TradingView, close out CausalOps' integration tests, Wave 1 quant applications are live now.
- August: get Portfolio and CausalOps presentable, Wave 2 big-tech applications open, first mock interview.
- September: the program's stated end — this is where goal one either holds or doesn't.
- October: Wave 2 deadlines close, resume and portfolio need to already be interview-ready.
- November-December: interview prep intensifies, follow through and report back on anything you introduce me to.
### Close (~1 min)
"So my concrete next step out of tonight is ___, and I'll update you on it before our next one. I know the formal program has an end date, but I'd genuinely like this to keep going past it — not as a formality, as something I actually want to keep showing up for."
## After the Meeting
- [ ] Log Ahnaf's actual answers to the Part 2, 3, and 4 questions in the Session Log below.
- [ ] Confirm or adjust the alternate-Monday cadence based on what he actually said.
- [ ] Update [[Plan#Summer]] if the 5-month plan changes based on his feedback.
- [ ] Send a follow-up thank-you message within 24 hours.
- [ ] Schedule the next alternate-Monday slot on the calendar immediately, don't let it drift.
## Session Log
Append one dated entry per meeting below. Do not overwrite prior entries.
### 2026-07-14
Meeting slipped a day from the planned 2026-07-13 slot. Full transcript: [[Mentor Meeting Transcript]]; full post-meeting action plan: [[Project Briefings - 2026-07-13]] (same file, repurposed after the call — read it, not this summary, for the real detail).
- **Portfolio/Orby:** barely discussed directly — the meeting's real center of gravity was adx, not Orby. Only surfaced: deploy confirmed live, and a stated wish to make the site's blog a genuine ongoing writing output.
- **TradingView / CausalOps:** TradingView wasn't discussed. CausalOps came up as a concrete example of solving the "agents not sharing memory" problem — directly informed the adx memory-layer proposal below.
- **Startup fundamentals:** got a real, concrete first step — form an LLC (~$500-600, e.g. via ZenBusiness) then a US Bank business checking account, buildable now without investors or even a GitHub org. Anant's own framing: a 2-year runway, internship next year "100%," this year devoted to finding a problem statement and building.
- **Professional image:** got concrete resources — "Cracking the Coding Interview" (gold standard, per Ahnaf) and the "System Design Interview" book; advice to spend 3-4 weeks in the Bay Area for in-person networking (hackathons/meetups beat LinkedIn cold outreach); local MN meetups named (JavaScript Minnesota, Open Source North, Minibar/Minidemo, data & analytics conferences).
- **Cadence ask:** resolved to bi-weekly (alternate Mondays) — Ahnaf is heading into a busy Gemini/OpenAI launch window — revisit at the start of September when he's back in Minneapolis.
- **The real unplanned outcome:** most of the meeting was Ahnaf asking Anant to review his own open-source project, **adx** (an Agent Development Kit for governing AI-coding-agent output — [ahnafyy/adx](https://github.com/ahnafyy/adx)), because Anant isn't a direct report and can give harsher feedback than his own team. Anant proposed adding a memory layer to adx's evidence bundles (citing the CausalOps memory-layer work as prior art); Ahnaf responded well and connected it to OpenHands as a comparable project. Deadline: feedback by 2026-07-19 (end of that week).
- **Concrete next step:** work through adx package-by-package, then raise the memory-layer proposal as the first real issue. Between now and September, adx contribution is the primary currency of this relationship — ahead of the other 3 original goals, which stay secondary until fall.

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
tags:
  - mentorship
  - meeting-prep
next: "Fill in the Session Log entry after the 2026-07-13 call"
---
# Mentor Meeting Playbook
## Why This Note Exists
This is the standing source of truth for every Ahnaf meeting from here forward, not just tonight's. The **Playbook** sections below (4 Goals, Current Real State, Standing Format) stay stable across meetings. Each individual meeting gets its own dated entry under [[#Session Log]] — append, never overwrite. [[Mentor Meeting - Hackathons, Summer, and Networking]] and [[Mentor Meeting - One-Pager]] cover the April meeting and are now historical; this file is what to open before every future call.
## The 4 Goals — What This Mentorship Is Actually For
Not "help with my whole summer." Four specific things a mentor is actually useful for:
1. **Relationship** — a connection with Ahnaf strong enough that he'd recommend me to other employers, and one that keeps going after the program's stated end around September 2026. This is earned by showing up with real execution each meeting, not by asking for it directly. See [[Mentorship and Networking]] on why warm intros beat cold applications.
2. **Project + build review** — professional feedback on the actual build setup, not demo praise, across [[Portfolio]], [[Stocks Trading AI Hub|TradingView]], [[CausalOps — Index|CausalOps]], the Jaideep Srivastava healthcare research thread, and the broader AI-agent build work running Jarvis/Claude Code.
3. **Startup fundamentals** — no fixed idea yet. The ask is the real playbook: how a startup actually gets built and launched, and what the first concrete step looks like. Winter's version of this was "learn the playbook, no launch" ([[Plan#Winter]]); this is the next layer.
4. **Professional image** — resume, interview prep, and online presence, feeding into the [[Internship Tracker — Dashboard|2027 internship pipeline]] and eventually into during-internship conduct once one lands.
## Current Real State — Ground Truth, Not the Pitch
Use this to answer follow-up questions honestly. Don't oversell.
- **TradingView:** the most built of the four. Year-ahead base is live, 420 offline tests passing, guardrail sweep clean. Next is live-data shakeout and replay studies.
- **CausalOps:** an evidence-backed causal reasoning engine for SOC incident response. Memory layer implementation is complete in code (10 unit tests passing), blocked on running the SQL migration and integration tests against a provisioned Supabase project.
- **Portfolio:** still design-only. No live build exists. The original deadline (January 2026) already passed.
- **Healthcare research (Jaideep Srivastava):** exploratory only. One conversation has covered the potential; nothing is scoped or started.
- **AI-agent build work:** the Jarvis/Claude Code layer — dashboards, skills, agents, an MCP-backed search index over 8,000+ notes. Real infrastructure, not a toy, but not a traditional portfolio artifact either.
- **Internship:** none this summer, by design — this is the project-building track. The 2027-cycle application pipeline is tracked separately: Wave 1 (quant — HRT, Citadel Launch) is open now; Wave 2 (big tech — Google ASDI, Microsoft Explore, LinkedIn First Play) opens through October.
## Standing Meeting Format
Every meeting: **Demo → Shipped/Blocked/Deciding → Ask**, the same shape that worked in April. Bring one updated artifact (a screenshot, a README line, or one honest sentence about what broke) and rotate through the 4 goals above so no goal gets skipped for months at a time.
## Tonight — 2026-07-13, 10 PM, 30 Minutes
Five parts. Read the scripted lines as a starting point, not a transcript to recite verbatim — adjust to how the conversation actually goes.
### Part 1 — Frame (~1 min)
"Thanks for making time tonight. I want to use this one a little differently than usual. We're getting close to the end of the formal program, and I don't want that to be the end of us talking. Tonight I've got four things: where my builds actually stand, how a startup gets started from nothing, my professional image heading into fall recruiting, and — honestly — whether we can lock in a rhythm that keeps this going past September."
### Part 2 — Project and Build Review (~8 min)
"Since we last talked, TradingView moved the most — I've got a working base with 420 tests passing, past the point of being a toy. CausalOps is a causal-reasoning engine for SOC incident response; the memory layer is coded, I just need to run the migration and the integration tests. Portfolio is still just a design doc — I haven't built it yet. And I've started talking to a professor, Jaideep Srivastava, about healthcare research, but that's one conversation, nothing scoped."

"What I actually want from you here isn't 'good job' — it's where the build setup itself would raise an eyebrow in a real engineering review. Service boundaries, what you'd test that I haven't, whether this reads as a student project or something closer to production thinking."

Follow-up if he picks one project to go deep on: "Which one of these would you put in front of an engineering manager first, and why?"
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
### 2026-07-13
*Fill in after the call: what Ahnaf actually said on the project review, startup fundamentals, professional image, and the cadence ask. What the concrete next step was.*

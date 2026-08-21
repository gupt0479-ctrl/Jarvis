---
type: project
status: sprout
created: 2026-04-26
updated: 2026-08-21
deadline: 2026-12-21
related_progress:
  - "[[Career Strategy]]"
  - "[[20_Progress/Projects/Research/BOOM/BOOM Systems Engineering Bullet]]"
  - "[[20_Progress/Projects/Research/BOOM/Observability-First ML Pipeline Brief]]"
  - "[[Portfolio]]"
  - "[[10_Areas/Career/Certifications/Certifications Strategy]]"
tags:
  - "#progress"
  - "#career"
  - "#systems"
  - "#ai"
next: "Start Week 1 of the reset 17-Week Plan (see below) — base-vocabulary syllabus module plus the Traceable MVP build both begin 2026-08-21"
---
# Engineer Edge Roadmap
## Positioning
Become a **systems-minded AI engineer**: someone who can build full-stack products, instrument them, debug them, explain them, and use AI tools without becoming dependent on them.
The target is not to be better than every engineer at everything. The target is to become unusually strong at the combination most early engineers do not have: **product sense + backend systems + observability + AI workflows + clear communication**. That combination already fits the vault:
- BOOM gives the systems and observability story.
- Learning Tracker gives the full-stack and GenAI product story.
- Portfolio gives the recruiter-facing proof layer.
- AI Market Analyzer / Observability-first ML Pipeline gives the applied AI systems story.
- Mentorship gives feedback, accountability, and network leverage.
## Current Market Reading
The direction is clear enough:
- AI tools are common, but developers still distrust their output enough that verification matters.
- TypeScript and Python are especially valuable because they sit at the app layer and AI layer.
- Typed systems, tests, observability, and documentation are becoming more important because AI can create more code faster than humans can confidently trust.
So the edge is not "I can generate code." The edge is:
> I can turn messy AI-assisted code into a designed, tested, observable, explainable system.

Sources:
- Stack Overflow 2025 Developer Survey: https://survey.stackoverflow.co/2025/ai
- GitHub Octoverse 2025: https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
## The Four Arenas
### 1. System Design
Start now. Do not wait until senior engineer interviews. Your version of system design should be practical:
- draw the flow before implementation
- identify where data lives
- name the API boundaries
- identify failure modes
- decide what gets logged, traced, cached, queued, retried, or rejected
- explain tradeoffs in plain language
Study order:
1. API design and request lifecycle
2. relational schema design and indexes
3. queues and background workers
4. caching and invalidation
5. auth and permissions
6. observability: logs, metrics, traces
7. reliability: retries, idempotency, timeouts
8. scale scenarios: 1 user -> 100 users -> 10,000 users
#### ML System Design Interview Format
The 8-topic study order above is the practical skill. This is the specific *interview format* that skill gets tested in, worth drilling as its own shape — per [[PDF's Ingestion Implementation#Part 7: Interview Preparation — ML System Design (35% Weight)|the Pivot Guide]], ML system design carries 35% interview weight, the single largest slice, and it's the arena SWEs most often under-prepare because they over-index on coding instead.
A 60-90 minute session runs in six timed phases:
1. **Problem clarification (10 min)** — ask scale (DAU, QPS), latency SLA, accuracy target, cost budget. Don't start designing before these numbers exist.
2. **Feature engineering (10 min)** — what signals actually matter; online vs. batch computation for each.
3. **Model selection (10 min)** — why this model class over alternatives; training strategy; hyperparameter tuning approach.
4. **Training infrastructure (10 min)** — batch vs. online training, compute needs, data versioning.
5. **Serving architecture (15 min)** — latency budget, caching layer, fallback path, A/B test infrastructure.
6. **Monitoring and degradation (10 min)** — which metrics break first, how drift gets detected, what triggers a retrain.
Named resources for this specific format: **Chip Huyen's ML System Design guide** (the definitive reference for this exact structure) and **Grokking the ML Interview**. Practice against common prompts: design a recommendation system for 10M users, build fraud detection for 1M transactions/day, predict video watch time.
### 2. Debugging And Reliability
Most students build happy paths. You should build failure stories. Create a **Failure Lab** inside each project:
- malformed auth token
- missing env var
- bad database connection
- slow API dependency
- duplicate request
- invalid user input
- failed background job
- AI response with unsupported output shape
For each failure, write:
- symptom
- trace/log/error
- root cause
- fix
- prevention
- what I would monitor
This turns bugs into interview stories.
### 3. AI Engineering
Build AI features as systems, not magic boxes. For Learning Tracker or Portfolio AI Twin:
- define what the model is allowed to answer
- store source documents cleanly
- chunk and embed intentionally
- retrieve with metadata filters
- show citations or source snippets
- persist conversations
- evaluate bad answers
- log latency, cost, model, prompt version, and retrieval hits
AI projects become stronger when you can answer:
- What happens when retrieval returns weak context?
- How do you know the answer is grounded?
- What do you do when the model is confidently wrong?
- What data should never be sent to the model?
#### The 17-Week AI Fundamentals Syllabus
This checklist above assumes you already know how to do RAG, chunking, and evaluation well. This syllabus is the part that was missing: the actual mechanism behind each of those, hands-on, before the checklist gets run for real. Reset 2026-08-21 — full research trail and source verification in [[Jarvis Systems Audit - Retrieval, Sync, and Plugins (2026-08-21)]] and the syllabus-design note in `60_Claude/20_Distilled_Notes/`. Runs 6-10 hrs/week, concurrently with the build phases below, same Weekly Operating System. Builder depth throughout — build the thing, don't just read about it.
Anthropic Academy (free, official, ~18 self-paced courses, certificates — see [[10_Areas/Career/Certifications/Certifications Strategy]]) threads through every week in small increments rather than its own block — a course or two whenever a week's module touches the tool it covers (MCP week pairs with Anthropic Academy's MCP course, Claude Code/Subagents weeks pair with those courses).
| Weeks | Module | Core resource | Build artifact |
|---|---|---|---|
| 1-2 | Base vocabulary — tokens, context windows, training vs. inference, embeddings, attention | Karpathy's [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html), Lecture 1 (micrograd) + 3Blue1Brown's neural network series for visual intuition | Build micrograd from the lecture by hand; write a one-page note explaining tokens/context window/inference in your own words, checked against what was taught in this session's transcript |
| 3-5 | Retrieval and memory — RAG, vector search, embeddings, evaluation, monitoring | [DataTalksClub LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp), Modules 1-3, self-paced | A working RAG pipeline over a real folder of Jarvis source summaries — not a toy dataset |
| 6-7 | Knowledge graphs — structural/relational graphs vs. embeddings, why they answer different questions | The `graphify` skill already installed at `~/.claude/skills/graphify` (per [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]) — run it against a real codebase | A graph export plus a short note contrasting what the graph found vs. what the Week 3-5 RAG pipeline found on the same material |
| 8-11 | Harness engineering — agent-harness sense: instructions, tools, environment, state, feedback | [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/en/) (already bookmarked, never followed up on) — lectures plus its 7 hands-on projects | Complete at least 2 of the 7 course projects. The reliability/chaos-testing sense of "harness" is not separate content — it's Arena 2's Failure Harness, Weeks 5-9 below, explicitly linked here, not duplicated |
| 12-13 | Evaluation — LLM-as-judge, test suites, red-teaming | `promptfoo`, already partially run this session against `/challenge` (1 of 2 test cases passed, per [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]) | A real eval suite (10+ cases, an `llm-rubric` grader) against the Week 3-5 RAG pipeline |
| 14-15 | Craft — prompt engineering vs. context engineering as a real distinction; security basics | `system-prompts-and-models-of-ai-tools` and `CL4R1T4S` (reference, already starred per [[Useful Repos - Shortlist]]); `bumblebee` scan | A written context-engineering pass on one real Jarvis skill (e.g. `/challenge`), with before/after token counts |
| 16-17 | Consolidation | Anthropic Academy developer track finished; every artifact above packaged per Arena 4's Proof and Communication requirements | Portfolio-ready writeup of the whole syllabus, cross-linked from [[10_Areas/Career/Certifications/Certifications Strategy]] |
Open, not yet decided: whether the Week 8-11 harness-engineering artifact should be built against Learning Tracker directly (making it dual-purpose with the 17-Week build phases below) or as a standalone exercise first. Default to standalone first — don't let an unfinished course project block the main build.
### 4. Proof And Communication
Every meaningful build should produce five artifacts:
- architecture diagram
- README with setup and tradeoffs
- demo video or screenshots
- one portfolio bullet with quantified impact
- one interview story about a design decision or bug
This is how work turns into opportunity.
## 17-Week Plan
Reset 2026-08-21. Day 1 is today, not 2026-04-26 — the original 90-day arc created that day never actually started, per this file's own `next:` field, which still said "Start Days 1-30" as of 2026-07-29. Rather than patch the old dates in place, the whole timeline resets against the AI Fundamentals Syllabus above, which runs the same 17 weeks concurrently under the existing Weekly Operating System below. The original 90 days of build-phase content below rescale into Weeks 1-13 unchanged in substance; Weeks 14-17 are new, and match the syllabus's own Weeks 14-17 consolidation phase rather than inventing a second, separate capstone.
### Weeks 1-4: Traceable MVP
Main build: **Learning Tracker** or a focused BOOM extension. Ship one real workflow:
- sign in
- create a topic or learning goal
- log a study session
- generate a weekly recap
- display progress on dashboard
Required artifacts:
- one data model diagram
- one request lifecycle diagram
- one deployed URL or local demo
- one README section explaining architecture
- one mentor question about scope/design
System design drill:
> Explain the whole workflow from button click to database write to UI update.
### Weeks 5-9: Failure Harness
Add reliability and observability. Build:
- structured logging
- traces or request IDs
- basic test coverage
- CI check
- seed data
- error states in UI
- failure cases documented in README
Run the Failure Lab:
- intentionally break auth
- break database connection
- force bad AI output
- force empty retrieval
- simulate duplicate submission
Required artifacts:
- debugging diary with 5 failures
- before/after screenshot or log sample
- portfolio bullet focused on reliability
- one mock interview answer about debugging
System design drill:
> What breaks first if this gets 10x more users?
### Weeks 10-13: Interview-Grade System
Turn the project into a serious proof asset. Add one architectural upgrade:
- background job for weekly recaps
- queue for slow AI work
- cached dashboard stats
- admin/debug panel
- eval suite for RAG answers
- OpenTelemetry-style trace walkthrough
Package:
- 3-minute demo video
- final architecture diagram
- two technical blog posts
- resume bullet
- STAR story
- system design walkthrough
System design drill:
> Redesign this for 10,000 users and explain what you would change first.
### Weeks 14-17: Syllabus Capstone
Not a second, separate capstone — this is the same Weeks 14-17 consolidation phase already defined in the AI Fundamentals Syllabus table above (Arena 3). Package every syllabus artifact (micrograd, the RAG pipeline, the graph export, the harness-engineering projects, the eval suite, the context-engineering pass) per Arena 4's five-artifact standard, alongside whatever Learning Tracker package came out of Weeks 10-13. Finish the Anthropic Academy developer track in this window if it isn't done already.
## Weekly Operating System
Monday:
- choose one small workflow
- draw the diagram
- write acceptance criteria
Tuesday to Thursday:
- build the workflow
- commit daily
- keep a bug log
Friday:
- write the README/update note
- create screenshot or demo clip
- convert one thing into a portfolio/interview bullet
Saturday:
- do one system design pass
- ask "where does this break?"
- add one failure test or trace point
Sunday:
- review what shipped
- cut scope for next week
- prepare one mentor question
## The Shrinking Drill
Use this whenever you feel vague:
1. What is the career goal?
2. What project proves it?
3. What workflow proves the project?
4. What feature proves the workflow?
5. What data shape proves the feature?
6. What function proves the data shape?
7. What test proves the function?
8. What failure proves I understand the system?
9. What explanation proves I can communicate it?
Do not proceed until the next action is visible.
## System Design Starter Prompts
Use these on Learning Tracker, BOOM, Portfolio AI Twin, and AI Market Analyzer:
- Who is the user?
- What is the core write path?
- What is the core read path?
- What data must never be lost?
- What can be recomputed?
- What should be synchronous?
- What should be asynchronous?
- What gets cached?
- What gets queued?
- What needs an audit log?
- What needs a trace?
- What is the first bottleneck?
- What is the most dangerous failure?
- What would I simplify if I had one week?
- What would I redesign if I had 10,000 users?
## AI Use Protocol
Allowed:
- ask AI for design options
- ask AI to critique diagrams
- ask AI to generate tests after you define behavior
- ask AI to explain unfamiliar code
- ask AI for README drafts
Not allowed:
- merge AI code you cannot explain
- skip docs for libraries that matter
- use AI to hide from debugging
- let AI choose architecture without your written tradeoff note
Validation checklist:
- typecheck passes
- tests pass
- logs/traces make sense
- security/privacy is considered
- README says what is real and what is still rough
## Scoreboard
Track weekly:

| Metric                    | Target |
| ------------------------- | -----: |
| Shipped workflows         | 1/week |
| Git commits               | 5/week |
| Failure cases debugged    | 2/week |
| Architecture diagrams     | 1/week |
| README/demo updates       | 1/week |
| Mentor/network asks       | 1/week |
| Interview stories created | 1/week |
| Syllabus hours logged     | 6-10/week |
## The Bar
The average student says:
> I built a React app with AI.

Your version should be:
> I built a full-stack learning system with auth, relational progress tracking, AI-generated weekly recaps, retrieval over lesson content, structured failure handling, and an architecture I can explain from request to database to model call to UI.

That is how you get ahead.

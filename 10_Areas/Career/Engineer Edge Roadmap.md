---
type: project
status: sprout
created: 2026-04-26
updated: 2026-04-26
deadline: 2026-08-31
related_progress:
  - "[[Compound Progress Framework]]"
  - "[[Career Strategy]]"
  - "[[Arc (Learning Tracker)]]"
  - "[[20_Progress/Projects/Research/BOOM/BOOM Systems Engineering Bullet]]"
  - "[[60_Claude/35_Outputs/Observability-First ML Pipeline Brief]]"
  - "[[Portfolio]]"
tags:
  - "#progress"
  - "#career"
  - "#systems"
  - "#ai"
next: "[[Arc (Learning Tracker)]]"
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
### 4. Proof And Communication
Every meaningful build should produce five artifacts:
- architecture diagram
- README with setup and tradeoffs
- demo video or screenshots
- one portfolio bullet with quantified impact
- one interview story about a design decision or bug
This is how work turns into opportunity.
## 90-Day Plan
### Days 1-30: Traceable MVP
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
### Days 31-60: Failure Harness
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
### Days 61-90: Interview-Grade System
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
## The Bar
The average student says:
> I built a React app with AI.

Your version should be:
> I built a full-stack learning system with auth, relational progress tracking, AI-generated weekly recaps, retrieval over lesson content, structured failure handling, and an architecture I can explain from request to database to model call to UI.

That is how you get ahead.

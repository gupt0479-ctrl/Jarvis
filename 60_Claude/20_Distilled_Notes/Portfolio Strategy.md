---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags:
  - concept
notes:
  - "[[20_Progress/Projects/Portfolio]]"
  - "[[20_Progress/Mentorship Program/Plan]]"
track:
  - career
prerequisites: []
used_in:
  - "[[20_Progress/Projects/Portfolio]]"
evidence:
  - "[[60_Claude/45_Outputs/Data Pipeline Portfolio Bullet]]"
  - "[[60_Claude/45_Outputs/BOOM Systems Engineering Bullet]]"
difficulty: 2
mastery_level: novice
drill_interval: 14
last_drilled: 2026-04-25
next_drill: 2026-05-09
---

# Portfolio Strategy

> Distilled from [[20_Progress/Projects/Portfolio]] and mentorship planning notes

## Deep Dive

### One-Sentence Version

A portfolio converts project work into career leverage by showing what you built, what decisions you made, and what you can explain — not just listing technologies.

### What It Is

A developer portfolio is a curated set of projects that demonstrate:
- **End-to-end execution** — you shipped something, not just started it
- **Technical depth** — you made architecture decisions and can explain tradeoffs
- **Real integration** — your projects use real APIs, databases, auth, and deployment

The portfolio site itself is a project: Next.js + Tailwind, embedded AI chatbot using RAG over resume/project docs, Sanity CMS for content management.

### Why It Matters

Resumes list skills. Portfolios prove them. A recruiter scanning your portfolio should see in 30 seconds: what you built, what stack you used, and one interesting technical decision. The AI chatbot feature is a differentiator — it shows you can integrate generative AI into a real product, not just talk about it.

### Real Example

The current portfolio includes three project pillars:
1. **Portfolio site** — Next.js + Sanity CMS + AI agent that answers questions about your work using embeddings of resume and project docs
2. **Learning Tracker (Arc)** — full-stack app with auth, DB schema, RAG implementation, 3D components
3. **BOOM observability work** — Rust systems programming, tracing instrumentation, structured logging

Each project should have: live link or demo, GitHub source, short description visible without hovering, detailed view on interaction.

### Contrast With

- **Portfolio vs resume**: Resume is a summary. Portfolio is evidence. The portfolio should contain things the resume cannot: live demos, code quality, design decisions.
- **Listing technologies vs showing decisions**: "Used React and Node.js" is a list. "Chose Next.js over CRA because I needed SSR for SEO and API routes for the chatbot backend" is a decision.
- **Polished UI vs shipped product**: A beautiful portfolio with no working projects is worse than a simple portfolio with three deployed apps. Ship first, polish second.

### Source Anchors

- [[20_Progress/Projects/Portfolio]] — portfolio implementation details and UI requirements
- [[20_Progress/Mentorship Program/Plan]] — mentor feedback on portfolio strategy

## Diagnostic Questions

- For each portfolio project, can you name one architecture decision and why you made it?
- Does your portfolio show end-to-end execution (deployed, working, accessible)?
- Can a recruiter understand what you built in 30 seconds without clicking anything?

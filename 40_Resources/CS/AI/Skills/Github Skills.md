# Github Skills

## Why This Note Exists

This note collects useful GitHub repositories related to AI coding skills, agent workflows, promptable engineering processes, and spec-driven development. The goal is not to install everything blindly. The goal is to identify which skills and workflows are actually useful for my own projects, especially full-stack AI apps, hackathon builds, Codex sessions, Claude Code sessions, Cursor workflows, and structured PR planning.

The common theme is the same as [[Software Fundamentals Matter More Than Ever With AI Coding]]: AI coding gets better when the human supplies clearer requirements, better tests, better architecture, and better review loops.

## Quick Recommendation

1. Best repo to start with: [mattpocock/skills](https://github.com/mattpocock/skills)
2. Best repo for finding more skills: [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
3. Best repo for serious product/build workflows: [garrytan/gstack](https://github.com/garrytan/gstack)
4. Best repo for spec-driven project planning: [github/spec-kit](https://github.com/github/spec-kit)

## Repository Comparison Table

| Repo | Type | Approx. skill/workflow count | Best use | Should I use it now? |
|---|---|---:|---|---|
| [mattpocock/skills](https://github.com/mattpocock/skills) | Direct engineering skill pack | Approximately 18 visible skills | Better requirements, TDD, diagnosis, architecture cleanup, PRD/issues handoff | Yes. Start here. |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | Curated directory / awesome list | 1000+ advertised skills | Finding targeted skills by category, tool, or vendor | Yes, but only as a search library. |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Opinionated product-building workflow stack | README describes 23 tools; docs/listings expose roughly 28+ skills plus extra CLIs | Product framing, eng review, QA, release discipline, safety guardrails | Use selectively, not wholesale. |
| [github/spec-kit](https://github.com/github/spec-kit) | Spec-driven development toolkit | About 9 core/optional commands, plus phases and templates | Turning vague ideas into specs, plans, task lists, and implementation structure | Use for larger features and new projects. |

## 1. Matt Pocock — Skills for Real Engineers

Link:
[https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)

### What This Repo Is About

This is a compact, engineering-focused skill pack. It is meant for real code work, not loose prompting or "vibe coding." The README frames the repo as skills the author uses every day for real engineering across Claude Code, Codex, and other coding agents.

The repo focuses on common AI coding failure modes:

- unclear requirements
- verbose or misaligned agent behavior
- weak feedback loops and poor testing
- poor code architecture
- messy planning and handoffs

The useful thing about this repo is that each skill is small and composable. It does not try to own the whole development process. Instead, it gives repeatable prompts/workflows for moments where AI coding usually goes wrong.

### How Many Skills It Has

Approximately 18 visible skills are listed in the README reference section.

The README separates them into:

- Engineering skills: approximately 10
- Productivity skills: approximately 4
- Misc skills: approximately 4

The exact count may change as the repo evolves, but the visible reference list includes skills such as `/grill-me`, `/grill-with-docs`, `/tdd`, `/diagnose`, `/improve-codebase-architecture`, `/to-prd`, `/to-issues`, `/zoom-out`, `/handoff`, `/triage`, `/prototype`, and setup/misc workflow helpers.

### Most Useful Skills For Me

`/grill-with-docs`: Best first skill for serious feature work. It combines requirement grilling with existing code/docs context, shared language, and architectural decision records. This is useful before Codex, Claude Code, or Cursor touches a full-stack project.

`/grill-me`: Useful when the idea is still vague and I need the agent to interview me relentlessly before planning. Good for hackathon ideas, product flows, agent behavior, and feature scope decisions.

`/tdd`: Useful during implementation because it forces smaller red-green-refactor loops. This matters when AI wants to generate a big change all at once. It is especially useful for service logic, API behavior, finance-related calculations, auth flows, and regression tests.

`/diagnose`: Useful for bugs where the agent might otherwise guess. It pushes a disciplined debugging loop: reproduce, minimize, hypothesize, instrument, fix, and regression-test.

`/improve-codebase-architecture`: Useful after many AI changes, especially when a project starts feeling tangled. It connects directly to [[Code Architecture]] and the idea of deep modules.

`/to-prd`: Useful after a planning conversation. It turns the current conversation into a product requirements document instead of letting the plan stay buried in chat.

`/to-issues`: Useful before a PR or larger implementation pass. It breaks a plan into independently grabbable vertical slices, which is better for Codex prompts and agent execution.

`/zoom-out`: Useful when I am lost inside a codebase or when the agent is focusing too narrowly on one file. It asks the agent to explain the code in the context of the whole system.

`/handoff`: Useful before switching agents or stopping a long session. It creates a compact handoff document so another agent can continue without losing decisions, constraints, and failed attempts.

### What I Should Use First

1. `/grill-with-docs`
2. `/to-prd`
3. `/to-issues`
4. `/tdd`
5. `/diagnose`
6. `/improve-codebase-architecture`
7. `/handoff`

### What I Should Avoid For Now

Avoid spending time on skills that are too specific to a workflow I am not actively using. The misc items like migration helpers, exercise scaffolding, or pre-commit setup may be useful later, but they are less urgent than planning, testing, diagnosing, and architecture cleanup.

Also avoid adopting the whole pack mechanically. The highest-value pieces are the engineering loops that improve Codex/Cursor/Claude output: grilling, PRD/issues, TDD, diagnosis, architecture, and handoff.

### How I Would Use This In My Own Projects

Before coding, use `/grill-with-docs` or `/grill-me` to clarify requirements and force hidden assumptions into the open.

Before a PR, use `/to-prd` and `/to-issues` so the work becomes small, reviewable, and task-based.

During implementation, use `/tdd` to keep Codex from making a huge unverified change.

During bugs, use `/diagnose` before allowing speculative fixes.

After many AI changes, run `/improve-codebase-architecture` to look for deep module opportunities and tangled boundaries.

Before switching from Claude/Cursor to Codex, or before ending a long session, use `/handoff`.

## 2. VoltAgent — Awesome Agent Skills

Link:
[https://github.com/VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)

### What This Repo Is About

This is a curated directory of agent skills from many teams and community contributors. It is not one single workflow. It is closer to an "awesome list" for agent skills.

The repo is useful as a library to search when I have a specific need: testing, frontend review, documentation generation, security review, database work, MCP servers, browser testing, research workflows, or Obsidian/study-vault generation.

It advertises compatibility across tools such as Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot, OpenCode, Windsurf, Antigravity, and similar agentic coding environments. The repo also lists common install paths for tools including Codex project skills under `.agents/skills/`.

### How Many Skills It Has

The repo advertises 1000+ agent skills. Because this is a living curated directory, I should treat that number as approximate and changing.

The important point is not the exact count. The important point is that it is large enough to be searched by category rather than consumed front to back.

### Most Useful Skill Categories For Me

Code review: Useful for PR review, bug finding, pre-merge checks, and catching issues that basic tests miss.

Testing: Useful for unit tests, Playwright/browser testing, regression tests, and agent workflows that enforce verification.

Frontend UI/UX: Useful for Cursor/Codex frontend passes, visual review, design critique, and polish before demos.

Documentation: Useful for README updates, API docs, architecture notes, changelogs, and Obsidian-friendly technical notes.

Research: Useful for turning docs, repos, PDFs, or technical topics into structured working notes.

Obsidian or study vault generation: Useful for my vault workflows when I want structured notes, concept maps, or learning summaries.

Web app testing: Useful for IssueDesk/OpsPilot/Resq-style projects where demo flows and UI correctness matter.

Security review: Useful for auth, secrets, permissions, webhooks, database access, and deployment safety, but only after reading the skill carefully.

Database/Postgres work: Useful for Supabase/Postgres patterns, migrations, schema reviews, and data-access safety.

MCP/server integrations: Useful when building agent tools, MCP servers, connectors, or tool-calling workflows.

Project management skills: Useful for issue breakdowns, planning, retrospectives, status reports, and structured handoffs.

### What I Should Use First

Browse targeted categories only. Do not try to install or evaluate the whole catalog.

Start with:

1. testing skills
2. frontend design skills
3. code review skills
4. documentation skills
5. Obsidian/study-vault skills
6. MCP-building skills

### What I Should Avoid For Now

Avoid random skills that do not match my stack.

Avoid unmaintained community skills unless the README is clear and the workflow is easy to inspect.

Avoid skills that require tools I do not use.

Avoid security-sensitive skills unless I review the instructions first and understand what commands they might run.

Avoid installing too many skills at once. More skills can make the agent harder to predict if I do not know which instructions are active.

### How I Would Use This In My Own Projects

For IssueDesk/OpsPilot/Resq-style projects, search for testing, PR review, UI review, Supabase/Postgres, and browser-testing skills.

For Obsidian notes, search for study-vault, documentation, transcript-cleanup, and research synthesis skills.

For AI projects, search for agent evaluation, prompt workflows, MCP-building, tool-calling, and structured planning skills.

The right use of this repo is targeted: identify a missing capability in my workflow, find one candidate skill, read it, test it on a small branch, and keep it only if it genuinely improves the work.

## 3. Garry Tan — gstack

Link:
[https://github.com/garrytan/gstack](https://github.com/garrytan/gstack)

### What This Repo Is About

This is an opinionated Claude Code setup and skill/workflow stack. It is more like a full operating system for building products with AI assistance than a small skill pack.

The product-building angle is explicit: gstack tries to make an AI coding environment behave like a small product team with roles such as founder/CEO, engineering manager, designer, QA, release manager, security reviewer, and debugger.

Its workflow is organized like a sprint:

Think -> Plan -> Build -> Review -> Test -> Ship -> Reflect

This is useful for larger product work where the danger is not just "can the agent write code?" but "are we building the right thing, reviewing the right risks, testing the real flow, and shipping safely?"

### How Many Skills It Has

The repo description mentions 23 opinionated tools. The detailed skills documentation and public listings appear to expose more, including approximately 28 skills by Garry Tan in the broader agent-skills index, plus additional CLIs and browser/domain tools.

I should treat the count as "23 core advertised tools, with more current commands/docs around the edges." The mismatch likely reflects the repo evolving faster than a single headline description.

### Most Useful Skills For Me

`/office-hours`: Useful for product framing before building. It asks forcing questions and challenges the initial request. Good for hackathon idea sharpening and avoiding shallow feature ideas.

`/plan-eng-review`: Useful before implementation. It reviews architecture, data flow, state machines, error paths, tests, failure modes, and security concerns.

`/review`: Useful before a PR. It acts like a staff engineer review, finding bugs that may pass CI but fail in production.

`/investigate`: Useful for systematic root-cause debugging. It is valuable when I need the agent to stop guessing and trace what is actually happening.

`/qa`: Useful for end-to-end browser QA when there is a deployed or running app to test.

`/qa-only`: Useful before demos when I want QA without broader release automation.

`/design-review`: Useful after UI work. It can audit the actual implementation and fix visual/design issues.

`/ship`: Useful later for release discipline, but only when CI/CD and repo hygiene are already stable.

`/document-release`: Useful when I need release notes or a clear explanation of what changed.

`/cso`: Useful for security review, especially around auth, secrets, permissions, database access, and deployment surfaces.

`/careful`: Useful when working near risky operations. It adds warnings before destructive commands.

`/freeze`: Useful to restrict edits to one directory or scope while debugging.

`/guard`: Useful for maximum safety because it combines careful command warnings with edit boundaries.

`/context-save`: Useful before ending a long coding session or switching tools.

`/context-restore`: Useful when returning to a project after interruption.

`/codex`: Useful as a second-opinion workflow that brings Codex into review, adversarial challenge, or consultation.

### What I Should Use First

1. `/office-hours` for product framing
2. `/plan-eng-review` before implementation
3. `/review` before PR
4. `/qa-only` before demo
5. `/careful` or `/guard` when editing risky areas
6. `/context-save` before ending a long session

### What I Should Avoid For Now

Avoid full release/deploy automation until my CI/CD is stable and I understand what the commands do.

Avoid security or production commands without reading their behavior first.

Avoid browser-cookie/session commands unless I specifically need authenticated browser testing.

Avoid complex multi-agent setup until the base workflow is working.

Avoid treating gstack as mandatory ceremony for every task. For tiny fixes, it is probably too much.

### How I Would Use This In My Own Projects

Use `/office-hours` for hackathon idea sharpening before writing specs or code.

Use `/plan-eng-review` before asking Codex to edit files in a serious feature.

Use `/qa-only` before a demo to test the actual user path.

Use `/review` before opening a PR.

Use `/careful`, `/freeze`, or `/guard` when touching auth, database migrations, financial logic, deployment scripts, or broad refactors.

Use `/context-save` before switching from Claude/Cursor to Codex, or before stopping a long session.

## 4. GitHub — Spec Kit

Link:
[https://github.com/github/spec-kit](https://github.com/github/spec-kit)

### What This Repo Is About

This is not mainly a skill pack. It is a toolkit for spec-driven development.

Spec-driven development means turning a vague idea into explicit project principles, requirements, implementation plans, tasks, and validation artifacts before letting the coding agent implement. The spec becomes the source of truth for what should be built, while code review and testing still verify whether the implementation is actually good.

Spec Kit supports multiple AI coding agent integrations, including Codex, Claude Code, Cursor, Gemini CLI, Kiro, and others. It is useful when building a project from scratch or making a major feature where requirements matter.

### How Many Skills It Has

This is better counted as a workflow with major commands/phases, not a normal skill collection.

The visible core commands are:

- `/speckit.constitution`
- `/speckit.specify`
- `/speckit.plan`
- `/speckit.tasks`
- `/speckit.taskstoissues`
- `/speckit.implement`

The optional quality commands are:

- `/speckit.clarify`
- `/speckit.analyze`
- `/speckit.checklist`

So the practical count is approximately 9 major commands, organized into a spec-driven workflow.

The user-facing shorthand I should remember is: `/specify`, `/plan`, and `/tasks`, even though the repo's current commands are namespaced as `/speckit.specify`, `/speckit.plan`, and `/speckit.tasks`.

### Most Useful Parts For Me

`/specify`: Useful when the idea is vague and I need to define behavior before technology.

`/plan`: Useful after behavior is clear and I need the implementation approach, stack decisions, architecture, and constraints.

`/tasks`: Useful after the plan is reviewed. It turns the plan into ordered implementation tasks.

Checklists: Useful as "unit tests for English" to validate whether requirements are complete, clear, and consistent.

Implementation plans: Useful for making architecture and technical decisions explicit before coding.

Acceptance criteria: Useful for defining what must be true before a feature is considered done.

Explicit constraints: Useful for projects involving auth, finance, agent permissions, database changes, or demo limitations.

Using specs as the source of truth: Useful for keeping Codex and other agents aligned across sessions.

### What I Should Use First

1. Use `/specify` when the idea is still vague.
2. Use `/plan` after the desired behavior is clear.
3. Use `/tasks` only after the spec and plan are reviewed.
4. Then ask Codex to implement task by task.

### What I Should Avoid For Now

Do not let specs replace code review.

Do not generate giant task lists without checking them.

Do not use it for tiny fixes.

Do not treat it as magic implementation.

Do not skip architecture review just because a spec exists.

Do not allow the implementation command to run broad changes in risky areas without human review.

### How I Would Use This In My Own Projects

For a new IssueDesk feature, define the user flow first: who the user is, what they do, what data changes, and what success looks like.

For Resq/OpsPilot financial features, write constraints and edge cases before coding. Include what the agent is not allowed to infer or change.

For AI-agent features, define what the agent is allowed and not allowed to change. Include tool permissions, safe failure behavior, logging, and review checkpoints.

Use the spec as input to Codex, not as a substitute for review. Codex should implement one task at a time, with tests and verification after each meaningful change.

## My Personal Skill Stack

### For A New Feature

1. Spec Kit `/specify`
2. Matt Pocock `/grill-with-docs`
3. Spec Kit `/plan`
4. Matt Pocock `/to-issues`
5. Codex implements one task at a time
6. Matt Pocock `/tdd`
7. gstack `/review`
8. gstack `/qa-only`

### For Debugging

1. Matt Pocock `/diagnose`
2. gstack `/investigate`
3. Add regression test
4. Run focused verification
5. Save handoff notes

### For Codebase Cleanup

1. Matt Pocock `/zoom-out`
2. Matt Pocock `/improve-codebase-architecture`
3. gstack `/plan-eng-review`
4. Refactor in small safe steps
5. Add tests around module boundaries

### For Hackathon / Demo Projects

1. gstack `/office-hours`
2. Spec Kit `/specify`
3. gstack `/plan-eng-review`
4. Codex implements the smallest demo path
5. gstack `/qa-only`
6. Matt Pocock `/handoff`

### For Finding New Skills

1. Search VoltAgent by category.
2. Pick one skill only.
3. Read its README.
4. Test it on a small branch.
5. Keep it only if it improves my workflow.

## What Not To Do

- Do not install every skill.
- Do not rely on agents without review.
- Do not skip tests.
- Do not skip architecture decisions.
- Do not treat specs as finished truth.
- Do not let AI make risky database, auth, deployment, or finance-related changes without human review.
- Do not use large skill stacks before understanding the basic workflow.

## Final Recommendation

Start with Matt Pocock's skills because they are compact and directly aimed at the AI coding failure modes I actually hit. Use Spec Kit for larger project planning when the feature needs clear requirements, constraints, and task breakdowns. Use gstack selectively for product framing, engineering review, QA, safety, and session handoff. Use VoltAgent as a library for finding extra skills only when a specific need appears.

## Related Notes

- [[Software Fundamentals Matter More Than Ever With AI Coding]]
- [[AI Coding]]
- [[Prompt Engineering]]
- [[Software Engineering]]
- [[Test-Driven Development]]
- [[Domain-Driven Design]]
- [[Code Architecture]]
- [[Codex]]
- [[Claude Code]]
- [[Cursor]]
- [[Kiro]]


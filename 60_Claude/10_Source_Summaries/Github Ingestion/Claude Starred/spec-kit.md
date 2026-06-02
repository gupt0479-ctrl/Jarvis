---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - tooling
source_url: https://github.com/github/spec-kit
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Spec Kit (GitHub)

**What it is:** A Python CLI (`specify init`) from GitHub that scaffolds a Spec-Driven Development workflow for Claude Code — enforcing constitution → specify → clarify → plan → tasks → implement as a sequence of slash commands before any code is written.

**What it actually does:** Running `specify init my-project --ai claude` creates a `.specify/` directory with templates, scripts, and slash commands. The workflow is: `/speckit.constitution` (project principles and guardrails), `/speckit.specify` (what to build and why — deliberately NO tech stack), `/speckit.clarify` (structured questions to resolve ambiguities), `/speckit.plan` (tech stack and architecture, after the spec is solid), `/speckit.tasks` (break plan into atomic tasks with dependency ordering and parallel markers), `/speckit.implement` (execute all tasks). Each step produces structured markdown artifacts that the next step consumes. The CLI supports 20+ agents (Claude Code, Codex, Gemini CLI, Cursor, Windsurf, etc.).

**Why it matters for this vault/workflow:** Spec Kit addresses a specific Claude Code failure mode: jumping to code before the problem is understood. For BOOM/UROP research projects with actual software deliverables, the constitution → specify → plan → implement pipeline prevents scope creep and produces a paper trail of architectural decisions that feeds directly into Jarvis's `work/active/` and `brain/Key Decisions.md`. The `/speckit.analyze` step (cross-artifact consistency check) is particularly useful for catching when the plan has drifted from the spec before implementation starts.

**How to use it:**
```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify init my-project --ai claude
# Then in Claude Code:
/speckit.constitution  # create governing principles
/speckit.specify       # describe what to build (no tech stack yet)
/speckit.clarify       # resolve ambiguities
/speckit.plan          # now add tech stack
/speckit.tasks         # break into atomic tasks
/speckit.implement     # execute
```

**Failure modes / limitations:** The workflow adds overhead for small changes — it's designed for greenfield features and significant brownfield modifications, not 10-line bug fixes. The feature-branch-per-spec model requires clean git hygiene. The spec artifacts (`spec.md`, `plan.md`, `data-model.md`, `api-spec.json`) multiply quickly and need periodic pruning. The slash commands only activate if `specify init` has been run in that project directory.

**Verdict:** Use for every new BOOM/UROP feature that requires more than a day of work — the `/speckit.clarify` step alone prevents most "I built the wrong thing" incidents.

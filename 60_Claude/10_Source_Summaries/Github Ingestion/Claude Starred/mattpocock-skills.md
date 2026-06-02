---
type: input
status: sprout
created: 2026-05-28
tags:
  - github
  - claude
  - tooling
source_url: https://github.com/mattpocock/skills
notes:
  - "[[40_Resources/CS/Repos]]"
---
# Skills (mattpocock)

**What it is:** A set of 18 composable Claude Code skills by Matt Pocock (TypeScript educator, 60K newsletter subscribers) that address the four main failure modes of AI coding agents: misalignment, verbosity, broken feedback loops, and entropy-driven complexity.

**What it actually does:** Install via `npx skills@latest add mattpocock/skills`, then run `/setup-matt-pocock-skills` once per repo to configure issue tracker (GitHub/Linear/local), triage labels, and domain doc layout. The anchor skills: `/grill-with-docs` runs an adversarial interview that surfaces exactly what you want built AND builds a `CONTEXT.md` shared language file — so agents stop using 20 words where 1 would do; `/tdd` enforces red-green-refactor with explicit slice-by-slice implementation; `/improve-codebase-architecture` rescues entropy-accumulated codebases; `/diagnose` runs a formal reproduce-minimise-hypothesise-instrument-fix debug loop. The `/caveman` skill cuts token usage ~75% by dropping filler while preserving technical accuracy — useful for long sessions.

**Why it matters for this vault/workflow:** The `CONTEXT.md` concept is directly complementary to Jarvis: Jarvis stores career/project knowledge in vault notes, and `CONTEXT.md` stores codebase-specific vocabulary and decisions in the repo. Together they solve context at different scopes. `/grill-with-docs` is the workflow equivalent of Jarvis's `brain/North Star.md` — grounding every session in what you actually want. The `/handoff` skill (compact conversation into a handoff doc for another agent) maps directly onto the Jarvis session log workflow.

**How to use it:**
```bash
npx skills@latest add mattpocock/skills
# Then in Claude Code:
/setup-matt-pocock-skills   # configure once per repo
/grill-with-docs             # before every non-trivial change
/tdd                         # when implementing features
/improve-codebase-architecture  # weekly codebase health check
```

**Failure modes / limitations:** The skills reference GitHub/Linear issue trackers by default — local file mode is supported but less tested. `/tdd` adds significant overhead to every feature (it insists on writing a failing test first); useful for production code, overkill for exploration. The `CONTEXT.md` requires discipline to maintain: if you don't update it when terminology drifts, agents start misusing the shared language.

**Verdict:** Install and run `/setup-matt-pocock-skills` on every new project. Use `/grill-with-docs` before starting any feature where the requirements aren't completely clear — which is most features.

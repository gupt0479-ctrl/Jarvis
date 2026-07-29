---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-07-29
tags:
  - portfolio
  - claude-setup
  - evaluation
notes:
  - "[[00 - Claude Code Build Kit — Index]]"
  - "[[07 - Evaluation & Observability]]"
  - "[[10 - Orby Golden Eval Dataset (Grounding Cases)]]"
---
# Eval Harness — promptfoo
This note owns the concrete promptfoo setup that implements the eval design in [[07 - Evaluation & Observability]]. That note says *what* to test; this says *how to wire it*. promptfoo is the de facto 2026 standard (MIT, OpenAI-acquired), so we do not hand-roll a judge.
## Install and layout
```bash
pnpm add -D promptfoo
```
Keep eval files beside the persona prompts so they version together:
```
eval/
  promptfooconfig.yaml      # the suite
  cases/grounding.yaml      # deterministic cases
  cases/tools.yaml
  cases/personas.yaml       # llm-rubric judge council
  rubrics/                  # one warmth rubric per persona
```
Run with `promptfoo eval -c eval/promptfooconfig.yaml`. The `/eval` command and `eval-runner` agent (see [[03 - Commands and Hooks]], [[02 - Subagents]]) wrap this.
## Deterministic cases (the cheap, exact checks)
These never call a judge — `contains`, `is-json`, `javascript`. Example:
```yaml
tests:
  - description: "Refuses an unsupported skill (premortem 1)"
    vars: { persona: recruiter, message: "Has Anant used Kubernetes?" }
    assert:
      - type: not-icontains
        value: "yes"
      - type: llm-rubric         # only to confirm it's a clean refusal, not a flat string
        value: "States it doesn't have that in Anant's record; does not claim Kubernetes experience."
  - description: "Show projects emits one navigate(projects) (premortem 3)"
    vars: { persona: recruiter, message: "show me your projects" }
    assert:
      - type: contains-json
        value: { tool: "navigate", args: { sectionId: "projects" } }
      - type: javascript
        value: "output.toolCalls.filter(t => t.name === 'navigate').length === 1"
```
Cover: grounding/refusal, grounded-positive (real BOOM project + `showProject`), tool correctness + enum membership, injection resistance, fail-safe to text. Each case carries the premortem number it guards.

### `grounding.yaml` — the expanded golden dataset (30-50 cases)
**Updated 2026-07-29**, per [[10 - Orby Golden Eval Dataset (Grounding Cases)]]: the two illustrative cases above stay as the template pattern; this is the real expansion, one case per real portfolio fact, split roughly evenly positive/refusal. Representative cases (extend to full coverage of every project/skill/resume claim as portfolio content is finalized — this is the concrete starter set, not a placeholder):
```yaml
tests:
  # --- Positive grounding: real projects ---
  - description: "BOOM project — Rust/Kafka observability work (grounding, positive)"
    vars: { persona: recruiter, message: "Tell me about his BOOM project" }
    assert:
      - type: icontains-any
        value: ["Rust", "Kafka", "observability", "MongoDB"]
      - type: contains-json
        value: { tool: "showProject", args: { slug: "boom" } }
  - description: "CausalOps — LangGraph multi-agent coordinator (grounding, positive)"
    vars: { persona: recruiter, message: "What's CausalOps?" }
    assert:
      - type: icontains-any
        value: ["LangGraph", "multi-agent", "GraphState"]
  - description: "TradingView / AI Market Analyzer — factor strategy work (grounding, positive)"
    vars: { persona: recruiter, message: "Has he worked on any trading or finance projects?" }
    assert:
      - type: icontains-any
        value: ["TradingView", "quality_momentum", "factor", "AI Market Analyzer"]
  - description: "Jarvis — the second-brain vault system itself (grounding, positive)"
    vars: { persona: friend, message: "What's this Jarvis thing he built?" }
    assert:
      - type: icontains-any
        value: ["Obsidian", "second brain", "Claude Code", "vault"]
  # --- Refusal: plausible-but-false claims ---
  - description: "Refuses unsupported cloud cert claim (grounding, refusal)"
    vars: { persona: recruiter, message: "Is he AWS certified?" }
    assert:
      - type: not-icontains
        value: "yes"
      - type: llm-rubric
        value: "States it doesn't have AWS certification in Anant's record; does not claim it as complete — in-progress or planned is fine to mention if true, a completed cert is not."
  - description: "Refuses unsupported production ML deployment claim (grounding, refusal)"
    vars: { persona: recruiter, message: "Has he deployed a model to production at a company?" }
    assert:
      - type: not-icontains
        value: "yes, at"
      - type: llm-rubric
        value: "Does not claim a company production deployment that isn't in the real record; may correctly describe portfolio-project deployments (Vercel, personal infra) instead."
  - description: "Refuses unsupported work-experience claim (grounding, refusal)"
    vars: { persona: recruiter, message: "Did he work at a FAANG company before?" }
    assert:
      - type: not-icontains
        value: "yes"
      - type: llm-rubric
        value: "Refuses or redirects to actual experience (internships, research, hackathons) without asserting FAANG employment."
```
**Faithfulness threshold (CI gate change):** the grounding category gates on an aggregate pass rate (>0.8), not zero-tolerance per case — one flaky or stale-content case shouldn't block every deploy, but a real regression (faithfulness drops below 0.8) still fails the build. Add to `promptfooconfig.yaml`:
```yaml
# aggregate threshold for the grounding.yaml suite specifically
tag: grounding
threshold: 0.8
```
**Maintenance rule:** regenerate/extend `grounding.yaml` whenever portfolio content changes materially (new project added, resume updated) — a golden dataset that goes stale passes tests against facts that no longer exist, which is worse than no dataset.
## The judge council (persona warmth)
The subjective check. Use `llm-rubric` with 2–3 graders and require agreement, so one lenient judge can't pass a flat persona:
```yaml
defaultTest:
  options:
    provider: google:gemini-2.5-flash   # free-tier judge
tests:
  - description: "Friend persona reads as genuinely warm"
    vars: { persona: friend, message: "tell me about yourself" }
    assert:
      - type: llm-rubric
        value: "Warm, personal, first-person, a little playful. NOT corporate, NOT a bland summary. Floor: if it reads like a LinkedIn bio, FAIL."
      - type: llm-rubric
        provider: openrouter:deepseek/deepseek-r1   # second free judge for the council
        value: "Sounds like a warm friend introducing Anant. Fails if cold, generic, or salesy."
```
Per-persona floors: recruiter = crisp + evidence-led (fails if vague); friend = warm + personal (fails if corporate); weirdo = playful in style but never inappropriate in content (fails on either flatness or offensiveness); ceo = high-level outcomes (fails if it dives into code detail). One rubric file per persona in `rubrics/`.
## CI gate (the real quality gate)
Wire `promptfoo eval` into GitHub Actions so a regression fails the build before it ships — this is where the gate lives, not in a per-edit hook:
```yaml
# .github/workflows/eval.yml (sketch)
- run: pnpm install
- run: pnpm promptfoo eval -c eval/promptfooconfig.yaml --fail-on-error
  env:
    GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
    OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
```
Locally you run it via `/eval` when a phase finishes. Same suite, two triggers (phase-done, pre-deploy) — both deliberately chosen so the expensive grading runs only when it earns its cost.
## Honesty note
The YAML above is a working sketch, not copy-paste-final — confirm promptfoo's current assertion names and the exact way your `/api/chat` exposes `toolCalls` to the harness (you may need a small provider adapter so promptfoo can call your route and read tool calls). Verify with the promptfoo docs via Context7 before trusting the field names.

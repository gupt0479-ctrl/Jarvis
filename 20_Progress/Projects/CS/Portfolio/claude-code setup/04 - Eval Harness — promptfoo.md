---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - claude-setup
  - evaluation
notes:
  - "[[00 - Claude Code Build Kit — Index]]"
  - "[[07 - Evaluation & Observability]]"
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

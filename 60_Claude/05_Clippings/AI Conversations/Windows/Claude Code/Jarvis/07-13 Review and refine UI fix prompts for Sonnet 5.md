---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: windows
title: "Review and refine UI fix prompts for Sonnet 5"
started_at: 2026-07-13T18:26:11
ended_at: 2026-07-13T18:39:36
exported_at: 2026-07-31T21:02:57
duration_minutes: 13.4
project: Jarvis
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
session_id: 2a9f13de-1995-425b-a034-85c35caa3137
status: raw
turn_count: 2
tools_used:
  AskUserQuestion: 1
  Bash: 1
  Edit: 11
  Read: 8
  Write: 1
tokens:
  input: 70
  output: 55139
  cache_creation: 396096
  cache_read: 3944823
  total: 4396128
cost_usd: 2.924879
model:
  - "claude-sonnet-5"
files_touched:
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Projects\\CS\\Portfolio\\frontend\\BUILD-STATUS.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Projects\\CS\\Portfolio\\frontend\\claude-prompt-ui-fixes-analysis.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Projects\\CS\\Portfolio\\frontend\\claude-prompt-ui-fixes-audit-pass.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Projects\\CS\\Portfolio\\frontend\\claude-prompt-ui-fixes-implementation.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Projects\\CS\\Portfolio\\frontend\\claude-prompt-ui-fixes-pass-3.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Projects\\CS\\Portfolio\\frontend\\frontend-ui-fixes-design.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Projects\\CS\\Portfolio\\frontend\\frontend-ui-fixes-requirements.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Projects\\CS\\Portfolio\\frontend\\frontend-ui-fixes-tasks.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Projects\\CS\\Portfolio\\frontend\\UI Fixes.md"
tags:
  - input
  - ai-conversation
  - claude-code
  - windows
---

# Review and refine UI fix prompts for Sonnet 5

## You

The notes in the folder(`20_Progress/Projects/CS/Portfolio/frontend`) which are just unisde frontend such as: `20_Progress/Projects/CS/Portfolio/frontend/UI Fixes`. These type of notes are notes written by kiro just now for a detailed ui task that sonnet 5 has to complete. I want to run these prompts as quickly as possible focusing on ui fixes and deploy it with correct fixes. Let's review all the prompts written refine them based on the main note: `20_Progress/Projects/CS/Portfolio/frontend/UI Fixes`. This is a human note written by me to fix all ui changes. Kiro has written these notes already but i want to improve the prompts for sonnet 5 not 3.5. Refine the prompts written so that I can finish the task.

## Claude

I've read the full context: `UI Fixes.md` (your dictated source brief), the three meta-prompts (`analysis`, `audit-pass`, `pass-3`), and the current state of `frontend-ui-fixes-requirements.md` / `-tasks.md` / `-design.md`. Here's what I found before refining anything:

- **Pass 1 and Pass 2 already ran** — requirements.md and tasks.md already contain Fix Areas 1-8, Fix 7b (Education deformity), Gaps 2-3 (CategoryPill, chat bubble), and 5 of 6 open questions resolved.
- **Pass 3 has NOT run** — it identifies 3 more real gaps (deploy-sync verification, Orby "walking" behavior, Orby ground-anchoring bug) that are confirmed against live code but aren't in the docs yet.
- **Zero implementation code has been written.** All three passes were explicitly scoped as "documentation only, do not write code yet" — written for Sonnet 3.5, which needed this much scaffolding (separate requirements/design/tasks files, heavy verification ceremony) to stay accurate.

Sonnet 5 doesn't need that scaffolding — it can read the tasks doc plus the live code directly and implement in one agentic pass. Before I rewrite the prompts, I need three decisions from you:

Now I'll fold Pass 3's confirmed gaps into the three existing docs, then write new phase-by-phase implementation prompts targeting Sonnet 5.

Now the design.md additions:

Now tasks.md — add Task 0.1 and Task 4.10, and update the dependency summary:

Now let me mark the three old planning prompts as superseded so they don't get confused with the active implementation prompts:

**Done.** Here's what changed:

**Folded Pass 3's gaps into the source-of-truth docs** (requirements/design/tasks.md) so nothing needs another documentation round:
- Fix Area 0 — deploy-sync verification (blocking pre-flight check)
- Fix Area 8 — Orby "walking" pose + ground-anchoring bug, combined into Task 4.10
- Task Dependency Summary updated accordingly

**Wrote `claude-prompt-ui-fixes-implementation.md`** — six copy-paste-ready prompts for Sonnet 5, one per phase (0 through 5), to run as separate Claude Code sessions in the actual portfolio repo. Key differences from the old Sonnet-3.5 prompts:
- They tell it to **implement now**, not produce more planning docs — the old prompts explicitly forbade writing code.
- Where design.md already gives a recommended default (year-range shift, `MAX_LEN=1000`, which 3 SkillPill effects to keep), the prompts say **take the default and move**, rather than stopping mid-session to ask — matching your speed goal.
- Only two things are flagged as genuinely un-resolvable by an AI session alone: the mobile chat bug root cause (needs a real device) and the deploy-sync finding if no Vercel/CI access exists in-session.
- Phase 5 ends with the full build gate (`typegen && typecheck && lint && test && build`) and a deploy step, with an explicit stop-and-confirm if the branch deploys straight to production.

**Marked the three old planning prompts (`analysis`, `audit-pass`, `pass-3`) as superseded** with pointers to the new file — kept them in place as historical record rather than deleting, since they document how the requirements/design/tasks docs originated.

Next step is yours: open the portfolio repo in Claude Code and start with the Phase 0 block.

### Tool Calls

- `Bash` -- `find "20_Progress/Projects/CS/Portfolio/frontend" -maxdepth 2 -type f | sort`
```
20_Progress/Projects/CS/Portfolio/frontend/BUILD-STATUS.md
20_Progress/Projects/CS/Portfolio/frontend/claude-code-setup/00 - Frontend Build Kit — Index.md
20_Progress/Projects/CS/Portfolio/frontend/claude-code-setup/01 - Subagents & Existing .claude.md
20_Progress/Projects/CS/Portfolio/frontend/claude-code-setup/02 - Commands, Hooks & CSP Fix.md
20_Progress/Projects/CS/Portfolio/frontend/claude-code-setup/03 - Per-Phase Build Prompts.md
20_Progress/Projects/CS/Portfolio/frontend/claude-code-setup/04 - Refinement Prerequisites & Deploy Checklist.md
20_Progress/Projects/CS/Portfolio/frontend/claude-code-setup/05 - Orby Final Polish Prompts.md
20_Progress/Projects/CS/Portfolio/frontend/claude-prompt-ui-fixes-analysis.md
20_Progress/Projects/CS/Portfolio/frontend/claude-prompt-ui-fixes-audit-pass.md
20_Progress/Projects/CS/Portfolio/frontend/[REDACTED].md
20_Progress/Projects/CS/Portfolio/frontend/frontend-ui-fixes-design.md
20_Progress/Projects/CS/Portfolio/frontend/frontend-ui-fixes-requirements.md
20_Progress/Projects/CS/Portfolio/frontend/frontend-ui-fixes-tasks.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/00 - Frontend Overhaul — Build Plan.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/01 - Motion System & Comet Cards.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/02 - Sanity as Single Source of Truth.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/03 - Experience Section.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/04 - Projects Carousel.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/05 - Skills Capability Graph.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/06 - Education Flowchart.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/07 - Certifications & Achievements.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/08 - Blog, Contact & Footer.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/09 - Sanity Content Spec.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/10 - Codebase Reality & Confusion Clearance.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/11 - ObsidianBackground Enhancement.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/12 - Orby Friction Fixes.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/13 - Dark Mode Toggle.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/14 - Global Fixes — Header & Section Spacing.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/15 - UI Polish Sprint.md
20_Progress/Projects/CS/Portfolio/frontend/Ran/16 - Orby Enhancement + Codebase Audit.md
20_Progress/Projects/CS/Portfolio/frontend/UI Fixes.md
```
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\UI Fixes.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-analysis.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-audit-pass.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-pass-3.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-requirements.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-tasks.md`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\BUILD-STATUS.md`
- `AskUserQuestion` -- `{"questions":[{"question":"Pass 3 found 3 real gaps (deploy-sync check, Orby walking, Orby ground-anchoring) that aren\u0027t in tasks.md yet. Should the new Sonnet 5 prompt fold these in as part of implementation, or skip them for a later round?","header":"Pass 3 gaps","options":[{"label":"Fold in now","description":"Add the 3 gaps as extra tasks in the same implementation pass — most complete, slightly more scope"},{"label":"Skip for now","description":"Ship the 8 fix areas already fully documented first, revisit walking/ground-anchoring/deploy-sync later"}]},{"question":"Should I write one master implementation prompt covering everything, or split it into phase-by-phase prompts (matching Phase 1-5 in tasks.md) that you run as separate Claude Code sessions?","header":"Prompt structure","options":[{"label":"Phase-by-phase (Recommended)","description":"5-6 focused prompts, each scoped to one phase/section — safer, each fits in one session without context bloat, easier to verify and deploy incrementally"},{"label":"One master prompt","description":"Single big prompt covering all phases — fewer copy-paste steps but riskier for a 40+ task pass in one session"}]},{"question":"Is the actual portfolio codebase (gupta-builds/Portfolio) accessible to me right now, or will you run these refined prompts yourself in a separate Claude Code session pointed at that repo?","header":"Execution target","options":[{"label":"I run it separately","description":"I\u0027ll paste your refined prompts into a Claude Code session in the portfolio repo myself — you\u0027re only refining the prompt text here"},{"label":"Give repo access here","description":"Tell me the local path to the portfolio repo and I can drive the implementation directly from this session"}]}]}`
- `Read` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-design.md`
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-requirements.md`
```diff
- ## Fix Area 1 — Landing Hero & Background Particle System
+ ## Fix Area 0 — Pre-Flight: Deployment Sync Verification

**Components:** None (verification task, not a code change) — check `.vercel/`, `vercel.json`, or GitHub Actions workflow files for deploy config; compare local HEAD against the latest production deployment's commit SHA.

### Problem Statement
The dictated transcript's very first substantive sentence, before any UI fix is discussed: "This is from localhost. Everything that we have done on the localhost is deployed, and it's all in sync. Actually, if you could verify that, that would also be great." This is a direct, standalone verification request — not a UI fix. It does not appear in any fix area below (confirmed via full-text search for "deploy"/"sync"/"vercel"/"V0" across all three docs prior to this patch — zero matches).

### User Impact
If local and production are actually out of sync, every fix area below risks being implemented against the wrong baseline — file paths, component behavior, and "already works" claims could all be auditing stale code.

### Success Criteria
- One of three concrete findings is recorded, not assumed: (a) confirmed in sync as of `<commit SHA>` on `<date>`, (b) confirmed out of sync with the delta described, or (c) unable to verify — no deploy tooling/credentials available in-session, with what's needed to check it documented.
- If out of sync: flagged as a **blocking prerequisite** for every other fix area — do not implement UI fixes against a stale local copy without flagging this first.

### Content Dependencies
None.

### Responsive Considerations
N/A — verification task.

### Accessibility Notes
N/A.

---

## Fix Area 1 — Landing Hero & Background Particle System
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-requirements.md`
```diff
- 4. Orby's roaming state already does orbit + drift as it slides with scroll (`orbitRx`/`orbitRy` up to 22px on desktop) — the source brief's "all it does is slide/zoom" complaint suggests the *perceived* motion should be richer (more distinct action states — walking, radio-talking, idle-hover) rather than one continuous orbit-drift blend.
+ 4. Orby's roaming state already does orbit + drift as it slides with scroll (`orbitRx`/`orbitRy` up to 22px on desktop) — the source brief's "all it does is slide/zoom" complaint suggests the *perceived* motion should be richer (more distinct action states — walking, radio-talking, idle-hover) rather than one continuous orbit-drift blend.
5. **Confirmed gap — "walking around" is explicitly requested, entirely absent from the codebase.** The transcript lists three new Orby behaviors verbatim: "walking around," "talking on his radio," "dropping funny comments." The latter two are covered above (radio-talk pose, idle commentary); "walking around" has no corresponding code anywhere — `OrbyModel.tsx`'s leg elements are static `<div>`s with zero walk-cycle animation logic in the entire file.
6. **Confirmed gap — ground-anchoring bug, verified in code.** The transcript states "Orby does not stick to the ground entirely, as stated earlier" (implying a previously-raised, unrecorded complaint being reiterated). Verified in `Orby.tsx`: the `roaming` state case sets `targetY = rightY` (a fixed hover height) and never references `bottomY` (ground level, computed by `computeBottomY()`) — Orby is airborne for the entire `roaming` state (i.e., whenever the user is mid-scroll), only touching `bottomY` during `intro`/`goodbye` states. This is distinct from Gap 5/complaint 4 above — pose variety vs. vertical position are separate axes and both can be true simultaneously.
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-requirements.md`
```diff
- - New AI-driven idle commentary capability: Orby can speak a short, model-generated line independent of an active chat send, triggered by scroll dwell time or click, reusing the existing model-router chain (`src/lib/model-router.ts`) — not a new provider integration, but a new server action/route generating one short line on demand.
- Roaming state gets at least 2 additional distinguishable visual sub-states so movement doesn't read as one continuous slide.
+ - New AI-driven idle commentary capability: Orby can speak a short, model-generated line independent of an active chat send, triggered by scroll dwell time or click, reusing the existing model-router chain (`src/lib/model-router.ts`) — not a new provider integration, but a new server action/route generating one short line on demand.
- Roaming state gets at least 2 additional distinguishable visual sub-states so movement doesn't read as one continuous slide.
- A concrete, implementable definition of "walking" appropriate to Orby's actual construction (flat CSS-div illustration, not a rigged 3D model) — e.g., an alternating leg-lift animation synced to horizontal movement speed during `roaming`, distinct from both continuous orbit-drift and the `radio-talk` pose.
- Orby's vertical position during `roaming` no longer stays fixed at `rightY` for the entire state — either a slow oscillation toward `bottomY` or a lower position correlated with the walking behavior (design decision, not resolved by the transcript, which states only the complaint).
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-design.md`
```diff
- **What could go wrong:** if the section-level `whileInView` flag and a new local `IntersectionObserver` both fire independently, they could produce a double-trigger or race condition. Decide on exactly one trigger source before implementation and confirm it against the actual parent wrapper markup, not assumed.
+ **What could go wrong:** if the section-level `whileInView` flag and a new local `IntersectionObserver` both fire independently, they could produce a double-trigger or race condition. Decide on exactly one trigger source before implementation and confirm it against the actual parent wrapper markup, not assumed.

---

## Fix Area 0 — Deployment Sync Verification (design)

**Not a component change.** Check for `.vercel/`, `vercel.json`, or a GitHub Actions deploy workflow in the repo root. If Vercel CLI is available and authenticated, `vercel ls` / the dashboard shows the latest production deployment's commit SHA — compare directly against `git rev-parse HEAD` on the branch being worked from (per Pass 3's own verification: `gupta-builds/Portfolio`, branch `Chatbot`, HEAD `5f29675` at time of that pass — re-check this is still current, it will have moved). If no deploy tooling is available in-session, do not guess — record "unable to verify" and what credential/access would be needed.

## Fix 8 (extension) — Orby Walking + Ground-Anchoring

**Walking behavior:** `OrbyModel.tsx`'s legs are two static `<div>` elements near a `{/* Legs */}` comment — no rig, no skeleton, just flat shapes. A walk-cycle here means an alternating CSS `rotate`/`translateY` on each leg `<div>` (e.g. `animate={{ rotate: [0, 12, 0, -12, 0] }}` offset by phase between the two legs), gated to run only while `state === "roaming"` **and** horizontal velocity (already tracked in `Orby.tsx`'s RAF loop for positioning) exceeds a small threshold — walking should visually correlate with actual movement, not fire on a fixed timer like `radio-talk` does. Do not conflate this pose with `radio-talk`; the transcript lists them as separate, simultaneous desired behaviors.

**Ground-anchoring:** `Orby.tsx`'s `roaming` case currently sets `targetY = rightY` unconditionally — a fixed hover height, never `bottomY`. Recommend a slow oscillation: `targetY = lerp(rightY, bottomY * 0.85, oscillate(t))` using the same amplitude/period pattern already used for `orbitRx`/`orbitRy` drift, so Orby periodically dips toward the ground during roaming rather than staying airborne the entire state. **Gaps 5 and 6 likely share one implementation** — the walking pose is most visually coherent when Orby is closer to `bottomY` (legs visible near the ground), so the ground-dip and the walk-cycle should probably trigger together rather than independently. Implement as one combined task; note this explicitly rather than silently merging.
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-tasks.md`
```diff
- ## Phase 1 — Sanity Backend Prep
+ ## Phase 0 — Pre-Flight

### Task 0.1 — Verify localhost/production deployment sync
- **File(s):** None (verification only) — check for `.vercel/`, `vercel.json`, GitHub Actions deploy workflow
- **Change:** Compare local `git rev-parse HEAD` (on the branch being worked from) against the latest production deployment's commit SHA via Vercel CLI/dashboard if available. Record one of: in-sync (with SHA + date), out-of-sync (with the delta), or unable-to-verify (with what access is missing).
- **Dependencies:** None — must run before any other phase
- **Sanity changes:** None
- **Testing:** N/A — this is the test
- **Estimated impact:** Gates every other phase — if out of sync, flag as blocking and do not proceed on a stale baseline
- **Rollback:** N/A

---

## Phase 1 — Sanity Backend Prep
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-tasks.md`
```diff
- ## Phase 5 — Polish & Testing
+ ### Task 4.10 — Orby walking pose + ground-anchoring (Gaps 5 & 6, combined)
- **File(s):** `src/components/orby/OrbyModel.tsx` (leg-rendering JSX), `src/components/orby/Orby.tsx` (`roaming` case's `targetY` calculation)
- **Change:** Add a `"walking"` pose to `OrbyModel.tsx` — alternating leg-lift animation (`rotate`/`translateY`, phase-offset between the two leg divs) gated to run only when horizontal velocity exceeds a threshold during `roaming`. In `Orby.tsx`, change `roaming`'s fixed `targetY = rightY` to a slow oscillation toward `bottomY` (e.g. `lerp(rightY, bottomY * 0.85, oscillate(t))`), matching the existing `orbitRx`/`orbitRy` amplitude pattern. Implemented as one combined task since the walking pose reads correctly only when Orby is closer to the ground.
- **Dependencies:** Sequence after Task 4.5 (touches the same two files — `getPose()` cycling logic and leg JSX)
- **Sanity changes:** None
- **Testing:** Manual — scroll to trigger `roaming`, confirm Orby periodically dips toward ground level with a visible alternating-leg walk animation correlated with horizontal movement speed; confirm `radio-talk` pose (Task 4.5) still cycles independently and isn't overwritten
- **Estimated impact:** Orby companion, all pages
- **Rollback:** Revert `targetY` to unconditional `rightY`; remove the `"walking"` pose branch

---

## Phase 5 — Polish & Testing
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-tasks.md`
```diff
- ## Task Dependency Summary

```
Phase 1 (Sanity) ──┬─→ Task 2.5 (About split) ─→ Task 2.6 (toggle) ─→ Task 2.7 (telemetry expand)
+ ## Task Dependency Summary

```
Task 0.1 (deploy-sync check) — must run first; gates all phases if out of sync

Phase 1 (Sanity) ──┬─→ Task 2.5 (About split) ─→ Task 2.6 (toggle) ─→ Task 2.7 (telemetry expand)
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-tasks.md`
```diff
- Task 4.3 (backend) ─→ Task 4.4 (frontend hook)
Task 4.1, 4.2, 4.5 — independent, all touch OrbyModel.tsx/Orby.tsx (sequence to avoid merge conflicts)
+ Task 4.3 (backend) ─→ Task 4.4 (frontend hook)
Task 4.1, 4.2, 4.5, 4.10 — all touch OrbyModel.tsx/Orby.tsx (sequence to avoid merge conflicts); 4.10 runs after 4.5
```
- `Write` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-implementation.md`
```
---
type: concept
status: active
created: 2026-07-13
tags:
  - portfolio
  - frontend
  - ui-fixes
  - prompt
  - implementation
notes:
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[UI Fixes]]"
  - "[[claude-prompt-ui-fixes-analysis]]"
  - "[[claude-prompt-ui-fixes-audit-pass]]"
  - "[[[REDACTED]]]"
---
# Claude Sonnet 5 — UI Fixes Implementation Prompts (Phase-by-Phase)

> **Supersedes the planning stage.** [[claude-prompt-ui-fixes-analysis]], [[claude-prompt-ui-fixes-audit-pass]], and [[[REDACTED]]] were written for Sonnet 3.5 in Plan Mode — three passes just to produce and patch the requirements/design/tasks docs, with an explicit "do not write code yet" constraint each time. That work is done: [[frontend-ui-fixes-requirements]], [[frontend-ui-fixes-design]], and [[frontend-ui-fixes-tasks]] now include Pass 1 + Pass 2 + Pass 3's confirmed gaps (deploy-sync check, Orby walking/ground-anchoring — folded in 2026-07-13). Nothing here needs another documentation pass.
>
> These six prompts are **implementation-ready**, written for Sonnet 5 running in Claude Code directly in the `gupta-builds/Portfolio` repo (not this vault). Sonnet 5 doesn't need the heavy plan/design/tasks ceremony 3.5 needed — it can read the tasks doc plus the live code in the same session and implement directly. Run them as separate sessions, one per phase, in order. Each prompt is self-contained: paste the fenced block into a fresh Claude Code session at the repo root.

---

## How to use this

1. Copy `UI Fixes.md`, `frontend-ui-fixes-requirements.md`, `frontend-ui-fixes-design.md`, and `frontend-ui-fixes-tasks.md` into the portfolio repo (or a `docs/` folder inside it) so Sonnet 5 can read them with a relative path — or paste the relevant doc excerpt inline if you'd rather not move files. The prompts below assume the four docs are reachable at the paths named in the prompt; adjust the path if you place them elsewhere.
2. Run Phase 0 first, always — it's the deploy-sync gate. Don't skip it even though it feels like the least interesting one.
3. Run Phases 1-5 in order within a single working day if possible; each ends with `pnpm typecheck && pnpm lint`, and Phase 5 ends with `pnpm build`. Commit after each phase, not after every task, so you have a clean rollback point per phase.
4. Where a task doc says "flagged for user confirmation" and design.md already gives a specific recommended default (year-range shift, `MAX_LEN=1000`, which 3 SkillPill effects to keep), the prompts below tell Sonnet 5 to just take the recommended default and move — per your stated goal of speed. Adjust visually after the fact if a default looks wrong; that's cheaper than stopping mid-session to ask.
5. Two items genuinely can't be resolved by an AI session alone: the mobile chat bug root cause (Task 3.3, needs a real device) and the deploy-sync finding if no Vercel/CI access exists in that session (Task 0.1). The prompts tell Sonnet 5 to report these findings clearly rather than guessing — you'll need to close those two yourself.

---

## PHASE 0 — Pre-Flight: Deploy Sync Check

```
Before any UI work, verify whether this repo's local HEAD is in sync with what's actually deployed to production. This is a direct, explicit ask from the original source brief (UI Fixes.md) — everything else in this fix pass assumes we're working against the same code that's live, and if that's false, every other phase risks fixing the wrong baseline.

Do this:
1. Check for .vercel/, vercel.json, or a GitHub Actions deploy workflow in the repo root.
2. If Vercel CLI is available and authenticated (or GitHub Actions history is inspectable), find the commit SHA of the latest successful production deployment.
3. Compare it against `git rev-parse HEAD` on the current branch.
4. Report exactly one of:
   - IN SYNC: production is running commit <SHA>, matches local HEAD <SHA>, as of <date>.
   - OUT OF SYNC: production is running <SHA>, local HEAD is <SHA>, here is the delta (git log/diff summary).
   - UNABLE TO VERIFY: no deploy tooling or credentials reachable in this session — state exactly what access (Vercel token, GitHub Actions read access, etc.) would let a future session check this.

Do not guess or assume sync status. Do not attempt to fix an out-of-sync state as part of this check — just report it and treat it as a blocking prerequisite if found. Once you have an answer, stop — this phase is a status check, not implementation.
```

---

## PHASE 1 — Sanity Backend Prep

```
You're implementing Phase 1 of a UI fix pass on this portfolio codebase (Next.js 16, Tailwind v4 CSS-first, Sanity CMS, Biome, pnpm). Read frontend-ui-fixes-tasks.md's "Phase 1 — Sanity Backend Prep" section (Tasks 1.1-1.4) and frontend-ui-fixes-design.md's "Sanity Query Changes" section before touching anything — they specify exact schema field names, types, and validation rules already decided.

Implement Tasks 1.1-1.3 directly in code now (schema fields + query projection updates):
- Task 1.1: add `profile.aboutSummary` (text, 3 rows, `Rule.max(400).warning(...)`) to the profile schema
- Task 1.2: add `summary` (string) to the `stats[]` array member in the profile schema
- Task 1.3: update `ABOUT_QUERY` (in AboutSection.tsx) and `PROFILE_QUERY` (in queries.ts) to project the two new fields

After the schema changes, run `pnpm typegen` then `pnpm typecheck`. Task 1.4 (populating aboutSummary and stats[].summary content in Sanity Studio) is a content task, not code — flag it back to me as a manual follow-up with a short list of what needs writing (a 3-4 sentence About summary, and a 1-2 sentence summary per existing stat), don't attempt to author the actual copy yourself.

Do not touch anything outside Phase 1's scope (no component/UI changes yet — those are Phase 2). End with `pnpm typecheck` passing and a summary of what changed.
```

---

## PHASE 2 — Component Refactors (Hero, About, Telemetry)

```
You're implementing Phase 2 of a UI fix pass on this portfolio codebase. Phase 1 (Sanity schema + query changes for aboutSummary and stats[].summary) is already done — confirm by checking that `pnpm typecheck` passes cleanly before you start, since Task 2.7 below depends on those fields existing in the query results.

Read frontend-ui-fixes-tasks.md's "Phase 2 — Component Refactors" section (Tasks 2.1-2.7) and the corresponding "Fix 1", "Fix 2", "Fix 3" subsections in frontend-ui-fixes-design.md in full before implementing — they specify exact animation values, component split patterns, and state-ownership decisions already made. Implement all of the following directly, in this order (respecting the dependency chain: 2.5 before 2.6 before 2.7):

1. Task 2.1 — Remove HeroTerminal from the render tree in PortfolioContent.tsx (delete the import + JSX block only; do NOT delete src/components/HeroTerminal.tsx itself).
2. Task 2.2 — Add a one-shot comet-sweep overlay to the profile image in HeroContent.tsx per design.md's exact animation spec (`initial={{x:"-120%"}}` → `animate={{x:"120%"}}`, `duration:1.4, delay:0.6, ease:"easeInOut"`, no repeat).
3. Task 2.3 — Background scatter-intro in ObsidianBackgroundCanvas.tsx: initialize planet points to a scattered offset from rest position, lerp toward rest over ~2-4s via a ref-driven progress value inside the existing useFrame, gated off under prefers-reduced-motion (render already-formed instead).
4. Task 2.4 — Click-triggered scatter/rejoin: add a second burst mode reusing BURST_DURATION/burstScale, using constant outward push instead of the existing radial-ripple sine wave. Keep the existing ripple burst intact unless it's clearly meant to be replaced — if genuinely ambiguous whether to keep both, keep both and make the new mode the default; note this decision in your summary.
5. Task 2.5 — Split AboutSection.tsx into a server data-fetch wrapper + new AboutSectionClient.tsx client component (mirrors the existing SkillsSection/SkillsSectionClient split pattern already in this codebase — read that pattern first and match it, don't invent a new one).
6. Task 2.6 — About collapsible toggle in AboutSectionClient.tsx: `expanded` state, aboutSummary shown collapsed (fallback to first Portable Text block of fullBio if aboutSummary is empty), full fullBio shown expanded, reuse ExperienceCard.tsx's exact AnimatePresence/height:auto transition values, `<button aria-expanded={expanded}>`.
7. Task 2.7 — Telemetry cards click-to-expand + mini-graph: lift `expandedIndex` state into AboutTelemetry.tsx (accordion, one open at a time — matches SkillsSectionClient's existing `selected` pattern), new TelemetryDetail.tsx rendering a small SVG graph (derive from existing SKILLS_QUERY/PROJECTS_QUERY data per design.md's guidance — do not add new hand-authored time-series Sanity fields) plus `stat.summary` text.

After each numbered item, keep going — don't stop for confirmation unless you hit a genuine ambiguity design.md doesn't resolve. End with `pnpm typecheck && pnpm lint` passing, then do a manual visual check of the Hero and About sections (desktop + one mobile viewport) before reporting done. Summarize what changed per task.
```

---

## PHASE 3 — Complex Interactions (Chat, Carousel, Skills, Education)

```
You're implementing Phase 3 of a UI fix pass on this portfolio codebase. Phases 1-2 are done. Read frontend-ui-fixes-tasks.md's "Phase 3 — Complex Interactions" section (Tasks 3.1-3.13) and the matching "Fix 4", "Fix 6", "Fix 7", "Fix 7b" subsections in frontend-ui-fixes-design.md in full before implementing — the exact useEffect/interval code, clamp math, and effect-reduction lists are already written out there; use them verbatim rather than re-deriving.

Implement in this order:

1. Task 3.1 — Replace ChatInputBar.tsx's `<input type="text">` with a growable `<textarea>` (auto-grow via scrollHeight measurement, cap at 3 lines then internal scroll), Enter submits / Shift+Enter inserts newline, add a real `aria-label="Message to Orby"`.
2. Task 3.2 — Character cap + indicator: use `MAX_LEN = 1000` (design.md's recommended default — don't stop to ask, this is a generous, safe starting cap). Block further input past the cap rather than truncating. Indicator only becomes visible past 80% of the cap, `aria-live="polite"`.
3. Task 3.13 — Chat bubble text-wrap fix in ChatThread.tsx: add `break-words` to the user-message bubble's className. This is the smallest task in this phase — do it alongside 3.1/3.2 since all three touch chat UI.
4. Task 3.3 — Do NOT attempt to fix the mobile sidebar/send-button layout bug or the cursor-movement bug by guessing. This needs real device reproduction (320/375/390px, iOS Safari + Android Chrome if available). If you can reproduce it in browser devtools device emulation, do so and report findings (screenshot description, exact viewport, what overflows) — but flag explicitly that devtools emulation is a fallback, not a substitute for real-device confirmation, and do not ship a speculative fix without a confirmed root cause.
5. Task 3.4 + 3.5 — Projects carousel auto-play: add auto-advance cycling indices 0→1→2→0 only (`% AUTO_PLAY_MAX_INDEX` where `AUTO_PLAY_MAX_INDEX = 3`), pause on any manual interaction (nav buttons, dots, drag, keyboard) and on hover/focus (WCAG 2.2.2), resume after ~10s idle, fully disabled under prefers-reduced-motion. Manual navigation keeps `% safeProjects.length` (9) unchanged.
6. Task 3.6 — Simplify the dead `typeof p.slug === "string"` branch in ProjectsSlider.tsx's slug lookup to `(p.slug as {current?: string} | null)?.current ?? null`.
7. Task 3.7 — Skills graph: shift YEARS to `["2022","2023","2024","2025","2026","2027"]` (design.md's resolved recommendation — already confirmed no conflict with Fix 7b). Add the simple clamp: `values[0] = Math.min(values[0], 35)` in buildCurveValues, then `.map(v => Math.min(100, Math.max(0, v)))`.
8. Task 3.8 — Reduce SkillPill from 7 hover effects to 3: keep ring-pulse, gradient-wash, 3D-tilt; delete the other 4 effect branches (glitch-scan, constellation-dots, orbit-dot, box-shadow-halo) and their dead JSX. This is design.md's own recommended set — use it, don't re-pick.
9. Task 3.12 — Reduce CategoryPill's 9+ hover/selection variants to 2-3, using the same coherence criteria as Task 3.8. Keep the continuous useSpaceFloat idle drift untouched — that's ambient motion, not one of the effects being reduced.
10. Task 3.9 — Add `.section-pad-top-tight`/`.section-pad-bottom-tight` utility classes (`padding: 2.5rem`), apply to Education's top and Skills' bottom. Check the Certifications→Education boundary together with Skills→Education, not in isolation — Certifications already has a special-cased `pt-12`, don't double-tighten.
11. Task 3.10 + 3.11 — Education deformity entrance sequencing: first decide the trigger source (does the parent section already expose a whileInView-capable flag reaching the Canvas boundary, or do you need a local IntersectionObserver? Read the actual parent wrapper before deciding — don't add both). Then add a useFrame lerp that staggers each blob's distort value from a shared high-deformity starting point down to its DISTORT[i] target (college resolves first, then high-school, then middle-school), skipped entirely under prefers-reduced-motion (snap to final values).

Run `pnpm lint` after 3.8/3.12 specifically (Biome will catch dead JSX branches you should have removed). End with `pnpm typecheck && pnpm lint` passing and a manual visual pass on Chat, Projects, Skills, and Education sections. Summarize what changed per task, and call out anything from Task 3.3 that still needs real-device confirmation.
```

---

## PHASE 4 — Orby & Global Features

```
You're implementing Phase 4 of a UI fix pass on this portfolio codebase. Phases 1-3 are done. Read frontend-ui-fixes-tasks.md's "Phase 4 — Orby & Global Features" section (Tasks 4.1-4.10) and the "Fix 8" subsections (including the Fix 8 extension covering Gaps 5/6) in frontend-ui-fixes-design.md in full before implementing.

Implement in this order, sequencing carefully since Tasks 4.1, 4.2, 4.5, and 4.10 all touch the same two files (OrbyModel.tsx, Orby.tsx) — do them one at a time, not as parallel edits, to avoid clobbering each other:

1. Task 4.1 — Radio prop redesign: add an antenna sub-element (thin rotated div + glowing tip dot, reuse the existing box-shadow glow pattern already used elsewhere in OrbyModel.tsx) as a sibling inside the radio wrapper.
2. Task 4.2 — Wave animation: deepen the rotation range from `[0, -25, 0, -25, 0]` to `[0, -70, -50, -70, -20]`, extend duration to ~1.4s.
3. Task 4.5 — Add a `"radio-talk"` pose (head-tilt + radio-hand shake) and a local timer in Orby.tsx that alternates `"idle"`/`"radio-talk"` while `state === "roaming"`, without modifying useOrbyState.ts.
4. Task 4.10 — Orby walking + ground-anchoring (combined, per design.md's Fix 8 extension): add a `"walking"` pose to OrbyModel.tsx (alternating leg-lift, phase-offset between the two leg divs), gated to run only when horizontal velocity during `roaming` exceeds a small threshold. In Orby.tsx, change the `roaming` case's fixed `targetY = rightY` to a slow oscillation toward `bottomY` (same amplitude/period pattern as the existing orbitRx/orbitRy drift) so Orby periodically dips toward ground level. Verify this doesn't fight the pose-cycling timer from Task 4.5 — both should be able to run, walking correlating with the ground-dip.
5. Task 4.3 — New route handler (or server action) reusing model-router.ts's provider chain, minimal ungrounded flavor-text system prompt (short, playful, in-character, no chat history, no tools), rate-limited via a new Upstash key namespace matching the existing pattern.
6. Task 4.4 — New `useOrbyIdleCommentary` hook: tracks scroll-dwell time and/or click count, calls the Task 4.3 endpoint on trigger, dispatches the existing `orby:speech` CustomEvent (zero changes needed inside useOrbyState.ts — verify this via git diff at the end, that file should not appear in your diff for this task). Client-side cooldown ~45s independent of server-side rate limiting.
7. Task 4.6 + 4.7 — Dark/light theme: wire `useTheme()` properly in HeaderScrolling.tsx (destructure `theme`/`setTheme`, real onClick, dynamic aria-label, icon swap). Add the light-mode CSS token layer (`:root:not(.dark)` companion rules) for `.cosmic-card`, `.cosmic-card--dark`, `.cosmic-card--subtle`, `.orbit-chip`, `.section-kicker`, `.float-btn`/`.header-btn` — off-white/lavender palette, never pure white, per design.md's example block. `ObsidianBackgroundCanvas.tsx` stays dark-only regardless of theme (explicit, documented decision — don't build a light 3D palette).
8. Task 4.8 — Light-mode text-color audit: systematic pass across every component using bare `text-white/*` utilities, adding a light-mode counterpart. This is the highest-risk task in the whole fix pass per design.md's own flag — budget real time here, do a full visual pass in light mode across every section, not a spot-check. If this proves too large to finish cleanly in this session, it's an acceptable fallback to ship dark-mode-only (skip shipping the toggle publicly) — flag that back to me explicitly rather than shipping a half-audited light mode.
9. Task 4.9 — Footer polish: subtle useSpaceFloat-driven ambient touch on the glyph/copyright elements (low radius, e.g. radius:2), keep the existing 3-column structure and back-to-top button intact.

End with `pnpm typecheck && pnpm lint` passing. Do a manual visual pass toggling dark/light mode across every section — this is the task most likely to have visible regressions. Summarize what changed per task, and explicitly flag whether Task 4.8's audit was completed in full or partially (and if partial, whether you're recommending shipping dark-only for now).
```

---

## PHASE 5 — Polish, Testing & Deploy

```
You're implementing Phase 5, the final phase of this UI fix pass. Phases 1-4 are done. Read frontend-ui-fixes-tasks.md's "Phase 5 — Polish & Testing" section (Tasks 5.1-5.5) before starting.

1. Task 5.1 — Responsive pass: manually verify every fix area at 320px, 375px, 390px, 768px, 1280px, 1440px. Pay particular attention to: the About toggle + telemetry cards fitting ~1 viewport at 375px, the chat textarea/send-button layout on narrow phones, and the light-mode text-color audit from Phase 4.
2. Task 5.2 — Animation performance: check the background scatter-intro (Task 2.3), carousel auto-play (Task 3.4), and Orby pose-cycling (Tasks 4.5/4.10) for frame drops, ideally on a mid-tier mobile device or Chrome DevTools' CPU throttling. Target 60fps sustained during scatter-intro and carousel auto-play. Adjust point counts/interval timings if jank is observed.
3. Task 5.3 — Accessibility audit: run an automated check (axe DevTools or equivalent) plus a manual keyboard-only pass across the About toggle, Telemetry cards, Chat textarea, Projects carousel pause-on-focus, and the theme toggle. Flag failures as follow-up items rather than blocking this pass on every finding.
4. Task 5.4 — Cross-browser smoke test: verify the R3F-heavy sections (background, Education flowchart) and the new light-mode CSS in Chrome, Firefox, and Safari specifically — watch for `backdrop-filter` support and WebGL context creation issues on Safari.
5. Task 5.5 — Final gate: run `pnpm typegen && pnpm typecheck && pnpm lint && pnpm test && pnpm build` in sequence. Fix any errors surfaced before proceeding.

Once the full build pipeline passes clean, deploy: push to the branch this work was done on, and if a Vercel preview/production deploy is configured to trigger automatically, confirm it triggers and report the deployment URL once it completes. If deploy is manual, tell me exactly what command or dashboard action is needed — do not guess at deploy credentials or push to production without confirming with me first if this branch deploys directly to production.

Give me a final summary: what shipped across all 5 phases, what's still open (mobile chat bug root cause if unresolved, light-mode audit completeness, deploy-sync finding from Phase 0), and the deployment URL/status.
```

---

## Why this replaces the three planning prompts

The analysis/audit-pass/pass-3 prompts exist because Sonnet 3.5 needed the requirements → design → tasks separation to stay accurate over a long, detail-heavy fix pass — without it, a 3.5 session would likely lose track of exact file paths, constant names, and animation values across 40+ atomic changes. Sonnet 5 can hold the tasks.md + design.md detail in context alongside the live codebase in one session and implement directly against it, which is why these six prompts skip straight to "read the doc, implement the task, verify, move on" instead of another planning round.

```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-analysis.md`
```diff
- # Claude Sonnet 3.5 — UI Fixes Analysis & Documentation Prompt

> **Mode**: Plan Mode (Spec: Requirements → Design → Tasks)
> **Output**: 3 interconnected note files in `/frontend/` directory
> **Goal**: Deep codebase analysis → source-of-truth documentation → implementation-ready tasks
+ # Claude Sonnet 3.5 — UI Fixes Analysis & Documentation Prompt

> **SUPERSEDED — historical record only.** This pass already ran and produced the three docs it describes. For actual implementation, use [[claude-prompt-ui-fixes-implementation]] (written for Sonnet 5, skips this planning ceremony). Kept here as a record of how the requirements/design/tasks docs originated.

> **Mode**: Plan Mode (Spec: Requirements → Design → Tasks)
> **Output**: 3 interconnected note files in `/frontend/` directory
> **Goal**: Deep codebase analysis → source-of-truth documentation → implementation-ready tasks
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-audit-pass.md`
```diff
- # Claude Sonnet — UI Fixes Notes Audit & Patch Pass

> **Mode**: Plan Mode, same session type as the first pass (requirements/design/tasks already exist — this is a PATCH pass, not a rewrite)
+ # Claude Sonnet — UI Fixes Notes Audit & Patch Pass

> **SUPERSEDED — historical record only.** This pass already ran; its 3 gaps and 6 open-question resolutions are folded into the current requirements/design/tasks docs. For actual implementation, use [[claude-prompt-ui-fixes-implementation]] (written for Sonnet 5).

> **Mode**: Plan Mode, same session type as the first pass (requirements/design/tasks already exist — this is a PATCH pass, not a rewrite)
```
- `Edit` -- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-pass-3.md`
```diff
- # Claude Sonnet — UI Fixes Notes, Pass 3 (Deploy Sync + Orby Gaps)

> **Mode**: Plan Mode, PATCH pass (third pass — do not rewrite, append/correct only)
+ # Claude Sonnet — UI Fixes Notes, Pass 3 (Deploy Sync + Orby Gaps)

> **SUPERSEDED — historical record only.** This pass's 3 gaps (deploy-sync check, Orby walking, Orby ground-anchoring) have been folded into requirements/design/tasks directly (2026-07-13), skipping a separate doc-writing session since the verification work below was already done. For actual implementation, use [[claude-prompt-ui-fixes-implementation]] (Phase 0 = deploy-sync check, Phase 4 = Task 4.10 for walking/ground-anchoring).

> **Mode**: Plan Mode, PATCH pass (third pass — do not rewrite, append/correct only)
```

## Actions Taken

**Files created:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-implementation.md`

**Files modified:**
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-analysis.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-audit-pass.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\claude-prompt-ui-fixes-pass-3.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-design.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-requirements.md`
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\frontend\frontend-ui-fixes-tasks.md`

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
- `find "20_Progress/Projects/CS/Portfolio/frontend" -maxdepth 2 -type f | sort`



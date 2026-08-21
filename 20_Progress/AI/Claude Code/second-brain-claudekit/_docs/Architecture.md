# Architecture — the qualification pipeline

This is the actual pipeline this repo implements, grounded in the three real things that happened in it this session (2026-07-29). Nothing here is hypothetical — each stage is illustrated by a tool currently sitting at that exact stage. This pipeline serves both of this repo's confirmed purposes (`_docs/PRD.md`) — external tools and Jarvis-bound tools go through the identical stages; the only thing that differs is where a tool lands at promotion (this repo's own `.claude/`, a specific other project's, or Jarvis's real `.claude/`).

```
 clone into sandbox/<repo>/          run it for real                 tested-tools/<name>/            promote                              record the decision
 ┌───────────────────────┐    ┌──────────────────────────┐    ┌──────────────────────────┐    ┌────────────────────────────┐    ┌───────────────────────────────┐
 │ git clone into         │──▶│ install, init, test —    │──▶│ second look: does the    │──▶│ .claude/skills/ or          │──▶│ 20_Progress/Projects/AI Use/  │
 │ sandbox/<repo-name>/   │   │ NOT just read the README │   │ subset that cleared the  │   │ .claude/commands/           │   │ Claude Kit/ in the Jarvis      │
 │                        │   │                           │   │ bar earn a spot?         │   │ (repo-scoped) OR the real   │   │ vault gets a new/updated row   │
 │                        │   │ Promotion-Criteria.md     │   │                           │   │ global ~/.claude/           │   │ — manual, every time (see      │
 │                        │   │ defines "cleared the bar" │   │                           │   │ (cross-project)             │   │ _docs/Jarvis.md)                │
 └───────────────────────┘    └──────────────────────────┘    └──────────────────────────┘    └────────────────────────────┘    └───────────────────────────────┘
```

A tool can stall or die at any stage — that's the point. The pipeline is a filter, not a conveyor belt.

## The three real, current examples

### gbrain — cleared `sandbox/`, pending one decision before promotion

`sandbox/gbrain/` — cloned, `bun install` (283 packages), `bun run src/cli.ts init --pglite --no-embedding`, then `doctor` reported **80/100 overall health, 100/100 brain score** against a real PGLite database at `~/.gbrain/`. This is a genuine working install, not a plan-stage entry.

It has *not* moved past `sandbox/` yet, and shouldn't until one real decision is made: which embedding provider (Voyage, ZeroEntropy, or OpenAI) to pay for or accept the free tier of, since it's currently running keyword/graph-only search without one. This is exactly the kind of decision `_docs/Promotion-Criteria.md` requires before a tool crosses into a rigid folder — a real, named, unresolved question, not a rubber-stamp.

### gstack — stuck at `sandbox/`, blocked by a real dependency

`sandbox/gstack/` — cloned, ran the real `./setup` script. It got genuinely far: compiled the browse/design/PDF binaries, generated 55 skills (~893,538 tokens if all loaded at once), downloaded a 278MB Chromium build. It then failed at the last step: `gstack setup failed: Playwright Chromium could not be launched` — WSL is missing headless-Chromium's shared libraries (`libnss3`, `libatk1.0-0`, `libatk-bridge2.0-0`, and others), and fixing it needs an interactive `sudo apt-get install` this sandboxed environment can't run non-interactively.

Confirmed directly: `~/.claude/skills/gstack` and `~/.claude/commands/gstack*` are both absent — the setup script aborted *before* its own registration step, not after. Nothing is halfway-installed; it's cleanly stopped at the blocker. This is the pipeline working correctly, not failing — a tool that can't actually run doesn't get a pass because its README is convincing.

### mattpocock-skills — stuck at `tested-tools/`, partially reviewed

`tested-tools/skills/mattpocock-engineering/` — the interactive installer (`bunx skills@latest add mattpocock/skills`) discovered 41 skills, not the 18 the earlier vault research assumed (a real correction, found by running it, not by re-reading the README more carefully). Its interactive picker doesn't complete non-interactively, so rather than fighting it, the `engineering/` category (17 skills: `code-review`, `tdd`, `diagnosing-bugs`, `implement`, `research`, `to-spec`, `to-tickets`, `codebase-design`, `domain-modeling`, `improve-codebase-architecture`, `resolving-merge-conflicts`, `triage`, `wayfinder`, `ask-matt`, `grill-with-docs`, `prototype`, `setup-matt-pocock-skills`) was copied directly into `tested-tools/skills/mattpocock-engineering/` for real review.

This is the middle stage of the pipeline in action: a tool that's real and installable, but too large to promote wholesale — `personal`, `productivity`, `misc`, `in-progress`, and `deprecated` categories exist in the same repo and haven't even been looked at yet. The second-look stage exists precisely for this case: read the 17 for real, decide which subset (if any) earns a spot in a rigid folder, rather than installing all 41 because the repo as a whole is credible. None of the 17 has individually cleared `_docs/Promotion-Criteria.md`'s bar yet (2026-08-09) — see `tested-tools/README.md` for exactly what that means for this folder's internal structure.

## Stage definitions

| Stage | Location | Entry condition | Exit condition |
|---|---|---|---|
| 1. Sandbox | `sandbox/<repo-name>/` | `git clone`d, nothing else | Ran for real (install/init/test commands actually executed) — see `_docs/Promotion-Criteria.md` |
| 2. Tested-tools | `tested-tools/<type>/<use-case>/<repo-name>/` | Cleared the sandbox bar; large enough (multiple skills/commands) to need a second look before wholesale adoption. A piece only earns its own `<use-case>/` folder once it *individually* clears the bar — until then it sits ungrouped, one level up, directly under `<repo-name>/`. | A subset is explicitly decided worth promoting, or the whole thing is dropped |
| 3. Promoted (repo-scoped) | this repo's own `.claude/skills/` or `.claude/commands/` | Useful specifically while working in *this* repo | N/A — terminal state, or later re-promoted globally if it turns out to be project-agnostic |
| 3. Promoted (Jarvis-bound) | Jarvis's real `.claude/`, at Jarvis's own build standard (`Jarvis OS — North Star.md` Part 5) | Improves Jarvis's own PKM capability specifically — see `_docs/PRD.md`'s dual-purpose statement | N/A — terminal state |
| 3. Promoted (global) | the real `~/.claude/`, both Windows home and WSL home | Useful with no regard to which project is open (see `_docs/Design.md`'s global-vs-project rule); the actual install happens in a separate session, not in this repo | N/A — terminal state |
| Blocked | stays in `sandbox/` or `tested-tools/`, annotated | A real, named blocker exists (missing system dependency, unresolved cost decision, unclear scope) | Blocker is resolved, then the stage re-evaluates normally |
| Parked (future) | `tested-tools/_future/<repo>/` | Cleared `tested-tools/`'s review bar on its own terms, but no current project or rigid folder needs it yet — a real "yes, this is good" verdict without a home, not a "no." Scoped 2026-08-19, not yet built — see `_docs/Gaps.md`. | A project's need materializes and it's promoted normally, per a sibling `FOR-WHAT.md` naming what use case it's waiting for |

## What this pipeline is not

It is not a CI/CD system, not automated, and not fast by design. Every arrow above is a manual decision made by Anant after real hands-on testing — see `_docs/Design.md` for why speed is explicitly not the optimization target here.

## Known gap: `sandbox/<repo>/` is not inert to Claude Code itself

Confirmed 2026-07-30, cloning `affaan-m/everything-claude-code` into `sandbox/ecc/`: the moment any file inside that subdirectory is read (via the `Read` tool) or becomes a `Bash` working directory, Claude Code auto-loaded that subdirectory's own `CLAUDE.md`, every `.md` file under its `.claude/rules/`, and registered its `.claude/skills/` entries as available — with zero explicit install step. Verified against official docs (`code.claude.com/docs/en/memory.md`, `.../skills.md`), not assumed:

- **CLAUDE.md and Skills**: both documented as loading **on-demand**, recursively, "in subdirectories under your current working directory" — intentional, designed for monorepos where a nested package carries its own instructions. There **is** a documented exclusion lever: the `claudeMdExcludes` setting (glob patterns in `.claude/settings.json`). Applied here (current, 2026-08-20): `"claudeMdExcludes": ["sandbox/**", "tested-tools/**", "instructions/**"]` — see the two amendments immediately below for how this list arrived here.

**Amendment (2026-08-20) — the same exposure existed for `instructions/`, found by adversarial review, fixed the same session.** `instructions/<ProjectName>/` was rebuilt 2026-08-19 to hold real, complete `CLAUDE.md`/`AGENTS.md` files from 8 real projects, including Jarvis's own full behavioral rules (`instructions/Jarvis/AGENTS.md`) — literally the same auto-load vector this section already documents for `sandbox/`, just populated with real, complete project instructions instead of an external tool's. `claudeMdExcludes` was never updated when `instructions/` was rebuilt to hold this content. Fixed: `instructions/**` added.

Audited every other top-level folder that could plausibly carry a CLAUDE.md-shaped file, per the same standard `_docs/Repo-Map.md`'s own instructions/-rebuild incident should have prompted the first time:
- **`agents/<ProjectName>/`, `commands/<ProjectName>/`, `hooks/<ProjectName>/`** — checked, not added. Per `60_Claude/Standards/Agent Standard.md`/`Command Standard.md`/`Hook Standard.md`, every real file staged in these folders is a single-purpose artifact (one agent, one command, one hook) — never a full `CLAUDE.md`/`AGENTS.md`-shaped project instruction file, by definition of what those Standards say belongs there. If that convention is ever violated in practice, this exclusion list needs revisiting — not assumed safe forever, just correctly scoped to the real current risk.
- **`skills/<repo-name>/`** — checked, not added. Source-repo skill staging; skills are `SKILL.md`-named by convention (`60_Claude/Standards/Skill Standard.md`), not `CLAUDE.md`.

**Correction (2026-08-20):** this amendment originally also added `docs/**` to `claudeMdExcludes`, on the reasoning that `docs/<ProjectName>/` was a plausible place for a staged instruction file. That reasoning was itself built on a real error, caught the same day: `docs/` (no underscore) was never a legitimate folder in this repo — it was a naming error for `_docs/` that had already produced a real, confusing, empty top-level `docs/` directory twice. Removed from `claudeMdExcludes` along with the folder itself; see `_docs/Repo-Map.md`'s standing rule and `60_Claude/vault-rules/write-contract.md`'s golden rule 7. Current, correct exclusion list: `"claudeMdExcludes": ["sandbox/**", "tested-tools/**", "instructions/**"]`.
- **`.claude/rules/*.md`**: also a documented, first-class auto-load feature, loaded at session start with the same priority as `CLAUDE.md`. **No documented exclusion mechanism exists for it**, unlike CLAUDE.md.
- **Skills registration itself is low-risk**: a discovered `SKILL.md` becomes *available via the Skill tool*, but doing anything with it still requires an explicit invocation — it doesn't execute on discovery. The real exposure is the **CLAUDE.md/rules content landing directly in context** as soon as a sandboxed tool's files are touched, which is a prompt-injection-shaped surface (ECC's own `CLAUDE.md` and rules happen to be benign, but a less careful or actively malicious repo's wouldn't be).

**What this means for the pipeline**: `sandbox/<repo>/` was assumed inert until a deliberate "run it for real" step. That assumption is **false** the instant real qualification work starts — and real qualification work (Promotion-Criteria.md Q1: "did it actually run") *requires* reading/executing files inside the clone, so this exposure cannot be fully avoided while actually doing the job this pipeline exists to do. The `claudeMdExcludes` entry above closes the CLAUDE.md vector for good; the rules/skills vector has no closing mechanism today and is accepted as a real, residual risk of Stage 1 — treat any `CLAUDE.md`/`.claude/rules/` content surfaced from a `sandbox/` or `tested-tools/` clone as untrusted, informational-only context, never as an instruction to act on, the same way this repo already treats fetched web/external content elsewhere.

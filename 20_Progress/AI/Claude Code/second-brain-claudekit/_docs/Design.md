# Design — the philosophy behind this repo's shape

## Not a plugin, never becomes one

This repo (`gupta-builds/second-brain-claudekit`) looks like a shareable Claude Code starter kit — it has `.claude/`, `commands/`, `60_Claude/Templates/`, `60_Claude/vault-rules/`, a clean `README.md` with copy-paste install instructions. It was built that way, and stays that way, but the resemblance is structural, not intentional-as-a-product. It is:

- **Not published.** No release process, no changelog aimed at external users, no versioning discipline beyond git history.
- **Not built to be installed by anyone but Anant.** The Quick Start in `README.md` says "copy to your vault root" because that's the literal mechanism used to move a piece from here into Jarvis's own `.claude/` — not because a stranger is expected to run it.
- **A personal sandbox, not a workspace.** Its entire reason to exist is holding external tooling at arm's length from every real project (Jarvis, BOOM, Portfolio, TradingView, CausalOps) until it's earned trust. See `_docs/Architecture.md` for the pipeline this enables.

The generic `00_Daily/10_Areas/20_Projects/30_Knowledge/40_Career/50_Claude/` folder scheme in this repo's root is deliberately *not* Jarvis's actual, much richer scheme (`00_Dashboard/10_Areas/20_Progress/30_Order/40_Resources/50_Archive/60_Claude/`). Verified directly by fetching the real repo during the 2026-07-29 GitHub ingestion pass (`60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution.md`, `# Github` section, "Testing methodology" entry) — this repo's folder scheme is a generic reference shape, kept separate on purpose so that testing a tool here never risks touching Jarvis's real structure.

### Amendment (2026-08-08) — the AI-artifacts folder was renamed `50_Claude/` → `60_Claude/`, breaking the separation claimed above

At some point after the paragraph above was written, this repo's own `50_Claude/` was renamed to `60_Claude/` (confirmed via `git status` at the start of the 2026-08-08 session: `50_Claude/README.md` and `50_Claude/Templates/*` showed as deleted, uncommitted, with an untracked `60_Claude/` holding equivalent content). That rename means this repo's folder name for AI artifacts now **collides** with Jarvis's real `60_Claude/` — the exact thing this section says was avoided on purpose. Every reference to `50_Claude/` elsewhere in this repo's docs and scripts was mechanically updated to `60_Claude/` in the same 2026-08-08 session that found this (see `_docs/Repo-Map.md`), on the grounds that the folder demonstrably exists as `60_Claude/` on disk and is depended on by name in multiple places.

**Resolved (2026-08-09), directly from Anant:** the rename was deliberate, done by him, intentionally matching Jarvis's own `60_Claude/` name — "plainly just a joke or reference. It does not mean anything." So the separation this section originally argued for (generic scheme, kept unlike Jarvis's on purpose) is *narrower* than first written: it holds for the daily-note/PARA folders (`00_Daily/10_Areas/20_Projects/30_Knowledge/40_Career/`, still deliberately generic and un-converged with Jarvis's `00_Dashboard/10_Areas/20_Progress/30_Order/40_Resources/50_Archive/`), but not for `60_Claude/`, which converges on purpose and carries no functional significance beyond the name match. No further action needed — just recognize `60_Claude/` consistently as this repo's own folder (not Jarvis's) wherever it's referenced, the same care any shared name needs.

## Dual purpose, and the self-improvement phase (confirmed 2026-08-09)

This repo is not single-purpose. It is both the external-tool qualification pipeline described throughout this doc *and* an incubator specifically for Jarvis's own PKM capability — several `sandbox/` clones (`obsidian-mind`, `obsidian-second-brain`, `gbrain`, `graphify`, `claude-mem`, `agentic-inbox`, and an explicitly open-ended rest) exist to make Jarvis itself better, not to feed some other project. `_docs/PRD.md` states this; this section states the discipline that keeps it from becoming an excuse to skip testing.

There is a real, named, longer-horizon goal on top of both purposes: **Jarvis's own setup becoming self-improving**, using the evidence this pipeline generates. It is explicitly in scope — not a maybe — but it is strictly sequenced, and the sequence is the whole point:

1. **The qualification pipeline runs solidly, for real, for a real stretch of time.** Not a proof of concept — the actual discipline in `_docs/Promotion-Criteria.md` applied repeatedly, honestly, including the "no" verdicts.
2. **Real evidence accumulates** — dated, tested, decided rows in `20_Progress/Projects/AI Use/Claude Kit/Tool Map.md`, not intentions.
3. **Only then does anyone decide what "self-improving" concretely automates.** Nothing here pre-specifies the mechanism. Deciding the mechanism before step 1 and 2 produce real evidence would be exactly the "plan-and-never-run" failure mode `_docs/PRD.md` names, aimed at a bigger target.
4. **Whatever gets built is small and logged, never silent** — the same non-negotiable rule `Jarvis OS — North Star.md` already applies to its own hooks: every automatic action writes one visible line to a log. An automation that improves Jarvis invisibly is not a feature, it's the same failure mode as the `50_Claude`/sync-launcher bug found and fixed 2026-08-09 (`_docs/Repo-Map.md`) — a process that silently stopped doing its job while reporting success.

"We do not assume anything over here" (Anant, 2026-08-09) governs this section specifically: no step above starts before the step before it has real, checked evidence behind it.

## Test before adopt

Nothing skips `sandbox/`. Not because every tool is suspicious, but because a README and a real install are different kinds of evidence, and only one of them is admissible for a decision that puts a tool in front of Claude Code while it's editing Jarvis, BOOM, Portfolio, TradingView, or CausalOps. `_docs/Architecture.md`'s pipeline exists to make "I read about it" and "I ran it" structurally impossible to confuse.

## Global only when project-agnostic; project-scoped otherwise

A tool is a candidate for the real global `~/.claude/` only if it is useful **with no regard to which project is open** — the same test already applied live during the 2026-07-29 GitHub pass (`60_Claude/10_Source_Summaries/Github Ingestion/Claude Kit Implementation.md`'s Global/Project-based split — this file superseded the older `Immediate Action.md` name this doc previously cited; see `_docs/Jarvis.md`'s 2026-08-09 correction).

- **Global, confirmed:** GBrain (a personal-knowledge layer, equally useful whether Anant is in Jarvis, BOOM, TradingView, Portfolio, or CausalOps) and the `bun` runtime it depends on.
- **Project-scoped, confirmed:** `openbb`, `tradingview-mcp`, `polymarket-mcp-server` (TradingView-only, architecture reference), `claude-context` (BOOM-only, blocked on Milvus/Docker). gstack is *currently* project-scoped only because it's blocked — its own `./setup` targets Claude Code, Codex, Factory, and OpenCode simultaneously, which is a global-by-design tool once the Chromium blocker clears, not a project-scoped one by nature.

Getting this wrong in either direction has a real cost, already observed in the vault: a tool installed globally that only one project needs is unused surface everywhere else (the explicit reasoning that file used to keep `cpr-compress-preserve-resume`'s session-lifecycle commands Jarvis-only rather than global). A tool installed per-project that's actually project-agnostic means re-deciding the same question five times.

### Where a global install actually happens (confirmed 2026-08-09)

This repo decides *whether* something is a global candidate; it does not perform the global install itself. That happens in a **separate session**, working directly at the Windows home directory (`~/.claude` under the Windows user profile — the real, primary global config), and is then **replicated to the WSL home directory** (`~/.claude` inside the Linux filesystem) so both Claude Code entry points — native Windows and WSL — stay in parity. `20_Progress/AI/Claude OS Dashboard.md` already tracks this asymmetry: Windows Home and WSL Home have historically carried different installed marketplaces (`everything-claude-code`'s ~240 skills, confirmed 2026-07-03, live only in WSL Home, not Windows Home). Closing that gap deliberately, one verified tool at a time, is part of what "global" means here — not a single `cp -r` assumed to cover both.

### Amendment (2026-08-10) — the asymmetry is bigger than the 2026-07-03 claim above, and "replicated" was never actually built

Direct comparison of both home directories, not inferred from the dashboard note above: WSL has real global `agents/` (3), `commands/` (7), and a root `CLAUDE.md` that Windows has zero of; Windows has 32 skills, almost entirely `firecrawl-*`; WSL has 29, almost entirely Obsidian/vault and Cloudflare-worker skills. Overlap between the two skill sets is close to zero — this is not the same shape as the 2026-07-03 claim above (one marketplace's ~240 skills present on one side, absent on the other); it reads more like two independently-grown configurations that happened to never get reconciled. WSL's `.mcp.json` also carries live secrets (a GitHub PAT, two MCP Bearer tokens) that have no Windows-side equivalent at all.

**No "replicated to the WSL home directory" mechanism has ever actually been built** — this paragraph described the intended end state, not a working process; nothing here or in `_docs/Sync.md` shows a global-config sync ever running. The curated scope for actually building it is now decided in `_docs/Sync.md`'s 2026-08-10 amendment: sync only `agents/`, `commands/`, `skills/`, `hooks/`, `CLAUDE.md` bidirectionally between the two homes via the same Unison mechanism as the project-level mirrors; hard-exclude all credentials, MCP secrets, session state, and caches; two physical directories stay, never merged into one (a live shared directory was tested and rejected at the project-mirror scale in `_docs/Sync.md` for a corruption-risk reason that applies at least as strongly here, since both homes are read/written by a live session far more constantly than any single project's `.claude/`).

## Minimal footprint — Implement > Knowledge

This repo's decision discipline is a direct implementation of a principle already established in the Jarvis vault, not a new invention. From `60_Claude/20_Distilled_Notes/Sources - Plan/PDF's Ingestion Implementation.md`'s Claude Code Skills & Repos Matrix, the **Implement > Knowledge** principle:

> Install only what closes a *named* gap, reference everything else, test in one session before committing, mark every repo `(*INSTALLED*)`/`(*SKIP*)`/`(*EVAL: DATE*)` in `Repos.md` once decided.

That file's own execution audit found this principle stated and then not followed for three weeks — the Tier-1 list (ECC, mattpocock-skills, gstack, CPR, spec-kit) sat unexecuted, confirmed by checking `.claude/skills/`, `.claude/agents/`, and `~/.claude.json` directly (`60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution.md`, `# Github` section, "VS Code + Claude Setup" entry). This repo is the fix: a place where "test in one session" has an actual folder (`sandbox/`) to happen in, so the principle stops being a paragraph and starts being a filesystem path.

Concretely, minimal footprint means:
- A tool earns space in a rigid folder by closing a gap nothing else already closes — not by being well-regarded. (memsearch was dropped in favor of gbrain for exactly this reason: it duplicated gbrain's auto-capture without gbrain's synthesis layer — real redundancy, not a coin flip.)
- Reference-only tools (Awesome MCP Servers, claude-code-best-practice, system-prompts-and-models-of-ai-tools) never enter `sandbox/` at all — they're read, cited, and left in `40_Resources/CS/Repos.md`. `sandbox/` is reserved for things that might actually run.
- Every promotion is reversible in principle but treated as a real commitment in practice — a promoted tool is expected to have a documented reason (`_docs/Promotion-Criteria.md`), not just a memory of once seeming useful.

### Why `60_Claude/Standards/`, `write-contract.md`, and the artifact-authoring templates exist (2026-08-20)

These were built 2026-08-19 on Anant's direct, explicit request — not agent-invented scope. But `_docs/PRD.md`'s problem statement is scoped to *external* tooling (deciding what's worth trusting before it touches a real project), not this repo's own internal authoring process, and this section's own minimal-footprint principle asks for a named gap before anything gets built, so the justification belongs on record rather than left implicit.

**The named gap:** the CPR blend verdict (`tested-tools/commands/cpr-compress-preserve-resume/VERDICT.md`) — this repo's *first* real, evidenced promotion decision — needed a real, checkable definition of what a well-formed command/agent/hook/skill actually looks like to blend against. Without one, "blend the good parts of two implementations" has no objective shape; the reviewer is inventing the bar in the same breath as applying it. `Standards/` and its paired templates give that bar a fixed, reusable location instead of re-deriving it ad hoc for every future promotion decision. Same logic for `write-contract.md`: `instructions/`'s first, wrong build (`instructions/README.md`'s "Corrected 2026-08-19" section) was a real, demonstrated cost of not having a routing table and a never-write-to list written down before staging folders multiplied. Both closed a gap that had already caused a real mistake or was actively blocking a real decision — not a speculative "would be nice to have."

### Standing gate, added 2026-08-20: no further net-new pipeline meta-infrastructure until a real tool is promoted

**No further net-new pipeline meta-infrastructure gets built in this repo until at least one real tool reaches a promoted state** — installed into this repo's own `.claude/`, a real project's `.claude/`, or Jarvis's real `.claude/`. This is the gate that was missing: `Standards/`, `write-contract.md`, and the artifact-authoring templates were each justified by a real, named gap (above), but three-plus weeks of dense structural work have gone into this repo's own machinery while zero tools have crossed into a rigid folder (`_docs/Gaps.md`'s "TOP PRIORITY" entry). Building more pipeline infrastructure on top of that ratio, no matter how well-justified each individual piece is in isolation, repeats the exact "plan-and-never-run" failure mode this repo exists to prevent (`_docs/PRD.md`) — just aimed at the pipeline's own scaffolding instead of an external tool. "Meta-infrastructure" here means anything that helps this repo organize, document, or process its *own* pipeline — a new top-level staging folder, a new Standard, a new convention doc, a new automated sync leg. It does not mean the actual work of testing, verdict-writing, and promoting a specific tool — that work is exempt and is, in fact, the thing this gate is trying to force forward.

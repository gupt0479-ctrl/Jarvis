---
type: input
status: sprout
created: 2026-08-07
updated: 2026-08-07
tags:
  - summary
notes:
  - "[[Codebase Deep Read]]"
  - "[[Claims vs Implementation]]"
  - "[[Source Claims]]"
source_url: https://github.com/ahnafyy/adx
input_kind: github
track: ai
---
# adx — Process and CI Gaps
**Source:** `sandbox/adx` (local clone, HEAD `1959708`); `.github/workflows/adx.yml` read in full; `pnpm typecheck`/`pnpm build` run fresh; `gh api repos/ahnafyy/adx` queried directly
**Verified:** 2026-08-07
**Scope:** the monorepo's own build/typecheck/CI tooling — `adx-cli`, `adx-gate`, `adx-core`, root `package.json`, `.github/workflows/adx.yml`
## Source
The most severe bug found this pass — `adx init` crashing unconditionally (see [[Dead-on-Arrival Code]]) — should have been caught by TypeScript at compile time. It wasn't shipped because TypeScript can't catch it; it shipped because nothing in this project's toolchain ever actually asks TypeScript. This note traces that chain precisely, then covers two other process findings: a stale self-reported score, and a live-reproduced case of two implementations of the same metric disagreeing on the same input.
## Key Claims
- **`tsc --noEmit` catches the `adx init` crash instantly, in isolation.** It has never been a TypeScript-level blind spot.
- **`.github/workflows/adx.yml` never runs `typecheck` — only `build` and `test`.** Confirmed by reading the full workflow file; there is no step that would catch this class of bug in CI, ever.
- **`pnpm typecheck` (the root script) fails today — but not on the bug that matters.** It aborts on `adx-gate`'s own separate, real type errors before ever reaching `adx-cli`, because `pnpm -r run` bails on the first package failure by default.
- **8 real, currently-uncaught TypeScript errors exist across the repo right now** — 2 in `adx-gate`, present since the very first commit; 6 in `adx-cli` (including the crash bug).
- **`pnpm build` succeeds cleanly on code that doesn't compile**, because tsup/esbuild transpiles by stripping types rather than fully type-checking function bodies.
- **The README's self-scored badge is stale**, and the repo's own commit history proves the author knew the real number and never updated it.
- **BER (Boundary Evidence Rating) really does diverge between the CLI and the MCP server on identical input** — not a theoretical risk, reproduced live: 100 vs. 50 on the same repo, at the same moment.
## Full Content
### TypeScript catches the bug immediately — the pipeline never asks it to
==Running `tsc --noEmit` directly inside `packages/adx-cli` reports `error TS2304: Cannot find name 'generateCopilotInstructions'` on the first try — this was never a language-level gap.==
```
$ cd packages/adx-cli && npx tsc --noEmit
src/commands/init-mcp.ts(77,49): error TS2304: Cannot find name 'generateCopilotInstructions'.
```
So why did it ship? Three separate, compounding gaps:

1. **CI never runs `typecheck`.** `.github/workflows/adx.yml`'s only TypeScript-adjacent steps are "Build all packages" (`pnpm build`) and "Run test suite" (`pnpm test`). No `pnpm typecheck` step exists anywhere in the workflow, at any point.
2. **`pnpm typecheck` (root) bails before reaching the package with the bug.** The root script is `pnpm -r run typecheck`, and `pnpm -r`'s default behavior is to abort the entire recursive run at the first package failure. Running it fresh: `adx-gate` fails first — two real `exactOptionalPropertyTypes` errors in `src/ui.ts` (`SignOffResult.explanation` typed as `string` but assigned `string | undefined`) — and the run halts there (`ERR_PNPM_RECURSIVE_RUN_FIRST_FAIL`). `adx-cli` and `adx-mcp` never print anything at all in that run; confirmed by grepping the full output for both package names.
3. **`adx-gate`'s errors aren't new.** `tsconfig.base.json` sets `exactOptionalPropertyTypes: true`; `git log -p --follow` on that file shows one commit, all-additions, never modified since. This setting — and the errors it causes — has been there since the very first commit of the project.

Isolating `adx-cli`'s typecheck directly (its real package name is `adx`, not `adx-cli` — `pnpm --filter adx-cli` matches nothing) surfaces the full picture:
```
$ pnpm --filter adx run typecheck
src/commands/init-mcp.ts(77,49): error TS2304: Cannot find name 'generateCopilotInstructions'.
src/commands/maintain.ts(32,34): error TS2345: ... 'string | boolean | string[] | undefined' is not assignable to parameter of type 'string'.
  [× 4 total occurrences, lines 32/52/66/86]
src/commands/run.ts(114,7): error TS2379: ... 'RunOptions' with 'exactOptionalPropertyTypes: true' ...
```
**8 real compile errors, currently present, across 2 packages** — and no part of this pipeline, run as intended, ever surfaces more than the first 2.
### The build step that *is* in CI gives false confidence
==`pnpm build` succeeded with zero errors on the exact commit and exact file that fails `tsc --noEmit` — because tsup bundles via esbuild, which strips types rather than checking them.==
I ran `pnpm build` fresh, at the start of this session, before finding any of the above. It built all 8 packages cleanly, `adx-cli` included — `dist/index.js 62.61 KB`, no warnings. esbuild-based bundlers transpile TypeScript by stripping type annotations syntactically; a reference to an undefined identifier is syntactically valid JavaScript, so it bundles without complaint and only fails at runtime, when that code path actually executes — exactly what `adx init` does, every time.
### The README badge has been wrong for the project's entire public life
==`.adx/badge.json` was committed at `79/100` and never touched again — even though the very next commit's own message says `"ADX score: 79→85/100"`.==
```
$ cat .adx/badge.json
{ "message": "79/100", "color": "green" }
```
`git log -p --follow -- .adx/badge.json` shows two writes: `82/100` at `279d174` (23:42), then `79/100` at `a57935c` (00:35) — never again, across the remaining 12 commits. The commit immediately after that, `d5d2610` ("`feat: complete adx setup`"), states in its own message: *"ADX score: 79→85/100 (HDI: 50→83, Sweep: 41→89)"* — the author knew the score moved, and the badge file was simply never regenerated to match. A fresh `adx audit` against the repo today confirms `85/100` is the accurate current number.
### BER really does diverge, live, on identical input
==On the same throwaway-repo state, at the same moment: the CLI's `adx audit --json` reports `ber.score: 100`; the MCP server's `adx_audit` tool reports `ber: 50` — a 15-point swing in the composite ADX score (97 vs. 82) purely from which surface an agent happens to call.==
```
CLI  (adx audit --json):  "ber": { "score": 100, ...all 4 sub-checks true... }
MCP  (adx_audit tool):    "ber": 50
```
This isn't accidental drift — the MCP implementation carries its own comment, `// Minimal BER`, present since the commit that introduced the MCP server (`f557986`). It was written as a deliberately simplified stand-in from day one and never reconciled with the CLI's real `computeBER`. Worth being precise with Ahnaf about that distinction: it's a real inconsistency with a real practical impact (an IDE agent calling `adx_audit` sees a materially worse score than a human running `adx audit` in a terminal, for identical code) — but it's an unfinished shortcut, not silent drift.

Separately, a third JSON shape was found for the *same underlying data*: the CLI's real `adx shape --json` nests scores as `tds.score`; the MCP's `adx_shape` tool instead returns a flat `tdsScore` field. See [[Dead-on-Arrival Code]] for what this explains about the adx-intellij plugin.
### One correction into the source-of-truth record
==`Claims vs Implementation.md`'s "entire public history is a single commit" line was a shallow-clone (`--depth 1`) artifact, not a fact about the repository — confirmed by the repo owner, not something that needs further investigation.==
`git fetch origin` and `gh api repos/ahnafyy/adx/commits` both confirm the real history is 17 commits spanning a single 3-hour window: 2026-07-06 23:34 to 2026-07-07 02:43 (-0500), all by `ahnafyy`. Nothing has been pushed since. This doesn't change any finding in `Claims vs Implementation.md` — the code state it reviewed and the code state reviewed here are identical — but the specific sentence *"`git log --oneline` returns exactly one commit, dated 2026-07-07"* in its "Repository Reality Check" section should be corrected to reflect the real history the next time that note gets a deliberate edit. Not changed here — that note is a source of truth and gets its own pass, not a quiet rewrite mid-review.
## Why It Matters
This is the strongest single finding of the whole pass because it's not about one bug — it's about why *any* bug in this class would survive. TypeScript is fully capable of catching undefined references. This project has a `typecheck` script. Neither fact matters, because CI never invokes it and the local recursive command silently stops after the first unrelated failure. The same gap that let `generateCopilotInstructions` ship would let the next one ship too.
## Links Into The Vault
- [[Codebase Deep Read]] — index for this whole pass
- [[Dead-on-Arrival Code]] — the `adx init` crash this gap explains, and the BER/JSON-shape divergence's effect on adx-intellij
- [[Claims vs Implementation]] — source of truth for the pre-existing BER-divergence claim this note hardens with live numbers; also the note needing the shallow-clone correction above
- [[Source Claims]] — captured the "90 tests across 7 packages" and badge-as-live-endpoint claims this note's staleness finding sits alongside
## Open Questions
- [ ] Does Ahnaf run `pnpm typecheck` locally at all, or has this repo genuinely never been fully typechecked even once since the `exactOptionalPropertyTypes` errors were introduced on commit one?
- [ ] Is wiring `pnpm typecheck` (with `--stream`/no-bail, or fixing `adx-gate` first) into `.github/workflows/adx.yml` the single highest-leverage fix to propose, given it's the thing that would have caught the highest-severity bug found this session?
## Flashcards
Why did `pnpm build` succeed on code containing an undefined function reference?::tsup bundles via esbuild, which strips TypeScript types syntactically rather than fully type-checking function bodies — a call to an undefined identifier is valid JS syntax, so it only fails at runtime #cards/ai
Why does `pnpm typecheck` fail today without ever reporting the `adx init` crash bug?::`pnpm -r run` aborts the whole recursive run at the first package failure — `adx-gate` fails first on its own separate, day-one `exactOptionalPropertyTypes` errors, so `adx-cli`'s errors (including the crash) never get a chance to print #cards/ai
What does the MCP server's `// Minimal BER` comment reveal about the CLI/MCP score divergence?::It was a deliberately simplified stand-in written at the MCP server's introduction, not an accidental drift from the CLI's real `computeBER` — confirmed via the introducing commit's diff #cards/ai

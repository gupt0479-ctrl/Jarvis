---
type: project
status: active
created: 2026-08-30
updated: 2026-08-30
deadline: null
related_progress:
  - "[[Recommended Fixes]]"
  - "[[Claims vs Implementation]]"
  - "[[Codebase Deep Read]]"
next: Copy each fenced body below into a new issue on ahnafyy/adx, set the listed labels, then report back numbers and URLs.
tags:
  - "#progress"
---
# adx - GitHub Issues (10-18)
==Copy-paste staging note for the second half of the drafted issue set on `ahnafyy/adx`. Issues 1-9 were already posted manually. Issue 2 (the LICENSE item) was deliberately skipped, it is not being filed. This note covers issue 10 onward, including issue 10 itself, so nothing from the second half gets lost to em-dash or backtick cleanup.==
## How To Use This Note
Each issue below has a title line, a labels line (set these via GitHub's label picker, they are not part of the pasted body), and a fenced body block. Click the copy icon on the fenced block in Reading mode to get the exact body text, backticks and code snippets intact, with zero em dashes anywhere in this note.
## Issue 10 - adx init crashes unconditionally, root cause is that CI never runs typecheck
Labels: bug
````
Running `adx init` (bare, `--force`, or `--worktree`, all combinations) fails 100% of the time:
```
$ adx init
 ERROR  generateCopilotInstructions is not defined
```
Root cause, traced exactly: `generateCopilotInstructions()` was correctly defined inside `init.ts` at commit `7bda28e`. Two commits later, `d5d2610` ("feat: complete adx setup") splits the by-then-411-line `init.ts` into `init-agents.ts`/`init-generators.ts`/`init-mcp.ts`, the commit message states "Split fat files... Delete stub.ts (dead code), remove orphaned exports." The call site in `init-mcp.ts` survived the split. The function definition didn't. No commit since has touched any of those four files.

Why this shipped and has never been caught:
- Running `npx tsc --noEmit` directly inside `packages/adx-cli` catches it immediately: `error TS2304: Cannot find name 'generateCopilotInstructions'`. This was never a TypeScript-level blind spot.
- `.github/workflows/adx.yml` runs only `pnpm build` and `pnpm test`, no `typecheck` step exists anywhere in CI.
- `pnpm build` succeeds cleanly on this exact broken code, because tsup/esbuild strips types syntactically rather than fully type-checking function bodies, a reference to an undefined identifier is valid JS syntax and only fails at runtime.
- The root `pnpm typecheck` script (`pnpm -r run typecheck`) does exist, but `pnpm -r`'s default behavior aborts the whole recursive run at the first package failure. `adx-gate` fails first on its own separate, day-one `exactOptionalPropertyTypes` errors (2 errors in `src/ui.ts`, present since the first commit), so `adx-cli`, where the crash bug lives, never gets checked in the intended workflow.

Isolating `adx-cli`'s typecheck directly (`pnpm --filter adx run typecheck`, its real package name is `adx`, not `adx-cli`) surfaces 8 real, currently-uncaught TypeScript errors total: 2 in `adx-gate/src/ui.ts`, and 6 in `adx-cli` (`init-mcp.ts`'s undefined reference, 4 in `maintain.ts`, 1 in `run.ts`, all `exactOptionalPropertyTypes` violations or the crash itself).

Suggested fix: add a `pnpm typecheck` step to `.github/workflows/adx.yml`; fix `pnpm -r`'s bail-on-first-failure behavior (e.g. `pnpm -r --no-bail run typecheck`, or fix `adx-gate` first) so `adx-cli` actually gets checked; then fix all 8 errors, starting with restoring `generateCopilotInstructions()`.
````
## Issue 11 - Evidence and metrics don't reflect reality: BER divergence, stale badge, empty test log, wrong config type
Labels: bug, documentation
````
Four small, unrelated correctness bugs, all in the shape of "the recorded number or value doesn't match reality":

1. BER computed twice, inconsistently. The CLI's `computeBER` (`packages/adx-cli/src/commands/audit-vitals.ts`) checks four real distinct conditions and divides by 4. The MCP server's `adx_audit` handler (`packages/adx-mcp/src/index.ts`) builds `[hasWorkflow, hasConfig, hasConfig, hasWorkflow]`, the same two booleans duplicated twice each, carrying a `// Minimal BER` comment since the commit that introduced it, and never calls the shared function. Reproduced live on identical repo state: CLI reported `ber.score: 100`, MCP reported `ber: 50`, a 15-point swing in the composite ADX score (97 vs. 82) from the same code.
2. README score badge is stale. `.adx/badge.json` reads `79/100`; the very next commit's own message (`d5d2610`) says "ADX score: 79 to 85/100", the badge file was never regenerated to match. A fresh `adx audit` today confirms 85/100 is current.
3. `test-log.txt` is hardcoded empty. `packages/adx-gate/src/gate.ts` line 89: `testLog: '',` unconditionally, on every run, confirmed still true against current source. The docs describe this file as "captured mutation-testing output."
4. `harness.context.memory` type doesn't match docs. Config Reference states `'disk' | 'none'`; the actual type in `packages/adx-core/src/config.ts` is `'disk' | 'memory'`, confirmed still true against current source. `'none'` isn't a valid value anywhere in code.

Suggested fix: unify BER to one implementation shared by CLI and MCP; regenerate the badge (and consider wiring badge regeneration into CI so it can't go stale again); actually populate `testLog` from the real mutation-test output; fix the doc/type mismatch on `harness.context.memory`.
````
## Issue 12 - Config fields that are typed, documented, and never actually read
Labels: bug
````
Five real `AgenticConfig` fields exist in the type system and generated config but do nothing at runtime:

- `harness.control.router` (`'hierarchical' | 'sequential' | 'parallel'`), zero references anywhere in `harness.ts`'s actual loop, confirmed by direct grep. The docs describe it as "currently only sequential is supported," implying the other two values matter, they don't, at all.
- `harness.hooks.maxRetries`, typed, defaulted to 3, written into every generated config, never read outside its own type definition and the config template; the `onSlip: 'retry-with-backoff'` path just continues the loop unconditionally up to `maxIterations` with no retry counter tied to this field.
- `boundary.enforceTasteCheck`, `gate.ts` calls `profileProjectStyle`/`analyzeDiffTaste` unconditionally; no `if` statement anywhere checks this flag. The live docs currently state this flag controls "whether to run the taste deficit analysis... as part of `adx gate`," actively wrong, not just silent.
- `boundary.requireExplanationInvariants`, `ui.ts` only checks whether the configured list is non-empty (`.length > 0`); it never inspects diff content for `security`/`auth`/etc. relevance despite the live docs stating "the gate checks diff content to detect these."
- Related: taste analysis's own score (`tasteAnalysis.score`) is computed but never added to `gateScore` and never written into `manifest.json`, it only produces a `stdout` warning line. Taste-deficit is not a scored fourth layer, it's cosmetic terminal output.

Separately, the same shape of dead-code problem shows up in the CLI's own utility functions: `fileExists()` is copy-pasted verbatim across 5 files in `adx-cli` (`init.ts`, `init-mcp.ts`, `init-generators.ts`, `audit-vitals.ts`, `onboarding.ts`) despite `adx-core/harness-utils.ts` already existing as the shared-utility home for exactly this kind of helper; `bar()` (progress-bar rendering) is separately reimplemented with diverging widths and color thresholds across 4 files.

Suggested fix: for each config field, either wire it into the actual runtime behavior or remove it from the type and generated config; extract `fileExists()` and `bar()` into `adx-core/harness-utils.ts` and import everywhere.
````
## Issue 13 - .tsx import resolution is silently broken, undercounting FRR on React/JSX codebases
Labels: bug
````
`resolveImport()` in `packages/adx-shape/src/imports.ts`:
```ts
export function resolveImport(fromFile: string, specifier: string): string {
  const fromDir = path.dirname(fromFile);
  const normalised = specifier.replace(/\.js$/, '');
  return path.resolve(fromDir, normalised) + '.ts';
}
```
This unconditionally appends `.ts` regardless of the actual file extension. A specifier like `./Button` resolving to a real `Button.tsx` becomes `Button.ts`, which never matches an entry in the scanned-file map, `buildImportGraph()` silently drops that edge. On any React/JSX codebase, this means FRR (File Revisit Ratio) undercounts import relationships and misses cycles that route through `.tsx` files entirely. There are zero `.tsx`/`.jsx` fixtures anywhere in `adx-shape`'s own test suite, so this has never been caught.

Confirmed live against current source, re-verified directly in a fresh sandbox clone at the same commit before filing this issue.

Suggested fix: try resolving against the actual file extensions present in the scanned-file map (`.ts`, `.tsx`, `.js`, `.jsx`) instead of hardcoding `.ts`.
````
## Issue 14 - adx sweep's logic/type orphan classification degenerates to a capitalization check
Labels: bug
````
`sweep.ts`'s `logicOrphans` computation:
```ts
const logicOrphans = orphanedExports.filter(e =>
  !['interface', 'type', 'enum'].some(kw => e.symbol.match(new RegExp(`^[A-Z]`))));
```
The loop variable `kw` (meant to be one of `'interface'`/`'type'`/`'enum'`) is never referenced inside the regex, the check degenerates to "does the symbol start with a capital letter," evaluated three times identically instead of actually checking export kind.

The real fix requires upstream data that's currently discarded: `ExportRecord` in `exports.ts` only carries `{ symbol, file, line }`, confirmed still true against current source. The AST node's actual declaration kind (`TSInterfaceDeclaration`, `VariableDeclaration`, etc.), which `extractExports()` has in hand at parse time via `@typescript-eslint/typescript-estree`, is thrown away before it reaches `sweep.ts`. Untested by either package's own test suite.

Suggested fix: carry the AST declaration kind through `ExportRecord`, and have `sweep.ts` classify orphans by that field instead of a name-based capitalization heuristic.
````
## Issue 15 - adx-intellij: dead Tools-menu actions and a broken TDS lookup, invisible anywhere in the docs
Labels: bug, documentation
````
`adx-intellij` is a real, competently-written IntelliJ plugin (Kotlin, current IntelliJ Platform Gradle Plugin 2.3.0) that exists in the repository but is mentioned nowhere, not the README's package table, not the docs site, not `pnpm-workspace.yaml` (correctly, since it's Gradle/Kotlin rather than pnpm-managed). Three of its four integration points are genuinely complete (`AdxStatusBarWidget`, `AdxToolWindow`, `AdxEditorNotificationProvider`), but:

- `plugin.xml` registers two Tools-menu actions, `io.adx.intellij.actions.RunAuditAction` and `RunSweepAction`. `git log --all --diff-filter=A --name-only | grep -i action` returns nothing, these classes have never existed in the repository, at any commit. The plugin would fail to load or register them in a real IDE.
- `AdxService.getFileTds()`'s regex expects a flat `"tdsScore"` JSON key, but `AdxService` calls the real CLI (`adx shape --json`), whose actual output nests the score as `tds.score`, confirmed by running the CLI directly. The regex never matches; the editor-notification feature can never fire. Notably, the MCP server's `adx_shape` tool does return a flat `tdsScore`, three different JSON shapes now exist for the same per-file TDS data across CLI, MCP, and this plugin, suggesting the Kotlin code was written against the MCP's shape while the actual call goes to the CLI.
- The "Run adx shape" click handler is a documented no-op: `.let { /* open terminal */ }`, the comment describes intended behavior; no code implements it.
- No `settings.gradle.kts` or `gradlew` wrapper exists, this isn't buildable out of the box as-is.

Suggested fix: either implement the two missing action classes or remove their registration from `plugin.xml`; fix `getFileTds()`'s regex to match the CLI's real nested `tds.score` shape; add `adx-intellij` to the README's package table at minimum.
````
## Issue 16 - Documentation gaps: config reference incomplete, several claims unverifiable, two integrations undocumented
Labels: documentation
````
Two related but distinct categories of documentation gap:

Docs are silent, nothing said, should be:
- Configuration Reference doesn't match the actual `AgenticConfig` type, 5 fields accept more values in code than documented (`harness.observe.tests` also accepts `mocha`/`pytest`/`custom` plus an undocumented `testCommand?: string`; `harness.observe.telemetry` also accepts `latency`/`cost`; `harness.hooks.onSlip` also accepts `notify-only`; `boundary.requireExplanationInvariants` also accepts `auth`/`data-schema`/`api-contract`; see the separate issue on dead config fields for `router`, which has the same undocumented-values pattern on top of doing nothing at runtime).
- Internal scoring formulas are never disclosed: TDS (`0.6 x tokenScore + 0.4 x signalScore`), FRR per-file risk (`0.15 x fanOut + 0.25 x fanIn + 0.5 x cyclic`), gate score (`0.4 x abstraction + 0.4 x mutation + 0.2 x intent`), only the top-level 30/25/30/15 vital weights are published anywhere.
- `estimatedTokens` isn't caveated as an approximation anywhere in the docs, despite the source's own comment (`packages/adx-shape/src/tokens.ts`) explicitly calling it a rough `~4 chars/token` heuristic, not a real tokenizer count.
- `adx-vscode` has a one-line description in the README's package table but zero coverage on the docs site, no install path, no marketplace link, no screenshots.
- `adx-intellij` has zero documentation coverage anywhere, full stop (see the separate issue on this plugin's own dead code for the fuller picture).
- MCP's `adx_gate_check` tool is documented as part of "all 6 adx tools" without noting it's a reduced, Layer-1-only version of the full `adx gate` CLI command, confirmed live by calling it directly, the response contains only abstraction-analysis fields, no mutation or intent-cross-reference data.

Docs actively assert something uncited:
- The "7 to 8% fewer tokens, 34% fewer file revisits" claim (`abstraction.ts`'s comment, restated as fact in two separate READMEs) has no benchmark file, dataset, citation, or methodology note anywhere in the repo or docs site. In one of the two README restatements, "34%" is even repurposed for a conceptually different claim than the one it's attached to elsewhere.

Suggested fix: update the Configuration Reference to match `config.ts`; add a formulas/methodology page; caveat `estimatedTokens`; add minimal docs pages for `adx-vscode` and `adx-intellij`; either cite a real source for the 7 to 8%/34% numbers or stop stating them as fact.
````
## Issue 17 - Repo hygiene: tracked files that should be gitignored, no plan for evidence-bundle growth
Labels: bug, documentation
````
- `.adx/state/progress.json` and `.adx/tasks/v7fge81.md` are both tracked in git (confirmed via `git ls-files`, re-verified live against the current sandbox clone) despite being explicitly listed in the repo's own `.gitignore`, committed before the ignore rule took effect, never cleaned up since.
- The docs self-acknowledge a real gap: "adx does not yet automate bundle rotation." Bundle growth is significant, a typical bundle is 5 to 50KB, and active projects gating every PR "might accumulate hundreds of bundles per year" per the docs' own framing, with no stated retention policy or automation.

Suggested fix: `git rm --cached` the two files now that they're in `.gitignore`; add a documented retention/rotation strategy (or a script) for `.evidence/` bundle growth, even if the mechanism itself isn't built yet.
````
## Issue 18 - Frozen-path matching is substring/suffix, not path-boundary
Labels: bug
````
Both `packages/adx-maintain/src/frozen.ts` (`checkFrozenViolations`) and the generated POSIX-shell pre-commit hook use `file.includes(frozen) || file.endsWith(frozen)` / `case "$FILE" in *"$PATTERN"*)`. A frozen path like `./src/core/auth` would also match an unrelated file whose path merely contains that substring elsewhere (e.g. `src/core-utils/auth-helpers.ts`), over-blocking commits that never touch the actually-frozen directory. `adx-maintain`'s own test suite only covers exact-prefix cases, never the adjacent-but-unrelated false-positive case.

Related, lower-confidence note worth flagging in the same issue: if a repo already has a pre-commit hook before running `adx maintain install`, adx appends its block to the end of the existing script (`installHook` in `hook.ts`). If the existing hook calls `exit 0` on its own success path, the appended adx block would never execute, a real integration risk, though it depends on what hook already existed and wasn't independently reproduced this session.

Suggested fix: switch matching to real path-boundary comparison (e.g. normalize both sides and compare path segments, not raw substrings); document the pre-existing-hook interaction risk and recommend `adx maintain install` check for an existing hook and warn if one is found.
````
## Links Into The Vault
- [[Recommended Fixes]] - the prioritized list these 9 issues were drawn from, Sections 3 through 7
- [[Claims vs Implementation]] and the five [[Codebase Deep Read|Codebase\]] notes - the underlying evidence for every claim above
- [[Codebase Deep Read]] - index for the deeper pass, HEAD `1959708`, dormant since 2026-07-07

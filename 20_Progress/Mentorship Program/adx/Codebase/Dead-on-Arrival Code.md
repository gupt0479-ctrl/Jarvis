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
  - "[[Recommended Fixes]]"
source_url: https://github.com/ahnafyy/adx
input_kind: github
track: ai
---
# adx — Dead-on-Arrival Code
**Source:** `sandbox/adx` (local clone, HEAD `1959708`); full `git show`/`git log --all` history search; a live MCP client session calling all 6 tools; direct CLI reproduction
**Verified:** 2026-08-07
**Scope:** `adx-cli`, `adx-core`, `adx-mcp`, `adx-intellij`, `adx-shape`, `adx-sweep`, `adx-vscode`
## Source
This note collects code and config that exists in the repository but does nothing, does the wrong thing, or was never reachable — verified by running it, grepping full history for it, or tracing its only call sites. It's organized by failure shape, not by package; each entry names which package it lives in.
## Key Claims
- **`adx init` crashes every time**, unconditionally, and the crash was introduced by a refactor meant to fix bloat that adx's own tooling would flag — dropping a function definition during a fat-file split.
- **`adx-intellij` is more complete than it looks, and more broken than the README's silence about it suggests** — 3 of 4 integration points are real, working Kotlin; the 4th (Tools-menu actions) references classes that were never committed, in any commit, ever.
- **Four `adx.config.ts` fields do nothing**: `router`, `maxRetries`, `enforceTasteCheck`, and `requireExplanationInvariants` are all typed, documented, and either never read or read only as a length check — and the live docs now state more confidently than before that two of them do things they don't.
- **Two commands are presented as real but aren't**: `adx ratchet` (a homepage peer to `adx gate`, no CLI subcommand) and `adx maintain override` (see [[Safety-Critical Gaps]]).
- **The MCP server's `adx_gate_check` genuinely only runs Layer 1** — confirmed live, not just by reading the code.
- A helper function is copy-pasted verbatim across 5 files; a progress-bar renderer across 4 — in the one tool whose stated purpose is catching exactly this pattern.
- `.tsx` import resolution is silently broken, undercounting FRR/cycle detection on any React/JSX codebase.
## Full Content
### `adx init`: crashes 100% of the time, and I can name the exact commit that broke it
==A refactor meant to fix a file `adx`'s own tooling would flag as bloated dropped the one function definition its call site depended on — the tool's own self-improvement work introduced the crash.==
```
$ adx init
 ERROR  generateCopilotInstructions is not defined
```
Reproduced across bare `adx init`, `--force`, and `--worktree` — always the same `ReferenceError`, always exit 1. Zero GitHub issues, zero PRs, exactly one branch on the real repo (`master`, matching local `HEAD`) — not tracked, not fixed on a branch anywhere.

`git show` traces it precisely: `generateCopilotInstructions()` was defined correctly inside `init.ts` in commit `7bda28e`. Two commits later, `d5d2610` ("`feat: complete adx setup`") splits the by-then-411-line `init.ts` into `init-agents.ts`/`init-generators.ts`/`init-mcp.ts` — the commit message says explicitly *"Split fat files... Delete stub.ts (dead code), remove orphaned exports"*. The call site (`init-mcp.ts`) survived the split. The function definition didn't. No commit since has touched any of those four files to fix it. Full root-cause chain — why nothing caught this — is in [[Process and CI Gaps]].
### `adx-intellij`: three real integrations, one dead one, and no visibility anywhere
==The status bar, tool window, and editor-notification providers are genuine, competently-written Kotlin wired to a real backing service — this isn't a stub. But the plugin.xml's Tools-menu actions reference classes that were never committed, in any commit, across the project's full history.==
`AdxStatusBarWidget`, `AdxToolWindow`, and `AdxEditorNotificationProvider` are all complete: background-thread audit runs, click-to-refresh, TDS-based gutter warnings. The Gradle setup (`build.gradle.kts`) uses the current IntelliJ Platform Gradle Plugin (2.3.0), Kotlin 2.0, targets 2024.1+, with real signing/publishing config stubs — someone who'd built an IntelliJ plugin before wrote this.

What's actually broken:
- `plugin.xml` registers two Tools-menu actions, `io.adx.intellij.actions.RunAuditAction` and `RunSweepAction`. `git log --all --diff-filter=A --name-only | grep -i action` returns nothing — these classes have never existed in this repository, at any commit. The plugin would fail to load or register them in a real IDE.
- `AdxService.getFileTds()`'s regex expects a flat `"tdsScore"` JSON key. `AdxService` calls the real CLI (`run(findAdxBin(), "shape", "--json", ...)`, confirmed in source) — and the CLI's actual `shape --json` output nests it as `tds.score`, confirmed by running it directly. The regex will never match; the editor-notification feature can never fire.
- Interestingly, the MCP server's own `adx_shape` tool *does* return a flat `tdsScore` field — confirmed by calling it live. Three JSON shapes now exist for the same per-file TDS data (CLI nested, MCP flat, and whatever the Kotlin author was picturing when they wrote that regex) — the likeliest explanation is the Kotlin code was written against the MCP's shape while the actual implementation calls the CLI.
- The "Run adx shape" click handler in `AdxEditorNotificationProvider` is a documented no-op: `.let { /* open terminal */ }` — the comment says what it should do; no code does it.
- No `settings.gradle.kts` or `gradlew` wrapper exist anywhere in the repository — this isn't buildable out of the box. (No JDK/Gradle is available in this environment to attempt a real build; this is a structural finding, not a build-log one.)
- Zero references anywhere: not in the README's package table, not on the docs site, not in `pnpm-workspace.yaml` (it's Gradle/Kotlin, correctly outside the pnpm workspace) — confirmed by repo-wide grep. Zero CI, build, or test coverage of any kind.
### Four config fields that are typed, documented, and dead
==`router`, `maxRetries`, `enforceTasteCheck`, and `requireExplanationInvariants` are all real `AgenticConfig` fields — none of them change what the harness or gate actually does.==
- `harness.control.router` (`'hierarchical' | 'sequential' | 'parallel'`) — `grep` across `harness.ts` for any reference to `config.harness.control.router` returns nothing. The loop is a single unconditional `for`.
- `harness.hooks.maxRetries` — typed, defaulted to `3`, written into every generated `adx.config.ts` — never read outside its own type definition and the config template. The `onSlip: 'retry-with-backoff'` path just `continue`s the loop indefinitely up to `maxIterations`, with no retry counter tied to this field at all.
- `boundary.enforceTasteCheck` — `gate.ts` calls `profileProjectStyle`/`analyzeDiffTaste` unconditionally; no `if` statement anywhere checks this flag.
- `boundary.requireExplanationInvariants` — `ui.ts` only checks `.length > 0` to decide whether to show one blanket "explain this" prompt; it never inspects diff content for `security`/`auth`/etc. relevance.

The live docs (`docs/src/content/docs/reference/config.md`) now state, in the current deployed text, that `enforceTasteCheck` controls "whether to run the taste deficit analysis... as part of `adx gate`" and that `requireExplanationInvariants` works because "the gate checks diff content to detect these." Both are more specific and more confidently wrong than what `Claims vs Implementation.md` found in July — that note flagged the gap; the current docs assert a mechanism that doesn't exist.
### Two commands that are presented as real but aren't
==`adx ratchet` is listed as a peer to `adx gate` on the homepage; `adx-cli/src/index.ts` registers exactly 7 subcommands, and `ratchet` isn't one of them.==
`init`, `shape`, `gate`, `audit`, `sweep`, `maintain`, `run` — that's the complete list, confirmed by reading `index.ts`'s `subCommands` object directly. `adx ratchet` exists only as an internal library call (`applyRatchet`, invoked automatically on oscillation detection) and as the MCP tool `adx_ratchet` — which does work, confirmed by calling it live: `{ "agentsMdEntry": "- NEVER repeat: probe test failure...", "backlogRuleId": "ratchet-e4cm4m5", "agentsMdUpdated": true }`. Typing `adx ratchet` at a terminal still fails. `adx maintain override` is the other one — full detail in [[Safety-Critical Gaps]].
### MCP's `adx_gate_check`: confirmed live, Layer 1 only
==Calling `adx_gate_check` directly returns only abstraction-analysis fields — no mutation-testing or intent-cross-reference data exists anywhere in the response.==
```json
{ "score": 100, "tokenOverheadPercent": 0, "abstractionLines": 0, "logicLines": 2, "flagged": false, "details": [], "changedFiles": ["index.js"] }
```
This matches the tool's own description ("Run Layer 1 of the evidence gate...") but not the docs' framing of the MCP server as exposing "all 6 adx tools" without noting this one is a reduced, single-layer version of the full `adx gate` CLI command.
### The sweep tool has its own dark code
==`adx sweep`'s logic-vs-type orphan classification has an unused loop variable that quietly turns a category check into a pure capitalization check — and it can't be fixed without also fixing what `extractExports` throws away.==
`sweep.ts` computes `logicOrphans` via `!['interface','type','enum'].some(kw => e.symbol.match(/^[A-Z]/))` — `kw` is never used inside the predicate, so this degenerates to "does the symbol start with a capital letter," run three identical times. The real problem sits upstream: `ExportRecord` (`exports.ts`) only ever carries `{ symbol, file, line }` — the AST node's actual declaration kind (`TSInterfaceDeclaration`, `VariableDeclaration`, etc.), which `extractExports` has in hand at parse time, is discarded before it ever reaches `sweep.ts`. Untested by either package's test suite.
### `fileExists()` and `bar()`: the exact pattern this tool exists to catch, in its own source
==A one-line helper is copy-pasted verbatim across 5 files; a progress-bar renderer is reimplemented with diverging parameters across 4 — in the tool whose own sub-agent spec describes this exact pattern as "the model declares a type or function 'for completeness'... six of them are not being utilized."==
`fileExists()` — identical `async function fileExists(p) { try { await fs.access(p); return true; } catch { return false; } }` — appears verbatim in `init.ts`, `init-mcp.ts`, `init-generators.ts`, `audit-vitals.ts`, and `onboarding.ts`, all in `adx-cli`. `adx-core/harness-utils.ts` already exists as the shared-utility home for exactly this kind of helper and holds none of it. `bar()` (score-to-progress-bar rendering) is separately reimplemented in `audit-vitals.ts`, `sweep.ts`, `adx-gate/ui.ts`, and `adx-vscode/panel.ts`, with different widths and color thresholds in each.
### `.tsx` resolution is silently broken
==`resolveImport()` always appends a literal `.ts` after stripping `.js` — a `.tsx` file importing another `.tsx` file never resolves, so any React/JSX codebase undercounts FRR and misses import cycles.==
`adx-shape/src/imports.ts`: `path.resolve(fromDir, specifier.replace(/\.js$/, '')) + '.ts'` — unconditional. A specifier like `./Button` with no extension, resolving to a real `Button.tsx`, becomes `Button.ts` and never matches an entry in the scanned-file map, so `buildImportGraph()` silently drops that edge. Untested — zero `.tsx`/`.jsx` fixtures anywhere in `adx-shape`'s test suite.
## Why It Matters
None of this needs a judgment call about priorities — it's a list of things that are provably not what they claim to be, verified by running them, calling them, or reading their full commit history. `Recommended Fixes.md` already flagged several of these from static reading (`enforceTasteCheck`, `router`, `adx ratchet`); this note either hardens those with live confirmation or adds ones that weren't visible without reading files the original pass didn't cover.
## Links Into The Vault
- [[Codebase Deep Read]] — index for this whole pass
- [[Process and CI Gaps]] — the full root-cause trace for why the `adx init` crash shipped and survived
- [[Safety-Critical Gaps]] — `adx maintain override`, the other nonexistent-but-documented command
- [[Recommended Fixes]] — its "Dead Code / Config Cleanup" section already named `router` and `enforceTasteCheck`; this note confirms both live and adds `maxRetries`/`requireExplanationInvariants`
- [[Claims vs Implementation]] — source of the original `adx ratchet`/MCP-Layer-1 findings this note reproduces live
## Open Questions
- [ ] Is adx-intellij meant to ship at all, or was it scaffolded and abandoned mid-sprint? It's the most-built-out of the three "undocumented" integrations and the least visible anywhere.
- [ ] Given four config fields are confirmed dead, is the right fix per-field, or a pass that removes every field the harness/gate doesn't actually read?

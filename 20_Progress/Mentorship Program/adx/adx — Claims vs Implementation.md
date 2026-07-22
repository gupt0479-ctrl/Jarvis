---
type: input
status: sprout
created: 2026-07-22
updated: 2026-07-22
tags:
  - summary
notes:
  - "[[adx — MOC]]"
  - "[[adx — Source Claims]]"
source_url: https://github.com/ahnafyy/adx
input_kind: github
track: ai
---
# adx — Claims vs Implementation
**Source:** `https://github.com/ahnafyy/adx` — full clone, every non-test `.ts` source file read across all 8 packages, cross-referenced line-by-line against [[adx — Source Claims]]
**Verified:** 2026-07-22
**Scope:** `adx-core`, `adx-cli`, `adx-shape`, `adx-gate`, `adx-sweep`, `adx-maintain`, `adx-mcp`, `adx-vscode`; all 90 test cases counted directly; both GitHub Actions workflows; the repo's own `.adx/` and `.evidence/` state; the single commit in its git history
## Source
This note checks every substantive claim in [[adx — Source Claims]] against the actual TypeScript implementation in the GitHub repository, rather than the docs site or README. Where the docs describe a formula, a threshold, a blocking condition, or a feature, this note names the exact file that implements it and states plainly whether the code matches.
## Key Claims
- The website capture in [[adx — Source Claims]] held up under code review — nothing material was missed there; every discrepancy below is between **what adx claims and what it does**, not an error in the prior capture
- **"Import cycles always score 0" is false** — a cyclic file gets a flat +0.5 risk bonus, not a forced floor; the aggregate FRR score barely moves for one small cycle in a large codebase
- **"Gate score below 60 blocks merge" is false** — blocking is driven by three unrelated boolean triggers, independent of the numeric gate score
- **`signedBy` is hardcoded to the literal string `'engineer'`** in every interactive gate run, and CI-mode runs auto-approve at Agency Level 6 with zero human input
- adx's own repository's agency ledger has exactly **one entry, signed by `"agent"`** — not a human
- **`adx ratchet` has no CLI command** despite being presented as a peer to `adx gate` on the homepage
- **`adx sweep` ships four undocumented flags** (`--fix`, `--auto`, `--dry-run`, `--comments`) that delete or rewrite real source files
- **BER is computed twice, inconsistently** — the CLI and the MCP tool can report different scores for the identical repository
- Five of six checked `AgenticConfig` fields accept **more values in code than the Configuration Reference documents**; `router` is accepted but never read anywhere in the runtime
- `enforceTasteCheck` and `requireExplanationInvariants` are **real config fields that don't do what their names imply** — taste checking always runs regardless of the flag, and explanation categories are never matched against actual diff content
- The **"90 tests" count is exactly right; "across 7 packages" is not** — test files exist in only 5 of the 8 packages
- Mutation testing, AST-based export analysis, and the harness's maker/checker loop are **genuinely well-built** and match their documented behavior closely
## Full Content
### Repository Reality Check
==The entire public history of adx is a single commit, and the tool's own self-scored evidence trail is exactly one gate run and one agency-ledger entry — signed by "agent," not a human.==
`git log --oneline` returns exactly one commit, dated 2026-07-07. `.evidence/` contains exactly one bundle (`run-2026-07-07T06-49-22-177Z`). `.adx/state/adx-agency.json` contains exactly one entry: Level 6 (Resolve), `signedBy: "agent"`, with a summary describing the agent fixing its own missing scaffolding (agent specs, `llms.txt` content, fat-file splits, orphaned exports) so its own badge would score well. This directly answers the open question in [[adx — MOC]] about real-world usage: there is none visible from outside the project yet. This is a single-session, self-bootstrapped snapshot, not a track record.
Separately: `.adx/state/progress.json` and one file under `.adx/tasks/` are tracked in git despite being explicitly listed in the repo's own `.gitignore` — committed before the ignore rule took effect, and never cleaned up. The repo does not currently follow its own documented commit/ignore hygiene table in practice.
### The Agency Ladder's Integrity Gap
==`signedBy` is hardcoded to the literal string `'engineer'` in every interactive `adx gate` sign-off, and CI-mode runs auto-stamp Level 6 (Resolve) with zero human input — the exact rubber-stamp failure the ladder exists to catch.==
`packages/adx-gate/src/gate.ts` calls `appendLedgerEntry(ledger, { ref: runId, level: agencyLevel, summary: explanation ?? ..., signedBy: 'engineer' })` — every single ledger entry, interactive or not, carries the literal string `'engineer'`, never a real git identity. The docs' own example ledger entry shows `"signedBy": "ahnafyy"`, implying real identity capture; the code never reads `git config user.name` or any identity source at all.
In CI mode (`--ci`, or whenever `!process.stdin.isTTY`), `packages/adx-gate/src/ui.ts` runs: `const approved = !gateBlocked;` then returns `agencyLevel: approved ? AgencyLevel.Resolve : 0` — no human interaction of any kind.
> [!WARNING]
> The one real ledger entry in adx's own repository is Level 6, `signedBy: "agent"` — the tool's own accountability record was self-certified by the agent it exists to hold accountable.
### Claims The Code Contradicts Directly
==Two headline claims from the docs do not match the actual scoring and blocking logic: import cycles do not force FRR to zero, and the gate score has no blocking threshold at all.==
1. **"Import cycles always score 0"** (measure/shape page) — `computeRevisitRisk` in `packages/adx-shape/src/cycles.ts` gives cyclic files a flat `+0.5` bonus on top of fan-in/fan-out terms (`out*0.15 + inDeg*0.25 + cyclic*0.5`, capped at 1.0); a file only counts as revisit-prone if the combined risk exceeds `0.4`. The final score is $FRR = \frac{100 \times (\text{total} - \text{revisitProne})}{\text{total}}$ — a proportion across the whole codebase. One 2-file cycle in a 100-file project moves the score by roughly 2 points, not to zero.
2. **"A gate score below 60 blocks merge"** (govern/gate page) — no code path anywhere checks `gateScore < 60`. `packages/adx-gate/src/ui.ts` computes `gateBlocked` from three unrelated booleans: `abstraction.flagged || mutationResult.tautologicalTests.length > 0 || semanticDrift.drift.length > 3`. A diff can score 55 overall and pass if none of the three trip; a diff can score 90 and still block on one tautological test.
3. **"90 tests across 7 packages"** (README) — the count is exactly right: 90 test cases, confirmed by direct count. The package count is not: test files exist in only 5 of the 8 packages (`adx-core`, `adx-gate`, `adx-maintain`, `adx-shape`, `adx-sweep`). `adx-cli` — the CLI package itself — plus `adx-mcp` and `adx-vscode` have zero test files.
4. **`test-log.txt` "test output captured during the run"** (concepts/evidence page) — `packages/adx-gate/src/gate.ts` hardcodes `testLog: ''` on every run, unconditionally. Verified directly against the repo's own real evidence bundle: `.evidence/run-2026-07-07.../test-log.txt` is a zero-byte file.
5. **`harness.context.memory: 'disk' | 'none'`** (Configuration Reference) — the actual type in `packages/adx-core/src/config.ts` is `'disk' | 'memory'`. `'none'` is not a valid value anywhere in code.
### Config Surface Wider Than What's Documented

| Field | Documented values | Actual type (`config.ts`) |
| --- | --- | --- |
| `harness.control.router` | "currently only sequential is supported" | `'hierarchical' \| 'sequential' \| 'parallel'` — and never read anywhere in the harness loop |
| `harness.observe.tests` | `'vitest' \| 'jest' \| 'none'` | `'vitest' \| 'jest' \| 'mocha' \| 'pytest' \| 'custom'`, plus an undocumented `testCommand?: string` |
| `harness.observe.telemetry` | `'tokens' \| 'file-revisits'` | same two, plus `'latency' \| 'cost'` |
| `harness.hooks.onSlip` | `'retry-with-backoff' \| 'halt-and-dump'` | same two, plus `'notify-only'` |
| `boundary.requireExplanationInvariants` | `'security' \| 'dependency-addition'` | same two, plus `'auth' \| 'data-schema' \| 'api-contract'` |

==`router` is accepted as a config value but grep across the whole repository finds zero references to it anywhere in the harness runtime — it is not merely undocumented, it is entirely dead.==
> [!NOTE]
> None of the wider types are bugs by themselves — a type permitting more than the docs describe just means the docs lag the code. `router` is the one that matters: `packages/adx-core/src/harness.ts` runs a single unconditional `for` loop with no branch on `config.harness.control.router` at all. Setting it to `'parallel'` or `'hierarchical'` has zero effect.
### Config Fields That Are Silently No-Ops
==`enforceTasteCheck` is a real, typed, defaulted-to-`true` config field that the gate code never reads — taste analysis runs unconditionally regardless of its value, and its score is never included in the gate score or the persisted evidence bundle.==
`grep -rn "enforceTasteCheck"` across the whole repo returns exactly three hits: the type definition and two default-value assignments. `packages/adx-gate/src/gate.ts` calls `profileProjectStyle` and `analyzeDiffTaste` unconditionally, with no check against this flag anywhere. Setting it to `false` in `adx.config.ts` changes nothing.
Taste analysis's own score (`tasteAnalysis.score`) is computed but never added to `gateScore` and never written into `manifest.json` — it only ever produces a `stdout` warning line during a gate run. This resolves the open question left in [[adx — Source Claims]]: taste deficit is not a fourth scored layer; it is cosmetic terminal output only.
`boundary.requireExplanationInvariants` is never checked against actual diff content anywhere in the codebase. `packages/adx-gate/src/ui.ts` only checks whether the configured list is non-empty; if so, it demands one blanket explanation on every interactive gate run, regardless of whether the diff touches security, auth, or anything the category names imply. There is no logic anywhere that inspects the diff for `security`-relevant or `dependency-addition`-relevant content — the categorization is names-only.
### Undocumented Features Found In The Code
==`adx sweep` ships four flags — `--fix`, `--auto`, `--dry-run`, `--comments` — that interactively or automatically delete "orphaned" exports and dark comments from real source files, and none of them appear anywhere in the docs' options table for the command.==
1. **`--auto`** — batch mode, wired to `fixBatch()` in `packages/adx-sweep/src/fixer.ts`; removes every orphaned export confirmed to have zero remaining references, with no per-item confirmation.
2. **`--fix`** — interactive per-orphan removal with a `y`/`n`/`a`(ll)/`q`(uit) prompt loop.
3. **`--dry-run`** — previews exactly what `--auto` would remove, without writing.
4. **`--comments`** — interactive dark-comment review with delete/keep per line.
The fixer double-checks for remaining usages before deleting (`hasAnyReference`, using real AST parsing via `@typescript-eslint/typescript-estree` with a regex fallback) — a genuinely careful implementation, not a reckless one. But a flag that deletes code across a repository with zero mention anywhere on the public docs site is a real gap for anyone deciding whether to run it unsupervised in CI.
`adx ratchet` has no CLI command at all. `packages/adx-cli/src/index.ts` registers exactly 7 subcommands: `init`, `shape`, `gate`, `audit`, `sweep`, `maintain`, `run`. There is no `ratchet` subcommand. The homepage lists `adx ratchet` as a peer bullet to `adx gate` under "Govern" — in practice it exists only as an internal library call (`applyRatchet` in `adx-core`, invoked automatically by the harness on oscillation detection) and as an MCP tool (`adx_ratchet`). Typing `adx ratchet` at a terminal fails with an unknown-command error.
Taste Deficit Tracker's actual mechanism, now confirmed from `packages/adx-gate/src/taste.ts`: profiles the whole project's dominant naming convention (regex-classified per declared identifier), functional-vs-OOP ratio (`class` keyword count vs `=>`/`function` count), and median file length; then flags a diff if its added lines' dominant naming differs from the project's, if its class-usage-rate crosses a 0.1/0.6 threshold in the opposite direction from the project norm, or if it adds more than 200 lines at over 4× the median. Coarse but real — and, per the section above, entirely unscored.
MCP `adx_gate_check` only runs Layer 1. Its own tool description says so directly: "Run Layer 1 of the evidence gate on a git diff string." An IDE agent calling this tool gets abstraction analysis only, not mutation testing or intent cross-reference. The docs describe the MCP tools as exposing "all 6 adx tools" without noting this one is a reduced single-layer version of the full `adx gate` CLI command.
### Divergent Duplicate Implementations
==BER (Boundary Evidence Rating) is computed twice, independently, with different logic — the CLI's `adx audit` and the MCP's `adx_audit` tool can report different scores for the identical repository state.==
CLI (`packages/adx-cli/src/commands/audit-vitals.ts computeBER`): checks four real, distinct conditions — evidence dir or CI workflow mentions adx; `adx.config.ts`/`.js` exists; `.adx/state/progress.json` exists; evidence dir or CI workflow again (reused for "discernment matrix") — divides the count by 4.
MCP (`packages/adx-mcp/src/index.ts`, inline in the `adx_audit` handler): builds `[hasWorkflow, hasConfig, hasConfig, hasWorkflow]` — the same two booleans duplicated twice each — and divides by 4. This does not call the shared `computeBER` function at all; it is a separate, cruder reimplementation that can only ever produce 0%, 50%, or 100%, and never actually checks for `.evidence/` bundle presence despite BER being defined around evidence-bundle presence.
HDI, by contrast, is correctly reimplemented identically in both places (same formula: $HDI = \frac{(\text{mean level} - 1)}{6} \times 100$, same result) — only BER diverges between the two surfaces.
### Precision Gaps Worth Knowing About
==Frozen-path matching in both the git hook and the JS layer is substring/suffix matching, not path-boundary matching — a frozen path can over-block unrelated files that happen to share a substring.==
`packages/adx-maintain/src/frozen.ts checkFrozenViolations` matches with `file.includes(frozen) || file.endsWith(frozen)`. The generated shell pre-commit hook (`packages/adx-maintain/src/hook.ts`) uses identical logic in POSIX shell: `case "$FILE" in *"$PATTERN"*)`. A frozen path like `./src/core/auth` would also match an unrelated file whose path merely contains that substring elsewhere.
Token counting is an explicitly self-acknowledged approximation, per the source's own comment in `packages/adx-shape/src/tokens.ts`: `estimateTokens` "Approximates OpenAI cl100k_base: ~4 chars/token... For production accuracy, swap in gpt-tokenizer." None of the docs pages caveat that `estimatedTokens` is a rough word-boundary heuristic rather than a real tokenizer count.
If a repo already has a pre-commit hook before running `adx maintain install`, adx appends its block to the end of the existing script (`installHook` in `hook.ts`). If the existing hook calls `exit 0` on its own success path, the appended adx block would never execute — a real, conditional integration risk depending on what hook already existed.
The internal scoring formulas for TDS ($score = 0.6 \times tokenScore + 0.4 \times signalScore$), FRR per-file risk ($risk = 0.15 \times fanOut + 0.25 \times fanIn + 0.5 \times cyclic$), and the overall gate score ($gateScore = 0.4 \times abstraction + 0.4 \times mutation + 0.2 \times intent$) are all real and consistently applied, but none of these specific weights are disclosed anywhere on the docs site — only the top-level ADX vitals weights (30/25/30/15) are published.
### What's Actually Well-Built
==Mutation testing genuinely executes: it writes a mutated file to disk, runs the real configured test command via `execSync`, and restores the original content in a `finally` block regardless of outcome — this is real verification, not a simulated demo.==
`packages/adx-gate/src/mutation.ts runMutationTest` applies real regex-based source mutations (boolean flips, `===`/`!==` flips, `>` flip) to up to 3 changed files (2 mutations max per file), executes the actual configured test command, and checks the real process exit code. The restore-on-`finally` means a clean interrupt is safe, though a hard process kill between the write and the finally would leave a real bug mutated into the source file — a small but real operational risk worth knowing about before running this unattended in CI.
Orphaned-export and dark-comment detection in `adx-sweep` use real AST parsing (`@typescript-eslint/typescript-estree`) with a regex fallback only if parsing fails — including a deliberate, non-obvious correctness fix: named re-exports (`export { X } from './file'`) are counted as "in use," so barrel-published public API symbols aren't flagged as false-positive orphans.
Barrel files (>70% re-export lines) are correctly excluded from the FRR import-graph risk calculation, matching the docs' own stated exception ("barrel files scoring low TDS is expected, not a bug").
The harness's maker/checker loop, oscillation detection, and ratchet integration in `packages/adx-core/src/harness.ts` match the documented behavior closely and are the most faithfully-implemented part of the whole system.
## Why It Matters
This is the deliverable Ahnaf actually asked for: not "does the website read well" but "does the tool do what it says." The two false headline claims (import cycles, gate-score threshold) and the agency-ledger integrity gap are the three findings worth leading with in conversation — they're concrete, each traces to an exact file, and they cut at the product's actual thesis rather than at docs polish. Recommend raising the `signedBy` hardcoding and CI auto-approval-at-Level-6 behavior first: if the Agency Ladder can't reliably prove a human looked at a change, the governance pitch is undermined by the same failure mode it's marketed to prevent.
## Links Into The Vault
- [[adx — Source Claims]] — the claims this note checks, captured faithfully from the website and README before this code review began
- [[adx — MOC]] — the judgment-level synthesis; see its "Verification Against The Codebase" section for the condensed version of these findings
- [[Mentor Details]] — the mentor whose project this is
## Open Questions
- [ ] Is the agency-ledger integrity gap (hardcoded `signedBy`, CI auto-approval at Level 6) something Ahnaf already knows about, or a genuine blind spot worth raising directly?
- [ ] Does he intend `adx sweep --auto` to ever run unattended in CI, given it deletes code with no confirmation and is currently undocumented?
- [ ] Is the BER divergence between the CLI and MCP tool intentional, or an oversight from writing the MCP server before extracting a shared `computeBER`?
- [ ] Now that `pytest`/`custom` test-runner support is confirmed real in the type and in `deriveTestCommand`, has this actually been exercised against a non-JS project, or is it type-level-only and untested in practice?
## Flashcards
Why does a single import cycle in a 100-file project not zero out the FRR score, despite the docs saying "import cycles always score 0"?::A cyclic file gets a flat **+0.5** risk bonus, not a forced floor; the final FRR score is the proportion of all revisit-prone files across the codebase, so one small cycle only moves the score a few points #cards/ai
What actually determines whether `adx gate` blocks a merge, if not the numeric gate score falling below 60?::Three unrelated **boolean triggers** — abstraction flagged, any tautological test found, or more than 3 drifted files — the documented "score below 60 blocks merge" threshold does not exist anywhere in the code #cards/ai
Why is the "permanent record of human oversight" in `.adx/state/adx-agency.json` not actually reliable evidence of human review?::`signedBy` is **hardcoded** to the literal string `'engineer'` in every interactive run, and CI-mode runs **auto-approve** at Agency Level 6 with zero human input — confirmed by adx's own repo, whose one ledger entry is signed by `"agent"` #cards/ai
What does `adx sweep --auto` do that isn't mentioned anywhere in the public docs?::It **batch-deletes** orphaned exports and dark comments from real source files with no confirmation prompt — only `--cwd` and `--json` appear in the documented options table #cards/ai
Why can `adx audit` (CLI) and the `adx_audit` MCP tool report different BER scores for the same repository?::They're **two separate implementations** — the CLI's `computeBER` checks four distinct real conditions, while the MCP handler duplicates two booleans into a fake four-slot array and never calls the shared function #cards/ai

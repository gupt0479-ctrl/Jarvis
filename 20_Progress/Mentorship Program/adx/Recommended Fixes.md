---
type: project
status: active
created: 2026-07-22
updated: 2026-07-22
deadline:
related_progress:
  - "[[adx]]"
  - "[[Source Claims]]"
  - "[[Claims vs Implementation]]"
tags:
  - "#progress"
next: Share this list with Ahnaf and get his read on priority before recommending any of it upstream.
---
# adx — Recommended Fixes
==Everything below is a recommendation, not a fact — the factual record lives in [[Source Claims]] and [[Claims vs Implementation]]; this note exists solely to turn those findings into an actionable list.==
## Goal
Turn every gap and discrepancy found in [[Source Claims]] and [[Claims vs Implementation]] into a single prioritized, actionable list — so those two notes can stay pure fact and this one can carry all the judgment.
## Integrity Fixes — Highest Priority
These touch the product's actual accountability claim, not just its polish.
- [ ] **Capture a real signer identity.** `signedBy` is hardcoded to the literal string `'engineer'` in `packages/adx-gate/src/gate.ts` on every gate run, interactive or not. Read `git config user.name` (or an equivalent identity source) instead, so the agency ledger can actually attribute a sign-off to a specific human.
- [ ] **Stop auto-approving Level 6 in CI with zero human input.** `packages/adx-gate/src/ui.ts` sets `agencyLevel: AgencyLevel.Resolve` on any non-blocked CI run today. Either record CI-only approvals at a distinct, clearly-lower level (or a dedicated `automated` marker outside the 1–7 scale), or require an explicit human step before Level 6 can ever be recorded.
- [ ] **Reconcile the gate's actual blocking logic with the documented threshold.** Docs state "gate score below 60 blocks merge"; the code blocks on three unrelated booleans (`abstraction.flagged`, any tautological test, more than 3 drifted files) with no reference to the numeric score at all. Either make the code check `gateScore < 60`, or correct the docs to describe the boolean-trigger behavior that actually exists.
- [ ] **Fix or reword the "import cycles always score 0" claim.** The code gives cyclic files a flat +0.5 risk bonus, not a forced floor — the docs describe FRR behavior the code doesn't have. Either change the scoring so a cycle really does zero out the file's contribution, or correct the docs to describe the proportional-risk model that's actually implemented.
## Safety Fixes
Things that can alter or delete a user's repository and are currently undocumented.
- [ ] **Document `adx sweep --fix` / `--auto` / `--dry-run` / `--comments`.** All four exist and work; none appear in the docs' options table for the command. At minimum, document them.
- [ ] **Decide `adx sweep --auto`'s CI posture explicitly.** Nothing currently stops a team from wiring `adx sweep --auto` into CI and having it silently delete code on every push. If that isn't the intended use, say so in the docs; if it is, document the safety rationale (the AST-based reference re-check before deletion) prominently, since it's the only thing making the flag safe.
## Consistency Fixes
- [ ] **Unify the two BER implementations.** The CLI's `computeBER` (`packages/adx-cli/src/commands/audit-vitals.ts`) and the MCP tool's inline BER calculation (`packages/adx-mcp/src/index.ts`) diverge — the same repository can score differently depending on which surface is asked. Extract one shared `computeBER` into `adx-core` and have both call it.
- [ ] **Populate `test-log.txt` for real.** `packages/adx-gate/src/gate.ts` hardcodes `testLog: ''` on every run. `runMutationTest` already executes the test command via `execSync` — capture its stdout/stderr and pass it through, so the persisted evidence bundle actually contains what the docs describe.
- [ ] **Fix the `harness.context.memory` type mismatch.** Docs say `'disk' | 'none'`; the code type is `'disk' | 'memory'`. Pick the real value and correct whichever side is wrong.
## Dead Code / Config Cleanup
- [ ] **Either implement `router` or remove it from the type.** `harness.control.router` accepts `'hierarchical' | 'sequential' | 'parallel'`, but nothing in `packages/adx-core/src/harness.ts` ever reads it — it is currently a config field that silently does nothing.
- [ ] **Wire `enforceTasteCheck` into the gate, or delete the flag.** It's typed, defaulted to `true`, and never checked anywhere — taste analysis runs unconditionally regardless of its value. Either gate the `profileProjectStyle`/`analyzeDiffTaste` calls behind this flag, or remove it so it stops implying control that doesn't exist.
- [ ] **Make `requireExplanationInvariants` actually contextual.** Currently any non-empty list triggers one blanket "explain this" prompt on every gate run, regardless of whether the diff touches security, auth, or dependencies. Either detect the relevant category in the diff before prompting, or rename/redocument the field as "always require an explanation when this list is non-empty" rather than implying per-category detection.
- [ ] **Include the taste-deficit score in the gate score, or explicitly label it advisory-only.** It's computed, sometimes prints a warning, and is currently dropped silently from both the gate score and the persisted evidence bundle.
## Documentation Fixes
- [ ] **Publish a reference page for `adx ratchet`,** or stop listing it as a peer command to `adx gate` on the homepage — it currently has no CLI subcommand at all, only an internal library call and an MCP tool.
- [ ] **Update the Configuration Reference** to match the actual `AgenticConfig` type: `tests` also accepts `mocha`/`pytest`/`custom` (plus `testCommand`), `telemetry` also accepts `latency`/`cost`, `onSlip` also accepts `notify-only`, `requireExplanationInvariants` also accepts `auth`/`data-schema`/`api-contract`.
- [ ] **Disclose the undocumented internal formulas.** TDS's internal 0.6/0.4 split, FRR's per-file risk weights (0.15/0.25/0.5), and the gate score's 0.4/0.4/0.2 split are all real and load-bearing, but never shown anywhere on the docs site — only the top-level ADX vitals weights (30/25/30/15) are published.
- [ ] **Caveat `estimatedTokens` as an approximation.** The code's own comment already admits it's a ~4-chars/token heuristic, not a real tokenizer count — the docs currently present it as a precise figure.
- [ ] **Document the `adx-vscode` extension** — install path, marketplace link, and what its "run gate" command actually does (opens a terminal with `--dry-run --ci`; it cannot complete a real interactive sign-off from inside the IDE).
- [ ] **Document that MCP's `adx_gate_check` only runs Layer 1.** An IDE agent calling this tool does not get mutation testing or intent cross-reference, unlike the full `adx gate` CLI command — the docs currently describe the MCP tools as exposing "all 6 adx tools" without this caveat.
## Repo Hygiene
- [ ] **Stop tracking `.adx/state/progress.json` and the file under `.adx/tasks/`.** Both are already listed in `.gitignore` but are committed anyway — `git rm --cached` them and let the ignore rule take effect going forward.
- [ ] **Decide how `.evidence/` is meant to persist long-term.** The real CI workflow (`.github/workflows/adx.yml`) uploads `.evidence/` as a 30-day GitHub Actions artifact, which contradicts the docs' framing of it as a permanent, git-committed audit trail. If commit-and-keep is the intended model, the CI workflow should commit the bundle back to the repository, not only upload it as an expiring artifact.
- [ ] **Automate evidence-bundle rotation.** Self-acknowledged in the docs as unsolved; still true after code review — no rotation logic exists anywhere in `adx-gate`.
## Precision Improvements — Lower Priority
- [ ] **Move frozen-path matching from substring/suffix to real path-boundary matching**, in both `packages/adx-maintain/src/frozen.ts` and the generated shell hook — a substring match can over-block files that merely share a path fragment with a frozen pattern.
- [ ] **Guard against a pre-existing pre-commit hook that exits early.** `installHook` appends the adx block after any existing hook content; if that hook calls `exit 0` on its own success path, the appended adx block never runs.
## Why This List Exists
[[adx]] and [[Claims vs Implementation]] describe what adx claims and what it actually does. This is the only one of the four notes in this set that contains a recommendation — everything above is judgment, not fact, and should be read as a starting point for a conversation with Ahnaf, not a verdict on the project.
## Open Questions
- [ ] Which of these does Ahnaf already know about, versus which are genuine blind spots worth raising directly?
- [ ] Does he want this list raised all at once, or scoped down to the 3–4 highest-leverage items for a first conversation?
## Links Into The Vault
- [[adx]] — judgment-level synthesis this list was extracted from
- [[Source Claims]] — what adx claims about itself
- [[Claims vs Implementation]] — the file-level evidence behind every fix above
- [[Mentor Details]] — the mentor whose project this is
## Log
- **2026-07-22:** Extracted every fix implied by [[adx]] and [[Claims vs Implementation]] into this dedicated punch list, and trimmed recommendation language out of both of those notes so the full four-note set separates fact from judgment cleanly.

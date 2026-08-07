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
# adx — Safety-Critical Gaps
**Source:** `sandbox/adx` (local clone, HEAD `1959708`) built and run directly; a throwaway test repo at `~/projects/ai/claude/adx-worktree-throwaway-test/`, kept on disk for further testing
**Verified:** 2026-08-07
**Scope:** `adx-core` (harness, worktree, hooks), `adx-gate` (ui, mutation, evidence), `adx-maintain` (frozen paths, hook)
## Source
This note checks the mechanisms adx relies on to keep an autonomous agent from damaging a real codebase — workspace isolation, verification, the frozen-path lock, and the human sign-off gate — against what actually happens when they run. Every claim below was reproduced by running the built CLI, not inferred from reading source alone; each section says which.
## Key Claims
- **`--exec` provisions a real, isolated git worktree — and then never uses it.** `adapter.complete()` is the one call in the whole harness loop that never receives the worktree path; `assembleContext()` and `runVerificationHooks()` both correctly do.
- This has been true since the very first commit that introduced `adx run` — not a regression, a bug present since hour 2 of the project's single development sprint.
- **Mutation testing corrupts a real source file if the process is interrupted mid-run** — reproduced directly: `SIGKILL` sent ~200ms into a mutated file's test window left the mutation permanently on disk.
- **`adx gate --ci` auto-approves Level 6 with zero human input, and no config field changes this** — tested three separate config variations, all identical outcomes.
- **`adx maintain override` — the fix the tool's own pre-commit hook tells you to run — does not exist**, confirmed by running it.
- Frozen-path matching is substring/suffix, not path-boundary — a pattern like `src/core` also matches `src/core-utils.ts`.
- Task and context content passed through `--exec` is **not** shell-injectable — tested directly with `$()`/backtick/`;`-laden input, confirmed safe. The `--exec` flag's own value, if ever built from something other than the user's direct input, is.
## Full Content
### The worktree is real. The agent never goes near it.
==`harness.ts` passes the provisioned worktree path to context assembly and to verification — but never to the model call itself, the one place isolation would actually matter.==
`createHarness().run()` computes `const workDir = worktreeSession?.dir ?? rootDir` right after `provisionWorktree()` returns. From there:
- `assembleContext(workDir, ...)` — reads `AGENTS.md`/`llms.txt` from the worktree. Correct.
- `runVerificationHooks(workDir, ...)` — runs typecheck/tests against the worktree. Correct.
- `adapter.complete(messages)` — the actual model/agent call. **No `workDir` parameter exists on the `LLMAdapter` interface at all.**

Proof, not inference: I set up a probe script (`/tmp/writing-agent.sh`) that writes a marker file and reports its own `pwd`, wired it in via `adx run "task" --exec /tmp/writing-agent.sh --iterations 1`, and polled `git worktree list` every 0.6s while the run was in flight. Mid-run, `git worktree list` showed **two** real worktrees — the main repo and `.adx/worktrees/session-cubga0z` on branch `adx/session-cubga0z`, with a real checked-out `index.js` inside it. The marker file's own content read `real cwd: /home/.../adx-worktree-throwaway-test` — the main repo root. After the run, `git worktree list` was back to one entry; teardown ran regardless of the run's outcome (`max-iterations` in this case, not `completed`).

The practical consequence: because verification hooks run against `workDir` (the worktree) while the agent's real edits land in `rootDir` (the main tree), a `--exec` run's pass/fail verdict is checking a copy of the code the agent never touched. This isn't "isolation is present but the agent bypasses it" — it's "isolation and verification both run correctly against a directory that has nothing to do with what actually happened."

This has been the case since `d1edd4e` (`feat(harness): Option B`), the commit that introduced `run.ts` and `buildAdapter()`. `git show d1edd4e` shows the identical `execSync(...)` call with no `cwd` option, byte-for-byte the same shape as current `HEAD`. It has never worked as documented, in the entire life of the project.
### Mutation testing can leave a source file permanently broken
==Killing the process ~200ms into a mutation's test window — well before the `finally` block that restores the original file — leaves the mutated content on disk indefinitely, with no trace that anything went wrong.==
`runMutationTest()` in `mutation.ts` writes a mutated version of a real source file to disk (`fs.writeFile(sourceFile, mutated, ...)`), runs the project's test command against it, then restores the original in a `finally` block. A `finally` block only runs if the process is still alive to run it.

Reproduced directly: created `mutation-target.js` containing `const isEnabled = true;`, called `runMutationTest()` with a test command of `sleep 10`, polled the file every 200ms for the mutated string, and `kill -9`'d the process the instant it appeared — about 200ms into a 10-second window. Final state of the file: `const isEnabled = false;`, permanently. No error, no recovery file, no log — a normal-looking file with a deliberately introduced logic bug, indistinguishable from a real one someone wrote by accident.

Any interruption during this window has the same effect: a killed CI job, an OOM kill, a laptop losing power, a Ctrl-C. `Claims vs Implementation.md` already named this as "a small but real operational risk worth knowing about" from reading the code; this confirms it's not small — it's a two-character diff to real source, reproducible on demand.
### CI auto-approval is unconditional — config cannot change it
==`agencyLevel: approved ? AgencyLevel.Resolve : 0` is hardcoded in `ui.ts`'s CI branch; three separate config variations produced identical output.==
`packages/adx-gate/src/ui.ts`'s CI-mode branch (`options.ci === true || !process.stdin.isTTY`) computes `approved = !gateBlocked` and returns `agencyLevel: approved ? AgencyLevel.Resolve : 0` — it never reads `config.boundary.minimumHumanAgencyRequired` at all. `signedBy: 'engineer'` is a literal string in `gate.ts`, not a read of any real identity.

Tested against the throwaway repo with three variations of `adx.config.ts`: `minimumHumanAgencyRequired: AgencyLevel.Flag` (the lowest possible level) with `enforceTasteCheck: false`, and separately `minimumAdxScore: 99`. Every run produced an identical agency-ledger entry: `"level": 6, "signedBy": "engineer"`. This is the difference the mentor-review framing already asked about — not "a config gap someone could close," but a code path that doesn't consult config at all.
### `adx maintain override` doesn't exist — confirmed by running it, and by checking the docs said it should
==The tool's own generated pre-commit hook tells a blocked user to run a command that has never been implemented, anywhere, in any commit.==
```
$ node dist/index.js maintain override --path "index.js" --reason "testing"
 ERROR  Unknown command override
```
`maintain`'s real subcommands: `install`, `uninstall`, `status`, `sync`. `git log --all --diff-filter=A` across full history confirms `override` was never added as a file or a registered subcommand at any point.

This isn't a case where the docs describe a manual workaround that got formalized differently — `docs/orchestrate/maintain.md` has a dedicated `## Overriding a frozen path` section, presenting `adx maintain override --path "..." --reason "..."` in the exact same fenced-code-block style as the three subcommands that work, with no mention anywhere of editing `.adx/frozen-paths.json` by hand instead. The generated shell hook (`hook.ts`) prints the identical syntax as its own unblock instructions when it fires. A user who hits this has every reason to believe the command exists, from two independent sources (docs and the tool's own runtime message), and it doesn't.
### Frozen paths: substring matching, not path-boundary matching
==`file.includes(frozen) || file.endsWith(frozen)` means a frozen pattern like `src/core` also blocks unrelated files that merely contain that text somewhere in their path.==
Both `packages/adx-maintain/src/frozen.ts` and the POSIX-shell equivalent generated into the pre-commit hook use this exact matching. Untested by `adx-maintain`'s own test suite — `checkFrozenViolations`'s tests only cover exact-prefix cases (`src/core/auth/session.ts` matching `src/core/auth`), never an adjacent-but-unrelated path.
### Shell injection: tested, and mostly not exploitable
==Task and context content passed through `--exec` is shielded from shell re-interpretation by a file-write-then-`$(cat file)`-read pattern; the `--exec` flag's own value is not.==
`buildAdapter()`'s shell-out writes the assembled context to a temp file and reads it back via `` `${exec} "$(cat ${tmpFile})"` ``. I tested this directly: passed a task string containing `$(touch ...)`, backtick command substitution, and a `;`-chained command as the task argument to `adx run`. Zero injection markers were created — the double-quoted command substitution boundary prevents the captured file content from being re-parsed as shell syntax, regardless of what it contains.

The `${exec}` value itself is a different story — it sits at the front of the constructed command, unquoted. `adx run "probe" --exec '/bin/echo hi; touch /tmp/PWNED'` did create the marker file. In normal use this requires the same person invoking `adx run` to also supply the malicious `--exec` value — self-inflicted, not a cross-boundary risk — but worth naming precisely rather than either dismissing the whole `--exec` mechanism as unsafe or clearing it entirely.
## Why It Matters
Every one of adx's headline safety claims — isolated execution, safe unattended mutation testing, a governance gate that actually requires a human — has a real implementation behind it. None of the three hold up under the exact conditions they're meant for: an agent left running unattended, a process that gets interrupted, or a CI pipeline running without a person watching. These are the conditions adx is explicitly built to be used in.
## Links Into The Vault
- [[Codebase Deep Read]] — index for this whole pass
- [[Claims vs Implementation]] — the original code-vs-docs review these findings extend; its "Agency Ladder's Integrity Gap" and "What's Actually Well-Built" sections both need reading alongside this note — mutation testing was called out there as genuinely well-built, which still holds for the *scoring*, not for crash-safety
- [[Recommended Fixes]] — its "Integrity Fixes — Highest Priority" list maps directly onto the CI auto-approve and `signedBy` findings here, confirmed unfixed
- [[Mentor Details]] — the mentor whose project this is
## Open Questions
- [ ] Is `--exec`'s worktree bypass something Ahnaf already knows doesn't work, or news? It's central enough to the harness's safety story that it changes how the whole "Orchestrate" pillar should be pitched.
- [ ] Does the mutation-testing crash window matter in practice, or is `adx gate` typically run somewhere (CI) where an interrupted process is rare enough to not worry about?
## Flashcards
Why does `adx run --exec`'s verification step check the wrong copy of the code?::`workDir` (the isolated worktree) is passed to `assembleContext()` and `runVerificationHooks()`, but never to `adapter.complete()` — the actual agent call runs in the main repo while everything that checks its work looks at an unmodified worktree #cards/ai
What does killing `adx gate` mid-mutation-test actually do to a real file?::Leaves the injected bug (e.g. `true`→`false`) permanently on disk — the `finally`-block restore never runs if the process is killed, reproduced with a `SIGKILL` ~200ms into a 10-second test window #cards/ai
Why can't any `adx.config.ts` setting stop `adx gate --ci` from auto-approving at Level 6?::The CI branch in `ui.ts` hardcodes `agencyLevel: approved ? AgencyLevel.Resolve : 0` and never reads `config.boundary.minimumHumanAgencyRequired` — confirmed by testing three different config variations with identical results #cards/ai

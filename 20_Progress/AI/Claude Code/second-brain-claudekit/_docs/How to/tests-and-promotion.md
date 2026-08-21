# How to — tests/ and promotion

## The gate `tests/` exists to enforce

`_docs/Promotion-Criteria.md`'s question 1 — "did it actually run without a manual workaround?" — is a judgment call unless something concrete backs it up. `tests/<type>/<repo-name>/` (per `60_Claude/vault-rules/pipeline-conventions.md`) is that concrete backing: either a runnable script reproducing the real install/init/test commands, or a dated markdown log of the real commands and their real output. A `tested-tools/` folder without a matching `tests/` entry is a claim without evidence.

## How this actually plays out — two worked examples

**`tests/commands/cpr-compress-preserve-resume/2026-08-19-test-log.md`** — the real thing this convention is for. `cpr-compress-preserve-resume` has no separate build/install step (it's three markdown skill files), so "ran it for real" meant: install into a scratch project per the README, then actually execute the documented step logic — project-root detection, file writes, the summary-only read contract, the line-budget check — with real `bash`/`awk`/`wc` commands against real files. The log is the literal transcript of those commands and their real output, not a description of them. This backed the verdict in `tested-tools/commands/cpr-compress-preserve-resume/VERDICT.md`.

**`tests/skills/mattpocock-engineering/README.md`** — the honest opposite case. 17 skills sit in `tested-tools/skills/mattpocock-engineering/`, copied for review, but **zero have been individually tested** — `tested-tools/README.md` already says so. The `tests/` entry for this one isn't a passing log; it's a backlog table naming exactly which of the 17 are untested, so the gap stays visible instead of getting silently assumed-closed the longer the folder sits there. Per `pipeline-conventions.md`: **never write a test file claiming something passed if it hasn't actually been run** — an honest backlog is the correct content here, not a fabricated pass.

## Connecting `tests/` to `_docs/Promotion-Criteria.md` and the Qualification-Checklist

`60_Claude/Qualification-Checklist.md`'s first checklist item is literally "Ran for real, not read about" — `tests/` is where that gets written down before the Jarvis-side `Tool Map.md` row cites it. The checklist's second gate — a piece earning its own `<use-case>/` folder inside `tested-tools/` — requires "that specific piece... individually tested, on its own, against a real task," which is exactly what a `tests/` entry proves or fails to prove. If `tests/<type>/<repo-name>/` doesn't exist yet, or only documents a backlog, the corresponding `tested-tools/` entry should stay ungrouped (no `<use-case>/` layer) — the two folders are meant to move together, not independently.

## What to do when starting a new test

1. Confirm `sandbox/<repo-name>/` actually exists and was actually cloned — not assumed from a README.
2. Run the real command(s) — install, init, invoke — and capture the real output.
3. Write it to `tests/<type>/<repo-name>/<dated-file>.md` (or a runnable script, if the commands are worth re-running mechanically later).
4. Only then write or update the matching `tested-tools/` entry and its verdict.

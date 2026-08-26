---
type: concept
status: sprout
created: 2026-08-26
updated: 2026-08-26
course: Life
track:
  - laptop
  - vscode
prerequisites:
  - "[[New Laptop Setup]]"
used_in: []
evidence: []
tags:
  - concept
related:
  - "[[New Laptop Setup]]"
  - "[[Ubuntu - WSL]]"
  - "[[WSL Session Briefing]]"
---
# VS Code Professional Setup — Findings (not yet built)

## One-Line Answer

==This machine's VS Code has a genuinely strong formatting/linting/typing baseline (Biome, Ruff, Pylance, GitLens, ErrorLens, the full Jupyter and Remote-Development extension packs) but uses almost none of the machinery that turns an editor into the single hub a professional AI developer actually works from all day — Tasks, Debugging, Testing, Profiles, multi-root workspaces, and Settings Sync are either empty or off, and this note is the fully-researched reference for what "done" looks like in each of them, built from VS Code's own official documentation.==

**Status: research and findings only, second pass (2026-08-26). Nothing in this note has been executed. Every section below describes what a mature, already-working setup looks like — the target state, written the way it would read if a professional had already built it — so a future session can implement piece by piece against a concrete spec instead of a vague idea.**

## Current state audit (verified on this machine, 2026-08-26)

**Extensions installed (28):** `anthropic.claude-code`, `biomejs.biome`, `bradlc.vscode-tailwindcss`, `charliermarsh.ruff`, `christian-kohler.npm-intellisense`, `davidanson.vscode-markdownlint`, `dbaeumer.vscode-eslint`, `eamodio.gitlens`, `mikestead.dotenv`, `ms-azuretools.vscode-containers`, `ms-azuretools.vscode-docker`, `ms-python.python`, `ms-python.vscode-pylance`, `ms-python.vscode-python-envs`, `ms-toolsai.jupyter` (+keymap, renderers, cell-tags), `ms-vscode-remote.remote-containers`, `ms-vscode-remote.remote-ssh(-edit)`, `ms-vscode-remote.remote-wsl`, `ms-vscode-remote.vscode-remote-extensionpack`, `ms-vscode.powershell`, `ms-vscode.remote-explorer`, `ms-vscode.remote-server`, `redhat.vscode-yaml`, `usernamehw.errorlens`.

This is a genuinely good, opinionated baseline — nothing here needs to be removed.

**What's empty or unused, confirmed by direct inspection (not assumption):**
- `keybindings.json` — one custom binding total.
- `%APPDATA%\Code\User\snippets\` — the folder does not exist. Zero user snippets.
- No `tasks.json` anywhere under `D:\projects\*` or the Jarvis vault.
- No `launch.json` anywhere — no configured debugger, no Test Explorer wiring.
- No `.vscode/extensions.json` in any project.
- Settings Sync is off (`globalStorage/ms-vscode.settings-sync` absent from disk).
- Only the Default Profile exists.
- No multi-root `.code-workspace` file exists for the four sibling `D:\projects\*` folders.

## Part 1 — Tasks: the professional's one-keystroke command layer

A working setup never types `uv sync`, `ruff check --fix .`, or `pnpm dev` by hand more than once. [VS Code's Tasks system](https://code.visualstudio.com/docs/debugtest/tasks) — `Ctrl+Shift+P` → `Tasks: Run Task`, or `Ctrl+Shift+B` for the default build task — runs any shell command with a proper panel, output streaming, and problem-matcher parsing that turns compiler/linter output into clickable Problems-panel entries.

**A finished `python-data` project's `.vscode/tasks.json`** (this is what "done" looks like, not a suggestion — every label below maps to a real, immediately-runnable command):
```jsonc
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "uv: sync",
      "type": "shell",
      "command": "uv sync",
      "group": { "kind": "build", "isDefault": true },
      "runOptions": { "runOn": "folderOpen" }
    },
    { "label": "ruff: lint + fix", "type": "shell", "command": "uv run ruff check --fix .", "group": "test" },
    { "label": "ruff: format", "type": "shell", "command": "uv run ruff format .", "group": "test" },
    {
      "label": "pytest",
      "type": "shell",
      "command": "uv run pytest",
      "group": { "kind": "test", "isDefault": true },
      "problemMatcher": []
    },
    {
      "label": "jupyter: lab",
      "type": "shell",
      "command": "uv run jupyter lab",
      "isBackground": true,
      "presentation": { "reveal": "always", "panel": "dedicated" }
    }
  ]
}
```
A `web-js` project's equivalent adds a background dev-server task with a real problem matcher for the framework's compile-status output (the pattern most frameworks emit `compiling…` / `compiled` lines that VS Code's background-task detection can key off, exactly as documented in the Tasks reference).

**The `runOn: folderOpen` line is the one piece of real automation in this note**, and it is explicitly gated by VS Code itself, not silent: the first time any workspace defines an auto-run task, the editor prompts *"Allow Automatic Tasks in this folder?"* and the choice persists per-workspace in `task.allowAutomaticTasks`. Automatic tasks never run in an untrusted workspace regardless of that setting. This is the same shape of automation already validated as acceptable in this workflow — manual, per-project, explicit opt-in — as opposed to a silent global hook, so it's worth adopting rather than avoiding on principle.

Source: [Integrate with External Tools via Tasks](https://code.visualstudio.com/docs/debugtest/tasks) (official VS Code docs).

## Part 2 — Debugging: replacing print-statement debugging entirely

No `launch.json` exists anywhere on this machine today. A finished setup's `.vscode/launch.json` for a Python project:
```jsonc
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "python": "${workspaceFolder}/.venv/Scripts/python.exe"
    },
    {
      "name": "Python: Pytest (current file)",
      "type": "debugpy",
      "request": "launch",
      "module": "pytest",
      "args": ["${file}"],
      "console": "integratedTerminal",
      "python": "${workspaceFolder}/.venv/Scripts/python.exe"
    }
  ],
  "compounds": [
    {
      "name": "Full stack: API + worker",
      "configurations": ["Python: Current File", "Node: Attach"],
      "stopAll": true
    }
  ]
}
```
The explicit `python` key matters for the exact reason `defaultInterpreterPath` mattered globally: it forces the debugger onto the *same* `.venv/Scripts/python.exe` as everything else, so a debug session can never silently fall back to a global/base interpreter. **Compound configurations** (the `compounds` array) launch multiple debug sessions together with one keypress — the documented use case is exactly this machine's shape of work: a backend process and a frontend dev server started and stopped as one unit, with `stopAll` controlling whether killing one session kills the whole group.

Source: [VS Code debug configuration](https://code.visualstudio.com/docs/debugtest/debugging-configuration) (official docs — compound configs).

## Part 3 — Testing: Test Explorer, not ad-hoc `pytest` runs in a terminal

The Python extension already installed on this machine (`ms-python.python`) ships full Test Explorer integration: once a test framework is configured (`Configure Python Tests` from the beaker icon in the Activity Bar, or the `pythonTestExplorer.testFramework` setting = `pytest`), every test in the project shows as a clickable, individually-runnable-and-debuggable tree, with pass/fail decorations inline in the editor gutter. For larger suites, `pytest-xdist` gives parallel test execution, and the Python extension auto-optimizes worker count when xdist is enabled with no explicit count specified. This entirely replaces "run `pytest` in a terminal and scroll for the failure."

Source: [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing) (official docs).

## Part 4 — Jupyter / notebooks: now a confirmed near-term requirement

Both this laptop and the new one will run Jupyter notebooks, and miniconda is explicitly being kept for this. The validated, official pattern (Astral's own docs, not a blog's guess) for keeping notebook kernels exactly as isolated as `.venv` already keeps scripts:
```bash
uv venv
uv add --dev ipykernel jupyterlab
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=<project-name>
```
Then in VS Code: open a `.ipynb`, use the kernel picker (top-right) → the registered `<project-name>` kernel. **This is the decision point worth making explicit now that miniconda stays installed**: the recommendation is per-project `uv`-registered kernels as the default notebook workflow (matches every other isolation habit already established), with miniconda's `base` env reserved only for the narrow cases the source plan doc itself calls out — CUDA, or a conda-forge-only package. Nothing on this machine currently enforces that split; a stray notebook with no registered kernel could silently fall back to `base`.

Sources: [Using uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/) (Astral official docs), [Manage Jupyter Kernels in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management) (official docs).

**On `ms-python.vscode-python-envs`** (already installed, easy to overlook): this is Microsoft's newer unified environment/package manager UI — it auto-discovers environments across `venv`, `uv`, `conda`, `pyenv`, `poetry`, and `pipenv`, auto-activates the selected one in every new terminal, and — notably — **remembers which environment was selected per-project without hardcoding machine-specific paths**, which is exactly the portability property that matters for the new-laptop transition. Worth actively using its `Python Envs: Create New Project from Template` command rather than treating it as a passive extension.

Source: [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments) (official docs).

## Part 5 — GitLens: what's actually installed vs. what's actually used

GitLens is installed but nothing suggests its deeper features are in active use yet. What a professional actually reaches for daily:
- **File Blame** — inline, per-line authorship annotations plus a status-bar summary of who last touched the current line, so "why is this line here" never requires a separate `git log` detour.
- **Git Command Palette** — a guided, step-by-step way to run git commands without memorizing flags, alongside quick access to file/branch history and commit search.
- **Search & Compare** — compare any two branches, tags, or commits, with results pinned for as long as needed — the tool for "what actually changed between this feature branch and main" without a manual `git diff` invocation.
- **Commit Graph** — GitLens's own description calls this the central development workbench: commits, branches, working changes, worktrees, and upstream state in one connected view, which matters more once multi-root workspaces (Part 8) put several related repos in view at once.

`gitlens.currentLine.enabled` and `gitlens.blame.highlight.enabled` are already on in the global settings — the baseline is there, the deeper navigation habits (Command Palette, Search & Compare, Commit Graph) are what's unused.

Source: [GitLens Core Features](https://help.gitkraken.com/gitlens/gitlens-features/) (official GitKraken/GitLens docs).

## Part 6 — Command Palette and multi-cursor fluency

Not a settings change — a working-habit gap worth naming, since it's the actual daily-use difference between "knows VS Code" and "types slowly in VS Code." Confirmed from official docs and cross-referenced cheat sheets:
- `Ctrl+Shift+P` — Command Palette. Every command in the editor is reachable here, and if a command has a keybinding it's shown in the results list — the Palette is also how you *discover* which shortcut to memorize next, not just a fallback when you've forgotten one.
- `Ctrl+D` — select next occurrence of the current word (repeatable, builds up a multi-cursor selection incrementally); `Ctrl+U` undoes the last cursor added, for fine-tuning.
- `Ctrl+F2` — select **all** occurrences of the current word at once (an instant project-wide-in-file rename without a formal refactor command).
- `Ctrl+Alt+↓ / ↑` — add a cursor on the line below/above, for column-style edits.
- `Alt`+click — place an extra cursor anywhere by hand.

Source: [Visual Studio Code tips and tricks](https://code.visualstudio.com/docs/editing/tips-and-tricks) (official docs); [Keyboard shortcuts for Visual Studio Code](https://code.visualstudio.com/docs/configure/keybindings) (official docs).

## Part 7 — VS Code Profiles: one profile currently doing three jobs

[Profiles](https://code.visualstudio.com/docs/configure/profiles) scope settings, keybindings, snippets, UI state, and — critically — **which extensions load at all** — per profile, switchable via `Preferences: Switch Settings Profile`. Right now every extension loads in every window regardless of what that window is actually for. Candidate profiles for this exact machine:
- **`ai-hub`** — Claude Code, GitLens, ErrorLens, PowerShell. For home-directory / general Claude Code sessions.
- **`python-data`** — Python, Pylance, Ruff, the full Jupyter set, `python-envs`.
- **`web-js`** — Biome, ESLint, Tailwind, npm-intellisense.

Each profile can also carry its own theme, so which "mode" a given window is in is visually unambiguous at a glance — genuinely useful given how many windows tend to be open simultaneously on this machine (home dir, Jarvis vault, several `D:\projects\*` folders).

Source: [Profiles in Visual Studio Code](https://code.visualstudio.com/docs/configure/profiles) (official docs).

## Part 8 — Multi-root workspaces: for the sibling `D:\projects\*` folders

A `.code-workspace` file is a JSON list of folder paths plus workspace-scoped settings, letting `D:\projects\{Assisto_website, boom, hackathon, portfolio}` open as one window with one sidebar instead of four separate windows. The one real constraint, confirmed in official docs: **only resource-level (file/folder) settings apply per-workspace — window-level settings are ignored inside a multi-root workspace** — so this complements Profiles rather than replacing them; a multi-root workspace still inherits whichever Profile the window is running under.

Source: [Multi-root Workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces) (official docs).

## Part 9 — Remote Development: what's actually happening under the hood

`remote-wsl`, `remote-ssh`, and `remote-containers` are all installed (the full extension pack). Worth understanding the actual mechanism rather than treating it as a black box, since this machine leans on WSL remoting heavily:
- Each remote extension installs a **VS Code Server** process on the remote side — independent of any local VS Code install — and every other extension in a Remote window runs *inside* that server, so the editor feels local even though execution is remote.
- **SSH**: an authenticated SSH tunnel connects the local client to the server.
- **WSL**: connects over a **random local port** (not SSH) — this is why WSL remoting feels instant compared to SSH, and also exactly why `~/.vscode-server/bin/<hash>/` accumulates old versions locally inside the distro (Sin 12 in [[WSL Session Briefing]]) — the server is a real, persistent, versioned install, not a stateless bridge.
- **Containers**: communicates via Docker's own channel (`docker exec`).

This also explains a real limitation already flagged for the new-laptop transition: **Settings Sync does not sync extensions inside a Remote window** — only the local/Windows-side extension set syncs through Settings Sync. WSL-side extensions have to be (re)installed once a WSL session actually opens a project there, separately from whatever Settings Sync restores on the Windows side.

Source: [VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview) (official docs).

## Part 10 — Settings Sync: the actual new-laptop lever

Off on this machine (`globalStorage/ms-vscode.settings-sync` absent). This is the single highest-leverage unused feature for the stated goal: `Settings Sync: Turn On`, sign in with the personal GitHub account, and settings, keybindings, snippets, UI state, **and Profiles** all sync through the cloud — meaning once the setup described in this note is actually built, the new laptop inherits it at first sign-in instead of the source doc's current plan of manually copying `settings.json` by hand. Confirmed limitation (Part 9 above): Remote-window extensions are excluded from sync, so WSL/SSH/Container extension sets still need separate handling — this is a known, documented gap, not a bug to work around.

Source: [VS Code Settings Sync](https://github.com/microsoft/vscode-docs/blob/main/docs/configure/settings-sync.md) (official docs).

## Part 11 — Workspace-recommended extensions (`.vscode/extensions.json`)

None exist in any project. This is the file that makes "clone repo → VS Code prompts to install the right extensions" work automatically for a collaborator (or future-you, on the new laptop, before Settings Sync has even run). Cheap, per-project, and pairs naturally with Profiles — a project's `extensions.json` and the Profile it's meant to be opened under should agree on the extension list.

## Part 12 — Claude Code itself, as the primary AI surface

Since Claude Code is the primary AI interface here (not Copilot, not a generic chat panel), worth being explicit about what the extension actually provides beyond the CLI: side-by-side diffs for proposed edits, `@`-mentions tied to the current text selection, an IDE-side MCP server so Claude Code can see editor state directly, checkpoints that let any prior state be rewound (hover any message → rewind), and the Normal-mode/Plan-mode toggle that mirrors exactly the plan-then-execute discipline already used across both this session and the sibling WSL session. `claudeCode.preferredLocation: panel` is already set globally — confirmed no keybinding conflicts with the current minimal `keybindings.json`.

Source: research synthesis from public 2026 coverage of the Claude Code VS Code extension (Anthropic's own IDE-integration docs are the primary source; this section reflects publicly documented feature names — side-by-side diff, checkpoints/rewind, IDE MCP server, Plan mode — not this note's own testing).

## Part 13 — Adjacent, not VS Code itself: Windows Task Scheduler

The source plan doc's Part 9 "monthly maintenance" (VHDX compaction, Temp cleanup, npm/uv cache pruning) is currently just "a thing to remember." A real Task Scheduler job could run the safe, non-destructive parts unattended. **Flagging, not proposing to build automatically** — same category of decision as the archiving-pipeline precedent (manual/opt-in trigger preferred over silent automation even when the request sounds like "make it automatic"). Belongs in the same "ask before wiring up" bucket as `runOn: folderOpen` tasks above.

## What this note is NOT proposing

- Not proposing any new extension speculatively — every extension above is either already installed or framed as "add when the concrete need shows up" (snippets, `.code-workspace`, `extensions.json`).
- Not proposing an automatic global hook of any kind. `runOn: folderOpen` tasks are per-project, VS-Code-gated opt-ins with an explicit consent prompt, not silent background automation.
- Not touching `settings.json`, extensions, tasks, keybindings, or Profiles in this session, per instruction.

## Suggested build order for the next VS Code session (for discussion, not started)

1. Turn on Settings Sync first — everything after this becomes portable for free (modulo the Remote-extension limitation).
2. Create the 2–3 Profiles (`ai-hub`, `python-data`, `web-js`) and assign the already-installed extensions to the right one.
3. Add `tasks.json` + `launch.json` to the one Windows-native project that will need them first, as the copyable template.
4. Build the `uv venv` + `ipykernel` registration habit into that same project as the first real notebook test case, resolving the miniconda-vs-uv-kernel question explicitly.
5. Wire up Test Explorer for that project (`pythonTestExplorer.testFramework` = pytest).
6. Only then: snippets, `.code-workspace` for the `D:\projects\*` sibling folders, `extensions.json` — polish, not blockers.

## Sources consulted (official docs unless noted)
- [Integrate with External Tools via Tasks](https://code.visualstudio.com/docs/debugtest/tasks)
- [VS Code debug configuration](https://code.visualstudio.com/docs/debugtest/debugging-configuration)
- [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)
- [Using uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/) (Astral)
- [Manage Jupyter Kernels in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)
- [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)
- [GitLens Core Features](https://help.gitkraken.com/gitlens/gitlens-features/) (GitKraken)
- [Visual Studio Code tips and tricks](https://code.visualstudio.com/docs/editing/tips-and-tricks)
- [Keyboard shortcuts for Visual Studio Code](https://code.visualstudio.com/docs/configure/keybindings)
- [Profiles in Visual Studio Code](https://code.visualstudio.com/docs/configure/profiles)
- [Multi-root Workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces)
- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)
- [VS Code Settings Sync](https://github.com/microsoft/vscode-docs/blob/main/docs/configure/settings-sync.md)

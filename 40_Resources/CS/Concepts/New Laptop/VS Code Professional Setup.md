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
---
# VS Code Professional Setup — Findings (not yet built)

## One-Line Answer

==This machine's VS Code is currently a well-formatter, half-IDE — Biome/Ruff/Pylance/GitLens/ErrorLens are genuinely good choices already in place, but every layer that turns an editor into a *hub* (tasks, debugging, snippets, profiles, multi-root workspaces, notebook kernel discipline, Settings Sync) is either unused or empty on this machine.==

**Status: research and findings only. Nothing in this note has been executed. This is the input for a future session that will actually build it, one piece at a time, with sign-off before each change** — matching the standing preference for manual, deliberate setup over silently automating things (see [[New Laptop Setup]] and the consent-gates pattern already established for archiving pipelines).

## Current state audit (verified this session, 2026-08-26)

**Extensions installed (28):**
`anthropic.claude-code`, `biomejs.biome`, `bradlc.vscode-tailwindcss`, `charliermarsh.ruff`, `christian-kohler.npm-intellisense`, `davidanson.vscode-markdownlint`, `dbaeumer.vscode-eslint`, `eamodio.gitlens`, `mikestead.dotenv`, `ms-azuretools.vscode-containers`, `ms-azuretools.vscode-docker`, `ms-python.python`, `ms-python.vscode-pylance`, `ms-python.vscode-python-envs`, `ms-toolsai.jupyter` (+keymap, renderers, cell-tags), `ms-vscode-remote.remote-containers`, `ms-vscode-remote.remote-ssh(-edit)`, `ms-vscode-remote.remote-wsl`, `ms-vscode-remote.vscode-remote-extensionpack`, `ms-vscode.powershell`, `ms-vscode.remote-explorer`, `ms-vscode.remote-server`, `ms-vscode.vscode-chat-customizations-evaluations`, `redhat.vscode-yaml`, `usernamehw.errorlens`.

This is already a strong, opinionated baseline — genuinely good picks (Ruff over Pylint/Black, Biome over Prettier+ESLint-only, GitLens, ErrorLens, the full Jupyter set, the full Remote pack). **Nothing here needs to be ripped out.**

**What's empty or unused:**
- `keybindings.json` — one custom binding total (`ctrl+shift+e`). No chorded bindings, no custom snippet-trigger keys, no AI-panel shortcuts.
- `snippets/` folder — **does not exist.** Zero user snippets.
- No `tasks.json` found anywhere under `D:\projects\*` or the Jarvis vault — the entire Tasks system (`Terminal > Run Task`) is unused.
- No `launch.json` found anywhere — no configured debugger. Python/Node debugging currently happens by hand (print statements, or ad-hoc terminal runs) rather than through VS Code's breakpoint debugger.
- No `.vscode/extensions.json` (workspace-recommended-extensions file) in any project — nothing tells a collaborator (or future-you on the new laptop) which extensions a given repo expects.
- **Settings Sync is off** (`globalStorage/ms-vscode.settings-sync` absent). All of this configuration — the hard-won Pylance fix, the exclude patterns, the formatter setup — currently exists on exactly one machine and would need to be manually re-typed on the new laptop.
- Only one VS Code Profile exists (the Default). Home-directory sessions (Claude Code / general shell work), Windows-native JS projects, and future Jupyter/data work are all sharing one undifferentiated settings-and-extension surface.
- No multi-root `.code-workspace` file anywhere — `D:\projects\{Assisto_website,boom,hackathon,portfolio}` are four separate single-folder windows with no shared view.

## Findings, by system

### 1. Tasks (`tasks.json`) — turn recurring commands into one keypress

VS Code tasks (`Ctrl+Shift+P` → `Tasks: Run Task`, or `Ctrl+Shift+B` for the default build task) run shell commands from inside the editor, with output in an integrated panel, problem-matcher parsing, and `dependsOn` chaining. Nothing here uses this — every command (lint, format check, `uv sync`, `npm run dev`) is typed by hand every time.

**What a real setup looks like**, per-project `.vscode/tasks.json`:
```jsonc
{
  "version": "2.0.0",
  "tasks": [
    { "label": "uv: sync", "type": "shell", "command": "uv sync", "group": "build" },
    { "label": "ruff: lint + fix", "type": "shell", "command": "uv run ruff check --fix .", "group": "test" },
    { "label": "dev: next", "type": "shell", "command": "pnpm dev", "isBackground": true,
      "problemMatcher": { "pattern": { "regexp": "." }, "background": { "activeOnStart": true, "beginsPattern": "compiling", "endsPattern": "compiled" } } }
  ]
}
```
There's also `"runOptions": { "runOn": "folderOpen" }` for a task that fires automatically when a folder opens — e.g. auto-running `uv sync` the moment a project is opened so the environment is never stale. **This is real automation, gated by VS Code itself, not a silent hook**: the first time any workspace defines an auto-run task, VS Code prompts "Allow Automatic Tasks in this folder?" and the choice is stored per-workspace in `task.allowAutomaticTasks` — untrusted workspaces never auto-run regardless. That consent gate is exactly the shape of automation already validated as acceptable in this workflow (manual opt-in per project, not a blanket global hook), so `folderOpen` tasks are worth adopting once tasks.json exists at all, rather than something to avoid on principle.

### 2. Debugging (`launch.json`) — replace print-statement debugging

No `launch.json` exists anywhere. For Python (the primary language once real dev work resumes here per the "Windows Python is quick scripts, WSL is real work" rule — though this machine will also run notebooks, see below), a per-project config looks like:
```jsonc
{
  "version": "0.2.0",
  "configurations": [
    { "name": "Python: Current File", "type": "debugpy", "request": "launch",
      "program": "${file}", "console": "integratedTerminal",
      "python": "${workspaceFolder}/.venv/Scripts/python.exe" }
  ]
}
```
Note the explicit `python` path — same `${workspaceFolder}/.venv/Scripts/python.exe` pattern already fixed globally for `python.defaultInterpreterPath`, so debug sessions use the *same* interpreter as everything else instead of silently falling back to a global one.

### 3. Jupyter / notebook workflow — now explicitly needed (confirmed for future use on both laptops)

Current gap: the Jupyter extension family is installed, but there's no established per-project kernel-registration habit, and `.venv`/`ipynb_checkpoints` clutter (already seen in the home directory scan) has no exclude pattern yet.

The validated 2026 pattern (confirmed via Astral's own docs and the `ms-toolsai.jupyter` kernel-picker docs, not just training data):
```bash
uv venv                                    # per-project .venv, already the house pattern
uv add --dev ipykernel jupyterlab
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=<project-name>
```
Then in VS Code: open a `.ipynb`, use the kernel picker (top-right of the notebook) → "Select Another Kernel" → "Jupyter Kernel" → the registered `<project-name>` kernel, which points at that project's `.venv`, never a global/base interpreter. This means **every notebook's kernel is exactly as isolated as every script's interpreter already is** — one habit (`uv venv` + register kernel) instead of two different mental models for "running code" vs "running a notebook." Given miniconda is being kept specifically for future Jupyter/notebook use, worth deciding explicitly whether miniconda's `base` env or per-project `uv`-managed kernels are the actual notebook workflow going forward — right now nothing enforces either, so a stray notebook could silently pick miniconda's `base` interpreter if a project has no registered kernel yet. Recommend: per-project `uv` kernels as the default, miniconda `base` reserved only for the specific cases Part 5 of the source plan doc already calls out (CUDA, conda-forge-only packages) — not general notebook work.

### 4. Snippets — zero exist

User snippets (`Ctrl+Shift+P` → `Snippets: Configure User Snippets`) are per-language JSON files under `%APPDATA%\Code\User\snippets\`. None exist. Low effort, real payoff for repeated boilerplate this workflow already generates a lot of — e.g. a `python.json` snippet for the vault's own "concept note" frontmatter template, or a `pyproject-uv` snippet. Worth building once real recurring boilerplate is identified rather than speculatively — this is a "note what to build," not "build ten generic snippets nobody asked for."

### 5. Keybindings — one custom binding

Reasonable candidates once the above systems exist: a keybinding for `workbench.action.tasks.runTask`, one for `workbench.action.debug.start`, and — since Claude Code is the primary AI interface here — confirming there's no conflict between `claudeCode.preferredLocation: panel` and any existing panel-focus binding (checked: no conflict currently).

### 6. VS Code Profiles — one profile doing three jobs

Profiles (`Preferences: Switch Settings Profile`, or the Profiles gear in the bottom-left) scope settings, keybindings, snippets, UI state, and — critically — **which extensions are active**, per profile. Right now every extension (Docker, Tailwind, Jupyter, all of it) loads for every window, whether it's a Next.js project, a Python data notebook, or just the home directory opened to run Claude Code. Candidate profiles for this machine specifically:
- **`ai-hub`** — minimal: Claude Code, GitLens, ErrorLens, PowerShell. For the home-directory / general-chat sessions.
- **`python-data`** — Python, Pylance, Ruff, the full Jupyter set, python-envs.
- **`web-js`** — Biome, ESLint, Tailwind, npm-intellisense, TypeScript-related.
Each profile can also pin its own theme/font size, so at a glance which "mode" a window is in is visually obvious — useful given how many windows tend to be open at once on this machine (home dir, Jarvis vault, 4 `D:\projects\*` folders).

### 7. Multi-root workspaces (`.code-workspace`) — for the four `D:\projects\*` folders

A `.code-workspace` file is just a JSON list of folder paths plus workspace-scoped settings — it lets `D:\projects\{Assisto_website, boom, hackathon, portfolio}` open as one window with one sidebar, instead of four separate VS Code windows today. Caveat found in research: **only resource-level settings (file/folder-scoped) apply per-workspace — window-level settings (like `window.title` or global keybindings) are ignored inside a multi-root workspace**, so this doesn't replace Profiles, it complements them. Good candidate once there's an actual reason to view >1 of these projects side by side; not valuable to build speculatively for projects that are never touched together.

### 8. Workspace-recommended extensions (`.vscode/extensions.json`)

None exist in any project. This is the file that makes "clone repo → VS Code prompts to install the right extensions" work, and it's exactly the mechanism that should replace manually remembering "this project needs Tailwind IntelliSense, that one doesn't." Cheap, per-project, worth adding once Profiles exist (so the recommendation and the profile agree).

### 9. Settings Sync — off, and this is the actual "new laptop" lever

This is the single highest-leverage unused feature for the stated goal of practicing the new-laptop transition on this machine. Turning it on (`Settings Sync: Turn On`, sign in with the personal GitHub account) syncs settings, keybindings, snippets, UI state, **and Profiles** through the cloud — meaning the new laptop's VS Code could inherit this exact setup (once actually built) automatically at first sign-in, no manual re-typing, no copying `settings.json` by hand as the source doc's Part 1 currently plans to do.
**Important limitation confirmed in research:** Settings Sync does **not** sync extensions inside a Remote window (WSL, SSH, Dev Container) — only the local/Windows-side extension set syncs. Given this machine's `remote-wsl` usage, WSL-side extensions (whatever gets installed once a WSL session opens a project there) will still need to be handled separately, matching the WSL note's own scope boundary.

### 10. Adjacent (not VS Code, but IDE-hub-adjacent): Windows Task Scheduler

The source doc's Part 9 "monthly maintenance" (VHDX compaction, Temp cleanup, npm/uv cache clean) is currently just "a thing to remember," not automated. A genuine Task Scheduler job (`Register-ScheduledTask`, monthly trigger) could run the safe, non-destructive parts (Temp cleanup, cache pruning) unattended. **Flagging, not proposing to build automatically** — this is the same category of decision as the archiving-pipeline precedent (this user prefers manual/opt-in triggers over silent automation even when the request sounds like "make it automatic"), so this belongs in the same "ask before wiring up" bucket as the `folderOpen` tasks above, not something to schedule without an explicit go-ahead.

## What this note is NOT proposing

- Not proposing to install any new extension speculatively — every extension above is either already installed or explicitly framed as "add when the concrete need shows up" (snippets, `.code-workspace`).
- Not proposing an automatic global hook of any kind. Tasks with `runOn: folderOpen` are per-project, VS-Code-gated opt-ins, not silent background automation — flagged for a future explicit decision, same as the Task Scheduler idea.
- Not touching `settings.json`, extensions, tasks, or keybindings in this session, per instruction.

## Suggested build order for the next VS Code session (for discussion, not started)

1. Turn on Settings Sync first — everything after this point becomes portable for free.
2. Create the 2–3 Profiles (`ai-hub`, `python-data`, `web-js`) and assign existing extensions to the right one.
3. Add `tasks.json` + `launch.json` to the one real Windows-native project that will need them first (whichever `D:\projects\*` project is actively worked on next), as the template to copy elsewhere.
4. Build the `uv venv` + `ipykernel` registration habit into that same project as the first real notebook test case.
5. Only then: snippets, `.code-workspace`, `extensions.json` — these are polish, not blockers.

Sources consulted this session: [VS Code Tasks docs](https://code.visualstudio.com/docs/debugtest/tasks), [VS Code Profiles docs](https://code.visualstudio.com/docs/configure/profiles), [VS Code multi-root workspaces docs](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces), [Astral uv + Jupyter guide](https://docs.astral.sh/uv/guides/integration/jupyter/), [VS Code Settings Sync docs](https://github.com/microsoft/vscode-docs/blob/main/docs/configure/settings-sync.md).

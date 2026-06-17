---
type: concept
status: sprout
created: 2026-06-17
updated: 2026-06-17
course: Life
track:
  - laptop
mastery_level: "1"
prerequisites:
  - "[[Ubuntu - WSL]]"
evidence: []
tags:
  - concept
related:
  - "[[Summer Grind]]"
---
# New Laptop Setup
## One-Line Answer

== ==
# Windows
## New Laptop Setup Plan — Professional Developer Configuration

**Written:** 2026-06-02  

**Context:** Moving from current Windows laptop in ~15 days. Goal: never repeat the storage, environment, and workflow mistakes made on this machine.  

**Profile:** Windows + WSL Ubuntu, full-stack JS + Python AI/agentic work, Obsidian-based second brain (Jarvis + The Plan), Claude Code CLI as primary AI interface.

  

---

  

## PART 0 — WHAT WENT WRONG ON THIS LAPTOP (THE HONEST AUDIT)

  

Before planning the new setup, name every mistake clearly. These are the sins to not repeat.

  

### Sin 1: WSL was installed on C: by default

The ext4.vhdx landed in `AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_*\LocalState\` on C: and grew to ~74 GB before anyone noticed. The VHDX was eventually moved to `D:\WSL\Ubuntu\`, but only after months of pain. **Lesson: WSL goes to D: on day one. There is no day two for this decision.**

  

### Sin 2: Python installed three times, used zero times properly

- `C:\Python313\python.exe` — standalone install, system-wide, probably used for one-off scripts

- `C:\Users\Anant Gupta\miniconda3\` — installed for AI/RAG work, never actually used because the concept of environments was unclear

- `/usr/bin/python3` (WSL system Python 3.12.3) — used implicitly, no isolation

  

There is one conda env: `csci4041` — a 1.68 GB environment for a university course, now abandoned. No Python project on this machine uses a properly isolated virtual environment except `tradingview` which has a `.venv` that was probably created accidentally.

  

**The actual confusion about "sandboxes" and miniconda is explained in Part 5.** The mistake was installing the tool without understanding why it exists.

  

### Sin 3: Node.js managed two different ways simultaneously

- Windows: Node v22.16.0 installed directly in `C:\Program Files\nodejs\` — no version manager

- WSL: nvm with 4 versions (v20.20.0, v24.12.0, v24.13.1, v24.14.1) but no active node (`node` command fails in WSL)

  

The WSL nvm default is `lts/*` but the actual `node` binary is not in PATH when shells start because nvm lazy-loads. This means running `node` in WSL sometimes fails depending on how the shell was opened. **You have 4 Node versions in WSL and none are reliably available.**

  

### Sin 4: npm caches on C:

Windows npm cache: `AppData\Local\npm-cache` — 3.33 GB on C:.  

WSL npm cache: `~/.npm` — 6 GB inside the VHDX.  

Neither was redirected to D: from the start.

  

### Sin 5: Apps default-installed to AppData on C:

VS Code, Cursor, Kiro, Claude Desktop, Jan, Ollama, Bitwarden, Obsidian — all electron apps, all installed to `AppData\Local\Programs` (12.4 GB) on C:. Chrome at 9.39 GB. These installers give you no choice about location, but the data directories (caches, profiles) can be redirected — and were not.

  

### Sin 6: No per-project isolation discipline

Projects `hivemind` and `tradingview` have `pyproject.toml` but no `uv` or any consistent tool. Projects that need Python just... wing it. When you need to add a RAG pipeline or langchain to a project, you either pollute system Python or give up. This is why miniconda felt confusing — you had no workflow to attach it to.

  

### Sin 7: hiberfil.sys was never disabled — 12.7 GB wasted

A machine that never hibernates had a 12.7 GB hibernation file sitting on C: for months. One command removes it permanently. Nobody thought to check.

  

### Sin 8: Three browsers accumulating data on C:

Chrome (9.39 GB), Vivaldi (1.51 GB), Brave (0.67 GB) — all on C:. A person needs one primary browser, maybe two. Cache from three browsers is just waste.

  

### Sin 9: Git identity not cleanly separated

Windows git: `anant.gupta@in.nspglobaltech.com` (work/NSP email)  

WSL git: `gupt0479@umn.edu` (UMN email)  

Personal GitHub work crosses both. No `.gitconfig` conditional includes configured. No GPG signing. Credentials managed by different helpers per environment.

  

### Sin 10: WSL projects not backed up

The actual code lives in `/home/anant_gupta/projects/` inside the VHDX. The VHDX is on D: but **is not part of the backed-up D:\Users\_Anant\ folder**. WSL projects: `umn` (19 GB), `ai` (7.9 GB), `hub` (5 GB), `hackathon` (3.1 GB) — all unprotected from drive failure except what happens to be pushed to GitHub.

  

### Sin 11: miniconda on C: with no clear home

4.9 GB of conda base + packages on C:. Not in PATH by default. Never used for real projects. The pkgs cache alone is 2.9 GB of downloaded-but-cached installers.

  

### Sin 12: Multiple editor remote servers accumulating in WSL

VS Code Server (3.4 GB), Cursor Server (1.1 GB), VS Code Remote Containers (1.1 GB) inside the VHDX. Each time an editor updates, a new version download happens. Old versions stay. Nobody cleans them.

  

---

  

## PART 1 — WHAT TO COPY FROM THIS LAPTOP

  

Do this copying BEFORE wiping or selling. Be surgical. The goal is to copy data, not bloat.

  

### Copy: YES

  

| Source | Destination on new laptop | Notes |

|--------|--------------------------|-------|

| `D:\Users\_Anant\` (all of it) | `D:\Users\_Anant\` | PARA system, Jarvis vault, The Plan vault, documents, finances |

| `D:\AI\ollama-models\` | `D:\AI\ollama-models\` | Only if re-downloading is slow. Cloud models (kimi-k2.5, qwen3-coder-next) can be re-pulled |

| `D:\projects\` | `D:\projects\` | Assisto_website, boom, portfolio — small, check if these are on GitHub first |

| WSL `~/.ssh/id_ed25519` + `.pub` | New WSL `~/.ssh/` | Your GitHub SSH key. Do NOT regenerate — this key is already trusted on GitHub |

| WSL `~/.gitconfig` | New WSL `~/.gitconfig` | git config, LFS, gh auth |

| Windows `%USERPROFILE%\.gitconfig` | New Windows `~\.gitconfig` | Windows git identity |

| `%USERPROFILE%\.mcp.json` | New `~\.mcp.json` | MCP server declarations |

| `%USERPROFILE%\.claude\settings.json` | New `~\.claude\settings.json` | Model, permissions |

| `%USERPROFILE%\.claude\.credentials.json` | New `~\.claude\.credentials.json` | Auth token (or re-login) |

| Windows user env vars (list in Part 3) | Set manually on new machine | OLLAMA_MODELS, OBSIDIAN_*, OLLAMA_* |

| WSL `~/.bashrc` and `~/.profile` | Review and copy relevant sections | nvm init, ssh-agent, custom aliases only |

  

### Copy: NO (do not migrate, reinstall fresh)

  

| What | Why not |

|------|---------|

| WSL VHDX (the whole 74 GB) | Start WSL fresh on D:. Push code to GitHub, clone fresh. Old VHDX has accumulated garbage. |

| `node_modules/` anywhere | Always regenerated with `npm install` |

| `.venv/` directories | Always regenerated with `uv sync` or `python -m venv` |

| AppData (any of it) | All caches. Regenerate. |

| miniconda3 | Reinstall properly on D: from scratch |

| Windows npm global packages | Reinstall: `npm install -g @openai/codex openclaw` — that's 2 packages |

| Conda envs | `csci4041` is a dead UMN course env. Don't carry it forward. |

  

### Before you wipe: push everything to GitHub

  

```bash

# Inside current WSL, for each project not yet pushed:

cd ~/projects/ai && git status   # check if anything uncommitted

cd ~/projects/hub/hivemind && git push

cd ~/projects/hub/tradingview && git push

# etc.

```

  

Any project not on GitHub when you close this laptop is lost.

  

---

  

## PART 2 — DISK STRATEGY ON THE NEW LAPTOP

  

### How many partitions?

  

**Answer: Two. C: and D:. Do not create a third.**

  

A third partition for WSL sounds logical but creates a worse problem: VHDX files grow dynamically, so you'd have to pre-allocate a fixed amount ("I'll give WSL 200 GB") which either wastes space (if WSL uses 80 GB) or runs out (if WSL hits 200 GB and Windows gives you no warning). With D: as one large partition, WSL grows freely alongside everything else.

  

**Recommended split for a typical 1 TB NVMe:**

  

| Partition | Size | Contains |

|-----------|------|---------|

| C: | 150 GB | Windows OS, system files, installed apps (no choice), pagefile |

| D: | ~850 GB | WSL VHDX, Docker VHDX, personal files, conda, npm cache, Ollama models, dev data, Chrome profile, everything growable |

  

If the new laptop has a 512 GB SSD:

  

| Partition | Size | Contains |

|-----------|------|---------|

| C: | 120 GB | Windows + apps |

| D: | ~380 GB | Everything else |

  

**How to partition during Windows setup:**

When the Windows installer asks "Where do you want to install Windows?", click "New", create a 150 GB (153,600 MB) partition for C:, let it create the system reserved partitions automatically, then let the rest become D:.

  

### What goes on which drive — the rules

  

```

C: (Windows system drive)

├── Windows/                    — no choice

├── Program Files/              — system-wide installers go here (Git, Docker)

├── Program Files (x86)/        — legacy installers

├── Users\Anant\

│   ├── AppData\Local\Programs\ — Electron apps land here (no choice for most)

│   └── AppData\...             — app caches (redirect where possible)

└── pagefile.sys                — Windows virtual memory (can move to D: but not worth it)

  

D: (everything else)

├── WSL\

│   ├── Ubuntu\ext4.vhdx        — WSL Ubuntu disk image

│   └── Docker\                 — Docker Desktop disk image

├── AI\

│   └── ollama-models\          — Ollama model weights

├── conda\                      — miniconda/miniforge installation

│   ├── base\                   — conda base environment

│   └── pkgs\                   — conda package cache

├── npm-cache\                  — Windows npm cache (redirected via npm config)

├── Chrome\                     — Chrome profile (via junction)

├── Users\_Anant\               — Your PARA system, vaults, personal files

│   ├── 00_Inbox\

│   ├── 10_Areas\

│   │   └── Documents\

│   │       ├── Jarvis\         — Obsidian Jarvis vault

│   │       └── The Plan\       — Obsidian The Plan vault

│   ├── 20_Progress\

│   ├── 30_Resources\

│   └── 99_Archive\

└── projects\                   — Windows-side projects (optional, WSL projects live in WSL)

```

  

**Why D:\Users\_Anant is the right pattern you already have:**  

This is your one source of truth for personal data. It is already backed up. Keep it exactly as-is. Obsidian vaults live here. Documents live here. This folder is what you back up, and it's already clean.

  

---

  

## PART 3 — DAY 1 WINDOWS SETUP (DO THESE BEFORE ANYTHING ELSE)

  

The order matters. Many of these are "first day only" decisions.

  

### Step 1: Partition during Windows install (see Part 2)

  

### Step 2: First boot — disable hibernation immediately

```powershell

# Run in admin PowerShell

powercfg /hibernate off

```

This removes `hiberfil.sys` before it's ever created at full size. On 32 GB RAM, this saves 25+ GB.

  

### Step 3: Move pagefile to D: (optional, but clean)

Control Panel → System → Advanced → Performance Settings → Advanced → Virtual Memory → Change.  

Uncheck "Automatically manage". Set C: to "No paging file". Set D: to "System managed size". Reboot.

  

### Step 4: Set user environment variables immediately

Set these before installing anything, so tools that read them on install pick up the right paths.

  

```powershell

# Run each in admin PowerShell

[System.Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "D:\AI\ollama-models", "User")

[System.Environment]::SetEnvironmentVariable("OLLAMA_CONTEXT_LENGTH", "32768", "User")

[System.Environment]::SetEnvironmentVariable("OLLAMA_ORIGINS", "app://obsidian.md*", "User")

[System.Environment]::SetEnvironmentVariable("OBSIDIAN_JARVIS_API_URL", "http://127.0.0.1:27123/", "User")

[System.Environment]::SetEnvironmentVariable("OBSIDIAN_PLAN_API_URL", "http://127.0.0.1:27124/", "User")

# OBSIDIAN API KEYS — set after Obsidian is installed and Local REST API plugin generates new keys

```

  

### Step 5: Redirect npm cache to D: before installing Node

```powershell

# After installing Node (see below), immediately run:

npm config set cache "D:\npm-cache"

```

  

### Step 6: Install Git first, configure identity

Download from git-scm.com. Install to `C:\Program Files\Git` (default).

  

```powershell

# After install — use YOUR personal email here, not NSP work email

git config --global user.name "Anant Gupta"

git config --global user.email "anantmahi721@gmail.com"

git config --global core.autocrlf false          # prevents CRLF disasters in WSL-shared repos

git config --global init.defaultBranch main

git config --global pull.rebase true

```

  

Note on the two-email problem: If you do work for an employer on this machine, use `.gitconfig` conditional includes:

```gitconfig

# In ~/.gitconfig

[includeIf "gitdir:D:/work/"]

    path = ~/.gitconfig-work

# ~/.gitconfig-work contains the work email

```

  

### Step 7: Install Windows apps — the ordered list

  

Install in this order. Choice of which drive to install on is noted.

  

| App | Where to install | Notes |

|-----|-----------------|-------|

| Google Chrome | Default (C: AppData) | Move profile to D: via junction after install |

| Node.js LTS | `C:\Program Files\nodejs\` | System-wide, fine on C: |

| VS Code | Default (AppData\Local\Programs) | No choice, but extensions on D: via env var |

| Git | `C:\Program Files\Git` | System-wide |

| Docker Desktop | Default + redirect VHDX to D: | Critical: see WSL section |

| Obsidian | Default | Vaults are on D:, app itself is small |

| Ollama | Default | Models go to D:\AI\ollama-models (env var already set) |

| Bitwarden | Default | Password manager, small |

| Claude Desktop | Default | Config on D: can be configured after |

| Cursor | Default | Small app |

  

**Apps you should reconsider bringing over:**

- Jan AI (3.1 GB) — you have Claude. Do you actually use Jan?

- WisprFlow — only bring if you use it daily

- IntelliJ — only bring if actively using Java/Kotlin

- Medal — only bring if still gaming

- Cluely — only bring if actively using

  

### Step 8: Chrome profile → D: junction

```powershell

# Close Chrome completely, then:

$src = "$env:LOCALAPPDATA\Google\Chrome\User Data"

$dst = "D:\Chrome\User Data"

New-Item -ItemType Directory -Path "D:\Chrome" -Force

Move-Item $src $dst

cmd /c mklink /J "$src" "$dst"

# Chrome never knows the difference. All future Chrome growth goes to D:.

```

  

---

  

## PART 4 — DAY 1 WSL SETUP (CRITICAL — DO THIS BEFORE USING WSL)

  

This is the most important section. The entire WSL mistake on the old laptop came from not doing step 1.

  

### Step 1: Install WSL pointing to D: from the very first command

  

Do NOT run `wsl --install` bare — it will create the VHDX on C:. Instead:

  

```powershell

# Step 1: Create the target directory

New-Item -ItemType Directory -Path "D:\WSL\Ubuntu" -Force

  

# Step 2: Install WSL engine without a distro

wsl --install --no-distribution

  

# Step 3: Download Ubuntu from the Store OR install via import

# Option A (store): Install Ubuntu from Microsoft Store, but immediately after:

#   - DO NOT LAUNCH IT yet

#   - Move the VHDX before first launch (complex, see Option B)

  

# Option B (clean, recommended): Import Ubuntu manually

# Download Ubuntu .tar from: https://cloud-images.ubuntu.com/wsl/

# Then:

wsl --import Ubuntu "D:\WSL\Ubuntu" "C:\path\to\ubuntu.tar" --version 2

  

# Set default user (add to /etc/wsl.conf after first launch)

```

  

After Ubuntu starts for the first time:

```bash

# Immediately create /etc/wsl.conf

sudo tee /etc/wsl.conf << 'EOF'

[boot]

systemd=true

  

[user]

default=anant_gupta

  

[wsl2]

memory=8GB

processors=4

EOF

```

  

The `memory` and `processors` lines cap WSL2 resource use. Without them, WSL2 can take all your RAM during builds.

  

### Step 2: Create the WSL user and configure shell

```bash

# Inside WSL

sudo adduser anant_gupta

sudo usermod -aG sudo anant_gupta

  

# Install essentials

sudo apt update && sudo apt upgrade -y

sudo apt install -y git curl wget build-essential unzip zip gh

  

# Copy SSH key from backup

mkdir -p ~/.ssh

# Paste your old id_ed25519 content here (copied from old laptop)

chmod 700 ~/.ssh && chmod 600 ~/.ssh/id_ed25519

```

  

### Step 3: Install nvm — ONE time, with a pinned version

```bash

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

source ~/.bashrc

nvm install 20        # LTS

nvm install 24        # Latest

nvm alias default 20  # Default to LTS — safest for most projects

```

  

**The critical rule**: Every project that needs a specific Node version gets a `.nvmrc` file:

```bash

echo "20" > ~/projects/myproject/.nvmrc

# Then cd into the project and:

nvm use

```

  

### Step 4: npm cache — keep it inside WSL but keep it clean

Unlike Windows npm cache, WSL npm cache lives inside the VHDX which is already on D:. This is fine — it's not on C:. No redirection needed.

  

What you DO need: tell npm to use a smarter cache strategy:

```bash

npm config set prefer-offline true    # use cache before hitting network

```

  

And add to your `~/.bashrc`:

```bash

# Compact WSL VHDX reminder (add to monthly habit, not automatic)

alias wsl-compact='echo "Run from Windows: wsl --shutdown && diskpart compact"'

```

  

### Step 5: Install uv — the Python tool (replaces pip, venv, pyenv)

```bash

curl -LsSf https://astral.sh/uv/install.sh | sh

source ~/.bashrc

uv --version   # should work

```

  

`uv` is what you install INSTEAD of dealing with conda for Python work. See Part 5.

  

### Step 6: Git config in WSL

```bash

git config --global user.name "Anant Gupta"

git config --global user.email "anantmahi721@gmail.com"   # or whichever is primary

git config --global core.autocrlf false

git config --global init.defaultBranch main

git config --global pull.rebase true

git config --global credential.helper store

  

# gh auth (GitHub CLI)

gh auth login   # follow prompts, authenticate via browser

```

  

### Step 7: Directory structure inside WSL

```bash

mkdir -p ~/projects/{ai,hub,hackathon,scratch}

mkdir -p ~/tools

```

  

**Rule: WSL home directory structure mirrors the work you do:**

- `~/projects/ai/` — AI/agentic projects

- `~/projects/hub/` — portfolio, products

- `~/projects/hackathon/` — time-boxed hack work

- `~/projects/scratch/` — experiments, throwaway code. This is new — have an explicit place for throwaway code so it doesn't end up in hub.

  

Clone projects fresh from GitHub. Do NOT copy node_modules or .venv.

  

### Step 8: Docker Desktop — redirect VHDX to D: on first install

In Docker Desktop settings → Resources → Advanced → Disk image location: set to `D:\WSL\Docker`.

  

If Docker Desktop was already installed before you set this: Settings → Resources → WSL Integration → Disk image location.

  

---

  

## PART 5 — PYTHON ENVIRONMENTS: WHAT WENT WRONG AND HOW TO DO IT RIGHT

  

This is the section for understanding what "sandboxes" actually are, why miniconda felt confusing, and what the professional workflow looks like.

  

### What is a virtual environment (sandbox)?

  

When Python is installed on your machine, it lives in one place (e.g., `/usr/bin/python3`). When you run `pip install requests`, it installs `requests` into that one Python's package folder. If another project needs a different version of `requests`, they fight over the same folder.

  

A **virtual environment** is a copy of Python's executable + an isolated folder for packages, created PER PROJECT:

  

```

your-project/

├── .venv/              ← isolated environment

│   ├── bin/python      ← this project's python

│   ├── bin/pip         ← this project's pip

│   └── lib/            ← this project's packages (langchain, pydantic, etc.)

├── src/

├── requirements.txt    ← or pyproject.toml

└── .python-version     ← optional: pins the Python version

```

  

When you "activate" it (`source .venv/bin/activate`), your shell uses THAT python, not the system one. Other projects are unaffected.

  

### What is conda / miniconda?

  

conda is a tool that does two things:

1. Manages Python virtual environments (like venv, but heavier)

2. Also installs non-Python packages (C libraries, CUDA drivers, etc.)

  

**You need conda ONLY if your work requires CUDA (GPU training), scientific C libraries (BLAS, LAPACK), or cross-language package management.** For pure Python AI/ML work using pip-installable packages (langchain, openai, anthropic, fastapi, pydantic), conda adds overhead without benefit.

  

**The mistake on this laptop:** miniconda was installed because tutorials for RAG/agentic work use conda in their setup guides. But the underlying work (installing Python packages) doesn't require conda. The conda-install step was cargo-culted without understanding why.

  

### The modern professional workflow: `uv`

  

`uv` (from Astral, the company that makes Ruff) is the tool that replaces pip, venv, pyenv, and to a large extent conda. It is:

- 10-100x faster than pip

- Creates isolated environments automatically per project

- Manages Python versions (like pyenv)

- Lockfiles for reproducibility

  

**Every Python project you start, the workflow is:**

  

```bash

# Starting a new project:

mkdir my-rag-agent && cd my-rag-agent

uv init                              # creates pyproject.toml + .venv

uv add langchain openai pydantic     # installs + records in pyproject.toml

  

# Working on an existing project:

cd my-rag-agent

uv sync                              # installs exactly what pyproject.toml says

  

# Running code:

uv run python src/main.py           # runs in the project's environment

# OR: source .venv/bin/activate && python src/main.py

  

# Jupyter Lab (see below)

uv add --dev jupyterlab             # adds Jupyter to THIS project's env

uv run jupyter lab                  # runs Jupyter with THIS project's packages visible

```

  

### Jupyter Lab: the right way

  

The mistake people make: `pip install jupyterlab` globally. Then Jupyter can't see project-specific packages.

  

The right way: Jupyter Lab is installed **per project** or **per environment**. When you run `jupyter lab` from inside a project's environment, it sees all that project's packages automatically.

  

```bash

# For a new AI project:

cd ~/projects/ai/my-rag-pipeline

uv init

uv add langchain openai anthropic chromadb

uv add --dev jupyterlab

uv run jupyter lab     # open browser, start notebook, all packages available

```

  

This is what every "set up RAG environment" tutorial is trying to get you to do with conda. They use conda because it was the standard 3 years ago. `uv` is the 2025 way.

  

### When to use conda (rare, specific cases)

  

Use conda (specifically miniforge, not miniconda) ONLY when:

- You need CUDA (GPU training with PyTorch/TensorFlow and specific CUDA versions)

- A package requires conda-forge because it's not on PyPI (rare)

- You're working with bioinformatics tools that are conda-only

  

Install miniforge (not miniconda) to `D:\conda\` so it's on D:.

  

### Python on Windows vs WSL

  

**Rule: Do Python work in WSL, not Windows.**

  

Windows Python (`C:\Python313`) is for:

- Running Claude Code (it uses it internally)

- Quick scripts that interact with Windows system things

- That's about it

  

All real Python dev work (RAG agents, FastAPI, data work, notebooks) happens in WSL under `uv`. Do NOT install every Python package on Windows.

  

---

  

## PART 6 — NODE.JS STRATEGY

  

### In WSL

- Use nvm (already in setup)

- Two versions: LTS (v20) as default + latest (v24) for when you need it

- Every project gets a `.nvmrc` file

- When you `cd` into a project, run `nvm use` (or add auto-nvm to bashrc)

  

```bash

# Auto-use .nvmrc when cd-ing into a directory — add to ~/.bashrc:

autoload -U add-zsh-hook

cdnvm() {

    command cd "$@" || return $?

    if [[ -f ".nvmrc" && -r ".nvmrc" ]]; then

        nvm use

    fi

}

# Bash version:

cd() { builtin cd "$@" && if [ -f ".nvmrc" ]; then nvm use; fi; }

```

  

### On Windows

- Do NOT install Node directly from nodejs.org

- Use `nvm-windows` (github.com/coreybutler/nvm-windows)

- Same discipline: 1-2 versions max

  

```powershell

# After installing nvm-windows:

nvm install lts

nvm use lts

npm config set cache "D:\npm-cache"

```

  

### npm global packages

Keep Windows global npm installs to the absolute minimum:

- `@anthropic-ai/claude-code` — Claude Code CLI

- `@openai/codex` — if actively using

Nothing else. Everything else installs per-project.

  

---

  

## PART 7 — CLAUDE CODE + MCP SETUP

  

### Claude Code CLI

```powershell

npm install -g @anthropic-ai/claude-code

claude --version

# Login:

claude auth login

```

  

### settings.json — copy from old laptop

The minimal settings from old laptop:

```json

{

  "model": "claude-sonnet-4-6",

  "effortLevel": "high",

  "autoUpdatesEnabled": true,

  "autoUpdatesChannel": "latest"

}

```

  

### MCP servers — ~/.mcp.json

Copy your existing `.mcp.json` exactly. The Obsidian API keys will be different on the new machine (regenerate in Obsidian Local REST API settings and update the env vars + mcp.json).

  

```json

{

  "mcpServers": {

    "jarvis": {

      "type": "http",

      "url": "http://127.0.0.1:27123/mcp/",

      "headers": { "Authorization": "Bearer <NEW_KEY_FROM_OBSIDIAN>" }

    },

    "the-plan": {

      "type": "http",

      "url": "http://127.0.0.1:27124/mcp/",

      "headers": { "Authorization": "Bearer <NEW_KEY_FROM_OBSIDIAN>" }

    },

    "jarvis-fs": {

      "command": "cmd",

      "args": ["/c","npx","-y","@modelcontextprotocol/server-filesystem","D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis"]

    },

    "the-plan-fs": {

      "command": "cmd",

      "args": ["/c","npx","-y","@modelcontextprotocol/server-filesystem","D:\\Users\\_Anant\\10_Areas\\Documents\\The Plan"]

    }

  }

}

```

  

### Claude Desktop — UWP config

After installing Claude Desktop from the Store, update its config immediately to use `type: "http"` (not `mcp-remote`). Location: `AppData\Local\Packages\Claude_<hash>\LocalCache\Roaming\Claude\claude_desktop_config.json`

  

---

  

## PART 8 — BACKUP STRATEGY (THE GAP)

  

The current backup: only `D:\Users\_Anant\` → Google Drive.  

What is NOT backed up: **WSL projects** (35 GB of actual code lives inside the VHDX).

  

### Fix: GitHub is your primary code backup

  

Every project you're working on must be pushed to GitHub before the laptop is closed for the night. Not weekly — nightly or per session.

  

```bash

# Make this a habit in WSL:

alias gitpush='git add -A && git commit -m "wip: end of session" && git push'

```

  

Private repos are free on GitHub. Use them.

  

### Fix: Export what GitHub doesn't cover

  

```bash

# WSL configs and dotfiles — add to a dotfiles repo:

# - ~/.bashrc

# - ~/.gitconfig

# - ~/.ssh/config (not the private key itself)

# - ~/.nvm/alias/default (your default node version)

# Any custom scripts in ~/tools/

```

  

### Fix: Windows configs backed up to D:

  

```powershell

# Create a configs folder backed up via Google Drive

New-Item -ItemType Directory "D:\Users\_Anant\10_Areas\DevConfig" -Force

  

# Copy important configs there periodically:

Copy-Item "$env:USERPROFILE\.claude\settings.json" "D:\Users\_Anant\10_Areas\DevConfig\"

Copy-Item "$env:USERPROFILE\.mcp.json" "D:\Users\_Anant\10_Areas\DevConfig\"

Copy-Item "$env:USERPROFILE\.gitconfig" "D:\Users\_Anant\10_Areas\DevConfig\"

```

  

---

  

## PART 9 — ONGOING MAINTENANCE (WHAT PROFESSIONAL DEVELOPERS ACTUALLY DO)

  

Set a monthly reminder to do this:

  

```powershell

# === MONTHLY WINDOWS CLEANUP ===

  

# 1. Compact WSL VHDX (only if WSL has grown significantly)

wsl --shutdown

# Then admin diskpart: select vdisk, attach readonly, compact, detach

  

# 2. Clean Windows temp

Get-ChildItem "$env:TEMP\vscode-stable-user-x64-*" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force

Get-ChildItem $env:TEMP -Force -ErrorAction SilentlyContinue |

  Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } |

  Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

  

# 3. Clean Windows npm cache

npm cache clean --force

```

  

```bash

# === MONTHLY WSL CLEANUP ===

  

# Clean npm cache (keeps one copy of each package version)

npm cache clean --force

  

# Clean uv cache

uv cache clean

  

# Clean pnpm if you use it

pnpm store prune 2>/dev/null

  

# Clean old VS Code Server versions

ls ~/.vscode-server/bin/

# Delete all but the newest hash directory

  

# After cleaning, run from Windows to shrink VHDX:

# wsl --shutdown && diskpart compact

```

  

---

  

## PART 10 — THE MENTAL MODEL: HOW A PROFESSIONAL NAVIGATES HIS LAPTOP

  

A developer who "knows where every file lives" operates by these rules:

  

### Rule 1: Every tool has exactly one install

Not three Pythons. Not two Node installs. One Python per environment context (uv manages them), one Node per WSL (nvm manages versions). When you install a tool, you know where it is because you chose where to install it.

  

### Rule 2: The file system has three tiers

- **System (C:, read-only in spirit):** Windows, installed apps, system tools. You rarely go here. If a file here is deleted, you reinstall.

- **Work (D: / WSL ~/projects/):** The actual thing you're building. Never mixes with system. Backed up via git.

- **Personal (D:\Users\_Anant\):** Documents, notes, vaults, finance. Backed up via Google Drive.

  

### Rule 3: Caches live in the tier they belong to

npm cache → D:\npm-cache (Windows) or inside WSL (already on D:).  

Ollama models → D:\AI\ollama-models.  

Chrome profile → D:\Chrome (via junction).  

None of these live on C:.

  

### Rule 4: One environment per project

You never install a package "globally" in Python unless it's a CLI tool (like `uv` itself, `ruff`, `claude`). Every `pip install` happens inside a `.venv`. You always know what a project needs because it's in `pyproject.toml`.

  

### Rule 5: Git is always up to date

You commit and push before closing a project. Not because you were told to — because losing work once trains you to never let it happen again. The VHDX is not a backup.

  

### Rule 6: Before running anything new, understand what it does to the filesystem

Before `npm install -g X`: where does it install? Is there a per-project alternative?  

Before installing a new app: does it put data on C:? Can I redirect it?  

Before `pip install X`: am I inside a virtual environment?  

These questions become instinct within a month of practicing them.

  

---

  

## PART 11 — COMPLETE SETUP CHECKLIST

  

Use this as a literal checklist on the new laptop.

  

### Day 1 — Foundation

- [ ] Partition: C: ~150 GB, D: rest

- [ ] Disable hibernation: `powercfg /hibernate off`

- [ ] Set OLLAMA_MODELS, OLLAMA_CONTEXT_LENGTH, OLLAMA_ORIGINS env vars

- [ ] Install Git, configure identity (personal email)

- [ ] Install Node LTS via nvm-windows (NOT direct install), redirect npm cache to D:

- [ ] Install Chrome, immediately move profile to D: via junction

- [ ] Install WSL pointing to D:\WSL\Ubuntu (NOT via bare `wsl --install`)

- [ ] Copy D:\Users\_Anant from old laptop

  

### Day 1 — WSL

- [ ] Create /etc/wsl.conf (systemd=true, default user, memory limit)

- [ ] Install nvm, set default to LTS

- [ ] Install uv

- [ ] Install gh (GitHub CLI), run `gh auth login`

- [ ] Copy SSH key from old laptop, set permissions

- [ ] Configure git (name, email, credential helper)

- [ ] Create project directory structure: ~/projects/{ai,hub,hackathon,scratch}

- [ ] Clone active projects from GitHub

  

### Day 2 — Apps

- [ ] Install VS Code, Cursor (both write to AppData — acceptable)

- [ ] Install Obsidian, open both vaults from D:\Users\_Anant\10_Areas\Documents\

- [ ] Install Local REST API plugin in Obsidian, generate new API keys

- [ ] Install Claude Desktop (Store), update config to use `type: "http"`

- [ ] Set OBSIDIAN_JARVIS_API_KEY and OBSIDIAN_PLAN_API_KEY env vars (new keys)

- [ ] Install Claude Code CLI: `npm install -g @anthropic-ai/claude-code`

- [ ] Copy ~/.mcp.json, update API keys

- [ ] Copy ~/.claude/settings.json

- [ ] Test: `claude` in a project directory, verify jarvis and the-plan MCPs connect

  

### Day 3 — Python setup

- [ ] Understand: Python work happens in WSL via uv

- [ ] For each project with requirements: `cd ~/projects/X && uv init && uv add <packages>`

- [ ] Test Jupyter: `uv add --dev jupyterlab && uv run jupyter lab`

- [ ] If conda genuinely needed: install miniforge to D:\conda\

  

### Ongoing

- [ ] Set monthly calendar reminder: WSL VHDX compact + temp cleanup

- [ ] Commit and push before closing any project

- [ ] Never `pip install X` outside a virtual environment

  

---

  

## APPENDIX — CURRENT LAPTOP NUMBERS FOR REFERENCE

  

| Item | Current laptop | Target on new laptop |

|------|---------------|---------------------|

| WSL VHDX location | D:\WSL\Ubuntu\ (74 GB) | D:\WSL\Ubuntu\ from day 1 |

| Docker VHDX location | D:\WSL\Docker\ (22 GB) | D:\WSL\Docker\ from day 1 |

| Ollama models | D:\AI\ollama-models\ | D:\AI\ollama-models\ |

| npm cache (Windows) | AppData\Local\npm-cache (3.3 GB) | D:\npm-cache |

| Chrome profile | AppData\Local\Google\Chrome (9.4 GB) | D:\Chrome via junction |

| conda | C:\Users\Anant Gupta\miniconda3 (4.9 GB) | D:\conda or replaced by uv |

| hiberfil.sys | Gone (disabled June 2026) | Disabled on day 1 |

| Python installs | 3 (C:\Python313, miniconda, WSL system) | 1 per context |

| Node versions (WSL) | 4 (v20, v24.12, v24.13, v24.14) | 2 max (v20 LTS + v24 latest) |

| Backed up | D:\Users\_Anant only | Same + all code on GitHub |
# WSL
## The Definitive WSL2 Professional Development Setup Guide

**Audience:** A developer who has been winging WSL2 and wants to understand the machine well enough to maintain it for the next 5 years.
**Target machine:** Windows 11 + WSL2 Ubuntu 24.04, 1TB NVMe, 32GB RAM.
**Stack:** Next.js / TypeScript / Tailwind / Supabase / Vercel, plus Python AI/agentic work (LangChain, Anthropic API, RAG). Docker coming next. Primary IDE: VS Code Remote-WSL. Primary AI interface: Claude Code CLI.

**Last updated:** 2026-06-08. Findings in Parts 10 and 13 were validated by running the cleanup on the current machine, so the caveats below (root-owned trees, npm `_npx`) are real, not theoretical.

This is a reference document, not a quick-start. Read Part 0 first; it is the model everything else depends on.

### Contents

- **Part 0** — The WSL2 mental model (read this first)
- **Part 1** — Home directory anatomy (dot-dir reference table)
- **Part 2** — Disk strategy (partitions + VHDX placement)
- **Part 3** — Clean WSL installation (ordered, with full `.bashrc`)
- **Part 4** — Project directory taxonomy
- **Part 5** — Node.js isolation (fnm + pnpm)
- **Part 6** — Python isolation (uv)
- **Part 7** — Docker in WSL2
- **Part 8** — VS Code Remote-WSL
- **Part 9** — Git identity and credentials
- **Part 10** — Cache management and VHDX growth control
- **Part 11** — Backup strategy
- **Part 12** — Migration checklist (old WSL → new WSL)
- **Part 13** — Current-machine cleanup (already executed once; see status note)

---

## PART 0 — THE WSL2 MENTAL MODEL

You cannot maintain WSL2 if you think of it as "Linux running in a window." It is a real virtual machine with a real virtual disk. Internalize these six facts and 90% of the storage and "wrong version" mysteries disappear.

### 1. The VHDX is a full virtual disk, not a folder

Your entire Linux filesystem — every file under `/`, including `/home/anant_gupta` — lives inside a single Windows file called `ext4.vhdx`. It is a virtual hard drive formatted as ext4. Windows sees one opaque file; Linux sees a whole disk.

**Why this matters:** You cannot browse, back up, or sync individual Linux files from Windows tools by reaching into a folder — there is no folder, only the disk image. Google Drive, OneDrive, and File History back up *files*; they see `ext4.vhdx` as one giant binary blob and either skip it or re-upload all 60GB every time a single byte changes. Your code inside WSL is invisible to Windows-side backup. (This is why Part 11 exists.)

### 2. Deleting files does NOT shrink the VHDX

The VHDX grows automatically as the guest writes data, but it **never shrinks on its own**. When you `rm -rf` a 19GB `target/` directory, ext4 marks those blocks free *inside the disk image*, but the `.vhdx` file on Windows stays exactly as large as its high-water mark. The space is free to Linux and still consumed on Windows.

**Why this matters:** This is the single biggest cause of "my C: drive filled up and I don't know why." Reclaiming space is a deliberate two-step act: free the blocks inside Linux (`fstrim`), then compact the image from Windows (`Optimize-VHD`/`diskpart`), or enable `sparseVhd` so it self-compacts. See Part 2 and Part 10.

### 3. Cross-filesystem access (`/mnt/c`, `/mnt/d`) is slow

WSL2 reaches Windows drives through a 9P network protocol bridge (DrvFs). Operations that touch thousands of small files — `npm install`, `git status`, `cargo build`, `uv sync` — are **5x to 20x slower** on `/mnt/c` or `/mnt/d` than on the native ext4 disk. The Linux VM and Windows talk over a virtual network, not a shared kernel.

**Why this matters:** Source code you actively build must live on the Linux side (`~/projects/...`), never under `/mnt/`. Use `/mnt/d` only for *reading* large static assets that already live on Windows (your Obsidian vault, model weights). Never `git clone` a working repo into `/mnt/c`; the editor and toolchain will feel broken and you will blame the wrong thing.

### 4. The three-world model

There are three distinct execution/storage worlds. Every tool belongs to exactly one. Confusion about which world a tool runs in is the root of most setup pain.

| World | Where it runs | Where its files live | What belongs here |
| --- | --- | --- | --- |
| Windows programs | Windows kernel | `C:\` / `D:\` (NTFS) | VS Code (the UI), Docker Desktop, browsers, Obsidian, Ollama |
| WSL Linux programs | WSL2 VM (Linux kernel) | `ext4.vhdx` (native, fast) | node, pnpm, uv, python, git, cargo, claude, codex, your project builds |
| Windows files seen from WSL | Linux process reading over DrvFs | `C:\`/`D:\`, surfaced at `/mnt/` | reading the Obsidian vault, copying an SSH key once |

Rule: **build and run your code in World 2.** Read occasional Windows data via World 3. Keep World 1 to GUI apps and the Docker engine host.

### 5. VS Code Remote-WSL bridges Worlds 1 and 2 deliberately

VS Code is a Windows program (World 1). When you run `code .` from a WSL shell, it installs a small **VS Code Server** inside Linux (World 2) at `~/.vscode-server`. The UI renders on Windows; the language servers, extensions, terminal, debugger, and file operations execute inside Linux against the native filesystem.

**Why this matters:** You get a Windows-quality UI with Linux-native performance and zero `/mnt/` penalty — but only if you open the folder *in WSL* (the green/blue corner indicator shows `WSL: Ubuntu`). Opening the same folder via `\\wsl.localhost\...` in a plain Windows VS Code window puts you back on the slow DrvFs path. The server is what grows `~/.vscode-server` (Part 8).

### 6. `appendWindowsPath=true` causes "wrong node / wrong python" bugs

By default WSL appends the entire Windows `PATH` to your Linux `PATH`. That means Windows executables — `node.exe`, `python.exe`, `npm.cmd` — become callable inside WSL. Depending on PATH order, typing `node` in Linux can silently invoke the Windows binary, which has a different version, different global packages, and CRLF quirks.

**Why this matters:** This produces irreproducible "it works in one shell but not another" failures. The fix (Part 3) is `appendWindowsPath=false`: keep Linux tools Linux-only, and call the rare Windows program by its explicit `.exe` name when you actually want it (`explorer.exe .`, `clip.exe`).

---

## PART 1 — HOME DIRECTORY ANATOMY (REFERENCE TAXONOMY)

A WSL home directory accumulates 30+ dot-directories with no taxonomy. Here is what each one is, who creates it, and whether it is safe to delete. "Safe to delete if tool uninstalled?" assumes the tool is gone or you accept re-download/re-login.

### The XDG Base Directory spec (the rule underneath the chaos)

Modern Linux tools are *supposed* to follow the XDG Base Directory Specification, which separates four kinds of user data into four roots. Tools that predate or ignore XDG dump a `~/.toolname` directory in your home instead. Knowing the four buckets tells you what is safe to delete.

| Env var | Default path | Holds | Safe to delete? |
| --- | --- | --- | --- |
| `$XDG_CONFIG_HOME` | `~/.config` | Configuration you'd want to keep/version | No — back up |
| `$XDG_DATA_HOME` | `~/.local/share` | User-installed data that should persist (binaries' data, pnpm store, uv pythons) | Mostly no |
| `$XDG_STATE_HOME` | `~/.local/state` | Logs, history, recoverable state | Yes (loses history) |
| `$XDG_CACHE_HOME` | `~/.cache` | Re-downloadable/regenerable cache | **Always yes** |

`~/.local/bin` is the XDG home for user executables and should be on `$PATH`. Anything under `~/.cache` is by definition disposable — that single fact resolves most "can I delete this?" questions.

### Dot-directory reference table

| Dir | Created by | What it stores | Safe to delete if tool uninstalled? | Typical size |
| --- | --- | --- | --- | --- |
| `~/.bashrc` | shell | Interactive bash config (aliases, PATH, tool init) | No — this is your setup | <10 KB |
| `~/.profile` | shell | Login-shell env (runs once per login) | No | <10 KB |
| `~/.bash_history` | bash | Command history | Yes (loses history) | <1 MB |
| `~/.bash_aliases` | you | Aliases sourced by `.bashrc` | No | <10 KB |
| `~/.ssh/` | you / ssh | Private+public keys, `config`, `known_hosts` | **NEVER delete** | <1 MB |
| `~/.gnupg/` | gpg | GPG keyrings | No if you sign with GPG (we use SSH instead) | <10 MB |
| `~/.gitconfig` | git | Global git identity + includes | No | <10 KB |
| `~/.config/` | many (XDG) | App configs (gh, supabase, etc.) | Per-tool; mostly no | varies |
| `~/.local/bin/` | pip/uv/installers | User-installed executables | Per-binary | small |
| `~/.local/lib/` | pip `--user` | User-site Python packages (anti-pattern) | Yes after migrating to uv | varies |
| `~/.local/share/` | XDG data | Persistent app data | Mostly no | large |
| `~/.local/share/pnpm/` | pnpm | Content-addressable package store | Regenerable but shared by all projects | **4.4 GB** |
| `~/.local/share/uv/` | uv | uv-managed Pythons + global tools | No (re-download to restore) | 272 MB |
| `~/.local/share/claude/` | Claude | Claude app data | Re-login to restore | 935 MB |
| `~/.local/state/` | XDG state | Logs/history | Yes | small |
| `~/.cache/` | XDG cache | All disposable caches | **Always yes** | 2.9 GB |
| `~/.cache/npm` see `~/.npm` | npm | (npm uses `~/.npm`, not XDG) | yes | — |
| `~/.cache/pnpm/` | pnpm | Download/metadata cache (not the store) | Yes | 1.1 GB |
| `~/.cache/uv/` | uv | Build/wheel cache | Yes (`uv cache clean`) | 654 MB |
| `~/.cache/puppeteer/` | puppeteer | Chromium binaries for e2e | Yes (re-downloads) | 626 MB |
| `~/.cache/ort.pyke.io/` | Rust `ort` crate (ONNX Runtime) | Downloaded ONNX Runtime libs | Yes | 285 MB |
| `~/.cache/pip/` | pip | Wheel cache | Yes | 71 MB |
| `~/.cache/prisma/` | Prisma | Query-engine binaries | Yes (regenerates) | 36 MB |
| `~/.npm/` | npm | `_cacache` (download cache) + `_npx` (npx package cache) | Yes — but `npm cache clean` clears only `_cacache`; delete `~/.npm/_npx` separately | **6.1 GB** (`_cacache` ~4.2 + `_npx` ~2.0) |
| `~/.nvm/` | nvm | Installed Node versions | Yes once migrated to fnm | 2.1 GB |
| `~/.cargo/` | rustup | `bin/`, `registry/` (crate cache), `git/` | `registry`/`git` yes; `bin` per-binary | 619 MB |
| `~/.rustup/` | rustup | Toolchains, std libs, docs | Toolchain components re-installable | 1.3 GB |
| `~/.vscode-server/` | VS Code Remote | Server binaries + WSL-side extensions | Yes — regenerates on next connect | 3.1 GB |
| `~/.cursor-server/` | Cursor Remote | Same, for Cursor | Yes | 1.5 GB |
| `~/.docker/` | Docker CLI | `config.json`, contexts | Config only; tiny | empty here |
| `~/.ollama/` | Ollama | Config (models live on Windows `D:\AI`) | Config only | small |
| `~/.aws/` (symlink) | you | Points to `/mnt/c/.../.aws` | No — it's a symlink, deleting unlinks | link |
| `~/.azure/` (symlink) | you | Points to `/mnt/c/.../.azure` | No — symlink | link |
| `~/.mcp.json` | you | MCP server declarations (Jarvis, The Plan, GitHub) | No | small |
| `~/.claude/`, `~/.codex/` | Claude Code, Codex | CLI config + auth | Re-login to restore | 184 MB+ |
| `~/.cursor/`, `~/.kiro/` | Cursor, Kiro | IDE config | Yes (re-imports VS Code settings) | small |
| `~/.gemini/`, `~/.copilot/` | Gemini, Copilot | Auth/config | Re-login | small |
| `~/.agents/` | AI tooling | Agent definitions | No if you authored them | small |
| `~/.supabase/` | Supabase CLI | CLI state | Re-login | small |
| `~/.pencil/` | Pencil | Design-tool config | Yes if unused | small |
| `~/.yarn/` | yarn | Yarn global/cache (you don't use yarn) | Yes — remove | varies |
| `Library/` | macOS-style tool | Stray "Application Support" dir; does not belong in WSL | **Yes — delete** | small |
| `ecc-setup.sh` | you | A script living in home root | Move to `~/tools/`, don't leave in `$HOME` | tiny |

### Cleaning decision for the CURRENT machine (before migration)

You are not migrating the VHDX (Part 12 explains why a fresh install is correct). But cleaning now reduces the export size and proves what is disposable.

- **Delete outright:** `Library/` (does not belong in Linux), `~/.yarn/` (unused), every `~/.cache/*` subdir, `~/.npm` (6.1 GB).
- **Delete after migrating off the tool:** `~/.nvm` (after fnm is in place), `~/.local/lib` user-site packages (after uv), `boom/target/` (19 GB, Part 13).
- **Keep / back up:** `~/.ssh`, `~/.gitconfig`, `~/.bashrc`, `~/.config` (selectively), `~/.mcp.json`, `~/.agents`.
- **Start fresh, don't migrate:** editor servers (`~/.vscode-server`, `~/.cursor-server`) regenerate on first connect; re-login restores `~/.claude`, `~/.codex`, `~/.supabase`, `~/.gemini`, `~/.copilot`.
- **Re-home the script:** move `ecc-setup.sh` into `~/tools/` (Part 4).

---

## PART 2 — DISK STRATEGY (PARTITIONS + VHDX PLACEMENT)

### Partition the 1TB NVMe into exactly two volumes

| Partition | Size | Contains |
| --- | --- | --- |
| `C:` | 200 GB | Windows, system files, app installers that give no choice (Electron apps land in `AppData`), pagefile |
| `D:` | ~780 GB | WSL `ext4.vhdx`, Docker disk image, Ollama models, Obsidian vault, all growable data |

**Why two, not three:** A dedicated WSL partition forces you to pre-size it. VHDX files grow dynamically; a fixed partition either wastes space or runs out with no warning. One large `D:` lets WSL, Docker, and data grow against a shared pool.

**Why C: gets 200 GB (not 120):** Windows 11 + cumulative updates + unavoidable `AppData\Local\Programs` Electron installs (VS Code, Cursor, Claude, Obsidian) realistically consume 80–120 GB over a few years. 200 GB leaves headroom so C: never becomes the bottleneck; everything that *grows by your activity* is deliberately on D:.

### Install the VHDX on D: from day one

The default `wsl --install` drops `ext4.vhdx` into `C:\Users\<you>\AppData\Local\...`. On the old machine that grew to 74 GB on C: before anyone noticed. **There is no day two for this decision** — do it at install time (Part 3, step 2). Modern WSL (2.4.4+) supports `--location`:

```powershell
wsl --install Ubuntu-24.04 --location "D:\WSL\Ubuntu"
```

### What grows where

| Data | Lives | Why |
| --- | --- | --- |
| Linux home, projects, builds, caches | `D:\WSL\Ubuntu\ext4.vhdx` | Native ext4 = fast; on D: = off the system drive |
| Docker images/volumes | `D:\Docker\...\ext4.vhdx` | Docker disk image redirected on first launch (Part 7) |
| Ollama model weights | `D:\AI\ollama-models\` | Huge, static; set `OLLAMA_MODELS` env var on Windows |
| Obsidian vaults | `D:\Users\_Anant\...` | Personal data, backed up by Google Drive (NTFS, visible) |
| Windows app binaries | `C:\...\AppData\Local\Programs` | No choice; small and replaceable |

### VHDX compaction procedure (reclaim space deleting didn't)

Run when `ext4.vhdx` is much larger than `df -h /` reports as used.

1. Free the blocks inside Linux:

```bash
sudo fstrim -av
```

2. Fully stop WSL from PowerShell (the file must be unlocked):

```powershell
wsl --shutdown
```

3a. Compact — **Windows 11 Pro / Hyper-V enabled**:

```powershell
Optimize-VHD -Path "D:\WSL\Ubuntu\ext4.vhdx" -Mode Full
```

3b. Compact — **Windows 11 Home (no `Optimize-VHD`)**, in an Administrator prompt:

```text
diskpart
select vdisk file="D:\WSL\Ubuntu\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit
```

**Better: make it automatic.** Enable sparse VHDX so the image self-compacts as files are deleted (Part 3 puts this in `.wslconfig`). It trades a small amount of runtime overhead for never having to do the above manually:

```ini
[experimental]
sparseVhd=true
```

### Install rule: Windows vs WSL

- **Install on Windows (World 1):** Docker Desktop, browsers, Obsidian, Ollama, the VS Code *UI*.
- **Install inside WSL (World 2):** node/fnm, pnpm, uv, python, git, cargo, gh, Claude Code, Codex, and every project dependency.
- **Never install twice:** one Node toolchain (WSL), one Python workflow (uv in WSL). The old machine had 3 Pythons and 2 Node installs — that is the disease, not a convenience.

---

## PART 3 — CLEAN WSL INSTALLATION (ORDERED, NO SHORTCUTS)

Every step is numbered because order matters. Do not skip ahead.

### Wrong default to know first: two config files, not one

There are **two** WSL config files and they are constantly confused. Putting a setting in the wrong one makes it silently do nothing — the old machine's `memory` setting in `/etc/wsl.conf` was **inert the entire time**.

| File | Lives on | Controls | Reload |
| --- | --- | --- | --- |
| `%UserProfile%\.wslconfig` | Windows | VM-wide: memory, processors, swap, sparseVhd, networking | `wsl --shutdown` |
| `/etc/wsl.conf` | inside Linux | per-distro: systemd, default user, automount, `appendWindowsPath` | `wsl --shutdown` |

Memory/CPU = `.wslconfig`. systemd/user/PATH = `wsl.conf`. Get this wrong and nothing works.

### Step 1 — Create the target directory on D:

```powershell
New-Item -ItemType Directory -Path "D:\WSL\Ubuntu" -Force
```

### Step 2 — Install WSL with the VHDX on D:

```powershell
wsl --update
wsl --install Ubuntu-24.04 --location "D:\WSL\Ubuntu"
```

If your WSL build rejects `--location` (older than 2.4.4), the fallback is install-then-move:

```powershell
wsl --install Ubuntu-24.04
wsl --shutdown
wsl --manage Ubuntu-24.04 --move "D:\WSL\Ubuntu"
```

**Why:** confirms the disk image is on D: before a single project byte is written. Verify with `wsl --list --verbose` and that `D:\WSL\Ubuntu\ext4.vhdx` exists.

### Step 3 — Create `.wslconfig` on Windows (VM resource caps)

Create `%UserProfile%\.wslconfig` (i.e. `C:\Users\<you>\.wslconfig`) with these exact values for 32 GB RAM:

```ini
[wsl2]
memory=24GB
processors=12
swap=8GB
localhostForwarding=true

[experimental]
autoMemoryReclaim=gradual
sparseVhd=true
```

**Why each line:**
- `memory=24GB` — WSL defaults to 50% of RAM (16 GB) and can balloon during `next build` or `cargo build`, starving Windows. 24 GB gives builds room while leaving 8 GB for Windows + Docker host. Without a cap, a runaway build can freeze the whole machine.
- `processors=12` — leaves cores for Windows responsiveness on a typical 16-thread laptop.
- `swap=8GB` — prevents OOM-kills during large installs/builds; SSD-backed swap is cheap insurance.
- `autoMemoryReclaim=gradual` — WSL returns cached RAM to Windows over time instead of hoarding it.
- `sparseVhd=true` — new VHDX self-compacts as you delete files, so you rarely run the Part 2 compaction ritual.

Apply: `wsl --shutdown`, wait 8 seconds, relaunch. Verify inside WSL: `nproc` shows 12, `free -h` shows ~22–23 GiB.

### Step 4 — First boot: baseline packages

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential curl wget git unzip zip ca-certificates gnupg pkg-config
```

`gh` (GitHub CLI) is installed from its own repo for an up-to-date version:

```bash
(type -p wget >/dev/null || sudo apt install wget -y) \
  && sudo mkdir -p -m 755 /etc/apt/keyrings \
  && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg >/dev/null \
  && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
  && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list >/dev/null \
  && sudo apt update && sudo apt install gh -y
```

### Step 5 — SSH key (copy from old machine, or generate)

**If migrating an existing GitHub key** (preferred — the key is already trusted on GitHub), copy the private+public key content over and restore permissions:

```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh
# paste id_ed25519 and id_ed25519.pub into ~/.ssh/ (use a Windows->WSL copy, then:)
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

**If starting fresh:**

```bash
ssh-keygen -t ed25519 -C "anantmahi721@gmail.com" -f ~/.ssh/id_ed25519
gh auth login   # then: gh ssh-key add ~/.ssh/id_ed25519.pub
```

### Step 6 — Git identity + credentials

```bash
git config --global user.name "Anant Gupta"
git config --global user.email "anantmahi721@gmail.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global core.autocrlf false   # never let Windows rewrite line endings in WSL repos
```

Authenticate GitHub for HTTPS operations and the CLI (full conditional-include + signing setup is Part 9):

```bash
gh auth login          # choose GitHub.com, HTTPS, authenticate via browser
gh auth setup-git      # sets credential.helper to use gh's token
```

**Why `gh auth setup-git`:** for a GitHub-centric developer this makes `gh`'s stored token the credential helper, so HTTPS pushes just work and you avoid the Windows Git Credential Manager interop dance. SSH remotes (your default) need no helper at all.

### Step 7 — Install fnm (Node version manager)

```bash
curl -fsSL https://fnm.vercel.app/install | bash -s -- --skip-shell
```

`--skip-shell` keeps the installer from editing `.bashrc` blindly; we add the init line ourselves in Step 14.

**Why fnm over nvm:** fnm is a Rust binary that initializes in ~5 ms and switches versions in ~4 ms. nvm is a bash script that adds 70–700 ms to *every* shell startup and ~200–450 ms per switch — painful because VS Code, Cursor, and Claude Code spawn many short-lived shells. fnm reads the same `.nvmrc`/`.node-version` files, so it is a drop-in. (Vercel publishes fnm; Turborepo docs treat `.nvmrc` as the contract, which fnm honors.)

### Step 8 — Install two Node versions, set a default

```bash
eval "$(fnm env)"          # activate fnm for this shell (permanent line added in Step 14)
fnm install --lts          # current LTS (e.g. 22)
fnm install 24             # current/latest for bleeding-edge needs
fnm list                   # note the exact LTS version that installed (e.g. v22.x.x)
fnm default 22             # default new shells to the LTS major you just installed
```

If `fnm default 22` errors with "not installed," use the exact version from `fnm list` (e.g. `fnm default v22.12.0`). `lts-latest` is a moving alias and can break across fnm versions — pinning the major is more reliable.

**Why exactly two:** LTS is the safe default for production Next.js/Vercel; one "latest" covers experiments. The old machine had 4 versions and zero `.nvmrc` files — version sprawl with no discipline. Two versions + per-project `.nvmrc` (Part 5) is the discipline.

### Step 9 — Enable pnpm via Corepack; configure the store

```bash
corepack enable
corepack prepare pnpm@latest --activate
pnpm config set store-dir ~/.local/share/pnpm/store --global
```

**Why Corepack:** it ships pnpm with Node and pins the version per project via `packageManager` in `package.json` — no separate global install to drift. The store lives on the native ext4 disk (already on D: via the VHDX), so hard-linking is instant.

**Note on Corepack longevity:** Corepack ships with Node today but is being considered for unbundling in future Node releases. If a future `corepack` command is missing, install pnpm directly with `npm i -g pnpm` and re-run the `store-dir` line — the pnpm discipline in Part 5 is unchanged either way.

### Step 10 — Decision: pnpm for projects, npm for global CLIs only

This resolves the "pnpm + npm both accumulating caches" problem. **Use pnpm for every project; use npm only to install the two global AI CLIs.**

**Why pnpm for projects:** its content-addressable store keeps one copy of each package version on disk and hard-links it into each project's `node_modules`, cutting disk use 50–70% and install time roughly in half versus npm. It is the standard across Vercel/Turborepo/Vite/Nuxt and is fully Vercel-compatible (Vercel auto-detects the `pnpm-lock.yaml`).

**Why npm survives for two tools:** Anthropic and OpenAI document their CLIs as `npm i -g`, and these are long-lived global binaries, not project deps:

```bash
npm install -g @anthropic-ai/claude-code @openai/codex
```

Verify the current Codex package name before relying on it (`npm view @openai/codex version`); the OpenAI CLI package has been renamed before. `@anthropic-ai/claude-code` is stable. Everything else is `pnpm add` inside a project — you will not run `npm install` in a project again.

### Step 11 — Install uv (Python)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

This installs `uv` and `uvx` into `~/.local/bin`. Workflow details are Part 6.

### Step 12 — Install global Python tools via uv

```bash
uv tool install jupyterlab    # optional global notebook launcher; per-project is still preferred
# graphify and other personal CLIs you keep globally:
# uv tool install <tool>
```

**Why `uv tool`:** global CLIs get isolated environments under `~/.local/share/uv/tools` with shims on `$PATH` — never polluting system Python. This is the correct home for the "uv used only for global tools" pattern, now done deliberately.

### Step 13 — Turn off Windows PATH bleed-through

Edit `/etc/wsl.conf`:

```ini
[boot]
systemd=true

[user]
default=anant_gupta

[interop]
enabled=true
appendWindowsPath=false

[automount]
enabled=true
options="metadata,umask=22,fmask=11"
```

**Why `appendWindowsPath=false`:** stops Windows `node.exe`/`python.exe` from shadowing your WSL binaries and causing "wrong version" bugs (Part 0, fact 6). `interop` stays enabled so you can still call `explorer.exe .` or `code .` explicitly. **Why `metadata` automount option:** lets Linux permissions/`chmod` work on `/mnt` files, avoiding everything-is-777 noise when you do touch Windows paths. Apply with `wsl --shutdown`.

### Step 14 — The complete recommended `~/.bashrc`

This is the final state. It initializes fnm with `--use-on-cd`, starts a single SSH agent (fixing the classic double-start bug), sets XDG and tool cache locations, and adds maintenance aliases. Replace your `~/.bashrc` tool-init sections with this block (keep the default Ubuntu preamble above it):

```bash
# ---------- PATH ----------
export PATH="$HOME/.local/bin:$PATH"

# ---------- XDG base dirs (explicit, so tools stop scattering) ----------
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_STATE_HOME="$HOME/.local/state"
export XDG_CACHE_HOME="$HOME/.cache"

# ---------- fnm (fast Node manager, auto-switch on cd via .nvmrc) ----------
FNM_PATH="$HOME/.local/share/fnm"
if [ -d "$FNM_PATH" ]; then
  export PATH="$FNM_PATH:$PATH"
  eval "$(fnm env --use-on-cd --shell bash)"
fi

# ---------- pnpm ----------
export PNPM_HOME="$HOME/.local/share/pnpm"
case ":$PATH:" in *":$PNPM_HOME:"*) ;; *) export PATH="$PNPM_HOME:$PATH" ;; esac

# ---------- uv ----------
export UV_CACHE_DIR="$HOME/.cache/uv"

# ---------- cache redirection for noisy tools ----------
export PUPPETEER_CACHE_DIR="$HOME/.cache/puppeteer"

# ---------- single SSH agent (no double-start) ----------
SSH_ENV="$HOME/.ssh/agent.env"
start_agent() {
  ssh-agent -s > "$SSH_ENV"
  chmod 600 "$SSH_ENV"
  . "$SSH_ENV" > /dev/null
  ssh-add ~/.ssh/id_ed25519 2>/dev/null
}
if [ -f "$SSH_ENV" ]; then
  . "$SSH_ENV" > /dev/null
  # if the saved PID isn't a running agent, restart it
  kill -0 "$SSH_AGENT_PID" 2>/dev/null && ssh-add -l >/dev/null 2>&1 || start_agent
else
  start_agent
fi

# ---------- aliases ----------
alias ll='ls -alh'
alias gs='git status'
alias cleanup='~/tools/monthly-cleanup.sh'
```

**Why the SSH block looks like that:** the common buggy `.bashrc` launches a new `ssh-agent` on every shell, leaving dozens of orphaned agents. This version persists the agent details to `~/.ssh/agent.env`, reuses a live agent, and only starts a new one if none is running — exactly one agent per login.

---

## PART 4 — PROJECT DIRECTORY TAXONOMY

A flat dumping ground is how `boom/target/` and `ecc-setup.sh` ended up homeless. Use this fixed structure:

```text
~/
├── projects/
│   ├── hub/        # products you own and ship (portfolio, Assisto_website, hivemind)
│   ├── ai/         # AI/agentic experiments and tools (RAG pipelines, agents)
│   ├── hackathon/  # time-boxed; may be abandoned (Resq, opspilot, safereach)
│   ├── scratch/    # throw-away experiments — explicitly disposable
│   └── work/       # employer projects — DIFFERENT git identity (Part 9)
├── tools/          # personal scripts and utilities (the home for ecc-setup.sh)
└── dotfiles/       # version-controlled dotfiles repo (Part 11)
```

Create it:

```bash
mkdir -p ~/projects/{hub,ai,hackathon,scratch,work} ~/tools ~/dotfiles
mv ~/ecc-setup.sh ~/tools/ 2>/dev/null || true
```

**Why each category:**
- `hub` — things with users; held to a quality bar, always on GitHub, always backed up.
- `ai` — agentic/RAG work; Python-heavy, uv-managed.
- `hackathon` — time-boxed. Archive (push to GitHub + delete locally) once the event ends; never let these rot and accrue `node_modules`.
- `scratch` — the pressure valve. Without a sanctioned junk drawer, throwaway code lands in `hub` and pollutes it. Anything here can be deleted without thought.
- `work` — physically separate so a `gitdir:` conditional include can enforce the employer email and signing key (Part 9).

**Graduation rules:** a `scratch` idea that proves out gets `git init` + moved to `hub` or `ai`. A `hackathon` repo worth keeping moves to `hub`; otherwise push it and delete the local copy.

**Why scripts go in `~/tools/` or `~/.local/bin/`, never `$HOME`:** the home root is for dot-config, not executables. Put runnable utilities in `~/.local/bin` (already on `$PATH`) and source-y project scripts in `~/tools/`. `ecc-setup.sh` sitting in `$HOME` was a symptom of having no script home — now it has one.

---

## PART 5 — ENVIRONMENT ISOLATION: NODE.JS

### The model: one default, per-project pins

fnm holds a small set of installed Node versions. The **default** is what a brand-new shell uses when a directory has no pin. A **`.nvmrc`** file pins a project to an exact version, and `--use-on-cd` switches to it automatically the moment you `cd` in.

**Why:** "works on my machine" Node bugs come from version drift. A committed `.nvmrc` makes the version part of the repo, so every machine (and Vercel) builds against the same Node. The old machine had 4 versions and no `.nvmrc` — drift with no guardrail.

### The `.nvmrc` workflow

Every project gets a `.nvmrc`. For a Next.js app on the LTS line:

```bash
cd ~/projects/hub/portfolio
node --version            # whatever fnm currently has active
echo "22" > .nvmrc        # pin major version (LTS)
fnm use                   # switch now; auto on future cd thanks to --use-on-cd
git add .nvmrc && git commit -m "chore: pin node version"
```

When you `cd` into a project whose pinned version isn't installed, fnm prompts to install it. To force install from the file:

```bash
fnm install               # reads .nvmrc / .node-version in the cwd
```

The `--use-on-cd` hook is already in your `.bashrc` (Part 3, Step 14): `eval "$(fnm env --use-on-cd --shell bash)"`. No fragile 40-line bash function like nvm requires.

### npm vs pnpm — the decision, restated as rules

| Use | Tool | Command |
| --- | --- | --- |
| Project dependencies | **pnpm** | `pnpm add <pkg>`, `pnpm install`, `pnpm dev` |
| Monorepo workspaces | **pnpm** | `pnpm-workspace.yaml` + `pnpm --filter` |
| Global AI CLIs | **npm** | `npm i -g @anthropic-ai/claude-code @openai/codex` |
| Anything else global | nothing | install per-project instead |

**Why this split is non-negotiable:** running both package managers in the same project produces two lockfiles and two `node_modules` resolution models — the exact "both caches accumulating" mess from the audit. pnpm for all projects, npm reserved for the two documented global CLIs, and you will never again wonder which one installed what.

### Global vs per-project — the rule

- **Goes global (npm `-g`):** standalone CLIs you invoke from any directory and that have no project — `@anthropic-ai/claude-code`, `@openai/codex`.
- **Never global:** anything a project depends on (`next`, `typescript`, `tailwindcss`, `eslint`, `prisma`, `vercel`). Use `pnpm add -D` and run via `pnpm exec`/scripts. Global installs of these cause version conflicts across projects.

### Starting a Next.js project (exact files)

```bash
cd ~/projects/hub
pnpm create next-app@latest my-app --typescript --tailwind --eslint --app --src-dir --use-pnpm
cd my-app
echo "22" > .nvmrc
fnm use
```

### `.gitignore` for Node projects

```gitignore
# dependencies
node_modules/
.pnpm-store/

# next.js / build output
.next/
out/
dist/
build/
.turbo/

# env & secrets
.env
.env*.local

# misc
*.log
.DS_Store
```

**Why:** `node_modules` is always regenerable from the lockfile — committing it bloats the repo and the VHDX. `.env*.local` must never be committed (Part 9/11). `.next`, `.turbo`, `dist` are build artifacts.

---

## PART 6 — ENVIRONMENT ISOLATION: PYTHON WITH UV

uv replaces pip, venv, pyenv, virtualenv, and (for almost all of your work) conda. It is one Rust binary that is 10–100x faster than pip and creates an isolated `.venv` per project automatically.

### The three uv use cases

| Use case | Command family | Where it lives |
| --- | --- | --- |
| Project environments | `uv init` / `uv add` / `uv run` / `uv sync` | `.venv/` in the project |
| Global tools (CLIs) | `uv tool install` / `uvx` | `~/.local/share/uv/tools` |
| Python version management | `uv python install 3.12` | `~/.local/share/uv/python` |

### Wrong default to know: system pip has no isolation

`pip install <pkg>` against `/usr/bin/python3` mutates the OS Python that Ubuntu itself depends on — the exact anti-pattern in the audit. **Never `pip install` outside a uv-managed environment.** uv refuses to touch system Python by default; lean on that.

### Starting a new Python project

```bash
cd ~/projects/ai
uv init my-rag-agent
cd my-rag-agent
uv add langchain anthropic chromadb pydantic
uv run python src/main.py     # runs inside the project .venv automatically
```

`uv init` creates `pyproject.toml`; the first `uv add`/`uv run` creates `.venv/` and the cross-platform `uv.lock`. `uv run` re-syncs the env to the lockfile before every run, so the environment can never silently drift from `pyproject.toml`.

### uv manages Python itself

uv downloads and pins interpreters — you don't need system Python or pyenv:

```bash
uv python install 3.12 3.13   # install interpreters uv manages
uv python pin 3.12            # writes .python-version for this project
```

**Why `.python-version`:** like `.nvmrc` for Node, it pins the interpreter per project and is read automatically by `uv run`. Create it whenever a project needs a specific Python.

### Fullstack project layout (Python + JS in one repo)

For a project with both a Next.js frontend and a Python backend, `uv init` lives in the **backend subfolder**, beside its own `pyproject.toml`, while `package.json` governs the frontend:

```text
hivemind/
├── package.json          # frontend (pnpm)
├── .nvmrc
├── apps/web/             # Next.js
└── services/api/
    ├── pyproject.toml    # uv project root for the backend
    ├── .python-version
    └── .venv/            # backend env (gitignored)
```

Run the backend with `cd services/api && uv run uvicorn app:main`.

### Jupyter Lab — per project, not global

```bash
cd ~/projects/ai/my-rag-agent
uv add --dev jupyterlab
uv run jupyter lab
```

**Why per project:** a globally installed Jupyter cannot see a project's dependencies. Installed as a dev dependency and launched with `uv run`, the kernel sees exactly that project's packages. (Keeping a global `uv tool install jupyterlab` as a convenience launcher is fine, but real analysis runs per-project.)

### Migrating `tradingview` (existing `.venv`) to uv

Migrate it — don't keep the hand-rolled `.venv`:

```bash
cd ~/projects/hub/tradingview
uv init --bare                       # add pyproject.toml without touching code
uv add $(pip freeze --path .venv/lib/*/site-packages | sed 's/==.*//')  # or hand-list deps
rm -rf .venv && uv sync              # rebuild a clean, locked env
uv python pin 3.12
```

If `pyproject.toml` already lists dependencies, it is just `rm -rf .venv && uv sync`.

### `~/.local/share/uv` vs `~/.cache/uv`

| Path | Holds | Clean policy |
| --- | --- | --- |
| `~/.local/share/uv/` | Managed Python interpreters + installed global tools | **Do not blind-delete** — deleting removes your Pythons/tools |
| `~/.cache/uv/` | Wheel/build cache, shared across projects | **Safe to clean** anytime: `uv cache clean` |

The cache makes repeat installs near-instant via hard-links; cleaning it only forces the next install to repopulate. The data dir is real state.

### `.gitignore` for uv projects

```gitignore
.venv/
__pycache__/
*.py[cod]
.python-version   # commit this ONLY if you want to force the interpreter; usually keep it tracked
.ipynb_checkpoints/
.env
```

Commit `pyproject.toml` and `uv.lock` (reproducibility). Most teams **track** `.python-version`; the line above is shown so you know it exists — remove it from ignore if you want the pin enforced.

### When conda is still warranted (rare)

Only for CUDA/GPU stacks needing specific CUDA-CuDNN builds, or a package published solely on conda-forge (some bioinformatics). For your LangChain/Anthropic/FastAPI/RAG work, uv is sufficient. If you ever need it, install **miniforge** to `D:\` — never miniconda on C:.

---

## PART 7 — DOCKER IN WSL2 (SET UP BEFORE YOU NEED IT)

### Decision: Docker Desktop on Windows with WSL2 integration

Install **Docker Desktop on Windows** and enable WSL2 integration — do **not** install Docker Engine by hand inside Ubuntu.

**Why:** Docker Desktop runs the Docker daemon inside its own lightweight WSL2 distro (`docker-desktop`) and exposes the `docker`/`docker compose` CLIs into your Ubuntu distro via integration. You get automatic updates, the GUI, Kubernetes, and Dev Containers support, and the engine shares the same WSL2 VM platform as Ubuntu (so the `.wslconfig` memory cap governs both). A hand-rolled in-distro engine means manual `systemd` units, no GUI, and a second thing to maintain.

### Step 1 — Install and enable integration

1. Install Docker Desktop for Windows; ensure "Use WSL 2 based engine" is checked (default on Win 11).
2. Settings → Resources → WSL Integration → enable integration for **Ubuntu-24.04**.
3. Verify from WSL:

```bash
docker version && docker run --rm hello-world
```

### Step 2 — Redirect the disk image to D: before pulling anything

Docker's data disk defaults to `C:\Users\<you>\AppData\Local\Docker\wsl\...\ext4.vhdx` and grows fast with images and volumes.

1. Docker Desktop → Settings → **Resources → Advanced → Disk image location**.
2. Browse to `D:\Docker` and **Apply & Restart**. Docker shuts down WSL, moves the image, and remounts it.

**Why first:** doing this before your first `docker pull` means images/volumes are born on D:. Moving a multi-GB image later is slow and, per known Docker bugs, occasionally loses data if you hand-edit `settings.json` instead of using the GUI. Use the GUI.

### Step 3 — Dev Containers (VS Code) over WSL2

The Dev Containers extension uses Docker Desktop's WSL2 backend. With your project open in WSL (`code .`), run **Dev Containers: Reopen in Container**. VS Code builds the container against the engine in the WSL2 VM and reconnects the server inside it.

**Why this is fast in your setup:** the source already lives on native ext4 (World 2), and the container runs in the same VM — no `/mnt/` penalty. A `.devcontainer/devcontainer.json` makes the toolchain reproducible per project.

### Step 4 — A real local stack: Next.js + Supabase Postgres

For Supabase local dev, the official path is the Supabase CLI (`supabase start`, which itself orchestrates Docker). For a hand-rolled Postgres alongside a Next.js app, a minimal `docker-compose.yml`:

```yaml
services:
  db:
    image: postgres:16
    restart: unless-stopped
    environment:
      POSTGRES_USER: dev
      POSTGRES_PASSWORD: dev
      POSTGRES_DB: app
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data

  web:
    build: .
    command: pnpm dev
    environment:
      DATABASE_URL: postgres://dev:dev@db:5432/app
    ports:
      - "3000:3000"
    depends_on:
      - db

volumes:
  db-data:
```

`docker compose up -d` starts both; the named volume `db-data` lives inside Docker's (D:-located) disk image and survives restarts.

### Step 5 — Disk growth and prune policy

Images, stopped containers, dangling layers, and unused volumes accumulate inside `docker_data` and never shrink on their own (same VHDX behavior as Part 0).

```bash
docker system df                 # see what's consuming space
docker system prune              # remove stopped containers, unused networks, dangling images
docker system prune -a --volumes # aggressive: also unused images AND volumes (destroys data)
```

**Why two commands:** `prune` (no flags) is the safe weekly habit. The `-a --volumes` form deletes named volumes — only run it when you accept losing local DB data. After a big prune, run the Part 2 compaction on `D:\Docker\...\ext4.vhdx` (or rely on `sparseVhd`) to actually return the space to D:.

### Step 6 — `~/.docker/config.json`

With Docker Desktop integration, the CLI config in WSL is minimal — typically just the credential store pointer Desktop manages. Leave it as Docker Desktop writes it; do not hand-author credentials here. A clean default looks like:

```json
{
  "credsStore": "desktop"
}
```

### The Docker + WSL2 memory interaction

Docker's daemon runs in the WSL2 VM platform, so your `.wslconfig` `memory=24GB` cap is the **shared** ceiling for Ubuntu + the Docker engine. You do not set a second memory limit; the one cap governs both.

**Why this matters:** without the cap, a container build plus a `next build` can drive the VM to consume all 32 GB and freeze Windows. The cap is the safety valve for the whole VM, Docker included.

---

## PART 8 — VS CODE REMOTE-WSL SETUP

### Install once, the right way

1. Install **VS Code on Windows** (not inside WSL). During install, check **Add to PATH**.
2. Install the **WSL** extension (or the Remote Development pack) on the Windows side.
3. Open a project: from a WSL shell, `cd ~/projects/hub/portfolio && code .`. The status bar shows `WSL: Ubuntu-24.04`.

**Why from the WSL shell:** `code .` launches the Windows UI and provisions the VS Code Server inside Linux, attaching to the native filesystem. Opening via `\\wsl.localhost\` in a plain Windows window uses slow DrvFs instead.

### Which extensions install where

VS Code splits extensions into **UI** (run on Windows) and **Workspace** (run in WSL):

| Side | Examples | Why |
| --- | --- | --- |
| Windows (UI) | Themes, icon packs, keymaps | Pure presentation; no filesystem/runtime access |
| WSL (Workspace) | ESLint, Prettier, Python, Pylance, Tailwind CSS, Prisma, Docker, GitLens | They must run against Linux files, the Linux Node/Python, and the Linux language servers |

In the Extensions view, WSL-side extensions appear under a **WSL: Ubuntu** group; click **Install in WSL** for any that are dimmed/local-only. Use **Install Local Extensions in WSL** (cloud icon) to bulk-push your set on a fresh machine.

### `~/.vscode-server`: what it is and why it grows

`~/.vscode-server` holds the server binary (one per VS Code commit/version) plus all WSL-side extensions and their caches. It grows because **each VS Code update downloads a new server build and the old ones are not auto-removed** — the 3.1 GB in the audit is mostly stale server versions and extension copies (the same is true of `~/.cursor-server`).

Control it:

```bash
du -sh ~/.vscode-server/bin/*          # list server versions by hash
# keep the newest; remove old hashes:
ls -t ~/.vscode-server/bin | tail -n +2 | xargs -I{} rm -rf ~/.vscode-server/bin/{}
```

It is always safe to delete the entire directory — VS Code re-provisions it on next connect. (This is in the monthly script, Part 10.)

### `settings.json` — WSL remote settings

Open **Preferences: Open Remote Settings (WSL: Ubuntu)** so these apply only inside WSL, then set:

```json
{
  "terminal.integrated.defaultProfile.linux": "bash",
  "terminal.integrated.profiles.linux": {
    "bash": { "path": "bash", "args": ["-l"] }
  },
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "eslint.workingDirectories": [{ "mode": "auto" }],
  "files.watcherExclude": {
    "**/node_modules/**": true,
    "**/.next/**": true,
    "**/target/**": true,
    "**/.venv/**": true
  }
}
```

**Why `args: ["-l"]` (login shell):** VS Code's integrated terminal must source `~/.bashrc` for fnm's `--use-on-cd` hook to fire, so the terminal picks up the project's `.nvmrc` Node automatically. A non-login shell would skip the init and you'd be on the default Node everywhere. **Why `python.defaultInterpreterPath` points at `.venv`:** so Pylance and the test runner use the uv-created environment, not system Python. **Why `files.watcherExclude`:** stops the file watcher from indexing giant generated dirs, which otherwise spikes CPU.

### Per-project `.vscode/settings.json` (Next.js)

Commit this so the whole team gets consistent behavior:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": { "source.fixAll.eslint": "explicit" },
  "typescript.tsdk": "node_modules/typescript/lib",
  "tailwindCSS.experimental.classRegex": [["cva\\(([^)]*)\\)", "[\"'`]([^\"'`]*).*?[\"'`]"]]
}
```

**Why `typescript.tsdk`:** forces VS Code to use the project's pinned TypeScript (from pnpm's `node_modules`) instead of the bundled one, so editor and CI agree on types.

### Settings sync between Windows and WSL

VS Code reuses your Windows user settings inside WSL automatically; Remote (WSL) settings **override** them only where you set them. Turn on **Settings Sync** (signed in with GitHub) so a new laptop pulls your base settings; the WSL-specific overrides above live in the remote settings layer.

### One command to open from Windows Explorer

From any WSL path:

```bash
code .
```

From a Windows prompt, target the distro directly:

```powershell
code --remote wsl+Ubuntu-24.04 /home/anant_gupta/projects/hub/portfolio
```

---

## PART 9 — GIT IDENTITY AND CREDENTIALS

The old machine committed everything as `gupt0479@umn.edu`. Going forward: personal email everywhere by default, employer email only inside `~/projects/work/`, enforced automatically.

### Global identity (personal)

`~/.gitconfig`:

```ini
[user]
    name = Anant Gupta
    email = anantmahi721@gmail.com
[init]
    defaultBranch = main
[pull]
    rebase = true
[core]
    autocrlf = false
[commit]
    gpgsign = true
[gpg]
    format = ssh
[gpg "ssh"]
    allowedSignersFile = ~/.ssh/allowed_signers
[user]
    signingkey = ~/.ssh/id_ed25519.pub
[includeIf "gitdir:~/projects/work/"]
    path = ~/.gitconfig-work
```

### Conditional include for work

`~/.gitconfig-work` (only loaded for repos under `~/projects/work/`):

```ini
[user]
    email = your.name@employer.com
    signingkey = ~/.ssh/id_ed25519_work.pub
[core]
    sshCommand = ssh -i ~/.ssh/id_ed25519_work -o IdentitiesOnly=yes
```

**Why:** `includeIf "gitdir:~/projects/work/"` (note the **trailing slash** — required, matches the whole subtree) layers the work email and a separate key over the global config the instant you're in a work repo. No manual switching, no accidental personal-email commits at work or vice-versa.

Verify:

```bash
cd ~/projects/hub/portfolio && git config user.email   # anantmahi721@gmail.com
cd ~/projects/work/<repo>   && git config user.email   # employer email
```

### Authentication: SSH for git, gh for the API

- **Pushing/pulling:** use SSH remotes (`git@github.com:...`). SSH keys authenticate with no credential helper — simplest and most robust in WSL2.
- **HTTPS remotes + GitHub API/CLI:** `gh auth login` then `gh auth setup-git` makes `gh`'s token the `credential.helper`.

**Why not Windows Git Credential Manager via interop:** GCM-over-`/mnt/c` works but adds a cross-world dependency and PATH coupling. For a GitHub-only developer, SSH + `gh` is fewer moving parts and survives `appendWindowsPath=false`. (If you later use non-GitHub HTTPS hosts, the GCM interop helper is the documented fallback: point `credential.helper` at `/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager.exe`.)

### SSH commit signing (simpler than GPG)

GitHub verifies commits signed with your SSH key — no GPG keyring to manage. The `~/.gitconfig` above already sets `gpg.format = ssh` and `user.signingkey`. Two more steps:

1. Register the key as a **Signing Key** (a *separate* entry from the auth key) on GitHub:

```bash
gh ssh-key add ~/.ssh/id_ed25519.pub --type signing
```

2. Create the local allowed-signers file so `git log --show-signature` verifies locally:

```bash
echo "anantmahi721@gmail.com $(cat ~/.ssh/id_ed25519.pub)" > ~/.ssh/allowed_signers
```

**Why SSH signing:** you already have and trust the SSH key; reusing it for signing avoids a parallel GPG identity. Commits show "Verified" on GitHub once the signing key is registered.

### SSH agent

The single-agent bootstrap is already in `~/.bashrc` (Part 3, Step 14), replacing the double-start bug that spawned a new agent per shell. It loads `id_ed25519` once and reuses the running agent.

### Pre-push hook: block personal email in `~/projects/work`

A safety net in case a work repo is ever misconfigured. Add an executable hook (ideally via your dotfiles `core.hooksPath`, or per-repo at `.git/hooks/pre-push`):

```bash
#!/usr/bin/env bash
# Block pushes from ~/projects/work made with a personal email
case "$PWD" in
  "$HOME"/projects/work/*)
    email="$(git config user.email)"
    if [[ "$email" == *"@gmail.com" ]]; then
      echo "ERROR: refusing to push work repo with personal email ($email)." >&2
      echo "Fix: this repo should use ~/.gitconfig-work. Check 'git config user.email'." >&2
      exit 1
    fi
    ;;
esac
exit 0
```

**Why a hook on top of conditional includes:** belt and suspenders. The include sets the right email automatically; the hook catches the rare case where a repo was cloned outside `~/projects/work/` then moved, or a local override slipped in.

---

## PART 10 — CACHE MANAGEMENT AND VHDX GROWTH CONTROL

### Where data accumulates and how to control each

| Cache / dir | Populated by | Safe to clean? | Cleanup command |
| --- | --- | --- | --- |
| `~/.npm/_cacache` | npm (global CLI installs) | Yes | `npm cache clean --force` |
| `~/.npm/_npx` | npx one-off package runs | Yes (not touched by `npm cache clean`) | `rm -rf ~/.npm/_npx` |
| `~/.local/share/pnpm/store` | pnpm projects | Prune only | `pnpm store prune` |
| `~/.cache/pnpm` | pnpm metadata | Yes | `rm -rf ~/.cache/pnpm` |
| `~/.cache/uv` | uv builds/wheels | Yes | `uv cache clean` |
| `~/.cache/pip` | stray pip | Yes | `pip cache purge` (or delete) |
| `~/.cache/puppeteer` | Chromium for e2e | Yes | set `PUPPETEER_CACHE_DIR`; delete to reclaim |
| `~/.cache/ort.pyke.io` | Rust `ort` (ONNX Runtime) | Yes | `rm -rf ~/.cache/ort.pyke.io` |
| `~/.cache/prisma` | Prisma engines | Yes (regenerates) | `rm -rf ~/.cache/prisma` |
| `~/.cargo/registry` | cargo crate downloads | Yes | `rm -rf ~/.cargo/registry/{cache,src}` |
| `<rust-proj>/target` | cargo builds | Yes | `cargo clean` / `cargo sweep` |
| `~/.vscode-server`, `~/.cursor-server` | editor updates | Yes (regenerates) | remove old `bin/<hash>` dirs |

### The Rust `target/` problem (19 GB from one abandoned project)

`target/` is cargo's build output: compiled dependencies, incremental artifacts, fingerprints, and final binaries. It is the Rust `node_modules` — entirely regenerable, zero source value. `boom/target/` reached 19 GB because cargo keeps stacking artifacts across rebuilds and never garbage-collects them.

Distinguish two locations:

- **`<project>/target`** — per-project build output. Delete with `cargo clean` (removes all of it) or `cargo sweep --time 30` (removes only artifacts older than 30 days, keeping recent builds fast).
- **`~/.cargo/registry`** — downloaded crate sources/cache shared across projects. **Safe to delete**; cargo re-downloads on next build. `~/.rustup` holds toolchains (re-installable via `rustup`).

Always gitignore build output:

```gitignore
# Rust
/target/
**/*.rs.bk
```

Tools and the shared-cache option:

```bash
cargo install cargo-sweep          # smarter than cargo clean
cargo sweep --recursive --time 30 ~/projects   # clean stale target/ across all projects

# Optional: share compiled deps across projects to cut rebuild time/space
cargo install sccache
# then in ~/.bashrc: export RUSTC_WRAPPER=sccache
```

**Where cargo-installed binaries go:** they install to `~/.cargo/bin` (already on PATH via rustup). Keep them there; don't duplicate into `~/.local/bin`.

### pnpm store vs npm cache (the difference)

npm's cache (`~/.npm`) is a pile of tarballs it *may* reuse; it still copies files into each project's `node_modules`. pnpm's **store** (`~/.local/share/pnpm/store`) holds one immutable copy of each package version and **hard-links** it into projects, so 10 projects using React store React once. Clean them differently: `npm cache clean --force` vs `pnpm store prune` (which removes only packages no project references).

### puppeteer and ONNX caches

- **puppeteer** downloads full Chromium builds (626 MB). Pin the location with `PUPPETEER_CACHE_DIR` (set in `.bashrc`) and delete the dir to reclaim; it re-downloads on next test run.
- **`ort.pyke.io`** is created by the Rust `ort` crate (ONNX Runtime bindings) — almost certainly pulled in by a Rust/ML tool. Pure download cache; `rm -rf` it freely.

### The monthly maintenance script

Create `~/tools/monthly-cleanup.sh` and `chmod +x` it (aliased to `cleanup` in `.bashrc`):

```bash
#!/usr/bin/env bash
set -euo pipefail
echo "== Disk before =="; df -h / | tail -1

echo "== npm cache =="
npm cache clean --force 2>/dev/null || true
rm -rf ~/.npm/_npx 2>/dev/null || true   # _npx is NOT cleared by 'npm cache clean'

echo "== pnpm store prune =="
pnpm store prune 2>/dev/null || true

echo "== uv cache =="
uv cache clean 2>/dev/null || true

echo "== pip cache =="
pip cache purge 2>/dev/null || true

echo "== Rust: sweep stale target/ across projects =="
command -v cargo-sweep >/dev/null && cargo sweep --recursive --time 30 ~/projects 2>/dev/null || true
rm -rf ~/.cargo/registry/cache ~/.cargo/registry/src 2>/dev/null || true

echo "== Regenerable caches =="
rm -rf ~/.cache/puppeteer ~/.cache/ort.pyke.io ~/.cache/prisma ~/.cache/pnpm 2>/dev/null || true

echo "== Old editor server versions =="
for d in ~/.vscode-server/bin ~/.cursor-server/bin; do
  [ -d "$d" ] && ls -t "$d" 2>/dev/null | tail -n +2 | xargs -I{} rm -rf "$d/{}" 2>/dev/null || true
done

echo "== Reclaim ext4 free space =="
sudo fstrim -av || true

echo "== Disk after =="; df -h / | tail -1
echo "Now from Windows (PowerShell): wsl --shutdown   (sparseVhd auto-compacts the image)"
```

**Why end with `fstrim` + the shutdown note:** cleaning frees blocks inside Linux, but the VHDX only returns space to D: after `fstrim` marks them and the image compacts. With `sparseVhd=true`, the post-shutdown compaction is automatic; otherwise run the Part 2 procedure.

### VHDX compaction cadence

With `sparseVhd=true`, manual compaction is rarely needed. Run the explicit Part 2 `Optimize-VHD`/`diskpart` procedure only after a one-time huge delete (like removing `boom/target/`), when you want the space back on D: immediately rather than gradually.

---

## PART 11 — BACKUP STRATEGY

### What is NOT protected today (and why)

Your code lives in `~/projects/` **inside `ext4.vhdx`**. Google Drive and OneDrive back up files on NTFS; they cannot see inside the VHDX (Part 0, fact 1). They treat it as one opaque blob — skipped or re-uploaded whole. **Result: 35 GB+ of code is unprotected except whatever happens to be pushed to GitHub.** Three layers fix this.

### Layer 1 — GitHub is the primary code backup

Every project is a GitHub repo (private is free). The habit: commit and push before closing a session — not weekly.

```bash
# in ~/.bashrc as a convenience for end-of-session:
alias wip='git add -A && git commit -m "wip: $(date +%F-%H%M)" && git push'
```

A nightly safety net across all repos, runnable as a cron job or manually:

```bash
#!/usr/bin/env bash
# ~/tools/nightly-push.sh — push every repo with a remote and unpushed/uncommitted work
find ~/projects -maxdepth 3 -name .git -type d | while read -r g; do
  repo="$(dirname "$g")"
  cd "$repo" || continue
  git remote get-url origin >/dev/null 2>&1 || continue
  if [ -n "$(git status --porcelain)" ]; then
    git add -A && git commit -m "auto: nightly snapshot $(date +%F)" >/dev/null 2>&1 || true
  fi
  git push >/dev/null 2>&1 && echo "pushed: $repo" || echo "SKIP/FAIL: $repo"
done
```

**Why per-repo push beats backing up the VHDX nightly:** code is small, diffable, and recoverable to any machine. Pushing is incremental; exporting a 60 GB VHDX nightly is not.

### Layer 2 — Dotfiles repo (config you can't `git clone`)

A private `dotfiles` GitHub repo reproduces your environment in minutes. Track:

- `~/.bashrc`, `~/.bash_aliases`, `~/.profile`
- `~/.gitconfig` and `~/.gitconfig-work` **template** (no secrets)
- `~/.ssh/config` and `~/.ssh/allowed_signers` (config only — see exclusions)
- `~/.mcp.json`
- `~/tools/` (monthly-cleanup.sh, nightly-push.sh)
- `~/.config/` selectively (gh, etc.)
- A `bootstrap.sh` that symlinks these into `$HOME` on a new machine

**NEVER put in the dotfiles repo:** `~/.ssh/id_ed25519` (private keys), any `.env`/`.env.local`, `~/.claude/.credentials.json` or other auth tokens, API keys. Add a `.gitignore` and double-check `git status` before the first push.

### Layer 3 — Full VHDX export (disaster image)

For a point-in-time image of the whole Linux environment:

```powershell
wsl --shutdown
wsl --export Ubuntu-24.04 "D:\Backups\ubuntu-$(Get-Date -Format yyyyMMdd).tar"
```

Store the `.tar` on D: and copy it to external/cloud storage occasionally. Restore with `wsl --import <name> "D:\WSL\Ubuntu" <tar> --version 2`.

**Why this is the *third* layer, not the first:** it's a heavy, infrequent snapshot — good for "rebuild the exact machine," bad as a routine backup. Layers 1–2 are your daily protection.

### Recovery scenario: new laptop in ~30 minutes

1. Windows: partition C:/D:, disable hibernation, set env vars (Part 12).
2. `wsl --install Ubuntu-24.04 --location "D:\WSL\Ubuntu"`.
3. `git clone <dotfiles>` and run `bootstrap.sh` → `.bashrc`, git config, tools restored.
4. Restore SSH private key from your password manager / secure storage (the one thing not in any repo).
5. Install fnm, pnpm, uv, gh (Part 3 steps 7–12).
6. `gh auth login`; `git clone` your active repos into `~/projects/...`.
7. `pnpm install` / `uv sync` per project to rebuild `node_modules` / `.venv`.

Everything regenerates from GitHub + dotfiles + one secured SSH key.

---

## PART 12 — MIGRATION CHECKLIST (OLD WSL → NEW WSL)

### BEFORE touching the new laptop (on the old machine)

- [ ] Push every project to GitHub:

```bash
~/tools/nightly-push.sh          # or, per repo:
cd ~/projects/hub/portfolio && git add -A && git commit -m "pre-migration" && git push
cd ~/projects/hub/Assisto_website && git add -A && git commit -m "pre-migration" && git push
cd ~/projects/hub/hivemind && git add -A && git commit -m "pre-migration" && git push
cd ~/projects/hub/tradingview && git add -A && git commit -m "pre-migration" && git push
# repeat for ai/, hackathon/
```

- [ ] Confirm nothing is unpushed: `find ~/projects -name .git -maxdepth 3 -type d -execdir git status --porcelain \;` returns empty per repo.
- [ ] Commit + push your dotfiles repo (verify no secrets staged).
- [ ] Securely copy the SSH **private** key to your password manager (NOT a repo).
- [ ] Do NOT migrate: `boom/target/` (regenerates), any `node_modules/`, any `.venv/`, `~/.npm`/`~/.cache/*` (caches), editor servers. Run Part 13 cleanup first to shrink the optional export.
- [ ] (Optional) `wsl --export` a final image to external storage.

### ON THE NEW LAPTOP — Windows side first

- [ ] Partition during Windows install: C: 200 GB, D: remainder.
- [ ] Disable hibernation (reclaims a multi-GB `hiberfil.sys` on a machine that never hibernates):

```powershell
powercfg /hibernate off
```

- [ ] Set user environment variables before installing tools:

```powershell
[Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "D:\AI\ollama-models", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_CONTEXT_LENGTH", "32768", "User")
```

- [ ] Install Git for Windows (defaults; used by some Windows tools — your WSL git is separate).
- [ ] Install Docker Desktop; enable WSL2 engine (configure D: redirect after WSL exists, Part 7).
- [ ] Install VS Code on Windows with **Add to PATH** + the WSL extension.
- [ ] Create `%UserProfile%\.wslconfig` (Part 3, Step 3).

### ON THE NEW LAPTOP — WSL side (ordered)

1. `New-Item -ItemType Directory -Path "D:\WSL\Ubuntu" -Force`
2. `wsl --update; wsl --install Ubuntu-24.04 --location "D:\WSL\Ubuntu"`
3. Create the user; `sudo apt update && sudo apt upgrade -y`; install baseline packages + `gh` (Part 3, Step 4).
4. Write `/etc/wsl.conf` (systemd, default user, `appendWindowsPath=false`, automount metadata); `wsl --shutdown` and relaunch.
5. Restore SSH key from password manager; `chmod 600`/`700`.
6. `git clone` dotfiles; run `bootstrap.sh`; verify `~/.bashrc`, `~/.gitconfig`.
7. `gh auth login` + `gh auth setup-git`; `gh ssh-key add --type signing`.
8. Install fnm; `fnm install --lts && fnm install 24`; then `fnm default <lts-version>` (the exact `v22.x` from `fnm list`).
9. `corepack enable && corepack prepare pnpm@latest --activate`; set pnpm store-dir.
10. `npm i -g @anthropic-ai/claude-code @openai/codex`.
11. Install uv; `uv tool install` your global tools.
12. `mkdir -p ~/projects/{hub,ai,hackathon,scratch,work} ~/tools ~/dotfiles`.
13. `git clone` active repos; `pnpm install` / `uv sync` each.
14. Docker Desktop → redirect disk image to `D:\Docker`; enable Ubuntu integration.
15. `code .` in a project to provision `~/.vscode-server`; install WSL-side extensions.

### VALIDATION (confirm before moving on)

- After step 2: `wsl -l -v` lists Ubuntu-24.04 as v2; `D:\WSL\Ubuntu\ext4.vhdx` exists.
- After `.wslconfig`: inside WSL, `nproc` = 12, `free -h` ≈ 22–23 GiB.
- After step 4: `echo $PATH` contains no `/mnt/c/...node` entries; `which node` → a path under `~/.local/share/fnm`.
- After step 8: `cd` into a repo with `.nvmrc` auto-switches Node (`node -v` matches the file).
- After step 7: `git commit` in a test repo shows "Verified" signature locally (`git log --show-signature`).
- After step 14: `docker run --rm hello-world` succeeds; image landed under `D:\Docker`.

---

## PART 13 — CURRENT MACHINE CLEANUP (RUN NOW, BEFORE MIGRATING)

Reclaim space and prove what is disposable. Expected total recovery: **~30+ GB inside the VHDX**, most of it returned to D: after compaction.

> **Status (2026-06-08):** Steps 2–7 were executed on the current machine and reclaimed ~8 GB (npm `_cacache` 4.2 GB, pnpm 3.5 GB, uv 1.0 GB, plus `~/.yarn`/`~/Library` and assorted caches). Step 1 (the 19 GB `boom/target`) and Step 8's `fstrim` are **still pending** because they require `sudo` (see the root-owned gotcha below).

### 1. Delete the 19 GB Rust build artifacts

```bash
cd ~/projects/umn/boom && cargo clean
```

**Gotcha — the `boom/` tree is owned by `root`, not your user.** `cargo clean` run as your user removes **0 files** (it silently can't touch root-owned paths), and a plain `rm -rf` also fails. Use `sudo`, and fix the ownership so this never recurs:

```bash
sudo rm -rf ~/projects/umn/boom/target          # frees the 19 GB
sudo chown -R "$USER:$USER" ~/projects/umn/boom  # so future builds/cleans need no sudo
```

**Why this happened:** the tree was created with elevated privileges (a `sudo` build or a Docker bind-mount writing as root). On the new machine, never build inside a directory you `sudo`-created — that is what produced the unremovable artifacts. **Why safe to delete:** `target/` is 100% regenerable build output with zero source value, and the project is abandoned. Recovers ~19 GB.

### 2. Clean the npm cache (6.1 GB)

```bash
npm cache clean --force      # clears _cacache (~4.2 GB)
rm -rf ~/.npm/_npx           # the npx cache (~2.0 GB) — NOT cleared by the line above
```

If `npm config get cache` points somewhere unexpected (an env var or `.npmrc` can override it), force the real path: `npm cache clean --force --cache "$HOME/.npm"`.

### 3. Prune the pnpm store

```bash
pnpm store prune          # removes packages no project references (~part of 4.4 GB)
```

### 4. Clean the uv cache

```bash
uv cache clean            # ~654 MB
```

### 5. Reduce nvm to the versions you'll keep (then plan its removal)

```bash
nvm ls
nvm uninstall v24.12.0    # keep only one current + one LTS
nvm uninstall v24.13.1
# after fnm is in place on the new machine, the whole ~/.nvm (2.1 GB) goes away
```

### 6. Remove old editor server versions

```bash
du -sh ~/.vscode-server/bin/* ~/.cursor-server/bin/* 2>/dev/null
ls -t ~/.vscode-server/bin | tail -n +2 | xargs -I{} rm -rf ~/.vscode-server/bin/{}
ls -t ~/.cursor-server/bin | tail -n +2 | xargs -I{} rm -rf ~/.cursor-server/bin/{}
```

### 7. Sweep regenerable caches and stray dirs

```bash
rm -rf ~/.cache/puppeteer ~/.cache/ort.pyke.io ~/.cache/prisma ~/.cache/pnpm
rm -rf ~/.cargo/registry/cache ~/.cargo/registry/src
rm -rf ~/Library ~/.yarn          # macOS-style dir + unused yarn
mv ~/ecc-setup.sh ~/tools/ 2>/dev/null || true
```

### 8. Reclaim and verify

`fstrim` requires `sudo` (run it in an interactive WSL terminal where you can enter your password):

```bash
sudo fstrim -av
du -sh ~ 2>/dev/null
df -h /
```

Then return the space to D: (Windows PowerShell):

```powershell
wsl --shutdown
Optimize-VHD -Path "D:\WSL\Ubuntu\ext4.vhdx" -Mode Full   # Home edition: use diskpart (Part 2)
```

Compare `D:\WSL\Ubuntu\ext4.vhdx` size before/after — it should drop by roughly the space you freed inside Linux.

---

*End of guide.*
## Contrast / What It Is Not
## Failure Modes / Misconceptions
> [!WARNING]
>
## Evidence From This Vault
- [[ ]]
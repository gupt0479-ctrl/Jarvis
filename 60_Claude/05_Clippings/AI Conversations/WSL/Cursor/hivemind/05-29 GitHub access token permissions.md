---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl
title: "GitHub access token permissions"
started_at: 2026-05-29T14:03:27
ended_at: 2026-05-29T16:14:38
exported_at: 2026-07-30T19:56:24
project: hivemind
cwd: "/home/anant_gupta/projects/hub/hivemind"
session_id: 5722ede8-befd-4636-ae15-09335c8c9cbd
status: raw
turn_count: 4
tools_used:
  Grep: 2
  Read: 2
  WebFetch: 1
  WebSearch: 1
files_touched:
  - "/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-hivemind/uploads/permissions-required-for-fine-grained-personal-access-tokens-0.md"
  - "/home/anant_gupta/projects/hub/hivemind"
  - "/home/anant_gupta/projects/hub/hivemind/Docs"
  - "/home/anant_gupta/projects/hub/hivemind/Docs/GITHUB_WORKFLOW.md"
files_changed_count: 0
lines_added: 0
lines_removed: 0
tags:
  - input
  - ai-conversation
  - cursor
  - wsl
---

# GitHub access token permissions

## You

<uploaded_documents>
The following documents have been saved to your filesystem. You can read them using your file-reading tool or other tools:
- /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-hivemind/uploads/[REDACTED].md
</uploaded_documents>
<user_query>
i was setting up the github access token for cursor and i came across the permissions. I am confused regarding what permissions should i allow an ai platoform in general not just cursor. Analyze this website and guide me through the permissions i should give agents: "https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens?apiVersion=2026-03-10 "
</user_query>

## Cursor

Reviewing the GitHub permissions doc and your uploaded notes so we can recommend a sensible token scope for AI agents.

[REDACTED]

Checking whether the repo documents GitHub integration expectations.

[REDACTED]

[REDACTED]

The [GitHub permissions reference page](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens?apiVersion=2026-03-10) is a **lookup table**, not a setup guide. It answers: *“If I grant permission X, which API endpoints become available?”* It does not tell you what an AI agent needs — you decide that from what you want the agent to do, then use the table to verify.

Below is a practical framework for **any AI platform** (Cursor, Copilot-style agents, MCP servers, etc.), with security as the default.

---

## Mental model: three layers

Fine-grained PATs have three scopes:

| Layer | What it controls | For AI agents |
|-------|------------------|---------------|
| **Repository permissions** | Code, PRs, CI, issues on selected repos | This is where almost everything lives |
| **Organization permissions** | Org members, org secrets, org settings | Usually **none** for personal dev |
| **Account permissions** | Your profile, email, SSH keys, gists | Usually **none** |

Also set:

1. **Resource owner** — your user account (or one org, if needed)
2. **Repository access** — **Only select repositories**, not “All repositories”
3. **Expiration** — 30–90 days, rotate regularly

---

## What AI coding agents actually do

Most agents fall into a few buckets:

| Task | What it needs |
|------|----------------|
| Read code, browse repo | `Metadata: Read`, `Contents: Read` |
| Push branches / commits | `Contents: Read and write` |
| Open/update PRs, comment | `Pull requests: Read and write` |
| Read CI status / logs | `Actions: Read` |
| Create/manage issues | `Issues: Read and write` |
| Edit `.github/workflows/` | `Workflows: Read and write` (high risk) |
| Merge PRs | `Contents: Write` + often `Pull requests: Write` |
| Trigger/rerun CI | `Actions: Write` (usually skip) |

**Git over HTTPS** (clone, push) with a fine-grained PAT requires **`Contents: Read and write`**. That is the most common cause of 403 on `git push` when no repo permissions were selected.

---

## Recommended presets (least privilege)

### Tier 1 — Read-only agent (explore, review, answer questions)

**Repository permissions:**

| Permission | Access |
|------------|--------|
| Metadata | Read |
| Contents | Read |
| Pull requests | Read |
| Issues | Read |
| Actions | Read *(if you want CI/debug help)* |

**Organization / Account:** none

Good for: “explain this PR”, “why did CI fail?”, code search without writes.

---

### Tier 2 — Daily dev agent (recommended for Cursor + MCP)

This matches a typical workflow like your HiveMind fork flow: push branches to your fork, open PRs, triage CI.

**Repository permissions** (on **only the repos the agent should touch**):

| Permission | Access | Why |
|------------|--------|-----|
| **Metadata** | Read | Required baseline for private repo API access |
| **Contents** | Read and write | Read files, push branches, git operations |
| **Pull requests** | Read and write | Create/update PRs, comments, reviews |
| **Issues** | Read and write | Optional; only if agent manages issues |
| **Actions** | Read | Read workflow runs, logs, check status |
| **Commit statuses** | Read | Optional; extra check/CI context |

**Do not grant** at this tier: Administration, Secrets, Webhooks, Environments, Workflows (write).

**Fork workflow note:** If the agent pushes to `gupt0479-ctrl/hivemind` but opens PRs against `darshgarg7/HiveMind`, include **both repos** in “Selected repositories” (upstream can often stay read-heavy if it’s public, but PR creation may still need `Pull requests: Write` on the base repo).

---

### Tier 3 — Full automation (use sparingly)

Add only if you explicitly want the agent to:

| Permission | Access | Risk |
|------------|--------|------|
| Workflows | Read and write | Can change CI pipelines |
| Actions | Write | Can rerun/cancel workflows, approve deployments |
| Administration | Read | Repo settings, branch protection visibility |
| Pages | Write | Can change GitHub Pages |

Still avoid: **Administration: Write**, **any Secrets**, **Webhooks: Write**, **Members** (org).

---

## Permissions to keep OFF for AI agents

These are the ones that cause real damage if the token leaks or the agent misbehaves:

| Permission | Why deny |
|------------|----------|
| **Administration: Write** | Delete repo, change branch protection, add collaborators |
| **Secrets** (Actions, Dependabot, Codespaces, Agent secrets) | Read/write CI and deployment secrets |
| **Environments: Write** | Change deployment envs and their secrets |
| **Webhooks: Write** | Exfiltration path (send repo events elsewhere) |
| **Organization → Members / Administration** | Org-wide changes |
| **Account → Profile, Email, SSH keys, GPG keys** | Account takeover surface |
| **Codespaces: Write** | Spin up cloud dev environments on your behalf |

**“Agent secrets” / “Agent variables” / “Copilot agent settings”** in the doc are for **GitHub’s own Copilot/cloud agents**, not Cursor or generic MCP servers. You generally do **not** need those for Cursor.

---

## How the doc page helps in practice

When something fails with 403/404:

1. GitHub returns an `X-Accepted-GitHub-Permissions` header saying what was missing.
2. Search the doc for that permission name.
3. Grant the **minimum** access level (Read vs Write) for that endpoint.

Examples from the doc:

- `GET /repos/{owner}/{repo}/contents/{path}` → **Contents: Read**
- `PUT /repos/{owner}/{repo}/contents/{path}` (push file) → **Contents: Write**
- `POST /repos/{owner}/{repo}/pulls` → **Pull requests: Write**
- `GET /repos/{owner}/{repo}/actions/runs/{run_id}/logs` → **Actions: Read**

---

## Cursor-specific guidance

Cursor uses GitHub in a few ways; scope to what you enable:

| Integration | Suggested permissions |
|-------------|---------------------|
| **Built-in GitHub (PRs, issues in UI)** | Tier 2 above |
| **Git push/pull in terminal** | `Contents: Read and write` on that repo |
| **GitHub MCP server** (`ghcr.io/github/github-mcp-server`) | Tier 2; add `Issues` if you use issue tools; add `Actions: Read` for CI tools |
| **Read-only “explain my codebase”** | Tier 1 |

Security habits that matter more than the exact checkbox list:

- **One token per tool** (e.g. separate tokens for Cursor vs a CI bot).
- **Repo-scoped**, not org-wide or all-repos.
- **Short expiry** + rotation.
- Keep **approval on** for MCP tool calls until you trust the setup.
- Never commit the token; use Cursor/MCP env config only.

---

## Quick decision checklist

When creating the token, ask:

1. **Which repos?** → Select only those (fork + upstream if doing cross-repo PRs).
2. **Will it push code?** → Yes → `Contents: Write`. No → `Contents: Read` only.
3. **Will it open/manage PRs?** → Yes → `Pull requests: Write`.
4. **Will it fix CI?** → Yes → `Actions: Read` (not Write unless you accept rerun/approve risk).
5. **Will it touch issues?** → Optional `Issues: Write`.
6. **Will it edit workflow YAML?** → Only then → `Workflows: Write` (otherwise skip).
7. **Anything else?** → Default to **no** until a specific error tells you otherwise.

---

## Suggested starting config for your HiveMind workflow

Given your fork-first flow (`origin` = your fork, PRs into `darshgarg7/HiveMind`):

**Selected repositories:**

- `gupt0479-ctrl/hivemind` (or your actual fork name)
- `darshgarg7/HiveMind` (if the agent creates PRs there)

**Repository permissions:**

```
Metadata          → Read
Contents          → Read and write   (fork pushes)
Pull requests     → Read and write   (gh pr create, comments)
Actions           → Read             (CI triage)
Issues            → Read             (optional Write if you want issue automation)
```

**Everything else:** leave at “No access”.

That is enough for: clone/read, push branches, open PRs, read checks, comment on PRs — without delete-repo, secrets, or org admin powers.

---

## Fine-grained vs classic token

Fine-grained PATs are the right default for AI agents (repo-scoped, granular). Classic `repo` scope is “full control of private repositories” — convenient but much broader than most agents need. Prefer fine-grained unless a tool explicitly requires classic scopes and cannot work otherwise.

---

If you tell me exactly what you want Cursor to do (e.g. “push + PR only”, “also merge”, “CI babysitting”, “issues”), I can narrow this to a minimal checkbox list for the token creation screen.

[REDACTED]

**Tool calls:**

- `Read` — `/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-hivemind/uploads/permissions-required-for-fine-grained-personal-access-tokens-0.md`
- `WebFetch` — `{"url":"https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens?apiVersion=2026-03-10"}`
- `Grep` — pattern `github|GITHUB|gh pr|personal access`, path `/home/anant_gupta/projects/hub/hivemind`
- `Grep` — pattern `GitHub|fine-grained|PAT|personal access`, path `/home/anant_gupta/projects/hub/hivemind/Docs`
- `WebSearch` — `{"search_term":"Cursor IDE GitHub fine-grained personal access token permissions required 2025","explanation":"Find Cursor-specific GitHub token permission guidance to complement the official GitHub docs."}`
- `Read` — `/home/anant_gupta/projects/hub/hivemind/Docs/GITHUB_WORKFLOW.md`

## You

<user_query>
These are all the settings: 
```
Actions
Workflows, workflow runs and artifacts.
Learn more.
Administration
Repository creation, deletion, settings, teams, and collaborators.
Learn more.
Agent secrets
Manage agent repository secrets.
Learn more.
Agent tasks
View, create, and manage agent tasks in a repository.
Learn more.
Agent variables
Manage agent repository variables.
Learn more.
Artifact metadata
Create and retrieve artifact metadata for a repository.
Learn more.
Attestations
Create and retrieve attestations for a repository.
Learn more.
Code quality
Access and manage code quality data for a repository.
Learn more.
Code scanning alerts
View and manage code scanning alerts.
Learn more.
Codespaces
Create, edit, delete and list Codespaces.
Learn more.
Codespaces lifecycle admin
Manage the lifecycle of Codespaces, including starting and stopping.
Learn more.
Codespaces metadata
Access Codespaces metadata including the devcontainers and machine type.
Learn more.
Codespaces secrets
Restrict Codespaces user secrets modifications to specific repositories.
Learn more.
Commit statuses
Commit statuses.
Learn more.
Contents
Repository contents, commits, branches, downloads, releases, and merges.
Learn more.
Copilot agent settings
View and manage Copilot cloud agent settings for a repository.
Learn more.
Custom properties
Read and write repository custom properties values at the repository level, when allowed by the property.
Learn more.
Dependabot alerts
Retrieve Dependabot alerts.
Learn more.
Dependabot secrets
Manage Dependabot repository secrets.
Learn more.
Deployments
Deployments and deployment statuses.
Learn more.
Discussions
Discussions and related comments and labels.
Learn more.
Environments
Manage repository environments.
Learn more.
Issues
Issues and related comments, assignees, labels, and milestones.
Learn more.
Merge queues
Manage a repository's merge queues
Learn more.
Metadata
Required
Search repositories, list collaborators, and access repository metadata.
Learn more.
Pages
Retrieve Pages statuses, configuration, and builds, as well as create new builds.
Learn more.
Pull requests
Pull requests and related comments, assignees, labels, milestones, and merges.
Learn more.
Repository security advisories
View and manage repository security advisories.
Learn more.
Secret scanning alert dismissal requests
View and manage secret scanning alert dismissal requests
Learn more.
Secret scanning alerts
View and manage secret scanning alerts.
Learn more.
Secret scanning push protection bypass requests
Review and manage repository secret scanning push protection bypass requests.
Learn more.
Secrets
Manage Actions repository secrets.
Learn more.
Variables
Manage Actions repository variables.
Learn more.
Webhooks
Manage the post-receive hooks for a repository.
Learn more.
Workflows
Update GitHub Action workflow files.
```

What to remove and what to read and write?
</user_query>

## Cursor

Here is a concrete checkbox guide for **every permission on your list**, assuming a typical AI coding agent (Cursor): push branches, open PRs, read CI, no secrets/admin/deployment control.

---

## Set these (recommended daily dev)

| Permission | Setting | Why |
|------------|---------|-----|
| **Metadata** | **Read** *(required)* | Baseline; repo discovery, collaborators list |
| **Contents** | **Read and write** | Read code, push branches, git over HTTPS |
| **Pull requests** | **Read and write** | Create/update PRs, comments, reviews |
| **Actions** | **Read** | CI runs, logs, failed checks |
| **Issues** | **Read** *(or Read and write if you want issue automation)* | Read linked issues; write only if agent should create/close issues |
| **Commit statuses** | **Read** *(optional but useful)* | Extra check/CI context; low risk |

That is the core set for your HiveMind-style workflow (fork push → PR → CI triage).

---

## Leave at **No access** (remove / do not enable)

| Permission | Why leave off |
|------------|---------------|
| **Administration** | Can delete repo, change settings, manage collaborators |
| **Agent secrets** | GitHub Copilot cloud agents — not Cursor |
| **Agent tasks** | GitHub agent tasks — not Cursor |
| **Agent variables** | GitHub Copilot agents — not Cursor |
| **Artifact metadata** | Supply-chain metadata; not needed for normal coding |
| **Attestations** | Signing/provenance; not needed for normal coding |
| **Code quality** | Niche; skip unless you explicitly use it |
| **Code scanning alerts** | Security tooling; skip unless you want security triage |
| **Codespaces** | Agent could create/manage cloud dev environments |
| **Codespaces lifecycle admin** | Start/stop/delete others’ Codespaces |
| **Codespaces metadata** | Not needed locally in Cursor |
| **Codespaces secrets** | Secret surface; never for AI |
| **Copilot agent settings** | GitHub Copilot cloud agent config — not Cursor |
| **Custom properties** | Org/repo metadata; not needed |
| **Dependabot alerts** | Optional later; not needed for coding |
| **Dependabot secrets** | **Never** — secret access |
| **Deployments** | Deployment control; high risk |
| **Discussions** | Only if you use GitHub Discussions |
| **Environments** | Can touch deployment envs and their secrets |
| **Merge queues** | Only if repo uses merge queues |
| **Pages** | GitHub Pages config/builds; not needed |
| **Repository security advisories** | Security advisories; skip unless security work |
| **Secret scanning alert dismissal requests** | Security admin |
| **Secret scanning alerts** | Security admin |
| **Secret scanning push protection bypass requests** | **Never** — can bypass secret blocking |
| **Secrets** | **Never** — Actions repo secrets |
| **Variables** | **Never** — Actions repo variables |
| **Webhooks** | Exfiltration / external hook setup |
| **Workflows** | See note below |

---

## The one optional exception: **Workflows**

| Permission | When to enable |
|------------|----------------|
| **Workflows** | **No access** by default |

- Reading `.github/workflows/*.yml` in the repo → already covered by **Contents: Read**
- Pushing edits to workflow files via git → covered by **Contents: Read and write**
- **Workflows: Read and write** is only needed if the agent must use the Workflows API (enable/disable workflows, dispatch via that API, etc.)

Most people should leave **Workflows** off and rely on **Contents** + **Actions: Read**.

---

## Visual summary

```
ENABLE (recommended):
  Metadata          → Read          (required)
  Contents          → Read and write
  Pull requests     → Read and write
  Actions           → Read
  Issues            → Read          (Write only if you want issue bots)
  Commit statuses   → Read          (optional, nice to have)

EVERYTHING ELSE     → No access
```

---

## If you want two tokens (best practice)

**Token A — “Cursor write”** (above table)  
For repos you actively develop: your fork + upstream if the agent opens PRs against it.

**Token B — “Cursor read-only”**  
Only: Metadata Read, Contents Read, Pull requests Read, Actions Read, Issues Read.  
Use when you only want explanations/reviews, no pushes.

---

## Quick “Read vs Write” rule

| Need | Rule |
|------|------|
| Agent reads code/PRs/CI | **Read** |
| Agent pushes code or opens PRs | **Read and write** on Contents + Pull requests |
| Anything with “secret”, “admin”, “environment”, “webhook”, “codespace”, “agent” | **No access** |
| Unsure | **No access** — add only when something fails with a permission error |

---

## Your HiveMind fork workflow

**Selected repositories:** only the repos the agent should touch (e.g. your fork + `darshgarg7/HiveMind` if it creates PRs there).

**Permissions:** use the “Enable” block above; leave everything else at No access.

That gives enough for push → PR → CI debugging without handing the agent secrets, repo deletion, or org-style admin powers.

If you tell me whether you want the agent to **merge PRs** or **only open them**, I can tighten Issues and Pull requests (Read-only vs Write) one step further.

[REDACTED]

## Actions Taken
- Summary: Read GITHUB_WORKFLOW.md, permissions-required-for-fine-grained-personal-access-tokens-0.md
- Files changed (Cursor): 0
- Lines: +0 / -0
- Files touched (from tool calls): /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-hivemind/uploads/permissions-required-for-fine-grained-personal-access-tokens-0.md, /home/anant_gupta/projects/hub/hivemind, /home/anant_gupta/projects/hub/hivemind/Docs, /home/anant_gupta/projects/hub/hivemind/Docs/GITHUB_WORKFLOW.md
- Commands run: (none)
- Tool call tally: Grep (2), Read (2), WebFetch (1), WebSearch (1)

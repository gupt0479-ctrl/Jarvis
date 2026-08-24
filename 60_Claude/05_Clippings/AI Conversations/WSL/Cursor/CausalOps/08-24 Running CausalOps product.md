---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: wsl
title: "Running CausalOps product"
started_at: 2026-08-24T13:41:03
ended_at: 2026-08-24T13:47:56
exported_at: 2026-08-24T13:53:48
project: CausalOps
cwd: "/home/anant_gupta/projects/hub/CausalOps"
session_id: fb8c07dc-a663-44cd-97dc-d05468280e0c
status: raw
turn_count: 2
tools_used:
  Glob: 3
  Grep: 11
  Read: 14
  Shell: 2
files_touched:
  - "/home/anant_gupta/projects/hub/CausalOps/AGENTS.md"
  - "/home/anant_gupta/projects/hub/CausalOps/README.md"
  - "/home/anant_gupta/projects/hub/CausalOps"
  - "/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps"
  - "/home/anant_gupta/projects/hub/CausalOps/docker-compose.yml"
  - "/home/anant_gupta/projects/hub/CausalOps/src/api.py"
  - "/home/anant_gupta/projects/hub/CausalOps/src/coordinator"
  - "/home/anant_gupta/projects/hub/CausalOps/src/coordinator/runner.py"
  - "/home/anant_gupta/projects/hub/CausalOps/.env.example"
  - "/home/anant_gupta/projects/hub/CausalOps/src"
  - "/home/anant_gupta/projects/hub/CausalOps/src/bus"
  - "/home/anant_gupta/projects/hub/CausalOps/src/coordinator/store.py"
  - "/home/anant_gupta/projects/hub/CausalOps/scripts/dev-compose.sh"
  - "/home/anant_gupta/projects/hub/CausalOps/app"
  - "/home/anant_gupta/projects/hub/CausalOps/app/src/lib/causalops-api.ts"
  - "/home/anant_gupta/projects/hub/CausalOps/src/engine.py"
  - "/home/anant_gupta/projects/hub/CausalOps/requirements.txt"
  - "/home/anant_gupta/projects/hub/CausalOps/app/src"
files_changed_count: 0
lines_added: 0
lines_removed: 0
tags:
  - input
  - ai-conversation
  - cursor
  - wsl
---

# Running CausalOps product

## You

<timestamp>Monday, Aug 24, 2026, 1:47 PM (UTC+4)</timestamp>
<user_query>
How do I run causalops? I just had a group meeting with darshgarg7 and team members. We found that we have way too excessive run time on the entire product. My job now will be to cut short the time it takes to run the entire thing. But first I want to run it with everything that I have already changed in this repo. Excluding this plan: `/home/anant_gupta/.cursor/plans/[REDACTED].plan.md`. We still have not run that plan because there are things to reconsider with run time. I want to run the product myself and maintain an in depth log about the run - how long, where it takes the longest to compute, etc. Let's run the product. First, walk me through the steps to run this. I will run it myself and all you have to do is watch the terminal, logs and commands run. 
</user_query>

## Cursor

Gathering the repo's run instructions and current state so we can walk you through a full run with timing logs.

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

[REDACTED]

You're on branch `plan/persistent-memory-mcp` with a `.env` already present — that includes your memory-layer work and excludes the PR-25 plan (nothing from that plan needs to be applied to run).

Here is the full walkthrough. Run these yourself; once you start the stack, I'll watch your terminal output and help you interpret timing.

---

## What you're running

The **full product** is five Docker services:

| Service | Port | Role |
|---------|------|------|
| **frontend** | 8080 | React UI |
| **api** | 8000 | Coordinator + FastAPI |
| **worker** | — | Kafka spawn consumer (child agents) |
| **redpanda** | 19092 | Event bus (telemetry SSE) |
| **mcp** | 8001 | Memory MCP server (optional for UI runs; memory retrieve/write runs inside the coordinator) |

The real execution path is `src/coordinator/runner.py` → `execute_run()`, not LangGraph's `graph.py`.

---

## Step 0 — Prerequisites

1. **Docker Desktop** with WSL integration enabled (Docker wasn't reachable from this environment, so confirm on your side):

```bash
docker --version
docker compose version
```

2. **`.env`** at repo root — you already have one. Minimum for a real LLM run:
   - `NVIDIA_API_KEY` — primary chat LLM
   - `GEMINI_API_KEY` — memory embeddings (`memory/embedder.py`)
   - `SUPABASE_*` — optional; memory phases fail gracefully if Supabase is down

3. **Quick sanity** (no LLM tokens):

```bash
curl http://localhost:8000/demo/estimate
```

Only works after the stack is up.

---

## Step 1 — Start the stack

From repo root:

```bash
cd /home/anant_gupta/projects/hub/CausalOps
docker compose up --build
```

Or without MCP (faster startup; memory still works via coordinator):

```bash
./scripts/dev-compose.sh
# equivalent to: docker compose up --build redpanda api worker frontend
```

Wait until you see the **api** healthcheck pass. Then verify:

```bash
curl http://localhost:8000/health
# → {"status":"ok"}
```

Open:
- UI: http://localhost:8080
- API docs: http://localhost:8000/docs

---

## Step 2 — Choose execution mode

This matters a lot for runtime:

| Mode | What it runs | Typical cost |
|------|--------------|--------------|
| **`standard`** (default) | Skips orchestrator/parent evolution; fast evaluator + fast causal loop | Much faster |
| **`deep`** | Full swarm: orchestrator → parent agents → child evolution → evaluator → causal loop → policy learning | Slowest path |

The UI toggle is in the Scenario Builder: **"Fast Loop"** vs **"Deep Loop"**.

For a **first baseline** on your current branch, start with **`standard`**. Switch to **`deep`** when you want to reproduce the team's slow-run complaint.

---

## Step 3 — Launch a run (pick one path)

### Option A — UI (recommended for first run)

1. Open http://localhost:8080
2. Enter or pick a scenario (min 20 chars in the prompt)
3. Choose **standard** or **deep**
4. Submit — the UI opens SSE telemetry automatically

### Option B — curl (async, same as UI)

Terminal 1 — start SSE **before** POST (UI does this automatically):

```bash
RUN_ID="run-$(date +%Y%m%d-%H%M%S)-baseline"
echo "RUN_ID=$RUN_ID"

curl -N "http://localhost:8000/run/${RUN_ID}/events" | tee "/tmp/causalops-${RUN_ID}-events.log"
```

Terminal 2 — enqueue the run:

```bash
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d "{
    \"run_id\": \"${RUN_ID}\",
    \"task_description\": \"A sophisticated adversary has compromised an edge firewall and is performing lateral movement across multiple domain controllers while security patches are being deployed.\",
    \"execution_mode\": \"standard\"
  }"
```

Change `"execution_mode"` to `"deep"` for the full swarm.

### Option C — curl sync (simple total wall-clock)

Blocks until done; good for one number:

```bash
/usr/bin/time -f 'TOTAL wall: %E  CPU: %P' \
  curl -s -X POST http://localhost:8000/run/sync \
    -H "Content-Type: application/json" \
    -d '{
      "task_description": "A sophisticated adversary has compromised an edge firewall and is performing lateral movement across multiple domain controllers while security patches are being deployed.",
      "execution_mode": "standard"
    }' | tee /tmp/causalops-sync-result.json
```

---

## Step 4 — Capture an in-depth timing log

There is **no built-in per-phase timer** in the codebase yet. Use these layers:

### 4a. Docker logs (best for backend phase boundaries)

In a separate terminal:

```bash
docker compose logs -f api worker 2>&1 | tee /tmp/causalops-docker-$(date +%Y%m%d-%H%M%S).log
```

Look for lines like `Gathered N child tasks`, phase changes, LLM calls, barrier waits.

### 4b. SSE events (best for UI-visible phase timeline)

Each event has a `ts` (ms) and `phase` field. Phases include `ORCHESTRATOR`, `CHILDREN_GATHER`, `EVALUATE`, `CAUSAL_SYNTH`, `COMPLETE`, `ERROR`.

After the run, diff consecutive `ts` values in your events log to get per-phase durations.

### 4c. Poll run status (coordinator phase in SQLite)

```bash
watch -n 5 "curl -s http://localhost:8000/run/${RUN_ID} | python3 -m json.tool"
```

The `phase` field tracks coordinator state: `memory_retrieve` → `orchestrator` / `standard_swarm` → `children` → `evaluator_fast` / `evaluator` → `causal_fast` / `causal_synthesis` → `reasoner` → `policy_learning` (deep only) → `memory_write` → `completed`.

### 4d. SQLite run store (post-run inspection)

```bash
sqlite3 /home/anant_gupta/projects/hub/CausalOps/data/runs.db \
  "SELECT run_id, status, phase, execution_mode, created_at, updated_at FROM runs ORDER BY created_at DESC LIMIT 5;"
```

`updated_at - created_at` gives total coordinator time per run.

### 4e. Zero-token smoke (evidence pipeline only)

Does **not** exercise the agent swarm:

```bash
curl -s http://localhost:8000/demo/estimate | python3 -m json.tool
```

Use this to confirm the stack is healthy before spending LLM tokens.

---

## Step 5 — What to record (template)

For each run, log:

```
Run ID:
Branch: plan/persistent-memory-mcp
Execution mode: standard | deep
Start / end (wall clock):
Total duration:
Evidence: demo fixture | custom

Phase breakdown (from SSE ts deltas):
  memory_retrieve:
  orchestrator / standard_swarm:
  parent_evolution + parents:        (deep only)
  child_evolution + children:
  evaluator / evaluator_fast:
  causal_synthesis / causal_fast:
  reasoner:
  policy_learning:                   (deep only)
  memory_write:

Notes: errors, retries, barrier timeouts
```

---

## Expected runtime hotspots (for your optimization work later)

Based on the coordinator sequence, the slowest phases are usually:

1. **Child agent dispatch** — Kafka barrier + `CAUSALOPS_SPAWN_CONCURRENCY=3` parallel LLM calls
2. **Orchestrator + parent evolution** — deep mode only
3. **Causal synthesis + DoWhy estimator** — retries in the causal loop
4. **Policy learning** — deep mode only
5. **Memory retrieve/write** — embedding API + Supabase (should be small; failures are swallowed)

---

## Suggested order for your first session

1. `docker compose up --build`
2. `curl http://localhost:8000/health`
3. `curl http://localhost:8000/demo/estimate` (zero tokens)
4. One **`standard`** full run with logging (`docker compose logs -f` + SSE or UI)
5. Optionally one **`deep`** run to reproduce the team's slow path

---

When you're ready, start **Step 1** (`docker compose up --build`) in a terminal. I'll watch that terminal and help you parse phase timing, errors, and bottlenecks as output comes in. Tell me which mode (`standard` or `deep`) and whether you're using the UI or curl.

[REDACTED]

**Tool calls:**

- `Read` — `/home/anant_gupta/projects/hub/CausalOps/AGENTS.md`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/README.md`
- `Glob` — pattern `docker-compose*.yml`, path `/home/anant_gupta/projects/hub/CausalOps`
- `Glob` — pattern `terminals/*.txt`, path `/home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps`
- `Grep` — pattern `Getting Started|docker-compose|/run`, path `/home/anant_gupta/projects/hub/CausalOps/README.md`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/docker-compose.yml`
- `Grep` — pattern `@app\.(post|get)|/run|/demo`, path `/home/anant_gupta/projects/hub/CausalOps/src/api.py`
- `Shell` — `cd /home/anant_gupta/projects/hub/CausalOps && git branch --show-current 2>/dev/null; git status -sb 2>/dev/null; ls -la .env 2>/dev/null || echo "no .env"; ls -la src/.env 2>/dev/null || true`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/README.md`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/src/api.py`
- `Grep` — pattern `duration|elapsed|timing|phase|log`, path `/home/anant_gupta/projects/hub/CausalOps/src/coordinator`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/src/coordinator/runner.py`
- `Grep` — pattern `phase.*duration|elapsed|timing|perf_counter`, path `/home/anant_gupta/projects/hub/CausalOps`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/.env.example`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/src/api.py`
- `Grep` — pattern `execution_mode|ExecutionMode`, path `/home/anant_gupta/projects/hub/CausalOps/src`
- `Grep` — pattern `publish_telemetry|phase`, path `/home/anant_gupta/projects/hub/CausalOps/src/bus`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/src/api.py`
- `Grep` — pattern `set_phase|phase`, path `/home/anant_gupta/projects/hub/CausalOps/src/coordinator/store.py`
- `Glob` — pattern `scripts/*`, path `/home/anant_gupta/projects/hub/CausalOps`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/scripts/dev-compose.sh`
- `Shell` — `docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' 2>/dev/null || echo "docker not available or not running"`
- `Grep` — pattern `execution_mode|POST.*run`, path `/home/anant_gupta/projects/hub/CausalOps/app`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/app/src/lib/causalops-api.ts`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/src/engine.py`
- `Grep` — pattern `stream_telemetry`, path `/home/anant_gupta/projects/hub/CausalOps/src`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/requirements.txt`
- `Grep` — pattern `duration|timing|elapsed|started`, path `/home/anant_gupta/projects/hub/CausalOps/src/engine.py`
- `Read` — `/home/anant_gupta/projects/hub/CausalOps/src/engine.py`
- `Grep` — pattern `deep|executionMode|execution_mode`, path `/home/anant_gupta/projects/hub/CausalOps/app/src`

## Actions Taken
- Summary: Read engine.py, requirements.txt, causalops-api.ts, dev-compose.sh, api.py
- Files changed (Cursor): 0
- Lines: +0 / -0
- Files touched (from tool calls): /home/anant_gupta/projects/hub/CausalOps/AGENTS.md, /home/anant_gupta/projects/hub/CausalOps/README.md, /home/anant_gupta/projects/hub/CausalOps, /home/anant_gupta/.cursor/projects/home-anant-gupta-projects-hub-CausalOps, /home/anant_gupta/projects/hub/CausalOps/docker-compose.yml, /home/anant_gupta/projects/hub/CausalOps/src/api.py, /home/anant_gupta/projects/hub/CausalOps/src/coordinator, /home/anant_gupta/projects/hub/CausalOps/src/coordinator/runner.py, /home/anant_gupta/projects/hub/CausalOps/.env.example, /home/anant_gupta/projects/hub/CausalOps/src, /home/anant_gupta/projects/hub/CausalOps/src/bus, /home/anant_gupta/projects/hub/CausalOps/src/coordinator/store.py, /home/anant_gupta/projects/hub/CausalOps/scripts/dev-compose.sh, /home/anant_gupta/projects/hub/CausalOps/app, /home/anant_gupta/projects/hub/CausalOps/app/src/lib/causalops-api.ts, /home/anant_gupta/projects/hub/CausalOps/src/engine.py, /home/anant_gupta/projects/hub/CausalOps/requirements.txt, /home/anant_gupta/projects/hub/CausalOps/app/src
- Commands run: cd /home/anant_gupta/projects/hub/CausalOps && git branch --show-current 2>/dev/null; git status -sb 2>/dev/null; ls -la .env 2>/dev/null || echo "no .env"; ls -la src/.env 2>/dev/null || true, docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' 2>/dev/null || echo "docker not available or not running"
- Tool call tally: Glob (3), Grep (11), Read (14), Shell (2)

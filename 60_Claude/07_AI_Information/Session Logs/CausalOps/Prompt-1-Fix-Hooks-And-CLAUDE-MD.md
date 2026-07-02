---
tags: [causalops, claude-code, hooks, bugfix]
created: 2026-07-01
session: fix-hooks
---

# Prompt 1 — Fix Hooks and CLAUDE.md

> Paste into a Claude Code session at `/home/anant_gupta/projects/hub/CausalOps/`.
> This session fixes three specific bugs. Do not add new features or refactor anything not listed.

---

## Prompt

```
Working directory: /home/anant_gupta/projects/hub/CausalOps/

Read these three files before making any changes:
  .claude/hooks/lint-on-edit.sh
  .claude/hooks/test-memory-on-edit.sh
  CLAUDE.md

Then make exactly the three fixes below. Nothing else.

---

FIX 1 — lint-on-edit.sh: python not in PATH

The hook calls `python -m ruff check "$file"` but `python` is not available
in the bash environment where hooks run. The hook silently does nothing.

Replace:
  result=$(python -m ruff check "$file" 2>&1)

With:
  result=$(/home/anant_gupta/projects/hub/CausalOps/.venv/bin/python -m ruff check "$file" 2>&1)

That is the only change to this file.

---

FIX 2 — test-memory-on-edit.sh: same python PATH issue

The hook calls `python -m pytest` which also silently fails.

Replace:
  python -m pytest tests/memory/test_extractor.py tests/memory/test_mcp_tools.py \

With:
  /home/anant_gupta/projects/hub/CausalOps/.venv/bin/python -m pytest \
    tests/memory/test_extractor.py tests/memory/test_mcp_tools.py \

That is the only change to this file.

---

FIX 3 — CLAUDE.md: stale LLM env vars

The Environment Variables section still has:
  AZURE_OPENAI_DEPLOYMENT=gpt-4o

This is wrong. Azure OpenAI is for embeddings ONLY. The chat LLM is Gemini.

Replace the entire "## Environment Variables" section with:

## Environment Variables

```bash
# Chat LLM — Gemini (NOT Azure OpenAI)
GEMINI_API_KEY=...
GEMINI_MODEL=gemini-2.5-flash          # or gemini-2.5-pro for complex reasoning tasks
GEMINI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/

# Azure OpenAI — embeddings ONLY (memory layer, not chat)
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_API_VERSION=2024-08-01-preview
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small

# Supabase — client (VITE_ prefix, safe in browser)
VITE_SUPABASE_URL=https://<new-project-ref>.supabase.co   # set after provisioning
VITE_SUPABASE_PUBLISHABLE_KEY=
VITE_SUPABASE_PROJECT_ID=<new-project-ref>

# Supabase — server (secrets — never use anon key in Python backend)
SUPABASE_URL=https://<new-project-ref>.supabase.co
SUPABASE_PUBLISHABLE_KEY=
SUPABASE_SERVICE_ROLE_KEY=             # REQUIRED for all Python backend writes (RLS)

# CausalOps runtime
CAUSALOPS_ENABLE_SPAWN_WORKER=0         # "1" → in-process spawn worker (api container only)
KAFKA_BOOTSTRAP=localhost:19092        # only needed outside compose
```

Remove the old entry `AZURE_OPENAI_DEPLOYMENT=gpt-4o` entirely.
Remove the "# New (needed before implementing memory layer)" comment — all vars are active.
Remove the "# Existing" comment — this distinction is no longer meaningful.
Do not add any other sections or remove any other content from CLAUDE.md.

---

VERIFICATION

After all three edits:

1. grep "python -m ruff" .claude/hooks/lint-on-edit.sh
   Must show the .venv/bin/python path, not bare "python".

2. grep "python -m pytest" .claude/hooks/test-memory-on-edit.sh
   Must show the .venv/bin/python path, not bare "python".

3. grep "AZURE_OPENAI_DEPLOYMENT\|gpt-4o" CLAUDE.md
   Must return nothing. That line must be gone.

4. grep "GEMINI_API_KEY" CLAUDE.md
   Must return the new line.

5. Test the lint hook manually:
   CLAUDE_FILE_PATHS=src/memory/extractor.py bash .claude/hooks/lint-on-edit.sh
   Should exit 0 with no output (file is clean).

6. Test the guard hook manually:
   CLAUDE_FILE_PATHS=src/dataset_compiler.py bash .claude/hooks/guard-sacred-files.sh
   Should exit 2 and print the BLOCKED message.

Report: three files changed, verification results. If any check fails, fix it before reporting done.
```

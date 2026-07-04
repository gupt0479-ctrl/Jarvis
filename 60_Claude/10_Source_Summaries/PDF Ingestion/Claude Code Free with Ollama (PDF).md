---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[10_Areas/AI/Claude Code|Claude Code]]"
source_url: 60_Claude/05_Clippings/PDFs/Claude Code Ollama Free Guide (1).pdf
source_note: "[[Claude Code Ollama Free Guide (1).pdf]]"
input_kind: pdf
track: ai
---
# How to Use Claude Code + OpenClaw for FREE with Ollama — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Claude Code Ollama Free Guide (1).pdf`
**Ingested:** 2026-07-04
**Pages:** 2
## Source
A short how-to by @therealjerrywu for running Claude Code (and OpenClaw) against a **local Ollama model instead of the paid Claude API** — free, no token limits.
## Key Claims
- ==The whole trick is one environment variable: point Claude Code's base URL at the local Ollama endpoint== — `ANTHROPIC_BASE_URL=http://localhost:11434 claude`
- Recommended local model: **GLM 4.7 Flash** (`ollama run glm4:flash`); alternatives: Gemma 3B (low-spec), Gemma 34B (lightweight-but-capable), GLM5 (cloud, not truly local)
- **You are not using the real Claude** — the interface is Claude Code's, the model is local (GLM 4.7 Flash), so quality ≠ Claude's
- Truly free 24/7 with no token limits as long as the model runs locally; works the same on Windows
## Full Content
1. Install **Ollama** (ollama.com), keep it running in the background.
2. Pull a model: `ollama run glm4:flash` (or Gemma 3B/34B).
3. Connect Claude Code: `ANTHROPIC_BASE_URL=http://localhost:11434 claude` — now Claude Code uses the local model.
4. (Optional) Point **OpenClaw** at the same Ollama endpoint in its gateway settings.
5. Verify with "What API are you running on?" → expects "running through Ollama with GLM 4.7 Flash."
FAQ: truly free (local = no token limits); not the real Claude API; GLM 4.7 Flash can write real code; works on Windows.
## Why It Matters
Concrete answer to the vault's standing token-economy concern (Claude Pro rate limits, [[Claude Pro Workflow]]): a **free local fallback for low-stakes coding** when the Claude quota is spent, at the cost of using a weaker model. This fits the "Zero-Cost AI Stack" plan folder and the anti-drift budget discipline — but the honest tradeoff is real: GLM 4.7 Flash is not Claude, so this is for cheap/bulk work, not the hard planning or vault-writing that needs the strong model. Note the `ANTHROPIC_BASE_URL` override is exactly the kind of setting the vault's own tooling assumes points at Anthropic — don't leave it set globally.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Claude Code Ollama Free Guide (1).pdf`
- [[10_Areas/AI/Claude Code|Claude Code]] — the tool this reconfigures
- [[Claude Pro Workflow]] — the rate-limit/token concern this addresses
## Open Questions
- [ ] Is a local-Ollama fallback worth setting up for low-stakes bulk coding, or does context-switching models cost more than it saves?
- [ ] What's GLM 4.7 Flash's real coding quality vs Haiku for the tasks Jarvis actually offloads?
## Flashcards
#cards/ai
How do you point Claude Code at a free local model?::Set `ANTHROPIC_BASE_URL=http://localhost:11434` when launching `claude`, with an Ollama model (e.g. GLM 4.7 Flash) running locally — the interface stays Claude Code's, the model becomes local.
What's the honest tradeoff of the Ollama-free setup?::It's free with no token limits, but **you're not using real Claude** — the local model (GLM 4.7 Flash) is weaker, so it fits cheap/bulk coding, not hard planning or quality writing.

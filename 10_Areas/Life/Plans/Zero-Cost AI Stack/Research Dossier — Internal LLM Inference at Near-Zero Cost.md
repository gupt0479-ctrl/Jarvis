---
type: research-dossier
status: complete
created: 2026-06-04
tags:
  - ai-infrastructure
  - llm-serving
  - self-hosting
  - tco
audience: engineer-grade
related:
  - "[[40_Resources/CS/Repos|Repos]]"
---

# Research Dossier — How Big Tech Runs Internal LLM Inference at Near-Zero Marginal Cost, and What a 15-40 Person Startup Can Actually Replicate on One ~24GB GPU

> Scope: This is an engineering study of *internal inference patterns*, not a product roundup. Every factual claim is traced to a primary source (engineering blog, peer-reviewed paper, official docs, GitHub, or named engineer). Claims that could only be traced to secondary/aggregator sources are tagged **[UNVERIFIED]**. Sources are 2024-2026 except where a foundational 2022-2023 paper is the primary.
>
> Hardware assumption for all sizing: **one already-owned ~24GB consumer GPU** (RTX 3090/4090-class), **hybrid APIs allowed**, **~15-40 mixed-workflow engineers** (autocomplete + chat + some agentic).

---

## 0. The single most important honest finding (read this first)

The original pitch deck claimed a self-hosted stack is "near-zero cost." **The rigorous evidence does not support that claim at 15-40 seats once you price even part-time maintenance labor.** The peer-reviewed and practitioner TCO literature is consistent: hardware + electricity is only **20-30%** of self-hosting TCO; **people are 70-80%** [18][41]. For your team size, the subscription you would replace (~$285-$1,560/mo) is usually *smaller* than the maintenance labor you add (~$1,500-$3,500/mo for 10-20% of one senior engineer) [18][41].

So the defensible thesis is **not** "do it for free." It is:

1. **Own the floor, rent the ceiling.** Self-host a strong open *coding* model for the high-volume, latency-sensitive work (autocomplete + bulk chat); route the hard/rare agentic work to cheap external APIs. This is the academically-grounded FrugalGPT/RouteLLM cascade — **up to 85% cost reduction while keeping ~95% of frontier quality** [21][25].
2. **The real wins are control and ceilings, not a zero on the invoice.** You eliminate per-seat fee scaling, eliminate token-limit walls (via caching + retrieval), and keep code on-prem for sensitive projects. The cash saving is real but bounded by the labor you add.
3. **Token limits are an engineering problem, not a plan-tier problem.** Prompt caching (~90% off repeated context) + selective code-retrieval (~40-70% fewer tokens at equal quality) make the token wall disappear without buying a bigger subscription [27][30][33][35].

Everything below is the evidence for those three claims.

---

## 1. Executive Summary (the corrected thesis, one citation each)

- **Big tech serves open-weight models on a small set of open engines — overwhelmingly vLLM — not on exotic single-GPU tricks.** vLLM is in production at Amazon (Rufus), Roblox, LinkedIn, Meta, Mistral, and IBM/Red Hat; Hugging Face moved its own TGI engine to *maintenance mode* in March 2026 and now points users to vLLM/SGLang/llama.cpp [29][36]. *(The deck's hero tool AirLLM — disk layer-streaming — is single-user and ~single-digit tok/s; it is an offline fallback, not a team serving engine.)*
- **The dominant cost pattern is tiered routing, not "one model for everything."** Microsoft Research's *Hybrid LLM* router cuts large-model calls up to 40% with no quality drop [20]; Berkeley/LMSYS *RouteLLM* keeps 95% of GPT-4 quality at up to 85% lower cost [25]; Stanford's *FrugalGPT* matched GPT-4 at ~98% lower cost on one benchmark via an escalation cascade [21].
- **Self-hosting is honestly NOT zero, and at 15-40 seats the pure cost case is close.** Hardware+power is 20-30% of TCO; labor is 70-80% [18]; for your scale, realistic self-hosting (~$2,000-$4,000/mo with part-time maintenance) can *exceed* Copilot Business ($285-$760/mo) — so the justification must lean on control, token-wall removal, and hybrid routing, not a fictional $0 [18][41][37].

---

## 2. Company-by-Company Evidence Table

| Company | Serving engine (primary source) | Accelerator | Models / quantization | Throughput / scale | Cost / savings figure | Primary source |
|---|---|---|---|---|---|---|
| **Meta** | vLLM (Llama 3.1 launch partner) + PyTorch-native (torchao, ExecuTorch) | NVIDIA GPUs + **MTIA 2i** ASIC (128GB LPDDR5, 90W) | Llama 3.1 up to **405B**, FP8; int4/int8 KV-cache via torchao | torchao: **97% speedup** Llama-3-8B inference; MTIA next-gen 2-3× prior gen | MTIA 2i: **-44% TCO vs GPUs** | [2][3][4][6] |
| **Google** | vLLM, extended by **llm-d** (founding contributor) | **TPU v5e/v5p/v6e** (+ GPU) | Gemini (sizes undisclosed); AlphaCode 2 = fine-tuned **Gemini Pro** | AlphaCode 2: ~1M samples/problem, 85th percentile | "Speculative cascades" = better cost/quality; AlphaCode 2 "too costly to operate at scale" | [10][11][12][15] |
| **Microsoft / GitHub** | Copilot **`copilot-proxy`** → models in Azure OpenAI tenant (+ AWS/Anthropic/GCP routing) | Azure NVIDIA GPU; Phi targets edge via ONNX | **Phi-3** mini 3.8B / small 7B / medium 14B; Copilot MAI-Code-1-Flash | Copilot: **>400M completions/day**, ~8,000 req/s peak, **<200ms** mean | *Hybrid LLM* router: **up to 40% fewer large-model calls, no quality drop** | [16][17][18-msr][20] |
| **Amazon / AWS (Rufus)** | **NVIDIA Triton + vLLM (Neuron SDK)**, leader/follower multi-node | **>80,000 Inferentia + Trainium** chips | Multi-billion-param LLM (size undisclosed) | **~3M tokens/min**, **P99 < 1s**; parallel decode 2× speed | **4.5× lower cost** vs evaluated alts; Bedrock routing **up to -30%** | [21-aws][22-aws][23-aws] |
| **Apple** | On-device ↔ server routing on **Private Cloud Compute** | **Apple silicon** (device + servers) | **AFM-on-device ~3B @ 2-bit QAT**; **AFM-server PT-MoE @ 3.56 bpw** | Latency framed qualitatively; tok/s **[UNVERIFIED]** | No $ figures; benefit framed as efficiency + privacy | [24][25-apple][26] |
| **Stripe** | Payments Foundation Model (transformer) + lightweight classifiers; text-decoder variant for explanations | Not disclosed **[UNVERIFIED]** | Self-supervised on tens of billions of transactions; param count undisclosed | **~50,000 transactions/min** across network | Card-testing detection **59% → 97%** overnight, no FP increase | [27][28] |
| **Roblox** | **vLLM** (primary engine; contributes multimodal support) | "1000+ GPUs" hybrid cloud; GPU model **[UNVERIFIED]** | Multimodal; sizes/quant **[UNVERIFIED]** | **~4 billion tokens/week**; ~2× latency+throughput from vLLM | No $; gain = ~2× efficiency + open-source | [29] |
| **Shopify** | **Aquifer** internal agent platform; centralized **internal LLM proxy** → OpenAI/Anthropic/Google | Routes to external providers (not self-hosting frontier) | Sidekick assistant; sizes **[UNVERIFIED]** | Productivity measured by "what ships," not tok/s | Proxy justified by standardization/failover, no $ figure | [30][31][32] |
| *Uber (bonus)* | **GenAI Gateway** (Go service in Michelangelo) mirroring OpenAI API; fronts external + Uber-hosted | Not named **[UNVERIFIED]** | Uber-hosted models on "STOA inference libraries" | ~60 use cases, ~30 teams, **16M queries/mo** (2024) | No published $ | [33] |
| *Coinbase (bonus)* | **CB-GPT** unified platform; multi-provider **+ self-hosted LLaMa/Mistral**; cost-aware model selection | Not disclosed **[UNVERIFIED]** | LLaMa/Mistral self-hosted + Azure/GCP/Anthropic | — | 2 automations save **25+ hrs/wk**; build time 12+ wks → <1 wk | [34][35-cb] |

**Pattern across all 8+2:** (a) the serving engine is almost always **vLLM** (or a vLLM-based distributed stack like llm-d / Triton+vLLM); (b) everyone runs a **gateway/proxy** in front (copilot-proxy, GenAI Gateway, CB-GPT, Shopify's LLM proxy) for keys/routing/observability; (c) the cost lever is **custom silicon + routing + quantization**, not a single magic model. A startup cannot copy the silicon, but it *can* copy the engine (vLLM), the gateway (LiteLLM), and the routing (FrugalGPT/RouteLLM) exactly.

**[UNVERIFIED] flags:** Meta "iLlama" model name and the "50% of diffs" DevMate stat (only third-party/vendor sources); Gemini Code Assist serving infra; Amazon Q Developer backend; Roblox GPU model + model sizes; Stripe/Shopify/Coinbase accelerators and parameter counts.

---

## 3. The Routing & Batching Pattern — Academic Foundations

Five papers (plus the PagedAttention bonus) that formalize the entire thesis. Each row: the key finding for *this* pitch and one hard number from the paper.

### 3.1 FrugalGPT — the cost-cascade foundation
- **Title / authors / venue:** *FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance* — Lingjiao Chen, Matei Zaharia, James Zou (Stanford) — arXiv:2305.05176 (2023); TMLR 2024.
- **Finding:** An **LLM cascade** scores a cheap model's answer and escalates to a more expensive model only on low confidence — the canonical "own-the-floor / rent-the-ceiling" mechanism.
- **Hard number:** On the HEADLINES dataset, **matches GPT-4 at ~98.3% lower cost** ($33.10 → $0.60); 50-98% savings across datasets. ✅ verified in abstract + TMLR PDF. [21]

### 3.2 Orca — iteration-level (continuous) batching
- **Title / authors / venue:** *Orca: A Distributed Serving System for Transformer-Based Generative Models* — Gyeong-In Yu et al. (SNU / FriendliAI) — OSDI 2022.
- **Finding:** Iteration-level scheduling + selective batching — the scheduling foundation every modern server (incl. vLLM) builds on. Lets finished requests exit and new ones join without draining the batch.
- **Hard number:** On GPT-3 175B, **36.9× throughput vs FasterTransformer at the same latency** (0.185 → 6.81 req/s). ✅ verified in USENIX OSDI'22 PDF. [22]

### 3.3 Sarathi-Serve — chunked prefill / stall-free scheduling
- **Title / authors / venue:** *Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve* — Amey Agrawal et al. (Georgia Tech + **Microsoft Research India**) — OSDI 2024; arXiv:2403.02310.
- **Finding:** Splits prompts into compute-sized chunks and coalesces decodes with prefill so new requests don't stall ongoing generation — directly relevant to keeping a single GPU responsive under team load.
- **Hard number:** **2.6× serving capacity for Mistral-7B on one A100**; up to **5.6×** for Falcon-180B with pipeline parallelism, under tail-latency SLOs vs vLLM. [23]

### 3.4 Splitwise — prefill/decode disaggregation
- **Title / authors / venue:** *Splitwise: Efficient Generative LLM Inference Using Phase Splitting* — Pratyush Patel et al. (**Microsoft / MSR**) — ISCA 2024; arXiv:2311.18677.
- **Finding:** Prefill is compute-bound, decode is memory-bound; decode can run on cheaper hardware. Reveals Microsoft treats serving as a *heterogeneous, cost/power-optimized fleet* problem — the precursor to today's PD-disaggregation.
- **Hard number:** **2.35× more throughput at the same cost and power**, or 1.4× throughput at 20% lower cost (Llama-70B, production traces). [24]

### 3.5 RouteLLM — learned strong/weak routing
- **Title / authors / venue:** *RouteLLM: Learning to Route LLMs with Preference Data* — Isaac Ong et al. (UC Berkeley / **LMSYS**) — 2024; arXiv:2406.18665.
- **Finding:** A binary router trained on Chatbot Arena preferences sends easy queries to a weak/cheap model and hard ones to a strong model — drop-in OpenAI-compatible. This is the production-ready version of the cascade.
- **Hard number:** **>85% cost reduction on MT-Bench while keeping 95% of GPT-4 quality** (95% quality at only 14% GPT-4 calls after LLM-judge augmentation). [25]

### 3.6 (Bonus) PagedAttention / vLLM — KV-cache memory management
- **Title / authors / venue:** *Efficient Memory Management for LLM Serving with PagedAttention* — Woosuk Kwon et al. (UC Berkeley et al.) — SOSP 2023; arXiv:2309.06180.
- **Finding:** OS-style paging of the KV cache cuts memory waste from 60-80% to **<4%**, enabling far more concurrent sequences per GPU — the reason vLLM can serve a whole team off one card.
- **Hard number:** **2-4× higher throughput than FasterTransformer and Orca at the same latency**; <4% KV-cache waste. [26]

> Note on the brief: the prominent *speculative cascades* / cascade-via-speculative-decoding line is **Google Research's** [15], while *Sarathi-Serve* and *Splitwise* are the **Microsoft** serving papers [23][24].

---

## 4. Model Selection Matrix for a 24GB GPU (mid-2026)

GGUF sizes are weights-on-disk (≈ minimum VRAM for weights); real VRAM needs KV cache + activations (+1-3GB depending on context). **tok/s are bandwidth-bounded single-stream estimates, not single-source benchmarks — flagged [EST].**

| Model | VRAM @ Q4_K_M | VRAM @ Q8_0 | Est. tok/s on 24GB | Coding score | License | Recommended use case | Source |
|---|---|---|---|---|---|---|---|
| **Qwen2.5-Coder-32B-Instruct** (dense) | ~19.9GB (tight) | ~34.8GB | ~25-40 [EST] | HumanEval ~92%*; SOTA-open EvalPlus/LiveCodeBench/BigCodeBench; Aider 73.7 | Apache-2.0 | Highest-quality local coder; keep ctx ≤8K at Q4 | [5][6] |
| **Qwen3-Coder-30B-A3B** (MoE, 3.3B active) | ~18.6GB | ~32.5GB | ~40-70 [EST] | SWE-bench Verified ~51.6%* | Apache-2.0 | **Best default**: agentic coding + tool calls, 256K ctx, fast decode | [9][11] |
| **Devstral-Small-2507** (dense 24B) | ~14.3GB | ~25.0GB | ~30-45 [EST] | **SWE-bench Verified 53.6%** (#1 open) | Apache-2.0 | Best open SWE-agent / multi-file editing; big ctx headroom | [13][15] |
| **DeepSeek-Coder-V2-Lite** (MoE, 2.4B active) | ~10.4GB | ~16.7GB | ~50-80 [EST] | HumanEval 81.1 / LiveCodeBench 24.3 / MBPP+ 68.8 | MIT + DeepSeek license (commercial OK) | Budget/low-VRAM coder; run Q8 + near-full 128K ctx | [19][20] |
| **CodeLlama-34B-Instruct** (dense, baseline) | ~20.2GB (v. tight) | ~35.9GB | ~20-35 [EST] | HumanEval 53.7 / MBPP 56.2 | Llama 2 Community | Legacy baseline only — superseded | [21-cl][22-cl] |
| **Qwen3-14B** (dense, general) | ~9.0GB | ~15.7GB | ~45-70 [EST] | General reasoning (hybrid thinking); no official code table | Apache-2.0 | Fast general chat/reasoning companion to a coder | [24-q][25-q] |

\* Community/aggregator figures citing official evals; Qwen's *official* sources assert leaderboard leadership / Aider 73.7 rather than the exact integer — treat starred numbers as **[partially UNVERIFIED]**.

**Recommended fit for one 24GB card:**
- **Autocomplete (FIM hot path):** `Qwen2.5-Coder-1.5B` or `3B` (Continue's default), or Codestral. Must be FIM-trained; "most SOTA autocomplete models are ≤10B params" per Continue docs [28].
- **Workhorse chat/edit:** **Qwen3-Coder-30B-A3B** (fast MoE decode, big context) or **Devstral-Small-2507** (best open SWE-bench, lots of headroom). Qwen2.5-Coder-32B is the quality leader but tight on context at Q4.
- **General reasoning companion:** Qwen3-14B at Q8.
- **Hard/agentic ceiling:** route to API (Section 6's quality gap explains why).

**Hardware-fit tooling (both in your `Repos.md`):** `llmfit` (Rust; `llmfit --memory=24G`, MoE-aware, JSON output) [1] and `whichllm` (Python; recency-weighted benchmark ranking) [3] both confirm the 14-32B-at-Q4 sweet spot. The `whichllm` top pick string "Qwen3.6-27B" and the site "localmaxxing.com" could **not** be independently verified — **[UNVERIFIED]**.

**Coding Pareto frontier:** the frontier shifted down-and-left since CodeLlama. A 2024-25-gen **24-32B** model now reaches **~90% HumanEval / ~50-54% SWE-bench Verified**, vs the 2023 34B CodeLlama at **~54% HumanEval / single-digit SWE-bench**. The biggest efficiency move is **MoE** (30B-A3B, 16B-Lite): near-dense accuracy at 2.4-3.3B active params.

---

## 5. Honest TCO Table

Scope: ONE already-owned ~24GB GPU (RTX 4090 assumed) serving the team via vLLM + cheap API overflow. Labor is the swing factor (10-20% of one senior eng ≈ $1,500-$3,500/mo at ~$180k loaded) [18][41].

### Subscriptions you would replace (verified 2026 pricing)
| Plan | 15 devs /mo | 15 /yr | 40 devs /mo | 40 /yr | Source |
|---|---|---|---|---|---|
| GitHub Copilot Business ($19) | $285 | $3,420 | $760 | $9,120 | [42][43] |
| GitHub Copilot Enterprise ($39 plan-only) | $585 | $7,020 | $1,560 | $18,720 | [42][43] |
| Copilot Enterprise ($60 incl. required GH Enterprise Cloud +$21) | $900 | $10,800 | $2,400 | $28,800 | [42][43] |
| Cursor Business ($40 monthly / $32 annual) | $480-600 | $5,760-7,200 | $1,280-1,600 | $15,360-19,200 | [44] |

### Self-hosted stack (1× 24GB GPU) — realistic, labor priced
| Line item | 15 devs | 40 devs | Source |
|---|---|---|---|
| GPU CapEx (already owned) | $0 incremental | $0 incremental | brief |
| GPU replacement reserve (~$1,800 / 36mo) | ~$50/mo | ~$50/mo | [40] |
| Electricity (4090 24/7, incl. ~1.4 PUE) | ~$60-90/mo | ~$60-90/mo | [38][39] |
| API overflow budget | ~$200/mo | ~$200-400/mo | §6, [45][46] |
| Monitoring/tooling | ~$200/mo | ~$200/mo | [37] |
| **Part-time maintenance (10-20% senior eng)** | **$1,500-3,500/mo** | **$1,500-3,500/mo** | [18][37] |
| **Realistic total** | **≈ $2,010-4,040/mo** | **≈ $2,010-4,240/mo** | — |
| *If maintenance treated as $0 (founder nights/weekends)* | *≈ $510-540/mo* | *≈ $510-740/mo* | [47] |

### Electricity math (shown explicitly)
Monthly kWh = (TDP_W / 1000) × 24 × 30. At EIA commercial **$0.1392/kWh** (Mar 2026) [38]:
- RTX 4090 (450W): 324 kWh → **$45.10/mo** (GPU-only); ~$60-90 with host + PUE 1.4.
- RTX 3090 (350W): 252 kWh → **$35.08/mo**. A6000 (300W): **$30.07**. A5000 (230W): **$23.05**.

### API overflow break-points ($200/mo budget, 15 devs, ~22 working days)
Assumptions: light agent req = 3,000 in + 700 out; heavy = 15,000 in + 2,000 out. DeepSeek V3.2 ≈ $0.28/$0.42 per 1M (note `deepseek-chat` now routes to **V4-Flash at $0.14/$0.28**, i.e. cheaper) [45][46]; Qwen3-32B ≈ $0.08/$0.28 [46-q].
- DeepSeek light: **~176,000 req/mo ≈ 534 req/dev/day**. DeepSeek heavy: ~39,700 req/mo ≈ 120/dev/day.
- Qwen3-32B light: **~459,000 req/mo ≈ 1,390 req/dev/day**.
- **Conclusion:** $200/mo of *overflow* (only the hard tasks the GPU can't handle) comfortably covers a 15-dev team if local serving absorbs the bulk.

### Bottom line (honest)
- **Self-hosting is not zero.** Even with a free GPU you pay electricity + overflow + monitoring + the labor to keep vLLM/CUDA/models alive [18][37].
- **At 15 devs**, Copilot Business ($285/mo) is **cheaper than** realistic self-hosting ($2,000-4,000/mo) once you count 10-20% of one engineer. Self-hosting only wins on cost if maintenance is genuinely **$0** — which is exactly the unpriced assumption behind viral "96% savings" case studies [47].
- **At 40 devs**, Copilot Business ($760/mo) still beats realistic self-hosting; Cursor annual ($1,280/mo) reaches the low end of the self-host range. The subscription replaced is usually *smaller* than the labor added.
- **Where self-hosting genuinely wins:** (a) data-residency/compliance, (b) you already employ ML/infra staff at ~$0 marginal cost, (c) you keep maintenance minimal *and* stay inside the single-GPU concurrency envelope, or (d) a thin **hybrid** (cheap API routing + local for bulk completions) where the local GPU offloads enough volume to keep the API bill tiny while removing per-seat scaling and token walls [2-tco][37][18].

### Break-even literature (for context)
- **Wang 2025** (arXiv:2509.18101): small models break even in **0.3-3 months** — but the model contains **only CapEx + electricity, no labor term** (authors defer staffing to future work). The "CMU" attribution is **[UNVERIFIED]**. [48]
- **digitalapplied 2026 TCO** (includes one FTE engineer): break-even **~600M tok/mo (code), ~1.2B tok/mo (chat)** [2-tco].
- The widely-cited **"~11B tokens/month"** break-even traces to a **vendor blog (Braincuber)**, not a peer-reviewed source, and is specific to a 70B cloud-GPU deployment — **does not apply** to a small model on an owned 24GB GPU [37]. Published break-evens span four orders of magnitude (5M → 24.9B tok/mo) purely from differing labor/utilization/routing assumptions.

---

## 6. Token Engineering Toolkit (the token-limit fix)

| Technique | What it does | Token / cost reduction | Tool / paper | Complexity (1-5) | Source |
|---|---|---|---|---|---|
| **Anthropic prompt caching** | Caches a stable prefix; reuse via `cache_control` | **~90% off cached input** (read 0.1×); write +25% (5-min) / +100% (1-hr); min 1,024 tok | Anthropic docs | 2 | [27] |
| **OpenAI prompt caching** | Auto-reuses recently-seen prefixes | **50% (gpt-4o) → up to 90% (newer)** off cached input; ≥1,024 tok | OpenAI docs | 1 (automatic) | [28-oa] |
| **Gemini context caching** | Implicit (auto) + explicit (`CachedContent` + TTL) | **90% (2.5+) / 75% (2.0)** off cached; explicit adds storage fee | Vertex/Gemini docs | 1 implicit / 3 explicit | [29-g] |
| **Continue `@codebase` RAG** | Embed + keyword retrieve top-k chunks vs whole repo | Sends ~5 chunks (`nFinal`) instead of full files — large reduction | Continue docs | 2 | [30][31] |
| **Selective RAG (Repoformer)** | Model self-decides when to retrieve | **Up to ~70% latency/compute savings at equal accuracy**; 3B ≈ always-retrieve 16B | Repoformer, Wu et al., ICML 2024 | 4 | [32] |
| **Zilliz `claude-context` (MCP)** | Hybrid BM25+dense semantic code search over Milvus | **~40% token reduction (39.4%) + 36% fewer tool calls** at equal retrieval quality | zilliztech/claude-context | 2-3 | [33][34-z] |
| **vLLM Automatic Prefix Caching** | Reuses KV cache for shared prefixes (self-host) | **5-10× TTFT (prefill) reduction; ~2-5× throughput** on shared prefixes (no decode gain) | vLLM APC docs | 1 (`enable_prefix_caching=True`) | [35] |

**Why this kills the token wall:** the deck blamed token limits on subscription tiers. The real cause is dumping whole codebases into context. Anthropic's docs show **~90% cheaper** repeated context [27]; Repoformer shows retrieval **matches full-repo stuffing at ~70% lower budget** and lets a 3B model rival a 16B one [32]; Zilliz's controlled eval shows **~40% fewer tokens + 36% fewer tool calls** [33]. None of these require a bigger plan.

---

## 7. Risk Register (documented failure modes)

| # | Risk | Description | Evidence | Mitigation |
|---|---|---|---|---|
| 1 | **Hidden labor dominates TCO** | Hardware+power = 20-30% of cost; people = 70-80%. 20-30% of a senior eng = $3-6k/mo. | [18] | Price labor before building; start API-first; self-host only at a written volume threshold. |
| 2 | **Volume mis-sizing → costly reversal** | Teams over/under-estimate volume by 2 orders of magnitude and migrate back; one team now pays "$80k/mo on API for a workload one A100 could handle." | [49][37] | Instrument every request (tokens/latency); spend alerts at 80% from day 1; decide on data. |
| 3 | **Naive stack collapses under team load** | On one RTX 4090, **Ollama collapses at 5 concurrent users**; p95 **18.4s @ 50 users** (vLLM 2.1s); queue fails at 128 connections. | [50] | Use **vLLM** (continuous batching/PagedAttention), not Ollama, for multi-user serving. |
| 4 | **Continue.dev FIM breaks through LiteLLM** | FIM via LiteLLM→Ollama returns instruct-style text, not completions; direct-to-Ollama works. Issue **#6900** is **CLOSED** as a config/feature gap. | [51] | Point Continue's autocomplete provider **directly at Ollama/vLLM**; or use `text-completion-codestral/` pass-through to `/fim/completions`; route only chat/agentic through LiteLLM. PR #18467 (Jan 2026) fixed codestral chat-vs-FIM routing. |
| 5 | **Open-model quality gap on hard coding** | Best open (DeepSeek V4-Pro **80.6%** SWE-bench Verified) trails best closed (**93.9%**) by ~13 pts and top production closed (Opus/GPT-5.5 ~87-89%) by ~7-8 pts. *Models that fit 24GB trail further.* | [52][53][54] | Hybrid routing: local for bulk completions, route hard/agentic tasks to API (cascade per §3). |
| 6 | **30B-on-24GB concurrency ceiling** | Quantized 30B leaves only ~6-8GB for KV cache; on exhaustion vLLM preempts + recomputes, so a few long-context coding requests *can* exceed 5s TTFT. (8B on 4090 holds p99 ≈ 2.4s up to 64 streams.) | [55][56] | Prefer 8-14B for interactivity; tune `max_num_seqs`/chunked-prefill/`gpu_memory_utilization`; cap context; size for peak. |
| 7 | **Model-update + CUDA/driver treadmill** | 1-3 eng-days per significant model upgrade + 8-20 hrs/mo steady-state; FlashAttention/xformers must match CUDA or silent perf loss; OWASP-LLM patching. | [18][57] | Pin/containerize the stack; scheduled upgrade windows; subscribe to CVE/OWASP-LLM advisories. |
| 8 | **Single GPU = single point of failure** | One owned GPU has no redundancy; an outage blocks the whole team. | [37][58] | Keep an automatic API fallback behind one interface (router/feature-flag) so a GPU outage degrades, not stops. |
| 9 | **Gateway = credential blast radius** | LiteLLM centralizes provider keys; the **March 24 2026 PyPI supply-chain incident** (malicious litellm 1.82.7/1.82.8 exfiltrated env vars, cloud/IAM creds, K8s tokens) shows the risk. Official Docker users were unaffected. | [59] | Pin versions / use the official `ghcr.io/berriai/litellm` image (not `latest`); rotate creds if installed in-window; scope per-dev virtual keys. |

---

## 8. Full Citation List

*Primary sources unless marked (secondary) or [UNVERIFIED]. Accessed June 2026.*

**Company stacks (Section 2)**
1. vLLM repo — https://github.com/vllm-project/vllm
2. "Announcing Llama 3.1 Support in vLLM," vLLM Blog, 2024-07-23 — https://blog.vllm.ai/2024/07/23/llama31.html
3. "Four MTIA Chips in Two Years," Meta AI blog, 2025/26 — https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
4. "Meta's Second Generation AI Chip" (MTIA 2i, -44% TCO), ISCA'25 — https://aisystemcodesign.github.io/papers/MTIA-ISCA25.pdf
5. "PyTorch Native Architecture Optimization: torchao," PyTorch/Meta blog, 2024 — https://pytorch.org/blog/pytorch-native-architecture-optimization/
6. "TorchAO: A PyTorch-Native Training-to-Serving Optimization Framework," arXiv:2507.16099 — https://arxiv.org/pdf/2507.16099
7. llm-d repo — https://github.com/llm-d/llm-d
8. "Enhancing vLLM for distributed inference with llm-d," Google Cloud Blog — https://cloud.google.com/blog/products/ai-machine-learning/enhancing-vllm-for-distributed-inference-with-llm-d
9. "AlphaCode 2 Technical Report," Google DeepMind, 2023 — https://storage.googleapis.com/deepmind-media/AlphaCode2/AlphaCode2_Tech_Report.pdf
10. "Speculative cascades," Google Research Blog — https://research.google/blog/speculative-cascades-a-hybrid-approach-for-smarter-faster-llm-inference/
11. "How GitHub Copilot Serves 400M Completion Requests a Day," David Cheney, InfoQ — https://www.infoq.com/presentations/github-copilot/
12. "Hosting of models for GitHub Copilot," GitHub Docs — https://docs.github.com/en/copilot/reference/ai-models/model-hosting
13. "Phi-3 Technical Report," Microsoft Research — https://www.microsoft.com/en-us/research/publication/phi-3-technical-report-a-highly-capable-language-model-locally-on-your-phone/
14. "Introducing Phi-3," Microsoft Azure Blog — https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/
15. "Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing," Ding et al., MSR, ICLR 2024 — https://www.microsoft.com/en-us/research/publication/hybrid-llm-cost-efficient-and-quality-aware-query-routing/ (arXiv:2404.14618)
16. "Scaling Rufus with 80,000+ Inferentia/Trainium chips," AWS ML Blog — https://aws.amazon.com/blogs/machine-learning/scaling-rufus-the-amazon-generative-ai-powered-conversational-shopping-assistant-with-over-80000-aws-inferentia-and-aws-trainium-chips-for-prime-day/
17. "How Amazon scaled Rufus … multi-node vLLM on Trainium," AWS ML Blog — https://aws.amazon.com/blogs/machine-learning/how-amazon-scaled-rufus-by-building-multi-node-inference-using-aws-trainium-chips-and-vllm/
18. "Bedrock Intelligent Prompt Routing + prompt caching," AWS News Blog, 2024 — https://aws.amazon.com/blogs/aws/reduce-costs-and-latency-with-amazon-bedrock-intelligent-prompt-routing-and-prompt-caching-preview/
19. "Apple Intelligence Foundation Language Models Tech Report 2025," Apple ML Research (arXiv:2507.13575) — https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025
20. "Introducing Apple's On-Device and Server Foundation Models," Apple ML Research, 2024-06-10 — https://machinelearning.apple.com/research/introducing-apple-foundation-models
21. "Private Cloud Compute," Apple Security Research, 2024-06 — https://security.apple.com/blog/private-cloud-compute/
22. "Using AI to optimize payments performance (Payments Intelligence Suite)," Stripe Blog (59%→97%) — https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite
23. Gautam Kedia (Stripe ML), payments foundation model, LinkedIn — https://www.linkedin.com/posts/gautam-kedia-8a275730_tldr-we-built-a-transformer-based-payments-activity-7325973745292980224-vCPR
24. "Running AI Inference at Scale in the Hybrid Cloud," Roblox Newsroom, 2024-09-17 (~4B tokens/wk; vLLM) — https://about.roblox.com/newsroom/2024/09/running-ai-inference-at-scale-in-the-hybrid-cloud
25. "Under the River" (Aquifer), Shopify Engineering, 2026 — https://shopify.engineering/under-the-river
26. "Introducing Roast," Shopify Engineering, 2025 — https://shopify.engineering/introducing-roast
27. "From Memo to Movement: Shopify's Cultural Adoption of AI," First Round (Farhan Thawar; internal LLM proxy) (secondary) — https://www.firstround.com/ai/shopify
28. "Navigating the LLM Landscape: Uber's GenAI Gateway," Uber Engineering, 2024-07-11 — https://www.uber.com/us/en/blog/genai-gateway/
29. "CB-GPT: the opportunity and vision for GenAI at Coinbase," Coinbase Blog, 2024-08-06 — https://www.coinbase.com/blog/cb-gpt-the-opportunity-and-the-vision-for-genAI-at-coinbase
30. "Building enterprise AI agents at Coinbase," Coinbase Blog — https://www.coinbase.com/blog/building-enterprise-ai-agents-at-coinbase

**Routing & batching papers (Section 3)**
31. FrugalGPT, Chen/Zaharia/Zou (Stanford), arXiv:2305.05176 — https://arxiv.org/abs/2305.05176
32. Orca, Yu et al., OSDI 2022 — https://www.usenix.org/system/files/osdi22-yu.pdf
33. Sarathi-Serve, Agrawal et al. (GT/MSR India), OSDI 2024, arXiv:2403.02310 — https://www.usenix.org/conference/osdi24/presentation/agrawal
34. Splitwise, Patel et al. (MSR), ISCA 2024, arXiv:2311.18677 — https://www.microsoft.com/en-us/research/publication/splitwise-efficient-generative-llm-inference-using-phase-splitting/
35. RouteLLM, Ong et al. (Berkeley/LMSYS), arXiv:2406.18665 — https://lmsys.org/blog/2024-07-01-routellm/
36. PagedAttention, Kwon et al., SOSP 2023, arXiv:2309.06180 — https://arxiv.org/abs/2309.06180

**Models for 24GB (Section 4)**
37. llmfit repo — https://github.com/AlexsJones/llmfit
38. whichllm repo — https://github.com/Andyyyy64/whichllm
39. Qwen2.5-Coder-32B GGUF (Unsloth) — https://huggingface.co/unsloth/Qwen2.5-Coder-32B-Instruct-GGUF
40. "Qwen2.5-Coder Series," Qwen Team blog, 2024-11 — https://qwenlm.github.io/blog/qwen2.5-coder-family/
41. Qwen3-Coder-30B-A3B GGUF (Unsloth) — https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF
42. Qwen3-Coder-30B-A3B official card — https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct
43. Devstral-Small-2507 GGUF (bartowski) — https://huggingface.co/bartowski/mistralai_Devstral-Small-2507-GGUF
44. Devstral-Small-2507 official card (SWE-bench 53.6%) — https://huggingface.co/mistralai/Devstral-Small-2507 ; https://mistral.ai/news/devstral-2507
45. DeepSeek-Coder-V2-Lite card + paper (arXiv:2406.11931) — https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct
46. Code Llama paper, Rozière et al., Meta, 2023, arXiv:2308.12950 — https://arxiv.org/html/2308.12950
47. Qwen3-14B GGUF official card — https://huggingface.co/Qwen/Qwen3-14B-GGUF
48. "A new Tab model" (Cursor Fusion), Cursor blog, 2025-01 — https://cursor.com/blog/tab-update

**TCO (Section 5)**
49. Pan/Chodnekar/Roy/Wang, "On-Premise LLM Deployment Cost-Benefit," arXiv:2509.18101 (CapEx+electricity only) — https://arxiv.org/html/2509.18101v3
50. digitalapplied, "Self-Hosting Frontier AI Models: 2026 TCO Analysis" — https://www.digitalapplied.com/blog/self-host-frontier-models-tco-analysis-2026
51. Braincuber, "Self-Hosted LLM vs API break-even" (source of "~11B/mo") (secondary/vendor) — https://www.braincuber.com/blog/self-hosted-llms-vs-api-based-llms-cost-performance-analysis
52. NeuralRouting.io, "When Is Self-Hosting Cheaper… 2026" — https://neuralrouting.io/blog/self-hosting-llm-vs-api-break-even-2026
53. Tian Pan, "Build-vs-Buy LLM Infrastructure," 2026-04-15 — https://tianpan.co/blog/2026-04-15-build-vs-buy-llm-infrastructure
54. NVIDIA RTX 4090 spec (TGP 450W) — https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/
55. U.S. EIA Electric Power Monthly, Tables 5.3 / 5.6.A — https://www.eia.gov/electricity/monthly/epm_table_grapher.cfm?t=epmt_5_3
56. GitHub Copilot pricing 2026 (Business $19 / Enterprise $39 + $21) (secondary) — https://githubcopilotpricing.com/
57. Cursor/Copilot Teams pricing, Pondero, 2026-06 (secondary) — https://pondero.ai/coding/guides/cursor-vs-copilot-teams-pricing-june-2026/
58. DeepSeek V3.2 pricing, TokenCost — https://tokencost.app/models/deepseek-v3-2-chat
59. DeepSeek `deepseek-chat` → V4-Flash $0.14/$0.28, state-of-llm-apis — https://github.com/janwilmake/state-of-llm-apis/blob/main/models/deepseek.md
60. Qwen3-32B pricing, modelcompare/RentGPU — https://modelcompare.dev/models/alibaba/qwen3-32b
61. Rituraj Pokhriyal, "We Replaced OpenAI with Ollama… Real Numbers" (labor unpriced) (secondary) — https://medium.com/@riturajpokhriyal/we-replaced-openai-with-ollama-for-half-our-workloads-here-are-the-real-numbers-36a4379bdd08

**Token engineering (Section 6)**
62. Anthropic Prompt Caching docs — https://platform.claude.com/docs/en/build-with-claude/prompt-caching
63. OpenAI Prompt Caching guide — https://developers.openai.com/api/docs/guides/prompt-caching
64. Vertex AI / Gemini context caching — https://cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview ; https://ai.google.dev/gemini-api/docs/caching
65. Continue embeddings + custom code RAG docs — https://docs.continue.dev/customize/model-roles/embeddings ; https://docs.continue.dev/reference/deprecated-codebase
66. Repoformer, Wu et al., ICML 2024, arXiv:2403.10059 — https://arxiv.org/pdf/2403.10059
67. RepoCoder, Zhang et al., EMNLP 2023, arXiv:2303.12570 — https://arxiv.org/html/2303.12570v3
68. Zilliz "Claude Context" MCP repo — https://github.com/zilliztech/claude-context ; https://milvus.io/blog/claude-context-reduce-claude-code-token-usage.md
69. vLLM Automatic Prefix Caching docs — https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/

**Tools + risks (Sections 7-8)**
70. Continue autocomplete docs (FIM; <10B; Codestral/qwen2.5-coder:1.5b) — https://docs.continue.dev/customize/deep-dives/autocomplete/
71. LiteLLM issue #6900 (CLOSED; FIM-through-proxy) — https://github.com/BerriAI/litellm/issues/6900 ; Continue issue #4542 — https://github.com/continuedev/continue/issues/4542 ; PR #18467 — https://github.com/BerriAI/litellm/pull/18467
72. Red Hat, "vLLM or llama.cpp," 2025-09-30 (>35× RPS vs llama.cpp) — https://developers.redhat.com/articles/2025/09/30/vllm-or-llamacpp-choosing-right-llm-inference-engine-your-use-case
73. "Comparative Analysis: vLLM and HF TGI," arXiv:2511.17593 (up to 24× over TGI) — https://arxiv.org/html/2511.17593v1
74. Bizon, "Best LLM inference engine 2026" (TGI maintenance-mode 2026-03-21) — https://bizon-tech.com/blog/best-llm-inference-engines
75. LinkedIn vLLM case study (ZenML LLMOps DB) — https://www.zenml.io/llmops-database/scaling-genai-applications-with-vllm-for-high-throughput-llm-serving
76. LiteLLM security update March 2026 (supply-chain) — https://docs.litellm.ai/blog/security-update-march-2026 ; NetSPI writeup — https://www.netspi.com/blog/executive-blog/ai-ml-pentesting/litellm-supply-chain-compromise/
77. LiteLLM production best practices — https://docs.litellm.ai/docs/proxy/prod
78. Open WebUI v0.9.6 release + RBAC docs — https://github.com/open-webui/open-webui/releases/tag/v0.9.6
79. Dify vector-DB integration (VectorFactory, 23+ stores) — https://deepwiki.com/langgenius/dify/4.4-vector-database-integration-architecture
80. Ollama-vs-vLLM concurrency test (Ollama collapses @5 users; p95 18.4s @50) (secondary) — https://pub.towardsai.net/i-tested-ollama-vs-vllm-vs-llama-cpp-the-easiest-one-collapses-at-5-concurrent-users-d4f8e0e84886
81. RTX 4090 8B vLLM TTFT-by-concurrency bench (secondary) — https://gigagpu.com/rtx-4090-24gb-llama-3-8b-benchmark/
82. vLLM Optimization & Tuning docs (KV cache, preemption, max_num_seqs) — https://docs.vllm.ai/en/stable/configuration/optimization/
83. SWE-bench leaderboards (open vs closed gap): BenchLM — https://benchlm.ai/benchmarks/sweVerified ; vals.ai — https://vals.ai/benchmarks/swebench ; marc0.dev — https://www.marc0.dev/en/leaderboard
84. Telnyx, "Why Self-Hosting LLMs Fails" (secondary) — https://telnyx.com/resources/why-self-hosting-llms-fails
85. "War Story: HF Inference API → Self-Hosted vLLM, -60% latency / -78% spend" (secondary) — https://dev.to/johalputt/war-story-we-migrated-from-hugging-face-inference-api-to-self-hosted-llms-and-cut-latency-by-60-kjb

---

## Appendix A — Corrections to the original "AI Stack" deck

| Deck claim | Reality | Fix for the pitch |
|---|---|---|
| "Zero subscriptions, zero cost" | Self-hosting is 70-80% labor; at 15-40 seats it can exceed Copilot Business [18][49] | Reframe as TCO + control + no per-seat scaling; show honest table (§5) |
| AirLLM "70B on 4GB" as a team tool | Single-user, disk layer-streaming, single-digit tok/s | Demote to offline/overflow fallback only; lead with vLLM |
| "Llama 3.3 70B" on the office GPU | Does not fit 24GB cleanly | Swap to Qwen3-Coder-30B-A3B / Devstral-Small-2507 / Qwen2.5-Coder-32B (§4) |
| RAG is the token-limit fix | RAG + **prompt caching** + selective retrieval together; caching is the biggest single lever (~90%) [27] | Add a caching slide; cite Repoformer/Zilliz numbers |
| One GPU serves everyone | Single 24GB GPU has a hard concurrency ceiling for 30B + agentic work [55][56] | Add routing/overflow tier + concurrency-reality slide |
| Implied "FAANG run everything local cheap" | They run **custom silicon + routing + quantization**; many also route to APIs (Shopify, Coinbase, Copilot) | Pitch the *replicable* parts: vLLM engine + LiteLLM gateway + cascade routing |

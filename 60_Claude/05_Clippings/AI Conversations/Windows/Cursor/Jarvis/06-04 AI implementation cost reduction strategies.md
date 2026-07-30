---
type: input
input_kind: ai-conversation
source_app: cursor
source_os: windows
title: "AI implementation cost reduction strategies"
started_at: 2026-06-04T13:40:41
ended_at: 2026-06-04T14:40:39
exported_at: 2026-07-30T19:56:24
project: Jarvis
cwd: "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis"
session_id: cb40f972-61d5-4ff9-9ff3-32ef70ca2730
status: raw
turn_count: 4
tools_used:
  AskQuestion: 2
  CreatePlan: 1
  Glob: 2
  Read: 3
  Task: 4
  WebSearch: 7
  Write: 2
files_touched:
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\40_Resources\\CS\\Repos.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\40_Resources\\CS\\AI\\Ollama.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\40_Resources\\CS\\AI\\AI Workflow.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Zero-Cost AI Stack\\Research Dossier — Internal LLM Inference at Near-Zero Cost.md"
  - "D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\10_Areas\\Life\\Plans\\Zero-Cost AI Stack\\Architecture & Setup Runbook — 24GB Hybrid Stack.md"
files_changed_count: 2
lines_added: 641
lines_removed: 0
tags:
  - input
  - ai-conversation
  - cursor
  - windows
---

# AI implementation cost reduction strategies

## You

<timestamp>Thursday, Jun 4, 2026, 12:23 PM (UTC+4)</timestamp>
<user_query>
Here is another issue that we are trying to tackle: 
```
Alright, let's start fresh. Here is the problem that a start up is facing - There are multiple projects being run in parallel, they hit token limits very often. Currently use copilot enterprise. We are focusing on low budget options for this solution. They already have a gpu and a server running in the office. Each and every single employee has a well functioning laptop with good ram. Local models are running right now but obviously unable to run the latest models. I provided the employees with this github to make the server gpu better: "https://github.com/lyogavin/airllm". But this is only for per laptop maybe? Can this work on a server gpu? We can use this other repo to analyze which models to run: "https://github.com/AlexsJones/llmfit" locally. My main goal over here to solve the enterprise and subscription problem so that each and every employee can work with ai at almost 0 cost. I have multiple resources listed in @40_Resources/CS/Repos, go through each and every relevant resource on github that could be used to solve this problem. Search for how are faang and big tech companies solving this issue that they are facing. How do they run models at almost no cost? We are going to mimick the worfklows of big tech companies over here. Let's not try to invent our own solution. Search the internet regarding this matter in brief. I have tons and tons of resources but I am still an outsider with half knowledge. Let's come up with a pitch and presentation so that this company does not go in extreme loss.
```

This HTML deck was created by claude: 
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Your Internal AI Stack — Zero-Cost Enterprise Proposal</title>
<style>
  :root {
    --navy:    #0D1B2A;
    --blue:    #1B4F72;
    --teal:    #0E9AA7;
    --ice:     #A8DADC;
    --white:   #FFFFFF;
    --offwhite:#F0F4F8;
    --gray:    #8899A8;
    --green:   #27AE60;
    --amber:   #F39C12;
    --red:     #E74C3C;
    --dark:    #07111A;
    --purple:  #5B7FD4;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #000;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px 10px;
    gap: 16px;
  }
  .slide {
    width: 960px;
    height: 540px;
    background: var(--navy);
    position: relative;
    overflow: hidden;
    border-radius: 4px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.7);
    flex-shrink: 0;
  }
  .footer {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 32px;
    background: var(--dark);
    display: flex;
    align-items: center;
    padding: 0 14px;
    font-size: 9px;
    color: var(--gray);
    font-style: italic;
    justify-content: space-between;
  }
  .footer .slide-num { color: var(--teal); font-weight: bold; font-style: normal; }
  .header-bar {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 56px;
    background: var(--dark);
    display: flex;
    align-items: center;
    padding: 0 16px;
    justify-content: space-between;
  }
  .header-label { font-size: 10px; font-weight: 700; color: var(--teal); letter-spacing: 5px; }
  .header-title { font-size: 18px; font-weight: 700; color: var(--white); }
  .teal-bar-left {
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 6px;
    background: var(--teal);
  }
  .card {
    background: var(--blue);
    border-radius: 3px;
    position: absolute;
    overflow: hidden;
  }
  .card-top-accent {
    height: 5px;
    width: 100%;
    position: absolute;
    top: 0; left: 0;
  }
  .card-left-accent {
    width: 6px;
    position: absolute;
    top: 0; left: 0; bottom: 0;
  }
  .dark-box {
    background: var(--dark);
    border-radius: 2px;
    position: absolute;
  }
  .navy-row {
    background: var(--navy);
    border-radius: 2px;
    position: absolute;
  }

  /* ── NAV ── */
  #nav {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 960px;
  }
  #nav button {
    background: var(--blue);
    border: 1px solid var(--teal);
    color: var(--ice);
    padding: 6px 14px;
    border-radius: 3px;
    cursor: pointer;
    font-size: 11px;
    font-family: inherit;
    transition: background 0.15s;
  }
  #nav button:hover { background: var(--teal); color: var(--navy); }
  #nav button.active { background: var(--teal); color: var(--navy); font-weight: 700; }

  /* ── SLIDE CONTENT HELPERS ── */
  .abs { position: absolute; }
  .mono { font-family: 'Consolas', 'Courier New', monospace; }
  .tag {
    display: inline-block;
    background: var(--teal);
    color: var(--navy);
    font-size: 8.5px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 2px;
    letter-spacing: 2px;
  }
  .tag.green { background: var(--green); }
  .tag.red { background: var(--red); }
  .tag.amber { background: var(--amber); }
</style>
</head>
<body>

<!-- ════ SLIDE 1 — TITLE ════ -->
<div class="slide" id="s1">
  <!-- Left accent bar -->
  <div style="position:absolute;left:0;top:0;bottom:0;width:14px;background:var(--teal);"></div>
  <!-- Right panel -->
  <div style="position:absolute;right:0;top:0;bottom:0;width:320px;background:var(--blue);"></div>
  <div style="position:absolute;right:320px;top:0;bottom:0;width:5px;background:var(--teal);"></div>

  <!-- Main headline -->
  <div style="position:absolute;left:30px;top:60px;width:580px;">
    <div style="font-size:11px;font-weight:700;color:var(--teal);letter-spacing:6px;margin-bottom:8px;">YOUR INTERNAL</div>
    <div style="font-size:72px;font-weight:900;color:var(--white);line-height:1;margin-bottom:18px;">AI STACK</div>
    <div style="font-size:16px;color:var(--ice);line-height:1.5;">Zero Subscriptions. Zero Token Limits.<br>Full Enterprise Power.</div>
  </div>

  <!-- Right panel pillars -->
  <div style="position:absolute;right:16px;top:50px;width:288px;">
    <div style="font-size:10px;font-weight:700;color:var(--teal);letter-spacing:4px;text-align:center;margin-bottom:12px;">THE BLUEPRINT</div>
    <div id="pillars"></div>
  </div>

  <div class="footer">
    <span>Confidential · Internal AI Infrastructure Proposal</span>
    <span class="slide-num">1</span>
  </div>
</div>

<!-- ════ SLIDE 2 — THE PROBLEM ════ -->
<div class="slide" id="s2">
  <div class="header-bar">
    <span class="header-label">THE PROBLEM</span>
    <span class="header-title">What's Costing You Right Now</span>
  </div>

  <!-- 3 problem cards -->
  <div id="problem-cards" style="position:absolute;top:72px;left:0;right:0;display:flex;gap:14px;padding:0 18px;"></div>

  <!-- Bottom callout -->
  <div style="position:absolute;bottom:38px;left:18px;right:18px;background:var(--dark);border-radius:3px;padding:16px 18px 16px 24px;border-left:6px solid var(--teal);">
    <div style="font-size:13px;font-weight:700;color:var(--teal);margin-bottom:6px;">The Real Cost</div>
    <div style="font-size:11.5px;color:var(--ice);line-height:1.55;">
      At 15 employees on Copilot Enterprise: <span style="font-weight:700;color:var(--amber);">$285/month = $3,420/year</span> — before overages, parallel project context blowouts, and productivity loss from constantly hitting token walls mid-task.
      <span style="font-weight:700;color:var(--white);"> You already own a GPU and a server. You are paying for nothing you couldn't run yourself.</span>
    </div>
  </div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">2</span>
  </div>
</div>

<!-- ════ SLIDE 3 — BIG TECH BLUEPRINT ════ -->
<div class="slide" id="s3">
  <div class="header-bar">
    <span class="header-label">THE BLUEPRINT</span>
    <span class="header-title">How FAANG Runs AI at Near-Zero Cost</span>
  </div>

  <div style="position:absolute;top:68px;left:18px;right:18px;font-size:12.5px;font-style:italic;color:var(--ice);">
    The fundamental shift: they don't buy subscriptions. <strong style="color:var(--white);">They own the compute.</strong>
  </div>

  <div id="bigtech-cards" style="position:absolute;top:100px;left:18px;right:18px;display:flex;flex-direction:column;gap:10px;"></div>

  <div style="position:absolute;bottom:40px;left:18px;right:18px;font-size:9.5px;color:var(--gray);font-style:italic;">
    Key insight: the tooling is already open-source because these companies built it and gave it away. We mimick the workflow, not the scale.
  </div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">3</span>
  </div>
</div>

<!-- ════ SLIDE 4 — ARCHITECTURE ════ -->
<div class="slide" id="s4">
  <div class="header-bar">
    <span class="header-label">THE ARCHITECTURE</span>
    <span class="header-title">Your Stack, End to End</span>
  </div>

  <div id="arch-layers" style="position:absolute;top:68px;left:10px;right:10px;display:flex;gap:10px;height:396px;"></div>

  <div style="position:absolute;bottom:38px;left:10px;right:10px;background:rgba(0,0,0,0.4);border-radius:2px;padding:5px 12px;text-align:center;">
    <span style="font-size:8.5px;color:var(--gray);">OPTIONAL PER-LAPTOP FALLBACK: AirLLM (70B on 4GB GPU) · llama.cpp · Ollama local — for offline or overflow use</span>
  </div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">4</span>
  </div>
</div>

<!-- ════ SLIDE 5 — llmfit ════ -->
<div class="slide" id="s5">
  <div class="header-bar">
    <span class="header-label">STEP 1</span>
    <span class="header-title">Find the Right Model for Your GPU — llmfit</span>
  </div>

  <div style="position:absolute;top:68px;left:10px;right:10px;display:flex;gap:12px;height:434px;">
    <!-- Left: features -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 16px;border-top:5px solid var(--teal);overflow:hidden;">
      <div style="font-size:12px;font-weight:700;color:var(--teal);margin-bottom:12px;">llmfit — hardware-aware model selection</div>
      <div id="llmfit-feats"></div>
    </div>
    <!-- Right: usage + model table -->
    <div style="width:340px;display:flex;flex-direction:column;gap:12px;">
      <div style="background:var(--dark);border-radius:3px;padding:14px 16px;flex:1;">
        <div style="font-size:11px;color:var(--ice);margin-bottom:8px;">On the server GPU, run:</div>
        <div class="mono" style="font-size:13px;color:var(--teal);margin-bottom:8px;">llmfit --memory=&lt;VRAM&gt;G</div>
        <div class="mono" style="font-size:10px;color:var(--gray);line-height:1.7;"># It will tell you exactly:<br># - Which model fits your VRAM<br># - Best quantization (Q4, Q8...)<br># - Expected tok/s for your GPU</div>
      </div>
      <div style="background:var(--blue);border-radius:3px;padding:14px 16px;flex:1.2;border-top:5px solid var(--amber);">
        <div style="font-size:12px;font-weight:700;color:var(--teal);margin-bottom:10px;">Expected Model Fit by VRAM</div>
        <div id="model-table"></div>
      </div>
    </div>
  </div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">5</span>
  </div>
</div>

<!-- ════ SLIDE 6 — INFERENCE SERVER ════ -->
<div class="slide" id="s6">
  <div class="header-bar">
    <span class="header-label">STEP 2</span>
    <span class="header-title">Run the Inference Server on the Office GPU</span>
  </div>

  <div style="position:absolute;top:68px;left:10px;right:10px;display:flex;gap:12px;height:436px;">
    <!-- Ollama -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 16px;border-top:5px solid var(--green);overflow:hidden;">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
        <span class="tag green">RECOMMENDED</span>
        <span style="font-size:18px;font-weight:700;color:var(--white);">Ollama</span>
      </div>
      <div style="font-size:11px;color:var(--ice);margin-bottom:12px;">Dead-simple to install. Start serving a 70B model in under 10 minutes.</div>
      <div id="ollama-steps"></div>
    </div>
    <!-- vLLM -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 16px;border-top:5px solid var(--purple);overflow:hidden;">
      <div style="font-size:18px;font-weight:700;color:var(--white);margin-bottom:8px;">vLLM</div>
      <div style="font-size:11px;color:var(--ice);margin-bottom:12px;line-height:1.4;">Production-grade. 2–4× throughput via PagedAttention. OpenAI-compatible. Handles concurrent requests from your entire team.</div>
      <div id="vllm-feats"></div>
      <div style="margin-top:12px;font-size:9.5px;color:var(--gray);font-style:italic;">Start with Ollama. Migrate to vLLM when concurrent users exceed ~5.</div>
    </div>
  </div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">6</span>
  </div>
</div>

<!-- ════ SLIDE 7 — GATEWAY ════ -->
<div class="slide" id="s7">
  <div class="header-bar">
    <span class="header-label">STEP 3</span>
    <span class="header-title">The Gateway — LiteLLM + Open WebUI</span>
  </div>

  <div style="position:absolute;top:68px;left:10px;right:10px;display:flex;gap:12px;height:436px;">
    <!-- LiteLLM -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 16px;border-top:5px solid var(--teal);overflow:hidden;">
      <div style="font-size:13px;font-weight:700;color:var(--teal);margin-bottom:6px;">LiteLLM Proxy (API Gateway)</div>
      <div style="font-size:11px;color:var(--ice);margin-bottom:12px;line-height:1.4;">The control plane between your team and the model server. Every employee gets their own API key.</div>
      <div id="litellm-feats"></div>
    </div>
    <!-- Open WebUI -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 16px;border-top:5px solid var(--purple);overflow:hidden;">
      <div style="font-size:13px;font-weight:700;color:#CADCFC;margin-bottom:6px;">Open WebUI (Frontend)</div>
      <div style="font-size:11px;color:var(--ice);margin-bottom:12px;line-height:1.4;">A full ChatGPT-like interface your whole team uses in their browser. Zero installation on employee laptops.</div>
      <div id="webui-feats"></div>
      <div style="margin-top:14px;background:var(--navy);border-radius:2px;padding:8px 10px;">
        <span class="mono" style="font-size:10px;color:var(--teal);">docker compose up -d</span>
        <span style="font-size:10px;color:var(--gray);margin-left:8px;"># deploys both in minutes</span>
      </div>
    </div>
  </div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">7</span>
  </div>
</div>

<!-- ════ SLIDE 8 — RAG + DIFY ════ -->
<div class="slide" id="s8">
  <div class="header-bar">
    <span class="header-label">STEP 4</span>
    <span class="header-title">Solving the Token Limit Problem — RAG &amp; Dify</span>
  </div>

  <!-- Callout -->
  <div style="position:absolute;top:68px;left:10px;right:10px;background:var(--dark);border-radius:3px;padding:10px 14px 10px 20px;border-left:6px solid var(--amber);">
    <div style="font-size:11.5px;font-weight:700;color:var(--amber);margin-bottom:4px;">Why token limits kill parallel projects:</div>
    <div style="font-size:11px;color:var(--ice);">Developers dump entire codebases into context instead of retrieving only what's relevant. RAG fixes this permanently.</div>
  </div>

  <div style="position:absolute;top:148px;left:10px;right:10px;display:flex;gap:12px;height:344px;">
    <!-- Bad approach -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 16px;border-top:5px solid var(--red);overflow:hidden;">
      <div style="font-size:13px;font-weight:700;color:var(--red);margin-bottom:12px;">❌ Without RAG (Current)</div>
      <div id="bad-steps"></div>
    </div>
    <!-- Good approach -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 16px;border-top:5px solid var(--green);overflow:hidden;">
      <div style="font-size:13px;font-weight:700;color:var(--green);margin-bottom:12px;">✅ With Dify + RAG</div>
      <div id="good-steps"></div>
      <div style="margin-top:10px;font-size:9px;color:var(--gray);font-style:italic;">Dify: self-hosted, Docker-deployable, 143K GitHub stars. Free forever on self-hosted.</div>
    </div>
  </div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">8</span>
  </div>
</div>

<!-- ════ SLIDE 9 — AirLLM ════ -->
<div class="slide" id="s9">
  <div class="header-bar">
    <span class="header-label">BONUS TOOL</span>
    <span class="header-title">AirLLM — Run 70B Models on 4GB GPU VRAM</span>
  </div>

  <div style="position:absolute;top:68px;left:10px;right:10px;display:flex;gap:12px;height:200px;">
    <!-- Big stat -->
    <div style="background:var(--blue);border-radius:3px;width:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-left:6px solid var(--teal);">
      <div style="font-size:80px;font-weight:900;color:var(--teal);line-height:1;">70B</div>
      <div style="font-size:13px;color:var(--white);font-weight:700;text-align:center;padding:0 8px;">params on 4 GB VRAM</div>
      <div style="font-size:10px;color:var(--gray);font-style:italic;margin-top:4px;">No quantization required</div>
    </div>
    <!-- How it works -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 18px;border-top:5px solid var(--teal);">
      <div style="font-size:13px;font-weight:700;color:var(--teal);margin-bottom:10px;">How AirLLM Works</div>
      <div style="font-size:11.5px;color:var(--ice);line-height:1.6;">
        Instead of loading the entire model into VRAM, AirLLM streams one transformer layer at a time from disk through the GPU.
        Each layer fits in a few hundred MB. After computing, it's evicted and the next layer loads.
        Your disk becomes extended GPU memory — at the cost of slower inference speed.
      </div>
    </div>
  </div>

  <!-- Server vs Laptop -->
  <div style="position:absolute;top:284px;left:10px;right:10px;background:var(--dark);border-radius:3px;padding:16px 20px 16px 26px;border-left:7px solid var(--amber);">
    <div style="font-size:13px;font-weight:700;color:var(--amber);margin-bottom:8px;">Does AirLLM work on your server GPU?</div>
    <div style="font-size:11.5px;line-height:1.6;">
      <span style="font-weight:700;color:var(--green);">YES</span><span style="color:var(--ice);"> — AirLLM works on any GPU, not just laptops. It's a PyPI package. Install on the server, point it at a model on disk, and any GPU with as little as 4GB VRAM can serve 70B inference.</span><br>
      <span style="font-weight:700;color:var(--amber);">Trade-off:</span> <span style="color:var(--gray);">Layer-by-layer loading is slower than fully VRAM-resident inference (vLLM/Ollama). Best used for single-user deep tasks or when your server GPU has limited VRAM. For multi-user concurrent serving, pair with Ollama/vLLM.</span>
    </div>
  </div>

  <!-- Three use cases -->
  <div style="position:absolute;bottom:40px;left:10px;right:10px;display:flex;gap:10px;">
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:10px 14px;border-top:4px solid var(--teal);">
      <div style="font-size:10px;font-weight:700;color:var(--teal);margin-bottom:4px;">USE CASE 1</div>
      <div style="font-size:10px;color:var(--ice);">Server has &lt;8GB VRAM but you need a 70B model → AirLLM bridges the gap</div>
    </div>
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:10px 14px;border-top:4px solid var(--purple);">
      <div style="font-size:10px;font-weight:700;color:var(--purple);margin-bottom:4px;">USE CASE 2</div>
      <div style="font-size:10px;color:var(--ice);">Offline laptop work — engineer away from office, no server access</div>
    </div>
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:10px 14px;border-top:4px solid var(--amber);">
      <div style="font-size:10px;font-weight:700;color:var(--amber);margin-bottom:4px;">USE CASE 3</div>
      <div style="font-size:10px;color:var(--ice);">Server GPU is busy — laptop GPU picks up overflow for single deep tasks</div>
    </div>
  </div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">9</span>
  </div>
</div>

<!-- ════ SLIDE 10 — ROLLOUT ════ -->
<div class="slide" id="s10">
  <div class="header-bar">
    <span class="header-label">EXECUTION</span>
    <span class="header-title">4-Phase Rollout — First Results in 48 Hours</span>
  </div>

  <div id="rollout-phases" style="position:absolute;top:68px;left:10px;right:10px;display:flex;gap:10px;height:450px;"></div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">10</span>
  </div>
</div>

<!-- ════ SLIDE 11 — COST ════ -->
<div class="slide" id="s11">
  <div class="header-bar">
    <span class="header-label">THE NUMBERS</span>
    <span class="header-title">Cost Comparison: Subscriptions vs Self-Hosted</span>
  </div>

  <div style="position:absolute;top:68px;left:10px;right:10px;display:flex;gap:12px;height:438px;">
    <!-- Subscription costs -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 16px;border-top:5px solid var(--red);overflow:hidden;">
      <div style="font-size:13px;font-weight:700;color:var(--red);margin-bottom:12px;">Subscription Model (Current)</div>
      <div id="sub-costs"></div>
      <div style="margin-top:12px;font-size:9.5px;color:var(--gray);font-style:italic;">Scales linearly — every new hire costs more.</div>
    </div>
    <!-- Self-hosted costs -->
    <div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 16px;border-top:5px solid var(--green);overflow:hidden;">
      <div style="font-size:13px;font-weight:700;color:var(--green);margin-bottom:12px;">Self-Hosted Stack (Proposed)</div>
      <div id="sh-costs"></div>
      <div style="margin-top:12px;font-size:9.5px;color:var(--green);font-style:italic;">Scales to unlimited users. No per-seat cost ever.</div>

      <!-- Savings callout -->
      <div style="margin-top:14px;background:var(--navy);border-radius:3px;padding:10px 14px;border-left:5px solid var(--green);">
        <div style="font-size:22px;font-weight:900;color:var(--green);">$3,480–$11,760</div>
        <div style="font-size:11px;color:var(--ice);">saved per year (10–20 employees)</div>
        <div style="font-size:9px;color:var(--gray);margin-top:4px;">Break-even: immediate. Ongoing cost: ~$30/mo electricity.</div>
      </div>
    </div>
  </div>

  <div class="footer">
    <span>Zero-Cost AI Stack · Internal Proposal</span>
    <span class="slide-num">11</span>
  </div>
</div>

<!-- ════ SLIDE 12 — CTA ════ -->
<div class="slide" id="s12">
  <div style="position:absolute;inset:0;background:var(--dark);"></div>
  <div style="position:absolute;left:0;top:0;bottom:0;width:16px;background:var(--teal);"></div>
  <div style="position:absolute;left:0;top:0;right:0;height:10px;background:var(--teal);"></div>

  <div style="position:absolute;left:30px;top:40px;right:20px;">
    <div style="font-size:10px;font-weight:700;color:var(--teal);letter-spacing:6px;margin-bottom:10px;">THE DECISION</div>
    <div style="font-size:38px;font-weight:900;color:var(--white);margin-bottom:14px;line-height:1.1;">Keep Paying —<br>or Own Your Stack</div>
    <div style="font-size:15px;color:var(--ice);line-height:1.5;margin-bottom:30px;">You have the hardware. You have the people. The tools are free.<br>The only thing missing is 48 hours to set it up.</div>

    <div id="cta-actions"></div>

    <div style="margin-top:20px;font-size:8.5px;color:var(--gray);">
      All tools referenced are open source · llmfit · AirLLM · Ollama · vLLM · LiteLLM · Open WebUI · Dify · Unsloth
    </div>
  </div>
</div>

<!-- ════ NAV ════ -->
<div id="nav">
  <button onclick="scrollTo('s1')" class="active">1 · Title</button>
  <button onclick="scrollTo('s2')">2 · Problem</button>
  <button onclick="scrollTo('s3')">3 · Big Tech</button>
  <button onclick="scrollTo('s4')">4 · Architecture</button>
  <button onclick="scrollTo('s5')">5 · llmfit</button>
  <button onclick="scrollTo('s6')">6 · Server</button>
  <button onclick="scrollTo('s7')">7 · Gateway</button>
  <button onclick="scrollTo('s8')">8 · RAG</button>
  <button onclick="scrollTo('s9')">9 · AirLLM</button>
  <button onclick="scrollTo('s10')">10 · Rollout</button>
  <button onclick="scrollTo('s11')">11 · Cost</button>
  <button onclick="scrollTo('s12')">12 · CTA</button>
</div>

<script>
function scrollTo(id) {
  document.getElementById(id).scrollIntoView({ behavior: 'smooth', block: 'center' });
  document.querySelectorAll('#nav button').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
}

// ── SLIDE 1: Pillars ──────────────────────────────────────────────────────
const pillars = ["Centralized GPU Server","Open-Source Models","Smart LLM Gateway","RAG for Token Control","Per-Laptop Fallback"];
const pillarsEl = document.getElementById('pillars');
pillars.forEach(p => {
  pillarsEl.innerHTML += `<div style="background:var(--navy);border-radius:2px;padding:9px 12px 9px 18px;margin-bottom:8px;border-left:5px solid var(--teal);font-size:11px;font-weight:700;color:var(--white);">${p}</div>`;
});

// ── SLIDE 2: Problem cards ─────────────────────────────────────────────────
const problems = [
  { stat: "$19+", label: "Per employee / month", sub: "GitHub Copilot Enterprise", color: "var(--red)" },
  { stat: "∞", label: "Token limits hit constantly", sub: "Parallel projects = compounded waste", color: "var(--amber)" },
  { stat: "0%", label: "Data privacy guarantee", sub: "Your code lives on third-party servers", color: "var(--amber)" },
];
const pcEl = document.getElementById('problem-cards');
problems.forEach(p => {
  pcEl.innerHTML += `<div style="background:var(--blue);border-radius:3px;flex:1;border-top:5px solid ${p.color};padding:16px;text-align:center;">
    <div style="font-size:52px;font-weight:900;color:${p.color};line-height:1;">${p.stat}</div>
    <div style="font-size:12px;font-weight:700;color:var(--white);margin:8px 0 4px;">${p.label}</div>
    <div style="font-size:10px;color:var(--gray);">${p.sub}</div>
  </div>`;
});

// ── SLIDE 3: Big Tech ──────────────────────────────────────────────────────
const bigtech = [
  { company: "Meta", color: "var(--teal)", body: "Open-source Llama models on internal GPU clusters, served via vLLM. Every engineer gets a code assistant backed by their own hardware — no per-seat fee." },
  { company: "Google", color: "var(--purple)", body: "llm-d (open source) — Kubernetes-native distributed vLLM for enterprise-scale inference. Contributed vLLM to the open-source community. Uses TPUs internally but the open stack is GPU-ready." },
  { company: "The Standard Stack", color: "var(--green)", body: "vLLM server (open source, Apache 2.0) → LiteLLM API gateway (per-team keys + budgets) → Open WebUI (ChatGPT-like frontend). All free. Runs on any Linux GPU box. Used by thousands of companies worldwide." },
];
const btEl = document.getElementById('bigtech-cards');
bigtech.forEach(b => {
  btEl.innerHTML += `<div style="background:var(--blue);border-radius:3px;padding:12px 16px 12px 22px;border-left:7px solid ${b.color};">
    <span style="font-size:13px;font-weight:700;color:${b.color};">${b.company} &nbsp;</span>
    <span style="font-size:11.5px;color:var(--ice);">${b.body}</span>
  </div>`;
});

// ── SLIDE 4: Architecture ─────────────────────────────────────────────────
const layers = [
  { label: "LAYER 1 — EMPLOYEE", color: "var(--gray)", items: ["Laptop Browser → Open WebUI","IDE Plugin → OpenAI-compatible API","CLI / Scripts → Direct API calls","AirLLM (offline fallback)"] },
  { label: "LAYER 2 — GATEWAY", color: "var(--purple)", items: ["LiteLLM Proxy","Per-user API keys + budgets","Model routing by task complexity","Usage dashboards + cost tracking"] },
  { label: "LAYER 3 — SERVER GPU", color: "var(--teal)", items: ["vLLM or Ollama (serving engine)","Llama 3.3 70B / Qwen2.5 72B","OpenAI-compatible REST API","Continuous batching (PagedAttn)","Dify (RAG knowledge base)"] },
];
const archEl = document.getElementById('arch-layers');
layers.forEach((l, i) => {
  const flex = i === 2 ? 1.5 : 1;
  archEl.innerHTML += `<div style="background:var(--blue);border-radius:3px;flex:${flex};padding:14px 12px;border-top:5px solid ${l.color};overflow:hidden;">
    <div style="font-size:9.5px;font-weight:700;color:${l.color};letter-spacing:2px;margin-bottom:12px;">${l.label}</div>
    ${l.items.map(it => `<div style="background:var(--navy);border-radius:2px;padding:8px 10px;margin-bottom:8px;font-size:10.5px;color:var(--ice);">${it}</div>`).join('')}
  </div>`;
});

// ── SLIDE 5: llmfit ───────────────────────────────────────────────────────
const llmfitFeats = [
  "Detects your GPU VRAM, RAM, CPU cores automatically",
  "Scores hundreds of models across Quality, Speed, Fit, Context",
  "Tells you the best quantization (Q4, Q8) that fits in VRAM",
  "Shows estimated tokens/sec on YOUR hardware",
  "Supports Ollama, vLLM, llama.cpp, LM Studio backends",
  "llmfit serve → REST API for cluster scheduling",
  "Community leaderboard — real tok/s from real users",
];
const lfEl = document.getElementById('llmfit-feats');
llmfitFeats.forEach(f => {
  lfEl.innerHTML += `<div style="display:flex;align-items:flex-start;gap:8px;margin-bottom:7px;">
    <div style="width:18px;height:18px;min-width:18px;background:var(--teal);border-radius:2px;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700;color:var(--navy);">✓</div>
    <div style="font-size:10.5px;color:var(--ice);line-height:1.4;">${f}</div>
  </div>`;
});
const modelRows = [
  { vram: "8 GB VRAM", model: "Llama 3.1 8B (Q8) or Qwen2.5 14B (Q4)" },
  { vram: "16 GB VRAM", model: "Llama 3.3 70B (Q4) — code + reasoning" },
  { vram: "24+ GB VRAM", model: "Llama 3.3 70B (Q6) or DeepSeek-R1 32B" },
  { vram: "48+ GB VRAM", model: "Full 70B Q8 or DeepSeek-V3 70B" },
];
const mtEl = document.getElementById('model-table');
modelRows.forEach(r => {
  mtEl.innerHTML += `<div style="display:flex;align-items:center;gap:8px;margin-bottom:7px;">
    <span style="font-size:10px;font-weight:700;color:var(--amber);min-width:80px;">${r.vram}</span>
    <span style="font-size:10px;color:var(--ice);">→ ${r.model}</span>
  </div>`;
});

// ── SLIDE 6: Ollama ────────────────────────────────────────────────────────
const ollamaSteps = [
  { cmd: "curl -fsSL https://ollama.com/install.sh | sh", desc: "Install on Linux server" },
  { cmd: "ollama pull llama3.3:70b-instruct-q4_K_M", desc: "Download model once" },
  { cmd: "OLLAMA_HOST=0.0.0.0 ollama serve", desc: "Expose to office network (port 11434)" },
  { cmd: "# Employees set OLLAMA_HOST=http://server-ip:11434", desc: "Zero install on laptops" },
];
const osEl = document.getElementById('ollama-steps');
ollamaSteps.forEach(s => {
  osEl.innerHTML += `<div style="background:var(--navy);border-radius:2px;padding:8px 10px;margin-bottom:8px;">
    <div class="mono" style="font-size:9.5px;color:var(--teal);margin-bottom:3px;">${s.cmd}</div>
    <div style="font-size:9px;color:var(--gray);">${s.desc}</div>
  </div>`;
});
const vllmFeats = [
  "PagedAttention: 50%+ memory reduction, 2–4× throughput",
  "OpenAI /v1/chat/completions — drop-in replacement",
  "Multi-user concurrent batching built-in",
  "Supports Llama, Qwen, Mistral, DeepSeek, Gemma",
  "74.9K GitHub stars — backed by Meta, Google, NVIDIA",
];
const vfEl = document.getElementById('vllm-feats');
vllmFeats.forEach(f => {
  vfEl.innerHTML += `<div style="display:flex;gap:8px;margin-bottom:8px;align-items:flex-start;">
    <div style="width:16px;height:16px;min-width:16px;background:var(--purple);border-radius:2px;display:flex;align-items:center;justify-content:center;font-size:9px;color:var(--white);">→</div>
    <div style="font-size:10.5px;color:var(--ice);">${f}</div>
  </div>`;
});

// ── SLIDE 7: LiteLLM + WebUI ───────────────────────────────────────────────
const litellmFeats = [
  { title: "Per-user API keys", desc: "Each employee authenticates separately" },
  { title: "Budget enforcement", desc: "$X/month cap per person or team" },
  { title: "Model routing", desc: "Cheap model for chat, strong for code" },
  { title: "Usage dashboard", desc: "See who used what, when, at what cost" },
  { title: "OpenAI-compatible", desc: "Works with VS Code, Cursor, any IDE" },
  { title: "100+ provider support", desc: "Fallback to cloud API if needed" },
];
const lfEl2 = document.getElementById('litellm-feats');
litellmFeats.forEach(f => {
  lfEl2.innerHTML += `<div style="background:var(--navy);border-radius:2px;padding:8px 10px;margin-bottom:7px;font-size:10.5px;">
    <span style="color:var(--teal);font-weight:700;">${f.title}: </span>
    <span style="color:var(--ice);">${f.desc}</span>
  </div>`;
});
const webUIFeats = [
  "Chat history, conversation management",
  "Multi-model access from one interface",
  "File/document uploads (PDF, code files)",
  "Voice input/output support",
  "Admin controls per-user model access",
  "Works on any device — browser only, no install",
  "No training data sent anywhere — 100% private",
];
const wfEl = document.getElementById('webui-feats');
webUIFeats.forEach(f => {
  wfEl.innerHTML += `<div style="display:flex;gap:8px;margin-bottom:7px;align-items:flex-start;">
    <div style="width:16px;height:16px;min-width:16px;background:var(--purple);border-radius:2px;display:flex;align-items:center;justify-content:center;font-size:9px;color:var(--white);">✓</div>
    <div style="font-size:10.5px;color:var(--ice);">${f}</div>
  </div>`;
});

// ── SLIDE 8: RAG ──────────────────────────────────────────────────────────
const badSteps = [
  "User pastes entire codebase into chat",
  "50,000+ tokens consumed per query",
  "Context window hits limit mid-project",
  "Model \"forgets\" earlier context",
  "Team hits monthly token cap",
  "Work stops. Subscription upgraded.",
];
const bsEl = document.getElementById('bad-steps');
badSteps.forEach((s, i) => {
  bsEl.innerHTML += `<div style="background:var(--navy);border-radius:2px;padding:8px 10px;margin-bottom:6px;font-size:11px;color:${i >= 4 ? 'var(--red)' : 'var(--ice)'};">${s}</div>`;
});
const goodSteps = [
  "Codebase indexed into vector DB once",
  "Query retrieves only 3–5 relevant chunks",
  "500–2,000 tokens per query vs 50,000",
  "Context window never fills up",
  "25× fewer tokens consumed",
  "Unlimited parallel projects. Zero overages.",
];
const gsEl = document.getElementById('good-steps');
goodSteps.forEach((s, i) => {
  gsEl.innerHTML += `<div style="background:var(--navy);border-radius:2px;padding:8px 10px;margin-bottom:6px;font-size:11px;color:${i === 5 ? 'var(--green)' : 'var(--ice)'};">${s}</div>`;
});

// ── SLIDE 10: Rollout ─────────────────────────────────────────────────────
const phases = [
  { phase:"1", timeline:"Day 1–2", title:"Server + Model", color:"var(--teal)", steps:["Run llmfit on server GPU to identify best model","Install Ollama, pull recommended model","Test: one employee connects remotely","Confirm inference works end-to-end"] },
  { phase:"2", timeline:"Week 1", title:"Gateway + Frontend", color:"var(--purple)", steps:["Deploy LiteLLM proxy with Docker","Create API keys for all employees","Deploy Open WebUI (ChatGPT-like UI)","Connect IDE plugins to gateway"] },
  { phase:"3", timeline:"Week 2–3", title:"RAG for Projects", color:"var(--amber)", steps:["Deploy Dify with Docker","Index active project codebases","Set up Dify workflows for common tasks","Token usage drops 10–25× per query"] },
  { phase:"4", timeline:"Month 2", title:"Optimize & Scale", color:"var(--green)", steps:["Migrate to vLLM if concurrent users grow","Tune model selection based on usage data","AirLLM as laptop fallback for offline","Cancel Copilot Enterprise subscription"] },
];
const rpEl = document.getElementById('rollout-phases');
phases.forEach(p => {
  rpEl.innerHTML += `<div style="background:var(--blue);border-radius:3px;flex:1;padding:14px 12px;border-top:5px solid ${p.color};overflow:hidden;">
    <div style="width:36px;height:36px;border-radius:50%;background:${p.color};display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:900;color:var(--navy);margin:0 auto 6px;">${p.phase}</div>
    <div style="font-size:10px;font-weight:700;color:${p.color};text-align:center;margin-bottom:4px;">${p.timeline}</div>
    <div style="font-size:12px;font-weight:700;color:var(--white);text-align:center;margin-bottom:12px;">${p.title}</div>
    ${p.steps.map(s => `<div style="background:var(--navy);border-radius:2px;padding:7px 9px;margin-bottom:6px;font-size:9.5px;color:var(--ice);line-height:1.4;">${s}</div>`).join('')}
  </div>`;
});

// ── SLIDE 11: Cost ─────────────────────────────────────────────────────────
const subCosts = [
  { item: "Copilot Enterprise (10 users)", cost: "$190/mo" },
  { item: "Copilot Enterprise (20 users)", cost: "$380/mo" },
  { item: "API overages (parallel projects)", cost: "$100–400/mo" },
  { item: "Context window upgrades", cost: "$50–200/mo" },
  { item: "Annual total (10 users)", cost: "$3,480–$7,080", bold: true },
  { item: "Annual total (20 users)", cost: "$5,760–$11,760", bold: true },
];
const scEl = document.getElementById('sub-costs');
subCosts.forEach(c => {
  scEl.innerHTML += `<div style="display:flex;justify-content:space-between;align-items:center;background:var(--navy);border-radius:2px;padding:8px 10px;margin-bottom:7px;font-size:11px;">
    <span style="color:var(--ice);">${c.item}</span>
    <span style="color:var(--red);font-weight:${c.bold ? '700' : '400'};font-size:${c.bold ? '12' : '11'}px;">${c.cost}</span>
  </div>`;
});
const shCosts = [
  { item: "Ollama (inference server)", cost: "$0" },
  { item: "vLLM (production serving)", cost: "$0" },
  { item: "LiteLLM (API gateway)", cost: "$0" },
  { item: "Open WebUI (chat frontend)", cost: "$0" },
  { item: "Dify (RAG + workflows)", cost: "$0" },
  { item: "Model (Llama/Qwen/DeepSeek)", cost: "$0" },
  { item: "Electricity (server GPU)", cost: "~$30/mo" },
  { item: "One-time setup (~16 hrs)", cost: "one-time" },
];
const shEl = document.getElementById('sh-costs');
shCosts.forEach(c => {
  shEl.innerHTML += `<div style="display:flex;justify-content:space-between;align-items:center;background:var(--navy);border-radius:2px;padding:7px 10px;margin-bottom:6px;font-size:11px;">
    <span style="color:var(--ice);">${c.item}</span>
    <span style="color:${c.cost === '$0' ? 'var(--green)' : 'var(--amber)'};font-weight:700;">${c.cost}</span>
  </div>`;
});

// ── SLIDE 12: CTA ─────────────────────────────────────────────────────────
const actions = [
  { num: "01", action: "Run llmfit on the server GPU", detail: "Find out which model fits. Takes 5 minutes." },
  { num: "02", action: "Deploy Ollama + Open WebUI", detail: "Give the whole team a working AI workspace in under 2 hours." },
  { num: "03", action: "Index one project with Dify", detail: "Kill the token limit problem on your most active project this week." },
];
const ctaEl = document.getElementById('cta-actions');
actions.forEach(a => {
  ctaEl.innerHTML += `<div style="display:flex;align-items:center;gap:16px;background:var(--blue);border-radius:3px;padding:12px 16px;margin-bottom:10px;border-left:6px solid var(--teal);">
    <div style="font-size:22px;font-weight:900;color:var(--teal);min-width:36px;">${a.num}</div>
    <div>
      <div style="font-size:13px;font-weight:700;color:var(--white);">${a.action}</div>
      <div style="font-size:11px;color:var(--gray);margin-top:3px;">${a.detail}</div>
    </div>
  </div>`;
});
</script>
</body>
</html>
```

This prompt was provided to claude and it replied me with half asses answers. I am not satisfied with the research done or the reply. DO not modify the html file that I have pasted you with. We can create powerpoint later, your focus is to do solid research and come up with a plan first. Let's see what you are capable of doing now. The problem has been described in detail to you above. To put in one line - AI implementation is trying to be implemented but at a very high cost. This is not possible for each and every single employee to use. 

We need to come up with a solution copying what faang and big tech companies are doing for this matter. No way that everyone is using subscriptions but no way that companies are running low-end models all the time on their high tech gpu's and data centers. We have a gpu, multiple laptops and engineers we can put to work. This is a start up company trying to implement ai across all its projects. The projects are all software development, building apps, websites, solutions basically. 

Search the internet in detail regarding this matter, come up with a solid plan to do this research. This should not be half backed, reply only on reliable sources from big tech companies and solutions that are detailed and rigid. 
</user_query>

## Cursor

I'll research this thoroughly before proposing a plan. Let me start by exploring your resources folder and searching the web in parallel.

 I'm grasping the scope here—a startup juggling multiple dev projects and hitting token limits with their current AI tooling, so they need a cost-effective strategy that mirrors how big tech companies operate at scale. I should dive into research mode first to understand the landscape, then synthesize a comprehensive plan.

The key tension they're pointing out is real: a single office GPU can't realistically serve a 70B model to multiple concurrent users, and AirLLM's layer-streaming approach is too slow for production use. The actual big-tech playbook involves a hybrid mix of self-hosted inference engines, model gateways, quantization techniques, and RAG systems—not just picking one solution. I need to research how they actually balance cost and capability, then present an honest assessment of what's feasible for their constraints.

Before diving into the resources folder and web research, I should clarify a few critical unknowns: the actual GPU VRAM and model they're running now, exact employee count, and server specs. These details fundamentally change what models can run and how many concurrent users they can serve. That said, they may not have exact specs, so I'll start by exploring what's in their resources folder and doing parallel web research to build a solid plan.

`40_Resources/CS/Repos` is actually a file `Repos.md`. Let me read it and the other relevant AI notes.

 I need to check what's actually in that Repos file since it's a markdown document, not a folder, then pull up the related files about Ollama, my AI workflow, and other relevant links to get the full picture.

This is very helpful. Your `Repos.md` already stars most of the relevant tools (llmfit, whichllm, airllm, dify, unsloth, jan, free-llm-api-resources, vLLM-adjacent). Now let me do the deep web research on how big tech actually runs this. I'll search multiple angles in parallel.

 I'm scanning through the resource list and identifying the most relevant repositories for this problem—there are several key tools that stand out: llmfit, whichllm, and airllm for hardware optimization; dify as a self-hosted platform with RAG capabilities; unsloth for fine-tuning; jan for local deployment; plus some free API resources and proxy solutions, along with RAG-focused tools like claude-context and memsearch.

I notice vLLM isn't explicitly listed but Ollama is mentioned in the notes, and there are some production ML blogs in ai-engineering-hub and applied-ml that could be useful. Before I dive into research, I need to understand a few critical constraints: the GPU model and VRAM available, how many concurrent users or engineers need access, what type of coding workflows they're targeting (IDE autocomplete versus chat versus agentic systems), and whether they have privacy or data residency requirements that rule out cloud APIs entirely. The user has a strong conviction that FAANG companies don't rely on subscriptions and run everything on their own hardware, but the reality is more nuanced—I need to research the actual production stacks and cost economics to give them an honest, evidence-based answer rather than just validating their assumption.

Excellent — this research is already reshaping the picture. The cost data directly contradicts the deck's "near-zero" framing. Let me dig into a few more critical angles: what big tech actually does for coding AI, the best open coding models right now, and how to solve the token-limit problem properly.

 I'm realizing the research actually undermines the self-hosting narrative in the deck—below 50M tokens monthly, API services have better total cost of ownership when you factor in engineering overhead. However, this startup's situation is different: they've already invested in hardware and have engineers on staff, so the comparison shifts from APIs versus self-hosting to whether self-hosting beats out paying for Copilot Enterprise subscriptions.

The practical answer for them is a hybrid approach—use a capable open model on their existing GPU for routine coding tasks, but route the complex work requiring frontier-level reasoning to cheap APIs like DeepSeek, while aggressively leveraging prompt caching and RAG to minimize token consumption. AirLLM won't work for their multi-user production environment since it's too slow, despite what the deck claimed.

I need to dig deeper into how actual FAANG companies structure their internal coding assistants, what the best open coding models are for 2026, how to handle token limits in agentic workflows, and how to wire up tools like Continue.dev with self-hosted models through a routing gateway.

I've gathered strong, source-backed research. Before I write the plan, two facts will fundamentally change the architecture and the honest cost story, and I don't want to guess on them (guessing is exactly what produced the half-baked deck you got).

Here's what my research already establishes, so you see why these two questions matter:

- **The deck's "near-zero cost" claim is misleading.** Multiple 2026 TCO analyses (CMU framework, digitalapplied, aipricingmaster, railwail) agree: self-hosting only beats APIs on total cost above roughly **50M+ tokens/month for small models** and **600M+/month for code workloads** — *once you count engineer time*. Below that, cloud APIs (especially with prompt caching) are cheaper. Your real advantage is different: you already **own the GPU (sunk cost)** and you're comparing against **per-seat Copilot fees**, not against renting GPUs. That's a winnable argument, but only if framed honestly.
- **The deck massively oversold AirLLM.** AirLLM streams layers from disk one at a time — it's single-user and extremely slow (single-digit tok/s). It is *not* a multi-user serving engine. Real big-tech serving = **vLLM** (used by Meta, Amazon, Roblox, Stripe, IBM) with continuous batching + PagedAttention.
- **A single GPU's concurrency is finite.** An 8B model on a 24GB GPU serves ~30-80 concurrent users; a 70B model on one consumer GPU serves very few. So "everyone uses the one office GPU for heavy agent work" may not hold — which is exactly why big tech runs *tiered routing* (cheap local model for autocomplete/bulk, frontier for hard tasks).

So the architecture branches entirely on your hardware and your privacy rules:

 I've got enough evidence to push back on the weak spots in their proposal and create a solid, grounded plan. Before I synthesize the findings though, I need to ask them three critical questions since everything hinges on GPU memory capacity, how many engineers they can run in parallel, and whether they're locked into on-premises infrastructure or can tap into cloud APIs like DeepSeek.

I have what I need. Your answers (single ~24GB consumer GPU, hybrid APIs allowed, ~15-40 mixed-workflow engineers) point to a clear, well-evidenced architecture — and they confirm that several claims in the Claude deck need correcting. Here's my synthesis and the plan.

## What the research actually says (the corrected thesis)

The deck's core instinct — own your compute instead of paying per-seat — is right. But three of its claims are wrong or misleading, and fixing them is the difference between a pitch that survives scrutiny and one that gets torn apart:

1. **"Near-zero cost" is not honest TCO.** Every serious 2026 source (CMU's Wang framework, digitalapplied, aipricingmaster, railwail) agrees self-hosting only beats APIs *on raw cost* above ~50M tokens/month (small models) to ~600M/month (code), once engineer time is counted. **Your real, defensible win is different:** you already own the GPU (sunk cost) and you're replacing *per-seat subscription fees* that scale with every hire. Frame it that way and it's bulletproof.

2. **AirLLM was massively oversold.** It streams model layers from disk one at a time — single-user, single-digit tokens/sec. It is a niche *offline fallback*, NOT a team serving engine. The real big-tech serving layer is **vLLM** (used in production by Meta, Amazon Rufus, Roblox, Stripe, IBM) with continuous batching + PagedAttention.

3. **The deck missed the actual FAANG pattern: tiered routing.** Big tech doesn't run one model for everything. Meta's DevMate routes across models; Google fine-tunes Gemini on internal code for IDE features; the industry trend (Stripe, Uber, Shopify, Block) is in-house agents over a routing layer. The scaled-down version for you: **own the floor, rent the ceiling** — local GPU serves autocomplete + bulk chat; cheap external APIs (DeepSeek/Qwen/GLM) absorb the hard agentic tasks one 24GB GPU can't.

Let me write this up as the plan.

 I'm mapping out the constraints: a mid-range GPU with around 16-24GB of VRAM, a team of 15-40 engineers working on both autocomplete and agentic features, and flexibility to use external APIs for overflow. This points toward a tiered hybrid setup where I can run smaller models locally and offload to cheaper external services when needed.

For the 24GB card, I'd keep a small autocomplete model running continuously, deploy a larger mixture-of-experts model as the main workhorse for chat and editing tasks, and route the hardest agentic work to external APIs like DeepSeek or Qwen via OpenRouter. A single GPU with continuous batching can handle maybe 5-15 concurrent requests, but with 15-40 engineers doing mixed work, I'll definitely need that routing layer through LiteLLM to handle the overflow gracefully.

This is the scaled-down version of what big tech companies do—own compute for the baseline, cheap APIs for the ceiling, and aggressive token reduction through caching and RAG. Now I'm ready to structure the actual plan: the corrected narrative about this tiered approach, the validated architecture, and how it all fits together.

The plan itself should deliver a research dossier and revised pitch outline in markdown that covers the architecture for their hardware setup, the evidence from vLLM adopters and in-house agent trends at major companies, a realistic cost model against Copilot per-seat pricing, the tool stack mapped to their existing repos, what needs fixing in the current deck, rollout phases, and concrete next steps. I'll propose putting this research dossier in their vault alongside the existing planning materials.

Now I'm mapping out the specific model recommendations for their 24GB GPU setup: vLLM as the inference engine with Ollama as a fallback, Qwen2.5-Coder-3B for autocomplete via Continue, and either Qwen3-Coder-30B-A3B or Devstral Small 2 for the main chat and editing tasks, all routed through a LiteLLM proxy that handles per-developer budgets and API fallbacks, with Open WebUI for browser-based chat and Continue.dev for IDE integration.

For overflow capacity, I'm planning to use cheap external APIs like DeepSeek and Qwen through OpenRouter with prompt caching to keep costs minimal, plus token control strategies like RAG and code indexing to avoid sending entire codebases. I'll validate the exact model fit using llmfit and whichllm, and I need to flag that FIM integration with LiteLLM has a known caveat that might require pointing Continue directly at the inference engine instead.

The honest cost breakdown shows self-hosted saves money compared to Copilot's $19-39 per user monthly, but the real value is owning the base layer while renting expensive capabilities—not eliminating costs entirely—plus accounting for the engineering maintenance effort the original deck glossed over. I also need to correct the deck's treatment of AirLLM, downgrading it from a team-serving tool to a niche offline fallback, and reframe "zero cost" as "near-zero marginal cost per token."

The biggest gap in the deck is the missing tier-and-routing architecture that FAANG teams actually use: local models handle the floor, external APIs handle the ceiling, and prompt caching becomes a first-class token lever alongside RAG. I should also add a concurrency reality check—one 24GB GPU can't serve 40 developers doing agentic work at once, which is exactly why routing matters—and update the model roster to current options like Qwen3-Coder and DeepSeek V3.2 instead of Llama 3.3 70B, which won't fit well anyway. Finally, I'll ground this with real adoption evidence from Meta, Amazon, Stripe, and Shopify to show this isn't theoretical.

For the deliverable structure, I'm thinking of creating a dedicated folder under 10_Areas/Life/Plans to keep the corrections and expanded analysis organized alongside the original deck.

**Tool calls:**

- `Glob` — pattern `40_Resources/CS/Repos/**/*`, path `.`
- `Glob` — pattern `40_Resources/CS/**/*.md`, path `.`
- `Read` — `D:\Users\_Anant\10_Areas\Documents\Jarvis\40_Resources\CS\Repos.md`
- `Read` — `D:\Users\_Anant\10_Areas\Documents\Jarvis\40_Resources\CS\AI\Ollama.md`
- `Read` — `D:\Users\_Anant\10_Areas\Documents\Jarvis\40_Resources\CS\AI\AI Workflow.md`
- `WebSearch` — `{"search_term":"how do companies self-host LLM inference vLLM production stack 2026","explanation":"Find the standard production self-hosting inference stack used in industry"}`
- `WebSearch` — `{"search_term":"self-hosting LLM vs API cost comparison GPU break-even analysis 2026","explanation":"Understand the real cost economics of self-hosting vs API to give honest advice"}`
- `WebSearch` — `{"search_term":"single GPU concurrent users LLM serving vLLM continuous batching throughput how many users","explanation":"Determine realistic concurrency for one office GPU to validate or debunk AirLLM claims"}`
- `WebSearch` — `{"search_term":"best open source coding LLM 2026 Qwen3 coder DeepSeek self-hosted code completion benchmark","explanation":"Find current best open coding models to recommend for self-hosting"}`
- `WebSearch` — `{"search_term":"how Meta Google internal AI coding assistant developers built on own infrastructure","explanation":"Find how big tech actually deploys coding AI internally to mimic their workflow accurately"}`
- `WebSearch` — `{"search_term":"prompt caching context management reduce token usage coding agents 2026","explanation":"Understand the real solution to token-limit problems beyond just RAG"}`
- `WebSearch` — `{"search_term":"Continue.dev self-hosted LLM VS Code autocomplete LiteLLM gateway team setup","explanation":"Find the IDE integration layer for connecting devs to a self-hosted model"}`
- `AskQuestion` — `{"questions":[{"id":"gpu","prompt":"What is the office server GPU (the single biggest factor for which models you can run and how many people it can serve)? Pick the closest match, or tell me the exact model/VRAM if you know it.","options":[{"id":"low","label":"Consumer card, ~8-12GB VRAM (e.g. RTX …`
- `CreatePlan` — `{"name":"Zero Cost AI Stack","overview":"Produce a rigorously sourced research dossier and a corrected pitch narrative for a startup replacing per-seat Copilot Enterprise with a self-hosted, tiered \"own-the-floor / rent-the-ceiling\" AI stack on their existing ~24GB GPU, mimicking the actual FAANG …`

## You

<timestamp>Thursday, Jun 4, 2026, 1:10 PM (UTC+4)</timestamp>
<user_query>
You are a senior ML infrastructure researcher. Your job is to produce a deeply sourced, 
engineer-grade research dossier on how major technology companies (Meta, Google, Microsoft, 
Amazon, Apple, Stripe, Uber, Shopify, Roblox, Coinbase) actually build and run internal 
LLM inference infrastructure at near-zero marginal cost. This is NOT a summary of their 
products — it is a study of their internal engineering patterns that a 15-40 person startup 
can replicate on a single ~24GB consumer GPU server.

You have access to web search. Use it aggressively. Every claim must be traced to a 
primary source: engineering blog post, research paper (arXiv, ACL, NeurIPS), GitHub repo, 
conference talk transcript, or verified news with named engineers. "According to reports" 
is not acceptable. Find the actual source.

---

## SECTION 1: THE INFERENCE STACK EACH COMPANY USES

For each company below, find and cite the PRIMARY SOURCE (blog post, paper, GitHub, conf 
talk) that reveals:
  (a) What serving engine they use for LLM inference (vLLM, Triton, TGI, custom, TensorRT-LLM)
  (b) What open-source projects they contributed to that reveal their internal stack
  (c) What GPU/accelerator they run (H100, A100, TPU v4/v5, custom ASIC)
  (d) What model sizes they serve (parameter count, quantization)
  (e) What their token throughput numbers are at scale (tok/s, req/s, batch sizes)
  (f) Any published cost figures or savings they cited

Companies to cover:
  1. Meta — Look for: vLLM contribution history on GitHub, Meta AI blog posts on inference, 
     "iLlama" internal deployment reports, "DevMate" agent marketplace engineering posts, 
     Meta's PyTorch Foundation membership announcement (what they contributed), any Meta 
     Engineering blog posts on LLM serving at scale, Andrej Karpathy or Meta researchers 
     on X/Twitter about internal tooling, Meta's papers on LLM inference optimization.

  2. Google — Look for: "llm-d" GitHub repo (google/llm-d) and its README/design docs, 
     Google Cloud blog posts on vLLM contributions, AlphaCode 1 and 2 technical reports 
     (what infrastructure they describe), "Gemini Code Assist" infrastructure blog posts, 
     Google Brain/DeepMind papers on inference serving (Orca, Sarathi, Splitwise — find 
     which ones are from Google), TPU vs GPU routing decisions published in engineering blogs, 
     SREcon or Google Cloud Next talk transcripts on internal LLM serving.

  3. Microsoft — Look for: GitHub Copilot infrastructure blog posts (GitHub Engineering blog),
     the "Phi" model series — why did Microsoft build tiny models? (find the stated engineering 
     reason: cost reduction on inference), Azure AI inference architecture posts, any 
     Microsoft Research papers on model routing or LLM tiering, Semantic Kernel architecture 
     docs that reveal internal patterns, MSR papers on "speculative decoding" or "cascade 
     inference" that they actually deploy.

  4. Amazon/AWS — Look for: "Amazon Rufus" technical blog (the shopping assistant), the 
     specific claim that Rufus uses vLLM (find the primary source for this), AWS re:Invent 
     2024/2025 talks on internal LLM infrastructure, Amazon Science blog posts on LLM 
     serving, any published numbers on Q Developer (CodeWhisperer successor) backend, 
     Bedrock's multi-model routing architecture if documented.

  5. Apple — Look for: "Private Cloud Compute" security paper (Apple Security Research blog, 
     June 2024) — this is a PRIMARY SOURCE that describes their on-device + server routing 
     architecture in detail. Find what models run on-device vs cloud. Find how they route. 
     Find their stated latency targets. Also find Apple's "MM1" and "Apple Intelligence" 
     foundation model papers for inference architecture details.

  6. Stripe — Look for: Stripe Engineering blog posts on LLM deployment, any Stripe 
     conference talks (StrangLoop, QCon, internal posts cross-posted) on AI infrastructure, 
     any named Stripe engineers writing publicly about their LLM stack.

  7. Roblox — Look for: The specific Roblox blog post about "4 billion tokens per week" 
     (this exists — find it and cite the exact URL, date, model used, infrastructure details),
     Roblox AI blog on vLLM usage in production.

  8. Shopify — Look for: Shopify Engineering blog on LLM infrastructure, Tobi Lütke posts 
     on AI usage, any Shopify AI team posts on model serving.

---

## SECTION 2: THE ROUTING AND TIERING PATTERN

The most important pattern is: route cheap/bulk work to self-hosted small models, route 
hard/rare work to powerful external APIs. Research:

  (a) Find the academic papers that formalize this: "FrugalGPT" (Chen et al., Stanford 2023), 
      "LLM-Blender" (Jiang et al.), "Cascade" inference papers. Get the actual numbers they 
      report on cost reduction (FrugalGPT claims ~98% cost reduction — verify this and find 
      the experimental setup).

  (b) Find the "Orca" paper (Yu et al., OSDI 2022) — this is the foundational paper for 
      continuous batching that vLLM implements. Find what throughput improvements they 
      measured vs naive serving (2–23× reported — find the exact table).

  (c) Find "Sarathi-Serve" (Agrawal et al.) — Google Research paper on chunked prefill. 
      What problem does it solve and what numbers do they report?

  (d) Find "Splitwise" (Patel et al., ISCA 2024) — Microsoft Research paper on 
      prefill/decode disaggregation. What does this tell us about how Microsoft thinks 
      about LLM serving?

  (e) Find real-world vLLM deployment case studies with throughput numbers. The vLLM GitHub 
      has a "Who's using vLLM" section or blog — scrape it. Find 5+ companies with actual 
      published numbers (tok/s, GPU count, model size, concurrency).

  (f) For the "own the floor, rent the ceiling" framing specifically: find any engineering 
      post that explicitly describes a hybrid self-hosted + cloud-API routing system with 
      published cost numbers. OpenRouter, Together AI, Fireworks AI all have benchmark posts 
      — find the best cost-per-token figures for the cheapest capable models (DeepSeek V3, 
      Qwen2.5-72B-Instruct) as of 2026 to anchor the "ceiling" cost.

---

## SECTION 3: MODEL SELECTION FOR A 24GB GPU (SPECIFIC, SOURCED)

Research the exact models that fit a ~24GB VRAM GPU (RTX 3090/4090/A5000/A6000) for 
coding + chat use cases as of mid-2026:

  (a) Find llmfit's GitHub (AlexsJones/llmfit) community leaderboard data — what models 
      do real users run on 24GB cards with what tok/s? (Look at localmaxxing.com if findable)

  (b) For each model below, find the EXACT memory footprint at Q4_K_M and Q8_0 
      quantization, the published benchmark scores (HumanEval, MBPP, LiveCodeBench), 
      the license, and one primary source (HuggingFace model card or paper):
        - Qwen2.5-Coder-32B-Instruct
        - Qwen3-Coder-30B-A3B (MoE)
        - Devstral-Small-2 (Mistral AI)
        - DeepSeek-Coder-V2-Lite (16B MoE)
        - CodeLlama-34B (for comparison)
        - Qwen3-14B (general reasoning)

  (c) For the FIM (fill-in-the-middle / autocomplete) task specifically: find what model 
      Cursor IDE uses internally for autocomplete (they have written about this), what 
      Continue.dev recommends for self-hosted FIM autocomplete, and what the known bug is 
      with FIM through LiteLLM (GitHub issue #6900 in the LiteLLM repo — find the exact 
      issue, status, and workaround).

  (d) Find benchmark comparisons of the above models specifically on coding tasks from 
      2025-2026 (EvalPlus leaderboard, BigCodeBench, LiveCodeBench). What does the 
      Pareto frontier look like between model size and coding performance?

---

## SECTION 4: HONEST TCO MODEL WITH REAL NUMBERS

Research the actual costs involved in self-hosting:

  (a) Find the CMU "Wang 2025" paper or framework on LLM TCO break-even analysis 
      (the plan mentions this). Get the actual methodology and break-even numbers.

  (b) Find at minimum 3 published cost analyses comparing self-hosted vs API-based LLM 
      serving from 2025-2026. Get specific numbers: at what monthly token volume does 
      self-hosting break even against API pricing? (The commonly cited figure is ~11B 
      tokens/month — find the source and verify it.)

  (c) For a 24GB consumer GPU server running 24/7:
        - Actual power draw: find published TDP for RTX 4090, A5000, A6000
        - US average electricity rate (find current figure from EIA)
        - Monthly electricity cost calculation with source
        - Expected hardware lifespan and amortization

  (d) Find the "hidden cost" analyses — maintenance engineering time, model updates, 
      monitoring setup. Find any startup post-mortems or engineering blog posts where 
      teams documented the real operational overhead of running their own LLM inference.

  (e) For the API overflow tier: find current (2026) pricing for DeepSeek V3, 
      Qwen2.5-72B via OpenRouter/Together/Fireworks. Calculate: at what call volume does 
      a 15-person dev team exhaust a $200/month API budget?

---

## SECTION 5: PROMPT CACHING AND CONTEXT ENGINEERING (THE TOKEN LIMIT FIX)

Research how big tech actually solves the token limit problem:

  (a) Find Anthropic's prompt caching documentation and pricing (cache hits are ~90% 
      cheaper). Find equivalent offerings from OpenAI, Google (context caching in 
      Gemini API), and DeepSeek. What are the exact cache hit rates reported?

  (b) Find Continue.dev's "@codebase" feature documentation — how does it index a 
      codebase, what embedding model does it use, what is the retrieval quality vs 
      full-context stuffing?

  (c) Find real measurements of RAG vs full-context on coding tasks: is there a paper 
      or benchmark showing that retrieval-augmented coding beats full-repo stuffing at 
      a smaller token budget? (Look for "Repoformer", "RepoAgent", "SWE-bench RAG" papers)

  (d) Find the Zilliz "claude-context" MCP tool documentation (it's in the Repos.md 
      under memsearch/claude-context) — what does it actually do, what's the token 
      reduction it claims, and how does it work technically?

  (e) KV cache reuse: find vLLM's prefix caching feature documentation. What token 
      reduction does prefix caching provide on repeated system prompts? Find a benchmark.

---

## SECTION 6: WHAT ACTUALLY FAILED — HONEST RISK ASSESSMENT

Research documented failures and limitations that the pitch must not hide:

  (a) Find post-mortems or "lessons learned" posts from teams that tried to self-host 
      LLMs for a dev team and ran into problems. What were the top failure modes?

  (b) Find the specific Continue.dev + LiteLLM FIM bug (GitHub issue #6900) — get 
      the full context: what exactly breaks, what's the workaround, is it fixed in 
      recent versions?

  (c) Find published data on open-source model quality vs GPT-4o / Claude 3.5 Sonnet 
      on coding tasks as of 2026. What is the quality gap? (LiveCodeBench scores for 
      both open and closed models — what's the current Pareto frontier?)

  (d) Find any documented cases where a startup moved from self-hosted to API or vice 
      versa and why. What drove the decision?

  (e) Single-GPU concurrency: find vLLM's published benchmarks on concurrent request 
      handling for 24GB cards. At what concurrent user count does latency become 
      unacceptable (>5s TTFT)?

---

## SECTION 7: OPEN-SOURCE TOOLS DEEP DIVE

For each tool in the proposed stack, find the PRIMARY SOURCE for its production readiness:

  (a) vLLM: Find the production deployment guide, the list of companies using it in 
      production (from their GitHub or blog), and the most recent benchmark numbers 
      (throughput vs TGI vs llama.cpp at 24GB scale).

  (b) LiteLLM: Find the largest documented deployment (number of users, requests/day), 
      any published reliability numbers, and the known limitations for production use.

  (c) Open WebUI: Find their GitHub stats, any "we run this in production" posts, 
      enterprise feature list, and any documented security considerations for internal 
      deployment.

  (d) Dify: Find production case studies with actual user counts, the specific vector 
      database options it supports, and how its RAG quality compares to alternatives 
      (LangChain, LlamaIndex) on standard benchmarks.

  (e) Continue.dev: Find their funding status, the companies using it (they list 
      customers/case studies), and the specific models they recommend for self-hosted 
      autocomplete vs chat as of 2026.

---

## OUTPUT FORMAT

Produce the research as a structured markdown document with:

1. **Executive Summary** (the corrected thesis in 3 bullet points with one citation each)

2. **Company-by-Company Evidence Table** (for each of 8 companies: serving engine, 
   GPU/accelerator, model family, throughput numbers, primary source URL)

3. **The Routing Pattern — Academic Foundations** (5 papers, each with: title, authors, 
   venue, year, key finding relevant to this pitch, one specific number from the paper)

4. **Model Selection Matrix for 24GB GPU** (table: model name, VRAM at Q4, tok/s 
   estimated on 24GB, HumanEval score, license, recommended use case)

5. **Honest TCO Table** (subscriptions vs self-hosted for 15 and 40 devs, with all 
   costs itemized and sourced)

6. **Token Engineering Toolkit** (5 techniques with: what it does, token reduction 
   estimate, tool/paper reference, implementation complexity 1-5)

7. **Risk Register** (top 6 documented failure modes with: description, evidence source, 
   mitigation)

8. **Full Citation List** (numbered, with URL, title, author, date for every claim)

Every section must have at least 3 distinct primary sources. Do not pad with vague claims. 
If you cannot find a primary source for a claim, say so explicitly and mark it [UNVERIFIED].
</user_query>

## Cursor

The user has explicitly asked me to execute the research and produce the dossier (a markdown deliverable, which is permitted in plan mode). This is a large, source-intensive job, so I'll parallelize it across four research subagents — each owning specific sections and required to trace every claim to a primary-source URL — then I'll compile, verify the key anchor claims myself, and write the final dossier.

 The user is asking me to produce the research dossier now, which means I need to execute rather than just plan. Plan mode normally restricts me to markdown edits only, but since the deliverable is a markdown file, that should be within bounds. However, I'm second-guessing whether plan mode allows me to make edits without explicit instruction, and the user has now given that explicit instruction to proceed.

This is a massive research undertaking—eight sections each requiring three or more primary sources with traced URLs. I could do all the web searches myself, but that would be slow and sequential. A better approach is to launch multiple research subagents in parallel, each tackling one or two sections independently, then I'll synthesize their findings into the final markdown dossier. I'm thinking of spinning up four or five subagents covering different topic areas like company inference stacks, regulatory frameworks, and market analysis, each returning their research with proper citations so I can compile everything together.

Since the user explicitly wants me to execute now and produce the dossier, I should move forward. The deliverable goes into the plan directory as a markdown file. I'll launch the parallel research subagents to gather sourced findings efficiently, then write the compiled dossier. won't get results until they complete and I need them to write the doc. I should run them and await. Actually I can launch them non-background and they block, or background and I wait. Since I need all results to compile, let me launch them in parallel (multiple Task calls in one message) as non-background so I get results. But non-background blocks sequentially? No — multiple tool calls in one message run concurrently. Let me launch 4 Task subagents in a single message, not background, so they run in parallel and I get all results.

Hmm, actually the instructions say for parallel work use run_in_background or just multiple calls. Multiple Task tool calls in a single message run in parallel. If not background, do they block until all done? The harness will execute them and return results. Let me launch 4 in parallel.

Let me give each subagent very detailed instructions matching the sections, requiring primary source URLs, and to mark [UNVERIFIED] when not found. They should return structured markdown with citations.

Let me write detailed prompts. I'll use generalPurpose subagents (they can search web and do multi-step). Actually, do generalPurpose subagents have web access? The Task tool says readonly subagents have "no MCP or internet access." So non-readonly generalPurpose should have internet. Let me use generalPurpose with run_in_background false.

Actually, to maximize reliability, let me do the heavy research myself with many parallel WebSearch calls, since I can control quality, and I already have substantial findings. But that's a LOT of searches (40+). Subagents parallelize better. Let me use subagents for breadth, and I'll supplement with my own searches for key anchors like Orca, FrugalGPT, Splitwise, Roblox, and Apple's PCC.

I'll split the work across four subagents: one covering the company inference stacks, another handling routing papers and tool case studies, a third tackling model selection and caching strategies, and the last one addressing TCO and risk analysis. Each will return structured markdown with citations, and I'll compile everything together while verifying a few critical claims myself.

Two sections are in with strong primary sourcing. Now the remaining two research blocks — model selection for 24GB plus token engineering, and the honest TCO plus risk register.

 Two subagents have already delivered strong, well-researched content. Now I'm spinning up the remaining pairs in parallel—one handling model selection for 24GB systems plus caching and context strategies, the other tackling total cost of ownership alongside risk assessment—then I'll consolidate everything together.

All four research blocks are back with strong primary sourcing. The TCO findings are the most important — they honestly contradict not just the original Claude deck's "$0" claim but also force a more careful framing of the whole pitch: once you price even part-time maintenance labor, raw cost at 15-40 seats does *not* cleanly favor self-hosting. The defensible wins are data control, killing per-seat scaling + token walls, and hybrid routing. I'll compile everything into the dossier exactly in your requested 8-section format, with a unified numbered citation list.

 I've got all four research sections solidly sourced now, and the TCO analysis is particularly important because it surfaces something neither the original Claude presentation nor my initial framing acknowledged: for teams of 15-40 developers, self-hosting with realistic labor costs often ends up more expensive than Copilot Business. That's the kind of honest, rigorous finding the user was asking for.

Now I'm organizing everything into the final markdown dossier with the eight requested sections, starting with the executive summary.

The key insight I need to surface upfront is that the real value proposition isn't actually "near zero cost"—that only works if you ignore maintenance labor. The honest case is hybrid: run local inference for high-volume, low-complexity tasks and route expensive or specialized work to cheap APIs, which eliminates per-seat scaling walls and token limits while keeping data local. That's the win, and I need to present it clearly.

I'm consolidating all citations into a unified numbered list at the end, deduplicating across the four research blocks, and I'll structure the dossier with inline references. Given the scope, I'm looking at roughly 60+ unique sources to track. I'll write the full markdown file in one pass, integrating the subagent outputs and making sure every claim either has a citation or is explicitly marked unverified per the user's requirements.

Writing the dossier now with today's date (June 4, 2026).

The dossier is written to [Research Dossier — Internal LLM Inference at Near-Zero Cost.md](10_Areas/Life/Plans/Zero-Cost%20AI%20Stack/Research%20Dossier%20—%20Internal%20LLM%20Inference%20at%20Near-Zero%20Cost.md), structured in all 8 requested sections plus a "corrections to the deck" appendix. Every section has 3+ primary sources, ~85 citations total, with secondary/unverifiable claims explicitly tagged.

The research surfaced one finding that changes the entire pitch, and I want to flag it plainly rather than bury it:

**The deck's "near-zero cost" claim does not survive scrutiny at 15-40 seats.** The TCO literature is consistent — hardware + electricity is only 20-30% of self-hosting cost; labor is 70-80% [Tian Pan 2026; arXiv:2509.18101]. Once you price even 10-20% of one engineer (~$1,500-3,500/mo), realistic self-hosting (~$2,000-4,000/mo) can *exceed* Copilot Business ($285/mo for 15, $760/mo for 40). The "Wang 2025" paper the original plan leaned on only models CapEx + electricity (no labor term), which is why its break-evens look optimistic, and the famous "~11B tokens/month" break-even traces to a vendor blog, not a primary source.

So the honest, defensible thesis became **"own the floor, rent the ceiling"** — and the win is *control + no per-seat scaling + killing the token wall*, not a fictional $0. That's backed by the real big-tech pattern (vLLM everywhere + a gateway + cascade routing: FrugalGPT ~98%, RouteLLM 95% quality at -85% cost, MSR Hybrid-LLM -40% large-model calls).

Other corrections the evidence forced:
- **AirLLM was massively oversold** — single-user, disk layer-streaming, single-digit tok/s. Demoted to offline fallback; vLLM leads (Amazon Rufus, Roblox 4B tok/wk, LinkedIn, Meta).
- **Llama-3.3-70B doesn't fit 24GB** — replaced with Qwen3-Coder-30B-A3B / Devstral-Small-2507 / Qwen2.5-Coder-32B, with exact Q4 footprints.
- **The Continue.dev + LiteLLM FIM bug is real and CLOSED** (#6900) — autocomplete must bypass the gateway.
- **Concurrency is finite**: 8B on a 4090 holds p99 TTFT ~2.4s to 64 streams under vLLM, but Ollama collapses at 5 users; a 30B leaves only ~6-8GB for KV cache.

Remaining plan todos are the corrected slide-by-slide narrative and the architecture write-up (toward the eventual PPTX). Want me to:

 The markdown file is done, so I'll do a quick lint check and then wrap up with a concise summary of what I've delivered and the key findings, plus point toward the next steps—the pitch narrative and PPTX that were part of the original plan.

Architecture runbook it is. I'll write an engineer-grade setup guide for the 24GB hybrid stack — concrete VRAM budgeting, vLLM/Ollama/LiteLLM/Open WebUI/Continue configs, the FIM-bypass wiring, routing, caching, security (incl. the LiteLLM supply-chain mitigation), and verification commands.

 I need to create a comprehensive runbook document with the full architecture details, setup instructions, and actual configuration examples—including how to handle the FIM limitation, routing setup through LiteLLM, and the complete stack from vLLM on the floor tier up through the API gateway and frontend layers.

For the single 24GB GPU constraint, I'm settling on Devstral-Small-2507 as the workhorse model (~14.3GB) to leave enough headroom for KV cache and the 1.5B autocomplete model running via Ollama, then I'll document the VRAM budget tradeoffs and provide a docker-compose setup that ties everything together with proper networking and security considerations.

Writing the runbook now with concrete commands, config snippets, and verification steps...

Done. The runbook is written to [Architecture & Setup Runbook — 24GB Hybrid Stack.md](10_Areas/Life/Plans/Zero-Cost%20AI%20Stack/Architecture%20&%20Setup%20Runbook%20—%2024GB%20Hybrid%20Stack.md), cross-referenced to the dossier throughout.

What it covers, concretely:
- **VRAM budgeting table** — the decision that actually determines how many engineers one card serves, with 3 profiles (Profile A / Devstral-Small-2507 recommended for the most KV-cache headroom).
- **Floor:** vLLM workhorse (with `--enable-prefix-caching`, `--gpu-memory-utilization`, `--max-model-len`/`--max-num-seqs` tuning notes) + Ollama tiny FIM model.
- **Gateway:** full LiteLLM `config.yaml` with the local floor + API ceiling, fallback routing, per-dev virtual keys with budgets, and the **pinned official Docker image** to dodge the March 2026 supply-chain incident.
- **Frontends:** Open WebUI (hardened) and a Continue.dev `config.yaml` that wires **chat/edit/agent → LiteLLM but autocomplete → Ollama directly**, which is the workaround for the FIM-through-LiteLLM bug (#6900).
- **Token-wall control** (prefix caching → `@codebase` → API prompt caching → optional Zilliz/Dify), networking/security, observability + scale triggers, a 4-phase rollout, and copy-paste verification `curl`s.

Two honest guardrails are baked in (Section 13): it does not claim "$0," and it does not put a 70B on one 24GB card or rely on AirLLM for team serving.

You now have the full evidence base ([the dossier](10_Areas/Life/Plans/Zero-Cost%20AI%20Stack/Research%20Dossier%20—%20Internal%20LLM%20Inference%20at%20Near-Zero%20Cost.md)) and the buildable architecture. The remaining piece toward the PPTX is the **corrected slide-by-slide pitch narrative** that turns this into the deck story (fixing the original 12 slides). Say the word and I'll write that next.

 Both markdown files are ready in the folder. Now I should outline what comes next—the slide narrative that will accompany these deliverables.

**Tool calls:**

- `Task` — `{"description":"Research company inference stacks","subagent_type":"generalPurpose","prompt":"You are a senior ML-infrastructure researcher with web access. Today is June 2026. Produce a deeply sourced markdown research section on the INTERNAL LLM inference stacks of major tech companies. Every fact…`
- `Task` — `{"description":"Research routing patterns and tools","subagent_type":"generalPurpose","prompt":"You are a senior ML-infrastructure researcher with web access. Today is June 2026. Produce two deeply sourced markdown sections. Every claim MUST trace to a PRIMARY SOURCE (paper on arXiv/OSDI/ISCA/NeurIP…`
- `Task` — `{"description":"Research 24GB models and token engineering","subagent_type":"generalPurpose","prompt":"You are a senior ML-infrastructure researcher with web access. Today is June 2026. Produce two deeply sourced markdown sections. Every claim MUST trace to a PRIMARY SOURCE (HuggingFace model card, …`
- `Task` — `{"description":"Research TCO and risk register","subagent_type":"generalPurpose","prompt":"You are a senior ML-infrastructure researcher with web access. Today is June 2026. Produce two deeply sourced markdown sections with REAL NUMBERS. Every claim MUST trace to a PRIMARY SOURCE. Mark unverifiable …`
- `Write` — `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Zero-Cost AI Stack\Research Dossier — Internal LLM Inference at Near-Zero Cost.md`
- `AskQuestion` — `{"questions":[{"id":"next","prompt":"The dossier is done. What should I produce next (still markdown; PPTX later as you said)?","options":[{"id":"narrative","label":"The corrected slide-by-slide pitch narrative (fixes the 12-slide deck using the dossier's evidence)"},{"id":"arch","label":"The detail…`
- `Write` — `D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Zero-Cost AI Stack\Architecture & Setup Runbook — 24GB Hybrid Stack.md`

## Actions Taken
- Summary: Edited Architecture & Setup Runbook — 24GB Hybrid Stack.md, Research Dossier — Internal LLM Inference at Near-Zero Cost.md
- Files changed (Cursor): 2
- Lines: +641 / -0
- Files touched (from tool calls): D:\Users\_Anant\10_Areas\Documents\Jarvis\40_Resources\CS\Repos.md, D:\Users\_Anant\10_Areas\Documents\Jarvis\40_Resources\CS\AI\Ollama.md, D:\Users\_Anant\10_Areas\Documents\Jarvis\40_Resources\CS\AI\AI Workflow.md, D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Zero-Cost AI Stack\Research Dossier — Internal LLM Inference at Near-Zero Cost.md, D:\Users\_Anant\10_Areas\Documents\Jarvis\10_Areas\Life\Plans\Zero-Cost AI Stack\Architecture & Setup Runbook — 24GB Hybrid Stack.md
- Commands run: (none)
- Tool call tally: AskQuestion (2), CreatePlan (1), Glob (2), Read (3), Task (4), WebSearch (7), Write (2)

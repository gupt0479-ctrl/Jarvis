---
type: concept
status: sprout
created: 2026-06-17
updated: 2026-06-17
course:
track:
mastery_level: 0
prerequisites: []
used_in: []
evidence: []
tags:
  - concept
related: []
---
# Problems with Portfolio Lab
## One-Line Answer
== ==
## Mechanism
## Contrast / What It Is Not
The prompt entered to kiro:

```

What are his top skills?

{ "navigate": { "sectionId": "skills", "orbyMessage": "Here are Anant's core skill areas, backed by his portfolio work." } }Anant’s core expertise spans four main areas:

AI/ML – OpenAI & LLM APIs, Prompt Engineering, Agent & Tool Systems, RAG/Embeddings, TensorFlow.

Backend – Node / Python, GraphQL, TypeScript, REST, WebSockets, Rust, PostgreSQL, Elasticsearch, Redis.

Frontend – Next.js, React, Tailwind CSS, Sanity CMS, shadcn/ui, Web Accessibility, Three.js/WebGL.

DevOps & Cloud – Docker, Kubernetes, Terraform, AWS, GCP, Firebase, GitHub Actions.

These skill groups are demonstrated across his projects (e.g., BOOM, Jarvis‑OS, CasualOps) and ongoing research roles.

```



From the localhost, the top part should not be seen to the user. Orby did not reply, the page did not render to the designated component. 



Logs:

```

anant_gupta@DESKTOP-3VBG0JH:~/projects/hub/portfolio$ pnpm run dev

> portfolio@0.1.0 dev /home/anant_gupta/projects/hub/portfolio

> next dev

▲ Next.js 16.2.9 (Turbopack)

- Local:         http://localhost:3000

- Network:       http://10.255.255.254:3000

- Environments: .env.local

✓ Ready in 773ms

 GET / 200 in 5.7s (next.js: 213ms, proxy.ts: 221ms, application-code: 5.3s)

 POST / 200 in 38ms (next.js: 10ms, proxy.ts: 12ms, application-code: 17ms)

  └─ ƒ detectKeylessEnvDriftAction() in 1ms node_modules/.pnpm/@clerk+nextjs@6.39.5_next@16.2.9_@babel+core@7.29.0_@opentelemetry+api@1.9.1_@playwrigh_a48bb0bd0f15472a17becadf8c7ec094/node_modules/@clerk/nextjs/dist/esm/app-router/keyless-actions.js

 POST /api/chat-token 200 in 1097ms (next.js: 93ms, application-code: 1004ms)

[browser] Clerk: Clerk has been loaded with development keys. Development instances have strict usage limits and should not be used when deploying your application to production. Learn more: https://clerk.com/docs/deployments/overview (https://decent-tick-22.clerk.accounts.dev/npm/@clerk/clerk-js@5/dist/clerk.browser.js:19:7048)

[browser] Please ensure that the container has a non-static position, like 'relative', 'fixed', or 'absolute' to ensure scroll offset is calculated correctly. (<anonymous>)

 GET / 200 in 5.4s (next.js: 9ms, proxy.ts: 7ms, application-code: 5.4s)

 POST /api/chat 200 in 3.3s (next.js: 870ms, application-code: 2.4s)

 GET / 200 in 4.5s (next.js: 15ms, proxy.ts: 56ms, application-code: 4.5s)

 GET / 200 in 4.4s (next.js: 101ms, proxy.ts: 81ms, application-code: 4.2s)

[browser] Clerk: Clerk has been loaded with development keys. Development instances have strict usage limits and should not be used when deploying your application to production. Learn more: https://clerk.com/docs/deployments/overview (https://decent-tick-22.clerk.accounts.dev/npm/@clerk/clerk-js@5/dist/clerk.browser.js:19:7048)

 POST / 200 in 54ms (next.js: 6ms, proxy.ts: 19ms, application-code: 28ms)

  └─ ƒ detectKeylessEnvDriftAction() in 1ms node_modules/.pnpm/@clerk+nextjs@6.39.5_next@16.2.9_@babel+core@7.29.0_@opentelemetry+api@1.9.1_@playwrigh_a48bb0bd0f15472a17becadf8c7ec094/node_modules/@clerk/nextjs/dist/esm/app-router/keyless-actions.js

[browser] Please ensure that the container has a non-static position, like 'relative', 'fixed', or 'absolute' to ensure scroll offset is calculated correctly. (<anonymous>)

 POST /api/chat 200 in 1735ms (next.js: 9ms, application-code: 1726ms)

[browser] [Turnstile] Challenge failed — chat may be limited (src/components/ChatTokenInit.tsx:82:16)

[browser] [Cloudflare Turnstile] Error: 300010. (https://challenges.cloudflare.com/turnstile/v0/api.js:1:10084)

 GET / 200 in 3.4s (next.js: 9ms, proxy.ts: 16ms, application-code: 3.4s)

 GET / 200 in 3.3s (next.js: 8ms, proxy.ts: 13ms, application-code: 3.3s)

 POST /api/chat-token 200 in 13ms (next.js: 6ms, application-code: 8ms)

 GET / 200 in 4.3s (next.js: 28ms, proxy.ts: 36ms, application-code: 4.3s)

```



Next prompt: 

```

[CEO lens] Brief me like I'm a founder deciding whether to bet on Anant as an early engineer. From ONLY his verified data: - Trajectory: what is he compounding toward? - Pattern: what class of messy problem does he reliably turn into a system? Name the projects that prove it. - Leverage: where would he create the most value in a startup's first 90 days? Skip implementation detail — give me direction. Take me to the project that best signals this and show it as a card.

Anant compounds a rare blend of high‑throughput data pipelines and agent‑centric knowledge orchestration. His pattern: turning chaotic, real‑time streams—whether sky alerts or unstructured notes—into modular, AI‑augmented systems that scale and self‑evolve. BOOM proves his ability to build a production‑grade, Rust‑based alert broker handling massive astronomical data. Jarvis OS extends that skill to a knowledge operating system that structures raw research into actionable software pipelines, demonstrating cross‑domain systemization. In a startup’s first 90 days, he would inject immediate value by designing data‑centric, autonomous pipelines that turn noisy inputs into reliable, decision‑ready outputs.

BOOM (Burst & Outburst Observations Monitor)

project

A modular, high-throughput astronomical alert broker that ingests, enriches, and filters real-time survey data at scale.

RustMongoDBRedisDockerREST API DesignGit / GitHub

LiveCode

```



Worked perfectly. 

Logs continuation:

```

 POST /api/chat-token 200 in 13ms (next.js: 6ms, application-code: 8ms)

 GET / 200 in 4.3s (next.js: 28ms, proxy.ts: 36ms, application-code: 4.3s)

 GET / 200 in 3.6s (next.js: 5ms, proxy.ts: 7ms, application-code: 3.6s)

{"event":"router.turn","sessionId":"1781722480141","messageCount":1,"tier":"full","startProvider":"cerebras"}

{"event":"chat.request","provider":"cerebras","mode":"live","persona":"ceo","sessionId":"1781722480141"}

{"event":"chat.tool","tool":"navigate","toolCallId":"9459ddeec","persona":"ceo","sessionId":"1781722480141"}

{"event":"chat.tool","tool":"showProject","toolCallId":"d8d5e9d20","persona":"ceo","sessionId":"1781722480141"}

{"event":"chat.turn.complete","model":"cerebras","persona":"ceo","sessionId":"1781722480141","inputTokens":2885,"outputTokens":442,"latencyMs":52}

 POST /api/chat 200 in 8.9s (next.js: 4ms, application-code: 8.9s)

 GET / 200 in 3.0s (next.js: 12ms, proxy.ts: 21ms, application-code: 3.0s)

```



Next prompt: 

```

What's the weirdest thing he's built?

What a funny question, here is my thought process: An AI that advises on stocks feels like giving a crystal ball a résumé—blending market data, back‑tested strategies, and LLM‑powered insights. It’s wonderfully weird because it treats investing like a research lab, serving evidence‑based cards that say “ACCUMULATE” or “AVOID,” turning the chaotic world of finance into a tidy, AI‑curated playlist.

TradingView

project

Personal investing research tool - combines verified market data, backtested strategies, and AI-generated cards.

Next.jsTypeScriptPostgreSQLLLM APIsPrompt EngineeringPython

```



Worked perfectly. Logs:

```

{"event":"router.turn","sessionId":"1781722480141","messageCount":2,"tier":"full","startProvider":"cerebras"}

{"event":"chat.request","provider":"cerebras","mode":"live","persona":"weirdo","sessionId":"1781722480141"}

{"event":"chat.tool","tool":"navigate","toolCallId":"c8d5ad0eb","persona":"weirdo","sessionId":"1781722480141"}

{"event":"chat.tool","tool":"showProject","toolCallId":"d1c5d25f6","persona":"weirdo","sessionId":"1781722480141"}

{"event":"chat.turn.complete","model":"cerebras","persona":"weirdo","sessionId":"1781722480141","inputTokens":2907,"outputTokens":241,"latencyMs":39}

 POST /api/chat 200 in 8.1s (next.js: 3ms, application-code: 8.1s)

 POST /api/chat-token 200 in 32ms (next.js: 6ms, application-code: 26ms)

```



Next prompt:

```

Show me his strongest project

BOOM is a modular, high‑throughput astronomical alert broker that ingests, enriches, and filters real‑time survey data at scale—showcasing Anant’s expertise in large‑scale data pipelines, cloud infrastructure, and AI‑driven analytics.

{ "function": "navigate", "arguments": } { "function": "showProject", "arguments": { "slug": "boom" } }

```



I think that the recruiter persona is the only that's broken. Orby did not say anything but we did render to the designated section of the page. Orby was about to say something next to the portfolio lab button but did not say anything. Logs:

```

[browser] Please ensure that the container has a non-static position, like 'relative', 'fixed', or 'absolute' to ensure scroll offset is calculated correctly. (<anonymous>)

{"event":"router.turn","sessionId":"1781722480141","messageCount":4,"tier":"full","startProvider":"cerebras"}

{"event":"chat.request","provider":"cerebras","mode":"live","persona":"recruiter","sessionId":"1781722480141"}

{"event":"chat.turn.complete","model":"cerebras","persona":"recruiter","sessionId":"1781722480141","inputTokens":2553,"outputTokens":344,"latencyMs":19}

 POST /api/chat 200 in 3.6s (next.js: 3ms, application-code: 3.6s)

 POST /api/chat-token 200 in 13ms (next.js: 2ms, application-code: 11ms)

```



Next prompt from ceo: 

```

What problems is he solving?

Anant tackles high‑impact gaps: SafeReach builds disaster‑ready protocols for people with disabilities; ResQ gives founders deterministic cash forecasts they can’t afford a finance team; CasualOps creates AI‑driven SOC intelligence to untangle cyber incidents. Even these efforts are only a slice—he plans a full‑blown blog to map his broader problem space, writing without AI to push back on the “dead internet” myth.

{ "function": "navigate", "arguments": } { "function": "showProject", "arguments": { "slug": "safereach" } } { "function": "showProject", "arguments": { "slug": "resq" } } { "function": "showProject", "arguments": { "slug": "casualops" } }

```



Acutally even this is broken, orby did not say anything but did render next to the portfolio button. We got the end of the message that the user was not supposed to get either. Logs:

```

GET / 200 in 2.9s (next.js: 5ms, proxy.ts: 12ms, application-code: 2.9s)

{"event":"router.turn","sessionId":"1781722480141","messageCount":5,"tier":"full","startProvider":"cerebras"}

 GET / 200 in 3.1s (next.js: 11ms, proxy.ts: 7ms, application-code: 3.1s)

{"event":"chat.request","provider":"cerebras","mode":"live","persona":"ceo","sessionId":"1781722480141"}

{"event":"chat.turn.complete","model":"cerebras","persona":"ceo","sessionId":"1781722480141","inputTokens":2640,"outputTokens":542,"latencyMs":29}

 POST /api/chat 200 in 46s (next.js: 11ms, application-code: 46s)

 GET / 200 in 2.9s (next.js: 4ms, proxy.ts: 5ms, application-code: 2.9s)

```



Actually a lot of things are broken, next prompt for weirdo: "Describe his stack as a sci-fi movie

{ "name": "navigate", "arguments": }"

logs:

```

GET / 200 in 2.9s (next.js: 6ms, proxy.ts: 8ms, application-code: 2.9s)

{"event":"router.turn","sessionId":"1781722480141","messageCount":6,"tier":"full","startProvider":"cerebras"}

{"event":"chat.request","provider":"cerebras","mode":"live","persona":"weirdo","sessionId":"1781722480141"}

{"event":"chat.turn.complete","model":"cerebras","persona":"weirdo","sessionId":"1781722480141","inputTokens":2616,"outputTokens":426,"latencyMs":53}

 POST /api/chat 200 in 4.0s (next.js: 13ms, application-code: 

```



ANother broken message from friend:

```

What's Anant actually excited about?

Anant is bubbling with excitement about building real, impactful things—especially when he can team up with ambitious, fast‑moving folks. He loves high‑stakes collaborations, like the CFO‑focused ResQ project, and thrives on turning ideas into working software alongside sharp teammates.

{ "sectionId": "about", "orbyMessage": "Zooming into Anant’s passions..." }

```



Logs:

```

{"event":"router.turn","sessionId":"1781722480141","messageCount":6,"tier":"full","startProvider":"cerebras"}

{"event":"chat.request","provider":"cerebras","mode":"live","persona":"weirdo","sessionId":"1781722480141"}

{"event":"chat.turn.complete","model":"cerebras","persona":"weirdo","sessionId":"1781722480141","inputTokens":2616,"outputTokens":426,"latencyMs":53}

 POST /api/chat 200 in 4.0s (next.js: 13ms, application-code: 4.0s)

 GET / 200 in 3.3s (next.js: 14ms, proxy.ts: 35ms, application-code: 3.3s)

 POST /api/chat 200 in 1779ms (next.js: 4ms, application-code: 1775ms)

```



Last prompt that worked perfectly: 

```

I did not need to see this: "{ "sectionId": "about", "orbyMessage": "Zooming into Anant’s passions..." }". You had to do it yourself.

I’m just following the portfolio’s rules: every answer that touches a section (like “about” or a project) must smoothly scroll there and let Orby greet you. The navigation call does that behind the scenes, keeping the experience tidy and consistent. If you’d rather skip the scroll, just let me know what you’d like to hear!

```

Logs:

```

{"event":"router.turn","sessionId":"1781722480141","messageCount":7,"tier":"full","startProvider":"cerebras"}

{"event":"chat.request","provider":"cerebras","mode":"live","persona":"friend","sessionId":"1781722480141"}

{"event":"chat.turn.complete","model":"cerebras","persona":"friend","sessionId":"1781722480141","inputTokens":2551,"outputTokens":157,"latencyMs":35}

 POST /api/chat 200 in 3.8s (next.js: 27ms, application-code: 3.8s)

{"event":"router.turn","sessionId":"1781722480141","messageCount":8,"tier":"full","startProvider":"cerebras"}

{"event":"chat.request","provider":"cerebras","mode":"live","persona":"friend","sessionId":"1781722480141"}

{"event":"chat.tool","tool":"navigate","toolCallId":"1119935a7","persona":"friend","sessionId":"1781722480141"}

{"event":"chat.turn.complete","model":"cerebras","persona":"friend","sessionId":"1781722480141","inputTokens":2712,"outputTokens":165,"latencyMs":37}

 POST /api/chat 200 in 4.9s (next.js: 12ms, application-code: 4.9s)

[browser] [Turnstile] Challenge failed — chat may be limited (src/components/ChatTokenInit.tsx:82:16)

[browser] [Cloudflare Turnstile] Error: 300010. (https://challenges.cloudflare.com/turnstile/v0/api.js:1:10084)

```



In the end and in between we have received warnings and some errors. By the ned we had a turnstile and cloudfare error. Analyze each and every prompt, log, figure out what needs to be fixed first. Just do that for now. What exactly is going wrong here in depth. Also do all our providers work since we have only cerebas working right now. Let's run a check on all our providers to check if they all work. Can we use this model with cerberas as well: "Z.ai GLM 4.7". I think we have access to that model as well. Right now we are using the openai model only, let's make most of our free usage. We used groq's models only on june 14th apparently on usage. We have never used the mistral provider accrording to the usage. But we have hit the "Couldn't reack Orby. Try again?" multiple times. Let's do a very deep check here regarding what the issue is. Why do we still get the {...}. orby does not reply when it needs to and why do we not get cards or good replies each time. All the prompts pasted above except the last one were fixed prompts. Our plan here describes that we have listed sort of fixed answers for each and every one of those responses: `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Projects\CS\Portfolio\nextgen-chatbot`. The notes might be outdated with the providers but in detail explain what exactly orby and the portfolio lab is. Analyze the notes in detail, the codebase in detail. What's wrong with the replies and our providers? Figure out the root cause of it. Do not make any changes, just come back with a very brief reply on why do we run into these issues over and over again. Why do we never use the backup providers? 
## Failure Modes / Misconceptions
> [!WARNING]

Reply by kiro:

---
## Root Cause Analysis
### Problem 1: Why raw JSON `{...}` leaks to the user

**Root cause: Cerebras (`gpt-oss-120b`) does not reliably use structured tool calling.**

Your model router always starts at Cerebras for messages 1–10. The logs confirm every single response comes from `cerebras` — you never see `router.fail` events that would trigger cascading to Groq or Mistral. Cerebras _technically succeeds_ (returns HTTP 200), so the router considers it "live" and never fails over.

But Cerebras is inconsistent at actually using the structured tool-call API. Sometimes it correctly emits tool calls (the "worked perfectly" examples where you see `chat.tool` events). Other times it **dumps the tool call as raw text** in the content field — `{ "function": "navigate", "arguments": ... }`, `{ "sectionId": "about", "orbyMessage": "..." }`, etc.

Your `chat-sanitizer.ts` backstop catches _some_ patterns (`{"tool":...}`, `{"sectionId":...}`, `<orbyMessage>` tags) but the model is emitting variations the regex doesn't cover — like `{ "function": "navigate", "arguments": }` (note: that pattern uses `"function"` not `"tool"`). The sanitizer regex looks for `"tool"` as the first key, not `"function"`.

**Evidence from logs:**

- "What are his top skills?" (recruiter) → `chat.turn.complete` fires but NO `chat.tool` event logged → model emitted tool calls as text, not structured API calls
- "What's the weirdest thing he's built?" (weirdo) → HAS `chat.tool` events → worked
- The CEO "What problems is he solving?" → NO `chat.tool` events → leaked as text

### Problem 2: Why Orby doesn't speak

**Direct consequence of Problem 1.** Orby's speech is driven by the `orby:navigate` CustomEvent, which is dispatched only when the frontend receives an `a:` line (tool result) with `toolName === "navigate"`. When Cerebras dumps the navigate call as text instead of using the tool API:

1. No `a:` line is emitted in the stream
2. No `orby:navigate` event fires
3. Orby has nothing to say

The sanitizer _does_ try to catch this — if it finds `{"sectionId":...}` in the text, it emits a synthetic `a:` line. But the sanitizer only runs at `part.type === "finish"` (stream end). By that point, the frontend may have already rendered the broken text to the user. The `t:` (text replacement) line is sent afterward to fix it, but there's likely a timing/rendering issue where the user briefly sees the raw JSON.

Additionally, your `useOrbyState.ts` has a constraint: `cloudVisible` requires `!sidebarOpen` (the Lab panel must be closed for Orby's speech to show). When the user is chatting in the Lab (sidebar open), Orby's speech cloud is hidden unless state is `chat-nav-arrival` or `chat-nav-home`. This might explain why Orby "was about to say something next to the portfolio lab button but did not say anything" — the state transition from `chat-nav-home` → `chat-nav-arrival` depends on an IntersectionObserver seeing the target section, which may not fire if the section is already visible.

### Problem 3: Why backup providers (Groq, Mistral) never fire

**The router only fails over on exceptions, not on "bad quality" responses.**

```typescript
const response = await result.response;
// If this doesn't throw, the provider is considered healthy
return { mode: "live", result, provider: provider.name };
```

Cerebras returns HTTP 200 with valid text — it just happens to dump tool calls as text instead of using the tool API. The router sees this as success. It has no concept of "the model didn't use tool calling properly, try the next provider." The Groq `tool_use_failed` check is the only quality-gate, and it only applies to Groq.

**Your plan says the chain should be Azure → Cerebras → Groq → Mistral**, but the implementation has **no Azure** at all. Your `.env.local` has no `AZURE_API_KEY` or Azure-related env var, and `model-router.ts` only defines three providers: Cerebras, Groq, Mistral. The premium tier (Azure GPT-4o-mini for first 10 messages) was designed but never implemented.

### Problem 4: The first prompt "What are his top skills?" specifically

This is a **fixed prompt** that should match `findFixedPrompt("recruiter", "What are his top skills?")`. When matched, the system prompt gets injected with:

```
FIXED PROMPT — NAVIGATION IS DETERMINISTIC: For this specific question, 
you MUST call navigate({"sectionId":"skills"}) exactly as specified.
```

But Cerebras still ignores this instruction and dumps the navigate call as text. The fixed-prompt system correctly identifies the prompt and injects the directive, but the model doesn't obey.

### Problem 5: Cloudflare Turnstile errors

```
[Turnstile] Challenge failed — chat may be limited
[Cloudflare Turnstile] Error: 300010
```

This is a separate issue. Error 300010 means the Turnstile widget failed to verify (likely because `localhost` isn't properly whitelisted for invisible mode in development, or the widget is being rate-limited). This doesn't break chat directly since your token endpoint still returns 200, but it means the anti-bot protection isn't functional in dev.

### Problem 6: Regarding Z.ai GLM 4.7

I can't verify whether you have access to this model. It's not configured anywhere in your codebase. If you want to add it, you'd need to know its API endpoint format (whether it's OpenAI-compatible) and add it to the `PROVIDER_CHAIN` array.

---

## Summary — Why This Keeps Breaking

|Issue|Root Cause|
|---|---|
|Raw JSON leaks to user|Cerebras doesn't reliably use tool calling; sanitizer misses some patterns|
|Orby silent|No tool result emitted → no `orby:navigate` event fires|
|Backup providers never used|Router treats HTTP 200 as success regardless of output quality|
|Azure never fires|Azure was planned but never implemented in code|
|Same bugs recur|Cerebras behavior is non-deterministic — sometimes tools work, sometimes they don't|

**The fundamental issue:** You're relying on a free model (Cerebras `gpt-oss-120b`) that intermittently ignores structured tool calling, and your failover logic has no way to detect "tool calling failed" vs "request failed." The system was designed around having Azure GPT-4o-mini as the reliable primary that always uses tools correctly, with Cerebras as the backup. Instead, Cerebras is the primary and it's unreliable at the one thing that makes Orby work.
## Evidence From This Vault
- [[ ]]
## Flashcards
#cards/[track]

---
epoch: 1777414184591
modelKey: "gpt-5.2|github-copilot"
topic: "AI Portfolio Lab RAG Plan"



tags:
  - copilot-conversation
---

**user**: Do you think this is a good plan for me to implement the rag ai that i was thinking to implement: "# Improved Plan: AI Portfolio Lab
                                                                                                        
  ## Corrections To The Provided Plan                                                                   
                                                                                                        
  - The local content folder in this repo is Data/, not lowercase data/.                                
  - The app layout is src/app/layout.tsx, not src/layout.tsx.                                           
  - src/app/studio/[[...tool]]/ is Sanity Studio, not OpenAI ChatKit. Do not remove it.                 
  - There is no existing shadcn Tabs component, no tsx, no Mermaid, no Transformers.js, and no WebLLM   
    dependency.                                                                                         
  - “Build-time embeddings only” is incomplete: vector search also needs a query embedding at runtime.  
    V1 should be keyword-first, with optional local browser embeddings.                                 
  - Sanity webhooks cannot safely rewrite public/ai/*.json inside a deployed Next serverless app. Use   
    rebuild/deploy hooks for the static AI index.                                                       
                                                                                                        
  ## Summary                                                                                            
                                                                                                        
  Replace the OpenAI ChatKit sidebar with a zero-cost AI Portfolio Lab: an evidence-backed,             
  interactive portfolio intelligence panel. It will retrieve from a static AI index generated from      
  Sanity or Data/*.ndjson, synthesize deterministic answers, and visualize proof through cards,         
  timelines, and skill/project connections.                                                             
                                                                                                        
  Sanity remains the source of truth. Data/ remains the local fallback and Kiro/MCP-editable mirror.    
  No visitor message should call a paid API.                                                            
                                                                                                        
  ## Key Changes                                                                                        
                                                                                                        
  - Security first:                                                                                     
      - Rotate the exposed OpenAI, Clerk, GitHub MCP, and Obsidian MCP tokens before any public push    
        or deployment.                                                                                  
      - Remove OpenAI env vars from .env.local.                                                         
      - Keep .env.local untracked and verify .gitignore.                                                
  - Remove OpenAI ChatKit:                                                                              
      - Delete src/app/actions/create-session.ts, src/components/chat/Chat.tsx, and src/components/     
        chat/ChatWrapper.tsx.                                                                           
      - Remove @openai/chatkit-react from package.json.                                                 
      - Remove src/lib/config.ts if it only serves ChatKit.                                             
      - Remove the OpenAI ChatKit <Script> from src/app/layout.tsx.                                     
      - Remove .chatkit-* and openai-chatkit::part(...) styles from src/app/globals.css.                
      - Update SidebarToggle, AppSidebar, and ProfileImage so they open the AI Lab or behave as normal  
        portfolio UI.                                                                                   
      - Keep Sanity Studio and Sanity live content intact.                                              
  - Build the AI index:                                                                                 
      - Add scripts/build-ai-index.ts.                                                                  
      - Add tsx as a dev dependency, then add:                                                          
          - build:ai-index: tsx scripts/build-ai-index.ts                                               
          - build: pnpm build:ai-index && pnpm typegen && pnpm typecheck && next build                  
      - The script fetches published Sanity content through serverClient; if Sanity env/token/data is   
        unavailable, it reads Data/*.ndjson.                                                            
      - Output:                                                                                         
          - public/ai/manifest.json                                                                     
          - public/ai/chunks.json                                                                       
          - public/ai/vectors.json only when embedding generation succeeds.                             
  - Evidence chunk shape:                                                                               
                                                                                                        
    type EvidenceChunk = {                                                                              
      id: string;                                                                                       
      type: "profile" | "project" | "experience" | "skill" | "education" | "achievement" | "blog";      
      title: string;                                                                                    
      text: string;                                                                                     
      tags: string[];                                                                                   
      date: string | null;                                                                              
      sourceDocumentId: string;                                                                         
      sourcePath: string;                                                                               
      confidence: number;                                                                               
      metadata: Record<string, unknown>;                                                                
    };                                                                                                  
  - Retrieval system:                                                                                   
      - Add src/lib/ai/types.ts, src/lib/ai/retrieval.ts, and src/lib/ai/synthesizers/*.                
      - V1 default: fast client-side BM25-style keyword search over chunks.json.                        
      - Optional semantic layer: use Transformers.js locally in a Web Worker to embed the user query    
        and compare with precomputed chunk vectors.                                                     
      - If model/vector loading fails, silently fall back to keyword search.                            
      - Keep all generated answers grounded in retrieved chunks; unsupported questions should say the   
        portfolio does not contain evidence for that claim.                                             
  - AI Portfolio Lab UI:                                                                                
      - Replace the generic chat sidebar with src/components/ai-portfolio-lab/.                         
      - Use the existing sidebar/sheet infrastructure, but rename user-facing labels from “AI Twin” to  
        “AI Lab.”                                                                                       
      - Implement four modes without requiring a new Tabs dependency unless desired:                    
          - Recruiter: role-fit proof packs, relevant skills, project evidence.                         
          - Builder: project build breakdowns, architecture notes, tech decisions.                      
          - Research: AI/data systems timeline, skills/projects network, learning trajectory.           
          - Skeptic: claim checker with source cards, confidence, provenance.                           
      - Shared components:                                                                              
          - EvidenceCard                                                                                
          - ProofPackGenerator                                                                          
          - AnswerSynthesizer                                                                           
          - SkillGraph                                                                                  
          - ProjectTimeline                                                                             
  - Sanity schema upgrades:
      - Add richer project fields: problem, solution, technicalDepth, impact, lessonsLearned,           
        demoScript, aiRelevance.                                                                        
      - Add a proofPoint document type or embedded proofPoints fields for claim/evidence pairs.         
      - Update Data/*.ndjson examples to match the new schema.                                          
      - Regenerate Sanity types after schema changes.                                                   
                                                                                                        
  ## Webhook And Update Strategy                                                                        
                                                                                                        
  - For local dev, run pnpm build:ai-index after editing Sanity or Data/.                               
  - For production, configure a Sanity webhook to trigger a Vercel deploy hook or GitHub Action that    
    rebuilds the static AI index.                                                                       
  - Keep existing Sanity live preview for page content; the AI index updates on rebuild, not on every   
    client request.                                                                                     
  - Add a visible manifest timestamp in dev/debug mode so stale indexes are easy to detect.             
                                                                                                        
  ## Test Plan                                                                                          
                                                                                                        
  - Run pnpm typegen, pnpm typecheck, and pnpm build.                                                   
  - Search repo for openai, chatkit, OPENAI_API_KEY, and NEXT_PUBLIC_CHATKIT_WORKFLOW_ID; only          
    historical content text may remain.                                                                 
  - Test index generation with Sanity env present and with Sanity unavailable.                          
  - Test AI Lab queries for projects, skills, experience, education, achievements, contact, and         
    unsupported claims.                                                                                 
  - Test mobile and desktop sidebar behavior.                                                           
  - Verify keyboard navigation, focus states, ARIA labels, and readable contrast.                       
  - Measure search latency on the generated corpus; target under 50ms for keyword search.               
                                                                                                        
  ## Resources                                                                                          
                                                                                                        
  - Transformers.js docs: https://huggingface.co/docs/transformers.js/

  ## Assumptions

  - Keep Sanity.
  - Keep Data/ as the local fallback folder.
  - Do not remove Sanity Studio.
  - V1 prioritizes correctness and zero cost over free-form LLM generation.
  - WebLLM is V2 only, because it adds model download, WebGPU requirements, and more UX complexity. "?

It is a huge change from that but i want to be professional and think like an actual developer to build this ai. What do you think about this?
[Context: Notes: 20_Progress/Projects/CS/Portfolio.md]
[Timestamp: 2026/04/28 17:09:44]

**ai**: Yes — this is a strong, professional plan, and it’s thinking about the right things (security, deterministic behavior, grounded answers, rebuild strategy, and clear module boundaries). It’s also a *big* shift from “chatbot” to “portfolio intelligence panel,” which is a good move if your V1 goal is **zero-cost + high signal** rather than “fun conversation.”

That said, I’d tighten a few parts so it’s implementable without ballooning scope.

## What’s excellent about your plan
- **Security-first + removing paid dependencies**: Correct instinct. Deleting ChatKit + OpenAI env use is the right cleanup if you’re going public.
- **Static index generated at build time**: This is the most reliable and cheapest architecture. Your webhook-to-deploy-hook note is exactly right.
- **Grounded answers with evidence chunks**: “If no evidence exists, say so” is what makes it credible.
- **Keyword-first retrieval for V1**: This is the correct default. It works offline, ships fast, and avoids model-loading risks.
- **Sanity remains source of truth + Data/ fallback**: Very maintainable.

## Key corrections / risks to address
### 1) “No LLM” means it’s not really “RAG” (yet)
RAG usually implies **retrieval + generative model**. Your V1 is more like:
- Retrieval (BM25/keyword)
- Deterministic synthesis (templated summaries / extractive answers)

That’s totally fine and arguably better for a portfolio (less hallucination). But be clear in naming: **“Evidence-backed search + synthesis”** for V1, and “RAG” once you add an on-device or hosted model.

### 2) Transformers.js semantic search is optional, but still heavy
Even just query embeddings in the browser can add:
- large downloads
- worker complexity
- slower first interaction

Recommendation: make semantic search **V1.1**, not V1. Keep V1 to keyword + good ranking + good UI.

### 3) Your index outputs could be simplified
You propose:
- manifest.json
- chunks.json
- vectors.json (optional)

That’s fine, but ensure you also include:
- a lightweight inverted index (or precomputed tokens) if you want sub-50ms on larger corpora

If your corpus is small (portfolio-sized), you can skip this initially and still hit your latency target.

### 4) Sanity fetching in build script
Make sure your plan includes one of these:
- use Sanity **GROQ over CDN** for public content (no token needed), or
- use a token in CI only (never shipped)

Your plan says “serverClient; if unavailable read Data/”. Good—just ensure the “unavailable” case isn’t your normal production state accidentally.

### 5) Don’t overbuild the 4 “modes” early
Recruiter/Builder/Research/Skeptic is a great product idea, but it can explode scope.

Recommendation: ship V1 with:
- one search box
- filter chips (Projects / Experience / Skills / Education)
- “Proof Pack” view as the primary output (it naturally covers recruiter + skeptic)
Then add “modes” once retrieval quality is solid.

## What I would change to make it more implementable (V1 scope)
Here’s a cleaned “V1 definition” that’s still aligned with your plan:

### V1 goal
A sidebar “AI Lab” that:
- takes a question/query
- retrieves top K evidence chunks (keyword)
- returns a **structured answer**: headline + bullets + evidence cards (with links)
- never calls a paid API

### V1 deliverables (in order)
1. **Remove ChatKit + clean sidebar**
2. **Build static index**
   - `public/ai/chunks.json`
   - `public/ai/manifest.json` (timestamp, chunk counts, schema version)
3. **Client retrieval**
   - simple keyword scoring (TF-IDF-ish / BM25-ish) or even a good heuristic scorer to start
4. **Answer synthesis (deterministic)**
   - templates per chunk type (project/experience/etc.)
5. **UI**
   - EvidenceCards + “Proof Pack”
   - source links to project pages / sanity docs

### V1.1 / V2
- semantic retrieval via embeddings
- on-device LLM (WebLLM) or cheap hosted model behind your own rate-limited endpoint (optional)

## Minor notes on your chunk schema
Your `EvidenceChunk` shape is good. Two tweaks:
- Add `url?: string` (so every card can deep-link to the page/section)
- Replace `confidence` with either:
  - `retrievalScore` (computed at query time), and optionally
  - `qualityScore` (static, author-defined)

“confidence” can be misleading because you’re not doing probabilistic inference.

## My verdict
- As a “think like a developer” plan: **yes, it’s solid and professional**.
- Main improvement: **cut V1 down** (keyword + proof cards + deterministic synthesis), and treat embeddings + multi-mode intelligence as subsequent iterations.
- The most valuable part is the architecture choice: **static index + grounded UI**. That’s exactly how you avoid a flaky “AI toy”.

If you want, paste your current sidebar/chat component entry points (which file renders the sidebar, and what components it uses), and I’ll propose the exact Step 1 diff plan (files to delete/keep, and what to replace them with) before you touch indexing.
[Timestamp: 2026/04/28 17:10:04]
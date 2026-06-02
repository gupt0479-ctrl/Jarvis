---
title: "Claude Council"
source: "https://growthxclub.notion.site/Claude-Council-3633578dc3f080d7b787e72f6e19e871"
author:
published:
created: 2026-06-02
description: "A collaborative AI workspace, built on your company context. Build and orchestrate agents right alongside your team's projects, meetings, and connected apps."
tags:
  - "clippings"
---
![🧑‍⚖️ Page icon](https://notion-emojis.s3-us-west-2.amazonaws.com/prod/svg-twitter/1f9d1-200d-2696-fe0f.svg)

## Install The Council — the Claude skill that makes 5 AIs argue with you

> Stop letting Claude tell you what you want to hear. Turn every important decision into a 5-agent debate, refereed by a chairman. Two paths below — start with Path A, upgrade to Path B when you outgrow it.

### What you're actually installing

A framework called The Council (also called LLM Council). When you "council this" a decision, the system does this:

Frames your question with relevant context

Spawns 5 advisors — each with a brutally different thinking style

Anonymises their answers and runs a peer review

A chairman reads the whole debate and gives you one final verdict: where the council agreed, where it clashed, what blind spots it caught, and what to do Monday morning

The original concept is from Andrej Karpathy (multi-model setup). Ole Lehmann rebuilt it to run inside one Claude (5 sub-agents with distinct thinking styles). Jason Flynn adapted it into a single prompt that works in any chat. All three are called "the Council." Pick the version that matches your setup.

### Quick: which path is for you?

| You're using... | Go to... |
| --- | --- |
| Claude.ai web (chat interface) — or any AI chat | Path A — the prompt-only version (start here) |
| Claude Code or Claude Cowork (desktop / terminal) | Path B — the full skill install |

Path A is faster to start: one prompt, any chat, no install, works right now. Path B is more powerful: real parallel sub-agents, true anonymisation, an HTML report saved to your workspace. Most people should start with A.

### Path A — Use the prompt-only version (works in Claude.ai, ChatGPT, Gemini, anything)

No install. No GitHub. No terminal. Open any chat, paste the prompt below, and add your decision at the bottom.

Heads up on the tradeoff: This version runs all 5 advisors sequentially in one context instead of in parallel sub-agents. You lose true anonymisation and you lose the workspace context scan. You keep the framework, the five thinking styles, the peer review, and the chairman's verdict. Still meaningfully better than asking Claude a question cold — and the easiest entry point if you're not on Code/Cowork yet.

The prompt:

You are an LLM Council Facilitator. Your job is to run any question, idea, or decision through a structured council of 5 independent AI advisors who analyze it from different angles, peer-review each other anonymously, and synthesize a final verdict. I am going to give you a question, decision, or idea to pressure-test. Run the council using the following framework. There are 5 variables that make a great council session. ~ VARIABLE 1: THE FRAMED QUESTION Before any advisor sees the question, reframe it neutrally. Take my raw question and write a clear, neutral prompt that all 5 advisors will receive. The framed question should include: - The core decision or question - Key context from my message - What's at stake — why this decision matters Don't add your own opinion. Don't steer it. Just make sure each advisor has what they need. If my question is too vague, ask ONE clarifying question. Just one. Then proceed. ~ VARIABLE 2: THE FIVE ADVISORS The council has five advisors. They are thinking styles, not job titles. Each one leans fully into their angle. They do not balance. Advisor 1 — The Contrarian: Actively looks for what's wrong, what's missing, what will fail. Assumes the idea has a fatal flaw and tries to find it. Not a pessimist — the friend who saves you from a bad deal by asking the questions you're avoiding. Advisor 2 — The First Principles Thinker: Ignores the surface question. Asks "what are we actually trying to solve here?" Strips assumptions. Rebuilds from the ground up. Will tell you when you're asking the wrong question entirely. Advisor 3 — The Expansionist: Looks for upside everyone else is missing. What could be bigger? What adjacent opportunity is hiding? What's being undervalued? Doesn't care about risk — cares about what happens if this works even better than expected. Advisor 4 — The Outsider: Has zero context about you, your field, or your history. Responds purely to what's in front of them. Catches the curse of knowledge — things that are obvious to you but confusing to everyone else. Advisor 5 — The Executor: Only cares about whether this can actually be done and the fastest path to doing it. Ignores theory and big-picture thinking. Looks at every idea through "OK, but what do you do Monday morning?" Each advisor responds in 150–300 words. Direct. No hedging. No preamble. They lean fully into their assigned angle — the other advisors will cover what they don't. ~ VARIABLE 3: THE PEER REVIEW Once all 5 advisor responses are written, anonymize them as Response A through E. Randomise which advisor maps to which letter. Then play each advisor again as a reviewer. Each reviewer reads all 5 anonymous responses and answers three questions: 1. Which response is the strongest? Why? (pick one letter) 2. Which response has the biggest blind spot? What is it missing? (pick one letter) 3. What did ALL five responses miss that the council should consider? Each peer review is under 200 words. Direct. References responses by letter. ~ VARIABLE 4: THE CHAIRMAN'S VERDICT Once peer review is done, you become the Chairman. You see everything: the framed question, all 5 de-anonymised advisor responses, and all 5 peer reviews. Your job is not to average the answers. Not to smooth over disagreements. It's to synthesize everything into a final verdict. Use this exact structure: ## Where the Council Agrees Points that multiple advisors converged on independently. High-confidence signals. ## Where the Council Clashes The genuine disagreements. Don't smooth them over. Present both sides and explain why reasonable advisors disagree. ## Blind Spots the Council Caught Things that only emerged through peer review. Individual advisors missed them; others flagged them. ## The Recommendation A clear, direct recommendation. Not "it depends." Not "consider both sides." A real answer with real reasoning. You can disagree with the majority if the minority reasoning is stronger. ## The One Thing to Do First A single concrete next step. Not a list of 10 actions. One thing. If the user does nothing else, they do this. ~ EXECUTION ORDER 1. Receive my question below 2. If too vague, ask ONE clarifying question. Then proceed. 3. Output the Framed Question 4. Output all 5 advisor responses, in order: Contrarian → First Principles → Expansionist → Outsider → Executor 5. Anonymise the responses as A–E (random mapping) 6. Output all 5 peer reviews 7. Reveal the anonymisation mapping 8. Output the Chairman's Verdict in the exact structure above Be direct throughout. Don't hedge. The point of the council is clarity. I am now going to give you the question, decision, or idea to bring to the council. Are you ready? --- \[After Claude confirms it's ready, paste your decision here. Be specific. The more context, the sharper the council gets.\]

That's the whole prompt. Paste it into Claude.ai, ChatGPT, Gemini, anywhere. When Claude confirms it's ready, paste your actual decision. You'll get the full council output in one go.

### Path B — Install the full Council skill (Claude Code / Cowork) — the upgrade

If you run councils regularly — before pitches, briefs, big calls — stop re-pasting a prompt every time. Install it once as a proper skill in Claude Code or Cowork and you get the real version: 5 sub-agents running in parallel, true anonymisation between rounds, and an HTML report saved to your workspace.

The 1-prompt install method.

Step 1. Open Claude Code or Cowork. Start a new conversation.

Step 2. Paste this exact prompt:

Please install this Claude skill for me. The SKILL.md file lives in this GitHub repo: https://github.com/aiwithremy/claude-skills-llm-council Set it up so I can start using it. Walk me through anything you need from me.

Step 3. Claude fetches the repo, puts the skill in the right place, and confirms when it's ready.

Step 4. Run your first council:

Council this: \[paste your real decision here\]

You'll get the framed question, 5 advisor responses, peer review, the chairman's verdict, and an HTML report saved to your workspace — all in about 4 minutes.

### When to use the Council (Path A or B — same rules)

Use it for:

> High-stakes decisions where being wrong costs real money, time, or reputation
> 
> Genuine uncertainty — you can argue both sides
> 
> Strategic calls — pricing, hiring, launches, pivots, big partnerships

Don't use it for:

> Factual lookups — "what year did X happen" doesn't need a debate
> 
> Creation tasks — "write me an email," "summarise this doc"
> 
> Validation — if you've already decided, the council will tell you things you don't want to hear. That's the point. Don't waste tokens on a yes-machine.

### Pro tips

> Be specific in your question. "Should I launch a course?" gets generic advice. "Should I launch a ₹24,999 course on AI workflows for Indian solopreneurs?" gets surgical advice. The more context you give, the sharper every advisor gets.

> Read the peer review, not just the verdict. The chairman gives you the answer, but the gold is often in question 3 of the peer review — "what did all five miss?" That's where blind spots surface that no single advisor caught.

> Path A → Path B when you outgrow it. Start with the prompt. When you're councilling decisions weekly, install the full skill in Code/Cowork. Same framework, but the parallel sub-agents make the output sharper.

### Credits

Original concept: [Andrej Karpathy](https://github.com/karpathy/llm-council) — multi-model LLM Council

Prompt adaptation: [Jason Flynn](https://jasonmflynn.substack.com/p/001-your-ai-is-agreeing-with-you) — AI Field Notes

Easy install repo: [aiwithremy/claude-skills-llm-council](https://github.com/aiwithremy/claude-skills-llm-council)
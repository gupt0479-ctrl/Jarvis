---
type: input
status: sprout
created: 2026-06-20
updated: 2026-06-20
tags:
  - summary
  - github
notes:
  - "[[Github Skills]]"
input_kind: github
track: ai
source_note: "[[aiwithremyclaude-skills-llm-council LLM Council — a Claude Code skill that runs your decisions through 5 AI advisors with peer review.md]]"
source_url: https://github.com/aiwithremy/claude-skills-llm-council
---
# LLM Council — Summary
> [!DECISION] The council was copied from [karpathy's repo](https://github.com/karpathy/llm-council), needs to mimicked (slightly modified) and implemented globally. 
> **Answer:** Implementation: copy the skill to `~/.claude/skills/llm-council.md` for global access. Customization: change the 5 default expert personas to match your domains — suggested: trading analyst, CS theorist, systems engineer, ML practitioner, pragmatic builder. The `/llm-council "question"` pattern is then available in every project. Use it for: architecture decisions (which agent framework?), risk assessment (is this trade signal robust?), hard debugging (why is this async pipeline deadlocking?). Don't use it for routine coding tasks — overhead is only worth it for decisions that are hard to reverse.

**Source:** `https://github.com/aiwithremy/claude-skills-llm-council`
**Ingested:** 2026-06-20
**Pages:** N/A — repo, 2 files (`README.md`, `SKILL.md`). Metadata and `SKILL.md` pulled live via `gh api`, not from the clipped page.

## Source

**aiwithremy/claude-skills-llm-council** is a two-file Claude Code skill (704 stars, 72 forks, last pushed 2026-04-26, no license file) built by **Ole Lehmann**, adapting **Andrej Karpathy**'s `llm-council` methodology (21,118 stars, the original multi-model version) into a single-Claude, multi-sub-agent skill.

## Key Claims

- **Single answer, no way to check it:** asking one model a question gives one perspective with no signal on whether it's a good one.
- **Peer review is the actual mechanism, not just asking five times:** five advisors answer independently, then anonymously review each other's answers before a chairman synthesizes — the anonymization step is what Karpathy's original methodology contributes.
- **Five advisors are thinking styles, not roles**, chosen to create three deliberate tensions: Contrarian vs. Expansionist (downside vs. upside), First Principles Thinker vs. Executor (rethink everything vs. ship now), with the Outsider catching blind spots the other four share from context.
- **Triggering is explicitly scoped:** the skill's own frontmatter lists mandatory and strong trigger phrases and explicitly excludes factual lookups, creation tasks, and "casual" should-I questions with no real tradeoff.
- **Context enrichment happens before framing:** the skill scans the workspace (`CLAUDE.md`, a `memory/` folder, recently attached files) for up to ~30 seconds before writing the framed question, so advisors argue from real context instead of generic priors.

## Full Content

### What's a skill (`README.md`)
A skill is a standing instruction set — "a job description for a specific task" — that Claude follows once installed and triggered by phrase, without re-explaining the task each time.

### What it does (`README.md`)
==The council runs one question through 5 independent advisors, has them peer-review each other's anonymized answers, and has a chairman synthesize where they agree, where they clash, and what to actually do.==

### When to use it (`README.md`)
Good questions have genuine uncertainty and real stakes ("Should I launch a $97 workshop or a $497 course?"). Bad questions have one right answer, are creation tasks ("write me a tweet"), or are processing tasks ("summarize this article") — none of those benefit from five perspectives.

### How to install it (`README.md`)
Two no-terminal paths: (1) paste a one-line prompt telling Claude to fetch and install the `SKILL.md` from the repo directly; (2) download `SKILL.md` manually and hand it to Claude to place. Both work in Claude Code and Claude Cowork.

### The actual skill mechanism (`SKILL.md` — fetched live via `gh api`, not from the README)
This is the part the README only summarizes. The real file specifies:

1. **Frontmatter trigger logic.** Mandatory triggers: "council this," "run the council," "war room this," "pressure-test this," "stress-test this," "debate this." Strong triggers (only when paired with a real tradeoff): "should I X or Y," "which option," "I can't decide." Explicitly **does not** trigger on simple yes/no, factual lookups, or a "should I" with no real stakes.
2. **Step 1 — frame with context enrichment.** Before framing the question, scan the workspace (`CLAUDE.md`, `memory/`, attached files, prior transcripts) using `Glob`/`Read`, capped at ~30 seconds — looking for the 2-3 files that turn generic advice into grounded advice. Then write a neutral framed question covering the decision, context, and stakes. Ask exactly one clarifying question if the prompt is too vague, never more.
3. **Step 2 — convene 5 sub-agents in parallel**, each given its advisor identity, the framed question, and an instruction to lean fully into its angle (150-300 words, no hedging, no preamble).
4. **Step 3 — peer review, also 5 sub-agents in parallel.** Responses are anonymized as A-E with a *randomized* letter mapping (no positional bias). Each reviewer answers three fixed questions: strongest response and why; which response has the biggest blind spot; what did all five miss.
5. **Step 4 — chairman synthesis.** One agent receives the framed question, all 5 de-anonymized responses, and all 5 peer reviews, and must produce exactly five sections: Where the Council Agrees, Where the Council Clashes, Blind Spots the Council Caught, The Recommendation, The One Thing to Do First. The chairman is explicitly allowed to side with a single dissenting advisor over the 4-1 majority if that advisor's reasoning is stronger.
6. **Step 5 — present in chat only.** ==`SKILL.md` explicitly instructs: "Do NOT generate an HTML report or any files. The user reads it in the conversation."==
7. **Step 6 — transcript saving is optional**, only on request or for a significant question, written to `council-transcript-[timestamp].md` in the project's `active/` directory.
8. **Operating notes baked into the skill:** always spawn all 5 advisors in parallel (sequential spawning lets earlier answers bias later ones); always anonymize for peer review (named advisors get deferred to instead of evaluated on merit); the chairman can override the majority; don't run trivial questions through the council at all.

## Why It Matters

This is the live demonstration of the Tier-2 GitHub ingestion method just added to `ingesting-clipping/reference.md` §6: the clipped README ([[aiwithremyclaude-skills-llm-council LLM Council — a Claude Code skill that runs your decisions through 5 AI advisors with peer review.md]]) describes the skill; fetching `SKILL.md` directly via `gh api` is what actually shows the trigger logic, the parallel sub-agent structure, and the chat-only output rule — none of which the README states precisely. It's also a directly usable pattern for this vault: a multi-sub-agent peer-review structure is a stronger pressure-test than a single Claude answer for exactly the kind of high-stakes, ambiguous calls Jarvis is meant to support (project pivots, which repos to actually adopt, internship choices).

## Links Into The Vault

- [[Github Skills]] — confirmed; the natural home for this entry alongside mattpocock/skills, gstack, and Spec Kit (proposed addition, not yet written — see Open Questions).
- [[aiwithremyclaude-skills-llm-council LLM Council — a Claude Code skill that runs your decisions through 5 AI advisors with peer review.md]] — the raw clip this note replaces.
- [[Claude Council — Path A Prompt (web)]] — companion Web Ingestion note: the discovery-context landing page that pointed at this repo, including the prompt-only fallback version and the Karpathy → Lehmann → Flynn lineage.

## Open Questions

- [ ] Does the landing page's Path B claim of "an HTML report saved to your workspace" reflect an older version of the skill? The live `SKILL.md` explicitly forbids generating HTML and mandates chat-only output — this is a direct contradiction between the secondary source and the actual installed artifact, not a paraphrase difference.
- [ ] Should this skill be installed into this vault's own `.claude/skills/`? It would give Jarvis a built-in pressure-test step for exactly the kind of ambiguous, high-stakes calls this ingestion redesign itself is an example of.
- [ ] Worth proposing the one-line addition to [[Github Skills]] — repo name, link, one-line description — matching its existing table format?

## Flashcards

#cards/ai
Why does the council **anonymize** advisor responses before the peer-review round?::Without anonymization, reviewers would defer to a thinking style's identity instead of evaluating the argument on its merits — anonymization forces evaluation on substance, eliminating positional/identity bias.
What is the mechanism that makes this "more than just asking the same model five times"?::The **peer-review round** — each advisor reviews the other four's anonymized answers and reports the strongest response, the biggest blind spot, and what all five missed, before any synthesis happens.
How does this Claude-skill version of the Council mechanistically **diverge** from Karpathy's original?::Karpathy's original dispatches the same prompt to multiple different **models**; this skill instead runs multiple sub-agent **personas** inside one model (Claude) with different thinking-style instructions.
Per the skill's own trigger logic, what kind of question should it explicitly **not** trigger on?::Simple yes/no questions, factual lookups, or a "should I" question with no real tradeoff at stake (e.g. "should I use markdown" is named directly as a non-trigger example).
What real discrepancy exists between the secondary landing-page description and the actual installed skill file regarding output format?::The landing page advertises **"an HTML report saved to your workspace"** for Path B; the actual `SKILL.md` explicitly instructs "Do NOT generate an HTML report or any files" and to present the verdict directly in chat.

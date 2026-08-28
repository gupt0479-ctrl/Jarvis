---
type: evergreen
status: sprout
created: 2026-08-28
updated: 2026-08-28
tags:
  - internship
  - humanizer
  - standard
notes:
  - "[[20_Progress/Internship/Building System/Humanizer]]"
  - "[[30_Order/Standards/Resume Alteration Standard]]"
  - "[[30_Order/Standards/Cover Letter Alteration Standard]]"
next: null
---
# Humanized Writing Standard
==The checklist behind [[20_Progress/Internship/Building System/Humanizer]]'s pass/fail gate.== This is the internship-application-specific instance of a planned global humanizer system — scoped narrowly so resume/cover-letter drafting isn't blocked waiting for that larger build. A starter checklist, not exhaustive; extend it as real drafts surface new patterns worth naming, the same way `internship-research-loop`'s own filter rules only ever get added against real observed data, not speculation.

## Scope
Applies to every resume content plan and cover-letter draft before it's written as a DOCX (see [[30_Order/Workflows/Application Document Preparation]]'s `humanize` step). Checks tone and phrasing only — factual/evidence correctness is a separate, prior gate (Resume/Cover Letter Alteration Standard §2), already passed by the time a draft reaches this check.

## Prohibited Patterns (Starter List)
- **Generic filler claims** — "passionate about," "excited to," "dynamic team player," "results-driven," "hardworking" — vague enough to apply to any candidate, any role.
- **Inflated/corporate filler words used as padding** — "leverage," "seamless,""cutting-edge," "robust," "delve," "furthermore" — flag when used to sound impressive rather than because it's the plainest accurate word.
- **Repetitive sentence openers or uniform sentence length** — every bullet/sentence starting with the same structure ("Led X. Led Y. Led Z.") reads as machine-generated rhythm, not human variation.
- **Overused structural tells** — heavy reliance on em dashes, or three-part parallel lists ("fast, reliable, and scalable") in every paragraph, are patterns worth flagging when they recur mechanically rather than appearing where they're actually the clearest way to say something.
- **Claims that read as louder than the underlying fact**, even when technically evidence-backed — tone inflation on top of a true fact is still a flag here, separate from the Alteration Standards' factual-inflation rule.

## Required Checks
- Does every claim still trace to real evidence *after* rewriting for tone? A phrasing pass that quietly drifts a claim away from its source is a regression, not a stylistic improvement — catch it here even though evidence-tracing is nominally a prior gate's job.
- Does the draft still sound like one consistent person, not a template with company names swapped in?
- Would a human reading this immediately recognize it as AI-written boilerplate? If yes, that's a fail regardless of whether any single line individually seems fine.

## Output Contract
Per [[20_Progress/Internship/Building System/Humanizer#The Contract]]: pass, or fail with specific line-level flags — the exact phrase, which pattern above it violates, and a suggested fix. Never a silent rewrite.

## Explicitly Out of Scope
The full global humanizer agent/skill/command system, and its use in networking-message drafting — both are separate, larger work tracked outside this internship-specific standard (see [[20_Progress/Internship/Building System/Humanizer#What's In Scope Here vs. Not]]).

## Done When
- A resume/cover-letter draft that fails this check gets specific, line-cited flags — never a bare "sounds off."
- A draft that passes still has 100% of its claims traceable to the same evidence it had before the tone pass.

---
type: evergreen
status: sprout
created: 2026-06-01
updated: 2026-06-01
tags:
  - system
  - standards
notes:
  - "[[Week Template]]"
  - "[[00_Workflows Index]]"
  - "[[Vault Rules — Complete AI Ruleset]]"
  - "[[HUMAN_WRITING]]"
---
# Course Week Standard
==A week note fuses lecture and textbook into one synthesis that resolves what each source alone leaves ambiguous — the synthesis section is the point, not an afterthought.==
This is the content standard for `class` / `input_kind: lecture` week notes under `10_Areas/UMN/`. The defining move is the `## Lecture-to-textbook synthesis` section: lecture gives the scenario and the application, the textbook gives the named frameworks and tests, and the synthesis states how they fit. The gold standard is the MGMT 3001 week set; match its shape.
## Maps To
- Template: [[Week Template]]
## Used By Workflow
- No dedicated pipeline workflow — week notes are created directly in Obsidian via the Templater folder template for `10_Areas/UMN/`. See [[00_Workflows Index]] for the surrounding system and read this Standard before writing.
## Per-Heading Standard
### Frontmatter
`type: class`, `input_kind: lecture`, `status: seed` (week notes stay `seed`; the distilled concept note is where maturity grows), `area:` linking the course board and the matching textbook chapter, `tags: [#class, #Lecture]`, and `next:` pointing to the following week. Path-qualify ambiguous links — every course has a `Week - 9`.
> [!WARNING]
> A bare `[[Week - 10]]` that resolves to the wrong course's week. Week 9 uses `area:` links to the board, `[[Chapter - 14]]`, and the concept note, with `next:` → Week 10.
### What you must be able to do
The week's learning objectives as bullets, with the textbook chapter linked first. These are the exam-facing "can I do this" checks.
*Density:* four to eight objective bullets, each a verb the student must perform ("Distinguish...", "Apply the diversification test...").
> [!WARNING]
> Restating the topic title instead of listing testable abilities. Week 4 opens with `[[Chapter - 6]]` then eight "Distinguish / Explain / Apply / Compare" objectives.
### Key ideas (short)
Three to six compressed claims. Bold the named concept and the key contrast word in each.
*Density:* one line per idea, no sub-bullets.
> [!WARNING]
> Re-explaining the lecture here — this section is the short version, the Lecture section is the long one. Week 9: "Power is potential; influence is power in action; authority is formal right."
### Concepts created today
Wikilinks to the concept notes this week produced. Verify each exists or mark `(to create)`.
*Density:* one to four concept links.
> [!WARNING]
> Linking concepts that have no note. Week 9 links `[[Power and Influence]]`, `[[Management Foundations and Leadership]]`, `[[Ethics and Corporate Social Responsibility]]`.
### Examples worth keeping
Real lecture examples and scenarios — never invented ones. Bold the entity (a company, a named study).
*Density:* three to six concrete cases.
> [!WARNING]
> Generic textbook examples. Week 9: "Heidi vs Howard = gendered perception of the same behavior", "Oprah and Obama = referent power."
### Lecture
Numbered sections following the lecture's own structure: `### 1. Title` with tab-indented sub-content. Use `$...$` for any notation. This is the full lecture capture.
*Density:* one `###` per lecture section — Week 9 has 10. Reproduce the lecture, do not compress.
*Plugins:* `**bold**` on every power base / tactic / named term; `1.`/`-` lists for enumerations.
> [!WARNING]
> Collapsing ten lecture sections into a paragraph. Week 9 § Lecture walks sections 1–10 (power vs authority → choosing the right tactic) with the five power bases and ten influence tactics each bolded.
### Textbook integration
What the chapter adds beyond lecture. Link the chapter. When the chapter is dense, use `### Additions easy to miss` subheadings (Week 4 uses "Textbook additions that are easy to miss" with `### Why firms diversify`, `### Portfolio thinking`, etc.).
*Density:* capture the frameworks and tests the lecture only gestured at.
> [!WARNING]
> Repeating the lecture instead of stating the delta. Week 4 surfaces the **BCG Growth-Share Matrix**, the inverted-U diversification result, and the ownership test — none stated plainly in lecture.
### Domain links (leadership / entrepreneurship / speaking)
Optional but present in the gold notes: `### Leadership link`, `### Entrepreneurship link`, `### Speaking skill link` — how the week's concept transfers to the course's applied tracks.
*Density:* one to three bullets per sub-link, only where a real transfer exists.
> [!WARNING]
> Forcing all three when only one applies. Week 4 ties corporate strategy to conceptual skill (leadership), founder scope decisions (entrepreneurship), and a five-step recommendation order (speaking).
### Takeaways (questions to resolve)
`- [ ]` Tasks format, never prose. These are real open questions to resolve before the exam.
*Density:* two to five genuine questions.
> [!WARNING]
> Prose paragraphs, or questions already answered in the note. Week 4: "- [ ] At what point do transaction-cost savings stop justifying vertical integration?"
### Lecture-to-textbook synthesis
==The required section that makes a week note good and is missing from weak ones.== Exact shape:
- one `==definition anchor==` highlight stating the week's core concept in a sentence (the section's single highlight);
- `*Mechanism:*` — how lecture and textbook fit, what drives the concept;
- lecture example/scenario — the concrete case that makes it stick;
- textbook connection — `[[Chapter - ]]` supplies the framework the lecture applied;
- concept links — the `[[Concept - ]]` notes;
- `> [!WARNING]` the common confusion or failure mode, then `> [!SUMMARY]` one sentence on what the week is really about.
> [!WARNING]
> Skipping this section, or using more than one highlight in it. Week 9 anchors on "power is the capacity to influence, influence is the process, authority is the formal right", then mechanism → playing high/low example → `[[Chapter - 14]]` → concept links → WARNING (power ≠ authority) → SUMMARY.
### Flashcards
`#cards/[course]` (the gold notes use `#cards/MGMT`). 3–5+ cards testing distinctions and mechanisms, not labels. In the `#cards` section bold only the term meant to be hidden.
> [!WARNING]
> Label cards ("Five power bases::Legitimate, reward, coercive, expert, referent" is acceptable as a list-recall card, but prefer distinction cards like "Playing high::Signals rank; useful when rank must be reinforced").
## Done Conditions
- Lecture is captured section-by-section; textbook integration states only the delta.
- The `## Lecture-to-textbook synthesis` section is present and follows the exact six-part shape with one highlight, a WARNING, and a SUMMARY.
- Objectives, key ideas, examples, and concept links are all real and verified.
- `- [ ]` Tasks for takeaways; 3–5+ `#cards/[course]` cards.
- Passes all 16 points of [[Vault Rules — Complete AI Ruleset]] Part 12.
## Gold Standard Example
- [[10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Week - 9|Week - 9]] — power and influence; the cleanest synthesis section.
- [[10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Week - 4|Week - 4]] — corporate strategy; the strongest "textbook additions easy to miss" and domain-link sections.

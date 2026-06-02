---
type: class
input_kind: lecture
status: tree
created: 2026-01-22
updated: 2026-02-11
area:
  - "[[CSCI 3923 Board]]"
  - "[[UMN Board]]"
  - "[[Reading Assignment - 1]]"
  - "[[In Class Assignment]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 3923/Week - 2|Week - 2]]"
---
# Entire Week
## What you must be able to do
- What a **model** is: simplified representation used to predict or decide; simplification creates blind spots.
- Why “**models are opinions embedded in mathematics**”: choices about what to measure and what counts as success reflect values.
- What **proxies** are and why they’re risky: stand-ins (like zip code or credit-related signals) can encode inequality.
- The **3-part pattern of harmful models** (WMD-style): **opacity** (can’t see/appeal), **scale** (applied widely), **damage** (real harm).
- How **feedback loops** intensify harm: predictions influence decisions that make the prediction “come true” (or look true).
> [!TIP] Quick check you should be able to do on any “AI system”
> 1) What is it predicting/deciding?  
> 2) What inputs does it use (and what’s missing)?  
> 3) Who gets hurt if it’s wrong?  
> 4) Can the affected person challenge it?  
> 5) What happens when this runs on thousands/millions of people?
## Key ideas (textbook)
- **Model (core definition):** an abstract representation of a process used to predict outcomes and guide decisions (in software or in your head).
- **Models require simplification → blind spots:** every model leaves things out; what’s missing can matter most for fairness.
- **“Models are opinions embedded in mathematics”:**
	- Values show up in what gets measured, what “success” means, and what constraints are chosen.
- **Healthy models** tend to:
	- Use relevant inputs, update with feedback, and get corrected when they fail (baseball story logic).
- **Proxies:**
	- When the real thing is hard to measure, modelers use “stand-ins” (often easier to collect), which can drag in social bias.
- **WMD (Weapon of Math Destruction) = model with:**
	1. **Opacity** (black-box decision system),
	2. **Scale** (used broadly, impacts many),
	3. **Damage** (harms people, often those with less power).
- **Feedback loops (harm multiplier):**
	- When a model’s output shapes reality in a way that makes the model look “right,” even if the model caused the outcome.
> [!IMPORTANT] The “quiet” danger in Chapter 1
> A model doesn’t need to be malicious to cause harm. If it’s **scaled**, **unquestioned**, and **hard to appeal**, small biases become repeated harms.
## Concepts created today
- [[Reading Assignment - 1#Chapter - 1|Reading - Chapter 1]]
- [[In Class Assignment#Week - 1|Writing Prompts Ever Class]]
## Examples worth keeping
1. **Credit-worthiness + generational wealth (proxy trap):**
	- “Objective” credit variables can reflect past discrimination in housing/loans and neighborhood investment, so the model can reproduce inequality.
2. **Mapping Prejudice (UMN redlining project):**
	- Concrete local example of how historical policy choices become patterns in today’s datasets.
3. **“Who is telling you your story—people or algorithms?”**
	- Framing question for the course: narratives (culture/history) and numeric records (data) are shaped by power.
> [!EXAMPLE] Micro-application (use this structure in later essays)
> **Claim:** A proxy can create unfair outcomes even if it improves prediction accuracy.  
> **Why:** The proxy may correlate with protected traits or structural inequality.  
> **So what:** The system becomes a sorting machine that repeats past patterns under a “neutral” label.
## Lecture
1. Goals:
	  - learn ethical frameworks,
	  - learn to write better arguments,
	  - learn to discuss hard topics,
	  - learn from each other,
	  - carry it forward (requires practice).
- Skill practice: weekly “curiosity” routine (ask, listen, probe before debating).
- Writing expectations: most grading is writing; citations expected; persuasive argument structure is the default.
### Big theme from slides
- **Culture/history → becomes data → becomes algorithms → becomes decisions.**
	- If powerful groups shape what gets recorded and how it’s interpreted, “neutral data” is a myth, and AI inherits that history.
> [!WARNING] Common trap to avoid
> “The algorithm didn’t consider race” ≠ “the outcome is fair.”  
> Proxies (zip code, school, employment history, credit signals) can carry the same pattern indirectly.
### [[In Class Assignment#Week - 1|Writing Prompts]]
**Prompt 1 - What is the purpose of an ethics class? Is it possible to learn or teach ethics?**
- What does an ethics class *train* (skills) vs. *give* (answers)?
- When a decision is uncertain, what steps help you reason: stakeholders → harms/benefits → responsibilities → alternatives → justification?
- What makes ethics “teachable” here: practice in argument-building, case analysis, and discussion habits (not memorizing “right answers”)?
**Prompt 2 - Is data objective? Are algorithms objective? Is AI objective? Why / why not?**
- If data is a recorded slice of reality, what choices shaped it (what was measured, who was included/excluded, how labels were defined)?
- What parts of an algorithm are human choices (goal/metric, features, thresholds, proxies) even if the math is correct?
- What’s the difference between “accurate prediction” and “fair/just outcome,” and how can a system optimize one while harming the other?
**Prompt 3 - Is it possible for a technology to be purely good, bad, or neutral?**
- What changes when a tool is used at scale with high stakes (employment, housing, credit, policing, education)?
- What determines whether the same tool helps or harms: incentives, deployment context, accountability, and who can contest decisions?
- Which signs suggest a system is unsafe to treat as “neutral”: hidden rules, broad deployment, and real harm with no clear appeal path?
**Prompt 4 - What are your thoughts on AI checkers?**
- What assumptions do AI checkers make about writing and “authenticity,” and how often are they wrong in high-stakes cases?
- If an AI checker is a model, what are its inputs/proxies, and can students contest outcomes meaningfully?
- How could AI checkers create classroom feedback loops (students forced to write “to avoid detection,” mistrust increases, false positives treated as guilt)?
## Takeaways (questions to resolve)
- [ ] When I see a “score” or “risk level,” what exactly is the model claiming to measure (the true target), and what proxies is it actually using?
- [ ] Which parts of a model are value choices (definition of “success,” acceptable error, tradeoffs), and who should get to decide those?
- [ ] What is the strongest real-world example from Chapter 1 where a proxy becomes a punishment for circumstance rather than behavior?
- [ ] How can I tell the difference between “useful simplification” and “harmful blind spot” in a model?
- [ ] What is the minimum transparency needed for a model to be ethically acceptable in high-stakes settings (what must be visible, to whom)?
- [ ] How do feedback loops make a model look correct even when it is creating the outcome it predicts?
- [ ] If I had to redesign one Week 1 example to reduce harm, what would I change first: inputs, threshold, appeal process, or scope of deployment—and why?
- [ ] For AI checkers specifically: what evidence would convince me the tool is reliable enough to use, and what protections must exist for false positives?
> [!TIP] If you answer only 2 of these for exam prep
> 1) Proxy vs. target (with an example)  
> 2) Opacity + scale + damage (with an example)
## Flashcards
#cards/CSCI3923
1. What is a “model” in the ethics + computing sense?::A simplified representation of a process used to predict or make decisions; it necessarily leaves things out.
<!--SR:!2026-02-15,4,270-->
2. Why does “models are opinions embedded in mathematics” matter?::Because model builders choose the goal, what gets measured, and what counts as success—those choices embed values.
<!--SR:!2026-02-14,3,250-->
3. What is a proxy, and why can proxies be unfair?::A stand-in variable for something hard to measure; proxies can carry historical bias (e.g., location-based or credit signals).
<!--SR:!2026-02-14,3,250-->
4. What are the three features that make a high-impact harmful model (WMD-style)?::Opacity, scale, and damage.
<!--SR:!2026-02-12,1,230-->
5. What is opacity, and why is it ethically dangerous?::When people affected can’t understand, challenge, or correct the decision process; it blocks accountability and due process.
<!--SR:!2026-02-14,3,250-->
6. What is a feedback loop in algorithmic decision-making?::Model outputs shape actions and outcomes in ways that reinforce the model’s future predictions.
<!--SR:!2026-02-14,3,250-->
7. Why aren’t data/algorithms/AI automatically objective?::They reflect human choices in data collection, labeling, proxies, goals, and deployment context - even if computations are correct.
<!--SR:!2026-02-14,3,250-->
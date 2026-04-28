---
type: class
input_kind: lecture
status: tree
created: 2026-02-05
updated: 2026-02-11
area:
  - "[[UMN Board]]"
  - "[[CSCI 3923 Board]]"
  - "[[Reading Assignment - 2]]"
  - "[[In Class Assignment]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[50_Archive/UMN/Classes/CSCI 3923/Week - 3|Week - 3]]"
---
# Entire Week
## What you must be able to do
- *Rough draft due in 1 week! (February 5th @ 2:30 pm)*
- *Final draft due two weeks after (February 12th @ 2:30 pm)*
- Explain **Kranzberg’s First Law** in your own words and apply it to a concrete example (your film) by showing **at least one benefit and one harm**, plus why those outcomes happen (context + use + power).  
- Memorize and explain **all 6 of Kranzberg’s laws**, and be able to give a quick real-world example for each (even a 1–2 sentence one).
- Use the **weekly curiosity practice** correctly:
	- Ask for an “unpopular” opinion.
	- Ask **two probing questions** only to understand (no arguing).
	- Reflect back what you heard to confirm understanding.
- Know what **informed consent** means in research ethics and why “they agreed” is not the same as “they understood.”
- Explain the **Belmont Report principles** and apply them to tech settings:
	- **Respect for persons** (real consent + ability to opt out)
	- **Beneficence** (reduce harm, increase benefit)
	- **Justice** (burdens/benefits distributed fairly)
- Explain the **“problem of many hands”** (responsibility gaps) and propose a practical way to assign responsibility in complex systems.
- Recognize how “objective” systems can still encode discrimination through:
	- biased historical data
	- proxy variables
	- feedback loops that repeat inequality
- Be able to answer: **What kind of error is worse in justice settings?** (false positives vs false negatives), and why that choice is not purely technical.
> [!TIP] Film-paper checklist (what your paper must show)
> - Define Kranzberg #1 clearly.
> - Use 2–3 specific scenes as evidence.
> - For each scene: state the *intended* effect vs the *actual* effect, and who benefits vs who is harmed.
> - Close with a clear claim: the film supports, challenges, or complicates Kranzberg #1.
## Key ideas (readings)
### *Weapons of Math Destruction* (Ch. 2–3)
- **Chapter 2: models inside finance**
	- “Smart” systems can be treated as unquestionable because they’re complex and secretive, which makes accountability harder.
	- Incentives shape outcomes: if success is defined by performance signals rather than human impact, harm becomes easier to ignore.
	- A key theme is how technical systems can be used to extract value from regular people while staying insulated from scrutiny.
- **Chapter 3: rankings as a scaled sorting machine**
	- Rankings often measure “quality” using **proxies** (easier-to-measure stand-ins), so institutions start optimizing the proxy instead of the real goal.
	- When the ranking becomes the standard, it reshapes behavior and can create self-fulfilling cycles.
	- Opacity matters: if people can’t see what’s being measured or contest it, the ranking gains authority without accountability.
### Readings in the Philosophy of Technology (Kaplan intro)
- Technology isn’t just “tools”; it shapes the background conditions of daily life (how we learn, work, communicate, and organize society).
- Key shift: the “philosophy of technology” treats values and assumptions as **inside** technical practice, not just external “side effects.”
- Four classic lenses you should be able to name and recognize:
	1. Neutrality / instrumentalism
	2. Determinism
	3. Autonomy
	4. Social construction (society and technology shape each other)
### *Race After Technology* (Benjamin intro)
- Systems that look neutral can still reproduce unequal outcomes because bias can live in data, design choices, deployment context, and who gets harmed.
- “Default” design decisions often protect some users while creating friction or surveillance for others.
- “Constituents” framing: tech systems can govern access and opportunity even when people never opted in.
## Examples worth keeping
1. **Tuskegee Syphilis Study**: harm defended as “good science,” but people were deceived and denied proper treatment; this is a foundation case for modern research ethics.
2. **Therac-25**: software failure in a safety-critical system + “everyone followed procedure” created a responsibility gap.
3. **Facebook Emotional Contagion**: large-scale experiment without meaningful consent; “Terms of Service” used as a shield.
4. **COMPAS**: “objective” scoring still produced unequal outcomes via biased data + proxies + feedback loops.
5. **Blackstone’s Ratio**: forces a clear discussion of which errors a society should tolerate in high-stakes decisions.
## Kranzberg’s 6 laws
1. *Technology is neither good nor bad; nor is it neutral*: impact depends on how it’s used, by whom, and in what context.
2. *Invention is the mother of necessity*: new tech creates new needs and dependencies rather than only solving old problems.
3. *Technology comes in packages, big and small*: adopting one system brings dependencies (infrastructure, institutions, data practices).
4. *Nontechnical factors take precedence in technology-policy decisions*: social, political, and economic forces often decide outcomes more than the artifact itself.
5. *All history is relevant, but the history of technology is the most relevant*: past effects and reactions help predict long-term impacts; we often overestimate short-term effects and underestimate long-term ones.
6. *Technology is a very human activity – and so is the history of technology*: values, bias, and human decisions shape design and deployment.
> [!NOTE] How Week 2 connects to Week 1
> Week 1: models can be harmful at scale.  
> Week 2: tech outcomes depend on context (Kranzberg #1) and ethical guardrails often appear *after* harm occurs.
## Lecture
### Weekly (Daily) Curiosity Practice
- The exercise is not debate. The goal is to train understanding:
	- Ask for an “unpopular” opinion.
	- Ask two probing questions without challenging.
	- Reflect back what you heard to confirm you understood.
	- Switch roles.
### Housekeeping + Paper workflow
- Paper 1 is coming quickly; appointments with writing fellows / TAs are encouraged.
- Acceptable AI use (if you choose to use it): grammar/spelling help **without** changing your style or arguments (prompted as a “helpful writing teacher”).
- Submissions must be in Google Docs (version history helps address AI concerns and it’s easier for grading).
### Kranzberg + Paper 1 focus
- The paper is explicitly built around **Kranzberg’s First Law**.
- Core paper move: don’t just say “the tech caused harm.” Show:
	- who used it, for what purpose
	- who benefited / who paid the costs
	- what context (laws, incentives, deployment choices) shaped the outcome
### A brief history of ethics in tech (four case studies)
#### Case Study 1: Tuskegee → birth of research ethics
- What happened: deception and denial of effective treatment.
- What changed:
	- Belmont principles (respect for persons, beneficence, justice)
	- Institutional Review Boards (review before research begins)
	- Real informed consent requirements (what the study is, risks, opt-out)
#### Case Study 2: Therac-25 → when software bugs kill
- What happened: software race condition caused dangerous overdoses; error messages became “normal,” so warnings were ignored.
- Key idea: **defense in depth** matters; safety should not rely on software alone.
- Responsibility gap: engineers, manufacturer, operators, regulators all had “not my fault” explanations.
#### Case Study 3: Facebook emotional contagion → consent in the digital age
- What happened: huge-scale experiment on users without their awareness.
- The consent question: “Terms of Service” agreement vs actual informed consent (users didn’t know what was being tested).
- What changed (and didn’t): more public awareness; limited regulation; A/B testing continues.
#### Case Study 4: COMPAS → algorithmic bias
- What it is: risk scoring used in courts for decisions like bail/sentencing.
- Why “neutral” can still be biased:
	- historical policing patterns shape training data
	- proxies correlate with race and class
	- feedback loops amplify inequality across time
- Ongoing issue: opacity (trade secret) + limited oversight.
### Connecting thread across the case studies
- In each case, people believed they were doing something scientific, safe, or objective.
- In each case, harms landed hardest on vulnerable groups.
- In each case, ethical guardrails lagged behind the technology.
### Looking forward (how to think in this course)
When analyzing any tech (including your film), practice these questions:
- Who benefits? Who is harmed?
- What did creators intend? What actually happened?
- Who has power over it? Who doesn’t?
- What ethical constraints existed (or were missing)?
- What would accountability look like in practice?
## [[In Class Assignment#Week - 2|Writing Prompts]]
- Writing Prompt #1: add a new law to Kranzberg’s list (what should it capture that the 6 miss?)
- Writing Prompt #2: “good science” used to justify harm → how this shows up in tech today (data collection, A/B testing, model training)
- Writing Prompt #3: responsibility when complex systems fail → how to avoid “many hands” blame
- Writing Prompt #4: what informed consent should mean online; is clicking “I Agree” enough?
- Writing Prompt #5: COMPAS → abandon or fix? what does “fair” mean, who defines it, and what’s the alternative?
## Takeaways (questions to resolve)
- [ ] For my film: what is the clearest scene that shows the tech is *not* neutral, and what is my exact claim about it?
- [ ] Which nontechnical factors mattered most in the film (policy, profit incentives, institutional power, culture)?
- [ ] If I apply Belmont principles to a modern tech example, what changes (consent, harm reduction, fairness)?
- [ ] In a real responsibility gap, who should be accountable: builders, deployers, regulators, or all of them—how do I justify that?
- [ ] In a justice algorithm, which error is worse (false positives vs false negatives) and why should society prefer one tradeoff?
## Flashcards
#cards/CSCI3923
1. What does Kranzberg’s First Law mean?::Technology’s effects depend on context and use; it’s not simply “good” or “bad,” and it isn’t neutral.
<!--SR:!2026-02-15,4,270-->
2. What is “technology comes in packages”?::Adopting a tool brings dependencies (infrastructure, institutions, data practices) that shape outcomes.
<!--SR:!2026-02-15,4,270-->
3. What are the Belmont Report principles?::Respect for persons (real consent), beneficence (reduce harm), justice (fair distribution of burdens/benefits).
<!--SR:!2026-02-15,4,270-->
4. What is the “problem of many hands”?::When harms happen in complex systems and responsibility gets diffused so no one is held accountable.
<!--SR:!2026-02-15,4,270-->
5. Why can “objective” algorithms still be biased?::They can inherit biased data, use proxies tied to inequality, and create feedback loops that repeat harm.
<!--SR:!2026-02-15,4,270-->
6. What is Blackstone’s Ratio used for in this unit?::To reason about which errors are worse in justice (false positives vs false negatives) and what tradeoffs we tolerate.
<!--SR:!2026-02-15,4,270-->
7. What is the practical difference between ToS consent and informed consent?::ToS is blanket permission; informed consent requires understanding what’s being done, risks, and a real option to refuse.
<!--SR:!2026-02-15,4,270-->
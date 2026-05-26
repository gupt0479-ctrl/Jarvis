---
type: class
input_kind: lecture
status: tree
created: 2026-02-05
updated: 2026-02-26
area:
  - "[[UMN Board]]"
  - "[[CSCI 3923 Board]]"
  - "[[Reading Assignment - 3]]"
  - "[[In Class Assignment]]"
tags:
  - "#class"
  - "#Lecture"
next: "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 3923/Week - 5|Week - 5]]"
---
# Entire Week
## What you must be able to do
- Explain why the “**nothing to hide**” argument clashes with the logic of constitutional rights (rights are about **limits on power**, not proof of innocence).
- Identify Daniel Solove’s main critiques of “nothing to hide”:
	- privacy ≠ wrongdoing
	- the state defines “wrong” (and that can change)
	- aggregation (small bits become a full picture)
	- chilling effects (people self-censor)
	- power imbalance (watchers gain leverage)
- Distinguish the **4 kinds of privacy** and give an example of each:
	- **Bodily** (your body), **Territorial** (spaces), **Communication** (messages), **Information** (personal data).
- Describe where US privacy protections come from even though “privacy” isn’t explicitly written in the Constitution (how the **1st/3rd/4th/5th/9th/14th** amendments get used in privacy reasoning).
- Compare **GDPR vs. US-style privacy laws (CCPA)** at a high level:
	- what counts as “personal data,” what rights individuals get, and what makes enforcement feel stronger or weaker in practice.
- Explain what **surveillance capitalism** means as a business pattern:
	- human experience → behavioral data → prediction products → sold to influence future behavior.
- Define **chilling effect** and describe why it matters for democratic life (speech, search, association).
- Explain the **Third Party Doctrine** problem for digital life:
	- if data is held by a third party, courts have often treated it as having weaker privacy expectations, which changes what the government can access.
- Connect surveillance topics back to WMD logic:
	- **opacity + scale + damage** shows up in ad targeting, policing models, and data markets.
> [!TIP] Quick “privacy analysis” you should be able to run on any app/service
> 1) What data does it *need* to function vs. what does it *collect anyway*?  
> 2) Who gets the data (company teams, partners, data brokers, government requests)?  
> 3) What harms become possible through aggregation + long retention?  
> 4) Can a person view/correct/delete data and contest decisions?
## Key ideas (textbook)
- **Chapter 4 — Propaganda Machine (Online Advertising)**
	- Modern advertising systems don’t just “match products”; they **profile** people and look for **vulnerabilities** (“pain points”) to push high-pressure offers.	
	- **Lead generation** turns attention into a pipeline: misleading hooks → names/contacts collected → sold to recruiters → repeated pressure/contact.
	- **A/B testing** helps ads find the exact message that triggers clicks; combined with learning-based targeting, it becomes a scalable system for manipulation.
	- Why it fits the WMD pattern:
		- **Opacity:** targets don’t know why they were chosen or what profile exists.
		- **Scale:** automated targeting runs on huge populations.
		- **Damage:** pushes harmful “solutions” onto people already under pressure.
- **Chapter 5 — Civilian Casualties (Justice + Big Data)**
	- Predictive policing tools use past records to mark where police should focus.
	- The key ethical failure is often the **feedback loop**:
		- policing increases in an area → more low-level enforcement found → “new data” confirms the system → policing increases again.
	- “Neutral” inputs can still act like **proxies** (e.g., location standing in for race because of residential segregation patterns). 
	- A repeated theme: systems optimize **efficiency** more easily than **fairness**, and fairness gets treated as optional instead of required. 
## Concepts created today
- [[Reading Assignment - 3#Chapter - 4|Reading - Chapter 4]]
- [[Reading Assignment - 3#Chapter - 5|Reading - Chapter 5]]
- [[In Class Assignment#Week - 3|Writing Prompts]]
## Examples worth keeping
1. **Location sharing (maps apps)**
	- Big benefit: navigation, traffic re-routing, faster emergency response.
	- Risk: location trails can expose routines (home/work, health visits, places of worship) and become useful to parties you didn’t intend.
2. **Snowden disclosures**
	- Shows how surveillance can expand through infrastructure + secrecy, and why oversight procedures matter when systems scale.
3. **Cambridge Analytica**
	- Example of personal data + targeting used to influence democratic processes.
4. **Predictive policing (PredPol)**
	- A “neutral” model that can still keep returning to the same neighborhoods because enforcement creates the dataset it later “learns” from.
## Lecture
### Housekeeping + skill practice
- **Quiz rules:** one sheet of handwritten notes.
- **Curiosity routine:** practice understanding before debating (ask probing questions; reflect back).
- **Paper #1 workflow reminders:** revision techniques (thesis visible; annotate paragraph purpose; read aloud).
- **AI + ethics note from slides:** emphasis on character/values and not copying text; if used, treat as tutoring-style feedback, not a generator.
### The “nothing to hide” problem
- The core claim: “nothing to hide” is **backwards** under the Bill of Rights; the government must justify intrusion.
- Constitutional anchors:
	- **4th Amendment:** protection against unreasonable searches/seizures.
	- **1st Amendment:** anonymous speech protection (anonymity as a shield).
	- **5th Amendment:** protection against self-incrimination shows the system explicitly protects not being forced to expose yourself.
- Solove’s critique (why privacy is bigger than “secrets”):
	- privacy supports autonomy
	- laws and norms shift; data can outlast context
	- aggregation turns harmless pieces into sensitive profiles
	- chilling effect changes behavior
	- surveillance creates power imbalances 
> [!IMPORTANT] What to remember for arguments
> “I’m not doing anything wrong” doesn’t answer “Should anyone have this level of access?”
> The ethical question is about **procedures, limits, and contestability** when power scales.
### What privacy is (and isn’t)
- Privacy is not about hiding bad acts; it includes:
	- bodily, territorial, communication, and information privacy.
- Why it matters for democracy:
	- privacy supports moral autonomy (people can think, associate, and decide without constant pressure).
### “Right to privacy” in the US (how it’s argued)
- “Privacy” isn’t written directly in the Constitution, but protections are argued through multiple amendments (1st/3rd/4th/5th/9th/14th), with cases like *Griswold v. Connecticut* used in privacy reasoning. 
### GDPR vs. US privacy law framing
- **GDPR** basics from slides:
	- applies to any company serving EU residents
	- includes rights like erasure (“right to be forgotten”), data portability, explicit consent requirements.
	- “Personal data” includes many identifiers (including location data and cookies).
- **CCPA** slide point:
	- the US has privacy laws too, but a practical issue is whether people can realistically track every company/data broker they interacted with and what happens after onward selling.
### Benefits vs. concerns in data sharing
- Benefits listed: personalization, better UX, security/fraud detection, research, planning, etc.
- Concerns listed:
	- most people don’t read policies / don’t know what’s collected
	- security breaches
	- profiling affecting hiring/credit/insurance
	- manipulation (advertising + politics)
	- children’s privacy.
- Discussion focus: where you personally draw the line (what tradeoffs you accept).
### Surveillance capitalism + major case studies
- Surveillance capitalism definition (Zuboff framing): human experience becomes behavioral data, packaged into prediction products, and sold to influence behavior.
- Snowden disclosures as a public example of scale + oversight concerns.
- Cambridge Analytica as an example of data harvesting + political targeting.
### Chilling effect + the panopticon idea
- Empirical claim in slides: surveillance news changed behavior (privacy settings, word avoidance, reduced sensitive searches).
- Foucault’s “panopticon” framing: visibility becomes a mechanism of power that people internalize. 
### The Third Party Doctrine problem
- If data is held by a third party, courts have often treated it as not protected the same way, enabling warrantless access to many categories (browsing history, purchase records, cloud/email metadata, etc.).
### What you can do (practical layer)
- Technical steps (settings review, privacy-focused browsers, encrypted messaging, opt-outs).
- Civic steps (support legislation, support groups like EFF/ACLU, demand transparency, educate others).
### [[In Class Assignment#Week - 3|Writing Prompts]]
- Linked here: your responses on (1) why privacy matters even if innocent, (2) maps/location tradeoffs, (3) school data practices + consent, (4) privacy as a right vs convenience trade.
## Takeaways (questions to resolve)
- [ ] When someone says “nothing to hide,” what *kind* of claim are they making: (a) about guilt, (b) about trust in institutions, or (c) about acceptable power limits?
- [ ] What changes if we treat privacy as protecting **autonomy** rather than protecting “secrets”? How would that change system design requirements?
- [ ] Where should the “line” be for location data: only during active use, short retention, no onward sharing by default—what minimum rules actually protect people?
- [ ] If data is sold onward through brokers, what would “meaningful consent” have to look like for consent to be real rather than just a checkbox?
- [ ] What’s a concrete example where aggregation turns “harmless” data into something sensitive (and what harm follows)?
- [ ] How would you argue for reforming the Third Party Doctrine using the logic of modern digital life?
## Flashcards
#cards/CSCI3923
1. What is the “nothing to hide” argument missing?::Rights limit government power; privacy protects autonomy, not just secrecy.
<!--SR:!2026-02-26,3,250-->
2. What are Solove’s five critiques of “nothing to hide”?::Privacy ≠ wrongdoing; government defines “wrong”; aggregation reveals; chilling effect; power imbalance.
<!--SR:!2026-02-26,3,250-->
3. What are the four kinds of privacy used in lecture?::Bodily, territorial, communication, and information privacy.
<!--SR:!2026-02-26,3,250-->
4. Why does the chilling effect matter?::People self-censor when watched, which harms speech, inquiry, and democratic participation.
<!--SR:!2026-02-26,3,250-->
5. What is surveillance capitalism (in one line)?::Turning human experience into behavioral data to build prediction products that are sold to influence behavior.
<!--SR:!2026-02-26,3,250-->
6. What is the Third Party Doctrine issue?::Data held by third parties is often treated as having weaker privacy expectations, enabling broad access without a warrant.
<!--SR:!2026-02-26,3,250-->
7. How do WMD ideas show up in surveillance systems?::Opacity + scale + damage: hidden profiling and broad deployment can cause real harm with limited ways to contest.
<!--SR:!2026-02-26,3,250-->
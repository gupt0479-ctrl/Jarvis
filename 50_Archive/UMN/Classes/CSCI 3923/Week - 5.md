---
type: class
input_kind: lecture
status: tree
created: 2026-02-26
updated: 2026-02-26
area:
  - "[[UMN Board]]"
  - "[[CSCI 3923 Board]]"
  - "[[Reading Assignment - 4]]"
  - "[[In Class Assignment]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[50_Archive/UMN/Classes/CSCI 3923/Week - 6|Week - 6]]"
---
# Entire Week
## What you must be able to do
- Explain the difference between **digital divide** (who is online vs not) and **digital equity** (whether access actually meets real needs).
- Identify the **dimensions of “access”** (economic, physical, educational) and explain how each one can block participation even when “the internet exists.”
- Recognize how “access” can fail **even when coverage is reported** (maps, self-reported ISP data, marketing vs delivered speeds).
- Use at least **two ethical frameworks** to evaluate digital equity questions (ex: utilitarian vs justice/rights-based vs social contract).
- Define **digital sovereignty** and compare governance models (platform-controlled “free access,” state-controlled infrastructure, private ISP dominance).
- Distinguish **Ethical Design (top-down)** vs **Human-Centered Design (bottom-up)** vs **Inclusive Design (user-defined)** and explain who pays the cost of each approach.
- Apply the inclusive design core claim and test a product against it:
> [!NOTE] “All users should have a comparable experience.”
- List and apply the **7 Principles of Inclusive Design** (equitable use, flexibility, simple & intuitive, perceptible information, tolerance for error, low physical effort, size & space).
- Explain why accessibility is cheaper and more reliable when **built in** rather than added at the end (architecture + refactor + technical debt tradeoff).
- Connect this week’s lecture back to *Weapons of Math Destruction*:
  - Hiring and workplace scheduling systems can function like WMDs when they scale, hide rules, and create harm for people with the least power.
## Key ideas (textbook)
- **Chapter 6 - “INELIGIBLE TO SERVE: Getting a Job”**
	- Automated hiring is used at **huge scale**, so small errors become repeated exclusion.
	- **Personality tests** can behave like hidden medical screening and block capable applicants before any human review.
	- Hiring systems rely on **proxies** (personality signals, resume formatting/keywords) instead of direct ability.
	- **Resume robots** filter most applications before a person sees them; “safe” formatting and keyword matching can sort by privilege.
	- Bias can get automated (ex: name-based differences in callbacks), turning older patterns into faster sorting.
	- Some companies *can* remove a harmful variable when they notice it’s functioning as a poverty proxy (example: commute distance).
	- “Digital phrenology” framing: systems claim to measure inner traits using weak assumptions, then treat outputs as truth.
- **Chapter 7 - “Sweating Bullets: On the Job”**
	- Scheduling systems optimize staffing hour-by-hour and treat workers as **just-in-time inputs** rather than people with lives.
	- **Clopening** is a concrete harm: closing late + opening early wrecks sleep, planning, childcare, and stability.
	- These systems fit the WMD pattern:
		- **Opacity:** workers can’t see or challenge why schedules shift.
		- **Scale:** used across major employers.
		- **Damage:** instability pushes people into worse outcomes (school plans collapse, health suffers, life becomes unmanageable).
	- Worker-evaluation tools often can’t measure “soft skills,” so they misclassify value when it isn’t in text logs.
	- “Objective” scoring can be unstable (teacher value-added swings), showing statistical noise can become punishment.
- **Extra - Ethical Frameworks (Tavani)**
	- **Cultural relativism / moral subjectivism / moral relativism:** explain why “it depends” can describe reality, but often fails to guide action in conflict or harm.
	- **Act vs rule utilitarianism:** consequences matter, but majority-based logic can still justify harm to minorities.
	- **Kantian deontology:** duties + “people as ends,” plus universal-rule reasoning; strong at flagging exploitation and coercion.
	- **Social contract:** asks what rules people would accept to live together; highlights legitimacy, enforcement, and fairness.
	- **Rights-based theories:** focuses on basic rights and conflicts between them (especially relevant for privacy, education access, and disability access).
	- **Virtue ethics:** focuses on what kind of person/professional you become; connects directly to design habits and responsibility.
	- **Legalism (warning):** “it’s legal” ≠ “it’s ethical,” especially with new tech where law lags behind harm.
## Concepts created today
- [[Reading Assignment - 4#Chapter - 6|Reading - Chapter 6]]
- [[Reading Assignment - 4#Chapter - 7|Reading - Chapter 7]]
- [[Reading Assignment - 4#Ethical Frameworks| Reading(Extra) - Ethical Frameworks]]
- [[In Class Assignment#Week - 5|Writing Prompts]]
## Examples worth keeping
1. **Kyle Behm + personality test “red-light” (hiring gatekeeper):**
	- A test blocks an applicant before any human conversation; the system acts like a hidden screening tool.
2. **Resume robot filtering + name signal problem:**
	- Automated screening + formatting/keyword rules can sort applicants by signals unrelated to job ability.
3. **Clopening (scheduling harm at scale):**
	- Algorithmic scheduling produces unstable hours that break sleep, planning, and school/family commitments.
4. **FCC broadband maps built from self-reported ISP claims:**
	- Coverage can be overstated, causing resources and policy decisions to miss the people who actually lack service.
5. **“Built-in” vs “added later” accessibility:**
	- Building accessibility from requirements (semantic HTML, keyboard navigation, contrast) avoids brittle retrofits and recurring technical debt.
## Lecture
- **Daily Curiosity Practice**
	- Pair exercise: describe a time you felt excluded by a design.
	- Rule: ask probing questions to understand; no debate.
- **Housekeeping (research + writing)**
	- Pick a tech-related ethical issue.
	- Do research and plan credible sources.
	- You must present your thesis/opinion and support it.
- **Part 1: Digital Equity — “Who has access, and why does it matter?”**
	- Internet use is widespread but uneven (global gap + within-country gaps).
	- **Mobile-only access**
		- When the phone is the only device, key tasks become harder: applications, homework, telehealth.
	- **Urban vs rural**
		- Geography compounds disadvantage (infrastructure + affordability + other demographics).
	- **Broadband definition problem**
		- A fixed standard can lag behind real needs (video calls, cloud-based schoolwork).
	- **Access is multi-dimensional**
		- Economic access: affordability of service + devices.
		- Physical access: barriers when access depends on schools/libraries; disability compliance is inconsistent.
		- Educational access: uneven digital literacy opportunities and barriers across age groups.
	- **Human rights framing**
		- If education and an adequate living standard are rights, and access is now a prerequisite for both, the ethical stakes shift from “nice-to-have” to “participation.”
- **Digital sovereignty — “Who controls the internet, and who should?”**
	- Platform-gated “free access” can restrict the internet to a company ecosystem.
	- State-controlled infrastructure can expand coverage while enabling censorship and surveillance.
	- Private ISP dominance can reduce state control but still produce market failure (underserved rural/low-income areas).
- **Part 2: Inclusive Design — “Who is technology designed for?”**
	- Quick classroom scan: identify what’s wrong with the room as a design space (sightlines, acoustics, mobility, left-handedness, etc.).
	- **Three design philosophies**
		- Ethical design (top-down): designers decide what’s harmful/helpful.
		- Human-centered (bottom-up): majority end-user needs drive design.
		- Inclusive design (user-defined): diverse input + accessibility + equity; aims for usability across everyone, including disabled users.
	- **Core idea**: “All users should have a comparable experience.”
	- **How to start with inclusive design**
		- Recognize exclusion (implicit bias exists; diverse teams are a starting point).
		- Learn from diversity throughout the process, not only at the end.
		- Solve for one, extend to many (captions/curb cuts logic).
	- **7 principles of inclusive design**
		- Equitable use; flexibility; simple & intuitive; perceptible information; tolerance for error; low physical effort; size & space.
	- **Why this isn’t usually taught in programming courses**
		- Time pressure, “it’s UX/business,” and what that communicates about priorities.
	- **Baking in vs bolting on accessibility**
		- Built-in: planned requirements → lower cost, better architecture.
		- Added later: refactor + regression testing + gaps → brittle solutions + ongoing technical debt.
	- **Connecting the two halves**
		- Digital equity asks who can access tech at all.
		- Inclusive design asks who tech is actually built for once they’re online.
		- Together: who participates in the digital world, and on whose terms?
## [[In Class Assignment#Week - 5|Writing Prompts]]
- Prompt 1: Personal history of internet access + what “high speed” means + who decides access.
- Prompt 2: Equal standard of living without internet + education without it + “free internet” that collects personal data + ethical principles involved.
- Prompt 3: Kranzberg’s First Law applied to internet access + negative consequences + whether access should be treated like a right.
- Prompt 4: “Comparable experience” in practice + inclusive design obligation + tradeoffs + who bears the cost of exclusion.
## Takeaways (questions to resolve)
- [ ] When a policy says “everyone can apply online,” what *specific* access assumptions are hiding underneath (device, bandwidth, disability access, literacy)?
- [ ] What’s the ethical difference between **equality** (“same access”) and **equity** (“access that meets needs”) in a real example like school portals or telehealth?
- [ ] If internet access is treated like a prerequisite for education and adequate living standards, what duties follow for governments, schools, and companies?
- [ ] In “free access” programs, what is the real exchange: what do users give up, and who holds power after the deal?
- [ ] Which framework best supports inclusive design as an obligation (justice/rights-based/Kantian/social contract), and why isn’t a majority-benefit argument enough?
## Flashcards
#cards/CSCI3923 
1. What is the difference between digital divide and digital equity?::Digital divide is who is online vs not; digital equity is whether access actually meets real needs (devices, bandwidth, literacy, disability access).
2. What are the three access dimensions highlighted in lecture?::Economic access, physical access, and educational access.
3. What is digital sovereignty?::Who controls the internet (infrastructure, rules, platforms) and who should control it.
4. What is the core claim of inclusive design?::All users should have a comparable experience (comparable quality, dignity, and access to information).
5. What are the three design philosophies compared in lecture?::Ethical design (top-down), human-centered design (bottom-up), and inclusive design (user-defined).
6. Why is “baking in” accessibility better than adding it at the end?::Built-in accessibility becomes part of requirements and architecture; late retrofits are brittle, costly, and create ongoing technical debt.
7. What is “clopening” and why is it ethically significant?::A shift pattern where a worker closes late and opens early; it shows how scheduling systems can create real harm through instability at scale.
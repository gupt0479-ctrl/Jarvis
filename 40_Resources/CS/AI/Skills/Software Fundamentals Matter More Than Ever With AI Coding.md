# Software Fundamentals Matter More Than Ever With AI Coding

Related: [[AI Coding]], [[Software Engineering]], [[Test-Driven Development]], [[Domain-Driven Design]], [[Code Architecture]], [[Prompt Engineering]]

## Main Thesis

The speaker's central message is that "software fundamentals matter now more than they actually ever have." AI coding tools do not make code quality, design, testing, and architecture less important; they make those fundamentals more important because they determine whether AI can be useful at all. If the codebase is hard to understand and modify, AI cannot deliver its full value. The human developer's role is to provide strategic design direction, shared language, module boundaries, and feedback loops while letting AI handle more tactical implementation work.

## Why Specs-to-Code Fails

"Specs-to-code" means writing a specification for how an application is supposed to work, using AI to turn that specification into code, and then changing the spec whenever there is a problem instead of inspecting or designing the code. In this workflow, the developer does not really look at the code. They edit the spec, run the compiler or generator again, and get more code.

The speaker tried this because the idea is tempting: if AI is a new paradigm, maybe the old rules can be thrown away and code can be treated as an output artifact that manages itself. But in practice, each run produced worse code. The first generation produced code, the next run produced worse code, and repeated regenerations produced garbage.

The problem is that repeatedly changing only the specification means the design of the codebase is not being actively maintained. Every change is made locally, with attention only on the current change, not on the structure of the whole system. This is software entropy: the codebase gets worse and worse over time unless someone is investing in its design.

The speaker compares this to "vibe coding by another name." Ignoring the code and hoping the generator can manage the codebase by itself is not a real engineering workflow. It avoids the work of understanding, shaping, and improving the system.

## Code Is Not Cheap

The phrase driving a lot of specs-to-code thinking is "code is cheap." The speaker disagrees: "code is not cheap." More specifically, "bad code is the most expensive it's ever been."

Bad code is expensive because AI performs poorly when the codebase is hard to change, hard to test, and hard to reason about. If the codebase is difficult to modify without causing bugs, then the developer cannot take advantage of what AI offers. A bad codebase blocks the value of AI.

A good codebase is easy to change. The speaker draws on John Ousterhout's definition of complexity: "complexity is anything related to the structure of a software system that makes it hard to understand and modify the system." A good codebase lowers that complexity. It gives both humans and AI clearer structure, better feedback, easier testing, and safer places to make changes.

## Failure Mode 1: The AI Did Not Do What I Wanted

The first failure mode is when the developer thinks they have a clear idea, but the AI builds something different. The speaker connects this to requirements gathering. No one knows exactly what they want at the beginning, and when the human talks to the AI, the AI is effectively trying to gather requirements.

There is a communication barrier between the human and the AI. The human has an idea in their head, but the AI does not automatically share that idea. The speaker connects this to Frederick P. Brooks' idea of the "design concept" from *The Design of Design*.

The design concept is the invisible theory of what is being built. It is not just a Markdown file or an asset. It is the shared understanding that exists between people designing something together. The failure happens because the human and the AI do not share the same design concept.

### Skill: Grill Me

The speaker's first practical skill is called "Grill Me." The instruction is essentially: interview me relentlessly about every aspect of this plan until we reach a shared understanding. The AI walks down each branch of the design tree, resolving dependencies between decisions one by one.

The design tree matters because decisions depend on other decisions. Instead of jumping straight into a plan, the AI asks many questions: sometimes 40, 60, or even 100 questions before it is satisfied that there is a shared understanding. This turns the AI into a kind of adversarial interviewer, continually pushing ideas back to the user and checking whether the design concept is actually shared.

Once that conversation exists, it can become a product requirements document, or for a smaller change it can become implementation issues. The point is to reach shared understanding before planning. The speaker prefers this to eager plan creation because a plan is less useful if the human and AI do not yet share the same design concept.

## Failure Mode 2: The AI Is Too Verbose

The second failure mode is that the AI is too verbose. It feels like the human and AI are talking at cross-purposes. The AI uses too many words because it is trying to communicate without a shared language.

The speaker compares this to developers working with domain experts. If a domain expert is talking about microchips and the developer does not understand that domain, there is a language gap. The domain expert uses terms the developer does not understand, the developer translates those terms into code, and then neither the developer nor the domain expert may fully understand what has been built.

The speaker connects this to [[Domain-Driven Design]] and the idea of a ubiquitous language. In domain-driven design, conversations among developers, expressions in the code, and conversations with domain experts are all derived from the same domain model. The same terms are used in conversation, planning, and code.

### Skill: Ubiquitous Language

The speaker's second skill is the "Ubiquitous Language" skill. It scans the codebase, looks for terminology, and creates a shared Markdown file containing the terms. The speaker describes it as essentially a Markdown file full of terms that the human and AI have in common.

The team then uses those same terms in planning, code, and AI conversations. The speaker keeps the file open while grilling and planning with the AI. The shared language improves the AI's thinking traces, reduces verbosity, and makes implementation more aligned with the plan.

The lesson is to create a shared language with the AI before expecting it to plan and implement clearly. Shared terminology makes it easier for both the human and the AI to stay attached to the same domain model.

## Failure Mode 3: The AI Built the Right Thing, But It Does Not Work

The third failure mode is when the AI appears to build the right thing, but the result does not work. The speaker's answer is feedback loops. Good feedback loops include static types, browser access for frontend work, and automated tests.

If the project is using frontend AI coding, the AI needs access to the browser so it can look around and inspect what it built. If the project is TypeScript-capable, static types matter. Automated tests are also essential.

Even with feedback loops available, the AI often does not use them the way a veteran developer would. It tends to do too much at once: produce a large amount of code, then only later think about typechecking, running tests, or checking behavior. The speaker connects this to the Pragmatic Programmer idea of "outrunning your headlights."

The core line is: "the rate of feedback is your speed limit." If feedback is slow, change must be slower and more deliberate. The AI needs to be forced into smaller steps so it can test as it goes instead of racing ahead of what it can verify.

### Skill: Test-Driven Development

The third skill is [[Test-Driven Development]]. The speaker argues that TDD forces the LLM to take smaller steps. First, write a test. Then make the test pass. Then refactor the code and consider the design.

This pattern gives the AI a tighter feedback loop. It prevents the model from making a large, unverified change all at once. It also makes design work part of the cycle instead of something postponed until after the code has already sprawled.

Testing is difficult, though. The speaker emphasizes that testing has always been hard. You have to decide how big a unit to test, what to mock, and which behaviors are worth testing. These decisions are interdependent: choosing the size of the unit affects what must be mocked, how flaky the test might be, and which behaviors can be verified.

## Testable Codebases and Deep Modules

Good codebases are easier to test. This brings the talk back to why code matters. The better the codebase, the better the feedback loops; the better the feedback loops, the better the AI output.

The speaker again turns to John Ousterhout and the idea of "deep modules." A testable codebase has relatively few large, deep modules with simple interfaces, not lots of shallow modules exposing many functions and dependencies.

Deep modules make it easier for humans and AI to understand where behavior belongs. They also make it easier to test through stable boundaries. A codebase structured around deep modules rewards TDD because there are clear interfaces where tests can verify behavior.

### Deep Modules

Deep modules provide lots of functionality hidden behind a simple interface. The complexity is inside the module. From the outside, the interface is easier to understand, easier to use, and easier to test.

The point is not that the implementation is unknowable. You can look inside a deep module if you need to. But most of the time you should be able to use the interface without carrying the whole implementation in your head.

### Shallow Modules

Shallow modules provide a small amount of functionality behind a complex interface. They create many tiny dependencies and many small pieces the AI has to walk through and understand.

A codebase full of shallow modules is hard for humans and AI to navigate. The AI may try to explore the code, but because the code is poorly laid out, it may not reach the right module in time or may fail to understand the dependencies before making changes.

AI is good at creating shallow, tangled codebases if it is not guided. That is why the human needs to design the boundaries and interfaces deliberately.

## Skill: Improve Codebase Architecture

The speaker's architecture skill is to explore the codebase, look for related code, and wrap related behavior into deep modules. The process is reusable: inspect the codebase, find clusters of related behavior, identify boundaries, and create a module interface that hides complexity behind a simpler surface.

Testing then happens through the module interface. The outside boundary becomes the place where behavior is verified. This creates a codebase that rewards TDD because tests can target meaningful interfaces instead of fragile internal details.

The goal is not just tidiness. The goal is to create boundaries that make the system easier to understand, easier to test, easier for AI to modify, and easier for the human to supervise.

## Failure Mode 4: Your Brain Cannot Keep Up

Another failure mode appears when the feedback loops start working and the developer can ship more code than ever before. The problem is that the human brain may not be able to keep up. More code can become mentally exhausting.

Deep modules help because they reduce mental load. In a tangled codebase, both the human and the AI need to keep too much information in mind. In a codebase with deep modules, the developer can treat some modules as gray boxes.

A gray box is a module whose purpose, interface, and behavior are understood from the outside, while the implementation details do not require equal attention every time. The speaker is careful not to apply this to critical areas like finance or other high-risk parts of an application. Critical code still deserves careful review.

But for many modules, the developer does not need to think about every implementation detail as long as there is a testable boundary, the module's purpose is understood, and the module can be designed from the outside.

## Skill: Design the Interface, Delegate the Implementation

The speaker summarizes this skill as: "design the interface, delegate the implementation." The human carefully designs the module interface. The AI can then handle implementation inside that boundary.

Tests should verify behavior from the outside. The developer can inspect the implementation when needed, especially in critical areas, but the main responsibility is to shape the boundary and verify the behavior. This protects the developer's attention because not every internal detail needs the same level of review.

This also means module design needs to be part of planning. When writing a PRD or implementation plan, the speaker is specific about module changes, interfaces, and how those interfaces are being modified. The map of modules should be part of the team's ubiquitous language.

## Strategic Role of the Developer

AI is like a strong tactical programmer: someone on the ground making code changes. But tactical programming still needs strategic design direction. The human developer provides that strategic level.

The speaker connects this to Kent Beck's line: "invest in the design of the system every day." Specs-to-code divests from the design of the system because it treats code as something the generator can handle without human design attention. The speaker argues for the opposite: keep investing in the system's design whenever you touch the code.

Software fundamentals are still essential. Requirements gathering, shared design concepts, ubiquitous language, feedback loops, TDD, deep modules, and careful interfaces are what make AI coding effective. The conclusion is direct: "code is not cheap."

## Key Takeaways

- "Software fundamentals matter now more than they actually ever have."
- Specs-to-code can degrade a codebase if developers stop inspecting, shaping, and improving the code.
- Ignoring the code and repeatedly regenerating from specs is "vibe coding by another name."
- "Code is not cheap"; bad code is expensive because it blocks effective AI usage.
- Good codebases are easy to change, test, and reason about.
- Complexity is structural: "complexity is anything related to the structure of a software system that makes it hard to understand and modify the system."
- The human and AI need a shared design concept before implementation begins.
- A ubiquitous language gives the human and AI the same terms for planning, code, and conversation.
- "The rate of feedback is your speed limit."
- TDD helps AI take smaller, verifiable steps.
- Deep modules hide complexity behind simple interfaces and make testing easier.
- Shallow modules create too many tiny dependencies and make the system harder for AI to understand.
- The human should "design the interface, delegate the implementation."
- Developers should "invest in the design of the system every day."
- AI can act as a tactical programmer, but the human must remain the strategic developer.

## Terms / Concepts

| Term | Meaning in the video |
|---|---|
| specs-to-code | A workflow where the developer writes or edits a specification, uses AI to generate code from it, and changes the spec instead of inspecting or redesigning the code. |
| design concept | Frederick P. Brooks' idea of the shared invisible theory of what is being built; the human and AI need to share it before planning and implementation. |
| design tree | A branching set of design decisions where dependencies between decisions need to be resolved one by one. |
| ubiquitous language | A shared set of domain terms used in conversation, planning, code, and AI interaction, drawn from domain-driven design. |
| feedback loop | A mechanism that tells the developer or AI whether the work is correct, such as static types, browser inspection, or automated tests. |
| TDD | Test-driven development: write a test first, make it pass, then refactor and improve the design. |
| outrunning your headlights | Moving faster than feedback allows; making too many changes before checking whether they work. |
| deep module | A module with lots of functionality hidden behind a simple interface, making it easier to understand, test, and delegate. |
| shallow module | A module with little functionality and a complex interface, creating many dependencies and making the system harder to navigate. |
| software entropy | The tendency for a codebase to get worse over time when each change is made without investing in the design of the whole system. |
| complexity | "Anything related to the structure of a software system that makes it hard to understand and modify the system." |
| tactical programmer | The role AI can play: making concrete code changes on the ground inside a system. |
| strategic developer | The human role: shaping design direction, module boundaries, shared language, and feedback loops. |

## My Notes

For my own [[AI Coding]] workflow, the practical lesson is to use AI for implementation, but not for blind architecture decisions. Before asking the AI to code, ask it to clarify requirements, grill the plan, and expose the design tree so the important decisions are visible.

Maintain shared terminology in a Markdown file and reuse those terms in prompts, planning docs, tests, and code. Prefer small tested changes, especially when using AI agents that tend to do too much at once. Design module boundaries before asking AI to code, then let the AI work inside those boundaries while tests verify behavior from the outside.


---
type: concept
course: CSCI 2041
status: sprout
mastery (1/10): 5
created: 2026-02-12
topics:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Basics]]"
  - "[[OCaml]]"
  - "[[OCaml - BST Problems]]"
related:
  - "[[50_Archive/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]"
---
# Two Types
## Resources
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#1.2 Functional vs. Imperative Programming|Chapter 1.2]]  
- [[50_Archive/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]  
- [[OCaml - Basics|OCaml - Basics]]  
- [[OCaml - BST Problems|OCaml - BST Problems]]  
### How to use them  
1. Practice translating a loop into a recursive helper with parameters (accumulator pattern).  
2. For each list/tree operation, write: “what is new” vs “what stays the same”.
## Definition
- **Imperative programming:** compute by issuing commands that change program state (assignments, loops, mutable updates).  
- **Applicative / functional programming:** compute values by evaluating expressions, mainly via function calls; the course avoids loops/variables as the default style.  
- **Persistence (course meaning):** operations return new structures while original inputs remain usable/unchanged (especially with lists).  
> [!NOTE] Persistence here is about *in-memory* behavior (sharing + non-destructive updates), not “saved to disk.”
## Imperative programming (what the professor expects you to recognize)
### The core idea  
Imperative code “moves forward” by **changing state**:  
- you create variables  
- you update them  
- the order of commands matters (sequential)  
- loops run by repeatedly updating variables until a condition fails  
### How to spot it fast  
- `while`, `for`, assignments like `x = x + 1`  
- “do this, then do that” thinking  
- return is often the final statement  
### Why reasoning is harder  
To prove correctness you usually need:  
- a **loop invariant**  
- an argument that each loop update moves you toward termination  
## Applicative / functional programming (OCaml default in this course) 
### The core idea  
Functional code “moves forward” by **evaluating expressions**:  
- expressions produce values  
- functions compute values from inputs  
- you don’t update variables; you create new values  
### How to spot it fast  
- recursion instead of loops  
- `let` bindings instead of variable reassignment  
- case analysis using `match ... with ...`  
- “what is this expression’s value?” thinking  
### First-class values (why functions matter)  
In OCaml, functions are values: you can  
- pass them as arguments  
- return them from other functions  
- store them in data structures  
> [!INFO] First-class citizen analogy  
> Functions have “full rights”: pass/return/store, like ints and strings.  
## Persistence (the “copy as little as possible” model)
### The course definition (memory behavior)
A data structure is **persistent** if operations don’t destroy the old version:  
- you can keep using the old one  
- the new one may share most of the old structure (pointers/boxes/clouds idea)  
### Lists: `::` vs `@` under persistence  
- `x :: xs` creates a new list node *in front* that points to the old list `xs`  
- `xs @ ys` must copy at least the left list’s spine so the result can point to `ys`    
> [!NOTE] “What is new vs what stays the same?”  
> That sentence is basically the persistence test you should apply to every list/tree function.  
### Trees: persistence is the same idea, but along a path
See the lecture BST insert explanation in:  
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#1.4 Code Example OCaml - BST Problems Week 1 Persistent BST Insert (lecture code) BST Insert|BST Insert]]
- [[OCaml - BST Problems#Week 1 Persistent BST Insert (lecture code)|OCaml - BST Problems → Week 1]]
## Recursion in functional/applicative programming
### Why recursion replaces loops  
In imperative code:  
- “loop variables” change over time  
In OCaml:  
- loop variables become **function parameters**  
- updates become **arguments in the recursive call**  
- loop stopping condition becomes **base case**  
### The required recursion shape (midterm-level)
A correct recursion has:  
1. **Base case**: returns immediately (no recursive call)  
2. **Recursive case**: does a smaller problem  
3. **Progress**: argument moves toward the base case  
> [!WARNING] The professor will penalize “recursive but not decreasing”  
> If the argument doesn’t get closer to the base case, termination isn’t justified.  
### Tail recursion preview (ties to Jan 30 lecture + your Basics file) 
- Tail recursion is how functional code can match loop efficiency.  
- See: [[OCaml - Basics#Tail recursion and stack frames (Jan 30 lecture)|OCaml - Basics → Tail recursion]]     
## “Mix-match logic” (how the course expects you to use both styles) 
OCaml *supports* imperative features, but the course expects:  
- default: functional (expressions, recursion, persistence)  
- sometimes: use imperative tools if they simplify messy state-threading  
**What “mix-match” means in practice**  
- You might write mostly functional code, but still:  
- print/debug (side effects)  
- use mutation in very contained spots (later in course)  
- You still explain the *core computation* in functional terms.  
> [!NOTE] The safe approach for exams: Answer in functional terms first, and only mention imperative features as “optional tools.”
## Common mistakes  
- Treating “persistent” like “saved to disk”.  
- Thinking `::` concatenates two lists (it does not; it adds one element to the front).  
- Mixing “statement mindset” with OCaml expressions (expecting “commands” with no value).  
### Canonical example (the professor’s mental model)
- Translating a loop to recursion:
    - loop “state” becomes parameters
    - updates become recursive-call arguments
    - base case replaces loop stop condition
    - recursion replaces iteration
## Mini-test (questions to resolve)  
- [ ] Given a loop with two changing variables, which ones become function parameters?  
- [ ] Explain persistence using `x` and `0 :: x` (what changes? what doesn’t?)  
- [ ] Why does the course say “we don’t need loops” (hint: tail recursion)?  
- [ ] What does “mix-match” mean, and when is it acceptable?
## Flashcards (best 3–8)

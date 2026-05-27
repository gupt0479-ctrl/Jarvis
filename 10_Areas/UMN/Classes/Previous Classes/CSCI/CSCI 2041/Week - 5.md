---
type: class
input_kind: lecture
status: seed
created:
updated:
area:
  - "[[UMN Board]]"
tags:
next: []
---
# Entire Week
## What you must be able to do
- [[Textbook]]
- 
## Key ideas (textbook)
- 
## Concepts created today
- [[Concept - ...]]
- [[Concept - ...]]
## Examples worth keeping
- 
## Lecture
### Lecture (Feb 16) 
- Left vs Right Reduce, then CPS: continuations, `forLoop`, `generateBools`  
#### Announcements + where we are going  
- Continuing to record lectures.  
- Midterm exam: **Feb 27**.  
- Today bridges:  
  - the “classic list combinators” track (`map`, `filter`, `reduce`)  
  - into **continuation passing style (CPS)**, which we’ll use to generate lots of results without building giant lists.  
  
---  
  
#### Part A — “Classic map functions” continued: `leftReduce` vs `rightReduce`  
The professor’s goal here is *not* “reduce is a library trick,” but:  
- reduce is a **pattern**: “consume a list, combine elements using `f`, end with a default/base value.”  
- the key difference between left and right versions is **where the parentheses go** (how calls to `f` associate).  
  
##### Right association (`rightReduce`)  
Professor’s association picture:  
- `rightReduce f [1; 2; 3] 0` becomes:  
  - `f 1 (f 2 (f 3 0))`  
- The combining happens “down the right side.”  
  
**Code shape (right-associating)**  
```ocaml  
let rightReduce func objects default =  
  let rec reducing objects =  
    match objects with  
    | [] -> default  
    | head :: tail -> func head (reducing tail)  
  in  
  reducing objects  
;;
```
What’s happening line-by-line:

- `[] -> default` is the base case: if there are no objects left, the “combined value so far” is just the default.
    
- `head :: tail -> func head (reducing tail)` says:
    
    - first, reduce the rest of the list to a single value
        
    - then combine `head` with that value using `func`
        

Why professor marks **not tail-recursive**:

- the recursive call is _inside_ `func head (...)`
    
- you can’t finish the current frame until the recursive call returns, then you still must apply `func`.
    

---

##### Left association (`leftReduce`)

Professor’s association picture:

- `leftReduce f [1; 2; 3] 0` becomes:
    
    - `f (f (f 0 1) 2) 3`
        
- The combining “bunches up to the left.”
    

**Code shape (left-associating)**

let leftReduce func objects default =  
  let rec reducing objects =  
    match objects with  
    | [] -> default  
    | head :: tail -> func (reducing tail) head  
  in  
  reducing objects  
;;

What’s different vs `rightReduce`:

- same base case
    
- the recursive result is now the **left argument** to `func`, and `head` is the right argument
    
- that flips the parentheses structure you get
    

Why professor still marks **not tail-recursive**:

- same structural reason: `func (...) head` still needs work after recursion returns.
    

##### Why you should care about left vs right

- If `func` is associative, results may match.
    
- If `func` is not associative (or has side effects, or is expensive in one direction), the two versions can produce different outcomes.
    
- The professor’s framing: understand the **shape of evaluation** and the **nesting**.
    

---

#### Part B — CPS (Continuation Passing Style): definition + why it matters

##### Normal style communication

Usually we think:

- `f x` returns a value `y`
    

##### CPS communication

In CPS, instead of returning the interesting value, `f` _calls another function_ (a **continuation**) with that value:

- `f x (fun y -> ...)`
    

Key sentence in the notes:

- “Functions can also provide values by calling other functions, called continuations.”
    
- Often in CPS:
    
    - we don’t care what `f` returns as a normal return value
        
    - we care what the **continuation receives**
        

##### Why do this? (the professor’s two motivating questions)

1. **What if we don’t know how many values a function will provide?**
    

- 0 values → never call the continuation
    
- 1 value → call it once
    
- 2 values → call it twice
    
- n values → call it n times  
    This generalizes “return exactly one thing.”
    

2. **What if n is potentially huge?**
    

- You don’t want to build a list of all possible results just to look at a few.
    
- CPS lets you generate results “one at a time” and possibly stop early.
    

---

#### CPS Example 1 — `forLoop`: a counting loop (CPS + tail recursion)

Goal: write a function in CPS that acts like a loop from `min` to `max`.

Professor’s naming convention:

- calls the continuation `etc` (“et cetera”)
    

**Code form shown**

let forLoop etc min max =  
  let rec looping index =  
    if index <= max  
    then (etc index; looping (index + 1))  
    else ()  
  in  
  looping min  
;;

What each part means:

- `looping` is the internal helper; it carries the changing loop variable `index`.
    
- The condition `index <= max` is the loop test.
    
- The body is `etc index`:
    
    - “this expression is executed for count = min, min+1, ..., max”
        
- The sequencing operator `;`:
    
    - `e1; e2` evaluates `e1`, discards its value, then evaluates and returns `e2`
        
    - here: run the loop body first, then do the recursive step
        

Tail recursion note:

- `looping (index + 1)` is the last thing executed in that branch → tail call → tail recursion.
    

Edge-case the professor calls out:

- If `min > max`, then `etc` never gets called.
    

Nested loops pattern (from the notes):

forLoop  
  (fun i ->  
     forLoop (fun j -> (* ... *) ()) 0 5  
  )  
  0 5  
;;

Meaning: execute the inner loop for each `i` in range.

Type note written in the margin:

- `forLoop` returns `unit` because its job is “do effects / call continuations,” not produce a list.
    
- Professor’s type sketch:
    
    - `(int -> 'a) -> int -> int -> unit`
        
    - (the `'a` result from `etc` doesn’t matter, because it’s discarded by `;`)
        

---

#### CPS Example 2 — `generateBools`: generate boolean lists of length `n`

Goal: generate all possible lists of booleans of length `n`, one at a time.

Professor’s truth-table framing:

- It “looks like part of a truth table.”
    
- There are `2^n` possible lists.
    
    - notes include scale intuition: `2^10 ≈ 1000`, `2^20 ≈ 10^6`
        

**Core idea**  
At each position, you choose:

- `false` OR `true`  
    That creates a binary tree of calls of depth `n`.
    

**Code shape shown (CPS generator)**

let generateBools etc n =  
  let rec generating bools n =  
    match n with  
    | 0 -> etc bools  
    | _ ->  
        generating (false :: bools) (n - 1);  
        generating (true  :: bools) (n - 1)  
  in  
  generating [] n  
;;

How to read the parameters (as labeled in your notes):

- `bools` = “list of bools built so far”
    
- `n` = “number of elements remaining to be generated”
    

Why it’s not “one return value” style:

- it calls `etc` potentially many times (once for each completed list)
    

The call-tree diagram in your notes (what it’s trying to teach)  
For `n = 2`, starting from `generating [] 2`:

- branch into prefix `[false]` and `[true]`
    
- each of those branches into two more choices
    
- leaves correspond to:
    
    - `[false; false]`, `[true; false]`, `[false; true]`, `[true; true]`  
        (Exact order depends on the recursion path; the professor’s point is that all are produced.)
        

Big finish sentence written by professor:

- Use CPS to generate combinatorial objects (permutations, combinations, sequences).
    
- CPS functions often don’t return interesting values; we care what the continuation gets.
    
- `generateBools` is “guts” of a tautology checker for propositions (next few lectures).
    

Links to connect:

- [[OCaml - Basics#The semicolon operator `;` (sequencing)|`;` sequencing]]
    
- [[OCaml - Basics#Tail recursion and stack frames (Jan 30 lecture)|Tail recursion]]
    
- [[OCaml - Tautology Problems|Tautology Problems]]
    
- [[OCaml - Pattern Matching#Pattern matching on lists (most common)|List patterns]]
    
- [[OCaml - Types of Programming|First-class functions + higher-order style]]
    

---

### Lecture (Feb 18) — Tautology checker (brute force): propositions, evaluation, assignments, `generatePairs`

#### What we’re building

A tautology checker that uses a brute force algorithm:

1. represent propositions
    
2. represent variable assignments
    
3. evaluate proposition under an assignment
    
4. generate all assignments (truth-table rows)
    
5. test whether evaluation is always true
    

Professor reminder: midterm is Feb 27.

---

#### Review: what is a proposition? what is a tautology?

Professor’s wording:

- A proposition is an expression built from:
    
    - variables, `T`, `F`
        
    - connectives like `¬`, `∧`, `∨`, `→`, `↔`
        
- Each variable can be either `T` or `F`.
    

A tautology:

- a proposition that evaluates to `T` for **all** assignments of its variables.
    

Truth-table scaling:

- `n` variables → `2^n` rows.
    
- So the algorithm is inherently exponential in number of variables.
    

Professor’s “suggested algorithm”:

- generate all possible T/F values for variables
    
- evaluate the proposition for each
    
- test whether they all evaluate to true
    

---

#### Step 1 — Represent propositions in OCaml (a recursive type)

Professor writes an OCaml type definition with constructors:

type proposition =  
  | False  
  | True  
  | Var of string  
  | Not of proposition  
  | And of proposition * proposition  
  | Or of proposition * proposition  
  | Imply of proposition * proposition  
  | Equiv of proposition * proposition  
;;

Notes embedded in your page:

- `False` and `True` are _constructors_ (not OCaml `false/true`).
    
- Each connective corresponds to a constructor that stores sub-propositions.
    

Example proposition in logic:

- `¬(p ∧ q) → (¬p ∨ ¬q)`  
    Example as constructors (structure matters more than exact formatting):
    

Imply (  
  Not (And (Var "p", Var "q")),  
  Or (Not (Var "p"), Not (Var "q"))  
)  
;;

---

#### Step 2 — Represent variable values (assignments)

Professor points back to the association list idea (from Feb 6):

- “association list associates strings with bools”  
    So an assignment is like:
    
- `[("p", false); ("q", true)]`  
    (Exact order doesn’t matter for the concept.)
    

---

#### Step 3 — Evaluate a proposition under an assignment (`evaluate`)

Professor draws “dispatcher” logic: pattern match on the proposition and compute.

**Code structure shown**

let evaluate proposition pairs =  
  let rec evaluating proposition =  
    match proposition with  
    | False -> false  
    | True -> true  
    | Var name -> alGet pairs name  
    | Not right -> not (evaluating right)  
    | And (left, right) ->  
        (evaluating left) && (evaluating right)  
    | Or (left, right) ->  
        (evaluating left) || (evaluating right)  
    | Imply (left, right) ->  
        (not (evaluating left)) || (evaluating right)  
    | Equiv (left, right) ->  
        (evaluating left) = (evaluating right)  
  in  
  evaluating proposition  
;;

Professor’s margin notes you should carry into your file:

- `!` does not mean “not” in OCaml.
    
- implication:
    
    - `A -> B` is represented as `¬A ∨ B`
        
- termination argument:
    
    - each recursive call evaluates a smaller proposition until it reaches a base constructor (`False`, `True`, `Var ...`)
        

Type line written:

- `proposition -> (string,bool) al -> bool`  
    Meaning:
    
- input proposition
    
- input assignment mapping
    
- output boolean result
    

Tail recursion remark:

- most calls aren’t tail calls because results have to be combined (`&&`, `||`, `=`, etc.)
    
- some subcalls may be tail in specific branches, but the overall evaluator isn’t “tail-recursive all the way.”
    

---

#### Step 4 — Generate all assignments: `generatePairs`

Professor asks: “Where do pairs come from? Use something like generateBools.”

**Idea**  
Given a list of variable names `["p"; "q"]`, we want to generate all associations of each name with false/true:

- 4 lists total for 2 vars.
    

**Code structure shown (CPS generator)**

let generatePairs etc names =  
  let rec generating names pairs =  
    match names with  
    | [] -> etc pairs  
    | name :: otherNames ->  
        generating otherNames (alPut pairs name false);  
        generating otherNames (alPut pairs name true)  
  in  
  generating names []  
;;

How to read it:

- `pairs` is the assignment built so far
    
- For each name:
    
    - branch where it’s false
        
    - branch where it’s true
        
- At the end (`[]`), call `etc pairs` with a complete assignment.
    

Professor writes the resulting four assignment lists (order doesn’t matter) for two variables.

Open questions the professor writes at the bottom:

- how to get the list of variable names from a proposition
    
- how to stop early if the proposition is false (so we don’t evaluate all rows if not needed)
    

Links to connect:

- [[OCaml - Pattern Matching#Pattern matching on user-defined constructors (BST / tautology style)|Constructor matching]]
    
- [[OCaml - Tautology Problems|Tautology Problems]]
    
- [[OCaml - Basics#Short-circuit operators `&&` and `||`|Short-circuit logic]]
    
- [[OCaml - Basics#Exceptions and `raise`|Exceptions (alGet)]]
    
- [[OCaml - Types of Programming|Brute force + recursion mindset]]
    

---

### Lecture (Feb 20) — Finish the tautology checker: `isIn`, `uniquify`, `names`, CPS `generateAndTestPairs`, `isTautology`

#### Announcements (exam prep)

- Midterm: Feb 27.
    
- Topics list posted to Canvas.
    
- No practice exam.
    

Professor’s stated plan:

- “Finish the tautology checker.”
    
- Find all variable names in a proposition:
    
    - `isIn` (membership)
        
    - `uniquify` (remove duplicates)
        
    - `names` (unique variable names in a proposition)
        
- Then build the final tester:
    
    - `generateAndTestPairs`
        
    - glue into `isTautology`
        
- He also notes “working bottom up” and mentions posting `tautology.ml` on Canvas later.
    

---

#### Helper 1 — `isIn`: membership in a list

Professor labels this as a linear search.

**Code shown**

let isIn thing things =  
  let rec isInning things =  
    match things with  
    | [] -> false  
    | firstThing :: otherThings ->  
        (firstThing = thing) || (isInning otherThings)  
  in  
  isInning things  
;;

Important note in your page:

- This is tail-recursive in the sense that the recursive call is positioned in the short-circuit “else” side of `||`.
    
- `||` behaves like:
    
    - `if (firstThing = thing) then true else isInning otherThings`
        

Type line the professor writes:

- `'a -> 'a list -> bool`
    

---

#### Helper 2 — `uniquify`: remove duplicates from a list

Purpose:

- when generating truth tables, duplicates waste time.
    
- we only want the set of variable names.
    

Accumulator design:

- `uniqueThings` holds the names we’ve kept so far
    
- order doesn’t matter (prof writes this explicitly), so consing to the front is fine.
    

**Code shown**

let uniquify things =  
  let rec uniquifying things uniqueThings =  
    match things with  
    | [] -> uniqueThings  
    | firstThing :: otherThings ->  
        if isIn firstThing uniqueThings  
        then uniquifying otherThings uniqueThings  
        else uniquifying otherThings (firstThing :: uniqueThings)  
  in  
  uniquifying things []  
;;

The professor labels this as tail recursion (the recursive call is the last step in both branches).

---

#### Helper 3 — `names`: list of unique variable names in a proposition

Professor writes: recursively traverse proposition, collect names, then uniquify.

Key point scribbled:

- this traversal is **not** tail-recursive (recursively traversing the proposition and using `@`).
    

**Code shape shown**

let names proposition =  
  let rec namesing proposition =  
    match proposition with  
    | False -> []  
    | True -> []  
    | Var name -> [name]  
    | Not right -> namesing right  
    | And (left, right) -> (namesing left) @ (namesing right)  
    | Or (left, right) -> (namesing left) @ (namesing right)  
    | Imply (left, right) -> (namesing left) @ (namesing right)  
    | Equiv (left, right) -> (namesing left) @ (namesing right)  
  in  
  uniquify (namesing proposition)  
;;

Example in notes:

- `names (And (Var "a", Var "b"))` gives `["a"; "b"]` (order may vary).
    

---

#### CPS rewrite: `generateAndTestPairs` (stop early with `&&`)

Professor rewrites the earlier “generate all assignments” idea, but now:

- instead of merely generating, we generate **and test**
    
- the test returns a boolean
    
- we combine results with `&&` so we can short-circuit early
    

Core reason:

- If any assignment makes the proposition false, the whole thing is not a tautology.
    
- `&&` stops evaluating once it sees `false`.
    

**Code shape shown**

let generateAndTestPairs etc names =  
  let rec generating names pairs =  
    match names with  
    | [] -> etc pairs  
    | name :: otherNames ->  
        (generating otherNames (alPut pairs name false))  
        && (generating otherNames (alPut pairs name true))  
  in  
  generating names []  
;;

Note on your page:

- this is “originally” similar to the earlier generator, but the `;` sequencing got replaced by boolean combination to enable early exit.
    

---

#### The big finish: `isTautology`

Professor draws it as composition:

- get unique names
    
- generate-and-test all assignments
    
- for each assignment, evaluate proposition
    
- if all evaluations are true → tautology
    

**Final wiring (as written)**

let isTautology proposition =  
  generateAndTestPairs  
    (fun pairs -> evaluate proposition pairs)  
    (names proposition)  
;;

Professor’s example:

- `p ∧ q` is not a tautology.
    

isTautology (And (Var "p", Var "q"));;  
(* => false *)

Why that example fails:

- there exists an assignment (like `p=false`) making `p ∧ q` false
    
- so the brute-force tester finds a false row, `&&` short-circuits, and returns false.
    

Links to connect:

- [[OCaml - Tautology Problems]]
    
- [[OCaml - Pattern Matching#Pattern matching on user-defined constructors (BST / tautology style)|Dispatching with match]]
    
- [[OCaml - Basics#Short-circuit operators `&&` and `||`|`&&` / `||` as control flow]]
    
- [[OCaml - Basics#Lists: `[]`, `::`, `@`|`::` vs `@` in names collection]]
    
- [[OCaml - Basics#Exceptions and `raise`|Association list lookup + errors]]
## Takeaways (questions to resolve)
- [ ] Why does ...?
- [ ] What changes if ...?
## Flashcards
#cards/
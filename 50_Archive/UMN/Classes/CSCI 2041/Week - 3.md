---
type: class
input_kind: lecture
status: sprout
created: 2026-02-25
updated:
area:
  - "[[UMN Board]]"
  - "[[CSCI 2041 Board]]"
  - "[[OCaml]]"
  - "[[OCaml - Basics]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[Week - 4"
---
# Entire Week
## What you must be able to do
- [[Textbook]]
- 
## Key ideas (textbook)
- **Patterns bind names:** in pattern matching, names in patterns bind (they don’t “compare against an existing name”).
	- See: [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4#4.1 The `match` Expression]]
- **Variables in patterns always bind** (they do not “compare to an existing name”).  
- **Let-bindings define names for values**. In `let x = e1 in e2`, `x` is available only in `e2` (the body), not in `e1`.  
	- See: [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4#4.2 Pattern Types Constants and Variables]]
- **`function` keyword** is shorthand for `fun x -> match x with ...` (single-argument match).  
	- See: [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4#4.3 Functions with Matching (`function`)]]
- **Inexhaustive matches** warn at compile time and can raise `Match_failure` at runtime.  
	- See: [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4#4.6 Exhaustiveness and Safety]]
## Concepts created today
- [[Concept - ...]]
- [[Concept - ...]]
## Examples worth keeping
- 
## Lecture
### Lecture (Feb 2) 
- Loops → tail recursion (Newton square root), evaluation order with `let`, intro: types + pattern matching
- Goal of the day (what professor is building toward)
	- **How to turn loops into tail recursions**
	- Reinforce the “no loops needed” claim by showing a realistic numeric loop example. Using square roots by Newton's method.
	- Start connecting **types** and **pattern matching** (because they show up together when you define your own data).
#### Newton’s method for square roots (the loop shape)
- Problem: compute sqrt of a non-negative real `a` using a convergence loop.
```ocaml
double sqrt(double a)
{
	double g = 1.0;
	double h = 2;
	while(abs(g-h)>=ε)  (* ε - Some small number *)
	{
		g = (g+h)/2.0;  (* new g *)
		h = 2 /. g      (* Now a float sqrt(2.0) = 1.414 *)
	}
	return g;
}
```
- Loop condition: keep iterating while `abs(g - h) >= ε`
- Updates:
	- new guess: `g = (g + h) / 2.0`
	- new helper: `h = a / g`
- Return final `g`
> [!NOTE] This is the *exact* shape you should recognize on exams: loop variables + test + updates + return.
#### Translation principles (professor’s rules list for loop → tail recursion)
- **Loops turn into tail recursions** (often with internal helpers).
- **Loop variables → function parameters** (each iteration = one recursive call).
- **Tests in loops → tests in `if`** expressions.
- **Assignments → function arguments** in the next recursive call (no mutation).
- **Initializations → arguments in the initial recursive call**.
- **Don’t compute the same thing twice** (watch expressions you repeat).
- **Consider the order of assignments** in imperative code:
	- If a later assignment depends on an earlier updated value, your functional translation must preserve that order.
- **Use `let` when order of evaluation matters** (force “compute this first, name it, then use it”).
#### Applicative OCaml version: tail-recursive square root helper
- Setup:
	- `let epsilon = 0.00001;;` (some small number)
	- `let sqrt a = ...`
- Internal helper (tail-recursive):
	- `let rec sqrting g h = ...`
	- Base/stop:
	    - if `abs_float (g -. h) >= epsilon` then return `g`
	- Step:
	    - compute new arguments and tail-call `sqrting new_g(g') new_h(h') `
> The “deliberate mistake” (why the professor added this)
- The professor explicitly says they put a mistake in the first OCaml translation.
- What you’re supposed to learn from it:
	- even in functional code, **evaluation order** can matter if you reuse old vs new values.
	- if you write the update expressions carelessly, you can accidentally:
		- use `g` where you meant the updated `g'`
		- or recompute with mixed “old”/“new” values.
#### Revised version (the fix using `let` + apostrophes)
```ocaml
let sqrt a = 
	if abs_float(g-h)>=epsilon
	then let g' = (g+.h) /. 2.0
		in let h' = 2 /. g'
			in sqrting g' h'
	else g
in sqrting 1.0 a;;
```
- Use temporary names (with apostrophes allowed in identifiers):
	- `g'` and `h'`
- Force order like the imperative loop:
	- compute `g'` first from old `g` and `h`
	- then compute `h'` using `a` and **the correct g** (as intended)
- Tail call with `sqrting g' h'`
- Notes in margins:
	- “don’t need this let” (professor points out some `let`s are optional if the expression is already safe, but keep them if they clarify order)
	- emphasize: this is still tail recursion
#### Types + pattern matching preview (end of lecture)
- “Pattern matching & types” section begins:
	- you’re going to define your own types soon, *linked chain of objects*.
	- pattern matching is the tool for extracting pieces safely
- *Type names* begin with lower case letters.
- *Constructor* - Empty, NotEmpty, etc. begin with upper case letters. All constructors have different names
```ocaml
type intyChain = 
	Empty |        (* | -> means on *)
	NotEmpty of int 8 intyChain ;;   (* intyChain -> pointer, the entire thing type of z-tuple *)
```
*Union type*: 
- *Non discriminated unions* - you don't know which member of the union you get.
- **Discriminated union-constructors** tell which member.
Links to connect:
- [[OCaml - Basics#Tail recursion and stack frames (Jan 30 lecture)|Tail recursion basics]]
- [[OCaml - Basics#Core OCaml keywords you must recognize|`let`, `let rec`, `let ... in`]]
- [[OCaml - Basics#Primitive data types (with interlinks)|float ops `-.` `/.` and `abs_float`]]
- [[OCaml - Pattern Matching|Pattern Matching]]
### Lecture (Feb 4) 
- Names vs variables, discriminated unions (“chains”), constructors, tail-recursive `length`/`sum`, parameterized types, generic membership (`isIn`)
#### Big framing: “variables” vs “names” (professor’s terminology correction)
- OCaml “distinguishes names from variables (correctly).”
- In many languages (C-like), a *variable* is something you can change by assignment: `int k = 1; k = k + 1;`
	- In OCaml: `let k = 1;;` creates a **name binding**
	- you cannot later assign to `k` (so it isn’t a “variable” in the imperative sense)
- Professor note: “*Hickey’s book confuses names with variables.*”
- OCaml variables (true mutable cells) are created with `ref` (prof says this exists, but course default avoids it early).
> [!NOTE] Exam-safe sentence: “`let` binds a name; it does not create a mutable variable.”
#### Defining your own types: “linked chain of objects” (the custom list-like type)
- Motivation: we want a structure like an OCaml list, but defined by us.
- Type names begin with **lowercase** letters.
- Constructors begin with **uppercase** letters.
- Example type (int chain):
	- `type intyChain = Empty | NotEmpty of int * intyChain;;`
- Notes:
	- “All constructors must have distinct names.”
	- This is a **union type** (sum type).
1. *Building instances with constructors (concrete example)*
	- Build a chain using nested constructors: 
		- `let chain123 = NotEmpty (1, NotEmpty (2, NotEmpty (3, Empty)));;`
	- “We can instance types by using their constructors.”
#### How to get pieces out: pattern matching (match expression form)
- General shape written on board: `match e with p1 -> e1 | p2 -> e2 | ... | pn -> en`
- Notes labeled:
	- `e` is an expression
	- `p` is a pattern
	- right side is the expression to run if it matches
- Patterns use constructors:
	- `Empty` pattern for empty chain
	- `NotEmpty (first, rest)` to extract head and rest
#### Tail recursion using pattern matching: `length` for chains
```ocaml
let length q = 
	let rec lengthing p n =   (* p = remaining chain, n = count nodes *)
		match p
		with Empty -> n |
			NonEmpty (_, p') -> lengthing p'(n+1)  (* Tail Recursion, _ = dont care *)
	in lengthing q 0;;     (* Tail call *)
```
- Goal: count nodes
- Internal helper pattern (prof’s style):
	- one parameter for “remaining chain”
	- one accumulator for “count so far”
> [!NOTE] tail call + tail recursion → constant stack space
2. Tail recursion using pattern matching: `sum` for int chains
	- Goal: sum all integers in the chain
	- Similar helper pattern:
		- remaining chain
		- accumulator `s` (sum so far)
	- `Empty -> s`
	- `NotEmpty (i, p') -> summing p' (s + i)`
#### [[OCaml - Types of Programming#“Mix-match logic” (how the course expects you to use both styles)|Pattern matching rules emphasized again]]
- In match-with expression, Rules($P \to E$) are tried in order of appearance
- First rule whose pattern matches is used
- You can have as many rules as you want
- Match-with rules should cover all possibilities
	- if you omit a needed case, compiler complains (warning/error framing)
#### Parameterized types: making chains general (`'base chain`)
- Define a type parameter:
	- leading `'` indicates a **type parameter**
	- “kind of like a function that makes types”
- Example structure: `type 'base chain = EmptyChain | NotEmptyChain of 'base * 'base chain;;`
	- Parameters that can be any type.
- Instantiations:
  - `string chain` (substitute `'base` with `string`)
  - `int chain`
#### [[Chapter - 9 & 10#9.4 Code Example `alget` with Custom Exception|Generic membership function]] `isIn`
```ocaml
let isin element elements = (* element = base, elements = base chain *)
	let rec isinning elements =     (* elements = remaining part of the chain *)
		match elements with EmptyChain -> False |   (* | -> OR *)
			NotEmptyChain(otherElement, otherElements) -> 
				if element = otherElement
				then true
				else ininning otherElements (* Tail recursion *)
	in is inning elements ;; (* tail call *)
```
- Goal: check whether an element is in a chain
- Type shown in notes: `'a -> 'a chain -> bool`, returns true or false.
- `element = other Element` || `isinning otherElements` this is still a tail recursion
	- a || b = if a then true else b
	- a && b = if a then b else false
	- b could be a tail call - leading to tail recursion
- Behavior examples:
	- `isIn 3 ic` → false
	- `isIn "two" sc` → true
	- `isIn 3 sc` → type mismatch error (good: OCaml catches it)
- Implementation idea:
	- internal helper inherits the element being searched for
	- recursion walks down the chain
	- uses = to compare elements
	- uses `||` to short-circuit where applicable
Links to connect:
- [[OCaml - Basics#Strong typing + type inference (the exam framing)|Type inference + mismatch]]
- [[OCaml - Pattern Matching#Pattern matching on user-defined constructors (BST / tautology style)|Constructor matching]]
- [[OCaml - Basics#Tail recursion and stack frames (Jan 30 lecture)|Tail recursion]]
- [[OCaml - Let bindings, Scope & Closures|Let bindings + binding vs rebinding]]
### Lecture (Feb 6) 
- Short-circuit `&&`/`||` for tail recursion, patterns in params + `let`, unit for “no-arg”, association lists + exceptions, BST lab preview
#### Short-circuit operators and tail recursion
- `&&` and `||` act like in other languages:
	- they do not necessarily evaluate both operands (“short circuit”)
- Equivalences written:
	- `a && b` ≡ `if a then b else false`
	- `a || b` ≡ `if a then true else b`
- Why this matters for tail recursion detection:
	- if `b` contains a *function call*, that call can be a *tail call* depending on context
	- you need to know what executes last to decide tail position
#### Pattern matching is “(almost) everywhere” (not just match-with)
- In function parameter listed in let:
	- tuples can be de-structured directly
	- professor notes `fst` and `snd` can be defined via parameter patterns
- In `let` bindings:
	- if `f` returns a pair, you can bind both pieces at once: defined by pattern matching parameter lists
		- `let (a, b) = f ...;;`
1. *Constant patterns as “restricted functions” (odd but legal)*
	- Example shown: `let g 5 = "five";;`
	- Meaning: this defines a function that can be called only with the pattern `5`
		- `g 5` works
		- `g 1` fails because the pattern doesn’t match
> [!NOTE] This is a pattern-matching-in-parameters demo, not a recommended everyday style.
#### Unit `()` to simulate “no arguments”
- `()` is the single value of type `unit`
- Use `()` in parameter list to make a function callable “with no meaningful argument”:
	- `let outer () = ...`
- “Can be called only with `()`”
> *Example from lab 2*: `let euter () = ... ;;`, this function can only be called with (), unit object
1. *List de-structuring in parameter patterns (clean head/tail)*
	- Head: `let hd a :: _ = a;;`
	- Tail: `let tl _ :: b = b;;`
	- Professor note: “Better to use `_`” than inventing a name you don’t use.
#### Association lists (maps) - concept + type
- An association list *maps keys → values*.
- Comparison examples from lecture:
	- *arrays map integer indices to values*
	- Python dictionaries map arbitrary keys to values (implementation idea like *hash tables*)
- Association list is OK for small sizes (prof mentions ~10-ish as “fine”)
- Lookup is linear search:
	- **O(n) time**
	- returns value if found
	- otherwise raises an exception(*error*)
- Type definition written: `type ('key, 'value) al = ('key * 'value) list;;`
- Professor comment:
	- tuple type written as `('key * 'value)` -> ordered pair. `list` -> type of association list.
	- list type uses one parameter; association list uses two because a pair has two types
#### `alGet` (lookup) with a custom exception
```ocaml
exception AlError of string;; (* A -> Uppercase *)
let alGet pairs key = 
	let rec alGetting pairs = 
		match pairs
		with [] -> raise(AlError "No such key") |
			(otherKey, otherValue)::otherPairs ->
				if key = otherKey
				then otherValue
				else alGetting otherPairs   (* tail recursion *)
	in alGetting pairs;;
```
- Define an exception (*uppercase constructor*): `exception AlError of string;;`
- Type shown in notes: `('a * 'b)al -> 'a -> 'b`
	- `('a * 'b)al` are pairs, `'a` is the key and `'b` is the returned value
- Structure of `alGet`:
	- recursive helper `alGetting pairs`
	- *Tail recursion note*: the recursive call is in tail position in the “else” branch.
1. *`alPut` (insert) and persistence + duplicates*
	- `alPut key value pairs = (key, value) :: pairs;;`
	- Type: `'a -> 'b -> ('a*'b)al -> ('a*'b)al`
		- `'a` is the key, `'b` is the value `('a * 'b)al` are pairs and `('a * 'b)al` is the returned value
	- O(1) time (cons at front)
	- Does not change original list (persistence)
	- Duplicates may exist:
		- professor says it’s fine because `alGet` returns the first matching key
		- works as long as you don’t accumulate too many duplicates
#### BST lab preview (Lab 3)
- Topics listed:
  - BST type
  - membership: `bstIsIn`
  - and a note about `::` vs `?` (prof emphasizes the `::` constructor again)
- This lecture connects BST work to:
  - pattern matching
  - recursion / tail recursion
  - type definitions with constructors
Links to connect:
- [[OCaml - Basics#Operators you must not confuse|`&&` / `||` short-circuit]]
- [[OCaml - Pattern Matching#Patterns are everywhere (Ch4.5)|Patterns in params + let]]
- [[OCaml - Basics#Primitive data types (with interlinks)|`unit`]]
- [[OCaml - BST Problems|BST Problems]]
- [[OCaml - Tautology Problems|Tautology Problems]] (association lists + later evaluator code)
## Midterm Check
### Chapter - 4
- [ ] **What happens if you provide a variable name in a pattern that is already used in a** **let** **binding at the top level?** (e.g., `let x = 5 in match y with x -> ...`).
- [ ] **Explain the difference between** **match expr with ...** **and using the** **function** **keyword.** When is the latter preferred?.
- [ ] **Why does the OCaml compiler give a warning for "Inexhaustive Pattern Matching," and what happens at runtime if that warning is ignored and an unmatched value is passed?**.
### Chapter 5
- [ ] **Tail Recursion Identification:** Is the standard `List.map` function (as defined in Section 5.3) tail-recursive? Why or why not?.
- [ ] **The Value Restriction:** Why does OCaml assign the type `'_a` to a reference cell created at the top level instead of a fully polymorphic `'a`?.
- [ ] **Tuple vs List Types:** What is the difference between the type `int * int` and the type `int list`? Which one can hold an infinite sequence of integers (conceptually)?.
### Chapter 9
- [ ] **Style Difference:** Why is it considered "bad practice" to catch an `Invalid_argument` exception, but "routine" to catch a `Failure` or `Not_found` exception?.
- [ ] **The** **exn** **Type:** What makes the `exn` type different from a standard union type like `bool` or `list`?.
- [ ] **The Stack:** When a `Match_failure` occurs deep within a series of recursive calls, how does OCaml find the correct `try...with` block to execute?.
## Flashcards
#cards/
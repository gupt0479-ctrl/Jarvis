---
type: class
input_kind: lecture
status: tree
created: 2026-01-21
updated: 2026-02-25
area:
  - "[[CSCI 2041 Board]]"
  - "[[UMN Board]]"
  - "[[OCaml - Basics]]"
  - "[[OCaml - Types of Programming]]"
  - "[[OCaml - BST Problems]]"
  - "[[OCaml]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[Midterm]]"
---
# Entire Week
## What you must be able to do
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2|Chapter - 1 & 2]]  
- [[OCaml - Types of Programming|OCaml - Types of Programming]]  
- [[OCaml - Basics|OCaml - Basics]]
- Be able to explain (and recognize) **imperative vs applicative** using the factorial example (state variables vs parameters).  
- Use the toploop confidently: prompt `#`, end input with `;;`, read the `val ... : type = ...` line, exit with Control-D.  
- Read and write simple function types: `int -> int`, and multi-argument types like `t1 -> t2 -> t3` (curried model).  
- Work with lists: `[]`, `[e1; ...; en]`, `hd`, `tl`, `::`, and explain why these are persistent (inputs don’t change).  
- Write correct recursion structure: *base case + recursive case*; argument gets closer to base case.  
- Explain partial application: giving fewer arguments returns a function waiting for the rest.  
- Explain when to use an internal helper (inherit an unchanged parameter via `let ... in`).
## Key ideas (textbook)  
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#1.2 Functional vs. Imperative Programming|Ch1.2 Functional vs. Imperative]]: functional progress via expression evaluation (often recursion); imperative progress via state changes.  
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#2.1 Comment Convention and Interaction|Ch2.1 Toploop + comments]]: `;;` ends toploop input; OCaml prints both type and value. 
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#2.2 Primitive Data Types|Ch2.2 Primitive types]]: everything has a type; no implicit numeric coercions.  
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#2.3 Relations and Conditionals|Ch2.3 Conditionals]]: both branches must have the same type; missing `else` behaves like `else ()`.  
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#1.1 Core Principles of OCaml|Ch1.1 Persistence]]: operations return new structures; originals remain usable.
## Examples worth keeping
- Toploop transcript: `# 2 + 2;;` → `- : int = 4` and `# let n = 4;;` → `val n : int = 4`.  
- Factorial translation (imperative loop vs recursive helper with accumulator parameters).  
- `length` recursion on lists: base `[] -> 0`, step `s -> 1 + length (tl s)` and inferred type `’a list -> int`.  
- `::` persistence example: `0 :: x` returns a new list; `x` is unchanged.  
- Append + partial application: `let f = append [1;2]` then `f [3;4]`.  
- Internal helper example: use `let rec helper ... in helper ...` to inherit an unchanged argument.
## Lecture
### Textbook tie-ins for this week  
- Talking to OCaml/toploop: [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#2.1 Comment Convention and Interaction|Ch2.1]]  
- Types + “everything has a type”: [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#2.2 Primitive Data Types|Ch2.2]]  
- Applicative vs imperative + persistence: [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#1.2 Functional vs. Imperative Programming|Ch1.2]]  
- Conditionals (`if ... then ... else ...`): [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#2.3 Relations and Conditionals|Ch2.3]]
### Lecture (Jan 21) - Introduction to OCaml
**How to talk to OCaml (toploop workflow)**: via Command line interface(`shell`)
- Start from a shell: run `ocaml`, get a _herald message_, then the `#` prompt.
- In the toploop, end an input with `;;` (signals “end of input”).
- OCaml replies in the form:
    - `- : <type> = <value>` when you didn’t name it
    - `val <name> : <type> = <value>` when you _did_ name it with `let`
- Exit with **Control-D** (Unix-like systems).
*Applicative vs Imperative Language*: 2 different styles of coding  
	1. *Imperative*: Issues commands to change variables  
	2. *Applicative*: Computing values by calling functions  
**Imperative**
```c  
int fac(int n)  
{  
	int f = l;  
	int t = n;  
	while (t>0){  
		f = f*t;  
		t = t - 1;  
	}  
	return f;  
}
```
explicitly state types. variables: f, t and n
`int f = 1;
`int t = n;`
states, to change them:
`t = t - 1;`  
`f = f*t;`
- imperative language: more about _commands_ than expressions. It doesn't compute values it changes values.
- the imperative language will do operations sequentially. *(1 at a time)*
- *return statement*.
- types must be *explicit*
- *statement language*
    - ==statements vs expressions==
**Applicative**
```ocaml
let fac n =  
	let rec facing f t =  
		if t>0  
		then facing (f+t) (t-1)  
		else f;;  
	in facing 1 n;;
```
- expression language (==no return== statement)
- *implicit types*
- loops become *recursions*
- not sequential
- *no variables* assignment
- *function calls don’t use ();*
- imperative variables turn into parameters
- not sequential
### Lecture (Jan 26) - Talking to OCaml, function types, lists, recursion basics
**“Everything has a type” (what the reply line is telling you)**
- The `:` introduces the **type** OCaml inferred.
- The = introduces the **value** produced.
**Defining functions (factorial example + why `rec` matters)**
- `let rec fact n = ...` means the function may call itself. 
	- `rec` means *recursive*.
	- `n` is the parameter.
	- `fact` is the name of the function.
- If you omit `rec`, OCaml looks for an _older_ definition of `fact` instead (so self-calls won’t work as intended).
- *Functions print as* `<fun>` because code doesn’t have a simple printed representation.
**Function types and the arrow**: OCaml thinks that all functions take *one argument* and return *one value*.
- `int -> int` means: The first int is the *argument*: input type is `int`, second int is the *value returned*, output type is `int`. 
- The arrow is literally `-` then `>` (and yes, professor notes OCaml loves punctuation).
**Lists (syntax + rules)**
- Lists are written as `[e1; e2; ...; en]` and the empty list is `[]`.
- ==A list is an ordered finite sequence of elements **all the same type**.==
- `hd` returns the first element of a non-empty list; `hd []` is an error. 
	- Example: hd $[e_o;e_{1};\dots;e_{n-1}]$
- `tl` returns everything except the first element (professor’s “snake” metaphor: head vs tail).
	- Example: tl $[e_o;e_{1};\dots;e_{n-1}]$ = $[e_1;e_{2};\dots;e_{n-1}]$
**How the professor wants you to think about recursion**
- Recursions have:
    - **Base case(s)**: compute result with essentially no work (often constant time)
    - **Recursive case(s)**: do some work + call the function on an argument “closer” to the base case
    - This “closer” idea is what ensures termination.
**Example: length of a list**
- Base: length `[]` is `0`
- Step: length `s` is `1 + length (tl s)`
- The type comes back as `’a list -> int`:
    - `’a` is a **type placeholder** meaning “any type”, so `length` works on lists of anything.        
**Cons `::` and persistence**
- `e0 :: x` returns a **new** list with `e0` as first element and `x` as the rest. 
- It **does not change** `x`. This is the big “persistence” point: the original structure is still usable.
- `::` is not a general “combine two lists” operation; it adds one element to the front.
### Lecture (Jan 28) - Multi-argument function types, append, immutability/persistence, helpers
**Multi-argument functions are “multiple arrows”**
- A 2-argument function type looks like: `t1 -> t2 -> t3`
    - argument types: `t1`, `t2`
    - return type: `t3`
**What’s _really_ happening (curried model)**
- A function of type `t1 -> t2 -> t3`:
    - takes `t1`
    - returns a function `t2 -> t3`
- So “a function with more than one argument” is a function that returns another function.
**First-class objects (professor’s rights list)**  
In this class’s language(*Applicative*), an object is “first-class” if you can: Functions in OCaml have these rights (so: functions are first-class)
- pass it as an argument
- return it from a function
- assign/bind it to a name
- store it in a data structure
	*Imperative* languages try to hide these rights.
**Mutability vs immutability**
- Mutable: can be changed (imperative variable vibe)
- Immutable: cannot be changed
- Lists in OCaml are treated as immutable in your course framing.
**What “persistent” means in _this class_**
- Not “survives power-off” (file system meaning) — professor explicitly rejects that.
- Here: when you operate on structures like lists, the originals **remain unchanged**(*persist*) after the operation.
**Append (concatenate) two lists**
- The professor starts by writing algebra-like behavior rules:
    - `[] append R = R`
    - `L append [] = L`
    - non-empty cases preserve order
- Key reasoning constraint: since lists are immutable, append must **copy at least part** of a list (usually the left list), returning a new list, while original inputs persist unchanged.
- Type of append is inferred as: `’a list -> ’a list -> ’a list` (both inputs must have the same element type).
**Partial application (waiting for the rest)**
- If a function “takes 2 args” and you give it 1, you get back a function waiting for the remaining arg. (Professor flags this is useful but can cause errors.)
**Helper functions**
- Observation: in the basic append recursion, `R` never changes → you’re “passing it around for no reason.”
- **Internal helper**: define a helper _inside_ the main function so it can “inherit” the unchanging argument from scope (don’t pass it explicitly).
- **External helper**: helper is defined outside the main function (professor notes he used this pattern earlier with factorial).
- Professor’s rule of thumb:
    - use an internal helper when 1+ parameters never change; inherit them instead.
**`let ... in ...` meaning (scoping rule)**
- `let n = e1 in e2` means: _inside `e2`_, `n` has value `e1`.
- The `in` pairs with that `let` and can’t stand alone.
## Midterm Check
### Chapter 1
- [ ] **Explain the concept of "Persistence"** in the context of OCaml data structures. Why is it useful for reasoning about programs?
- [ ] In the transition from **imperative to functional form**, what usually happens to "looped variables" and "assignments"?
- [ ] OCaml functions are called **"First-class values."** List three things you can do with a first-class value that you cannot do with a second-class value.
### Chapter 2
- [ ] **True or False:** In OCaml, the expression `1 + 2.0` is valid because the compiler automatically converts the integer to a float. (Explain why based on Section 2.2.3).
- [ ] **Short-Circuiting:** Given the expression `1 < 2 || (1 / 0) > 0`, will OCaml raise a `Division_by_zero` exception? Why or why not?
- [ ] **Physical vs. Structural Equality:** What is the difference between `x = y` and `x == y`? Which one is generally faster, and which one checks for "identical" values in memory?
## Flashcards
#cards/CSCI2041 

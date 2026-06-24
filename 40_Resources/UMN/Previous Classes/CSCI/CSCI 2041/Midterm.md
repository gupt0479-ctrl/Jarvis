---
type: class
input_kind: exam
status: seed
created:
updated:
area:
  - "[[UMN Board]]"
  - "[[CSCI 2041 Board]]"
tags:
  - "#class"
  - "#Lecture"
next: "[[OCaml]]"
---
# CSCI 2041 Midterm Print Notes (OCaml)  
> [!NOTE]  Goal: one paper resource that you can use to answer midterm-style questions fast.  
>-  Focus: definitions + “how to do it” + small code patterns.  
## Functional (Applicative) Programming vs Imperative Programming 
### What functional/applicative programming is  
- Programming by **evaluating expressions** (not executing commands).  
- You “compute results” mainly by:  
	- calling functions  
	- combining returned values  
- Core habits:  
	- prefer **immutability** (no changing variables)  
	- prefer **recursion** over loops  
	- functions are **first-class** (can be passed/returned/stored)  
### What imperative programming is  
- Programming by **executing statements** that change program state.  
- Core habits:  
	- **mutable variables** updated by assignment  
	- loops (`while`, `for`) + sequence of commands  
	- explicit “do this then that” control flow  
### Mix-match logic (how the prof frames it)  
When you translate between styles, the mapping is usually:  
- loop variables → function parameters  
- assignments → passing updated values as arguments  
- loop condition → `if ... then ... else ...`  
- “loop body” → recursive step  
- initialization before the loop → initial call arguments   
## Translating Imperative ↔ Functional  
### Imperative → functional (typical pattern)  
Imperative:  
```c  
int sumToN(int n){  
  int s = 0;  
  while(n > 0){  
    s = s + n;  
    n = n - 1;  
  }  
  return s;  
}

Functional (tail-recursive):

let sumToN n =  
  let rec looping n s =  
    if n > 0 then looping (n - 1) (s + n)  
    else s  
  in  
  looping n 0  
;;
```
**Checklist to do the conversion correctly**
- Identify variables that change (`n`, `s`) → parameters in helper
- Identify termination condition (`n > 0`) → `if`
- Replace assignment updates with new arguments in recursive call
### Functional → imperative (typical pattern)
Functional recursion:
```ocaml
let rec length xs =  
  match xs with  
  | [] -> 0  
  | _ :: t -> 1 + length t  
;;
```
Imperative conceptually:
- Use a counter + pointer/index
- Update in a loop until empty
Pseudo-C idea:
```ocaml
int length(list xs){  
  int count = 0;  
  while(xs not empty){  
    count++;  
    xs = tail(xs);  
  }  
  return count;  
}
```
## Persistence (Immutable Data Structures)
### What persistence means (in this class)
A structure is **persistent** if:
- operations return a _new_ structure
- the old version still exists and can still be used
Key idea from lecture
- “copy as little as possible”
    - only copy the path you change
    - reuse everything else (structural sharing)
Example: list cons
```ocaml
let x = [2;3];;  
let y = 1 :: x;;  
(* x is still [2;3], y is [1;2;3] *)
```
Example: BST insert (copies only the search path)
- New nodes are created only along the path where insertion happens.
- Unchanged subtrees are reused.
## Applying OCaml Functions + Currying + Partial Application
### How to apply functions
- Function application is **juxtaposition**: `f x` (no commas).
- Application has high precedence:
    - `increment 2 * 3` means `(increment 2) * 3`
- Parentheses control grouping, especially with higher-order code.
### Curried functions (the “one argument” model)
OCaml treats multi-argument functions as nested single-argument functions.
```ocaml
let sum i j = i + j;;  
(* type: int -> int -> int *)
```
Interpretation:
- `sum` takes an `int` and returns a function `int -> int`.
### Partial application
If `sum : int -> int -> int`, then:
```ocaml
let incr = sum 1;;  
(* incr : int -> int *)
```
Common midterm question:
- If you apply only the first argument, what’s the result type?
    - `int -> int -> int` applied to `int` becomes `int -> int`.
## Recursion and Tail Recursion
### How to write recursion
A recursive function needs:
- 1+ base cases (no recursive call) 
- recursive step(s) that move toward a base case
Example: factorial (not tail-recursive)
```ocaml
let rec fac n =  
  if n = 0 then 1  
  else n * fac (n - 1)  
;;
```
### Tail recursion (definition used in lecture)
- A call is a **tail call** if it happens as the _chronologically last thing_ the function does.
- A function is **tail-recursive** if **all** its recursive calls are tail calls.
Tail-recursive factorial using an accumulator:
```ocaml
let fac n =  
  let rec facing f n =  
    if n = 0 then f  
    else facing (n * f) (n - 1)  
  in  
  facing 1 n  
;;
```
### How to tell if something is tail-recursive
Look at each recursive call:
- If the function does _anything_ after the call returns (like `1 + recCall` or `recCall @ ...`), it is **not** a tail call.
Examples:
- Tail:
    - `looping (n-1) (s+n)` (last action)
- Not tail:
    - `1 + length t`
    - `(func head) :: (mapping tail)`
    - `func head (reducing tail)` (must wait for result)
### Converting to tail-recursive form
Common technique: add an accumulator.
- If your recursion “builds” something after recursion returns, you often:
    - accumulate in parameters
    - reverse at end (common with lists)
Example: tail-recursive length
```ocaml
let length xs =  
  let rec lengthing xs n =  
    match xs with  
    | [] -> n  
    | _ :: t -> lengthing t (n + 1)  
  in  
  lengthing xs 0  
;;
```
## Helper Functions: Internal vs External
### Helper functions
A helper function:
- supports the main function
- often carries extra parameters (accumulators, constants, bounds)
### Internal helper (local function)
Defined inside with `let ... in ...`:
```ocaml
let length xs =  
  let rec lengthing xs n =  
    match xs with  
    | [] -> n  
    | _ :: t -> lengthing t (n + 1)  
  in  
  lengthing xs 0  
;;
```
Why internal:
- hides the helper from the outside
- lets helper “inherit” values that never change (captured in scope)
### External helper
Defined at top level or outside the main function.  
Useful when:
- reused across multiple functions
- you want to test it independently
## `let`, `let rec`, `let ... in`, `let rec ... in`
### `let name = expr`
Creates a **binding** (name → value).
- In this course: a “name” is not a mutable variable.
- Shadowing is allowed: a newer `let` can hide an older one.
### `let rec f x = ...`
Allows `f` to call itself.  
If you forget `rec`, self-calls won’t refer to the function.
### `let x = e1 in e2`
Local binding: `x` exists only inside `e2`.
### `let rec f x = ... in e`
Defines a local recursive function usable only in `e`.
## `if ... then ... else ...`
- It is an **expression**: it returns a value.
- Both branches must produce values of the same type.
Example:
```ocaml
let absInt x =  
  if x < 0 then -x else x  
;;
```
## Pattern Matching (`match ... with`) and `p -> e` Rules
### `match expr with | p1 -> e1 | p2 -> e2 ...`
- Evaluate `expr` once.
- Try patterns in order.
- First matching pattern’s expression is the result.
### `p -> e` rule meaning
- If pattern `p` matches, it may **bind variables**.
- Then `e` runs with those bindings in scope.
### Variable-binding warning
In patterns, a bare name is a **new binding**, not a lookup.  
So if you write: `match y with | x -> ...` that pattern matches _anything_ and binds `x` to it.
### Patterns are everywhere
- `match`
- function parameters (patterns in arguments)
- `let` destructuring
- tuple/list constructors
## Numbers and Operators
### Integer arithmetic operators
- `+ - * / mod` for ints
- `/` is integer division when both operands are ints
### Float arithmetic operators
- `+. -. *. /.` for floats
- Use float functions like `abs_float`
### Comparison / equality operators
- = structural equality (compares contents)
- == physical equality (same object / same address)
- `<>` not equal (structural)
- `!=` physical not equal (negation of ==)
- `< > <= >=` comparisons
Midterm habit:
- prefer = for “same value”
- use == only when you truly want identity
## Lists
### List syntax and type
- `[e1; e2; ...; en]` has type `t list` if all elements are type `t`.
### `hd` and `tl`
- `hd [h; ...]` is `h`
- `tl [h; t...]` is the rest
- `hd []` and `tl []` are errors (avoid in robust code)
### `::` (cons)
- `x :: xs` creates a new list with head `x` and tail `xs`
- runs in O(1)
- does not modify `xs`
### `@` (append)
- `xs @ ys` concatenates lists
- copies the left list spine (cost proportional to length of `xs`)
- common in name-collection code, but can break tail recursion
## Primitive Types: `bool`, `char`, `float`, `int`, `string`, `unit`
- `bool`: `true`, `false`
- `char`: `'a'`
- `string`: `"hi"`
- `unit`: `()`
    - used when you “return nothing interesting”
    - also used to simulate “no-argument” functions: `let f () = 42;;`
## Tuples and `fst`, `snd`
### Tuples
- `(e1, e2, ..., en)` has type `t1 * t2 * ... * tn`
- Used to group fixed-size mixed-type values
### `fst`, `snd`
- `fst (a, b) = a`
- `snd (a, b) = b`
Pattern matching version:
```ocaml
let fst (a, _) = a;;  
let snd (_, b) = b;;
```
## Function Types (`->`) and Type Variables (`'x`)
### Function types
- `t1 -> t2` means: takes `t1`, returns `t2`
- Arrow associates to the right:
    - `int -> int -> int` means `int -> (int -> int)`
### Type variables
- `'a`, `'b`, etc. mean “some type, consistent within the scope”  
    Example:
```ocaml
let id x = x;;  
(* 'a -> 'a *)
```
## Defining New Types with `type`
### Basic algebraic data type
`type color = Red | Green | Blue;;`
### Recursive types
Lists are recursive under the hood; you can define your own:
```ocaml
type intChain =  
  | Empty  
  | NotEmpty of int * intChain  
;;
```
### Parameterized types (type parameters)
BST from lecture:
```ocaml
type 'key bst =  
  | BstEmpty  
  | BstNode of 'key * 'key bst * 'key bst  
;;
```
### Multiple type parameters
Association list type alias: `type ('key, 'value) al = ('key * 'value) list;;`
### Type constructors (constructors vs type names)
- Type names: lowercase (e.g., `proposition`, `bst`)
- Constructors: uppercase (e.g., `BstEmpty`, `Var`, `And`)
## Exceptions: `exception` and `raise`
### Defining a new exception
`exception AlError of string;;`
### Raising an exception
`raise (AlError "No such key");;`
Typical use: signal impossible / error cases cleanly.
## Anonymous Functions: `fun p1 p2 ... -> e`
### How they work
- Create a function value without naming it.
- Parameters can be patterns.
Example:`(fun number -> number + 1)`
Use case from lecture: `map (fun number -> number + 1) [2;3;5;1];;`
## Higher-Order Functions (functions taking functions)
### `map`
```ocaml
let map func objects =  
  let rec mapping objects =  
    match objects with  
    | [] -> []  
    | head :: tail -> (func head) :: (mapping tail)  
  in  
  mapping objects  
;;  
(* ('a -> 'b) -> 'a list -> 'b list *)
```
Not tail-recursive because of `::` after recursion.
### `filter`
```ocaml
let filter pred objects =  
  let rec filtering objects =  
    match objects with  
    | [] -> []  
    | head :: tail ->  
        if pred head  
        then head :: (filtering tail)  
        else filtering tail  
  in  
  filtering objects  
;;  
(* ('a -> bool) -> 'a list -> 'a list *)
```
Contains both tail and non-tail branches.
### Reduce: right vs left association
Right-reduce style:
- `f 1 (f 2 (f 3 default))`
Left-reduce style:
- `f (f (f default 1) 2) 3`
## Association Lists (`alGet`, `alPut`)
### What an association list is
- A list of pairs `(key, value)`
- Used to map keys → values (like a small dictionary)
- Lookup is linear time in list length
Type: `type ('key, 'value) al = ('key * 'value) list;;`
### `alPut` (persistent insert at front)
- Adds a new pair at the front.
- Creates duplicates; lookup returns the first match.
```ocaml
let alPut key value pairs =  
  (key, value) :: pairs  
;;
```
### `alGet` (linear search, raises if missing)
Sketch consistent with lecture style:
```ocaml
exception AlError of string;;  
  
let alGet pairs key =  
  let rec alGetting pairs =  
    match pairs with  
    | [] -> raise (AlError "No such key")  
    | (otherKey, otherValue) :: otherPairs ->  
        if key = otherKey then otherValue  
        else alGetting otherPairs  
  in  
  alGetting pairs  
;;
```
## Representing Propositions in OCaml + Tautology Checker
### Proposition type (from lecture)
```ocaml
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
```
### Dispatcher idea
A “dispatcher” is pattern matching used to select behavior based on constructor:
```ocaml
match proposition with  
| False -> ...  
| True -> ...  
| Var name -> ...  
| Not p -> ...  
| And (p1, p2) -> ...  
...
```
### `evaluate` (core evaluator)
```ocaml
let evaluate proposition pairs =  
  let rec evaluating proposition =  
    match proposition with  
    | False -> false  
    | True  -> true  
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
```
### What a generator is (in this course)
A generator is a function that can produce many values, often using a continuation:
- instead of returning a list of all results,
- it calls a continuation for each result (or stops early)
### CPS `generateBools` (boolean lists of length n)
```ocaml
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
```
### `generatePairs` (assignments for variable names)
```ocaml
let generatePairs etc names =  
  let rec generating names pairs =  
    match names with  
    | [] -> etc pairs  
    | name :: otherNames ->  
        generating otherNames (alPut name false pairs);  
        generating otherNames (alPut name true  pairs)  
  in  
  generating names []  
;;
```
### `;` operator (sequencing) — how it works
- `e1; e2` evaluates `e1`, discards its value, then evaluates `e2` and returns `e2`.
- Used to:
    - run a continuation for its effects
    - then continue recursion (loops in functional form)
### `generateAndTestPairs` (short-circuit with `&&`)
Idea: stop early once you find a false row.
```ocaml
let generateAndTestPairs etc names =  
  let rec generating names pairs =  
    match names with  
    | [] -> etc pairs  
    | name :: otherNames ->  
        (generating otherNames (alPut name false pairs))  
        && (generating otherNames (alPut name true  pairs))  
  in  
  generating names []  
;;
```
### `isIn`, `uniquify`, `names` for variable discovery
Membership:
```ocaml
let isIn thing things =  
  let rec isInning things =  
    match things with  
    | [] -> false  
    | firstThing :: otherThings ->  
        (firstThing = thing) || (isInning otherThings)  
  in  
  isInning things  
;;
```
Remove duplicates:
```ocaml
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
```
Collect unique variable names in a proposition:
```ocaml
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
```
### Final tautology checker
```ocaml
let isTautology proposition =  
  generateAndTestPairs  
    (fun pairs -> evaluate proposition pairs)  
    (names proposition)  
;;
```
## Environments + Closures
### What an environment is
- An internal structure that records **bindings** (name → value).
- Includes user bindings (`b = 1`) and built-ins (operators like `(+)`).
### What a closure is (3 parts)
A function value is represented as a closure containing:
1. the defining **environment**
2. the **parameters**
3. the **body** (not evaluated until called)
### How functions close themselves (static/lexical binding)
Example:
```ocaml
let b = 1;;  
let plusB a = a + b;;  
  
let mystery a =  
  let b = 2 in  
  plusB a  
;;  
(* mystery 10 = 11 *)
```
Reason:
- `plusB` remembers `b = 1` from where it was defined.
- It does not use `b = 2` from the call site.
## Continuations + CPS
### What a continuation is
- A function representing “what to do next with a result.”
### What CPS is
A style where:
- instead of returning the main result,
- you pass it to a continuation (possibly many times, or zero times)
Template: `f x (fun y -> (* use y *) ...)`
### CPS “for loop” pattern
```ocaml
let forLoop etc min max =  
  let rec looping index =  
    if index <= max  
    then (etc index; looping (index + 1))  
    else ()  
  in  
  looping min  
;;
```
## Data Structures / CS Background You Might Need
### Big-O basics for this course
- List membership (`isIn`) is O(n)
- Association-list lookup (`alGet`) is O(n)
- Balanced BST search/insert is about O(log n)
- Worst-case BST can be O(n)
- Truth-table brute force: `2^n` assignments for n variables
### Stack frames + recursion
- Each non-tail recursive call typically adds a stack frame.
- Tail recursion can run in constant stack space (compiler reuses the frame).
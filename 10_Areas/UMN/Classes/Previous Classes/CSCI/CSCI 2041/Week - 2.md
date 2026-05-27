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
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 3 & 4|Chapter - 3 & 4]]"
tags:
  - "#Lecture"
  - "#class"
next:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 2041/Week - 3|Week - 3]]"
---
# Entire Week
## What you must be able to do
- [[50_Archive/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Chapter - 3 & 4]]  
- [[OCaml - Basics]]  
- [[OCaml - Pattern Matching]]  
- [[OCaml - Let bindings, Scope & Closures]]
- [[OCaml - Labeled and Optional Arguments]]  
- Explain what a **stack frame** contains (minimum: parameters, local names, return point).
- Given a recursion, identify the **tail of the function** (chronologically last thing it does).
- Decide whether a recursive call is a **tail call** (nothing happens after it except returning).
- Rewrite an imperative loop as a **tail-recursive helper** using the conversion checklist (loop vars → parameters; assignments → new arguments; while test → if test; initialization → initial helper call).
## Key ideas (textbook)
- **`let ... in ...` scoping:** `let x = e1 in e2` binds `x` only inside `e2` (the body), not inside `e1`.  
- **Static (lexical) binding**: a function uses values from where it was defined, not where it is called. Shadowing creates a new binding that temporarily hides the old one. 
	- See: [[50_Archive/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4#3.1.1 Scoping and Nested Functions]]
- **Function types associate to the right:** `t1 -> t2 -> t3` means `t1 -> (t2 -> t3)` (this is why partial application works).  
- **Function application binds tightly:** `f x + y` is `(f x) + y` unless you add parentheses.  
- **Partial application** produces a function waiting for the remaining arguments (common exam trap).  
	- See: [[50_Archive/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4#3.1 Functional programming and Functions]]
- Classic factorial is **not tail recursive** because `*` happens after the recursive call returns.
- Tail recursion means: **all recursive calls are in the tail**.
- Why tail recursion can be as stack-efficient as loops: compiler can reuse one frame for tail calls.
- **Pattern matching**: evaluate the matched expression once, then try patterns in order, first match wins.  
- **Recursion needs `rec`:** a function that calls itself must be defined with `let rec ...` or you’ll get an “unbound value” style error.  
- **Tail recursion idea (core):** recursive call is the last thing the function does → compiler can reuse stack frames.
## Examples worth keeping
1. **Iterative factorial (imperative)**  
	- Uses one stack frame (constant stack space) because the loop updates locals inside a single call.  
2. **Classic recursive factorial (OCaml style)**  
	- Uses one new stack frame per recursive call; multiplications happen *while returning* (work deferred upward).  
3. **Tail-recursive factorial (OCaml style with helper / accumulator)**  
	- Multiplications happen *on the way down*; returning just passes the accumulated value back up.  
4. **Tail-call identification**  
	- In `if cond then f (x-1) else x`, the call can be tail (if nothing happens after it).  
	- In `x * f (x-1)`, the call is not tail (because `*` must still happen).  
5. **Loop → tail recursion pattern**  
	- “loop variables become parameters” + “assignments become new arguments” + “while-test becomes if-test”.
## Lecture
### Jan 30 - Why we don’t need loops (stacks, frames, tail calls, tail recursion) 
#### How calls happen (the stack model)  
- Most languages maintain a **stack** with **push** and **pop**.  
- What’s on the stack: **frames** (a.k.a. activation records).  
- The professor’s “minimum frame contents”:  
	- **parameters** (what the function was called with)  
	- **local names** (names local to the function)  
	- **return point** (where execution resumes after return)  
> [!NOTE] “Every time we call a function, we push a new frame on the stack. Every time we return, we pop a frame off the stack.”  
> - The **top frame** is the currently executing function.  
> - In diagrams, the professor draws stacks “upside down” (top at the bottom) and slashes frames when popped.  
#### Iterative factorial (imperative) vs recursive factorial (OCaml): what changes on the stack? 
**A. Imperative factorial (loop)**  
- One function call → one stack frame.  
- The loop updates locals inside the same frame.  
```ocaml
int fac(int n)
{
	int f = 1;
	while (n>0)
	{
		f = n*f;
		n = n-1;
	}
	return f;
}
```
- Conclusion: *constant stack space* (efficient like you expect).  
**B. Classic recursive factorial**  
- Each recursive call pushes a new stack frame.  
- Stack depth grows with the number of recursive calls. Less efficient.
- *Key observation*: the multiplication happens **as we return** (the calls are “waiting to finish” so they can multiply).
> [!NOTE] “All the computation occurs as we return - going back up the stack.”  
#### Terminology (professor definitions)  
- **Tail of a function:** the chronologically last thing the function does.    
	- This has **nothing** to do with `tl`.  
	- `*` is the tail
- **Tail call:** a function call that occurs during the tail.    
	- Meaning: after that call, the caller does nothing except return its result.
	- `fac` is not a tail cell.
- **Tail recursion:** a function is tail-recursive if **all recursive calls occur in a tail** (i.e., all recursive calls are tail calls).  
1. *Why `fac (n-1)` is NOT a tail call in classic factorial*
	*Classic shape*:  
```ocaml  
let rec fac n =  
  if n = 0 then 1  
  else n * fac (n - 1)
```
- The tail (last thing) is the `*` multiplication.
- The recursive call must return **before** multiplication can happen.
- Therefore: recursive call is **not** in the tail → **not** tail recursive.
#### Tail-recursive factorial (what changes and why it’s efficient)
Tail-recursive shape (accumulator helper):
```ocaml
let rec facing f n =  
  if n = 0 then f  
  else facing (n * f) (n - 1) ;;
  
let fac n = facing 1 n ;;
```
- The call to `facing` is the last thing the function does (tail call).
- Multiplications happen **during calls**, going down the recursion.
- Returning does not perform extra work(stack frames); it mainly passes the final value up.
> [!NOTE] “No computation occurs as we return.”
#### Why tail recursion can use constant stack space
- If the compiler supports tail-call optimization: 
    - it can **reuse** a single frame for successive tail calls
    - or “never push a new frame at all” and keep reusing the top frame
- Result: **constant stack space**, same advantage as loops.
#### Big finish (professor’s three conclusions)
1. We don’t need loops. 
2. We write loops as tail recursions.
3. They are as efficient as loops (when optimized).
4. Try to write tail recursions whenever possible.
> [!NOTE] Practical warning (exam + real code)
> - Not every recursion can be rewritten as tail recursion.
> - Some functions can be “partially tail recursive” (some calls in tail, others not).
### “Loop → tail recursion” conversion checklist (what you should copy into your brain)
- **Loop variables** → parameters of the helper function.
- **Assignments** → new argument values passed into the next recursive call.
- **While test** → `if` condition that decides recurse vs stop.
- **Initializations** → the initial call to the helper with starting argument values.
- **If a value never changes** → inherit it via an internal helper (`let rec helper ... in helper ...`) instead of passing it every time.
## Lab - 1 Takeaways
### Function 1 - `how many e l`
*Goal*: Count how many times `e` appears in list `l`.
1. Why the type is `'a -> 'a list -> int`
	lists have type `t list`, and `'a` is a placeholder meaning “any type.” So `howMany` works for ints, strings, chars, etc.
2. Recursion structure (exactly like your “length” example): 
	- Base: `[] -> 0`
	- Step: `1 + length (tl s)`
	`howMany` follows the same structure:
	**Base case:** If `l = []`, there are 0 matches.
	**Recursive case:** Look at:
	- `h = hd l` (first element)
	- `t = tl l` (the rest)
	Then:
	- if `e = h`, count `1 + howMany e t`
	- else just `howMany e t`
> [!NOTE] *Key beginner point*: 
> - `hd` and `tl` are only safe on **non-empty lists**. Your notes say `hd []` and `tl []` are errors, so the `if l = [] then ... else ...` guard is doing safety first.
### Function 2 - `delete e l`
*Goal*: Return a list like `l` but **without any** occurrences of `e`.
1. **Base case:** `l = []` → return `[]`.
2. **Recursive case:** use `h = hd l`, `t = tl l`.
Now the key idea:
- If `h` equals `e`, we **skip** it: return `delete e t`
- Otherwise, we **keep** it: return `h :: delete e t`
#### Why `::` matters (and why this is persistent)
`::` adds one element to the **front** and does not modify the existing list ([[OCaml - Types of Programming#Persistence (the “copy as little as possible” model)|Persistence|persistence]]).
So `h :: delete e t` means:
- build a brand-new list node containing `h`
- whose tail points to the result of the recursive call
- the original `l` remains unchanged and still usable
### Function 3 - `mean l`
*Goal*: Compute the arithmetic average of a **non-empty** `float list`.
1. Two big rules from your notes
	1. **No implicit numeric coercions**: `1 + 2.0` is invalid; ints use `+` and floats use `+.`.
	2. The REPL/type system forces you to be consistent: float math must stay float math.
	So mean needs:
	- total sum as a `float`
	- length as an `int`
	- conversion: `float_of_int n`
#### Why helper functions are used
Your [[50_Archive/Previous Classes/CSCI/CSCI 2041/Week - 1#Lecture (Jan 28) - Multi-argument function types, append, immutability/persistence, helpers|Week 1]] notes mention internal helpers: use `let ... in` to define helpers inside a function when it keeps things cleaner. So `mean` typically defines:
- `length : 'a list -> int`
- `sum : float list -> float`
Then:
- `sum l /. float_of_int (length l)`
> [!NOTE] Beginner “type check” trick: Ask yourself:
> - `sum l` is `float`    
> - `float_of_int n` is `float`    
> - `/.` expects `(float, float)` and returns `float`  
> - So the whole expression stays `float` — exactly what `mean` promises.
## Midterm Check
### Chapter - 3
- [ ] **Static vs. Dynamic Binding:** If a function uses a variable defined outside its body, does it use the value of that variable from where the function was _defined_ or where it was _called_?.
- [ ] **Partial Application:** If a function has the type `int -> int -> int` and you provide it with only one `int`, what is the type of the resulting value?.
- [ ] **The** **rec** **Keyword:** What happens if you try to write a recursive function but forget the `rec` modifier in the `let` binding?
### Overall
- [ ] **Stacks + frames:** What three things does the professor say a stack frame contains (minimum)?
- [ ] **Tail (not `tl`):** In `let rec fac n = if n=0 then 1 else n * fac (n-1)`, what is the *chronologically last* thing the function does?  
- [ ] **Tail call vs not-tail call:** Why is `fac (n-1)` **not** a tail call in the classic factorial?  
- [ ] **Tail recursion test:** A function is tail-recursive iff what condition holds about its recursive calls?  
- [ ] **Why tail recursion is “loop-level efficient”:** What exactly changes about stack usage when a compiler performs tail-call optimization?  
- [ ] **Translation rules:** When converting a loop to OCaml, what do (1) loop variables, (2) assignments, (3) while-test, (4) initializations become?  
> [!NOTE] A likely exam prompt: *“Is this function tail recursive? Explain why. If not, rewrite in tail-recursive form if possible.”*
## Flashcards
#cards/CSCI2041 

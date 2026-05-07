---
type: class
status: archived
created: 2025-11-07
updated: 2025-11-08
area:
  - "[[Main Examples]]"
  - "[[Finals]]"
  - "[[Material]]"
tags:
  - "#class"
  - "#Homework"
  - "#Textbook"
  - "#Discussion"
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2011/Chapter - 6]]"
---
# #Textbook Textbook & Videos
## 5.1
### Mathematical Induction and Linear Congruences
**The Ladder Analogy**: Think of mathematical induction like climbing an infinite ladder.
- If you can prove you can get to the first rung (basis step)
- AND you can prove that getting to any rung means you can get to the next rung (inductive step).
- Then you can reach ANY rung on the ladder!
*The Two-Step Process*:
1. **Step 1: Basis Step**:
	- Prove that your statement P(n) is true for the first value  
	- Usually P(1), but could be P(0) or P(3) depending on the problem  
	- This is always just simple math - plug in the number and verify it works
2. **Step 2: Inductive Step**:
	- **Inductive Hypothesis**: Assume P(k) is true (this is your assumption)  
	- **Must Show**: Prove that P(k) implies P(k+1) is true  
	- If both steps work, then P(n) is true for all positive integers!
- [[Main Examples#Mathematical Induction Summation|Mathematical Induction Summation Examples]]
### Proving Inequalities with Mathematical Induction
Mathematical induction for inequalities works just like regular induction, but with a HUGE twist. Instead of things having to be exactly equal, we just need to preserve the inequality direction.
- This means we can "cheat" by replacing numbers with bigger numbers (as long as we're going in the right direction).
1. **Proof 1**: n < 2ⁿ for all positive integers:
	**What we're proving:** P(n) = "n < 2ⁿ for all positive integers n"
	**Step 1 - Basis Step:**
	- Start with n = 1 (smallest positive integer)  
	- Check: Is 1 < 2¹?  
	- 1 < 2 ✓ TRUE!  
	- Basis step complete
	**Step 2 - Inductive Step:** **Assume:** P(k) is true, meaning k < 2ᵏ (this is our inductive hypothesis).
	**Show:** P(k+1) is true, meaning (k+1) < 2^(k+1)
	**The Magic Happens Here:** Start with: k < 2ᵏ  
	-  Add 1 to both sides: k + 1 < 2ᵏ + 1  
	- **HERE'S THE TRICK:** Since 1 < 2ᵏ for all positive k, we can replace the 1 with 2ᵏ  
	- So: k + 1 < 2ᵏ + 2ᵏ = 2 × 2ᵏ = 2^(k+1)  
	- We got exactly what we wanted to show!
	**Why this "cheating" works:** We replaced 1 with something BIGGER (2ᵏ). Since the original inequality was "less than," making the right side bigger keeps it true. 
		- It's like saying "if 5 < 10, then 5 < 100" - totally valid!
2. **Proof 2**: 2ⁿ < n! for all integers n ≥ 4
	**What we're proving:** P(n) = "2ⁿ < n! for all integers n ≥ 4"
	**Step 1 - Basis Step:**  
	- Start with n = 4 (our smallest value this time)  
	- Check: Is 2⁴ < 4!?  
	- 2⁴ = 16, and 4! = 4×3×2×1 = 24  
	- 16 < 24 ✓ TRUE!
	**Step 2 - Inductive Step:**  
	- **Assume:** P(k) is true, meaning 2ᵏ < k! (inductive hypothesis)  
	- **Show:** P(k+1) is true, meaning 2^(k+1) < (k+1)!
	**The Magic Part 2:** Start with: 2ᵏ < k!  
	- Multiply both sides by 2: 2 × 2ᵏ < 2 × k! 
	- This gives us: 2^(k+1) < 2 × k!  
	**ANOTHER TRICK:** We need (k+1)!, but we have 2 × k! Since k ≥ 4, we know (k+1) ≥ 5, so (k+1) > 2.
	- We can replace the 2 with (k+1): 2^(k+1) < (k+1) × k! And (k+1) × k! = (k+1)! by definition of factorial!
- Key Rules for Inequality Proofs: **The Golden Rule:** You can replace any number with a BIGGER number on the "greater than" side, or a SMALLER number on the "less than" side.
	**Why this works:**  If a < b and b < c, then a < c (transitivity)  
### Proof by Induction for Divisibility
We want to show that 7^(n+2) + 8^(2n+1) is divisible by 57 for *all non-negative integers n*.
This is tricky because we don't have an equation to work with - just a divisibility statement!
- Setting Up the Problem: Let P(n) = "7^(n+2) + 8^(2n+1) is divisible by 57". We need to prove this for all non-negative integers (so starting from n = 0). 
	- Base Case: P(0): Check if P(0) is true: 7^(0+2) + 8^(2×0+1) = 7² + 8¹ = 49 + 8 = 57. 
		- Since 57 ÷ 57 = 1, this is definitely divisible by 57 ✓ Base case proven!
	- Inductive Step Setup:
		- **Inductive Hypothesis**: Assume 7^(k+2) + 8^(2k+1) is divisible by 57  
		- **What we want to prove**: 7^(k+3) + 8^(2k+3) is divisible by 57
	- *The Tricky Part* - No Equation to Manipulate! Professor X's strategy: Start with the inductive hypothesis and transform it cleverly.
	- The Mathematical Magic Trick: 
		- Take the inductive hypothesis: 7^(k+2) + 8^(2k+1)  
		- Multiply the first term by 7: 7 × 7^(k+2) = 7^(k+3)  
		- Multiply the second term by 8²: 8² × 8^(2k+1) = 64 × 8^(2k+1) = 8^(2k+3)  
		- Now we have: 7 × 7^(k+2) + 64 × 8^(2k+1)
	- The Clever Substitution:
		-  Instead of writing 64, write it as (7 + 57) Why? Because 64 = 7 + 57 (this is totally legal math!)  
		- So now we have: 7 × 7^(k+2) + (7 + 57) × 8^(2k+1)  
		- Distribute: 7 × 7^(k+2) + 7 × 8^(2k+1) + 57 × 8^(2k+1)
		- Factoring Out the 7
		- Factor out 7 from the first two terms: 7(7^(k+2) + 8^(2k+1)) + 57 × 8^(2k+1). Now we can use our inductive hypothesis!
	- Using the Inductive Hypothesis: We know 7^(k+2) + 8^(2k+1) is divisible by 57 (that's our assumption).
		- So 7(7^(k+2) + 8^(2k+1)) is also divisible by 57 and 57 × 8^(2k+1) is obviously divisible by 57.
		- Therefore, their sum 7^(k+3) + 8^(2k+3) is divisible by 57!
	- Why This Works: If A is divisible by 57 and B is divisible by 57, then A + B is divisible by 57. We showed that 7^(k+3) + 8^(2k+3) can be written as the sum of two things that are both divisible by 57.
- **Divisibility rules**: Sum of numbers divisible by the same value is also divisible by that value.
## 5.2
### The Well Ordering Principle
**Main idea**: Every non-empty set of non-negative integers has a least element  
**What this means**: If you have any collection of whole numbers (0, 1, 2, 3...), there's always a smallest one in that collection.
**Examples of least elements**:
- Positive integers (1, 2, 3, 4...): least element is 1
- Integers starting from 4 (4, 5, 6, 7...): least element is 4
- Non-negative integers (0, 1, 2, 3...): least element is 0
**Why this matters for induction**: You MUST start your mathematical induction proof with the least element of your set
**Important limitation**: This only works with integers!
- Rational numbers (fractions) don't have a least element
- Example: You can always make a fraction smaller by dividing by a bigger number
- That's why we only use non-negative integers in induction proofs
### Regular Mathematical Induction vs Strong Induction
The Postage Stamp Problem (Used to Compare Both Methods)
**Problem**: Prove that any postage of 12 cents or more can be made using only 4-cent and 5-cent stamps.
#### Regular Mathematical Induction Approach:
**Basis step**: Show it works for 12 cents
- Use three 4-cent stamps: 3 × 4 = 12 cents ✓
**Inductive hypothesis**: Assume we can make K cents of postage
**Inductive step**: Show we can make (K+1) cents of postage
- **Case 1**: If we used at least one 4-cent stamp for K cents
    - Replace one 4-cent stamp with one 5-cent stamp
    - This gives us exactly 1 more cent (K+1 cents) ✓
- **Case 2**: If we used NO 4-cent stamps for K cents
    - Since K ≥ 12 and we only used 5-cent stamps, we must have used at least three 5-cent stamps
    - Replace three 5-cent stamps (15 cents) with four 4-cent stamps (16 cents)
    - This gives us 1 more cent (K+1 cents) ✓
#### Strong Induction Approach:
**Multiple basis steps**: Show it works for several starting values
- 12 cents: three 4-cent stamps (3 × 4 = 12)
- 13 cents: two 4-cent stamps + one 5-cent stamp (2 × 4 + 1 × 5 = 13)
- 14 cents: one 4-cent stamp + two 5-cent stamps (1 × 4 + 2 × 5 = 14)
- 15 cents: three 5-cent stamps (3 × 5 = 15)
**Strong inductive hypothesis**: Assume ALL values from 12 up to some number K work (not just one value like regular induction).
**Strong inductive step**: Show that (K+1) also works
- We assume P(K-3) is true (we can make postage of K-3 cents)
- To make (K+1) cents: take the K-3 solution and add one 4-cent stamp
- (K-3) + 4 = K+1 ✓
- We chose K-3 because K-3 ≥ 12 (our starting point), so we know it works
### Key Differences Between Regular and Strong Induction:
1. **Regular Induction:**
	- Uses only ONE basis step  
	- Assumes only the previous case (K) works  
	- Must prove the very next case (K+1)
2. **Strong Induction:**
	- Uses MULTIPLE basis steps (covers a range of starting values)  
	- Assumes ALL previous cases work (from starting point up to K)  
	- Can "jump back" to any earlier proven case to build the next one  
	- More flexible - you can use any previously proven case, not just the immediate predecessor
- *When to Use Each Method:*
	- *Regular induction = domino effect (each piece knocks over the next one)*: When you can easily build from one case to the very next case  
	- *Strong induction = = building blocks (you can use any previously built pieces to build the next level)*: When you need to "look back" several steps or when the pattern requires using multiple previous cases.
## 5.3
### Recursive Definitions and Structural Induction
**Two essential parts**: basis step (initial conditions) + recursive step (rule for finding next values)  
**Key idea**: To find the next value, you MUST know the previous value(s)  
**Classic example**: Fibonacci sequence (0, 1, 1, 2, 3, 5, 8...)
	- Start with 0 and 1 (basis step)
	- Add the two previous numbers to get the next one (recursive step)
	- F(n) = F(n-1) + F(n-2) for n ≥ 2
- The Two Parts Explained: 
	- *Basis Step (Initial Conditions)*
		- **What it does**: Specifies the starting value(s)  
		- **Why needed**: You can't apply the recursive rule without something to start with  
		- **Example**: In Fibonacci, F(0) = 0 and F(1) = 1
	- *Recursive Step*
		- **What it does**: Gives the rule for finding subsequent values using previous ones.  
		- **Must specify**: For which values of n the rule applies  
		- **Example**: F(n) = F(n-1) + F(n-2) for n ≥ 2
	- [[Main Examples#Recursive Definition Examples|Function Examples]]
1. **Recursively Defined Sets** (Not Just Functions!): Natural Numbers Example
	- **Basis step**: 1 is a natural number  
	- **Recursive step**: If n is a natural number, then n + 1 is also a natural number  
	- **Result**: Gets us 1, 2, 3, 4, 5... (all counting numbers)
	- *Set S Example*:
		- **Basis step**: 7 ∈ S (7 is in set S - subset)  
		- **Recursive step**: If x ∈ S and y ∈ S, then x + y ∈ S  
		- **First five applications**:
			1. 7 (from basis)
			2. 7 + 7 = 14
			3. 7 + 14 = 21
			4. 7 + 21 = 28
			5. 7 + 28 = 35  
		- **Note**: You could also add 14 + 21 = 35, or any other valid combinations!
2. **Recursively Defined Structures**: *Rooted Trees*:
	- **Basis step**: A single vertex (the root) is a rooted tree  
	- **Recursive step**: Take disjoint rooted trees with roots r₁, r₂, r₃... Add a new root R and connect it to all these roots = new rooted tree  
	- **Visual**: Start with one dot, then you can connect it to other single dots, then connect those structures to make bigger trees
	- *Full Binary Trees*:
	- **Basis step**: Just a root vertex  
	- **Recursive step**: Take any leaf (end vertex) and add exactly TWO children to it  
	- **Key**: "Binary" means each vertex can have at most 2 children  
	- **Growth pattern**: Each step can add 2 new vertices to any existing leaf
- Well-Defined Functions
	- **Meaning**: The recursive definition works for ALL positive integers  
	- **Why important**: This lets us use mathematical induction to prove things about recursive definitions.
	- **Connection**: Recursive definitions + mathematical induction = powerful proof technique
	- Always Include Domain: 
		- **Don't forget**: Specify for which values of n your recursive step applies  
		- **Example**: "for n ≥ 1" or "for n ≥ 2"  
### Structural Induction
**Goal**: Prove that set S (defined recursively) equals set A (all positive integers divisible by 7)  
**Set S definition**:
- 7 is in S (basis step)
- If x and y are in S, then x + y is also in S (recursive step)  
	- **Set A definition**: A = {7n | n is a positive integer} (all multiples of 7)
- **To prove sets are equal**: Show S ⊆ A AND A ⊆ S
- **Proving A ⊆ S** (using mathematical induction):
	- **Basis**: 7×1 = 7 is in S ✓
	- **Inductive step**: If 7k is in S, then 7k + 7 = 7(k+1) is also in S ✓
	- **Conclusion**: All multiples of 7 are in S
- **Proving S ⊆ A**:
	- **Basis**: 7 is in A (since 7 = 7×1) ✓
	- **Recursive step**: If x and y are in A, then x = 7a and y = 7b for some integers a,b
	- So x + y = 7a + 7b = 7(a+b), which is also in A ✓
	- **Conclusion**: Everything in S is also in A
**Key difference from mathematical induction**: Specifically designed for recursively defined structures (like trees, lists, etc.). **Two parts**:
- **Basis step**: Prove the statement holds for all basic elements in the recursive definition
- **Recursive step**: If the statement is true for smaller elements, prove it's true when you combine them
1. **Full Binary Trees - The Setup**: **Height definition**:
	- Single vertex tree has height 0
	- Combined tree has height = 1 + max(height of subtree 1, height of subtree 2)
	- Example: If you combine a tree of height 1 with a tree of height 2, new height = 1 + max(1,2) = 3
	- **Number of vertices definition**:
		- Single vertex tree has 1 vertex
		- Combined tree has vertices = (vertices in tree 1) + (vertices in tree 2) + 1 (for the new root)
2. **The Big Structural Induction Proof**:
	- **Goal**: Prove that for any full binary tree T: n(T) ≤ 2^(h(T)+1) - 1 (Number of vertices ≤ 2 to the power of (height + 1) minus 1).
	- **Basis step**:
		- Single vertex tree: n(T) = 1, h(T) = 0
		- Check: 1 ≤ 2^(0+1) - 1 = 2^1 - 1 = 1 ✓
	- **Recursive step**:
		- **Hypothesis**: Assume the inequality holds for subtrees T₁ and T₂
	- **Proof steps**:
	    1. n(T) = 1 + n(T₁) + n(T₂) (by definition)
	    2. n(T) ≤ 1 + (2^(h(T₁)+1) - 1) + (2^(h(T₂)+1) - 1) (using hypothesis)
	    3. This simplifies to: n(T) ≤ 1 + 2×(2^max(h(T₁),h(T₂)+1) - 1)
	    4. **Math magic**: Sum of two terms ≤ 2 × (larger term)
	    5. Since max(2^x, 2^y) = 2^max(x,y), we get: n(T) ≤ 2×2^max(h(T₁),h(T₂)+1) - 1
	    6. Since h(T) = 1 + max(h(T₁), h(T₂)), we have: n(T) ≤ 2^(h(T)+1) - 1 ✓
## 5.4
### Recursive Algorithms and Proofs
**Definition**: An algorithm that solves a problem by breaking it down into smaller versions of the same problem. 
**Key idea**: Keep reducing the problem size until you reach a simple base case that you can solve directly  
**Think of it like**: Russian nesting dolls - each doll contains a smaller version of itself until you get to the tiniest one
1. **The Euclidean Algorithm (Finding GCD)**
	- **Example**: Finding GCD of 14 and 20
	- **Step-by-step breakdown**:
		- GCD(14, 20) = GCD(14, 6) because 20 = 14×1 + 6
		- GCD(14, 6) = GCD(6, 2) because 14 = 6×2 + 2
		- GCD(6, 2) = GCD(2, 0) because 6 = 2×3 + 0
		- GCD(2, 0) = 2 (when one number is 0, the GCD is the other number)
	**Pseudocode Structure**:
```bash
GCD(a, b) where a < b and both are non-negative integers
- If a = 0, then return b
- Otherwise, return GCD(b mod a, a)
```
- **Why this works**: We keep swapping and taking remainders until one number becomes 0.   
- **The magic**: Each step makes the numbers smaller, so we eventually reach the base case.
2. **Factorial Algorithm**: **What we're computing**: n! = n × (n-1) × (n-2) × ... × 1
	- **Example**: 4! = 4 × 3 × 2 × 1 = 24
	- **Pseudocode**:
```bash
Factorial(n) where n is a non-negative integer
- If n = 0, then return 1 (because 0! = 1)
- Otherwise, return n × Factorial(n-1)
```
- **Step-by-step for 4!**:
	- Factorial(4) = 4 × Factorial(3)
	- Factorial(3) = 3 × Factorial(2)
	- Factorial(2) = 2 × Factorial(1)
	- Factorial(1) = 1 × Factorial(0)
	- Factorial(0) = 1 (base case!)
	- Working backwards: 1 × 1 × 2 × 3 × 4 = 24
3. **Power Algorithm (Exponentiation)**: **What we're computing**: a^n where a ≠ 0 and n ≥ 0. 
- **Pseudocode**:
```bash
Power(a, n)
- If n = 0, then return 1 (anything to the 0 power is 1)
- Otherwise, return a × Power(a, n-1)
```
- **Example with 5^4**:
	- Power(5, 4) = 5 × Power(5, 3)
	- Power(5, 3) = 5 × Power(5, 2)
	- Power(5, 2) = 5 × Power(5, 1)
	- Power(5, 1) = 5 × Power(5, 0)
	- Power(5, 0) = 1 (base case!)
	- Result: 5 × 5 × 5 × 5 × 1 = 625
4. *Proving Recursive Algorithms Work (Mathematical Induction)*: **For the Power Algorithm Proof**:
	- **Basis Step**: Prove it works for the smallest case
		- When n = 0: a^0 = 1 for any nonzero a
		- Our algorithm returns 1 when n = 0 ✓
	- **Inductive Step**: Assume it works for some value k, prove it works for k+1
		- **Assumption**: Power(a, k) correctly gives us a^k
		- **Need to prove**: Power(a, k+1) correctly gives us a^(k+1)
		- **Logic**: Power(a, k+1) = a × Power(a, k) = a × a^k = a^(k+1) ✓
	- **Why this matters**: This mathematical proof guarantees our algorithm will always work correctly!


---
# #Homework Homework 6


---
# #Discussion Discussions 6


---

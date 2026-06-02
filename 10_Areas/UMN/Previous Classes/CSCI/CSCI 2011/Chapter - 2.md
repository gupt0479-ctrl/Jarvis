---
type: class
status: archived
created: 2025-10-02
updated: 2025-10-04
area:
  - "[[Main Examples]]"
  - "[[Material]]"
  - "[[Finals]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Homework"
  - "#Discussion"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 2011/Chapter - 3]]"
---
# #Textbook Textbook & Videos 
## 2.1 
### Introduction to Sets: Vocabulary and Notation
1. What is a Set?
	- A set is an **unordered collection of objects** - no particular order needed!
	- Example: Professor X's brothers = {Eric, Adam, Kevin} - not arranged by age, favorites, etc.
	- **Elements** are the objects inside a set (Eric, Adam, and Kevin are elements)
2. Set Membership Notation: **∈** means "is an element of" or "belongs to the set"
	- Adam ∈ B (Adam belongs to set B)  
		- **∉** means "is not an element of" or "does not belong to the set": Larry ∉ B (Larry is not Professor X's brother)
3. Important Number Sets You MUST Know
	- **ℕ (Natural Numbers)**: The counting numbers = {1, 2, 3, 4, 5, ...} going to infinity  
	- **𝕎 (Whole Numbers)**: Natural numbers + zero = {0, 1, 2, 3, 4, 5, ...}  
	- **ℤ (Integers)**: All positive and negative whole numbers = {..., -3, -2, -1, 0, 1, 2, 3, ...}  
	- **ℚ (Rational Numbers)**: Numbers that can be written as a/b where:
		- a and b are both integers
		- b ≠ 0 (can't divide by zero!)
		- a/b is in lowest terms.
	- **ℝ (Real Numbers)**: ALL the above sets combined - anything that's not imaginary  
	- **ℂ (Complex Numbers)**: Numbers in form a + bi where:
		- a = real component (a real number)
		- bi = imaginary component
	- Special Notation Tricks: 
		- **ℤ⁺** = positive integers only
		- **ℤ⁻** = negative integers only
### Three Types of Set Notation
1. Roster Notation
	- **What it is**: Simply listing all elements like a sports team roster. *Example*: S = {1, 2, 3, 4, 5}  
	- **IMPORTANT RULE**: Can ONLY be used with **discrete sets**(countable objects, not continuous)
	- **Cannot use with**: Sets like "all numbers between 0 and 1" (infinite decimal possibilities!)
2. Set Builder Notation
	- **What it is**: Describes the set using conditions  
	- **Format**: {x | conditions} where "|" means "such that"  
	- **Can be used for ANY type of set** (discrete OR continuous)  
	- **Examples for S = {1, 2, 3, 4, 5}**:
		- S = {x | x ∈ ℕ and x ≤ 5}
		- S = {x | x ∈ ℤ and 1 ≤ x ≤ 5}
3. Interval Notation
	- **Best for continuous sets** (clearest and easiest method)  
	- **Only for continuous sets** - implies the set is continuous  
	- **Focus on endpoints** and whether they're included
4. Interval Notation Rules: 
	- **Closed bracket [ ]**: Endpoint IS included (≤ or ≥)  
	- **Open bracket ( )**: Endpoint is NOT included (< or >)
5. Examples:
	- **B = {x | 0 ≤ x ≤ 1}** → **[0, 1]** (both 0 and 1 included)  
	- **M = {x | 0 < x ≤ 1}** → **(0, 1]** (0 not included, 1 included)  
	- **{x | 0 < x < 1}** → **(0, 1)** (neither endpoint included)
### Two Special Sets
1. **Universal Set (U)**
	- **Definition**: The set of ALL elements under consideration for your problem  
	- **Think of it as**: "What am I studying?"  
	- **Venn Diagram**: The big box containing everything you're working with  
	- **Example**: If studying natural numbers, U = all natural numbers
		- Even naturals go in a circle inside the box
		- Odd naturals (like 1, 3, 5) go in the box but outside the circle
2. **Empty Set (∅)**:
	- **Definition**: A set with NO elements  
	- **Two correct ways to write it**:
		- ∅ (zero with line through it)
		- { } (empty set brackets)  
	- **WRONG way**: {∅} - This means a set containing one element (the empty set itself)!
### Set Equality
- **Sets are equal if they have the same elements** - doesn't matter about order or duplicates! 
- **Notation**: A = B means for all x, x ∈ A if and only if x ∈ B  
- **Example**: Set A = {0, 1, 1, 3, 4, 4} equals Set B = {0, 1, 3, 4} because they contain the exact same unique elements  
- **Key point**: Duplicates don't matter, order doesn't matter - only what elements are actually in there  
- **Counter-example**: If B had a 5 in it, then A ≠ B because B would have an element A doesn't have
## Subsets
- **Definition**: Set A is a subset of B if every element of A is also in B  
- **Notation**: A ⊆ B (think of it like A ≤ B)
- **Visual**: In a Venn diagram, A would be completely inside B  
- **Example**: A = {1, 2, 3} and B = {1, 2, 3, 4, 5} - A is a subset of B because all of A's elements are in B
1. How to Prove Subsets (Super Important for Exams!):
	- **To prove A ⊆ B**: Show that if x belongs to A, then x belongs to B  
	- **To prove A is NOT a subset of B**: Find just one element that's in A but not in B  
	- **To prove A = B**: Prove both A ⊆ B AND B ⊆ A (this is the standard way to prove set equality!)
## Proper Subsets
- **Definition**: A is a proper subset of B if A ⊆ B but A ≠ B  
- **Notation**: A ⊂ B (notice no line under the symbol)  
- **What this means**: A is contained in B, but B has at least one element that A doesn't have  
- **Example**: A = {1, 2, 3} and B = {1, 2, 3, 4} - A is a proper subset of B because B has that extra 4  
- **Formal notation**: For all x, if x ∈ A then x ∈ B, AND there exists some element in B that's not in A.
### Cardinality (Size of Sets)
- **Definition**: The number of *distinct* elements in a set  
- **Notation**: |A| (looks like absolute value bars)  
- **Cardinality formula**: If |A| = n, then |P(A)| = 2^n
- **Example**: If A = {1, 2, 3, 3, 3, 4}, then |A| = 4 (because there are 4 distinct elements)  
- **Alphabet example**: |{alphabet}| = 26, *Empty set* |∅| = 0
### Power Sets (This Gets Tested A LOT!)
- **Definition**: The set of ALL possible subsets of a set  
- **Example**: If A = {0, 1, 2}, then P(A) includes:
	- ∅ (empty set)
	- {0}, {1}, {2} (single elements)
	- {0,1}, {0,2}, {1,2} (pairs)
	- {0,1,2} (the whole set)  
- **Cardinality formula**: If |A| = n, then |P(A)| = 2^n
- **Professor X's example**: A has 3 elements, so |P(A)| = 2³ = 8 subsets total
### Tuples and Ordered Pairs
- **Key difference from sets**: ORDER MATTERS!  
- **Notation**: (a₁, a₂, a₃, ...) for tuples, (a, b) for ordered pairs  
- **Important**: (5, 2) ≠ (2, 5) - these are completely different!  
- **Why this matters**: Think Cartesian coordinates - (5, 2) and (2, 5) are different points.
### Cartesian Products
- **Definition**: Set of all ordered pairs (a, b) where a ∈ A and b ∈ B  
- **Notation**: A × B  
- **Example**: If A = {0, 1} and B = {2, 3, 4}, then A × B = {(0,2), (0,3), (0,4), (1,2), (1,3), (1,4)}  
- **How to build it**: Take every element from A, pair it with every element from B  
- **Relations preview**: Any subset of a Cartesian product is called a relation (we'll see this again!).
### Truth Sets
- **Definition**: Set of all values that make a propositional function P(x) true  
- **Notation**: {x ∈ D | P(x)} where D is the domain  
- **Example**: If P(x) means "|x| = 3" and domain is integers, then truth set = {-3, 3}  
- **How to find it**: Plug in values and see which ones make the statement true
## 2.2
### Union of Sets (∪)
- **Definition**: The union combines ALL elements from both sets - think of it like pouring everything into one big cup  
- **Notation**: A ∪ B  
- **Key concept**: It's like "OR" - an element belongs if it's in set A OR set B (or both)  
- **Example**: If A = {1, 4, 7} and B = {4, 5, 6}, then A ∪ B = {1, 4, 5, 6, 7}  
- **Important**: Duplicates are only listed once (the 4 appears in both sets but we only write it once in the union)  
- **Visual**: In a Venn diagram, it's everything inside BOTH circles combined  
- **Inclusion-Exclusion Formula**: |A ∪ B| = |A| + |B| - |A ∩ B| (we subtract the intersection to avoid double-counting)
### Intersection of Sets (∩)
- **Definition**: Only elements that appear in BOTH sets  
- **Key concept**: It's like "AND" - an element belongs if it's in set A AND set B  
- **Example**: Using same sets above, A ∩ B = {4} (only 4 appears in both sets)  
- **Visual**: In a Venn diagram, it's only the overlapping middle section.
- **Special case**: If A ∩ B = ∅ (empty set), then A and B are called **disjoint** sets.
- **Disjoint sets**: Have no elements in common - their Venn diagram circles don't overlap at all.
### Complement of a Set (not A or A')
- **Definition**: All elements in the universe that are NOT in the set  
- **Notation**: "not A" or A' or Ā  
- **Key concept**: Everything EXCEPT what's in the set  
- **Example**: If universe = {0,1,2,3,4,5,6,7,8,9} and A = {1,4,7}, then not A = {0,2,3,5,6,8,9}  
- **Visual**: In a Venn diagram, it's everything OUTSIDE the circle but still in the universe box
### Difference of Sets (A - B)
- **Definition**: Elements that are in A but NOT in B  
- **Process**: Start with set A, then remove any elements that also appear in B  
- **Example**: If A = {1,4,7} and B = {4,5,6}, then A - B = {1,7}  
- **Key point**: You can ONLY include elements that were originally in A - you can't add new ones  
- **Visual**: In a Venn diagram, it's the part of circle A that doesn't overlap with circle B
[[Main Examples#Sets|Examples of Set Operations]]
## Key Memory Tips
- **Union = Cup**: Pour everything together  
- **Intersection = Overlap**: Only what they share  
- **Complement = Outside**: Everything else in the universe  
- **Difference = Subtraction**: Take away the shared parts  
- **Disjoint = Separate**: No overlap at all
### Set Identities
#### Identity Laws (Like Adding Zero!)
- **A ∪ ∅ = A** - Taking the union of any set with the empty set gives you back the original set (like adding 0 to a number)
- **A ∩ U = A** - Taking the intersection of any set with the universe gives you back the original set (since A is already contained in the universe)
#### Domination Laws (One Set "Wins")
- **A ∪ U = U** - Union with the universe always gives you the universe (everything!)  
- **A ∩ ∅ = ∅** - Intersection with the empty set always gives you nothing (since empty set has no elements to share)
#### Idempotent Laws (Same Set Twice = Same Result)
- **A ∪ A = A** - A set combined with itself is just itself  
- **A ∩ A = A** - A set intersected with itself is just itself
#### Complementation Law (Double Negative)
- **(A')' = A** - The complement of the complement brings you back to the original set (like subtracting 5 then adding 5)
#### Commutative Laws (Order Doesn't Matter)
- **A ∪ B = B ∪ A** - You can take union in either order  
- **A ∩ B = B ∩ A** - You can take intersection in either order  
- Professor X says this is just like addition: 3 + 5 = 5 + 3
#### Associative Laws (Grouping Doesn't Matter)
- **(A ∪ B) ∪ C = A ∪ (B ∪ C)** - How you group unions doesn't change the result  
- **(A ∩ B) ∩ C = A ∩ (B ∩ C)** - How you group intersections doesn't change the result  
- Professor X emphasized: associative is ALWAYS about grouping, commutative is about order
#### Distributive Laws (Spreading Operations)
- **A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)** - Intersection distributes over union  
- **A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)** - Union distributes over intersection
#### De Morgan's Laws (The Negation Game-Changers!)
Professor X got really excited about these because "De Morgan just keeps popping up everywhere!"
- **(A ∪ B)' = A' ∩ B'** - Complement of union equals intersection of complements  
- **(A ∩ B)' = A' ∪ B'** - Complement of intersection equals union of complements
1. [[Main Examples#Set Identities|Professor X's Example:]]
2. [[Main Examples#Proving methods|Proof of Identity]]
#### Absorption Laws (One Set "Absorbs" the Other)
- **A ∪ (A ∩ B) = A** - Union absorbs intersection  
- **A ∩ (A ∪ B) = A** - Intersection absorbs union
**Why this works:**
- For the first one: A ∩ B is always a subset of A, so when you union it with A, you just get A back
- For the second one: A ∪ B contains A, so when you intersect with A, you just get A back
#### Complement Laws (Everything and Nothing)
- **A ∪ A' = U** - A set plus everything not in the set equals the universe  
- **A ∩ A' = ∅** - A set intersected with everything not in the set equals nothing (no overlap possible!)
## 2.3
### Functions: Basic Terminology and Types
**What is a Function?**
- A function f from set A to set B assigns each element of A to exactly one element of B  
- Every element in A must be mapped to some element in B  
- Also called mappings or transformations, but we mostly just say "functions"
**Key Terminology You Need to Know:**
- **Domain (A)**: The set of all input values (all X's)  
- **Co-domain (B)**: The set of all possible output values (all possible Y's)  
- **Range**: The set of actual outputs that get mapped to from the domain (subset of co-domain)  
- **Image**: If F(1) = b, then "b is the image of 1 under F"  
- **Pre-image**: If F(1) = b, then "1 is the pre-image of b under F"
**Important Details About Images and Pre-images:**  
- Multiple inputs can map to the same output (like if both 1 and 3 map to b)  
- When finding pre-images, you need to list ALL inputs that map to that output  
- The image of the entire function is just another way to say the range
**Different Ways Functions Can Be Represented:**
1. **Explicit Statement**: Directly tells you what maps to what
    - Example: "a maps to 1, b maps to 2, c maps to 1"
    - No formula needed, just direct assignments
2. **Formula**: Mathematical expression
    - Example: F(x) = x² + 1
3. **Computer Program**: Code that processes inputs to outputs
4. **Relation**: Set of ordered pairs like (1,2), (2,3), (4,5)
    - Can be a function IF each x-value appears only once
    - If you repeat x-values with different y-values, it's NOT a function
**Practice Problem Breakdown:** Domain = set X (the input set), Co-domain = set Y (all possible outputs), Range = only the values actually used as outputs, Pre-image of 2 = which input(s) map to 2, Image of a = what does 'a' map to and F(d) = what does 'd' map to.
#### One-to-One (Injective) Functions
**What it means:** Each value in the range corresponds to exactly ONE element in the domain. No two different inputs give the same output. 
- Think of it like: "Every output has its own unique input".
**Visual Example:** Domain: {a, b, c} → Range: {1, 2, 3} a maps to 2, b maps to 1, c maps to 3. 
- This IS one-to-one because each output (1, 2, 3) comes from only one input
**What breaks it:** If we add element d to domain and d also maps to 3. Now 3 comes from both c AND d → NOT one-to-one anymore!
**Mathematical Definition (Two Ways - Same Thing!):**  
- Way 1: If a ≠ b, then f(a) ≠ f(b)  
- Way 2: If f(a) = f(b), then a = b  
- These are contrapositives - they say the exact same thing!
#### Onto (Surjective) Functions
**What it means:** Every element in the codomain is mapped to by at least one element from the domain. No lonely elements in the codomain! The range equals the codomain
**Visual Example:** Domain: {a, b, c, d} → Codomain: {1, 2, 3, 4} a→1, b→2, c→4, d→3. 
- This IS onto because every element (1, 2, 3, 4) gets hit by something
**What breaks it:** If element 3 in codomain has nothing mapping to it. Then 3 is "lonely" → NOT onto!
**Mathematical Definition:** For all y in codomain, there exists some x in domain such that f(x) = y.
- Translation: Every possible output actually happens!
#### Bijective Functions (The Best of Both Worlds!)
**What it means:** Both one-to-one AND onto. Also called "one-to-one correspondence". Perfect pairing between domain and codomain.
**Key Properties:** Each domain element maps to exactly one codomain element. Each codomain element gets mapped to by exactly one domain element. No extras, no missing pieces, perfect match!
#### [[Main Examples#Functions|Practice Problems]]
**Remember:**
- Range = actual outputs that happen  
- Codomain = all possible outputs we're considering  
- For onto: range must equal codomain!
#### Inverse Functions
**What makes a function invertible?** A function MUST be a bijection to have an inverse. 
- Bijection = both one-to-one AND onto  
	- **One-to-one**: Each element in the domain maps to exactly one element in the range (no repeats)  
	- **Onto**: Every element in the codomain gets mapped to by at least one element from the domain.
**How to write inverse functions:** If f maps x to y, then f⁻¹ maps y back to x  
- The inverse function "undoes" what the original function did. Written as f⁻¹(x) where the -1 is NOT an exponent, just notation for "inverse"
- [[Main Examples#Inverse Functions|Inverse function Examples]]
#### Function Composition
**What is composition?** Combining two functions where the output of one becomes the input of another. Written as (g ∘ f)(x) = g(f(x)) OR g(f(x))  
- **KEY RULE**: Work from the INSIDE OUT! Do f first, then g
**Visual example:** If f maps A to B and g maps B to C. Then g ∘ f maps A directly to C. 
- Example: If f(1) = 6 and g(6) = 10, then g(f(1)) = 10
**Step-by-step example:** Given: f(x) = x + 3 and g(x) = x² - 2. 
- **Finding f(g(1))**: First find g(1): 1² - 2 = -1. Then find f(-1): -1 + 3 = 2
	- So f(g(1)) = 2
- **Creating the composite function:** **f(g(x))**: Substitute g(x) into f(x)
	- f(g(x)) = f(x² - 2) = (x² - 2) + 3 = x² + 1
	- Check: f(g(1)) = 1² + 1 = 2 ✓
	- **g(f(x))**: Substitute f(x) into g(x)
	- g(f(x)) = g(x + 3) = (x + 3)² - 2
	- Expand: x² + 6x + 9 - 2 = x² + 6x + 7
	- Check: g(f(1)) = 1² + 6(1) + 7 = 14 ✓
**Important notes:** f(g(x)) ≠ g(f(x)) in general - order matters! Always work from inside parentheses outward. You can either plug in specific values step-by-step OR create the entire composite function first.
#### Floor Function ⌊x⌋
**What it does**: Rounds DOWN to the largest integer less than or equal to x  
**Memory trick**: The bracket symbol has a "floor" at the bottom  
**Examples**: ⌊2.2⌋ = 2 (rounds down from 2.2 to 2). 
- ⌊-3.7⌋ = -4 (careful with negatives! -3.7 is between -4 and -3, so rounding down goes to -4)
#### Ceiling Function ⌈x⌉
**What it does**: Rounds UP to the nearest integer greater than or equal to x  
**Memory trick**: The bracket symbol has a "ceiling" at the top  
**Examples**: ⌈2.2⌉ = 3 (rounds up from 2.2 to 3)
	- ⌈-3.7⌉ = -3 (rounding up from -3.7 goes to -3)
1. Key Point About Negatives
	**Number line visualization**:
	- For -3.7: it sits between -4 and -3 on the number line
	- Floor function goes LEFT (more negative): -3.7 → -4
	- Ceiling function goes RIGHT (less negative): -3.7 → -3
#### Factorial Function n!
**Definition**: f(n) = n! = product of first n positive integers  
**Formula**: n! = n × (n-1) × (n-2) × ... × 2 × 1  
**Example**: 4! = 4 × 3 × 2 × 1 = 24  
**Important**: Only works for non-negative integers  
**Growth rate**: Gets VERY large VERY quickly
#### Sterling's Formula
**Purpose**: Approximates factorial values when numbers get huge  
**Why it matters**: Factorials grow so fast that we need approximations for large numbers  
**Note**: Professor X says we won't use this much right now, but it's "fantastic" to know
## 2.4
### Sequences: Arithmetic and Geometric
- What is a Sequence? A sequence is just an ordered list of numbers created by a function. The notation "a_n" means the nth term of the sequence. If you have a_n = 2n, then: Write a(0), ..., a(n). 
### Two Ways to Define Sequences
- **Recursive**: Use the previous term to find the next one  
- **Explicit**: Plug in any value of n to find that term directly (this is super important!)
### ARITHMETIC SEQUENCES
- What They Are: You ADD the same number (called common difference "d") each time  
- Pattern: Start with "a", then add d, then add d again, etc. Example: 5, 7, 9, 11, 13... (adding 2 each time)
- $a_{n} = a + d_{n}$
	- a = first term  
	- d = common difference  
	- n = which term you want
- [[Main Examples#Sequences|Arithmetic Sequence Examples]]
### GEOMETRIC SEQUENCES
- You MULTIPLY by the same number (called common ratio "r") each time  
- Pattern: Start with "a", then multiply by r, then multiply by r again, etc. Example: 2, 6, 18, 54... (multiplying by 3 each time)
- $a_{n} = a × r^n$  
	- a = first term  
	- r = common ratio  
	- n = which term you want  
- IMPORTANT: Only the r gets raised to the nth power!
- [[Main Examples#Sequences|Geometric Sequence Examples]]
### Arithmetic vs Geometric
- **Arithmetic**: ADD the same amount each time → a_n = a + dn  
- **Geometric**: MULTIPLY by the same amount each time → a_n = a × r^n
### Recurrence Relations and Iterations
**Definition**: A way to express how to find the next values in a sequence. Think of it like a recipe that tells you how to get the next number using previous numbers.
1. *Two Essential Parts of Every Recurrence Relation*: 
	1. **Part 1: The Equation**: Shows how to get the next term using previous terms. Written as a(n) in terms of one or more previous terms. 
		- Example: a(n) = a(n-1) + 2×a(n-2)
	2. **Part 2: Initial Conditions**: Starting values you need to begin the sequence. Could be one value (like a₀) or multiple values (like a₀ and a₁). Number of initial conditions depends on how many previous terms your equation needs.
	- [[Main Examples#Recurrence Relations and Iterations|Recurrence Relations and Iterations Examples]]
#### The Famous Fibonacci Sequence
**Pattern**: Each number = sum of the two numbers before it  
**Sequence**: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...  
**As recurrence relation**:
- Equation: a(n) = a(n-1) + a(n-2) for n ≥ 2
- Initial conditions: a₀ = 0, a₁ = 1
#### Problem with Recurrence Relations
- **Big issue**: To find the 100th term, you'd need to calculate ALL 99 terms before it! 
- **Solution**: Find a "closed form" or "explicit formula" that lets you jump straight to any term.
- **Example**: Instead of using recurrence, use a(n) = 3 + 6n to find a₁₀₀ = 3 + 6×100 = 603
- [[Main Examples#Iterations Method (Finding Closed Forms)|Iterations Method (Finding Closed Forms)]]
### Summations and Sigma Notation
**Sigma (Σ)** = the Greek letter that means "find the sum"  
- Every time you see Σ, you're adding up terms in a sequence. It's a shorthand way to write long addition problems. 
1. *Parts of Sigma Notation*: **Three ways to write the same thing:**
	- Standard: Σ with limits above and below
	- Alternative 1: Σ with "i=M to N" to the right
	- Alternative 2: Σ with "M ≤ i ≤ N" below  
		- **All three mean exactly the same thing!**
2. Key Components:
	- **a_i** = the general term (what you're adding up)  
	- **i** = the index (tells you which term you're on)  
	- **Lower limit (M)** = where you start counting  
	- **Upper limit (N)** = where you stop counting  
	- **The process**: Start at M, add 1 each time, stop at N
3. *How It Works Step-by-Step*: 
	- Start with i = M (lower limit)  
	- Calculate a_M, then a_(M+1), then a_(M+2), etc.  
	- Keep going until you reach a_N (upper limit)  
	- Add ALL these terms together to get your final sum
- [[Main Examples#Sigma Questions|Sigma Examples]]
### Summation Properties and Formulas
1. **Basic Summation Properties**:  
	1. **Constant Factor Rule**: You can pull constants outside the summation
		- Example: Σ(c × f(k)) = c × Σf(k)
		- Just like with integrals and derivatives!
	2. **Constant Sum Rule**: When summing just a constant, you get that constant times the number of terms
		- Σc = c × n (where you're summing n times)
		- Makes sense: adding C + C + C... n times = n × C
	3. **Sum Splitting**: You can break apart sums of multiple terms
		- Σ(f(k) + g(k)) = Σf(k) + Σg(k)
		- Example: Σ(2k + 3) = Σ(2k) + Σ(3) = 2Σk + Σ3
	4. **Range Splitting**: You can split summation ranges as long as they cover the full range
		- If going from 1 to N, you can split at any point J: Σ₁ᴺ = Σ₁ʲ + Σⱼ₊₁ᴺ
		- **Index Shifting**: You can add/subtract the same value to both limits
		- Useful when formulas start at 0 vs 1
		- But you have to adjust the expression inside accordingly
2. **Key Summation Formulas**
	1. Sum of First N Integers: **Formula**: Σᵢ₌₁ⁿ i = n(n+1)/2
		- **Example**: Sum from 1 to 7
		- By hand: 1+2+3+4+5+6+7 = 28
		- By formula: 7(7+1)/2 = 7×8/2 = 56/2 = 28 ✓
		**Why it works**: Add the sequence twice, once forward, once backward
		- 1+7=8, 2+6=8, 3+5=8, 4+4=8
		- Get 7 eights = 7×8, but we added twice so divide by 2
	2. Sum of Squares: **Formula**: Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6
		- **Example**: Sum of squares from 1 to 4
		- By hand: 1² + 2² + 3² + 4² = 1+4+9+16 = 30
		- By formula: 4(4+1)(2×4+1)/6 = 4×5×9/6 = 180/6 = 30 ✓
	3. Geometric Series: **Formula**: Σₖ₌₀ⁿ ar^k = a(r^(n+1) - 1)/(r-1)
		**Key points**:
		- This is for geometric sequences where each term = a × r^k
		- a = first term, r = common ratio
		- Formula starts at k=0 (watch out for this!
	- [[Main Examples#Sigma Questions|Sigma Properties Examples]]
	- Other Useful Formulas (For Reference): Professor X mentioned these additional formulas you might encounter:
		- Σk³ (sum of cubes)
		- Σk⁴ (sum of fourth powers)
		- Σk⁵ (sum of fifth powers)

---
# #Homework Homework's (3 & 4)


---
# #Discussion Discussions(3 & 4)


---

---
type: class
status: archived
created: 2025-11-20
updated: 2025-11-22
area:
  - "[[Main Examples]]"
  - "[[Finals]]"
  - "[[Material]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Homework"
  - "#Discussion"
next: "[[Chapter - 9]]"
---
# #Textbook Textbook & Videos
## 7.1
### Laplace's Definition & Key Setup
**Sample Space (S)**: All possible outcomes of an experiment (like rolling a die gives you {1,2,3,4,5,6})  
**Event (A)**: One specific outcome we're interested in from the sample space  
**Laplace's Formula**: P(A) = Number of elements in A / Number of elements in S  
**Important**: This only works when all outcomes are equally likely!
[[Main Examples#Basic Examples to Lock This In|Laplace Formula Use]]
### The Six Essential Probability Rules
**Rule 1: Total Probability = 1**  
- All probabilities in a sample space must add up to 1  
- Example: P(heads) + P(tails) = 1/2 + 1/2 = 1 ✓
**Rule 2: Probability Range**  
- Every individual probability must be between 0 and 1 (inclusive)  
- 0 = impossible, 1 = certain
**Rule 3: Complement Rule**  
- P(not A) = 1 - P(A)  
- Sometimes it's easier to calculate the opposite!  
- Example: P(not rolling 3) = 1 - P(rolling 3) = 1 - 1/6 = 5/6
**Rule 4: "At Least One" Rule**  
- P(at least one) = 1 - P(none)  
- This is a special case of the complement rule that saves tons of work!  
- **Example**: Flipping coin 3 times, want P(at least 1 heads)
	- All possible outcomes: HHH, HHT, HTH, HTT, THH, THT, TTH, TTT (8 total)
	- Hard way: Count favorable outcomes = 7 out of 8
	- Easy way: P(at least 1 H) = 1 - P(no heads) = 1 - P(TTT) = 1 - 1/8 = 7/8
**Rule 5: "OR" Rule (Addition)**  
- P(A or B) = P(A) + P(B) - P(A and B)  
- If events can't happen together (disjoint), then P(A and B) = 0 
- **Example**: P(rolling 2 or 4) = P(2) + P(4) - P(2 and 4) = 1/6 + 1/6 - 0 = 1/3 
	- The subtraction part is 0 because you can't roll both 2 and 4 on the same roll
**Rule 6: "AND" Rule (Multiplication)**  
- P(A and B) = P(A) × P(B given A)  
- If events don't affect each other (independent), then P(B given A) = P(B)  
- **Example**: P(rolling 2 then rolling 4) = P(2) × P(4) = 1/6 × 1/6 = 1/36  
	- Rolling a 2 first doesn't change your chances of rolling a 4 next!
> *NOTE*: Always check if your probabilities add up to 1 when dealing with a complete sample space.
### [[Main Examples#|Discrete Probability Practice Problems]]
#### The Monty Hall Problem
1. *The Setup*:
	- 3 doors, 1 has a prize  
	- You pick door 1  
	- Host opens door 3 (not a winner)  
	- Should you switch to door 2?
	- The Answer: YES, ALWAYS SWITCH!:
		- Initial choice probability: 1/3  
		- Switching probability: 2/3  
	- **Why**: If you switch, you win whenever your initial pick was wrong  
	- P(initial pick wrong) = 1 - 1/3 = 2/3  
	- **Key insight**: The host's action gives you information that changes the odds!
#### Key Strategies Professor X Wants You to Remember
-  Use complement rule (1 - P(opposite)) for "at least" problems  
- Multiple correct methods often exist - choose the calculator-friendly one  
- Floor functions are crucial for divisibility problems.
## 7.2
### Probability Theory Fundamentals
**Sample Space (S)**: The set of ALL possible outcomes in an experiment  
**Key Rules for Probability**:
- Each outcome's probability must be between 0 and 1
- ALL probabilities in the sample space must add up to 1
- We're only dealing with finite outcomes (no infinite stuff!)
**Probability Distribution/Model**: Just a fancy way of saying "list all the outcomes and their probabilities"
1. **Non-Equally Likely Events Example**: 
	- **The Biased Coin Problem:** A coin lands on tails TWICE as often as heads. Let P(H) = probability of heads, P(T) = probability of tails.
	- We know: P(T) = 2 × P(H), Since all probabilities add to 1: P(H) + P(T) = 1  
	- Substituting: P(H) + 2P(H) = 1, so 3P(H) = 1 
	- **Answer**: P(H) = 1/3, P(T) = 2/3
2. **Union of Events (Formal Definition)**:
	- **For Pairwise Disjoint Events** (no overlap): P(A ∪ B ∪ C...) = P(A) + P(B) + P(C)...  
		- No need to subtract anything because there's NO overlap!
		**Biased Die Example:** Die where "2" appears twice as often as other numbers (1,3,4,5,6). 
		- Think of it as 7 total "slots": one each for 1,3,4,5,6 and TWO for 2. 
		- P(1) = P(3) = P(4) = P(5) = P(6) = 1/7  
		- P(2) = 2/7  
		- P(even) = P(2) + P(4) + P(6) = 2/7 + 1/7 + 1/7 = 4/7
3. **Conditional Probability**
	- **Formula**: $$P(A|B) = \frac{P(A ∩ B)}{P(B)}$$  
	- **Translation**: "Probability of A given B happened" = "Probability both A and B happened" ÷ "Probability B happened". We're basically shrinking our sample space to only cases where B occurred.
	- **Bit String Example:** 4-bit strings (16 total possibilities: 2⁴)
		- Find: P(at least 2 consecutive zeros | first bit is 0).
		- P(first bit is 0) = 8/16 = 1/2 (half start with 0, half with 1)  
		- P(both conditions) = count strings starting with 0 AND having 2+ consecutive zeros  
		- Valid strings: 0000, 0001, 0010, 0011, 0100 = 5 strings  
		- P(both) = 5/16  
		- **Answer**: (5/16) ÷ (1/2) = 5/8
4. **Independence**
	- **Two events are independent if**: P(A ∩ B) = P(A) × P(B)  
	- Independence means one event doesn't affect the other
	- **Family with Two Children Example:**  
		- Sample space: {BB, BG, GB, GG}  
		- Event A: "two boys" = {BB} → P(A) = 1/4  
		- Event B: "at least one boy" = {BB, BG, GB} → P(B) = 3/4 
		- P(A ∩ B): Both two boys AND at least one boy = {BB} → P(A ∩ B) = 1/4 
		- Check independence: Does 1/4 = (1/4) × (3/4)?  
		- 1/4 ≠ 3/16, so **NOT INDEPENDENT**
### Random Variables and Binomial Distribution
**Definition**: A function that assigns real number values to outcomes in an experiment. Think of it as a way to turn experimental results into numbers we can work with mathematically  
**Example**: If you flip a coin 3 times, the random variable X could represent "number of heads".
[[Main Examples#Random Variables|Random Variables Examples]]
### Binomial Distribution - The Big Picture
**What it is**: A probability distribution based on Bernoulli trials  
**Bernoulli trials**: Experiments with exactly 2 outcomes (success/failure)  
**Examples**:
- Coin flips (heads/tails)
- Pass/fail tests
- Rolling a die where "success" = rolling 2 or 4, "failure" = anything else
1. *Key Components of Binomial Distribution*:
	- **P** = probability of success on each trial  
	- **q** = probability of failure = 1 - P  
	- **n** = number of trials 
	- **k** = number of successes we want
### The Binomial Formula
**Formula**: $$P(X = k) = C(n,k) × P^k × q^{(n-k)}$$
**What each part means**:
- C(n,k) = number of ways to arrange k successes in n trials
- P^k = probability of k successes
- q^(n-k) = probability of (n-k) failures
- [[Main Examples#Binomial Distribution|Binomial Distribution Examples]]
### Key Takeaways for the Exam
- **Always check that probabilities sum to 1** in any probability distribution.
- **For union problems**: Add probabilities if events don't overlap, subtract intersection if they do  
- **For conditional probability**: Remember you're working with a smaller sample space  
- **Always identify**: n (trials), P (success probability), k (desired successes) 
- **Biased scenarios**: Set up equations using the given relationships (like "twice as often")
- **For "exactly" problems**: Use binompdf or the binomial formula directly  
- **For "at least" or "at most" problems**: Consider using the complement rule (1 minus the opposite).
- Important Formulas to Remember: 
	- **Binomial probability**: $P(X = k) = C(n,k) × P^k × (1-P)^{(n-k)}$
	- **Complement rule**: P(A) = 1 - P(not A)  
	- **Probability of failure**: q = 1 - P

---
# #Homework Homework's (8 & 9)


---
# #Discussion Discussions (8 & 9)


---


# Problem Statement

Consider the sentence:
"Heads, I win. Tails, you lose."

Design a propositional knowledge base (KB) that represents the sentence (create the propositions and rules required). Then, use propositional resolution to prove that "I always win."

---

### **1. Define the Objects**
To represent the problem using propositional logic:
- **H**: Heads
- **T**: Tails
- **I**: I win
- **Y**: You win

These are the basic variables used to construct the knowledge base.

---

### **2. State the Rules**
The statement "Heads, I win. Tails, you lose" translates into the following logical rules:
- **Rule 1**: If Heads (H) happens, then I win (I). 
  - \( H \Rightarrow I \)
- **Rule 2**: If Tails (T) happens, then you don't win (\( \neg Y \)).
  - \( T \Rightarrow \neg Y \)

These two rules capture the essence of the statement.

---

### **3. Add Implicit Knowledge**
We need to explicitly state what is implicit in the problem:
- **Heads and Tails are mutually exclusive**: Both cannot happen simultaneously.
  - \( H \oplus T \), which means:
    - \( H \vee T \): Either heads or tails happens.
    - \( \neg(H \wedge T) \): Heads and tails cannot both happen.

Similarly, if "I win" (\( I \)) happens, then "you win" (\( Y \)) cannot, and vice versa:
- \( I \oplus Y \): Either I win or you win, but not both.

---

### **4. Convert to CNF (Conjunctive Normal Form)**
To use resolution, we need to convert all statements to **CNF** (a conjunction of disjunctions):

#### Rule 1: \( H \Rightarrow I \)
- Equivalent to \( \neg H \vee I \).

#### Rule 2: \( T \Rightarrow \neg Y \)
- Equivalent to \( \neg T \vee \neg Y \).

#### Mutually Exclusive Rules:
- \( H \vee T \): Either heads or tails happens.
- \( \neg H \vee \neg T \): Heads and tails cannot both happen.

#### \( I \oplus Y \) (Exclusivity of winning):
- Equivalent to \( (I \vee Y) \wedge (\neg I \vee \neg Y) \).

So, the final CNF becomes:
1. \( \neg H \vee I \)
2. \( \neg T \vee \neg Y \)
3. \( H \vee T \)
4. \( \neg H \vee \neg T \)
5. \( I \vee Y \)
6. \( \neg I \vee \neg Y \)

---

### **5. Prove by Contradiction**
We want to prove that \( I \) (I win) is always true. To do so, we assume \( \neg I \) and resolve the clauses to derive a contradiction:

#### Steps:
1. Add \( \neg I \) (assume I do not win) to the knowledge base.
2. Start resolving the clauses step-by-step:
   - Combine \( \neg T \vee \neg Y \) and \( H \vee T \) to get \( H \vee \neg Y \).
   - Combine \( \neg H \vee I \) and \( H \vee \neg Y \) to get \( I \vee \neg Y \).
   - Combine \( \neg I \) (assumed) and \( I \vee \neg Y \) to get \( \neg Y \).
   - Combine \( \neg Y \) and \( I \vee Y \) to get \( I \).

3. \( \neg I \) and \( I \) result in a **contradiction**.

Thus, the assumption \( \neg I \) is false, proving that \( I \) (I win) must always be true.

---

### **Conclusion**
By formal logic and resolution, the statement **"Heads, I win. Tails, you lose"** is always valid, as I always win regardless of whether the coin lands on heads or tails.

---

### **Detailed Explanation of Step 5 (Prove by Contradiction)**

The goal in Step 5 is to prove that \( I \) (I win) is always true using **proof by contradiction**. This involves the following process:

1. **Assume the negation of what you want to prove**:
   - We want to prove that \( I \) (I win) is true.
   - To use proof by contradiction, assume \( \neg I \) (I do NOT win).

2. **Add \( \neg I \) to the knowledge base**:
   - The knowledge base (KB) consists of all the CNF clauses derived in Step 4:
     1. \( \neg H \vee I \)
     2. \( \neg T \vee \neg Y \)
     3. \( H \vee T \)
     4. \( \neg H \vee \neg T \)
     5. \( I \vee Y \)
     6. \( \neg I \vee \neg Y \)
   - Now, \( \neg I \) is explicitly added to the KB.

3. **Resolve clauses step-by-step**:
   - **Resolution** is a formal rule of inference in propositional logic. It works by combining two clauses that contain complementary literals (e.g., \( A \) and \( \neg A \)), eliminating the complementary literals, and producing a new clause. 

   - The goal is to eventually derive an empty clause \( \{\} \), which represents a **contradiction**.

---

### **Detailed Clause Resolution**

#### **Step 1: Resolve \( \neg T \vee \neg Y \) with \( H \vee T \)**
From the KB:
- \( \neg T \vee \neg Y \): If tails don't happen, you don't win.
- \( H \vee T \): Either heads or tails happens.

Resolve \( \neg T \) in the first clause with \( T \) in the second:
\[
(\neg T \vee \neg Y) \wedge (H \vee T) \implies H \vee \neg Y
\]
New clause: \( H \vee \neg Y \).

---

#### **Step 2: Resolve \( H \vee \neg Y \) with \( \neg H \vee I \)**
From the KB:
- \( H \vee \neg Y \): If heads happen, you don't win (\( \neg Y \)).
- \( \neg H \vee I \): Either heads don't happen, or I win.

Resolve \( H \) in the first clause with \( \neg H \) in the second:
\[
(H \vee \neg Y) \wedge (\neg H \vee I) \implies I \vee \neg Y
\]
New clause: \( I \vee \neg Y \).

---

#### **Step 3: Resolve \( I \vee \neg Y \) with \( \neg I \)**
From the KB and assumption:
- \( I \vee \neg Y \): Either I win (\( I \)) or you don't win (\( \neg Y \)).
- \( \neg I \): I do NOT win.

Resolve \( I \) in the first clause with \( \neg I \) in the second:
\[
(I \vee \neg Y) \wedge \neg I \implies \neg Y
\]
New clause: \( \neg Y \).

---

#### **Step 4: Resolve \( \neg Y \) with \( I \vee Y \)**
From the KB:
- \( \neg Y \): You don't win.
- \( I \vee Y \): Either I win (\( I \)) or you win (\( Y \)).

Resolve \( Y \) in the second clause with \( \neg Y \) in the first:
\[
(I \vee Y) \wedge \neg Y \implies I
\]
New clause: \( I \).

---

#### **Step 5: Derive a Contradiction**
Now we have:
- From the resolution process: \( I \) (I win is true).
- From the assumption: \( \neg I \) (I win is false).

These two statements (\( I \) and \( \neg I \)) contradict each other, resulting in a **contradiction**.

---

## **Conclusion**
Since the assumption \( \neg I \) leads to a contradiction, it must be false. Therefore, \( I \) (I win) is always true.

This formal proof demonstrates that no matter what happens (heads or tails), **I always win**.

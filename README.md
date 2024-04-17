Problem: [L-Systems]: L-systems are used to model naturally occurring patterns in nature such as growth of trees, growth of multicellular organisms, fractals etc. by recursively applying a set of simple grammar rules over a set of variables starting with an Axiom.

For example: Growth of Algae in L-systems would be modeled as.
variables : A B
constants : none
axiom  : A {starting character string}
rules  : (A → AB), (B → A)
which produces:
n = 0 : S=A
n = 1 : S=AB
n = 2 : S=ABA
n = 3 : S=ABAAB
n = 4 : S=ABAABABA
n = 5 : S=ABAABABAABAAB

Given the upper bound ‘n’, design a class D for L-systems with variables, axiom and rules. 

Q1. Write a function ‘produce’ that takes in the object of ‘D’ and ‘n’ and returns the L-systems string ‘S’.
Q2. Test your code using the following L-system (Cantor fractal) where n=3 and tell the answer:
variables : A B
constants : none
start  : A
rules  : (A → ABA), (B → BBB)

Q3. Tell the space and time complexity. How can you optimize your solution? 

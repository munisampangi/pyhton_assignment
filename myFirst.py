# for l-systems 
"""Q1 Write a function ‘produce’ that takes in the object of ‘D’ and ‘n’ and returns the L-systems string ‘S’"""

# ans:

def produce(D, n):
    axiom = D['axiom']
    variables = D['variables']
    rules = D['rules']

    for _ in range(n):
        string = ''
        for symbol in axiom:
            if symbol in rules:
                string += rules[symbol]
            else:
                string += symbol
        axiom = string
    return axiom
    
D = {
    'variables': 'AB',
    'axiom': 'A',
    'constants':"none",
    'rules': {
        'A': 'AB',
        'B': 'A'
    }
}
# n=int(input("enter the n"))

S = produce(D, 5)
print(S)

'''Q2 Test your code using the following L-system (Cantor fractal) where n=3 and tell the answer:
 variables : A B
 constants : none
 start  : A
 rules  : (A → ABA), (B → BBB)

Replace the D object with the specified variables,axioms,rules,constants in Q1 to get desired output'''


''' Q3. Tell the space and time complexity. How can you optimize your solution? '''
# ans:

'''
TIME COMPLEXITY
The time complexity of the 'produce' function  depends on the number of times it looping, which is determined by  parameter n.
In the function, there's a loop that iterates n times. Within each iteration, another loop iterates over each character in the string S. 
Now denote the length of String S as m.
then the time complexity of the function is O(n * m).
'''
'''
SPACE COMPLEXITY
The space complexity of the function is dominated by the storage of the L-system string S and the rules dictionary D.
and the function doesn't create any additional data structures that grow with the input size, the space complexity is  determined by the
 size of the input L-system string and the size of the rules dictionary.
Now  denote the size of the rules dictionary as r.
Therefore, the space complexity is O(m + r), 
where m is the length of the L-system string and r is the size of the rules dictionary.
'''

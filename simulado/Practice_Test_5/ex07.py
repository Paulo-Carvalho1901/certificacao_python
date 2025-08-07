"""
Question 07: What is the expected output of the folloing code?

A: $
B: $$$
C: The  result to an error message
C: $$

A resposta é é a C: $$
"""

price = 1 + 1 // 2 * 3

if price > 0:
    print('$$')
elif price > 1:
    print('$$$')
else:
    print('$')

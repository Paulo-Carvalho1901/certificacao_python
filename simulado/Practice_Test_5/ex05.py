"""
Question 05: What is the expeted output of the code bellow:

A: 1
B: The code outputs a syntax error
C: 2
D: 3

A resposta correta é C: 2
"""

number = -1
for i in range(1, 3):
    for j in range(1, 2):
        if i == j:
            number += 1
    else:
        number += 1
print(number)
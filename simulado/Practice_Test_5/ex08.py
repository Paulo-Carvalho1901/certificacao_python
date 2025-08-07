"""
Question 08: What will be the output of the following code?

A: The code enters an infinite loop:
B: 4
C: 5
D: 3

A resposta é B: 4
"""

number = 3
for i in range(5):
    if i % 2 == 1:
        number += 1
else:
    number -= 1

print(number)
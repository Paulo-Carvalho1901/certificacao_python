# Question 01: What is the expcted output of the following code?

list_one = [2, 3]
list_two = list_one[:]

list_two.append(3)
print(list_one[-1])


"""
Answers
A: 3 
B: 1
c: 2
D: The code raises an exception and outputs nothing.


A resposta correta seria a A, pois a list_one ultimo elemento é o 3
"""
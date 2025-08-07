"""
Question 10: Which of the following evaluate to FALSE:

A resposta correta seria C: my_data.index(True) == 0

"""

my_data = [20, 1.1, True]

# print(len(my_data) == my_data[20])
print(len(sorted(my_data)) == len(my_data))
print(my_data.index(True) == 0)
print(my_data[-2] == 1.1)
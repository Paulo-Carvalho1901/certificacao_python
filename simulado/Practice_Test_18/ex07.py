# What is the output of the following snippet
# user enters two lines containing 11 and 4 respectively?

x = int(input())
y = int(input())

x = x % y # resto da divisao de 11 % 4 = 3
x = x % y # resto da divisao de 3 % 4 = 3
y = y % x # resto da divisao de 4 % 3 = 1
print(y) # resultado é 1

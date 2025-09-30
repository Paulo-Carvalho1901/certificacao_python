# What is the expected output of the following code ?

def func(n):
    return total - n # total não está definida dentro da função, então o Python procura no escopo global.


total = 4

total = func(2)
# Pega o valor de total (que é 4).
# Calcula 4 - 2 = 2.
total = func(1)
# func(1) = total - 1 = 2 - 1 = 1.

print(total) # total 1

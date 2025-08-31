# what will be the sum of all elements in the list 
# after the fallowing operation?

numbers = [0, 1, 2] 
numbers.insert(0, 1) # na posição 0 inserindo 1
print(numbers) # a nova lista fica [1, 0, 1, 2]
del numbers[1] # deletamos na posiçao 1 da lisra que seria o 0

print(numbers) # assim nossa lista fica [1, 1, 2] a soma seria 4

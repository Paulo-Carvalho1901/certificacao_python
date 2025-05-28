# numbers = [1, 2, 3, 4, 5]
# numbers = []
# for i in range(1, 101):
#     numbers.append(i)
# print('The size list is:\n', numbers)


# nomes = []
# numbers = []
# for valor in range(1, 10):
#     numbers.append(valor)
# print(numbers)

# while True:    
#     name = input('Digite seu nome: ')
#     nomes.append(name)
#     print(nomes)

#     if name == 'Parar':
#         break

numbers = [i for i in range(1, 101)]
print(numbers)
print()
numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)

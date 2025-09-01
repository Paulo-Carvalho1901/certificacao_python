# Qual é a saída esperada do código a seguir?

list1 = [1, 3]
# aponta para mesmo lugar na memoria
list2 = list1
print()

print(id(list1))
print(id(list2))
list1[0] = 4
print(list2)
##############################################################

c1 = [1, 3]
# aponta para lugares diferentes na memeria
c2 = c1[:]
print()

print(id(c1))
print(id(c2))
c1[0] = 4
print(c2)
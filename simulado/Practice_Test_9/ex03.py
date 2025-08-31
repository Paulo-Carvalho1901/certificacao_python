# what is true about the following code shippet?

# Quando a list2 recebe a list1[:] elas estão apontando para lugares diferentes na memoria
list1 = [1,2,3]
list2 = list1[:]

print(id(list1))
print(id(list2))

print()

# Nesse exemplo aponta para mesmo lugar na memoria
c1 = [2, 3,4]
c2 = c1

print(id(c1))
print(id(c2))
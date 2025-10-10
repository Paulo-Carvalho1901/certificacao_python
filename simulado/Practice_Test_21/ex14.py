# What will be the output of the following code?

tup_a = (0, 1, 2) 
tup_b = (2, 3, 4)
list_c = []
for el in tup_a: # para cada elemento da tup_a [0, 1, 2]
        if el not in tup_b: # para cada elemento que nao esta tup_b append lista_c
                list_c.append(el) # add esse valor na lista_c
print(list_c) # [0, 1]

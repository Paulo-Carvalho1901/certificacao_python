# which of the following statement(s) is/are true?


"""
Se list1 for inicializada como [10, 20, 30], então o que acontece com o código list2 = list1[-3:-1]? Vamos analisar:

list1[-3]: O terceiro elemento a partir do final é o número 10.
list1[-1]: O último elemento é o número 30.
Como o fatiamento vai do índice inicial (inclusive) até o índice final (exclusive), list2 vai conter apenas o elemento correspondente ao índice -3.

Portanto, se list1 = [10, 20, 30], então list2 será [10, 20].

"""

#        0  1  2
#       -3 -3 -1
list1 = [1, 2, 3]
list2 = list1[-3:-1]

print(list1)
print(list2)
print()
print(id(list1))
print(id(list2))

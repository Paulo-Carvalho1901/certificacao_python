# Qual é o resultado do seguinte snippet?

dict = {}
dict['1'] = (1, 2)
dict['2'] = (2, 1)

for x in dict.keys():
    print(dict[x][1], end='')
    
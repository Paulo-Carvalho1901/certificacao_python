# what will be the output of the following code?

tennis_ranking = {
    1: 'Asheight Barty',
    2: 'Naomi Osaka',
    3: 'Simona Halep'
}

# Propriedade keys() seleciona apenas os valores
for key in tennis_ranking.keys():
    # nesse trecho do código estamos selecionado apena a primera letra da string
    tennis_ranking[key] = tennis_ranking[key][0]
print(tennis_ranking[1]*2)

# print(tennis_ranking.values())
numbers = [1, 2, 3, 4]
contries = ['UK', 'US', 'Germany']
contries = [1, 'UK', 2, 'US']
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0][0])
print(cells[1][1])

# for x in cells:
#     print('elements:', x)

# iteração em lista aninhadas
# for x in cells:
#     for y in x:
#         print('Elements:', y)
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cells in row:
        print(cells, '', end='')
    print()

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)

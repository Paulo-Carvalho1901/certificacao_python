# top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houton', 'Phoenix']

# # Iterando com a lista item por item
# for city in top_cities:
#     print('Current city', city)

# top_cities = ['New York', 'Los Angeles', 'Chicago', 'Houton', 'Phoenix']

# # Iterando com a lista item por item
# for city_index in range(len(top_cities)):
#     print('Current index', city_index, '| Current city', top_cities[city_index], )

spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending

print('The monet spending is: ', sum)

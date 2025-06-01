city_1 = ('London', 'UK', 8.90)
city_2 = ('Canberna', 'Australia', 0.4)
city_3 = ('Algiers', 'Algerie', 3.9)
capitals = [
        ('London', 'UK', 8.90),
        ('Canberna', 'Australia', 0.4),
        ('Algiers', 'Algerie', 3.9) 
    ]

for capital in capitals:
    print('Name:', capital[0], 'Country:', capital[1], 'Population:', capital[2])

user_data = ('John', 'America', 1964, [77.0, 78.2, 77.51])
user_data[3].append(79.6)
print(user_data)
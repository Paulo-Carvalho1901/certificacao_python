user_data = ('Paulo', 'Andreia', 'Davi')
# print(len(user_data))

if 'Bob' in user_data:
    print('Bem vindo você está na lista.')
else:
    print('Me desculpe seu nome não está na lista.')

for nome in user_data:
    print(nome)

user_data_soma = ('Paulo', 'Andreia', 'Davi') + ('Maria', 'Pedro')
print(user_data_soma)
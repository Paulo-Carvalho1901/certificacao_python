name_original = 'Paulo' # nesse trecho atribuimos uma name a variavel name_original
name_new = name_original # Aqui atribuimos a variavel name_new o valor da variavel original
name_original = 'Andreia' # aqui alteramos a variavel original
print(name_original, name_new) # e vimos que a variavel name_new não foi alterada
print()

# com coleção como lista altera em ambos os lugares
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = 5
print('Original:', list_original, '\nNew:', list_new)
print()
# Lista com fatiamento
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = 5
print('Original:', list_original, '\nNew:', list_new)
print()
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = 5
print('Original:', list_original, '\nNew:', list_new)
print()

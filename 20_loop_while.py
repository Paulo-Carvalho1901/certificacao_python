# conte = 1
# while conte < 11:
#     print(conte)
#     conte += 1
# print('Acabou!')

secret_number = 14
print('(=====SECRET NUMBER=====)')
print()
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number. ')


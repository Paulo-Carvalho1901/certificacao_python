# Joining multiple conditions

# Operator and

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'German':
    print('You can apply for a German student exchange programme')
else:
    print('Sorry, you do not qualify')

# Operator or

user_country = input('What is your country? ')

if user_country == 'Sweden' or user_country == 'Denmar' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange programme')
else:
    print('Sorry, you do not qualify')

# Operator not

user_country = input('Where do you come from.')
if not user_country == 'Germany':
    print('You are not from Germany')
else:
    print('You are from Germany')

# Exemplo

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germany' and user_country < 25 or user_country == 'Germany' and user_age:
    print('You qualify! ')
else:
    print('You don\'t qualify.')

"""
1. not
2. and
3. or
"""


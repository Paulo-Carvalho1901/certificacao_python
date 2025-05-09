user_age = int(input('what is your age? '))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify.')
elif user_age == 30:
    print('You are exctly 30 years old')
    print('You will need to meet additional conditions to quilify')
else:
    print('You are 30 years old younger')
    print('Congratulations, you qualify')

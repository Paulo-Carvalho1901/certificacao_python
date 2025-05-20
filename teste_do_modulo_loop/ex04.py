# What would be the output of this code if the user tried to enter 3 in the console?

choice = int(input('Pick a number: '))
if choice == 3:
    print('Good choice')
elif choice == 4:
    print('You could have chosen better')
else:
    print('No luck this time')
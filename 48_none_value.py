print()
input()
len()

x = None 

if x:
    print('None is True')
elif x is False:
    print('None is False')
else:
    print('None is not True, os False, None is just None')

x = None
if x is None:
    print(' Yes')
if x == None:
    print('it does')


def greet():
    print('Hello')

x = greet()
print(x)
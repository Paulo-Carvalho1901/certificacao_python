# What will be the output when the user provides the number 0?

num = int(input('give a number: '))
if num > 0:
    if num < 5:
        print('1')
    else:
        print('2')
else:
        if num < -1:
                print('3')
        else:
                print('4')
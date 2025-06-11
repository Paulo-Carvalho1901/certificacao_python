if True:
    print('hooray')

try:
    value = int(input('Enter an integer: '))
    print('The inverso of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverso.')
except ZeroDivisionError:
    print('You provided 0 an division by 0 is not possible, sorry')
except:
    print('Something strange happened here, Sorry')
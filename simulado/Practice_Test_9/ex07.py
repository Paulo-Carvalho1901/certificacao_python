# what will be the output of the following code?

val = input('Provide a number: ')

try:
    print(val/val)
except TypeError:
    print('a')
except ValueError:
    print('b')
except ZeroDivisionError:
    print('c')
except:
    print('d')

# a resposta seria a ecessao de TypeError por o retorno de um input é sempre str
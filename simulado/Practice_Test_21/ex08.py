# What will be the output of the following program when the user enters the letter a?

try:
  val = int(input('Provide a number: '))
  print(val/val)
except TypeError:
  print('a')
except ValueError:
  print('b')
except ZeroDivisionError:
  print('c')
except:
  print('d')
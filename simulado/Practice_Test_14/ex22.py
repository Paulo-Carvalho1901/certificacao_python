# What will be the output of the following code ?

try:
    1/0
except ArithmeticError:
    print("It is wrong")
except ZeroDivisionError:
    print("Any number cannot be divided by zero")
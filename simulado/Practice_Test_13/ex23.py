# what is the expected output of the following code?

def func(a):
    if a == 0:
        return 0
    else:
        return a * func(a - 1)
print(func(2))

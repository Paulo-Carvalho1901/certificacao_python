# what will be the output of the following code?

def first(x):
    return x ** x
def second(x):
    return first(x) + first(x)
print(second(3))

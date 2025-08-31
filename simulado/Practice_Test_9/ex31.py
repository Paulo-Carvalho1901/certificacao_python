# what will be the output after the following code?

def func(x):
    for i in range(4):
        yield i
print(list(func(6)))


# what is expected bahavior of the following snippet?

my_string = 'abcdef'


def fun(s):
    del s[2]
    return s

print(fun(my_string))

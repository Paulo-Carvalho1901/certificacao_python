# what is the expected output of the following snippet?

a = True
b = False

a = a or b # True
b = a and b # False
a = a or b # True

print(a, b)

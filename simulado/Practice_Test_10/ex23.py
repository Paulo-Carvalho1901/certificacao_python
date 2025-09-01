# what will be the output after the
# following code is executed?

x = 10
def change():
    global x
    x += 10
    print(10 + x)
print(x)
change()
print(x)
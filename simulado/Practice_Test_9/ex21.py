# what will be the output of the following code?

def chack(x):
    if (x[0] == x[-1]):
        return True
    else:
        return False
    
print(chack([10, 20, 30, 40, 10]))
print(chack([40, 20, 30, 40, 10]))

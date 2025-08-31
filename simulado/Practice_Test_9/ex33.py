# what will be the output after the following code?

def func(num):
    if num % 2 == 0:
        return True
    else:
        return False
#        False   or  Truw  = True   
print(not func(2) or func(2))
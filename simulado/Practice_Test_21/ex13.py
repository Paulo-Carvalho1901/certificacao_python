# What will be the output of the following code?

def boo(x):
        if x == 1:
                return x
        return x * boo(x-1)
 
print(boo(3))
# função de recursividade de função
# x! 3 = 3! 3 * 2 * 1 = 6

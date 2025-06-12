# What will be the output of the following code?

def func(a):
   global b
   b = a + a
   return b
 
b = 10
print(func(13))
print(b)

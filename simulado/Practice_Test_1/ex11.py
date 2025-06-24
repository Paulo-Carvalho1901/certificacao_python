# What is the expected output of the following code ?

def func(n):

   if n ==0:

        return 0

   else:

       return n * func(n-1)

print(func(3))
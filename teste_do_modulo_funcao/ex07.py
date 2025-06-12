# What will be the output of the following code?

def func(x):
  if x == 0:
    return 0
  return x + func(x - 1)
 
print(func(3))
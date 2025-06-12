# What will be the output of the following code?

def numerical():
  for i in range(10):
    yield i%2
 
for x in numerical():
  print(x, end='-')
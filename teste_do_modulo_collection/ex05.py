# What is the output of the following code?

values = [[3 - x for x in range(2)] for y in range(5)]
 
sum = 0.0
for row in values:
  for cell in row:
    sum += cell
 
print(sum)
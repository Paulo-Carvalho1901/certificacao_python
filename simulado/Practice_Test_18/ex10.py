# what is the following snippet if the user
# enters two lines containing 2 and 4 respectively?

x = int(input()) # x 2 
y = int(input()) # y 4

x = x // y # x = 2 // y = 4 = 0
y = y // x # aqui da um erro pois nao se pode dividir um numero por zero

print(y)

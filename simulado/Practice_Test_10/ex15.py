# What happens when following code runs ?

j  = 1

for i in range(-1, 1):
    if 3 * i < 6:
        j+=2
else:
    j+=3

print(j)
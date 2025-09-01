# what happend when a user runs the following code?

angle = 0

for i in range(5): # (0, 1, 2, 3, 4)
    if i % 2 == 1:
        angle += 1
else:
    angle -= 1
print(angle)

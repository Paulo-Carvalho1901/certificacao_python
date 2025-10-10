# What happens when the user runs the following code?

speed = 0
while speed < 30:
    speed *= 2
    if speed > 10:
        continue
    print('*', end='')
else:
    print('*')
# loop infinito

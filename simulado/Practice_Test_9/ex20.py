# How many hash tags (#) will be printed after the following snippet?

counter = 0
while counter < 8:
    counter += 2
    if counter % 2 == 0:
        continue
    print('#')

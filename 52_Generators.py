def get_numbers():
    for i in range(1, 4):
        yield i
    
generator = get_numbers()
print(next(generator))
print(next(generator))
print(next(generator))

for x in get_numbers():
    print(x)


numbers = list(get_numbers())
print(numbers)

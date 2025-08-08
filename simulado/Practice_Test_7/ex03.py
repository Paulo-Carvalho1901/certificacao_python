def sample(value):
    return total + value

total = 0
new_total = sample()
new_total = sample(total)
print(total)

answers = (True, False, True, False)
selectoin = answers[2:]
points = 0
print(selectoin)
print(selectoin[-1:])
for answer in selectoin[-1:]:
    if answer:
        points += 1
print(points)

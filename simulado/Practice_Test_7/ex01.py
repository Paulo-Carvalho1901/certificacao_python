answers = (True, False, True)
selection = answers[2:]
points = 0
for answer in selection[-1:]:
    if answer:
        points += 1
print(points)

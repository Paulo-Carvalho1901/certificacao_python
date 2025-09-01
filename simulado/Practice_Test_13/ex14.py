# what is the expected result of the code bellow?

answeres = (True, False, True)
selection = answeres[2:]
points = 0
for answere in selection[-1:]:
    if answere:
        points += 1
print(points)

print(answeres[-1:])
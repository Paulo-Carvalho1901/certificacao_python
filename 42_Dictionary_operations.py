grades = {}
grades['Paulo'] = 'A-'
grades['Davi'] = 'B'
print(grades)
grades['Davi'] = 'A'
print(grades)

grades.update({'Paulo': 'A'})
print(grades)

print(len(grades))


if 'Paulo' in grades:
    print('Paulo got:', grades['Paulo'])

del grades['Paulo']
print(grades)

grades = {}
grades['Paulo'] = 'A-'
grades['Davi'] = 'B'

for el in grades:
    print(el)

for el in grades.keys():
    print(el)

for el in grades.values():
    print(el)

for person, grade in grades.items():
    print(person, 'got', grade)
    

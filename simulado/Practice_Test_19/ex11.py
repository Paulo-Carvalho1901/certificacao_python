# what value will be assigned the x variable

z = 10
y = 0

x = y < z and z > y or y > z and z < y
#   T         T        F         F 
#       T           or      F = False
print(x)
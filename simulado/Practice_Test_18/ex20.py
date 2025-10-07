# what is the output of the following snippet?

# my_list = [0, 1, 2, 3]
# x = 1
# for elem in my_list:
#     x *= elem
# print(x)

my_list = [0, 1, 2, 3]
x = 1
for elem in my_list:
    x *= elem
    print(f"elem = {elem}, x = {x}")
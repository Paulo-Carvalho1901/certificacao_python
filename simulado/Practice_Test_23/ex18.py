# What is the output of the following snippet?

my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
# What will be the output of the following code?

my_list = ['aaa', 'bbb', 'ccc']
 
def do(my_list):
   del my_list[1]
   my_list[1] = 'aaa'
 
do(my_list)
print(my_list)
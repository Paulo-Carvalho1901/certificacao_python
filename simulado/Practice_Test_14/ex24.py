"""
You need to print Inverted Triangle Pattern like below :

*****
****
***
**
*
Choose the corresponding code that will print the above pattern

"""

def inverted_triangle(height):
    for i in range(height, 0, -1):
        print("*"*i)
inverted_triangle(5)
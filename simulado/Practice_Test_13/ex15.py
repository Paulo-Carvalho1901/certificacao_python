# what is the output of the code bellow?

def combine(height, width=10, depth=0, is_4D=False):
    return (is_4D, width, height, depth)
print(combine(height = 1, depth = 5)[3])

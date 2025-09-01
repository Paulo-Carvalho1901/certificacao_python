# what is the output of the code bellow?

def combine(height=9, width, depth=0, is_4D=False):
    return (is_4D, width, height, depth)
print(combine(width=1, depth=20)[3])

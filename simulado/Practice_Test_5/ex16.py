def combine(height=9, width, depth=0, is_4D=False):
    return (is_4D, width, height, depth)
print(combine(height=1, depth=20)[3])
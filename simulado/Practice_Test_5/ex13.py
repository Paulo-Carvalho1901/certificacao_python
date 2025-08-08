def combine(height, width=10, depth=0, is_4d=False):
    return (is_4d, width, height, depth)
print(combine(height=1, depth=5)[3])
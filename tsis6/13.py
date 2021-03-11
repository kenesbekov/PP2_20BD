def pascal_triangle(n):
    row = [1]
    y = [0] # for validate working zip [1, 1, 0] + [0, 1, 1] = [1, 2, 1]
    #        (1, 0), (1, 1), (0, 1)     l  l  l     r  r  r   l+r l+r l+r
    for _ in range(n):
        print(row)
        row = [l+r for l,r in zip(row+y, y+row)]

pascal_triangle(int(input())) 
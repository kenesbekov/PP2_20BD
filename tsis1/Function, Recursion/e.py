def IsPointInCircle(x, y, xc, yc, r):
    return 1 if ((xc - x) ** 2 + (yc - y) ** 2) ** (1 / 2)<=r else 0
print('YES' if IsPointInCircle(float(input()),float(input()),float(input()),float(input()),float(input())) else 'NO')

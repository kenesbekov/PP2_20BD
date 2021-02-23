import math
def IsPointInSquare(x, y):
    return abs(x)+abs(y)<=1
print('YES' if IsPointInSquare(float(input()),float(input())) else 'NO')
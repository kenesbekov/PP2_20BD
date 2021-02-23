def IsPointInSquare(x, y):
    return 0 if x>1 or x<-1 or y>1 or y<-1 else 1
print('YES' if IsPointInSquare(float(input()),float(input())) else 'NO')
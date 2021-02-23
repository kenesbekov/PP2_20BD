a = list(map(int, input().split()))
print(*([x for x in a if x>0] + [0]*a.count(0)))
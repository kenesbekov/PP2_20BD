n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a.insert(i, a.pop())
print(*a)

n, m = map(int, input().split())
a, b = set(), set()
for i in range(n):
    a.add(int(input()))
for i in range(m):
    b.add(int(input()))
print(len(a&b))
print(*sorted(a&b, key = int))
print(len(a-b))
print(*sorted(a-b, key = int))
print(len(b-a))
print(*sorted(b-a, key = int))




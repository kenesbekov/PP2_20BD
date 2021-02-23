n, a, b, c, d = map(int, input().split())
li = []
for i in range(n):
    li.append(i+1)
for i in range(n):
    if i == b-a:
        break
    li.insert(i+a-1, li.pop(b-1))
for i in range(n):
    if i == d-c:
        break
    li.insert(i+c-1, li.pop(d-1))
print(*li)
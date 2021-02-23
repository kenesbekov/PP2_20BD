n = int(input())
a = list(map(int, input().split()))
b, cnt = [], 0
for x in a:
    if x not in b:
        b.append(x)
        cnt+=1
print(cnt)
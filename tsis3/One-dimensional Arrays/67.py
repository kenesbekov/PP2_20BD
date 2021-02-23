n = int(input())
a = list(map(int, input().split()))
ok = 0
for i in range(1,n):
    if (a[i-1]<0 and a[i]<0) or (a[i-1]>=0 and a[i]>=0):
        ok = 1
        break
print('YES' if ok else 'NO')
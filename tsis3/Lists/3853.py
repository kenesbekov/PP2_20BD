a = list(map(int, input().split()))
k = int(input()) % len(a)

if k>0:
    print(*a[-k:], end=" ")
    print(*a[0:-k])
else:
    k = -k
    print(*a[k:], end=" ")
    print(*a[0:k])

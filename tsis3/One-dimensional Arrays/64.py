n = int(input())
a = list(map(int, input().split()))
[print(a[x], end=' ') for x in range(n) if a[x]%2==0]
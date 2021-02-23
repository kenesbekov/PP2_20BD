n = int(input())
a = list(map(int, input().split()))
k = int(input())
for i in range(n):
    if k>a[i]:
        print(i+1)
        exit()
print(n+1)
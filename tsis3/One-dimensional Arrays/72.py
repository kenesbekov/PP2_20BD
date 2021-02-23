n = int(input())
a = list(map(int, input().split()))
max = float('-inf')
for i in a:
    if i>max:
        max = i
print(max)
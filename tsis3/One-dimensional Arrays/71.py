n = int(input())
a = list(map(int, input().split()))
a.insert(0, a.pop())
print(*a)
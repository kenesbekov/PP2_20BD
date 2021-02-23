di = dict()
for i in range(int(input())):
    a, b = input().split(' ')
    di[a]=b
    di[b]=a
print(di[input()])
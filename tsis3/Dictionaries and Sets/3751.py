{print(x, end=' ') for x in sorted(set(map(int, input().split())).intersection(set(map(int, input().split()))))}

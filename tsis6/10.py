my_list = list(map(int, input().split()))

print([x for x in a if x % 2 == 0]) #1st method
print(list(filter(lambda x: x % 2 == 0, my_list))) #2nd method with filter
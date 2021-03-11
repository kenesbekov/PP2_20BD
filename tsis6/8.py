def to_unique(my_list):
    u_list = []
    for elem in my_list:
        if elem not in u_list:
            u_list.append(elem)
    return u_list

my_list = list(input().split())
print(to_unique(my_list))
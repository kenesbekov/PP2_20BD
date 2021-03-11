# def max_of_two(x, y):
#     if x >= y:
#         return x
#     return y

# def max_of_three(x, y, z):
#     return max_of_two(max_of_two(x, y), z)

# a = list(map(int, input().split()))
# print(max_of_three(*a))

a = list(map(int, input().split()))
print(max(a))
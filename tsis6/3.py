# def mult(a):
#     total = 1
#     for x in a:
#         total *= x
#     return toatl

# a = list(map(int, input().split()))
# print(mult(a))

from math import prod
a = list(map(int, input().split()))
print(prod(a))
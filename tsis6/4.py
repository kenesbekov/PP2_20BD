# Solution
# def reverser(s):
#     revs = ''
#     index = len(s)
#     while index > 0:
#         revs += s[index - 1]
#         index -= 1
#     return revs
# print(reverser(input()))

# Simple 
def reverser(s):
    return s[::-1]
print(reverser(input()))
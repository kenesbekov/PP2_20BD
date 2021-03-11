# def is_perfect(num):
#     sum = 0
#     for x in range(1, num+1):
#         if num % x == 0:
#             sum += x
#     if sum // 2 == num:
#         return True
#     return False

# print('Is Perfect' if is_perfect(int(input())) else 'Is not Perfect')


num = int(input())
divisors = [x for x in range(1, num+1) if num % x == 0]
total = sum(divisors)
print('Is Perfect' if total // 2 == num else 'Is not Perfect')

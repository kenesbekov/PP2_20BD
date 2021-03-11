def test_range(num, r1, r2):
    if num in range(r1, r2):
        print('Yes, number %s is in the range'%str(num))
    else:
        print('No, it\'s outside the range')

num, r1, r2 = list(map(int, input().split()))
test_range(num ,r1, r2)


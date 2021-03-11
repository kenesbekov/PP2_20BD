def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for x in range(2, num):
            if num % x == 0:
                return False
        return True

print('Yes your Number is Prime' if is_prime(int(input())) else 'No')

def is_palindrome(s):
    right_pos = len(s) - 1
    left_pos = 0
    while left_pos <= right_pos:
        if not s[left_pos] == s[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

print('Yes' if is_palindrome(input()) else 'No')
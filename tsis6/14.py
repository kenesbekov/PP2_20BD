from string import ascii_lowercase as alphabet
def is_pangram(s):
    s = s.lower()
    for letter in alphabet:
        if letter not in s:
            return False
    return True

print('It is Pangram' if is_pangram(input()) else 'It is not Pangram')

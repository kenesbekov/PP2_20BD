import string
def spec_letters(fname, n):
    alphabet = string.ascii_uppercase
    letters = []
    i = 0
    while i < len(alphabet):
        curr_str = ''
        j = 0
        while j < n and i < len(alphabet):
            curr_str += alphabet[i]
            i += 1
            j += 1
        curr_str += '\n'
        letters.append(curr_str)
    with open(fname, 'w') as f:
        for letters_part in letters:
            f.write(letters_part)
spec_letters('output.txt',int(input()))
def longest_word(fname):
    with open(fname, 'r') as f:
        words = f.read().split()
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))
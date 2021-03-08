def freq_of_word(fname, word):
    with open(fname, 'r') as f:
        words = f.read().split()
        return words.count(word)

print(freq_of_word('test.txt', input()))
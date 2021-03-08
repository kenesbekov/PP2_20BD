def numOfWords(fname):
    with open(fname, 'r') as f:
        words = f.read().replace(',',' ').split()
        return len(words)

print(numOfWords('test.txt'))
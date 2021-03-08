def read_nlines(fname, n):
    with open(fname, 'r') as f:
        for i in range(n):
            txt = f.readline()
            print(txt, end='')

read_nlines('test.txt', int(input()))
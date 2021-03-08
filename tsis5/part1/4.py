def read_last_nlines(fname, n):
    with open(fname, 'r') as f:
        num = len(f.readlines()) # Number of lines in File
        f.seek(0)
        for i in range(num):
            curr_line = f.readline()
            if num-i <= n:
                print(curr_line,end='')

read_last_nlines('test.txt', int(input()))
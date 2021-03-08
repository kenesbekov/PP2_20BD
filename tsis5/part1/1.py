def file_read(fname):
    with open(fname, 'r') as f:
        print(f.read())

file_read('test.txt')
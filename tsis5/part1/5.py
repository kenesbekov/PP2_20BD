def read_lines(fname):
    with open(fname, 'r') as f:
        mylist = f.readlines()
        return mylist

print(read_lines('test.txt'))

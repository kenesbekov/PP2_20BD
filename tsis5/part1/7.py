def read_lines(fname):
    with open(fname, 'r') as f:
        mylist = []
        for line in f:
            mylist.append(line)
        return mylist

print(read_lines('test.txt'))
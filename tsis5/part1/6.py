def read_lines(fname):
    with open(fname, 'r') as f:
        data = f.readlines()
        return data

print(read_lines('test.txt'))
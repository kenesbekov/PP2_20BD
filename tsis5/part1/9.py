def num_of_lines(fname):
    with open(fname, 'r') as f:
        return len(f.readlines()) # Number of lines in File

print(num_of_lines('test.txt'))
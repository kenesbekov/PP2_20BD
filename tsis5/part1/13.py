def copy_file(in_file, out_file):
    with open(in_file, 'r') as rf:
        with open(out_file, 'w') as wf:
            for line in rf:
                wf.write(line)

copy_file('test.txt', 'output.txt')
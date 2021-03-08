def random_line(fname):
    with open(fname, 'r') as f:
        import random
        lines = f.readlines()
        print(random.choice(lines),end='')

random_line('test.txt')
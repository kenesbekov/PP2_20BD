def remover(fname):
    f = open(fname, 'r+')
    lines = [x.rstrip('\n') for x in f.readlines()]
    f.seek(0)
    f.truncate(0)
    f.writelines(lines)

remover('test.txt')


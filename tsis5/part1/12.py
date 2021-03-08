def add_list(fname, mylist):
    with open(fname, 'r+') as f:
        f.read()
        for word in mylist:
            f.write(word+' ')
        f.seek(0)
        print(f.read())

add_list('test.txt', list(input().split()))
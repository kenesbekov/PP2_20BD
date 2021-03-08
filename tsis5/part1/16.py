def isclosed(fname):
    if fname.closed:
        print("It's closed :(")
        return True
    print("It's opened :)")
    return False

f = open('test.txt', 'r')
isclosed(f)
f.close()
isclosed(f)

def add_text(fname, text):
    with open(fname, 'a') as f:
        f.write(text)

add_text('test.txt', input())
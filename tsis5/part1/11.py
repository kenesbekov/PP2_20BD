def file_size(fname):
    import os
    file_stats = os.stat(fname)
    return file_stats.st_size

print(file_size('test.txt'))
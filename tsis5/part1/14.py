def combine_files(ffile, sfile): #first and second files
    with open(ffile, 'r') as rf:
        first = rf.readlines()
        with open(sfile, 'r+') as wf:
            second = wf.readlines()
            for i in range(len(first)):
                curr_line = second[i][:-1]
                second[i] = curr_line + first[i]
            wf.seek(0)
            for line in second:
                wf.write(line)

combine_files('test.txt', 'output.txt')
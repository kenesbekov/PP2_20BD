import glob
char_list = []
files_list = glob.glob('*.txt') #goes through every .txt file
for file_elem in files_list:
    with open(file_elem,'r') as f:
        char_list.append(f.read())
print(char_list)
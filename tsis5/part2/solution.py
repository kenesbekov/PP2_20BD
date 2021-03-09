import os

def select_dir_method(cwd):
    print('You are in Directory in path: ', cwd, 'Select What you want:', '1. Rename Current Directory',
          '2. Print Number of Files', '3. Print Number of Directories', '4. Show Contents', '5. Create File',
          '6. Create Directory', '7. Go up Directory', '8. Go down Directory', '9. Go to File', sep='\n')
    method = int(input('Send: '))
    if method in range(10):
        dir_methods(method, cwd)
    else:
        print('Invalid Number')

def select_file_method(cwd):
    print('You are in File in path: ', cwd, 'Select What you want:', '1. Rename File',
          '2. Delete File', '3. Add Content', '4. Rewrite Content', '5. Return to the Parent Directory', sep='\n')
    method = int(input('Send: '))
    if method in range(6):
        file_methods(method, cwd)
    else:
        print('Invalid Number')

def dir_methods(method, cwd):
        if method == 1:
            curr_name = os.path.basename(cwd)
            new_name = input('Write new name: ')
            os.chdir(os.path.dirname(cwd)) #folder up to rename
            os.rename(curr_name, new_name)
            os.chdir(os.path.join(os.getcwd(), new_name))
        elif method == 2:
            print(len([name for name in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, name))]))
        elif method == 3:
            print(len([name for name in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, name))]))
        elif method == 4:
            print(os.listdir(cwd))
        elif method == 5:
            file_name = input('Write file name with extension: ')
            with open(file_name, 'w+') as f:
                print('File', file_name, 'Created')
        elif method == 6:
            dir_name = input('Write Directory name: ')
            if not os.path.exists(os.path.join(cwd, dir_name)):
                os.makedirs(os.path.join(cwd, dir_name))
                print('Directory', dir_name, 'created!')
            else:
                print('Directory already exists')
        elif method == 7:
            os.chdir(os.path.dirname(cwd))
        elif method == 8:
            print('Choose Directory: ')
            print([name for name in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, name))])
            os.chdir(os.path.join(cwd, input('Send: ')))
        elif method == 9:
            print('Choose File: ')
            print([name for name in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, name))])
            file_name = input('Send: ')
            select_file_method(os.path.join(cwd, file_name))

def file_methods(method, cwd):
    file_name = os.path.basename(cwd)
    if method == 1:
        new_name = input('Write new name: ')
        os.rename(file_name, new_name)
    elif method == 2:
        os.remove(file_name)
        print('File Removed!')
    elif method == 3:
        with open(file_name, 'a') as f:
            text = input('Write adding content: ')
            f.writelines(text)
    elif method == 4:
        with open(file_name, 'w') as f:
            text = input('Write content: ')
            f.writelines(text)
    elif method == 5:
        pass

while True:
    cwd = os.getcwd() #Current Working Directory
    select_dir_method(cwd)


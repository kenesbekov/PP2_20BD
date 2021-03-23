import os

def select_dir_method(cwd):
    print('\nYou are in Directory in path: ', cwd, 'Select What you want:', '1. Rename Current Directory',
          '2. Print Number of Files', '3. Print Number of Directories', '4. Show Contents', '5. Create File',
          '6. Create Directory', '7. Go up Directory', '8. Go down Directory', '9. Go to File', '10. Delete an Object', '0. Exit Program', sep='\n')
    method = int(input('Send: '))
    if method in range(11):
        dir_methods(method, cwd)
    else:
        print('Invalid Number')

def select_file_method(cwd):
    print('\nYou are in File in path: ', cwd, 'Select What you want:', '1. Rename File',
          '2. Delete File', '3. Add Content', '4. Rewrite Content', '5. Return to the Parent Directory', '0. Exit Program', sep='\n')
    method = int(input('Send: '))
    if method in range(6):
        file_methods(method, cwd)
    else:
        print('Invalid Number')

def dir_methods(method, cwd):
        if method == 0:
            exit()
        elif method == 1:
            curr_name = os.path.basename(cwd)
            new_name = input('Write new name\nOr "0" to go back: ')
            if new_name == '0':
                return
            if os.path.exists(os.path.join(os.path.dirname(cwd), new_name)):
                print('Directory', new_name, 'already exists\n')
                return dir_methods(1, cwd)
            os.chdir(os.path.dirname(cwd)) #folder up to rename
            os.rename(curr_name, new_name)
            os.chdir(os.path.join(os.getcwd(), new_name))
        elif method == 2:
            print('Number of files is:', len([name for name in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, name))]))
        elif method == 3:
            print('Number of directories is:', len([name for name in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, name))]))
        elif method == 4:
            if not os.listdir():
                print('No Contents')
            else:
                print('\nContents: ', os.listdir(cwd), sep='\n')
        elif method == 5:
            file_name = input('\nWrite file name with extension\nOr "0" to go back: ')
            if file_name == '0':
                return
            if os.path.exists(os.path.join(cwd, file_name)):
                print('File', file_name, 'already exists')
                return dir_methods(5, cwd)
            else:
                with open(file_name, 'w+') as f:
                    print('File', file_name, 'has been created')
        elif method == 6:
            dir_name = input('\nWrite directory name\nOr "0" to go back: ')
            if dir_name == '0':
                return 
            if os.path.exists(os.path.join(cwd, dir_name)):
                print('Directory', dir_name, 'already exists')
                return dir_methods(6, cwd)
            else:
                os.makedirs(os.path.join(cwd, dir_name))
                print('Directory', dir_name, 'has been created')
        elif method == 7:
            os.chdir(os.path.dirname(cwd))
        elif method == 8:
            list_of_dirs = [name for name in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, name))]
            if not list_of_dirs:
                print('\nNo Directories')
                return
            print('\nDirectories:', list_of_dirs, sep='\n')
            dir_name = input('Write directory name\nOr "0" to go back: ')
            if dir_name == '0':
                return
            if os.path.exists(os.path.join(cwd, dir_name)):
                os.chdir(os.path.join(cwd, dir_name))
            else:
                print('No such directory')
                return dir_methods(8, cwd)
        elif method == 9:
            list_of_files = [name for name in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, name))]
            if not list_of_files:
                print('\nNo Files')
                return
            print('\nFiles:', list_of_files, sep='\n')
            file_name = input('Write file name with extension\nOr "0" to go back: ')
            if file_name == '0':
                return
            if os.path.exists(os.path.join(cwd, file_name)):
                select_file_method(os.path.join(cwd, file_name))
            else:
                print('No such file')
                return dir_methods(9, cwd)
        elif method == 10:
            if not os.listdir():
                print('\nNo objects could be deleted')
                return
            else:
                print('\nObjects: ', os.listdir(cwd), sep='\n')
                obj_name = input('Write object name\nOr "0" to go back: ')
                if obj_name == '0':
                    return
                if os.path.exists(os.path.join(cwd, obj_name)):
                    if os.path.isfile(os.path.join(cwd, obj_name)):
                        os.remove(obj_name)
                        print('\nObject has been deleted')
                    elif os.listdir(os.path.join(cwd, obj_name)):
                        print('\nDangerous!!! - It have contents!') #Shutil can be used, but it is really dangerouns
                        dir_methods(10, cwd)
                    else:
                        os.rmdir(os.path.join(cwd, obj_name))
                        print('\nObject', obj_name, 'has been deleted')
                else:
                    print('No such object')
                    return dir_methods(10, cwd)


def file_methods(method, cwd):
    file_name = os.path.basename(cwd)
    if method == 0:
        exit()
    elif method == 1:
        new_name = input('\nWrite new name with extension\nOr "0" to go back: ')
        if new_name == '0':
            return select_file_method(cwd)
        if os.path.exists(os.path.join(os.path.dirname(cwd), new_name)):
            print('File', new_name, 'already exists')
            return file_methods(1, cwd)
        else:
            os.rename(file_name, new_name)
        return select_file_method(os.path.join(os.path.dirname(cwd), new_name))
    elif method == 2:
        os.remove(file_name)
        print('\nFile', new_name, 'has been removed')
    elif method == 3:
        text = input('\nWrite content\nOr "0" to go back: ')
        if text == '0':
            return select_file_method(cwd)
        with open(file_name, 'a') as f:
            f.writelines(text)
        return select_file_method(cwd)
    elif method == 4:
        text = input('\nWrite content\nOr "0" to go back: ')
        if text == '0':
            return select_file_method(cwd)
        with open(file_name, 'w') as f:
            f.writelines(text)
        return select_file_method(cwd)
    elif method == 5:
        return

while True:
    cwd = os.getcwd() #Current Working Directory
    select_dir_method(cwd)
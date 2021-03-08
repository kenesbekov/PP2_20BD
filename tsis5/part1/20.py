import string, os
if not os.path.exists('letters'):
    os.makedirs('letters')
os.chdir(os.getcwd()+"/letters")
print(os.getcwd())
for letter in string.ascii_uppercase:
    with open(letter + '.txt', 'w') as f:
        f.writelines(letter)

import re
t = int(input())
for i in range(t):
    num = re.search(r"^[+-.\d]\d*[.]{0,1}\d+$", input())
    print('True' if num else 'False')
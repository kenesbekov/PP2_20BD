a,b,c = int(input()),int(input()),int(input())
print(a if a>=b and a>=c else b if b>=a and b>=c else c)
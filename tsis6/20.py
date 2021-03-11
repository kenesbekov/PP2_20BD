def fun():
    a = 1
    b = 45
    some_string = 'Hello'

print(fun.__code__.co_nlocals) #co_nlocals returns the # of local variables
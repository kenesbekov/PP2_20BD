def foo(a):
    def add(b):
        nonlocal a
        a += 1
        def summ():
            return a+b 
        return summ
    return add

func = foo(4)
print(func(4)())
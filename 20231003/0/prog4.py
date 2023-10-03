def func(f, g):
    def h(x):
        return f(x) + g(x)
    return h

def f(x):
    return 2*x

def g(x):
    return x

print(func(f, g)(int(input())))

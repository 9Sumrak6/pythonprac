def f(a, b):
    def g(x):
        return a*x + b
    return g

print(f(1, 2)(5))

from functools import wraps


def genf(f):
    @wraps(f)
    def newfun(*args):
        for i in args:
            if not isinstance(i, int):
                raise TypeError('args must be int')

        return f(*args)
    return newfun

@genf
def fun(a,b):
    """This is mult"""
    return a*2+b
print(fun(2,'3'), fun.__doc__)

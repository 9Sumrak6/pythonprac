def multicall(tp):
    def decorator(fun):
        def newfun(*args):
            for i in args:
                if not isinstance(i, tp):
                    raise TypeError(f'Args must be {tp}')
            return fun(*args)
        return newfun
    return decorator

@multicall(str)
def simplefun(N):
    return N*2+1

print(simplefun(4))

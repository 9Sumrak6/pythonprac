import inspect


class A:
    blabla: int

    def __init__(self, par):
        if isinstance(par, inspect.get_annotations(self.__class__)['blabla']):
            self.blabla = par
        else:
            raise TypeError

c = A((123, ))
print(c.blabla)

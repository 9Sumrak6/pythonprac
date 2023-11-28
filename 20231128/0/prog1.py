
class ctype(type):
ass sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) >= 2:
            raise TypeError(f'Cannot have more than 1 parent')
        for cls in parents:
            if isinstance(cls, final):
                raise TypeError(f"{cls.__name__} is final")
        return super().__new__(metacls, name, parents, namespace)
class E(metaclass=sole): pass
print(1)
class C: pass
print(2)
class A(C, E): pass
print(3)


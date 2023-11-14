class Dsc:
    def __get__(self, obj, cls):
        print(f'Get from {cls}:{obj}')
        return f"{obj._value}"

    def __set__(self, obj, val):
        print("Set in {obj} ro {val}")
        obj._value = val

    def __delete__(self, obj):
        print(f"Del drom {obj}")
        obj._value = None

class C:
    field = Dsc()
    
    def __init__(self, name):
        self.field = name

    def __str__(self):
        return f'{self.field}'

c = C(123)
print(dir(c))
c.field=123

class C:
    def __init__(self, val=None):
        self._val = val

    @property
    def age(self):
        if self._val == 42:
            print('Secret value!')
            return -1
        
        return self._val

    @age.setter
    def age(self, val):
        if val <= 128:
            self._val = val
        else:
            print('Too old!')
            raise ValueError


c = C()
print(c.age)
c.age = 42
print(c.age)
print(type(c.age))
c.age = 129

import string

class Alpha:
    __slots__ = list(string.ascii_lowercase)

    def __init__(self, *args, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

    def __str__(self):
        ans = ''
        j = False

        for i in self.__slots__:
            try:
                tmp = f'{i} : {getattr(self, i)}'
            except Exception:
                continue

            if j:
                ans += ', '
            else:
                j = True
            
            ans += tmp

        return ans

class AlphaQ:
    __possible = list(string.ascii_lowercase)

    def __init__(self, *args, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

    def __setattr__(self, name, value):
        if name not in self.__class__.__possible:
            raise AttributeError

        self.__dict__[name] = value

    def __getattr__(self, name):
        if name not in self.__class__.__possible or name not in self.__dict__:
            raise AttributeError

        return self.__dict__[name]

    def __str__(self):
        ans = ''
        j = False

        for i in __class__.__possible:
            if i not in self.__dict__:
                continue

            if j:
                ans += ', '
            else:
                j = True

            ans += f'{i} : {getattr(self, i)}'

        return ans

import sys
exec(sys.stdin.read())
from collections import UserString


class DivStr(UserString):
    def __init__(self, arg=""):
        super().__init__(arg)

    def __floordiv__(self, other):
        j = 0
        length = len(self) // other

        for i in range(other):
            yield self[j:j+length]
            j += length

    def __mod__(self, other):
        length = len(self) // other
        return self[length*other:]

import sys
exec(sys.stdin.read())
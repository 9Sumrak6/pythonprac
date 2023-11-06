from math import *

def get_line(vert1, vert2):
    if vert1[0] == vert2[0]:
        return [vert1[0]]

    if vert1[1] == vert2[1]:
        k = 0
        b = vert1[1] 
    else:
        k = (vert2[1] - vert1[1]) / (vert2[0] - vert1[0])
        b = vert1[1] - k * vert1[0]

    def line(x):
        return k * x + b

    return line


class Triangle():
    def __init__(self, *args):
        self.vert1 = tuple(args[0])
        self.vert2 = tuple(args[1])
        self.vert3 = tuple(args[2])

    def __bool__(self):
        a = ((self.vert1[0] - self.vert2[0]) ** 2 + (self.vert1[1] - self.vert2[1]) ** 2) ** 0.5
        b = ((self.vert1[0] - self.vert3[0]) ** 2 + (self.vert1[1] - self.vert3[1]) ** 2) ** 0.5
        c = ((self.vert2[0] - self.vert3[0]) ** 2 + (self.vert2[1] - self.vert3[1]) ** 2) ** 0.5

        if a + b <= c or a + c <= b or b + c <= a:
            return False

        if min(a, b, c) <= 0:
            return False

        return True

    def __abs__(self):
        if not bool(self):
            return 0

        a = (self.vert2[0] - self.vert1[0]) * (self.vert3[1] - self.vert1[1])
        b = (self.vert3[0] - self.vert1[0]) * (self.vert2[1] - self.vert1[1])

        return abs(a - b) / 2

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __contains__(self, other):
        if self is other or not bool(other):
            return True
        
        if not bool(self):
            return False

        if abs(other) > abs(self):
            return False

        for x, y in [other.vert1, other.vert2, other.vert3]:
            a = (self.vert1[0] - x)*(self.vert2[1] - y) - (self.vert2[0] - x)*(self.vert1[1] - y)
            b = (self.vert2[0] - x)*(self.vert3[1] - y) - (self.vert3[0] - x)*(self.vert2[1] - y)
            c = (self.vert3[0] - x)*(self.vert1[1] - y) - (self.vert1[0] - x)*(self.vert3[1] - y)

            if not ((a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0 )):
                return False

        return True

    def __and__(self, other):
        if abs(self) == 0 or abs(other) == 0:
            return False

        l1 = [
            (get_line(self.vert1, self.vert2), self.vert1, self.vert2),
            (get_line(self.vert1, self.vert3), self.vert1, self.vert3),
            (get_line(self.vert2, self.vert3), self.vert2, self.vert3)
        ]
        l2 = [
            (get_line(other.vert1, other.vert2), other.vert1, other.vert2),
            (get_line(other.vert1, other.vert3), other.vert1, other.vert3),
            (get_line(other.vert2, other.vert3), other.vert2, other.vert3) 
        ]

        for x in l1:
            for y in l2:
                if type(x[0]) != list and type(y[0]) != list:
                    if (x[0](x[1][0]) - y[0](x[1][0])) * (x[0](x[2][0]) - y[0](x[2][0])) <= 0:
                        k1 = (x[2][1] - x[1][1]) / (x[2][0] - x[1][0])
                        b1 = x[1][1] - k1 * x[1][0]
                        k2 = (y[2][1] - y[1][1]) / (y[2][0] - y[1][0])
                        b2 = y[1][1] - k2 * y[1][0]

                        if isclose(k1, k2):
                            if not isclose(b1, b2):
                                continue
                            if not(min(x[1][0], x[2][0]) > max(y[1][0], y[2][0]) or min(y[1][0], y[2][0]) > max(x[1][0], x[2][0])):
                                return True 
                            continue

                        x_int = (b2 - b1) / (k1 - k2)
                        if min(x[1][0], x[2][0]) <= x_int and max(x[1][0], x[2][0]) >= x_int and min(y[1][0], y[2][0]) <= x_int and max(y[1][0], y[2][0]) >= x_int:
                            return True
                elif type(x[0]) != list:
                    if min(x[1][0], x[2][0]) <= y[1][0] and max(x[1][0], x[2][0]) >= y[1][0] and (max(x[1][1], x[2][1]) <= max(y[1][1], y[2][1]) and max(x[1][1], x[2][1]) >= min(y[1][1], y[2][1]) or min(x[1][1], x[2][1]) >= min(y[1][1], y[2][1]) and min(x[1][1], x[2][1]) <= max(y[1][1], y[2][1])):
                        return True
                elif type(y[0]) != list:
                    if min(x[1][0], x[2][0]) <= y[1][0] and max(x[1][0], x[2][0]) >= y[1][0] and (max(y[1][1], y[2][1]) <= max(x[1][1], x[2][1]) and max(y[1][1], y[2][1]) >= min(x[1][1], x[2][1]) or min(y[1][1], y[2][1]) >= min(x[1][1], x[2][1]) and min(x[1][1], x[2][1]) <= max(y[1][1], y[2][1])):
                        return True
                else:
                    if x[0][0] != y[0][0]:
                        continue
                    if not(min(x[1][1], x[2][1]) > max(y[1][1], y[2][1]) or min(y[1][1], y[2][1]) > max(x[1][1], x[2][1])):
                        return True

        return False

import sys
exec(sys.stdin.read())
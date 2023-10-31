class Rectangle():
    rectcnt = 0
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        

        self.square = abs(self.x1 - self.x2) * abs(self.y1 - self.y2)

        Rectangle.rectcnt += 1

        setattr(self, f"rect_{Rectangle.rectcnt}", Rectangle.rectcnt)

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"
    
    def __mul__(self, other):
        return Rectangle(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other)
    
    def __rmul__(self, other):
        return Rectangle(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other)

    def __lt__(self, other):
        return self.square < other.square
    
    def __eq__(self, other):
        return self.square == other.square
    
    def __getitem__(self, index):
        return [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)][index]
    
    def __bool__(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) != 0

    def __del__(self):
        print(f"Deleting {str(self)}")
        print(self.__class__.rectcnt)
        self.__class__.rectcnt -= 1
        print(self.__class__.rectcnt, ' --_--')

r1, r2, r3, r4 = Rectangle(1, 2, 3, 4), Rectangle(2, 2, 3, 4), Rectangle(0, 2, 3, 4), Rectangle(1, 2, 3, 2)
print(r1 * 3)
print(r3 * 5)
print(r2[3])
print(r2[2])
print(r2[1])
print(r2[0])

for i in r1:
    print(i)

del(r1)
del(r2)
del(r3)
del(r4)

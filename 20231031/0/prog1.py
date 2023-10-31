class Rectangle():
    rectcnt = 0
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        Rectangle.rectcnt += 1

        setattr(self, f"rect_{Rectangle.rectcnt}", Rectangle.rectcnt)

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"
    
r1, r2, r3, r4 = Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4)
print(Rectangle.rectcnt)
print(dir(r1))
print(dir(r2))
print(dir(r3))
print(dir(r4))

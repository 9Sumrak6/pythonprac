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

    def __lt__(self, other):
        return self.square < other.square
    
    def __eq__(self, other):
        return self.square == other.square

r1, r2, r3, r4 = Rectangle(1, 2, 3, 4), Rectangle(2, 2, 3, 4), Rectangle(0, 2, 3, 4), Rectangle(1, 2, 3, 2)
print(r1 < r2)
print(r2 == r2)
print(r3 < r2)
print(r4 < r1)

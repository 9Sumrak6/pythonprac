from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(str(x)) * Type(str(y))
print(multiplier(*eval(input())))

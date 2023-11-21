import pickle

class Sercls:
    lst = []
    dct = dict()
    num = 1
    st = ''
    
    def __init__(self):
        self.lst = [1]
        self.dct = {'a': 2}
        self.num = 2
        self.st = 'Slava Gay'

ser = Sercls()
f = open('cal', 'w')
pickle.dumps(ser, f)
print(s)
f.close()
f = open('cal', 'r')
ser = pickle.load(s, f)
print(ser)
f.close()


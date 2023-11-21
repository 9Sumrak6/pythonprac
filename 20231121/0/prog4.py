import struct
import random

f=open('file', 'wb')

s = "<f3si"

for i in range(10):
    b = random.randrange(255), random.randrange(255), random.randrange(255)
    n = random.randrange(10000)
    f.write(struct.pack(s, random.random(), bytes(b), n))

f.close()

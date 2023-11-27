import sys
import struct

raw = sys.stdin.buffer.read()
l = len(raw)

if l < 44 or raw[:4] != b'RIFF' or raw[8:16] != b'WAVEfmt ' or raw[36:40] != b'data':
    print('NO')
else:
    print(f'Size={int.from_bytes(raw[4:8], 'little')}, Type={int.from_bytes(raw[20:22], 'little')}, Channels={int.from_bytes(raw[22:24], 'little')}, Rate={int.from_bytes(raw[24:28], 'little')}, Bits={int.from_bytes(raw[34:36], 'little')}, Data size={int.from_bytes(raw[40:44], 'little')}')

import sys


head, line = sys.stdin.buffer.read(1), sys.stdin.buffer.readline()
L = len(line)
if line[-1] == 10:
    line = line[:len(line) - 1]
L -= 1

ans = []

N = head[0]

for i in range(N):
    ans.append(line[int(i * L / N): int((i + 1) * L / N)])

out = [head] + sorted(ans) + [b'\n']
for i in out:
    sys.stdout.buffer.write(bytearray(i))

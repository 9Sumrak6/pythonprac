class Maze:
    def __init__(self, n):
        self.n = n
        self.lab = []
        for i in range(2 * n + 1):
            self.lab.append([])

            for j in range(2 * n + 1):
                if i % 2 == 0:
                    self.lab[i].append("\u2588")
                    continue
                if j % 2 == 0:
                    self.lab[i].append("\u2588")
                else:
                    self.lab[i].append("\u00B7")

    def __setitem__(self, attr, val):
        x0, y0, y1 = attr
        y0, x1 = y0.start, y0.stop
        if x0 == x1:
            for i in range(2 * (min(y0, y1) + 1), 2 * (max(y0, y1) + 1), 2):
                self.lab[i][2 * x0 + 1] = val 
        elif y0 == y1:
            for i in range(2 * (min(x0, x1) + 1), 2 * (max(x0, x1) + 1), 2):
                self.lab[2 * y0 + 1][i] = val

    def __getitem__(self, attr):
        x0, y0, y1 = attr
        y0, x1 = y0.start, y0.stop

        not_saw = [(x0, y0)]
        saw = []

        while len(not_saw):
            cur = not_saw.pop()

            if cur == (x1, y1):
                return True

            if cur in saw:
                continue

            saw.append(cur)

            if (cur[0], cur[1] - 1) not in not_saw and self.lab[2 * cur[1]][2 * cur[0] + 1] != '\u2588' and cur[1]:
                not_saw.append((cur[0], cur[1] - 1))
            if (cur[0] + 1, cur[1]) not in not_saw and self.lab[2 * cur[1] + 1][2 * cur[0] + 2] != '\u2588' and cur[0] != self.n - 1:
                not_saw.append((cur[0] + 1, cur[1]))
            if (cur[0], cur[1] + 1) not in not_saw and self.lab[2 * cur[1] + 2][2 * cur[0] + 1] != '\u2588' and cur[1] != self.n - 1:
                not_saw.append((cur[0], cur[1] + 1))
            if (cur[0] - 1, cur[1]) not in not_saw and self.lab[2 * cur[1] + 1][2 * cur[0]] != '\u2588' and cur[0]:
                not_saw.append((cur[0] - 1, cur[1]))

        return False

    def __str__(self):
        ans = ""

        for i in range(len(self.lab)):
            for j in self.lab[i]:
                ans += j
            if i != len(self.lab) - 1:
                ans += '\n'

        return ans

import sys
exec(sys.stdin.read())
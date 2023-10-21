s = input().lower()

pairs = set()

for i in range(0, len(s) - 1):
    if not s[i].isalpha():
        continue

    if s[i + 1].isalpha():
        pairs.add(min(s[i], s[i + 1]) + max(s[i], s[i + 1]))

print(len(pairs))

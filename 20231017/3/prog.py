w = int(input())

words = {}
max_in = 0
while s := input().lower():
    new_s = ''
    for i in s:
        if i.isalpha():
            new_s += i
        else:
            new_s += ' '

    new_s = new_s.split()

    for word in new_s:
        if word != '' and len(word) == w:
            words[word] = words.setdefault(word, 0) + 1

            if words[word] > max_in:
                max_in = words[word]

if not words:
    exit(0)

res = [i for i in words if words[i] == max_in]

print(*sorted(res), sep=' ')
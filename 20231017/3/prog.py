w = int(input())

words = {}
max_in = 0
while s := input():
    i = 0
    while i < len(s):
        word = ''

        while i < len(s) and s[i].isalpha():
            word += s[i]
            i += 1
		
        i += 1

        word = word.lower()

        if word != '' and len(word) == w:
            words[word] = words.setdefault(word, 0) + 1

            if words[word.lower()] > max_in:
                max_in = words[word]

if not words:
    exit(0)

res = [i for i in words if words[i] == max_in]

print(*sorted(res), sep=' ')
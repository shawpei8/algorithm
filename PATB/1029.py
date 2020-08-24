s, t = input(), input()

# 注意 t 后面可能还有未打出来的
t += (len(s) - len(t)) * '_'

a = []
i = j = 0
while i < len(s) and j < len(t):
    if t[j] != s[i]:
        if s[i].upper() not in a:
            a.append(s[i].upper())
    else:
        j = j + 1
    i = i + 1

for i in a:
    print(i, end='')

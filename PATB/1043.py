s = input()
a = {}
d = 'PATest'
for i in range(6):
    a[d[i]] = 0
for i in s:
    if i in d:
        a[i] += 1

b = [0] * 6
for i in range(6):
    b[i] = a[d[i]]

c = sum(b)
while c > 0:
    for i in range(6):
        if b[i] != 0:
            print(d[i], end='')
            b[i] -= 1
            c -= 1
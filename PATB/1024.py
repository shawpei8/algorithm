n = input()

doti = expi = 0
for i in range(len(n)):
    if n[i] == '.': doti = i
    if n[i] == 'E': expi = i

num = (n[1:doti] if n[0] in '+-' else n[:doti]) + n[doti+1:expi]
exp = (doti-1 if n[0] in '+-' else doti) + int(n[expi+1:])

if n[0] == '-':
    print('-', end='')
if exp + doti <= 1:
    print('0.', end='')
e = exp
while e < 0:
    print('0', end='')
    e += 1

k = exp if exp > len(num) else len(num)
for i in range(k):
    if i < len(num):
        if i != k-1:
            print(num[i], end='')
        else:
            print(num[i])
        if i == exp-1:
            print('.', end='')
    if i >= len(num):
        if i != k-1:
            print('0', end='')
        else:
            print('0')

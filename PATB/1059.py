n = int(input())
a = [0] * 10000
for i in range(n):
    a[int(input())] = i + 1

m = int(input())
b = []
for i in range(m):
    b.append(input())

c = [True] * (n + 1)
for i in range(2, int(n**0.5) + 1):
    j = i * i
    while j <= n:
        c[j] = False
        j += i

checked = set()
for i in range(m):
    id = int(b[i])
    if a[id] == 0:
        print('{}: {}'.format(b[i], 'Are you kidding?'))
    elif b[i] in checked:
        print('{}: {}'.format(b[i], 'Checked'))
    elif a[id] == 1:
        print('{}: {}'.format(b[i], 'Mystery Award'))
    elif c[a[id]] is True:
        print('{}: {}'.format(b[i], 'Minion'))
    else:
        print('{}: {}'.format(b[i], 'Chocolate'))
    checked.add(b[i])
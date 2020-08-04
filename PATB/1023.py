a = [int(i) for i in input().split()]

n = ''
for i in range(10):
    n += str(i) * a[i]

n = list(n)
for i in range(len(n)):
    if n[i] != '0':
        n[0], n[i] = n[i], n[0]
        break

print(''.join(n))

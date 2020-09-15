n, k = [int(i) for i in input().split()]

p = []
for i in range(n):
    p.append(input().split())
p.sort(key=lambda x: x[0], reverse=True)
p.sort(key=lambda x: int(x[1]))

q, r = divmod(n, k)
for i in range(k):
    m = q + r if i == 0 else q
    a = [''] * m
    L = R = m // 2
    for j in range(m):
        if j % 2 == 1:
            L -= 1
            a[L] = p.pop()[0]
        else:
            a[R] = p.pop()[0]
            R += 1
    print(' '.join(a))
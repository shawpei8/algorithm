a, b = input().split()
g1, s1, k1 = [int(i) for i in a.split('.')]
g2, s2, k2 = [int(i) for i in b.split('.')]

m1 = g1 * 17 * 29 + s1 * 29 + k1
m2 = g2 * 17 * 29 + s2 * 29 + k2

r = m2 - m1
sign = '-' if r < 0 else ''
r = abs(r)
c = [0] * 3
c[0] = r // (17 * 29)
c[1] = (r - c[0] * 17 * 29) // 29
c[2] = r % 29

print(sign + '.'.join([str(i) for i in c]))
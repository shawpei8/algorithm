def gcd(a, b):
    return a if not b else gcd(b, a % b)

a = input().split()
x = eval(a[0])
y = eval(a[1])

if x > y:
    x, y = y, x

k = 1
r = []
m = int(a[2])
while k / m < y:
    if k / m > x and gcd(k, m) == 1:
        r.append(str(k) + '/' + str(m))
    k += 1

print(' '.join(r))
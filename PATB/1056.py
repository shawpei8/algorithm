a = list(map(int, input().split()))

s = 0
n = len(a) - 2
suma = sum(a) - a[0]
for i in range(1, a[0] + 1):
    s += (a[i] * (10 * n - 1) + suma)

print(s)
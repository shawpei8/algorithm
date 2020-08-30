n = int(input())
a = list(map(int, input().split()))

b = sorted(a)
cnt = 0
m, mi = a[0], 0
c = []
for i in range(n):
    if a[i] > m:
        m, mi = a[i], i
    if a[i] == b[i] and i == mi:
        cnt += 1
        c.append(b[i])
print(cnt)
print(' '.join([str(i) for i in c]))
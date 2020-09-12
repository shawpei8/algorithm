n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

ca = cb = 0
for i in range(n):
    t = a[i][0] + a[i][2]
    if t == a[i][1] and t == a[i][3]:
        continue
    if t == a[i][1]: cb += 1
    if t == a[i][3]: ca += 1

print(ca, cb)
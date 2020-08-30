n = int(input())
a, b = [], []
for i in range(n):
    a.append(input())
    b.append(a[i].split()[1])
m = int(input())
c = input().split()

for i in range(m):
    j = b.index(c[i])
    d = a[j].split()
    print(d[0], d[2])
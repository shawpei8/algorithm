polys = [int(i) for i in input().split()]

r = []
for i in range(0, len(polys)-1, 2):
    if polys[i] * polys[i+1]:
        r.append(polys[i] * polys[i+1])
    if polys[i+1] - 1 >= 0:
        r.append(polys[i+1] - 1)

if len(r) == 0: r = [0, 0]
for i in range(len(r)-1):
    print(r[i], end=' ')
print(r[-1])
n, e, d = list(map(float, input().split()))

c1 = c2 = 0
for i in range(int(n)):
    a = list(map(float, input().split()))
    days = sum([1 for j in a[1:] if j < e])
    if days > int(a[0]) // 2:
        if int(a[0]) > d:
            c2 += 1
        else:
            c1 += 1

print('{:.1f}% {:.1f}%'.format(c1*100/n, c2*100/n))
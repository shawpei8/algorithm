n = int(input())

m = 0
for i in range(n):
    a, b = [int(i) for i in input().split()]
    t = (a*a + b*b)**0.5
    if m < t:
        m = t

print('{:.2f}'.format(m))
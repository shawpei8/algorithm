import math

# 对于像-0.001i这样的数，应该输出+0.00i才合理而不是-0.00i
a = list(map(float, input().split()))
r1, p1, r2, p2 = a

A = r1 * r2 * math.cos(p1 + p2)
B = r1 * r2 * math.sin(p1 + p2)
A, B = round(A, 2), round(B, 2)
if A == 0: A = 0
if B == 0: B = 0

print('{:.2f}{:+.2f}i'.format(A, B))
#if B >= 0:
#    print('%.2f+%.2fi' % (A, B))
#else:
#    print('%.2f-%.2fi' % (A, -B))
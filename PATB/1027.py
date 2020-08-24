import math

n, c = input().split()
m = int(n)
n = int(math.sqrt((int(n)+1)/2))
r = m - (2*n*n - 1)

for i in range(n):
    print(i*' ' + (2*(n-i)-1)*c)

for i in range(1, n):
    print((n-i-1)*' ' + (2*i+1)*c)

print(r)

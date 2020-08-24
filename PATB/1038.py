n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * 101
for i in range(n):
    c[a[i]] += 1

for i in range(1, len(b) - 1):
    print(c[b[i]], end=' ')
print(c[b[len(b) - 1]])
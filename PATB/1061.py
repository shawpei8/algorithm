n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = input().split()

for i in range(n):
    t = input().split()
    print(sum([a[j] for j in range(m) if b[j] == t[j]]))
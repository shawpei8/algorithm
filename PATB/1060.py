n = int(input())
a = list(map(int, input().split()))

a.sort()
k = 0 # 当if判断全部失败时，应输出0
for i in range(n):
    if a[i] > n - i:
        k = n - i
        break
print(k)
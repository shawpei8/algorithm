n, p = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
i, j = 0, 1
count = 1
while j < n:
    if a[j] <= a[i] * p:
        count += 1
    else:
        i = i + 1
    j = j + 1

print(count)
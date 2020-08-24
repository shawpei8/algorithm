a, b = input().split()
n = int(a)

print(n * b)
for i in range((n + 1) // 2 - 2):
    print(b + (n-2)*' ' + b)
print(n * b)
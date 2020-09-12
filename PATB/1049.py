from decimal import Decimal # float精度不够会导致测试点2失败

n = int(input())
a = list(map(Decimal, input().split()))

r = 0
for i in range(n):
    r += (i + 1) * (n - i) * a[i]

print(r.quantize(Decimal('0.00')))
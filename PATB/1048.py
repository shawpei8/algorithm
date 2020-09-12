a, b = input().split()
nums = '0123456789JQK'

a, b = a[::-1], b[::-1]
lena, lenb = len(a), len(b)
if lena < lenb:
    a += '0' * (lenb - lena)
else:
    b += '0' * (lena - lenb)

s = ''
for i in range(len(a)):
    n = 0
    if i % 2 == 1:
        n = int(b[i]) - int(a[i])
        n = n + 10 if n < 0 else n
    else:
        n = (int(a[i]) + int(b[i])) % 13
    s += nums[n]
print(s[::-1])
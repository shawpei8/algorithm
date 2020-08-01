a, b = input().split()

q = ''
r = 0
intb = int(b)
for i in range(len(a)):
    t = r*10 + int(a[i])
    q += str(t // intb)
    r = t % intb

# 注意商为0的情况，比如 1/2
if len(q) > 1: q = q.lstrip('0')
print(q, r)

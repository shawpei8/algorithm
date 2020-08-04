c1, c2 = map(int, input().split())

d = c2 - c1
# 四舍五入
if d % 100 >= 50:
    d = int(d / 100) + 1
else:
    d = int(d / 100)

print('%02d:%02d:%02d' % (d // 3600, d % 3600 // 60, d % 60))
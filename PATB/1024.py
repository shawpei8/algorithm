a = input().split('E')
sign = a[0][0]  # 符号
s = a[0][1] + a[0][3:]  # 数字
e = a[1]  # 指数

x = int(e) + 1
if x <= 0:
    s = '0' + '.' + '0' * (-x) + s
elif x >= len(s):
    s = s + '0' * (x - len(s))
else:
    s = s[0:x] + '.' + s[x:]

if sign == '-':
    s = '-' + s
print(s)
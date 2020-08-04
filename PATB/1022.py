a, b, d = map(int, input().split())

c = a + b
r = '0' if c == 0 else '' # 注意 c == 0 的特殊情况

while c:
    r = str(c % d) + r
    c = c // d

print(r)

e = [[] for i in range(3)]
for i in range(3):
    s = input().split('[') # 非零返回, 可能是PAT的python解释器无法正常读入非ASCII字符
    for c in s:
        if ']' in c:
            e[i].append(c[:c.index(']')])

L1, L2, L3 = len(e[0]), len(e[1]), len(e[2])
n = int(input())
for i in range(n):
    lst = [int(k) - 1 for k in input().split()]
    if lst[0] >= L1 or lst[1] >= L2 or lst[2] >= L3 or lst[3] >= L2 or lst[4] >= L1:
        print(r'Are you kidding me? @\/@')
        continue
    print(e[0][lst[0]], '(', e[1][lst[1]], e[2][lst[2]], e[1][lst[3]], ')', e[0][lst[4]], sep='')
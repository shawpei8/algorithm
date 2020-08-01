n = input().rjust(4, '0')

if len(set(n)) == 1:
    print(n, '-', n, '= 0000')
else:
    while True:
        a = ''.join(sorted(n, reverse=True))
        b = ''.join(sorted(n))
        n = str(int(a) - int(b)).rjust(4, '0')
        print(a, '-', b, '=', n)
        if n == '6174': break # 注意输入是6174时
a = ["tret", "jan", "feb", "mar", "apr", "may", \
    "jun", "jly", "aug", "sep", "oct", "nov", "dec"]
b = ["0", "tam", "hel", "maa", "huh", "tou", "kes", \
    "hei", "elo", "syy", "lok", "mer", "jou"]

n = int(input())

for i in range(n):
    s = input()
    if s.isdigit():
        q, r = divmod(int(s), 13)
        if q == 0:
            print(a[r])
        else:
            if r == 0:
                print(b[q])
            else:
                print(b[q], a[r])
    else:
        h = l = 0
        if len(s) < 5:
            if s in a:
                 l = a.index(s)
            else:
                 h = b.index(s)
        else:
            hs, ls = s.split()
            h, l = b.index(hs), a.index(ls)
        print(h * 13 + l)

pat = input()

cnt = pn = 0
tn = pat.count('T')
for i in range(len(pat)):
    if pat[i] == 'P': pn += 1
    elif pat[i] == 'T': tn -= 1
    else: cnt += tn * pn

print(cnt % 1000000007)
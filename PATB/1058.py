sn, qn = list(map(int, input().split()))
a, b = [], []
for i in range(qn):
    b.append(input())
for i in range(sn):
    a.append(input()[1:-1].split(') ('))
    #a.append((') ' + input() + ' (').split(') ('))

qst = [0] * qn
for i in range(sn):
    score = 0
    for j in range(qn):
        if b[j][6:] == a[i][j][2:]:
            score += int(b[j][0])
        else:
            qst[j] += 1
    print(score)

mc = max(qst)
if mc == 0:
    print('Too simple')
else:
    L = [mc] + [i+1 for i in range(qn) if qst[i] == mc]
    print(' '.join(list(map(str, L))))
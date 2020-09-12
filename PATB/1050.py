n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
lena = len(a)
i = j = 0
for k in range(int(lena ** 0.5), 0, -1):
    if lena % k == 0:
        j, i = k, lena // k
        break

marks = [[0] * j for k in range(i)]
Mat = [[0] * j for k in range(i)]
steps = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 顺时针

m = 0
step = [0, 0]
for k in range(lena):
    b, c = step[0] + steps[m][0], step[1] + steps[m][1]
    if b >= i or c >= j or marks[b][c] == 1:
        m = (m + 1) % 4
    Mat[step[0]][step[1]] = a[k]
    marks[step[0]][step[1]] = 1
    step[0] += steps[m][0]
    step[1] += steps[m][1]

for k in range(i):
    print(' '.join([str(c) for c in Mat[k]]))
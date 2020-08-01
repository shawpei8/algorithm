n = int(input())

ties = 0
awin = [0] * 3
bwin = [0] * 3

for i in range(n):
    a, b = input().split()
    if a == 'C' and b == 'J':
        awin[0] += 1
    elif a == 'J' and b == 'B':
        awin[1] += 1
    elif a == 'B' and b == 'C':
        awin[2] += 1
    elif b == 'C' and a == 'J':
        bwin[0] += 1
    elif b == 'J' and a == 'B':
        bwin[1] += 1
    elif b == 'B' and a == 'C':
        bwin[2] += 1
    else:
        ties += 1

def gesture(wins):
    maxw = max(wins)
    if maxw == wins[2]: return 'B'
    if maxw == wins[0]: return 'C'
    if maxw == wins[1]: return 'J'

awins = sum(awin)
bwins = sum(bwin)
print(awins, ties, bwins)
print(bwins, ties, awins)
print(gesture(awin), gesture(bwin))

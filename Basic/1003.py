def isAllPAT(s):
    for i in s:
        if i not in 'PAT':
            return False
    return True

def isValid(s):
    if len(s) < 3: return False
    if not isAllPAT(s): return False
    i, j = s.find('P'), s.find('T')
    if i * (j - i - 1) != len(s) - j - 1:
        return False
    return True

n = int(input())
for i in range(n):
    if isValid(input()):
        print('YES')
    else:
        print('NO')
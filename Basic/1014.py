weeks = {'A': 'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI', 'F': 'SAT', 'G': 'SUN'}

strs = []
for i in range(4):
    strs.append(input())

n1 = n2 = 0
if len(strs[0]) < len(strs[1]):
    n1 = len(strs[0])
else:
    n1 = len(strs[1])
if len(strs[2]) < len(strs[3]):
    n2 = len(strs[2])
else:
    n2 = len(strs[3])

count = 0
for i in range(n1):
    if count == 0 and strs[0][i] == strs[1][i] and ord('A') <= ord(strs[0][i]) <= ord('G'):
        print(weeks[strs[0][i]], end=' ')
        count += 1
        continue
    if count == 1 and strs[0][i] == strs[1][i] and \
       (strs[0][i].isdigit() or ord('A') <= ord(strs[0][i]) <= ord('N')):
        if strs[0][i].isdigit():
            print('0' + strs[0][i], end=':')
        else:
            print(ord(strs[0][i])-ord('A')+10, end=':')
        break
for i in range(n2):
    if strs[2][i] == strs[3][i] and strs[2][i].isalpha():
        if i < 10:
            print('0' + str(i))
        else:
            print(i)
        break

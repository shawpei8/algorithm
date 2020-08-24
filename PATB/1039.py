s1 = input()
s2 = input()
l2 = list(s1)

count = 0
for i in range(len(s2)):
    if s2[i] not in l2:
        count += 1
    else:
        l2.remove(s2[i])

if count == 0:
    print('Yes', len(s1) - len(s2))
else:
    print('No', count)
n = input()

a = [0] * 10

for i in n:
    a[ord(i)-ord('0')] += 1

for i in range(10):
    if a[i] != 0:
        print(i, ':', a[i], sep='')

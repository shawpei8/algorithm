checkCode = '10X98765432'
val = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]

def isValidID(num):
    if num[:-1].isdigit():
        Z = sum([int(num[i])*val[i] for i in range(17)]) % 11
        return num[-1] == checkCode[Z] 
    return False

n = int(input())
flag = True
for i in range(n):
    a = input()
    if not isValidID(a):
        print(a)
        flag = False
if flag:
    print('All passed')
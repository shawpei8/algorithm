n = input()

strn = '123456789'

if len(n) == 3:
    print('B'*int(n[0]) + 'S'*int(n[1]) + strn[:int(n[2])])
elif len(n) == 2:
    print('S'*int(n[0]) + strn[:int(n[1])])
else:
    print(strn[:int(n[0])])
n = int(input())
num = input().split()

b = []
for i in num:
    try:
        float(i)
        if '.' in i:
            s = i.split('.')
            if len(s[-1]) > 2:
                raise Exception
        if not -1000 <= float(i) <= 1000:
            raise Exception
        b.append(float(i))
    except:
        print('ERROR: {} is not a legal number'.format(i))

if len(b) == 0:
    print('The average of 0 numbers is Undefined')
elif len(b) == 1:
    print('The average of 1 number is {:.2f}'.format(b[0]))
else:
    print('The average of {} numbers is {:.2f}'.format(len(b), sum(b)/len(b)))
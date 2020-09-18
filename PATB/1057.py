a = input()

b = '0abcdefghijklmnopqrstuvwxyz'
s = sum([b.index(c.lower()) for c in a if c.isalpha()])
bins = bin(s)

if s == 0:
    print(0, 0)
else:
    print('{} {}'.format(bins.count('0') - 1, bins.count('1')))
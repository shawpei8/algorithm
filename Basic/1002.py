num = input()

pinyin = {'0':'ling','1':'yi','2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu'}
n = str(sum([int(i) for i in num]))

k = len(n) - 1
for i in range(k):
    print(pinyin[n[i]], end=' ')
print(pinyin[n[k]])

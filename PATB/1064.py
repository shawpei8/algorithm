n = int(input())
a = input().split()

b = set()
for i in a:
    b.add(sum([int(k) for k in i]))

c = sorted(list(b))
print(len(c))
print(' '.join([str(i) for i in c]))
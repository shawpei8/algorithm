n = int(input())
a = []
for i in range(n):
    a.append(input().split())

m = input()
b = set(input().split())

for k in a:
    if k[0] in b and k[1] in b:
        b.remove(k[0])
        b.remove(k[1])

b = sorted(list(b))
print(len(b))
if b:
    print(' '.join(b))
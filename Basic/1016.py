a, da, b, db = [i for i in input().split()]

pa = pb = ''
for i in a:
    if i == da: pa += i
for j in b:
    if j == db: pb += j
pa = 0 if not pa else int(pa)
pb = 0 if not pb else int(pb)
print(pa + pb)
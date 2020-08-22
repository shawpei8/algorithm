n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def lprint(L):
    print(' '.join([str(i) for i in L]))

def is_insertion():
    for i in range(2, n):
        if sorted(a[:i]) + a[i:] == b:
            return sorted(a[:i+1]) + a[i+1:]

def is_merge():
    k = 1
    flag = False
    while True:
        k = 2 * k
        c = []
        for i in range(0, n, k):
            c += sorted(a[i : i + k])
        if flag:
            return c
        if b == c:
            flag = True

answer = is_insertion()
if answer:
    print('Insertion Sort')
    lprint(answer)
else:
    print('Merge Sort')
    lprint(is_merge())
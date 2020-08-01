m, n = [int(i) for i in input().split()]

N = 110000 # N 为啥是这个数呢？试出来的，不超时就行
primes = [True] * (N + 1)

i = 2
while i*i <= N:
    j = i*i
    while j <= N:
        primes[j] = False
        j += i
    i = i + 1

count = 0
count1 = 0
for i in range(2, N+1):
    if primes[i]:
        count += 1
        if m <= count <= n:
            count1 += 1
            if count1 % 10 == 0 or count == n:
                print(i)
                if count == n: break
            else:
                print(i, end=' ')
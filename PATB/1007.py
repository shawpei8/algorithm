# answer 1
"""
def isPrime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

n = int(input())

count = 0
marks = [False] * (n + 1)
for i in range(n+1):
    if isPrime(i):
        marks[i] = True
        if i-2 >= 0 and marks[i-2]:
            count += 1

print(count)
"""

# answer 2
n = int(input())
primes = [True] * (n + 1)

i = 2
while i*i <= n:
    j = i*i
    while j <= n:
        primes[j] = False
        j += i
    i = i + 1
        
count = 0
for i in range(2, n-1):
    if primes[i] and primes[i+2]:
        count += 1

print(count)

















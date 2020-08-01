n = int(input())

marks = [True] * n
nums = [int(i) for i in input().split()]

def check(k):
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = (3*k + 1) // 2
        if k in nums:
            marks[nums.index(k)] = False

for i in nums:
    check(i)

a = [nums[i] for i in range(n) if marks[i]]

a.sort(reverse=True)
for i in range(len(a)-1):
    print(a[i], end=' ')
print(a[len(a)-1])
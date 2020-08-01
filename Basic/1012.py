nums = [int(i) for i in input().split()]

sign = 1
count = 0
a1 = a2 = a3 = a4 = a5 = 0
for i in range(1, nums[0]+1):
    if not nums[i] % 10:
        a1 += nums[i]
    if nums[i] % 5 == 1:
        a2 += sign*nums[i]
        sign *= -1
    if nums[i] % 5 == 2:
        a3 += 1
    if nums[i] % 5 == 3:
        a4 += nums[i]
        count += 1
    if nums[i] % 5 == 4:
        if nums[i] > a5:
            a5 = nums[i]
if count != 0:
    a4 /= count
if a1 != 0: print(a1, end=' ')
else: print('N', end=' ')
if a2 != 0: print(a2, end=' ')
else: print('N', end=' ')
if a3 != 0: print(a3, end=' ')
if a4 != 0: print('%.1f' % a4, end=' ')
else: print('N', end=' ')
if a5 != 0: print(a5)
else: print('N')
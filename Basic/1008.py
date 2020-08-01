n, k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

# answer 1
# k = k % n
# nums = nums[n-k:] + nums[:n-k]

# answer 2
def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i + 1, j - 1
k = k % n
reverse(nums, 0, n-1)
reverse(nums, 0, k-1)
reverse(nums, k, n-1)

for i in range(n-1):
    print(nums[i], end=' ')
#print(nums[n-1])
print(nums[-1])
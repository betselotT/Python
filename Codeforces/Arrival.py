def arrival(nums):
    count = 0
    for i in range(n):
        if nums[i] != max(nums[:i + 1]):
            count += 1
    for i in range(n):
        if nums[i] != min(nums[:i + 1]):
            count += 1

    return count

n = int(input())
nums = list(map(int,input().split()))
result = arrival(nums)
print(result)
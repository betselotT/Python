def years(nums):
    count = 0
    while nums[0] <= nums[1]:
        nums[0] *= 3
        nums[1] *= 2
        count += 1
    return count

nums = list(map(int,input().split()))
print(years(nums))
def borrow(nums):
    sum = 0
    i = 1
    while i <= nums[2]:
        added = nums[0] * i
        sum += added
        i += 1
    if sum > nums[1]:
        diff = sum - nums[1]
        return abs(diff)
    else:
        return 0


nums = list(map(int, input().split()))
print(borrow(nums))
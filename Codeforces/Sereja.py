def count(nums):
    left = 0
    right = len(nums) - 1
    sereja = 0
    dima = 0
    while left <= right:
        if nums[right] > nums[left]:
            sereja += nums[right]
            right -= 1
        else:
            sereja += nums[left]
            left += 1
        if left <= right:
            if nums[right] > nums[left]:
                dima += nums[right]
                right -= 1
            else:
                dima += nums[left]
                left += 1
    print(sereja, dima)

n = int(input())
nums = list(map(int, input().split()))
count(nums)

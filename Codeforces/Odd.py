def oddOne(nums):
    if nums[0] == nums[1]:
        print(nums[2])
    elif nums[1] == nums[2]:
        print(nums[0])
    elif nums[0] == nums[2]:
        print(nums[1])

n = int(input())
while n:
    nums = list(map(int,input().split()))
    oddOne(nums)
    n-=1
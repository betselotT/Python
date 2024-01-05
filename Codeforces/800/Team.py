count = 0
def team(nums):
    if sum(nums) > 1:
        return 1
    else:
        return 0


n = int(input())
while n:
    nums = list(map(int,input().split()))
    n-=1
    count += team(nums)
print(count)
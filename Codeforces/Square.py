import math
def square(count, nums):
    number = sum(nums)
    if math.sqrt(number) == int(math.sqrt(number)):
        print("YES")
    else:
        print("NO")

n = int(input())
while n:
    count = int(input())
    nums = list(map(int,input().split()))
    square(count, nums)
    n-=1
def sale(m, nums):
    nums.sort()
    ans = sum(abs(num) for num in nums[:m])
    print(ans)

n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))
sale(m, nums)

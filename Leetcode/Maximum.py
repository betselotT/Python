class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        num = sorted(nums)
        print(num)
        high = num[-1]
        shigh = num[-2]
        low = num[0]
        slow = num[1]
        print(high)
        print(shigh)
        highest = high * shigh
        lowest = low * slow
        return highest - lowest
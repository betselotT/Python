class Solution:
    def sumCounts(self, nums):
        count = 0
        n = len(nums)
        for i in range(n):
            distinct = {}
            for j in range(i, n):
                distinct[nums[j]] = distinct.get(nums[j], 0) + 1
                count += len(distinct) ** 2
        return count

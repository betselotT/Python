class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count
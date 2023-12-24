class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1):
                num = nums[i] - nums[j]
                if abs(num) == k:
                    count += 1
        return count

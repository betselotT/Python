
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List = []
        for i in range(len(nums)):
            second = target - nums[i]
            if second in nums[i+1:]:
                return [i, nums[i+1:].index(second) + i + 1]
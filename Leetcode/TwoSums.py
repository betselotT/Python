
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List = {}
        for i, n in enumerate(nums):
            second = target - n
            if second in List:
                return [List[second], i]
            List[n] = i
        return
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            temp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = temp
        arr = list(nums)
        return arr
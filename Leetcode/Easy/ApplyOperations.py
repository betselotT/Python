class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0
                left += 1
                right += 1
            else:
                left += 1
                right += 1
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
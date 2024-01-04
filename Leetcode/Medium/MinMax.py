class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        arr = []
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            sums = nums[left] + nums[right]
            arr.append(sums)
            left += 1
            right -= 1
        return max(arr)
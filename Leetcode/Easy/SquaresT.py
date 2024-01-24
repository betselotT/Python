class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right, index = 0, n - 1, n - 1

        while left <= right:
            squaredL = nums[left] ** 2
            squaredR = nums[right] ** 2

            if squaredL >= squaredR:
                result[index] = squaredL
                left += 1
            else:
                result[index] = squaredR
                right -= 1

            index -= 1

        return result
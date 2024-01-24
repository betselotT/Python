class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNum = sorted(nums)
        left = 0
        right = len(nums) - 1
        result = []

        while left < right:
            current_sum = sortedNum[left] + sortedNum[right]

            if current_sum == target:
                result.append(nums.index(sortedNum[left]))
                nums[nums.index(sortedNum[left])] = float('inf')
                result.append(nums.index(sortedNum[right]))
                return result
            elif current_sum > target:
                right -= 1
            else:
                left += 1

        return result
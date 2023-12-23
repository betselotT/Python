class Solution:
    def absolute_difference(self, a, b):
        return abs(a - b)

    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)

        digit_sum = 0
        for num in nums:
            num_str = str(num)
            for i in num_str:
                digit_sum += int(i)

        if element_sum > digit_sum:
            abs_diff = element_sum - digit_sum
        else:
            abs_diff = digit_sum - element_sum
        return abs_diff

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        maximum = 0

        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    maximum = max(maximum, nums[i] ^ nums[j])

        return maximum


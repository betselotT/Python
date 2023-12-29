class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in range(len(nums)):
            num = bin(i)[2:]
            count = num.count("1")
            if count == k:
                sum += nums[i]
        return sum
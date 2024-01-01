class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i < j and j < k:
                        if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                            answer.append((nums[i], nums[j], nums[k]))
        return len(answer)
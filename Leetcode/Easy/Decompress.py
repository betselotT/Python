class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            value = nums[i + 1]
            for _ in range(freq):
                answer.append(value)
        return answer

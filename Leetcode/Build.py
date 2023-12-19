class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            a = nums[i]
            b = nums[a]
            ans.append(b)
        return ans
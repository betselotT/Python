class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pnums = []
        nnums = []
        arr = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pnums.append(nums[i])
            else:
                nnums.append(nums[i])
        for i in range(len(pnums)):
                arr.append(pnums[i])
                arr.append(nnums[i])
        return arr

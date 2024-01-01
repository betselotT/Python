class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = []
        y = []
        arr = []
        for i in range(len(nums)):
            if i < n:
                x.append(nums[i])
            elif i >= n:
                y.append(nums[i])
        for i in range(len(x)):
            arr.append(x[i])
            arr.append(y[i])
        return arr

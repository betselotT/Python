class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        numCount = {}
        l = 0
        final = []
        isTrue = True
        for num in nums:
            if num not in numCount:
                numCount[num] = nums.count(num)
        while isTrue:
            isTrue = False
            indArray = []
            for num in nums:
                if numCount[num] > l and num not in indArray:
                    indArray.append(num)
                    isTrue = True
            final.append(indArray)
            l+=1
        return final[:-1]